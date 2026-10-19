// Procedural flowering plants common in Tamil Nadu home gardens.
//
//   import { createTNPlant, TN_PLANTS } from './models/tn-plants.js';
//   const p = createTNPlant(THREE, mergeGeometries, { type: 'malli', seed: 3 });
//
// Units: metres, +Y up. Origin = base of the plant at soil level.
// Meshes (plain Mesh + merged BufferGeometry, no InstancedMesh, so the path tracer can use them):
//   stems, leaves, flowers, and flower centres where the species has them. Seeded PRNG, no Math.random.

export const TN_PLANTS = {
  malli:          { name: 'Malli (Jasmine, Jasminum sambac)', note: 'white, scented, flowers most of the year', h: 0.9, w: 0.75, leaf: [0.055, 0.03], leafC: '#2f5a2a', nLeaf: 260, fl: 'star', flC: '#fbfaf3', flR: 0.022, nFl: 60, cenC: '#f1ecc8' },
  sembaruthi:     { name: 'Sembaruthi (Hibiscus, red)', note: 'big red flowers, used for pooja', h: 1.55, w: 0.85, leaf: [0.1, 0.06], leafC: '#2e6b2a', nLeaf: 300, fl: 'hibiscus', flC: '#c8102e', flR: 0.06, nFl: 14, cenC: '#f5d142' },
  nandiyavattai:  { name: 'Nandiyavattai (Crape jasmine)', note: 'white pinwheel flowers, glossy leaves', h: 1.2, w: 0.9, leaf: [0.11, 0.045], leafC: '#2d5f2c', nLeaf: 230, fl: 'pinwheel', flC: '#ffffff', flR: 0.035, nFl: 34, cenC: '#f3efd8' },
  vetchi:         { name: 'Vetchi / Idly poo (Ixora, red)', note: 'ball-shaped red flower clusters', h: 0.9, w: 0.7, leaf: [0.08, 0.035], leafC: '#2c5b28', nLeaf: 230, fl: 'ball', flC: '#e03a24', flR: 0.042, nFl: 16 },
  kanakambaram:   { name: 'Kanakambaram (Crossandra, orange)', note: 'orange flower spikes, worn in the hair', h: 0.6, w: 0.5, leaf: [0.08, 0.032], leafC: '#3b6e2e', nLeaf: 140, fl: 'spike', flC: '#ff7a1f', flR: 0.015, nFl: 16 },
  nithyakalyani:  { name: 'Nithya kalyani (Periwinkle, pink)', note: 'flowers every day, needs little water', h: 0.45, w: 0.45, leaf: [0.045, 0.022], leafC: '#356b2c', nLeaf: 150, fl: 'star', flC: '#e2558c', flR: 0.028, nFl: 34, cenC: '#8a1f4a' },
  rose:           { name: 'Rose (pink)', note: 'Indian pink rose', h: 0.75, w: 0.55, leaf: [0.05, 0.03], leafC: '#355e2b', nLeaf: 160, fl: 'rose', flC: '#c2185b', flR: 0.032, nFl: 8 },
  karuveppilai:   { name: 'Karuveppilai (Curry leaf)', note: 'for the kitchen, small tree kept trimmed', h: 1.4, w: 0.6, leaf: [0.035, 0.014], leafC: '#3d6b2b', nLeaf: 520, fl: null },
  tulsi:          { name: 'Tulsi (Holy basil)', note: 'in the Tulsi maadam, worshipped daily', h: 0.6, w: 0.5, leaf: [0.035, 0.022], leafC: '#3f6a32', nLeaf: 260, fl: 'spike', flC: '#7a4a7e', flR: 0.012, nFl: 14 },
  // garden plan (branch garden-v1): kitchen vegetables and herbs in the raised beds, climbing jasmine on the wall, lemon in a pot
  thakkali:       { name: 'Thakkali (Tomato)', note: 'in the vegetable bed GD-07', h: 0.8, w: 0.55, leaf: [0.06, 0.035], leafC: '#3f7330', nLeaf: 200, fl: 'ball', flC: '#d8341c', flR: 0.026, nFl: 9 },
  kathiri:        { name: 'Kathirikkai (Brinjal)', note: 'in the vegetable bed GD-07', h: 0.7, w: 0.5, leaf: [0.1, 0.06], leafC: '#4a6e3a', nLeaf: 120, fl: 'ball', flC: '#4a1d5e', flR: 0.04, nFl: 5 },
  milagai:        { name: 'Milagai (Chilli)', note: 'in the vegetable bed GD-07', h: 0.55, w: 0.45, leaf: [0.05, 0.02], leafC: '#356b2c', nLeaf: 170, fl: 'spike', flC: '#c4161c', flR: 0.009, nFl: 12 },
  keerai:         { name: 'Keerai (Amaranth greens)', note: 'in the vegetable bed GD-07, cut every 3 weeks', h: 0.35, w: 0.4, leaf: [0.06, 0.04], leafC: '#5b8a2c', nLeaf: 110, fl: null },
  pudina:         { name: 'Pudina (Mint)', note: 'in the herb bed GD-09', h: 0.22, w: 0.45, leaf: [0.035, 0.024], leafC: '#4f8f3a', nLeaf: 200, fl: null },
  karpooravalli:  { name: 'Karpooravalli (Ajwain leaf)', note: 'in the herb bed GD-09, for coughs and colds', h: 0.32, w: 0.4, leaf: [0.05, 0.045], leafC: '#76a052', nLeaf: 110, fl: null },
  kothamalli:     { name: 'Kothamalli (Coriander)', note: 'in the herb bed GD-09, sow every month', h: 0.28, w: 0.35, leaf: [0.025, 0.02], leafC: '#5f9a3e', nLeaf: 180, fl: null },
  vallarai:       { name: 'Vallarai (Gotu kola)', note: 'in the herb bed GD-09, low and spreading', h: 0.15, w: 0.45, leaf: [0.03, 0.03], leafC: '#4c8a36', nLeaf: 120, fl: null },
  mullai:         { name: 'Mullai (Climbing jasmine)', note: 'on the wire trellis GD-05', h: 1.6, w: 1.2, leaf: [0.07, 0.035], leafC: '#2f5e2a', nLeaf: 480, fl: 'star', flC: '#fbfaf3', flR: 0.02, nFl: 90, cenC: '#f1ecc8', base: 0.05 },
  elumichai:      { name: 'Elumichai (Lemon)', note: 'in a big pot GD-11', h: 1.15, w: 0.75, leaf: [0.07, 0.035], leafC: '#2f6b2a', nLeaf: 330, fl: 'ball', flC: '#e3cf2a', flR: 0.03, nFl: 14, base: 0.3, trunk: true },
};

