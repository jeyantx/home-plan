// Procedural neem tree (Azadirachta indica) — the existing tree on the plot, built from the site photos.
//
//   import { createNeemTree } from './models/neem-tree.js';
//   const neem = createNeemTree(THREE, { seed: 1, cut: true });
//
// Units: metres, +Y up. Origin = centre of the trunk at ground level.
// Host directions: south = +Z, east = +X, north (road) = -Z, west = -X.
//
// Options:
//   seed  (number, default 1)    deterministic randomness (seeded PRNG, never Math.random)
//   cut   (bool,  default true)  true  = after the planned cut: a short sawn stub of the south limb
//                                false = the south limb kept, ~7 m long, nearly horizontal, with a
//                                        flat skirt of foliage over the plot at ~4–6 m
//   flush (bool,  default false) tint ~15% of the leaf clusters reddish-brown (new flush, as in May)
//
// Form (from the photos): trunk 0.46 m across at chest height, bowing toward the south and a little
// east to a fork at (0.3 E, 3.0 up, 2.0 S). There it splits into a near-vertical leader and a big,
// nearly horizontal south limb. The leader splits again above ~4.5 m into 5–6 crooked main limbs
// carrying a wide, rounded, gappy umbrella crown, ~11.5–12 m tall, ~11 m E–W x ~10 m N–S, overhanging
// the road by ~3.5 m.
//
// Meshes (all plain Mesh + merged BufferGeometry, no InstancedMesh, so the path tracer can use them):
//   NeemTrunk     trunk, leader (and the uncut south limb) — orange-brown fissured bark
//   NeemBranches  main limbs, branches and twigs — darker grey-brown bark
//   NeemLeaves    crossed, drooping leaf-spray cards (alpha-tested compound-leaf atlas)
//   NeemStub      bark of the sawn stub            (cut = true only)
//   NeemStubCut   fresh-wood cut face with rings   (cut = true only)
// No per-frame work. Textures are canvases generated once per tree.

