// Procedural potted bamboo plant (artificial "bamboo tree" in a matte black pot).
//
//   import { createBambooPlant } from './models/bamboo-plant.js';
//   const plant = createBambooPlant(THREE, { seed: 1 });
//
// Units: metres. Origin = centre of the pot's base, +Y up.
// Options:
//   seed   (number, default 1)    deterministic randomness
//   height (number, default 1.5)  height of the top leaves above the pot base
//
// Draw calls: 4 (pot, moss, stems+twigs merged, leaves as one InstancedMesh).
// No per-frame work. Textures are tiny canvases generated once per plant.

export function createBambooPlant(THREE, opts = {}) {
  const seed = Number.isFinite(opts.seed) ? opts.seed : 1;
  const targetH = Number.isFinite(opts.height) ? opts.height : 1.5;
  const rnd = mulberry32(seed);
  const R = (a, b) => a + (b - a) * rnd();
  const TIP = 'Bamboo plant, 1.5 m, black pot';

  const group = new THREE.Group();
  group.name = 'BambooPlant';
  const tag = (mesh, name) => { mesh.name = name; mesh.userData.tip = TIP; group.add(mesh); return mesh; };

  // ------------------------------------------------------------------ pot
  const POT_H = 0.30, RT = 0.15, RB = 0.13, SOIL = 0.276;
  const prof = [
    [0, 0], [RB - 0.010, 0], [RB - 0.002, 0.003], [RB, 0.010],
    [RT - 0.003, POT_H - 0.016], [RT + 0.003, POT_H - 0.013], [RT + 0.005, POT_H - 0.006],
    [RT + 0.004, POT_H - 0.001], [RT, POT_H], [RT - 0.008, POT_H], [RT - 0.010, POT_H - 0.004],
    [RT - 0.012, SOIL - 0.012],
  ].map(([x, y]) => new THREE.Vector2(x, y));
  const potGeo = new THREE.LatheGeometry(prof, 48);
  const potMat = new THREE.MeshStandardMaterial({ color: 0x161616, roughness: 0.62, metalness: 0 });
  const pot = tag(new THREE.Mesh(potGeo, potMat), 'BambooPot');
  pot.castShadow = true; pot.receiveShadow = true;

  // ------------------------------------------------------------------ moss
  {
    const rings = 12, segs = 48, rMax = RT - 0.0115;
    const ph = Array.from({ length: 6 }, () => R(0, Math.PI * 2));
    const noise = (x, z) =>
      0.5 * Math.sin(x * 61 + ph[0]) * Math.sin(z * 57 + ph[1]) +
      0.3 * Math.sin(x * 137 + z * 41 + ph[2]) +
      0.2 * Math.sin(z * 173 - x * 89 + ph[3]);
    const pos = [], col = [], uv = [], idx = [];
    const cA = [0.07, 0.15, 0.04], cB = [0.16, 0.27, 0.07], cC = [0.20, 0.19, 0.08];
    for (let i = 0; i <= rings; i++) {
      const rr = (i / rings) * rMax;
      const n = i === 0 ? 1 : segs;
      for (let j = 0; j < n; j++) {
        const a = (j / segs) * Math.PI * 2 + (i % 2) * 0.05;
        const x = Math.cos(a) * rr, z = Math.sin(a) * rr;
        const nz = noise(x, z);
        const y = SOIL + 0.004 + 0.004 * nz + 0.006 * Math.pow(i / rings, 4);
        pos.push(x, y, z);
        const t = 0.5 + 0.5 * nz, b = Math.max(0, Math.sin(x * 97 + z * 23 + ph[4])) * 0.5;
        col.push(
          cA[0] + (cB[0] - cA[0]) * t + (cC[0] - cA[0]) * b,
          cA[1] + (cB[1] - cA[1]) * t + (cC[1] - cA[1]) * b,
          cA[2] + (cB[2] - cA[2]) * t + (cC[2] - cA[2]) * b);
        uv.push(x * 12, z * 12);
      }
    }
    for (let j = 0; j < segs; j++) idx.push(0, 1 + ((j + 1) % segs), 1 + j);
    for (let i = 1; i < rings; i++) {
      const a0 = 1 + (i - 1) * segs, a1 = 1 + i * segs;
      for (let j = 0; j < segs; j++) {
        const j1 = (j + 1) % segs;
        idx.push(a0 + j, a0 + j1, a1 + j, a0 + j1, a1 + j1, a1 + j);
      }
    }
    const g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
    g.setAttribute('color', new THREE.Float32BufferAttribute(col, 3));
    g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
    g.setIndex(idx);
    g.computeVertexNormals();
    const mossMat = new THREE.MeshStandardMaterial({ vertexColors: true, map: mossTexture(THREE, rnd), roughness: 1, metalness: 0 });
    const moss = tag(new THREE.Mesh(g, mossMat), 'BambooMoss');
    moss.receiveShadow = true; moss.castShadow = false;
  }

  // ------------------------------------------------------------------ stems + twigs (one merged geometry)
  const S = { pos: [], nor: [], uv: [], col: [], idx: [] };
  const UP = new THREE.Vector3(0, 1, 0);
  const tmpA = new THREE.Vector3();

  // tube along pts; per-point radius, v coordinate and colour
  function addTube(pts, rad, vs, cols, radial) {
    const base = S.pos.length / 3;
    let N = null;
    const T = new THREE.Vector3(), B = new THREE.Vector3(), n = new THREE.Vector3();
    for (let i = 0; i < pts.length; i++) {
      const p0 = pts[Math.max(0, i - 1)], p1 = pts[Math.min(pts.length - 1, i + 1)];
      T.subVectors(p1, p0).normalize();
      if (!N) {
        N = Math.abs(T.y) < 0.9 ? new THREE.Vector3(0, 1, 0) : new THREE.Vector3(1, 0, 0);
        N.sub(tmpA.copy(T).multiplyScalar(N.dot(T))).normalize();
      } else {
        N.sub(tmpA.copy(T).multiplyScalar(N.dot(T))).normalize();
      }
      B.crossVectors(T, N);
      for (let j = 0; j <= radial; j++) {
        const a = (j / radial) * Math.PI * 2;
        n.copy(N).multiplyScalar(Math.cos(a)).addScaledVector(B, Math.sin(a));
        S.pos.push(pts[i].x + n.x * rad[i], pts[i].y + n.y * rad[i], pts[i].z + n.z * rad[i]);
        S.nor.push(n.x, n.y, n.z);
        S.uv.push(j / radial, vs[i]);
        S.col.push(cols[i][0], cols[i][1], cols[i][2]);
      }
    }
    const w = radial + 1;
    for (let i = 0; i < pts.length - 1; i++) {
      for (let j = 0; j < radial; j++) {
        const a = base + i * w + j, b = a + w;
        S.idx.push(a, b, a + 1, a + 1, b, b + 1);
      }
    }
  }

  const leaves = []; // {p, d, len, wid, roll, tone}

  function pushLeaf(p, yaw, pitch, heightT, lenK) {
    const d = new THREE.Vector3(Math.cos(yaw) * Math.cos(pitch), Math.sin(pitch), Math.sin(yaw) * Math.cos(pitch));
    leaves.push({
      p: p.clone().addScaledVector(d, 0.004),
      d,
      len: R(0.085, 0.14) * lenK,
      wid: R(0.85, 1.15),
      roll: R(-0.45, 0.45),
      heightT,
    });
  }

  // twig with leaves: alternating single leaves along its outer part plus a small tip cluster
  function twig(p0, dir, len, r0, r1, droop, heightT, nLeaves) {
    const steps = 4, pts = [], rad = [], vs = [], cols = [];
    for (let i = 0; i <= steps; i++) {
      const u = i / steps;
      pts.push(p0.clone().addScaledVector(dir, len * u).add(tmpA.set(0, -droop * len * u * u, 0)));
      rad.push(r0 + (r1 - r0) * u);
      vs.push(u * len / 0.35);
      cols.push([0.86, 0.84, 0.62]);
    }
    addTube(pts, rad, vs, cols, 4);
    const at = (u) => { const f = u * steps, i = Math.min(steps - 1, Math.floor(f)); return pts[i].clone().lerp(pts[i + 1], f - i); };
    const tanYaw = Math.atan2(dir.z, dir.x);
    const nTip = Math.min(nLeaves, 2 + Math.floor(rnd() * 2));
    const nAlong = nLeaves - nTip;
    let side = rnd() < 0.5 ? -1 : 1;
    for (let k = 0; k < nAlong; k++) {
      const u = 0.35 + 0.6 * (k + R(0.1, 0.9)) / Math.max(1, nAlong);
      side = -side;
      pushLeaf(at(u), tanYaw + side * R(0.55, 1.25), R(-0.85, 0.05) + 0.3 * heightT, heightT, 1);
    }
    const tipPitch = Math.asin(Math.max(-1, Math.min(1, dir.y))) * 0.5;
    for (let k = 0; k < nTip; k++) {
      const f = nTip === 1 ? 0 : k / (nTip - 1) - 0.5;
      pushLeaf(at(1), tanYaw + f * R(0.6, 1.1) + R(-0.15, 0.15), tipPitch + R(-0.6, 0.15) + 0.2 * heightT, heightT, 1.05);
    }
    return pts;
  }

  const nMain = 5 + Math.floor(rnd() * 2);    // 5–6 main culms
  const nThin = 2;                             // thinner secondary culms
  const culms = [];
  const az0 = R(0, Math.PI * 2);
  for (let c = 0; c < nMain + nThin; c++) {
    const thin = c >= nMain;
    const az = az0 + (c / (nMain + nThin)) * Math.PI * 2 + R(-0.35, 0.35);
    const rr = thin ? R(0.04, 0.09) : R(0.015, 0.085);
    culms.push({
      thin,
      base: new THREE.Vector3(Math.cos(az) * rr, SOIL - 0.02, Math.sin(az) * rr),
      out: new THREE.Vector3(Math.cos(az), 0, Math.sin(az)),
      top: thin ? R(0.95, 1.12) : R(1.08, 1.40),
      r0: thin ? R(0.0038, 0.0045) : R(0.0055, 0.0075),
      lean: thin ? R(0.10, 0.16) : R(0.03, 0.11),
      bow: R(-0.02, 0.05),
      vOff: R(0, 10),
      tone: R(0.9, 1.06),
    });
  }
  // make sure one culm reaches near the full height
  culms.reduce((a, b) => (b.top > a.top && !b.thin ? b : a), culms[0]).top = 1.42;

  for (const cu of culms) {
    const L = cu.top - cu.base.y;
    const at = (s) => cu.base.clone()
      .addScaledVector(UP, s)
      .addScaledVector(cu.out, cu.lean * s + cu.bow * s * s / L);
    // node positions along length
    const nodes = [];
    let s = R(0.06, 0.10);
    while (s < L - 0.05) { nodes.push(s); s += R(0.15, 0.25) * (cu.thin ? 0.85 : 1); }
    // sample positions (regular + node detail)
    const samples = [];
    for (let q = 0; q <= L; q += 0.045) samples.push(q);
    samples.push(L);
    const nodeOffs = [-0.012, -0.005, -0.0018, 0, 0.0018, 0.005, 0.012];
    for (const nd of nodes) for (const o of nodeOffs) samples.push(nd + o);
    samples.sort((a, b) => a - b);
    const uniq = samples.filter((v, i) => v >= 0 && v <= L && (i === 0 || v - samples[i - 1] > 0.0008));
    const pts = [], rad = [], vs = [], cols = [];
    for (const q of uniq) {
      let nearest = 1;
      for (const nd of nodes) if (Math.abs(q - nd) < Math.abs(nearest)) nearest = q - nd;
      const ridge = Math.exp(-Math.pow(nearest / 0.0022, 2));
      const band = Math.exp(-Math.pow((nearest + 0.002) / 0.006, 2));
      const r = cu.r0 * (1 - 0.18 * q / L) * (1 + 0.17 * ridge);
      const k = cu.tone * (1 - 0.45 * band);
      const lowDark = q < 0.05 ? 0.75 + 5 * q : 1;
      pts.push(at(q)); rad.push(r); vs.push(cu.vOff + q / 0.35);
      cols.push([k * lowDark, k * 0.97 * lowDark, k * 0.9 * lowDark]);
    }
    // close the top with a short cone
    const topP = at(L);
    pts.push(topP.clone().addScaledVector(UP, 0.004)); rad.push(cu.r0 * 0.25); vs.push(cu.vOff + L / 0.35);
    cols.push([0.7, 0.65, 0.5]);
    addTube(pts, rad, vs, cols, cu.thin ? 8 : 10);

    // branches from nodes in the upper 2/3
    const yStart = cu.base.y + L * (cu.thin ? 0.45 : 0.36);
    let side = rnd() < 0.5 ? 0 : 1;
    const outYaw = Math.atan2(cu.out.z, cu.out.x);
    for (const nd of nodes) {
      const p = at(nd);
      if (p.y < yStart) continue;
      const ht = (p.y - yStart) / (cu.top - yStart);           // 0 low … 1 top
      side ^= 1;
      const nb = cu.thin ? 1 : (rnd() < 0.55 ? 2 : 1);
      for (let b = 0; b < nb; b++) {
        // alternate sides, biased outward
        let yaw = outYaw + (side ? 1 : -1) * R(0.5, 1.7) + (b ? R(-0.9, 0.9) : 0);
        const el = R(0.45, 0.95) + 0.25 * ht;
        const dir = new THREE.Vector3(Math.cos(yaw) * Math.cos(el), Math.sin(el), Math.sin(yaw) * Math.cos(el));
        const shape = Math.sin(Math.PI * (0.18 + 0.72 * ht));     // ovoid canopy
        const blen = (cu.thin ? 0.7 : 1) * (0.09 + 0.18 * shape) * R(0.75, 1.2);
        const start = p.clone().addScaledVector(dir, cu.r0 * 0.8);
        const fan = 5 + Math.floor(rnd() * 5);
        const bp = twig(start, dir, blen, 0.0019, 0.0011, R(0.15, 0.45), ht, fan);
        // side branchlets along the branch
        const nSub = blen > 0.14 ? 2 + (rnd() < 0.4 ? 1 : 0) : 1;
        for (let k = 0; k < nSub; k++) {
          const u = 0.35 + 0.5 * (k + R(0, 0.7)) / nSub;
          const i0 = Math.min(3, Math.floor(u * 4));
          const sp = bp[i0].clone().lerp(bp[i0 + 1], u * 4 - i0);
          const sy = yaw + (k % 2 ? 1 : -1) * R(0.5, 1.1);
          const se = el * R(0.3, 0.8);
          const sd = new THREE.Vector3(Math.cos(sy) * Math.cos(se), Math.sin(se), Math.sin(sy) * Math.cos(se));
          twig(sp, sd, R(0.05, 0.11), 0.0011, 0.0008, R(0.1, 0.4), ht, 4 + Math.floor(rnd() * 4));
        }
      }
    }
    // crown: short branchlets fanning out of the culm tip
    const nCrown = cu.thin ? 2 : 3 + Math.floor(rnd() * 2);
    for (let k = 0; k < nCrown; k++) {
      const yaw = R(0, Math.PI * 2), el = R(0.7, 1.25);
      const dir = new THREE.Vector3(Math.cos(yaw) * Math.cos(el), Math.sin(el), Math.sin(yaw) * Math.cos(el));
      twig(at(L - R(0.0, 0.06)), dir, R(0.05, 0.12), 0.0014, 0.0009, R(0.1, 0.3), 1, 4 + Math.floor(rnd() * 3));
    }
  }

  // ------------------------------------------------------------------ fit height (uniform scale about the soil centre)
  const leafGeo = makeLeafGeometry(THREE);
  leafGeo.computeBoundingBox();
  const lb = leafGeo.boundingBox;
  const M = new THREE.Matrix4(), X = new THREE.Vector3(), Y = new THREE.Vector3(), Z = new THREE.Vector3();
  const corner = new THREE.Vector3();
  const mats = leaves.map((lf) => {
    X.copy(lf.d);
    Y.copy(UP).addScaledVector(X, -UP.dot(X));
    if (Y.lengthSq() < 1e-6) Y.set(1, 0, 0);
    Y.normalize().applyAxisAngle(X, lf.roll);
    Z.crossVectors(X, Y);
    const m = new THREE.Matrix4().makeBasis(
      X.clone().multiplyScalar(lf.len),
      Y.clone().multiplyScalar(lf.len),
      Z.clone().multiplyScalar(lf.len * lf.wid));
    m.setPosition(lf.p);
    return m;
  });
  let maxY = 0;
  for (const m of mats) for (let c = 0; c < 8; c++) {
    corner.set(c & 1 ? lb.max.x : lb.min.x, c & 2 ? lb.max.y : lb.min.y, c & 4 ? lb.max.z : lb.min.z).applyMatrix4(m);
    if (corner.y > maxY) maxY = corner.y;
  }
  const k = (targetH - SOIL) / (maxY - SOIL);
  const fit = new THREE.Matrix4().makeTranslation(0, SOIL, 0)
    .multiply(new THREE.Matrix4().makeScale(k, k, k))
    .multiply(new THREE.Matrix4().makeTranslation(0, -SOIL, 0));

  // stems mesh
  {
    const g = new THREE.BufferGeometry();
    g.setAttribute('position', new THREE.Float32BufferAttribute(S.pos, 3));
    g.setAttribute('normal', new THREE.Float32BufferAttribute(S.nor, 3));
    g.setAttribute('uv', new THREE.Float32BufferAttribute(S.uv, 2));
    g.setAttribute('color', new THREE.Float32BufferAttribute(S.col, 3));
    g.setIndex(S.idx);
    g.applyMatrix4(fit);
    const stemMat = new THREE.MeshStandardMaterial({ map: barkTexture(THREE, rnd), vertexColors: true, roughness: 0.55, metalness: 0 });
    const stems = tag(new THREE.Mesh(g, stemMat), 'BambooStems');
    stems.castShadow = true; stems.receiveShadow = true;
  }

  // leaves: one InstancedMesh, two-tone green via instance colours
  {
    const leafMat = new THREE.MeshStandardMaterial({
      map: leafTexture(THREE), roughness: 0.5, metalness: 0, side: THREE.DoubleSide,
      emissive: 0x1e3a0e, emissiveIntensity: 0.35, // cheap stand-in for light passing through leaves
    });
    const im = new THREE.InstancedMesh(leafGeo, leafMat, mats.length);
    const light = new THREE.Color('#b2d85a'), mid = new THREE.Color('#6eaf3c'), deep = new THREE.Color('#53922f');
    const c = new THREE.Color();
    for (let i = 0; i < mats.length; i++) {
      im.setMatrixAt(i, M.multiplyMatrices(fit, mats[i]));
      const r = rnd();
      if (r < 0.42) c.copy(light).lerp(mid, R(0, 0.3));
      else if (r < 0.85) c.copy(mid).lerp(light, R(0, 0.25));
      else c.copy(deep).lerp(mid, R(0, 0.5));
      c.multiplyScalar(R(0.9, 1.08));
      im.setColorAt(i, c);
    }
    im.instanceMatrix.needsUpdate = true;
    if (im.instanceColor) im.instanceColor.needsUpdate = true;
    im.computeBoundingBox();
    im.computeBoundingSphere();
    const lm = tag(im, 'BambooLeaves');
    lm.castShadow = true; lm.receiveShadow = true;
  }

  group.userData.tip = TIP;
  return group;
}