export function createTNPlant(THREE, mergeGeometries, opts = {}) {
  const sp = TN_PLANTS[opts.type] || TN_PLANTS.malli;
  let s = (opts.seed ?? 1) * 9301 + 49297;
  const rnd = () => (s = (s * 16807) % 2147483647) / 2147483647;
  const rr = (a, b) => a + (b - a) * rnd();
  const V = (x, y, z) => new THREE.Vector3(x, y, z);
  const stems = [], leaves = [], flowers = [], centres = [];
  const flat = g => (g.index ? g.toNonIndexed() : g);

  // leaf shape: pointed ellipse in the XY plane, base at the origin, tip on +Y
  const leafGeo = (L, W) => {
    const sh = new THREE.Shape();
    sh.moveTo(0, 0); sh.quadraticCurveTo(W, L * 0.45, 0, L); sh.quadraticCurveTo(-W, L * 0.45, 0, 0);
    return flat(new THREE.ShapeGeometry(sh, 3));
  };
  const LG = leafGeo(sp.leaf[0] * 1.6, sp.leaf[1] * 0.85);   // drawn a little larger than life so the bush reads full from a distance
  const place = (g, pos, dir, roll, sc = 1) => {
    const q = new THREE.Quaternion().setFromUnitVectors(V(0, 1, 0), dir.clone().normalize());
    q.multiply(new THREE.Quaternion().setFromAxisAngle(V(0, 1, 0), roll));
    const mtx = new THREE.Matrix4().compose(pos, q, V(sc, sc, sc));
    return g.clone().applyMatrix4(mtx);
  };
  const stem = (a, b, r) => {
    const d = new THREE.Vector3().subVectors(b, a), L = d.length();
    const g = new THREE.CylinderGeometry(r * 0.7, r, L, 5, 1, true); g.translate(0, L / 2, 0);
    g.applyQuaternion(new THREE.Quaternion().setFromUnitVectors(V(0, 1, 0), d.normalize())); g.translate(a.x, a.y, a.z);
    stems.push(flat(g));
  };

  // canopy envelope: an ellipsoid sitting on a short bare base
  const H = sp.h * rr(0.9, 1.1), R = sp.w / 2 * rr(0.9, 1.1), base = H * (sp.base ?? (opts.type === 'karuveppilai' ? 0.35 : 0.12)), woody = opts.type === 'karuveppilai' || sp.trunk;
  const cy = base + (H - base) * 0.55, ry = (H - base) * 0.5;
  const onShell = (k = 1) => { const t = rr(0, Math.PI * 2), u = rr(-0.55, 1); const c = Math.sqrt(1 - u * u);
    return V(Math.cos(t) * c * R * k, cy + u * ry * k, Math.sin(t) * c * R * k) };

  // branches from the base to points on the canopy shell
  const nB = woody ? 5 : Math.round(rr(6, 9)), tips = [];
  for (let i = 0; i < nB; i++) {
    const tip = onShell(rr(0.75, 0.95)), mid = V(tip.x * 0.45 + rr(-0.04, 0.04), base + (tip.y - base) * 0.5, tip.z * 0.45 + rr(-0.04, 0.04));
    const r0 = woody ? 0.016 : 0.006;
    stem(V(rr(-0.02, 0.02), 0, rr(-0.02, 0.02)), mid, r0); stem(mid, tip, r0 * 0.6); tips.push(tip);
  }
  if (woody) stem(V(0, 0, 0), V(0, base + 0.1, 0), 0.025);

  // leaves on the canopy, facing outward and a little up
  const cen = V(0, cy, 0);
  for (let i = 0; i < Math.round(sp.nLeaf * 1.8); i++) {
    const p = onShell(Math.sqrt(rr(0.45, 1)));
    const out = new THREE.Vector3().subVectors(p, cen).normalize();
    const dir = out.multiplyScalar(0.8).add(V(rr(-0.4, 0.4), rr(0.1, 0.6), rr(-0.4, 0.4)));
    leaves.push(place(LG, p, dir, rr(0, Math.PI * 2), rr(0.8, 1.25)));
  }

  // flowers on the outer shell (most face up and out)
  const petalGeo = (L, W) => leafGeo(L, W);
  const flowerAt = (p, out) => {
    const r = sp.flR * rr(0.85, 1.15), roll = rr(0, Math.PI * 2);
    const face = out.clone().add(V(0, 0.8, 0)).normalize();
    const q = new THREE.Quaternion().setFromUnitVectors(V(0, 1, 0), face);
    const add = (g, arr) => { g.applyQuaternion(q); g.translate(p.x, p.y, p.z); arr.push(g) };
    if (sp.fl === 'star' || sp.fl === 'hibiscus' || sp.fl === 'pinwheel') {
      const n = 5, pg = petalGeo(r, r * (sp.fl === 'pinwheel' ? 0.35 : 0.6));
      for (let k = 0; k < n; k++) {
        const g = pg.clone();
        g.rotateX(-Math.PI / 2 + (sp.fl === 'hibiscus' ? 0.5 : 0.15));   // petals open out, hibiscus cup-shaped
        if (sp.fl === 'pinwheel') g.rotateY(0.6);
        g.rotateY(roll + k * Math.PI * 2 / n); add(g, flowers);
      }
      if (sp.cenC) {
        const c = flat(new THREE.SphereGeometry(r * (sp.fl === 'hibiscus' ? 0.12 : 0.18), 5, 4));
        if (sp.fl === 'hibiscus') { const st = flat(new THREE.CylinderGeometry(r * 0.03, r * 0.03, r * 0.9, 4)); st.translate(0, r * 0.45, 0); add(st, centres); c.translate(0, r * 0.9, 0) }
        add(c, centres);
      }
    } else if (sp.fl === 'ball') {   // ixora: a dome of tiny 4-petal florets
      const g = flat(new THREE.IcosahedronGeometry(r, 1)); g.scale(1, 0.7, 1);
      const pos = g.attributes.position;
      for (let k = 0; k < pos.count; k++) { const f = 1 + 0.12 * Math.sin(k * 12.9898 + (opts.seed || 1)); pos.setXYZ(k, pos.getX(k) * f, pos.getY(k) * f, pos.getZ(k) * f) }
      g.computeVertexNormals(); add(g, flowers);
    } else if (sp.fl === 'spike') {  // crossandra / tulsi: a short upright spike of small flowers
      const n = 6;
      for (let k = 0; k < n; k++) {
        const g = flat(new THREE.SphereGeometry(r, 5, 3)); g.scale(1.3, 0.6, 1.3); g.translate(0, k * r * 1.6, 0);
        g.applyQuaternion(new THREE.Quaternion().setFromUnitVectors(V(0, 1, 0), V(0, 1, 0))); g.translate(p.x, p.y, p.z); flowers.push(g);
      }
    } else if (sp.fl === 'rose') {   // rosette of curled petals
      for (let k = 0; k < 10; k++) {
        const L = r * (0.6 + k * 0.05), g = petalGeo(L, L * 0.8);
        g.rotateX(-Math.PI / 2 + 1.1 - k * 0.08); g.rotateY(roll + k * 2.4); add(g, flowers);
      }
    }
  };
  if (sp.fl) for (let i = 0; i < sp.nFl; i++) {
    const p = onShell(rr(0.92, 1.05)); if (p.y < cy - ry * 0.3) p.y = cy + rr(-0.1, 0.9) * ry;
    flowerAt(p, new THREE.Vector3().subVectors(p, cen).normalize());
  }
  for (const t of tips) if (sp.fl && rnd() < 0.6) flowerAt(t.clone().add(V(0, 0.02, 0)), V(0, 1, 0));

  const g = new THREE.Group(); g.name = 'TNPlant_' + (opts.type || 'malli');
  const mk = (arr, mat, nm) => { if (!arr.length) return; const geo = mergeGeometries(arr); const me = new THREE.Mesh(geo, mat); me.name = nm; me.castShadow = true; me.receiveShadow = true; g.add(me) };
  mk(stems, new THREE.MeshStandardMaterial({ color: '#5a4630', roughness: 0.9 }), 'stems');
  mk(leaves, new THREE.MeshStandardMaterial({ color: sp.leafC, roughness: 0.55, side: THREE.DoubleSide }), 'leaves');
  mk(flowers, new THREE.MeshStandardMaterial({ color: sp.flC || '#fff', roughness: 0.6, side: THREE.DoubleSide }), 'flowers');
  mk(centres, new THREE.MeshStandardMaterial({ color: sp.cenC || '#fff', roughness: 0.6 }), 'centres');
  g.userData.species = sp;
  return g;
}