export function createNeemTree(THREE, opts = {}) {
  const seed = Number.isFinite(opts.seed) ? opts.seed : 1;
  const cut = opts.cut !== false;
  const flush = opts.flush === true;
  const rngMain = mulberry32(mix(seed, 1));
  const rngSouth = mulberry32(mix(seed, 2));
  const rngTex = mulberry32(mix(seed, 3));
  let rnd = rngMain;
  const R = (a, b) => a + (b - a) * rnd();
  const TIP = 'Neem tree · existing · trunk 1\'6" · south branch to be cut';
  const TIP_STUB = 'Neem tree · sawn stub of the south branch';

  const V3 = THREE.Vector3;
  const UP = new V3(0, 1, 0);
  const smooth = (a, b, x) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };

  const group = new THREE.Group();
  group.name = 'NeemTree';
  const tag = (mesh, name, tip) => {
    mesh.name = name; mesh.userData.tip = tip;
    mesh.castShadow = true; mesh.receiveShadow = true;
    group.add(mesh); return mesh;
  };

  // ------------------------------------------------------------------ crown envelope
  // Dome on top, flatter (cubic) underside, low-frequency wobble for an irregular outline.
  const ph = [0, 1, 2, 3, 4, 5].map(() => R(0, Math.PI * 2));
  const C1 = new V3(0.3, 6.4, 0.5);
  const C2 = new V3(0.45, 5.0, 7.0); // extra lobe carried by the south limb when it is kept
  function shape(p, c, rx, ryu, ryd, rz, wob) {
    const dx = (p.x - c.x) / rx, dz = (p.z - c.z) / rz, dy = p.y - c.y;
    const h = Math.sqrt(dx * dx + dz * dz);
    let e;
    if (dy >= 0) { const v = dy / ryu; e = Math.sqrt(h * h + v * v); }
    else { const v = -dy / ryd; e = Math.pow(h * h * h * h + v * v * v * v, 0.25); } // flatter underside
    const az = Math.atan2(dz, dx), el = Math.atan2(dy / ryu, h + 1e-6);
    const w = 1 + wob * (0.6 * Math.sin(3 * az + ph[0]) * Math.cos(2 * el + ph[1])
      + 0.4 * Math.sin(5 * az + 2 * el + ph[2]) + 0.25 * Math.sin(8 * az - el + ph[3]));
    return e / w;
  }
  const envMain = (p) => shape(p, C1, 5.6, 5.05, 2.8, 4.45, 0.12);
  const envSouth = (p) => shape(p, C2, 3.4, 1.9, 1.4, 3.6, 0.1);
  const envBoth = (p) => Math.min(envMain(p), envSouth(p));
  let env = envMain;

  function outward(p) {
    const c = env !== envMain && envSouth(p) < envMain(p) ? C2 : C1;
    const o = new V3((p.x - c.x) / 5.4, ((p.y - c.y) / 4) * 0.6, (p.z - c.z) / 5);
    if (o.lengthSq() < 1e-6) o.set(1, 0, 0);
    return o.normalize();
  }
  const tmpQ = new V3();
  function room(p, d, max) {
    for (let t = 0.15; t < max; t += 0.15) {
      tmpQ.copy(p).addScaledVector(d, t);
      if (env(tmpQ) > 1) return t - 0.075;
    }
    return max;
  }

  // ------------------------------------------------------------------ tube buffers
  const newBuf = () => ({ pos: [], nor: [], uv: [], col: [], idx: [] });
  const TR = newBuf(); // trunk bark
  const BR = newBuf(); // branch bark
  const SB = newBuf(); // stub bark
  const LF = newBuf(); // leaves
  const tA = new V3(), tN = new V3(), tB = new V3(), tT = new V3(), tn = new V3();

  // Tube along pts with per-point radius and colour. Bark UVs keep a constant texel size:
  // the texture tile is ~0.36 m wide on the trunk, repeated a whole number of times around.
  function addTube(B, pts, rad, cols, radial, noiseAmp, tileW) {
    const base = B.pos.length / 3;
    const circ = 2 * Math.PI * rad[0];
    const rep = Math.max(1, Math.round(circ / tileW));
    const vScale = 1 / (2 * (circ / rep));
    const vOff = R(0, 8), nph = R(0, 6.28);
    let N = null, s = 0;
    for (let i = 0; i < pts.length; i++) {
      const p0 = pts[Math.max(0, i - 1)], p1 = pts[Math.min(pts.length - 1, i + 1)];
      tT.subVectors(p1, p0).normalize();
      if (!N) N = Math.abs(tT.y) < 0.9 ? new V3(0, 1, 0) : new V3(1, 0, 0);
      N.sub(tA.copy(tT).multiplyScalar(N.dot(tT))).normalize();
      tB.crossVectors(tT, N);
      if (i > 0) s += pts[i].distanceTo(pts[i - 1]);
      const v = vOff + s * vScale;
      for (let j = 0; j <= radial; j++) {
        const a = (j / radial) * Math.PI * 2;
        const rr = rad[i] * (1 + noiseAmp * (0.55 * Math.sin(3 * a + s * 2.1 + nph) + 0.45 * Math.sin(5 * a - s * 3.3 + nph * 2)));
        tn.copy(N).multiplyScalar(Math.cos(a)).addScaledVector(tB, Math.sin(a));
        B.pos.push(pts[i].x + tn.x * rr, pts[i].y + tn.y * rr, pts[i].z + tn.z * rr);
        B.nor.push(tn.x, tn.y, tn.z);
        B.uv.push((j / radial) * rep, v);
        B.col.push(cols[i][0], cols[i][1], cols[i][2]);
      }
    }
    const w = radial + 1;
    for (let i = 0; i < pts.length - 1; i++) {
      for (let j = 0; j < radial; j++) {
        const a = base + i * w + j, b = a + w;
        B.idx.push(a, b, a + 1, a + 1, b, b + 1);
      }
    }
    return { last: base + (pts.length - 1) * w, radial, N: N.clone(), B: tB.clone(), T: tT.clone(), c: pts[pts.length - 1].clone() };
  }

  // colour multiplier on the bark map: trunk bright, fading darker up the leader
  function trunkCol(p) {
    const k = smooth(2.6, 6.2, p.y);
    return [1 - 0.42 * k, 1 - 0.45 * k, 1 - 0.45 * k];
  }
  function branchCol(p, r) {
    const k = 0.92 + 0.08 * smooth(0.02, 0.1, r);
    const lo = 0.88 + 0.12 * smooth(3.5, 8, p.y);
    return [k * lo, k * lo, k * lo];
  }

  // ------------------------------------------------------------------ branch growth
  // A branch is a crooked polyline grown step by step with random kinks, tropism and envelope steering.
  function grow(p0, d0, len, r0, r1, lv, P) {
    const n = Math.max(2, Math.ceil(len / P.seg));
    const step = len / n;
    const pts = [p0.clone()];
    const d = d0.clone().normalize();
    const p = p0.clone();
    for (let i = 1; i <= n; i++) {
      const u = i / n;
      if (i > 1) {
        d.x += (rnd() - 0.5) * 2 * P.crook;
        d.y += (rnd() - 0.5) * 1.2 * P.crook;
        d.z += (rnd() - 0.5) * 2 * P.crook;
      }
      d.y += (P.up - P.flat * u) * step;
      if (P.steer) {
        tmpQ.copy(p).addScaledVector(d, step);
        const e = env(tmpQ);
        if (e > 0.9) d.addScaledVector(outward(p), -(e - 0.9) * P.steer);
      }
      d.normalize();
      p.addScaledVector(d, step);
      pts.push(p.clone());
    }
    const rad = pts.map((_, i) => r0 + (r1 - r0) * Math.pow(i / n, 0.85));
    const cum = [0];
    for (let i = 1; i < pts.length; i++) cum.push(cum[i - 1] + pts[i].distanceTo(pts[i - 1]));
    return { pts, rad, cum, len: cum[cum.length - 1], lv };
  }
  function sample(br, u) {
    const L = u * br.len;
    let i = 0;
    while (i < br.pts.length - 2 && br.cum[i + 1] < L) i++;
    const f = Math.min(1, Math.max(0, (L - br.cum[i]) / Math.max(1e-6, br.cum[i + 1] - br.cum[i])));
    return {
      p: br.pts[i].clone().lerp(br.pts[i + 1], f),
      t: br.pts[i + 1].clone().sub(br.pts[i]).normalize(),
      r: br.rad[i] + (br.rad[i + 1] - br.rad[i]) * f,
    };
  }
  // close the tip with a short cone and emit the tube
  function emitBranch(br, buf, radial, noise, colFn) {
    const n = br.pts.length;
    const tip = br.pts[n - 1].clone().addScaledVector(br.pts[n - 1].clone().sub(br.pts[n - 2]).normalize(), br.rad[n - 1] * 1.2);
    const pts = br.pts.concat([tip]);
    const rad = br.rad.concat([br.rad[n - 1] * 0.25]);
    const cols = pts.map((p, i) => colFn(p, rad[i]));
    addTube(buf, pts, rad, cols, radial, noise, 0.36);
  }

  const LV = {
    2: { dens: 2.5, u0: 0.15, th: [0.5, 1.05], out: 0.7, up: 0.12, lenA: 0.8, lenB: 0.36, min: 0.45, max: 2.7, minR: 0.025,
      P: { seg: 0.4, crook: 0.32, up: 0.03, flat: 0.28, steer: 3 } },
    3: { dens: 3.4, u0: 0.18, th: [0.55, 1.1], out: 0.5, up: 0.1, lenA: 0.5, lenB: 0.3, min: 0.26, max: 1.25, minR: 0.013,
      P: { seg: 0.3, crook: 0.38, up: 0.0, flat: 0.35, steer: 3 } },
    4: { dens: 2.4, u0: 0.25, th: [0.5, 1.0], out: 0.35, up: -0.05, lenA: 0.25, lenB: 0.2, min: 0.14, max: 0.55, minR: 0.0075,
      P: { seg: 0.3, crook: 0.28, up: -0.1, flat: 0.3, steer: 3 } },
  };
  const RADIAL = { 1: 10, 2: 6, 3: 4, 4: 3 };
  const clusters = []; // {p, t, k}

  function addCluster(p, t, k) {
    const e = env(p);
    if (rnd() > smooth(0.25, 0.7, e)) return; // the crown interior stays open
    clusters.push({ p: p.clone(), t: t.clone(), k, e });
  }

  // grow the children of `parent` at level lv, recursively down to the twigs
  function spawn(parent, lv, vigour) {
    const cfg = LV[lv];
    const count = Math.max(1, Math.round(parent.len * cfg.dens * vigour * R(0.8, 1.2)));
    let phi = R(0, Math.PI * 2);
    const perp = new V3(), q = new V3();
    for (let k = 0; k < count; k++) {
      const u = cfg.u0 + (1 - cfg.u0) * (k + R(0.15, 0.85)) / count;
      const s = sample(parent, u);
      phi += 2.4 + R(-0.6, 0.6);
      q.set(0, 1, 0); if (Math.abs(s.t.y) > 0.9) q.set(1, 0, 0);
      perp.crossVectors(s.t, q).normalize().applyAxisAngle(s.t, phi);
      const th = R(cfg.th[0], cfg.th[1]);
      const dir = s.t.clone().multiplyScalar(Math.cos(th)).addScaledVector(perp, Math.sin(th));
      dir.addScaledVector(outward(s.p), cfg.out).addScaledVector(UP, cfg.up).normalize();
      const space = room(s.p, dir, 8) * R(0.82, 1.0);
      const want = Math.min(cfg.max, cfg.lenA + cfg.lenB * parent.len * (1 - 0.55 * u)) * R(0.8, 1.2);
      const len = Math.min(want, space);
      if (len < cfg.min) {
        if (lv === 4 && space > 0.05) addCluster(s.p, dir, 0.85);
        continue;
      }
      const r0 = Math.min(s.r * 0.8, Math.max(cfg.minR, s.r * (0.42 + 0.38 * Math.sqrt(len / parent.len))));
      const r1 = Math.max(lv === 4 ? 0.004 : cfg.minR * 0.6, r0 * 0.35);
      const br = grow(s.p.clone().addScaledVector(dir, -s.r * 0.3), dir, len, r0, r1, lv, cfg.P);
      emitBranch(br, BR, RADIAL[lv], lv <= 2 ? 0.05 : 0.03, branchCol);
      if (lv < 4) {
        const vg = lv === 2 ? (rnd() < 0.18 ? 0.5 : 1) : vigour;
        spawn(br, lv + 1, vg);
        if (lv === 3) {
          // sprays straight off the young branch, along its outer part and at the tip
          addCluster(br.pts[br.pts.length - 1], sample(br, 1).t, 1.05);
          const nAl = Math.floor(br.len / 0.15);
          for (let a = 0; a < nAl; a++) {
            const sm = sample(br, 0.25 + 0.7 * (a + R(0.2, 0.8)) / Math.max(1, nAl));
            const sd = new V3(R(-1, 1), R(-0.6, 0.3), R(-1, 1)).normalize().lerp(sm.t, 0.35).normalize();
            addCluster(sm.p, sd, R(0.8, 1.0));
          }
        }
      } else {
        const st = sample(br, 1);
        addCluster(st.p, st.t, 1.0);
        const sm = sample(br, R(0.35, 0.7)); addCluster(sm.p, perp.clone().lerp(sm.t, 0.4).normalize(), 0.9);
      }
    }
  }

  // ------------------------------------------------------------------ trunk: bowed toward south + a little east
  const FORK = new V3(0.3, 3.0, 2.0);
  const BZ = [new V3(0, 0, 0), new V3(0.05, 1.0, 0.33), new V3(0.18, 2.2, 1.2), FORK];
  const bez = (t) => {
    const a = (1 - t) ** 3, b = 3 * (1 - t) ** 2 * t, c = 3 * (1 - t) * t * t, d = t ** 3;
    return new V3(
      a * BZ[0].x + b * BZ[1].x + c * BZ[2].x + d * BZ[3].x,
      a * BZ[0].y + b * BZ[1].y + c * BZ[2].y + d * BZ[3].y,
      a * BZ[0].z + b * BZ[1].z + c * BZ[2].z + d * BZ[3].z);
  };
  const Tbase = BZ[1].clone().sub(BZ[0]).normalize();
  const Tfork = BZ[3].clone().sub(BZ[2]).normalize();
  // trunk + leader as one continuous tube: the bowed trunk, then a short arc at the fork turning
  // the leader nearly straight up (the south limb leaves the outside of that bend)
  const trunkPts = [Tbase.clone().multiplyScalar(-0.18)], trunkRad = [0];
  {
    const NS = 36;
    for (let i = 0; i <= NS; i++) {
      const t = i / NS, p = bez(t);
      trunkPts.push(p);
      trunkRad.push(0.252 - 0.055 * t + 0.03 * Math.exp(-Math.max(0, p.y) / 0.22));
    }
    trunkRad[0] = trunkRad[1];
  }
  const leaderUp = new V3(-0.02, 1, -0.08).normalize();
  const arc = [FORK.clone()];
  {
    const d = new V3(), p = FORK.clone();
    for (let i = 1; i <= 4; i++) {
      d.copy(Tfork).lerp(leaderUp, i / 4).normalize();
      p.addScaledVector(d, 0.2); arc.push(p.clone());
    }
  }
  const leaderRest = grow(arc[arc.length - 1], leaderUp, 2.7, 0.18, 0.105, 1, { seg: 0.3, crook: 0.06, up: 0.25, flat: 0, steer: 0 });
  const leaderPts = arc.concat(leaderRest.pts.slice(1));
  const leaderRad = leaderPts.map((_, i) => i < arc.length ? 0.197 - 0.017 * (i / (arc.length - 1)) : leaderRest.rad[i - arc.length + 1]);
  const leader = { pts: leaderPts, rad: leaderRad, cum: [0], lv: 1 };
  for (let i = 1; i < leaderPts.length; i++) leader.cum.push(leader.cum[i - 1] + leaderPts[i].distanceTo(leaderPts[i - 1]));
  leader.len = leader.cum[leader.cum.length - 1];
  {
    const n = leaderPts.length;
    const tip = leaderPts[n - 1].clone().addScaledVector(leaderPts[n - 1].clone().sub(leaderPts[n - 2]).normalize(), 0.12);
    const pts = trunkPts.concat(leaderPts.slice(1), [tip]);
    const rad = trunkRad.concat(leaderRad.slice(1), [0.04]);
    addTube(TR, pts, rad, pts.map(trunkCol), 22, 0.045, 0.36);
  }

  // main limbs from the leader, 4–6, spreading into the umbrella
  const nL = 5 + (rnd() < 0.45 ? 1 : 0);
  const a0 = -Math.PI / 2 + R(-0.25, 0.25); // one limb always reaches north, over the road
  for (let i = 0; i < nL; i++) {
    // the last limb continues the leader; the one before it also climbs steeply to fill the crown top
    const top = i === nL - 1, high = i === nL - 2;
    const s = top ? sample(leader, 1) : sample(leader, 0.48 + 0.47 * (i + R(0.2, 0.8)) / (nL - 1));
    const az = a0 + i * (Math.PI * 2) / (nL - 1) + R(-0.3, 0.3);
    const el = top ? R(1.2, 1.4) : high ? R(0.95, 1.15) : R(0.6, 1.0);
    const dir = new V3(Math.cos(el) * Math.cos(az), Math.sin(el), Math.cos(el) * Math.sin(az));
    const len = room(s.p, dir, 12) * R(0.76, 0.9);
    const r0 = top ? 0.1 : s.r * R(0.66, 0.78);
    const limb = grow(s.p.clone().addScaledVector(dir, -0.04), dir, len, r0, r0 * 0.3, 1,
      { seg: 0.45, crook: 0.2, up: 0, flat: 0.32, steer: 2.5 });
    emitBranch(limb, BR, RADIAL[1], 0.06, branchCol);
    spawn(limb, 2, 1);
  }
  // lower laterals off the leader base (east, west, north, plus one at random)
  {
    const lat = [[0.1, 0.22], [Math.PI, 0.3], [-Math.PI / 2 + 0.3, 0.4], [R(1.2, 2.2), 0.34]];
    for (const [azb, u] of lat) {
      const s = sample(leader, u);
      const az = azb + R(-0.3, 0.3), el = R(0.3, 0.55);
      const dir = new V3(Math.cos(el) * Math.cos(az), Math.sin(el), Math.cos(el) * Math.sin(az));
      const len = Math.min(3.6, room(s.p, dir, 8) * R(0.8, 0.95));
      if (len < 0.8) continue;
      const br = grow(s.p.clone().addScaledVector(dir, -0.05), dir, len, s.r * 0.36, 0.025, 2, LV[2].P);
      emitBranch(br, BR, RADIAL[1], 0.05, branchCol);
      spawn(br, 3, 1);
    }
  }

  // ------------------------------------------------------------------ south limb (kept) or sawn stub (cut)
  const southDir = Tfork.clone().multiplyScalar(0.25).add(new V3(0.06, 0.02, 1)).normalize(); // nearly horizontal, rising slowly
  const southStart = FORK.clone().addScaledVector(Tfork, -0.16);
  if (!cut) {
    rnd = rngSouth; env = envBoth;
    const limb = grow(southStart, southDir, 6.4, 0.16, 0.06, 1, { seg: 0.45, crook: 0.08, up: 0.0, flat: 0.03, steer: 0.6 });
    emitBranch(limb, TR, 16, 0.05, trunkCol);
    spawn(limb, 2, 1);
    // short twigs with sprays all along the outer third so the limb end is not bare
    for (let k = 0; k < 9; k++) {
      const s = sample(limb, 0.66 + 0.34 * (k + 0.5) / 9);
      const d = new V3(R(-1, 1), R(-0.2, 0.5), R(-0.2, 1)).normalize();
      const tw = grow(s.p, d, R(0.35, 0.7), 0.025, 0.008, 4, LV[4].P);
      emitBranch(tw, BR, RADIAL[4], 0.03, branchCol);
      addCluster(tw.pts[tw.pts.length - 1], d, 1.0);
      addCluster(s.p, d.clone().lerp(s.t, 0.5).normalize(), 0.9);
    }
    rnd = rngMain; env = envMain;
  }

  // ------------------------------------------------------------------ leaf-spray cards
  // Each cluster is a rosette card (compound leaves radiating from the twig tip, bent into a shallow
  // umbrella) and, for most clusters, a hanging fan card (leaves drooping off the twig). Cards are
  // 3x3 grids; the front face is turned outward and the shading normal is blended toward the crown's
  // outward direction for soft, foliage-like lighting.
  {
    const PAD = 5 / 1024, C3 = 1 / 3;
    const cellUV = (k) => { const cx = k % 3, cy = (k / 3) | 0; return [cx * C3 + PAD, cy * C3 + PAD, (cx + 1) * C3 - PAD, (cy + 1) * C3 - PAD]; };
    const P = new V3(), S = new V3(), A = new V3(), B = new V3(), Nn = new V3(), O = new V3(), sn = new V3(), q = new V3();
    const DOWN = new V3(0, -1, 0);
    const minY = (z) => 3.5 + 0.5 * smooth(0.2, -1.4, z);
    const verts = [];
    let lowest = 0;
    const put = (uv, ix, iy, g, warm, fl) => {
      if (P.y < lowest) lowest = P.y;
      const u = uv[0] + (uv[2] - uv[0]) * (fl ? 1 - ix / 2 : ix / 2), v = uv[1] + (uv[3] - uv[1]) * (iy / 2);
      verts.push(P.x, P.y, P.z, sn.x, sn.y, sn.z, u, v, g * warm, g, g * (2 - warm) * 0.96);
    };
    for (const cl of clusters) {
      O.copy(outward(cl.p));
      const isFlush = flush && rnd() < 0.15;
      const ao = (0.5 + 0.5 * smooth(0.4, 1.0, cl.e)) * (0.84 + 0.16 * smooth(4, 9, cl.p.y));
      const tone = ao * R(0.78, 1.0), warm = R(0.95, 1.06);
      const topK = smooth(C1.y, C1.y + 4, cl.p.y);
      verts.length = 0; lowest = 1e9;
      let cards = 0;
      // rosette: faces up/outward, centred just past the twig tip
      {
        Nn.copy(O).multiplyScalar(0.6).addScaledVector(UP, 0.7 + 0.3 * topK).add(q.set(R(-0.35, 0.35), R(-0.2, 0.2), R(-0.35, 0.35))).normalize();
        A.set(1, 0, 0).sub(q.copy(Nn).multiplyScalar(Nn.x)).normalize().applyAxisAngle(Nn, R(0, 6.28));
        B.crossVectors(Nn, A);
        const D = R(0.76, 1.06) * cl.k, dr = R(0.1, 0.24);
        const uv = cellUV(isFlush ? 6 : [0, 1, 2, 8][Math.floor(rnd() * 4)]), fl = rnd() < 0.5;
        sn.copy(Nn).multiplyScalar(0.5).addScaledVector(O, 0.5).normalize();
        for (let iy = 0; iy <= 2; iy++) for (let ix = 0; ix <= 2; ix++) {
          const sx = ix / 2 - 0.5, sy = iy / 2 - 0.5, r2 = (sx * sx + sy * sy) * 2;
          P.copy(cl.p).addScaledVector(cl.t, 0.05).addScaledVector(A, sx * D).addScaledVector(B, sy * D)
            .addScaledVector(Nn, -dr * D * r2).addScaledVector(DOWN, 0.12 * D * r2);
          put(uv, ix, iy, tone * (0.92 + 0.08 * (1 - r2)), warm, fl);
        }
        cards++;
      }
      // fan: hangs off the twig, outward and down
      if (rnd() < 0.7 - 0.35 * topK) {
        S.copy(cl.t).multiplyScalar(0.4).addScaledVector(O, 0.55).addScaledVector(DOWN, R(0.35, 0.85)).normalize();
        const L = R(0.5, 0.74) * cl.k, W = L * R(0.85, 1.0), droop = R(0.1, 0.25);
        A.crossVectors(S, UP); if (A.lengthSq() < 1e-4) A.set(1, 0, 0);
        A.normalize().applyAxisAngle(S, R(-0.5, 0.5));
        Nn.crossVectors(A, S).normalize();
        if (Nn.dot(O) < 0) { A.negate(); Nn.negate(); }
        const uv = cellUV(isFlush ? 7 : 3 + Math.floor(rnd() * 3)), fl = rnd() < 0.5;
        sn.copy(Nn).multiplyScalar(0.4).addScaledVector(O, 0.6).normalize();
        for (let iy = 0; iy <= 2; iy++) for (let ix = 0; ix <= 2; ix++) {
          const t = iy / 2, sx = ix / 2 - 0.5;
          P.copy(cl.p).addScaledVector(S, -0.03 + L * t).addScaledVector(A, W * sx * (0.5 + 0.5 * t)).addScaledVector(DOWN, droop * L * t * t);
          put(uv, ix, iy, tone * (0.9 + 0.1 * t), warm, fl);
        }
        cards++;
      }
      if (lowest < minY(cl.p.z)) continue;
      const base = LF.pos.length / 3;
      for (let i = 0; i < verts.length; i += 11) {
        LF.pos.push(verts[i], verts[i + 1], verts[i + 2]); LF.nor.push(verts[i + 3], verts[i + 4], verts[i + 5]);
        LF.uv.push(verts[i + 6], verts[i + 7]); LF.col.push(verts[i + 8], verts[i + 9], verts[i + 10]);
      }
      for (let c = 0; c < cards; c++) for (let iy = 0; iy < 2; iy++) for (let ix = 0; ix < 2; ix++) {
        const a = base + c * 9 + iy * 3 + ix, b = a + 1, cc = a + 3, d = cc + 1;
        LF.idx.push(a, b, cc, b, d, cc);
      }
    }
  }

  // ------------------------------------------------------------------ sawn stub
  let stubCap = null;
  if (cut) {
    const pts = [], rad = [];
    const L = 0.66, n = 6;
    for (let i = 0; i <= n; i++) {
      const u = i / n;
      pts.push(southStart.clone().addScaledVector(southDir, L * u).add(new V3(0, 0.015 * Math.sin(u * 3), 0)));
      rad.push(0.162 - 0.012 * u);
    }
    const end = addTube(SB, pts, rad, pts.map(trunkCol), 16, 0.04, 0.36);
    // flat cut face, built from the last ring so its rim matches the bark exactly
    const pos = [], nor = [], uv = [], idx = [];
    const c = end.c, T = end.T;
    pos.push(c.x, c.y, c.z); nor.push(T.x, T.y, T.z); uv.push(0.5, 0.5);
    const rBase = rad[n] * 1.06;
    for (let j = 0; j <= end.radial; j++) {
      const k = (end.last + j) * 3;
      const x = SB.pos[k], y = SB.pos[k + 1], z = SB.pos[k + 2];
      pos.push(x, y, z); nor.push(T.x, T.y, T.z);
      const dx = x - c.x, dy = y - c.y, dz = z - c.z;
      const lu = dx * end.N.x + dy * end.N.y + dz * end.N.z, lv = dx * end.B.x + dy * end.B.y + dz * end.B.z;
      uv.push(0.5 + 0.5 * lu / rBase, 0.5 + 0.5 * lv / rBase);
    }
    for (let j = 0; j < end.radial; j++) idx.push(0, 1 + j, 2 + j);
    const g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
    g.setAttribute('normal', new THREE.Float32BufferAttribute(nor, 3));
    g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
    g.setIndex(idx);
    // make sure the fan faces along the limb (outward)
    const a = new V3(pos[3], pos[4], pos[5]).sub(c), b = new V3(pos[6], pos[7], pos[8]).sub(c);
    if (a.cross(b).dot(T) < 0) { for (let i = 0; i < idx.length; i += 3) { const t = idx[i + 1]; idx[i + 1] = idx[i + 2]; idx[i + 2] = t; } g.setIndex(idx); }
    stubCap = g;
  }

  // ------------------------------------------------------------------ materials + meshes
  rnd = rngTex;
  const trunkBark = barkMaps(THREE, rnd, { W: 256, H: 512, gx: 10, gy: 13,
    crack: [90, 68, 54], plates: [[156, 90, 58], [176, 106, 69], [140, 84, 56], [150, 100, 72], [122, 82, 62]] });
  const branchBark = barkMaps(THREE, rnd, { W: 128, H: 256, gx: 8, gy: 11,
    crack: [44, 36, 31], plates: [[96, 78, 66], [88, 72, 61], [104, 84, 70], [82, 68, 58]] });
  const trunkMat = new THREE.MeshStandardMaterial({ map: trunkBark.map, normalMap: trunkBark.normal, normalScale: new THREE.Vector2(1.4, 1.4),
    vertexColors: true, roughness: 0.93, metalness: 0 });
  const branchMat = new THREE.MeshStandardMaterial({ map: branchBark.map, normalMap: branchBark.normal, normalScale: new THREE.Vector2(1.0, 1.0),
    vertexColors: true, roughness: 0.9, metalness: 0 });
  const leafMap = leafAtlas(THREE, rnd, flush);
  const leafMat = new THREE.MeshStandardMaterial({
    map: leafMap, alphaTest: 0.5, side: THREE.DoubleSide, vertexColors: true, roughness: 0.82, metalness: 0,
    emissive: 0xffffff, emissiveMap: leafMap, emissiveIntensity: 0.14, // cheap stand-in for light passing through leaves
  });

  const toGeo = (B, withCol = true) => {
    const g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute(B.pos, 3));
    g.setAttribute('normal', new THREE.Float32BufferAttribute(B.nor, 3));
    g.setAttribute('uv', new THREE.Float32BufferAttribute(B.uv, 2));
    if (withCol) g.setAttribute('color', new THREE.Float32BufferAttribute(B.col, 3));
    g.setIndex(B.idx);
    g.computeBoundingBox(); g.computeBoundingSphere();
    return g;
  };
  tag(new THREE.Mesh(toGeo(TR), trunkMat), 'NeemTrunk', TIP);
  tag(new THREE.Mesh(toGeo(BR), branchMat), 'NeemBranches', TIP);
  tag(new THREE.Mesh(toGeo(LF), leafMat), 'NeemLeaves', TIP);
  if (cut) {
    tag(new THREE.Mesh(toGeo(SB), trunkMat), 'NeemStub', TIP_STUB);
    const cutMat = new THREE.MeshStandardMaterial({ map: cutFaceTexture(THREE, rnd), roughness: 0.8, metalness: 0 });
    stubCap.computeBoundingBox(); stubCap.computeBoundingSphere();
    tag(new THREE.Mesh(stubCap, cutMat), 'NeemStubCut', TIP_STUB);
  }

  group.userData.tip = TIP;
  group.userData.fork = FORK.clone();
  return group;
}