// ------------------------------------------------------------------ helpers

function mulberry32(a) {
  a = (a >>> 0) || 1;
  return function () {
    a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// Lanceolate leaf, unit length along +X, normal ~+Y, width along Z.
// Arched along its length and folded slightly along the midrib.
function makeLeafGeometry(THREE) {
  const N = 10, W = 0.068, FOLD = 0.2;
  const pos = [], uv = [], idx = [];
  for (let i = 0; i <= N; i++) {
    const t = i / N;
    let hw = W * Math.pow(Math.sin(Math.PI * Math.pow(t, 0.72)), 0.85);
    if (t < 0.06) hw = Math.max(hw, 0.006);
    const x = t;
    const y = 0.10 * t - 0.30 * t * t;
    const ye = y + FOLD * hw;
    pos.push(x, ye, -hw, x, y, 0, x, ye, hw);
    uv.push(0, t, 0.5, t, 1, t);
  }
  for (let i = 0; i < N; i++) {
    const a = i * 3, b = a + 3;
    idx.push(a, b, a + 1, a + 1, b, b + 1, a + 1, b + 1, a + 2, a + 2, b + 1, b + 2);
  }
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
  g.setIndex(idx);
  g.computeVertexNormals();
  return g;
}

function canvas(w, h) {
  const c = document.createElement('canvas');
  c.width = w; c.height = h;
  return c;
}

function finishTexture(THREE, c, repeat) {
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace;
  if (repeat) { t.wrapS = t.wrapT = THREE.RepeatWrapping; }
  t.anisotropy = 4;
  t.needsUpdate = true;
  return t;
}

// leaf: neutral light grey (tinted by instance colour) with a pale midrib and faint parallel veins
function leafTexture(THREE) {
  const c = canvas(64, 256), g = c.getContext('2d');
  const grd = g.createLinearGradient(0, 0, 64, 0);
  grd.addColorStop(0, 'rgb(205,205,200)');
  grd.addColorStop(0.35, 'rgb(232,232,226)');
  grd.addColorStop(0.5, 'rgb(240,240,232)');
  grd.addColorStop(0.65, 'rgb(232,232,226)');
  grd.addColorStop(1, 'rgb(205,205,200)');
  g.fillStyle = grd; g.fillRect(0, 0, 64, 256);
  // slightly yellower base
  const by = g.createLinearGradient(0, 0, 0, 256);
  by.addColorStop(0, 'rgba(255,240,170,0.35)');
  by.addColorStop(0.25, 'rgba(255,240,170,0)');
  g.fillStyle = by; g.fillRect(0, 0, 64, 256);
  // parallel veins
  g.fillStyle = 'rgba(60,70,40,0.10)';
  for (const x of [10, 17, 24, 40, 47, 54]) g.fillRect(x, 0, 1, 256);
  // midrib
  g.fillStyle = 'rgba(255,255,225,0.85)'; g.fillRect(30, 0, 4, 256);
  g.fillStyle = 'rgba(90,100,50,0.25)'; g.fillRect(29, 0, 1, 256); g.fillRect(34, 0, 1, 256);
  return finishTexture(THREE, c, false);
}

// bark: golden tan with darker brown blotches and fine vertical streaks (tiles both ways)
function barkTexture(THREE, rnd) {
  const W = 64, H = 256;
  const c = canvas(W, H), g = c.getContext('2d');
  g.fillStyle = '#e9c27a'; g.fillRect(0, 0, W, H);
  for (let i = 0; i < 70; i++) {
    g.fillStyle = rnd() < 0.5 ? 'rgba(255,225,160,0.12)' : 'rgba(140,90,40,0.10)';
    g.fillRect(rnd() * W, 0, 0.6 + rnd() * 1.6, H);
  }
  const blot = (x, y, rx, ry, a, col) => {
    for (const dx of [-W, 0, W]) for (const dy of [-H, 0, H]) {
      g.save(); g.translate(x + dx, y + dy); g.scale(1, ry / rx);
      const gr = g.createRadialGradient(0, 0, 0, 0, 0, rx);
      gr.addColorStop(0, `rgba(${col},${a})`);
      gr.addColorStop(0.55, `rgba(${col},${a * 0.7})`);
      gr.addColorStop(1, `rgba(${col},0)`);
      g.fillStyle = gr; g.fillRect(-rx, -rx, rx * 2, rx * 2); g.restore();
    }
  };
  for (let i = 0; i < 12; i++) {
    const x = rnd() * W, y = rnd() * H;
    const n = 2 + Math.floor(rnd() * 3);
    for (let k = 0; k < n; k++)
      blot(x + (rnd() - 0.5) * 14, y + (rnd() - 0.5) * 40, 4 + rnd() * 10, 14 + rnd() * 40, 0.22 + rnd() * 0.33, '118,72,30');
  }
  for (let i = 0; i < 25; i++) blot(rnd() * W, rnd() * H, 1 + rnd() * 3, 3 + rnd() * 10, 0.3 + rnd() * 0.3, '92,58,28');
  return finishTexture(THREE, c, true);
}

// moss: fine speckle detail
function mossTexture(THREE, rnd) {
  const c = canvas(64, 64), g = c.getContext('2d');
  g.fillStyle = 'rgb(200,200,190)'; g.fillRect(0, 0, 64, 64);
  for (let i = 0; i < 700; i++) {
    const v = rnd();
    g.fillStyle = v < 0.5 ? `rgba(40,50,20,${0.2 + rnd() * 0.4})` : `rgba(255,255,220,${0.15 + rnd() * 0.35})`;
    g.fillRect(Math.floor(rnd() * 64), Math.floor(rnd() * 64), 1 + Math.floor(rnd() * 2), 1 + Math.floor(rnd() * 2));
  }
  return finishTexture(THREE, c, true);
}
