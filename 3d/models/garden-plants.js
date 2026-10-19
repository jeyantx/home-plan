// Procedural garden plants for the garden plan (branch garden-v1): dwarf banana clump, areca (butterfly) palm, drumstick tree.
//
//   import { createBanana, createArecaPalm, createMoringa } from './models/garden-plants.js';
//   const b = createBanana(THREE, mergeGeometries, { seed: 6, height: 2.4, avoid: [1, 0] });
//
// Units: metres, +Y up. Origin = base of the plant at soil level.
// face = [x, z] (areca palm): all fronds grow toward that side, within +-spread radians (a pot in a corner).
// avoid = [x, z] or a list of them: directions (in the plant's own frame) toward a wall or a walkway; leaves and branches that point that way are kept short.
// Meshes: plain Mesh + merged BufferGeometry (no InstancedMesh), so the path tracer can use them. Seeded PRNG, no Math.random.

function avoidList(THREE, a) { if (!a) return null; const l = Array.isArray(a[0]) ? a : [a]; return l.map(v => new THREE.Vector2(v[0], v[1]).normalize()); }
const hit = (av, d) => Math.max(...av.map(v => d.dot(v)));
function prng(seed) { let s = (seed || 1) * 9301 + 49297; return () => (s = (s * 16807) % 2147483647) / 2147483647; }

function kit(THREE, mergeGeometries, seed) {
  const rnd = prng(seed), rr = (a, b) => a + (b - a) * rnd(), V = (x, y, z) => new THREE.Vector3(x, y, z);
  const flat = g => (g.index ? g.toNonIndexed() : g);
  const tube = (pts, r0, r1, seg = 6) => {   // tapered tube along a polyline of Vector3
    const curve = new THREE.CatmullRomCurve3(pts), n = Math.max(2, pts.length * 3), g = new THREE.TubeGeometry(curve, n, 1, seg, false);
    const p = g.attributes.position, tmp = new THREE.Vector3();
    for (let i = 0; i <= n; i++) {
      const t = i / n, c = curve.getPointAt(t), r = r0 + (r1 - r0) * t;
      for (let j = 0; j <= seg; j++) { const k = i * (seg + 1) + j; tmp.fromBufferAttribute(p, k).sub(c).multiplyScalar(r).add(c); p.setXYZ(k, tmp.x, tmp.y, tmp.z) }
    }
    g.computeVertexNormals(); return flat(g);
  };
  // a strip (leaf blade, leaflet) following a path: centre line pts, half-width w(t), fold = V-shape lift of the edges
  const strip = (pts, w, fold = 0, side = null, nSeg = 0) => {
    const curve = new THREE.CatmullRomCurve3(pts), n = nSeg || Math.max(4, pts.length * 4), pos = [];
    const up = V(0, 1, 0);
    const row = t => { const c = curve.getPointAt(t), tg = curve.getTangentAt(t); let s = new THREE.Vector3().crossVectors(tg, side || up); if (s.lengthSq() < 1e-6) s = V(1, 0, 0); s.normalize();
      const nrm = new THREE.Vector3().crossVectors(s, tg).normalize(), hw = w(t);
      return [c.clone().addScaledVector(s, -hw).addScaledVector(nrm, fold * hw), c.clone(), c.clone().addScaledVector(s, hw).addScaledVector(nrm, fold * hw)] };
    let prev = row(0);
    for (let i = 1; i <= n; i++) { const cur = row(i / n);
      for (let k = 0; k < 2; k++) { const a = prev[k], b = prev[k + 1], c = cur[k], d = cur[k + 1]; pos.push(a, c, b, b, c, d) }
      prev = cur }
    const g = new THREE.BufferGeometry().setFromPoints(pos); g.computeVertexNormals(); return g;
  };
  const leafCard = (L, W) => { const sh = new THREE.Shape(); sh.moveTo(0, 0); sh.quadraticCurveTo(W, L * 0.45, 0, L); sh.quadraticCurveTo(-W, L * 0.45, 0, 0); return flat(new THREE.ShapeGeometry(sh, 2)) };
  const place = (g, pos, dir, roll) => { const q = new THREE.Quaternion().setFromUnitVectors(V(0, 1, 0), dir.clone().normalize());
    q.multiply(new THREE.Quaternion().setFromAxisAngle(V(0, 1, 0), roll)); return g.clone().applyMatrix4(new THREE.Matrix4().compose(pos, q, V(1, 1, 1))) };
  const group = new THREE.Group();
  const mk = (arr, mat, name) => { if (!arr.length) return; const me = new THREE.Mesh(mergeGeometries(arr.map(flat)), mat); me.name = name; me.castShadow = true; me.receiveShadow = true; group.add(me); return me };
  const mat = (color, o = {}) => new THREE.MeshStandardMaterial({ color, roughness: 0.6, side: THREE.DoubleSide, ...o });
  return { rnd, rr, V, tube, strip, leafCard, place, group, mk, mat };
}