// ------------------------------------------------------------------ helpers

function mix(seed, k) {
  let h = (Math.imul((seed * 1000003) | 0, 2654435761) ^ Math.imul(k, 40503)) >>> 0;
  h = Math.imul(h ^ (h >>> 16), 2246822507) >>> 0;
  return (h ^ (h >>> 13)) >>> 0 || 1;
}

function mulberry32(a) {
  a = (a >>> 0) || 1;
  return function () {
    a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function canvas(w, h) {
  const c = document.createElement('canvas');
  c.width = w; c.height = h;
  return c;
}
// CPU-side 2D context: drawing + getImageData stay off the GPU (much faster to read back)
const ctx2d = (c) => c.getContext('2d', { willReadFrequently: true });

function dataTex(THREE, data, W, H, colorSpace) {
  const t = new THREE.DataTexture(data, W, H, THREE.RGBAFormat);
  t.colorSpace = colorSpace;
  t.wrapS = t.wrapT = THREE.RepeatWrapping;
  t.magFilter = THREE.LinearFilter;
  t.minFilter = THREE.LinearMipmapLinearFilter;
  t.generateMipmaps = true;
  t.anisotropy = 4;
  t.needsUpdate = true;
  return t;
}

// tileable fractal value noise in [0,1]
function tileNoise(W, H, nx, ny, oct, rnd) {
  const out = new Float32Array(W * H);
  let amp = 1, tot = 0;
  for (let o = 0; o < oct; o++) {
    const gx = nx << o, gy = ny << o;
    const grid = new Float32Array(gx * gy);
    for (let i = 0; i < grid.length; i++) grid[i] = rnd();
    for (let y = 0; y < H; y++) {
      const fy = (y / H) * gy, iy = Math.floor(fy), ty = fy - iy, sy = ty * ty * (3 - 2 * ty);
      const y0 = iy % gy, y1 = (iy + 1) % gy;
      for (let x = 0; x < W; x++) {
        const fx = (x / W) * gx, ix = Math.floor(fx), tx = fx - ix, sx = tx * tx * (3 - 2 * tx);
        const x0 = ix % gx, x1 = (ix + 1) % gx;
        const a = grid[y0 * gx + x0] + (grid[y0 * gx + x1] - grid[y0 * gx + x0]) * sx;
        const b = grid[y1 * gx + x0] + (grid[y1 * gx + x1] - grid[y1 * gx + x0]) * sx;
        out[y * W + x] += amp * (a + (b - a) * sy);
      }
    }
    tot += amp; amp *= 0.5;
  }
  for (let i = 0; i < out.length; i++) out[i] /= tot;
  return out;
}

// Fissured bark: tileable Voronoi plates on a noise-warped domain (jagged, irregular plate edges),
// a finer secondary crack network that breaks plates into small scales, flaky noise on the faces,
// and a matching tangent-space normal map from the same height field. Written straight into
// DataTextures (no canvas read-back), rows bottom-up.
function barkMaps(THREE, rnd, o) {
  const { W, H, gx, gy } = o;
  const cells = (nx, ny, jit) => {
    const cw = W / nx, ch = H / ny, px = new Float32Array(nx * ny), py = new Float32Array(nx * ny);
    for (let j = 0; j < ny; j++) for (let i = 0; i < nx; i++) {
      px[j * nx + i] = (i + 0.5 + jit * (rnd() - 0.5)) * cw; py[j * nx + i] = (j + 0.5 + jit * (rnd() - 0.5)) * ch;
    }
    return { nx, ny, cw, ch, px, py };
  };
  const vor = (G, x, y, ay, out) => {
    const cx = Math.floor(x / G.cw), cy = Math.floor(y / G.ch);
    let f1 = 1e9, f2 = 1e9, id = 0;
    for (let dj = -1; dj <= 1; dj++) for (let di = -1; di <= 1; di++) {
      let i = cx + di, j = cy + dj, ox = 0, oy = 0;
      if (i < 0) { i += G.nx; ox = -W; } else if (i >= G.nx) { i -= G.nx; ox = W; }
      if (j < 0) { j += G.ny; oy = -H; } else if (j >= G.ny) { j -= G.ny; oy = H; }
      const k = j * G.nx + i;
      const ddx = G.px[k] + ox - x, ddy = (G.py[k] + oy - y) * ay;
      const dd = ddx * ddx + ddy * ddy;
      if (dd < f1) { f2 = f1; f1 = dd; id = k; } else if (dd < f2) f2 = dd;
    }
    out[0] = Math.sqrt(f2) - Math.sqrt(f1); out[1] = id;
  };
  const G1 = cells(gx, gy, 0.85), G2 = cells(gx * 2, gy * 2, 0.9);
  const pc = [];
  for (let k = 0; k < gx * gy; k++) {
    const base = o.plates[Math.floor(rnd() * o.plates.length)], v = 0.85 + 0.3 * rnd();
    pc.push([base[0] * v, base[1] * v, base[2] * v]);
  }
  const fine = tileNoise(W, H, 32, 64, 2, rnd), mid = tileNoise(W, H, 12, 24, 2, rnd), big = tileNoise(W, H, 3, 4, 2, rnd);
  const wx = tileNoise(W, H, 6, 10, 2, rnd), wy = tileNoise(W, H, 6, 10, 2, rnd);
  const hgt = new Float32Array(W * H), d = new Uint8Array(W * H * 4), r1 = [0, 0], r2 = [0, 0];
  for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
    const p = y * W + x;
    let X = x + (wx[p] - 0.5) * G1.cw * 0.9, Y = y + (wy[p] - 0.5) * G1.ch * 0.9;
    X = (X + W) % W; Y = (Y + H) % H;
    vor(G1, X, Y, 0.52, r1);
    vor(G2, (X + 7.3) % W, Y, 0.7, r2);
    const nz = fine[p] * 0.6 + mid[p] * 0.4, bg = big[p];
    const w1 = 1.3 + 2.4 * bg + 1.2 * nz;
    const c1 = 1 - Math.min(1, Math.max(0, (r1[0] - w1 * 0.35) / w1));
    const c2 = (1 - Math.min(1, Math.max(0, (r2[0] - 0.5) / 1.3))) * (nz > 0.45 ? 0.75 : 0.25);
    const k1 = c1 * c1 * (3 - 2 * c1), crack = Math.max(k1, c2 * 0.8);
    const bevel = Math.min(1, r1[0] / (G1.cw * 0.2)) * (0.8 + 0.2 * Math.min(1, r2[0] / 3));
    const col = pc[r1[1]];
    const flake = 0.68 + 0.62 * nz + 0.25 * (mid[p] - 0.5);
    const weather = Math.max(0, bg - 0.55) * 1.6; // occasional greyer weathered patches
    for (let c = 0; c < 3; c++) {
      let v = col[c] * flake * (0.8 + 0.2 * bevel);
      v += (118 - v) * weather * 0.6;
      v += (o.crack[c] * (0.8 + 0.4 * nz) - v) * crack;
      d[p * 4 + c] = Math.max(0, Math.min(255, v));
    }
    d[p * 4 + 3] = 255;
    hgt[p] = (1 - crack) * (0.5 + 0.12 * bevel + 0.6 * fine[p] + 0.25 * mid[p]) - 0.3 * k1;
  }
  const map = dataTex(THREE, d, W, H, THREE.SRGBColorSpace);
  const nd = new Uint8Array(W * H * 4);
  const STR = 2.2;
  for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
    const xl = (x + W - 1) % W, xr = (x + 1) % W, yu = (y + H - 1) % H, ydn = (y + 1) % H;
    const dx = (hgt[y * W + xr] - hgt[y * W + xl]) * STR;
    const dy = (hgt[ydn * W + x] - hgt[yu * W + x]) * STR;
    let nx = -dx, ny = -dy, nz = 1;
    const l = Math.sqrt(nx * nx + ny * ny + nz * nz);
    const p = (y * W + x) * 4;
    nd[p] = (nx / l * 0.5 + 0.5) * 255; nd[p + 1] = (ny / l * 0.5 + 0.5) * 255; nd[p + 2] = (nz / l * 0.5 + 0.5) * 255; nd[p + 3] = 255;
  }
  const normal = dataTex(THREE, nd, W, H, THREE.NoColorSpace);
  return { map, normal };
}

// Fresh sawn face: pale wood with growth rings, sapwood band, thin bark rim, faint saw marks.
function cutFaceTexture(THREE, rnd) {
  const S = 256, c = canvas(S, S), g = ctx2d(c);
  const cx = S / 2 + (rnd() - 0.5) * 14, cy = S / 2 + (rnd() - 0.5) * 14;
  g.fillStyle = '#5a4436'; g.fillRect(0, 0, S, S);
  g.beginPath(); g.arc(S / 2, S / 2, S * 0.47, 0, Math.PI * 2); g.fillStyle = '#e3c89e'; g.fill();
  g.beginPath(); g.arc(S / 2, S / 2, S * 0.43, 0, Math.PI * 2); g.fillStyle = '#d9b98c'; g.fill();
  // heartwood slightly darker in the middle
  const hw = g.createRadialGradient(cx, cy, 0, cx, cy, S * 0.36);
  hw.addColorStop(0, 'rgba(196,150,100,0.55)'); hw.addColorStop(0.8, 'rgba(205,165,115,0.25)'); hw.addColorStop(1, 'rgba(205,165,115,0)');
  g.fillStyle = hw; g.beginPath(); g.arc(S / 2, S / 2, S * 0.43, 0, Math.PI * 2); g.fill();
  const ph = rnd() * 6.28;
  for (let r = 4; r < S * 0.42; r += 3 + rnd() * 4.5) {
    g.beginPath();
    for (let k = 0; k <= 64; k++) {
      const a = (k / 64) * Math.PI * 2;
      const w = r * (1 + 0.03 * Math.sin(3 * a + ph + r * 0.05) + 0.02 * Math.sin(5 * a - ph));
      const x = cx + Math.cos(a) * w * (1 - 0.08 * (r / S)), y = cy + Math.sin(a) * w;
      if (k) g.lineTo(x, y); else g.moveTo(x, y);
    }
    g.strokeStyle = `rgba(150,105,62,${0.25 + rnd() * 0.3})`;
    g.lineWidth = 0.8 + rnd() * 1.4; g.stroke();
  }
  // saw marks
  g.save(); g.beginPath(); g.arc(S / 2, S / 2, S * 0.43, 0, Math.PI * 2); g.clip();
  g.strokeStyle = 'rgba(120,85,50,0.08)'; g.lineWidth = 1;
  for (let y = -S; y < 2 * S; y += 5) { g.beginPath(); g.moveTo(0, y); g.lineTo(S, y + S * 0.3); g.stroke(); }
  // a few radial checks
  g.strokeStyle = 'rgba(110,75,45,0.45)';
  for (let i = 0; i < 4; i++) {
    const a = rnd() * 6.28, r0 = S * (0.05 + rnd() * 0.1), r1 = S * (0.18 + rnd() * 0.15);
    g.beginPath(); g.moveTo(cx + Math.cos(a) * r0, cy + Math.sin(a) * r0); g.lineTo(cx + Math.cos(a + 0.05) * r1, cy + Math.sin(a + 0.05) * r1); g.stroke();
  }
  g.restore();
  g.beginPath(); g.arc(cx, cy, 2.5, 0, Math.PI * 2); g.fillStyle = '#8a6440'; g.fill();
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4;
  return t;
}