// Dwarf banana (Poovan / Grand Naine): a clump of a mother plant with a bunch and two suckers. height = top of the leaves.
export function createBanana(THREE, mergeGeometries, opts = {}) {
  const K = kit(THREE, mergeGeometries, opts.seed || 6), { rr, V } = K, H = opts.height || 2.4;
  const av = avoidList(THREE, opts.avoid);
  const stems = [], leaves = [], ribs = [], dry = [], fruit = [], bud = [];
  const plant = (x, z, h, nLeaf, bunch) => {
    const sh = h * 0.5, r = 0.035 + h * 0.022;   // pseudostem height and radius
    stems.push(K.tube([V(x, 0, z), V(x + rr(-0.02, 0.02), sh * 0.5, z + rr(-0.02, 0.02)), V(x, sh, z)], r * 1.3, r * 0.8, 10));
    for (let i = 0; i < nLeaf; i++) {
      const az = i * 2.4 + rr(-0.3, 0.3), d = new THREE.Vector2(Math.cos(az), Math.sin(az)), age = i / Math.max(1, nLeaf - 1);
      let L = h * rr(0.62, 0.75), a0 = 1.25 - age * 0.45, a1 = -0.15 - age * 1.0;   // pitch (rad) at the petiole and at the tip: young leaves stand up, old ones droop
      if (av && hit(av, d) > (opts.avoidCos ?? 0.2)) { L *= 0.6; a0 = 1.4; a1 = 0.7 }   // toward the wall: short and upright
      const pts = [V(x + d.x * r * 0.6, sh * rr(0.92, 1.0), z + d.y * r * 0.6)], n = 10, step = L / n;
      for (let k = 1; k <= n; k++) { const a = a0 + (a1 - a0) * (k / n) ** 1.3, p = pts[k - 1];
        pts.push(V(p.x + d.x * Math.cos(a) * step, p.y + Math.sin(a) * step, p.z + d.y * Math.cos(a) * step)) }
      const W = L * 0.24, w = t => t < 0.22 ? 0.004 : W * 0.5 * Math.min(1, (t - 0.22) / 0.1) * (t > 0.85 ? 0.25 + 0.75 * (1 - t) / 0.15 : 1);
      const isDry = i === nLeaf - 1 && h > 1.5;
      (isDry ? dry : leaves).push(K.strip(pts, w, 0.12));
      if (!isDry) ribs.push(K.tube(pts.slice(0, 9), 0.014, 0.004, 4));
    }
    if (bunch) {   // stalk out of the top, curving down, a bunch of green fingers and the purple bud
      const s0 = V(x, sh, z), dx = bunch[0], dz = bunch[1], p1 = V(x + dx * 0.25, sh + 0.12, z + dz * 0.25), p2 = V(x + dx * 0.42, sh - 0.25, z + dz * 0.42), p3 = V(x + dx * 0.45, sh - 0.85, z + dz * 0.45);
      stems.push(K.tube([s0, p1, p2, p3], 0.025, 0.018, 6));
      for (let hnd = 0; hnd < 5; hnd++) { const y = sh - 0.3 - hnd * 0.11, cx = x + dx * 0.43, cz = z + dz * 0.43;
        for (let f = 0; f < 9; f++) { const a = f / 9 * Math.PI * 2 + hnd, ox = Math.cos(a) * 0.07, oz = Math.sin(a) * 0.07;
          fruit.push(K.tube([V(cx + ox, y, cz + oz), V(cx + ox * 2.2, y + 0.07, cz + oz * 2.2), V(cx + ox * 2.6, y + 0.16, cz + oz * 2.6)], 0.016, 0.01, 5)) } }
      const c = new THREE.ConeGeometry(0.06, 0.2, 8); c.rotateX(Math.PI); c.translate(p3.x, p3.y - 0.08, p3.z); bud.push(c);
    }
  };
  plant(0, 0, H, 11, [-0.6, 0.8]);
  plant(0.32, 0.22, H * 0.55, 6, null);
  plant(-0.25, 0.3, H * 0.35, 5, null);
  K.mk(stems, K.mat('#7c8a46', { roughness: 0.75 }), 'BananaStem');
  K.mk(leaves, K.mat('#4f8a2f', { roughness: 0.5 }), 'BananaLeaves');
  K.mk(ribs, K.mat('#9aa85a'), 'BananaMidribs');
  K.mk(dry, K.mat('#8a6a3a', { roughness: 0.9 }), 'BananaDryLeaf');
  K.mk(fruit, K.mat('#6f9a2c', { roughness: 0.45 }), 'BananaBunch');
  K.mk(bud, K.mat('#6a1f3a', { roughness: 0.5 }), 'BananaBud');
  K.group.name = 'Banana'; return K.group;
}