// ---------------------------------------------------------------- leaf atlas
// 3x3 atlas (cells of 341 px):
//   0,1,2,8  rosettes: 8–11 pinnate leaves radiating from the twig tip (2 has fresh light-green leaves)
//   3,4,5    fans: leaves drooping from a twig at the top centre (5 has fresh leaves)
//   6,7      reddish-brown new flush (rosette, fan) — drawn only with opts.flush
// Each compound leaf has 5–8 pairs of narrow, falcate, serrated leaflets. A handful of leaf sprites are
// drawn once and stamped (rotated, scaled, mirrored) to build the sprays, which keeps this fast.
// The canvas is copied into a DataTexture so the transparent texels keep a green colour (no dark
// fringes from alpha testing and mipmaps).
const MATURE = ['#4f7a35', '#4a7332', '#44692f', '#3f652c', '#3a5e29', '#56803a', '#4c7634'];
const PALE = ['#6b8d4e', '#729553', '#668a4a', '#7a9a5c'];
const FRESH = ['#86b34c', '#8fbb55', '#7bab45', '#9cc35e'];
const FLUSH = ['#8a4a2e', '#96553a', '#7c4229', '#a0603e', '#8e5a36'];

function leafAtlas(THREE, rnd, flush) {
  const S = 1024, CELL = S / 3;
  const c = canvas(S, S), g = ctx2d(c);
  // sprites: [kind, curve]
  const kinds = ['mature', 'mature', 'dark', 'dark', 'tip', 'pale', 'fresh', 'fresh'];
  if (flush) kinds.push('flush', 'flush', 'flushTip');
  const sprites = kinds.map((k, i) => leafSprite(k, (i % 2 ? 1 : -0.4) * (0.5 + 0.5 * rnd()), rnd));
  const byKind = (k) => sprites.filter((_, i) => kinds[i] === k);
  const pick = (a) => a[Math.floor(rnd() * a.length)];
  const green = () => { const r = rnd(); return pick(byKind(r < 0.42 ? 'mature' : r < 0.74 ? 'dark' : r < 0.88 ? 'pale' : 'tip')); };
  const freshMix = () => rnd() < 0.45 ? pick(byKind(rnd() < 0.6 ? 'fresh' : 'tip')) : green();
  const flushMix = () => rnd() < 0.6 ? pick(byKind(rnd() < 0.7 ? 'flush' : 'flushTip')) : green();
  const stamp = (spr, x, y, ang, len) => {
    const k = len / spr.height;
    g.setTransform(1, 0, 0, 1, 0, 0);
    g.translate(x, y); g.rotate(ang); g.scale(rnd() < 0.5 ? -k : k, k);
    g.drawImage(spr, -spr.width / 2, 0);
  };
  const rosette = (cell, n, src, lenK) => {
    const cx = (cell % 3) * CELL + CELL / 2, cy = ((cell / 3) | 0) * CELL + CELL / 2;
    const a0 = rnd() * 6.28, order = [];
    for (let i = 0; i < n; i++) order.push({ a: a0 + (i / n) * 6.28 + (rnd() - 0.5) * 0.4, d: rnd() });
    order.sort((p, q) => p.d - q.d);
    for (const o of order) stamp(src(), cx, cy, o.a, CELL * 0.47 * lenK * (0.8 + 0.2 * rnd()));
    g.setTransform(1, 0, 0, 1, 0, 0);
    g.fillStyle = '#4e4034'; g.beginPath(); g.arc(cx, cy, 3, 0, 6.28); g.fill();
  };
  const fan = (cell, n, src) => {
    const ox = (cell % 3) * CELL, oy = ((cell / 3) | 0) * CELL;
    const cx = ox + CELL / 2, top = oy + 8, tl = CELL * 0.1, tx = cx + (rnd() - 0.5) * 12;
    g.setTransform(1, 0, 0, 1, 0, 0);
    g.strokeStyle = '#4e4034'; g.lineWidth = 3.5; g.lineCap = 'round';
    g.beginPath(); g.moveTo(cx, top); g.lineTo(tx, top + tl); g.stroke();
    const order = [];
    for (let i = 0; i < n; i++) {
      const f = i / (n - 1) - 0.5;
      order.push({ a: -f * 2.5 + (rnd() - 0.5) * 0.25, f, d: rnd(), u: 0.3 + 0.7 * rnd() });
    }
    order.sort((p, q) => p.d - q.d);
    for (const o of order) {
      const bx = cx + (tx - cx) * o.u, by = top + tl * o.u;
      // longest straight down, shorter to the sides so the fan stays inside the cell
      const room = Math.min(CELL - 10 - (by - oy), (CELL * 0.5 - 8) / Math.max(0.25, Math.abs(Math.sin(o.a))));
      stamp(src(), bx, by, o.a, Math.min(room, CELL * 0.82) * (0.82 + 0.18 * rnd()));
    }
  };
  rosette(0, 10, green, 1); rosette(1, 9, green, 0.95); rosette(2, 10, freshMix, 1); rosette(8, 7, green, 1);
  fan(3, 8, green); fan(4, 7, green); fan(5, 8, freshMix);
  if (flush) { rosette(6, 10, flushMix, 1); fan(7, 8, flushMix); }
  g.setTransform(1, 0, 0, 1, 0, 0);
  const img = g.getImageData(0, 0, S, S);
  const d = new Uint8Array(img.data.buffer.slice(0));
  for (let i = 0; i < d.length; i += 4) {
    if (d[i + 3] < 10) { d[i] = 66; d[i + 1] = 100; d[i + 2] = 44; d[i + 3] = 0; }
  }
  const t = dataTex(THREE, d, S, S, THREE.SRGBColorSpace);
  t.wrapS = t.wrapT = THREE.ClampToEdgeWrapping;
  return t;
}

function shade(hex, k) {
  const n = parseInt(hex.slice(1), 16);
  const r = Math.min(255, ((n >> 16) & 255) * k), g = Math.min(255, ((n >> 8) & 255) * k), b = Math.min(255, (n & 255) * k);
  return `rgb(${r | 0},${g | 0},${b | 0})`;
}

// one compound leaf, base at top-centre, pointing down (+y); `curve` bends the rachis sideways
function leafSprite(kind, curve, rnd) {
  const W = 160, H = 360;
  const c = canvas(W, H), g = ctx2d(c);
  g.lineCap = 'round'; g.lineJoin = 'round';
  const pick = (a) => a[Math.floor(rnd() * a.length)];
  const N = 24, pts = [];
  for (let i = 0; i <= N; i++) {
    const t = i / N;
    pts.push([W / 2 + curve * 26 * t * t, 3 + t * (H - 10), Math.atan2(curve * 52 * t, H - 10)]);
  }
  const L = H - 10;
  const pairs = 5 + Math.floor(rnd() * 4);
  const dark = kind === 'dark' ? 0.82 : 1;
  const colOf = (tt) => {
    if (kind === 'fresh') return pick(FRESH);
    if (kind === 'flush') return pick(FLUSH);
    if (kind === 'tip' && tt > 0.62) return pick(FRESH);
    if (kind === 'flushTip' && tt > 0.55) return pick(FLUSH);
    if (kind === 'pale') return rnd() < 0.55 ? pick(PALE) : pick(MATURE);
    return rnd() < 0.14 ? pick(PALE) : pick(MATURE);
  };
  for (let k = 0; k < pairs; k++) {
    const t = 0.1 + 0.8 * (k / Math.max(1, pairs - 1));
    for (const side of [-1, 1]) {
      const tt = Math.min(0.96, t + (side > 0 ? 0.03 : 0));
      const [px, py, h0] = pts[Math.round(tt * N)];
      const h = h0; // heading measured from +y
      const ll = L * (0.17 + 0.09 * Math.sin(Math.PI * Math.min(1, tt * 1.05))) * (0.92 + 0.16 * rnd());
      const ll2 = Math.min(ll, (W / 2 - 4 - Math.abs(px - W / 2)) / Math.sin(1.0));
      const wl = ll2 * (0.12 + 0.03 * rnd());
      const a = h + side * (1.12 - 0.3 * tt + (rnd() - 0.5) * 0.16);
      leaflet(g, px, py, a, ll2, wl, side, shade(colOf(tt), dark * (0.9 + 0.2 * rnd())));
    }
  }
  const [ex, ey] = pts[N];
  leaflet(g, ex, ey - L * 0.04, 0, L * 0.2, L * 0.022, 0, shade(colOf(1), dark));
  g.strokeStyle = kind === 'fresh' ? '#7a9a45' : kind.startsWith('flush') ? '#6e4a30' : '#56683a';
  g.lineWidth = 2.6;
  g.beginPath(); g.moveTo(pts[0][0], pts[0][1]);
  for (let i = 1; i <= N; i++) g.lineTo(pts[i][0], pts[i][1]);
  g.stroke();
  return c;
}