// Areca (butterfly) palm, Dypsis lutescens: a clump of thin canes with arching feather leaves. height = above the soil.
export function createArecaPalm(THREE, mergeGeometries, opts = {}) {
  const K = kit(THREE, mergeGeometries, opts.seed || 3), { rr, V } = K, H = opts.height || 1.1;
  const av = avoidList(THREE, opts.avoid);
  const canes = [], rach = [], lfl = [];
  const nC = 6, face = opts.face == null ? null : Math.atan2(opts.face[1], opts.face[0]), spread = opts.spread ?? 0.5;
  for (let c = 0; c < nC; c++) {
    const ac = c / nC * Math.PI * 2 + rr(-0.3, 0.3), r0 = rr(0.02, 0.09), ch = H * rr(0.3, 0.55), lean = rr(0.04, 0.12);
    const a0 = face == null ? ac : face + (c / (nC - 1) - 0.5) * 2 * spread;   // face: all fronds grow toward one side (a corner pot), within +-spread
    const b = V(Math.cos(ac) * r0, 0, Math.sin(ac) * r0), top = V(b.x + Math.cos(a0) * lean * 0.6, ch, b.z + Math.sin(a0) * lean * 0.6);
    canes.push(K.tube([b, V((b.x + top.x) / 2, ch / 2, (b.z + top.z) / 2), top], 0.016, 0.011, 6));
    const nF = 3;
    for (let f = 0; f < nF; f++) {
      let az = a0 + (f - 1) * (face == null ? 0.9 : spread * 0.4) + rr(-0.15, 0.15); const d = new THREE.Vector2(Math.cos(az), Math.sin(az));
      let L = (H - ch) * rr(0.95, 1.25) + 0.25, rise = rr(0.9, 1.3);
      if (av && hit(av, d) > 0.3) { L *= 0.6; rise = 1.6 }
      const pts = [];
      for (let k = 0; k <= 6; k++) { const t = k / 6; pts.push(V(top.x + d.x * L * 0.75 * t, top.y + L * (rise * t - 0.85 * t * t), top.z + d.y * L * 0.75 * t)) }
      rach.push(K.tube(pts, 0.008, 0.003, 4));
      const curve = new THREE.CatmullRomCurve3(pts);
      for (let k = 2; k < 28; k++) { const t = k / 28, p = curve.getPointAt(t), tg = curve.getTangentAt(t), s = new THREE.Vector3().crossVectors(tg, V(0, 1, 0)).normalize();
        const ll = 0.24 * Math.sin(Math.PI * Math.min(1, t * 1.1)) + 0.05;
        for (const sg of [-1, 1]) { const dir = s.clone().multiplyScalar(sg).addScaledVector(tg, 0.9).add(V(0, -0.25, 0)).normalize();
          const tip = p.clone().addScaledVector(dir, ll), mid = p.clone().addScaledVector(dir, ll * 0.5).add(V(0, 0.02, 0));
          lfl.push(K.strip([p, mid, tip], t2 => 0.011 * Math.sin(Math.PI * Math.min(1, 0.15 + t2)), 0.3, null, 3)) } }
    }
  }
  K.mk(canes, K.mat('#a7a94a', { roughness: 0.6 }), 'ArecaCanes');
  K.mk(rach, K.mat('#9aa34a'), 'ArecaStalks');
  K.mk(lfl, K.mat('#4e8c34', { roughness: 0.5 }), 'ArecaLeaves');
  K.group.name = 'ArecaPalm'; return K.group;
}