function leaflet(g, x, y, a, ll, wl, side, col) {
  const M = 12, A = [], B = [];
  let px = x, py = y;
  for (let i = 0; i <= M; i++) {
    const s = i / M;
    const h = a - side * 0.5 * s; // falcate: curves toward the leaf tip
    const dx = Math.sin(h), dy = Math.cos(h);
    if (i > 0) { px += dx * ll / M; py += dy * ll / M; }
    let w = wl * Math.pow(Math.sin(Math.PI * Math.min(1, 0.08 + s * 0.92)), 0.7);
    if (i === M) w = 0;
    const ser = (i % 2 === 1) ? 1.15 : 0.92; // serrated edge
    const nx = dy, ny = -dx;
    const ob = s < 0.3 ? 0.7 : 0.95; // oblique (asymmetric) base
    A.push([px + nx * w * ser, py + ny * w * ser]);
    B.push([px - nx * w * ser * ob, py - ny * w * ser * ob]);
  }
  g.beginPath(); g.moveTo(x, y);
  for (const p of A) g.lineTo(p[0], p[1]);
  for (let i = B.length - 1; i >= 0; i--) g.lineTo(B[i][0], B[i][1]);
  g.closePath();
  g.fillStyle = col; g.fill();
  // midrib
  g.strokeStyle = 'rgba(215,230,170,0.3)'; g.lineWidth = 1;
  g.beginPath(); g.moveTo(x, y);
  let mx = x, my = y;
  for (let i = 1; i <= M; i++) { const h = a - side * 0.5 * (i / M); mx += Math.sin(h) * ll / M; my += Math.cos(h) * ll / M; g.lineTo(mx, my); }
  g.stroke();
}