// Drumstick tree (Murungai, Moringa oleifera), kept low: slim grey trunk, a few upright branches, airy fern-like leaves, hanging pods.
export function createMoringa(THREE, mergeGeometries, opts = {}) {
  const K = kit(THREE, mergeGeometries, opts.seed || 8), { rr, V } = K, H = opts.height || 3.0, CR = opts.crown || 0.7;
  const av = avoidList(THREE, opts.avoid);
  const wood = [], lf = [], pods = [];
  const fork = V(rr(-0.05, 0.05), H * 0.38, rr(-0.05, 0.05));
  wood.push(K.tube([V(0, 0, 0), V(0.03, H * 0.2, -0.02), fork], 0.07, 0.05, 8));
  const leafG = K.leafCard(0.03, 0.012);
  const nB = 5;
  for (let b = 0; b < nB; b++) {
    let az = b / nB * Math.PI * 2 + rr(-0.4, 0.4); const d = new THREE.Vector2(Math.cos(az), Math.sin(az));
    let reach = CR * rr(0.6, 1.0); if (av && hit(av, d) > 0.3) reach *= 0.5;
    const tip = V(fork.x + d.x * reach, H * rr(0.82, 1.0), fork.z + d.y * reach), mid = V(fork.x + d.x * reach * 0.4, H * 0.62, fork.z + d.y * reach * 0.4);
    wood.push(K.tube([fork, mid, tip], 0.035, 0.012, 6));
    const curve = new THREE.CatmullRomCurve3([fork, mid, tip]);
    for (let s = 0; s < 9; s++) {   // leaf sprays along the upper half of the branch: a rachis with pairs of tiny leaflets
      const t = 0.4 + s / 9 * 0.6, p = curve.getPointAt(t), a = rr(0, Math.PI * 2);
      const dir = V(Math.cos(a), rr(-0.4, 0.3), Math.sin(a)).normalize(), L = rr(0.25, 0.4);
      const e = p.clone().addScaledVector(dir, L).add(V(0, -L * 0.25, 0));
      wood.push(K.tube([p, p.clone().lerp(e, 0.5).add(V(0, 0.03, 0)), e], 0.004, 0.002, 3));
      for (let k = 1; k <= 9; k++) { const q = p.clone().lerp(e, k / 10), side = new THREE.Vector3().crossVectors(dir, V(0, 1, 0)).normalize();
        for (const sg of [-1, 1]) lf.push(K.place(leafG, q, side.clone().multiplyScalar(sg).add(V(0, 0.5, 0)), rr(0, 6.28))) }
    }
    if (b % 2 === 0) for (let k = 0; k < 3; k++) { const p = curve.getPointAt(rr(0.55, 0.9)), L = rr(0.3, 0.45), sw = rr(-0.06, 0.06);
      pods.push(K.tube([p, p.clone().add(V(sw, -L * 0.5, 0.02)), p.clone().add(V(sw * 1.5, -L, 0.04))], 0.008, 0.006, 4)) }
  }
  K.mk(wood, K.mat('#8d8a80', { roughness: 0.95 }), 'MoringaWood');
  K.mk(lf, K.mat('#6a9c3c', { roughness: 0.55 }), 'MoringaLeaves');
  K.mk(pods, K.mat('#5c7f2c', { roughness: 0.6 }), 'MoringaPods');
  K.group.name = 'Moringa'; return K.group;
}
