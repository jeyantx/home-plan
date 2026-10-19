// Procedural models of real vehicles, to real sizes, for checking the parking.
//
//   import { createVirtus, createHunter350, createAther450 } from './models/vehicles.js';
//   const car = createVirtus(THREE, mergeGeometries, { color: '#2f5d8c' });
//
// Units: metres, +Y up. Origin = centre of the footprint at ground level. Front of the vehicle = +Z.
// The vehicle's left side is +X, so the driver (right-hand drive, India) sits on the -X side.
// Plain Mesh + merged BufferGeometry per material (no InstancedMesh, no external textures), so the path tracer can use them.
//
// Animation hooks (all Groups, origin at the pivot):
//   car.userData.wheels = {fl, fr, rl, rr}   spin with .rotation.x
//   car.userData.steer  = {fl, fr}           steer with .rotation.y (contain the front spin groups)
//   bike.userData.wheels = {f, r}            spin with .rotation.x
//   bike.userData.steer  = group             fork, front wheel, mudguard, bars, lamp: steer with .rotation.y (about the steering-head axis)
//   bike.userData.lean   = group             whole bike; .rotation.z = 0 stands it upright (default: leaning on the side stand)
//   bike.userData.stand  = group             side stand
//   *.userData.dims = {length, width, height}

const flat = g => (g.index ? g.toNonIndexed() : g);
function mesh(THREE, mergeGeometries, parts, mat, name, parent) {
  const geo = mergeGeometries(parts.map(flat));
  const me = new THREE.Mesh(geo, mat); me.name = name; me.castShadow = true; me.receiveShadow = true; parent.add(me); return me;
}
// side profile [[z, y], ...] extruded across the width (centred on x = 0), with rounded edges
function sideExtrude(THREE, pts, width, bevel = 0.03, seg = 3) {
  const sh = new THREE.Shape(pts.map(([z, y]) => new THREE.Vector2(z, y)));
  const g = new THREE.ExtrudeGeometry(sh, { depth: Math.max(0.001, width - 2 * bevel), bevelEnabled: bevel > 0, bevelThickness: bevel, bevelSize: bevel, bevelSegments: seg, curveSegments: 10 });
  g.translate(0, 0, -(width - 2 * bevel) / 2); g.rotateY(-Math.PI / 2); return g;
}
// tyre: lathe of a rounded section, axis along X, centred on the origin
function tyre(THREE, R, w, segs = 40) {
  const pts = [], r0 = R - Math.min(0.11, R * 0.38), k = 10;
  for (let i = 0; i <= k; i++) { const a = -Math.PI / 2 + Math.PI * i / k; pts.push(new THREE.Vector2(R - w * 0.32 * (1 - Math.cos(a)) * 0.5 - (R - r0) * 0 , w / 2 * Math.sin(a))) }
  const prof = [new THREE.Vector2(r0, -w / 2 * 0.92), ...pts.map(p => new THREE.Vector2(Math.max(r0 + 0.01, p.x), p.y)), new THREE.Vector2(r0, w / 2 * 0.92)];
  const g = new THREE.LatheGeometry(prof, segs); g.rotateZ(Math.PI / 2); return g;
}
// alloy wheel: rim lip, dish and n spokes, axis along X; side = +1 / -1 for which face points out
function alloy(THREE, r, w, n, side) {
  const parts = [];
  const lip = new THREE.CylinderGeometry(r, r, w * 0.9, 32, 1, true); lip.rotateZ(Math.PI / 2); parts.push(lip);
  const hub = new THREE.CylinderGeometry(r * 0.2, r * 0.22, w * 0.5, 16); hub.rotateZ(Math.PI / 2); hub.translate(side * w * 0.2, 0, 0); parts.push(hub);
  for (let i = 0; i < n; i++) {
    const a = i * Math.PI * 2 / n, sp = new THREE.BoxGeometry(w * 0.18, r * 0.8, r * 0.13);
    sp.translate(0, r * 0.55, 0); sp.rotateX(a); sp.translate(side * w * 0.3, 0, 0); parts.push(sp);
  }
  return parts;
}

// ======================================================= VW Virtus =======================================================
export function createVirtus(THREE, mergeGeometries, opts = {}) {
  const L = 4.561, W = 1.752, H = 1.507, WB = 2.651, R = 0.316, h = L / 2;
  const zF = WB / 2 + 0.07, zR = -WB / 2 + 0.07;   // front and rear axle (front overhang a little longer)
  const zWs = zF - 0.35, zRoofF = zWs - 0.8, zRoofR = -0.8, zRs = -h + 0.85;   // windscreen base, roof front and back, rear-screen base (3-box sedan)
  const g = new THREE.Group(); g.name = 'VW Virtus';
  const paint = new THREE.MeshPhysicalMaterial({ color: opts.color ?? '#9ea3a8', roughness: 0.28, metalness: 0.55, clearcoat: 1, clearcoatRoughness: 0.06 });
  const glass = new THREE.MeshPhysicalMaterial({ color: '#141a20', roughness: 0.05, metalness: 0.2, clearcoat: 1, clearcoatRoughness: 0.03 });
  const black = new THREE.MeshStandardMaterial({ color: '#141518', roughness: 0.6 });
  const gloss = new THREE.MeshStandardMaterial({ color: '#0d0e10', roughness: 0.15, metalness: 0.3 });
  const chrome = new THREE.MeshStandardMaterial({ color: '#d9dde1', roughness: 0.12, metalness: 1 });
  const alloyM = new THREE.MeshStandardMaterial({ color: '#b8bcc1', roughness: 0.3, metalness: 0.85 });
  const rubber = new THREE.MeshStandardMaterial({ color: '#1a1b1d', roughness: 0.92 });
  const lampW = new THREE.MeshPhysicalMaterial({ color: '#e9eef2', roughness: 0.05, metalness: 0.4, emissive: '#fff4dd', emissiveIntensity: 0.25, clearcoat: 1 });
  const lampR = new THREE.MeshPhysicalMaterial({ color: '#9d0c16', roughness: 0.1, emissive: '#5a0610', emissiveIntensity: 0.35, clearcoat: 1 });
  const plateM = new THREE.MeshStandardMaterial({ color: '#f3f3ee', roughness: 0.5 });

  // ---- lower body: lofted rounded-rectangle sections from the rear bumper to the nose, wrapped over the wheels ----
  const smooth = (a, b, x) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t) };
  const lerp = (a, b, t) => a + (b - a) * t;
  const halfW = z => { const e = Math.abs(z), zs = h - 0.42; const base = W / 2 * (z > 0 ? 1 : 0.985);
    if (e <= zs) return base; const u = (e - zs) / (h - zs); return base * (0.8 + 0.2 * Math.pow(1 - Math.pow(u, 2.2), 1 / 2.2)) };
  const topY = z => {   // bonnet / belt / boot-deck line
    if (z > h - 0.25) return lerp(0.7, 0.8, smooth(h, h - 0.25, z));
    if (z > zWs) return lerp(0.8, 0.97, smooth(h - 0.25, zWs, z));                  // bonnet rising to the windscreen
    if (z > zRs) return lerp(0.975, 1.03, smooth(zWs, zRs, z));                      // rising belt line
    if (z > -h + 0.12) return lerp(1.035, 1.045, smooth(zRs, -h + 0.12, z));          // flat boot deck
    return lerp(1.045, 0.95, smooth(-h + 0.12, -h, z));                              // boot lid edge down to the rear
  };
  const botY = z => { const e = Math.abs(z); return e > h - 0.5 ? lerp(0.2, 0.33, smooth(h - 0.5, h, e)) : 0.2 };
  const arch = (z, y) => {   // lift points under a wheel arch up to the arch line, so the wheel shows below it
    for (const zc of [zF, zR]) { const dz = z - zc, RA = R + 0.07;
      if (Math.abs(dz) < RA) { const ya = R + Math.sqrt(RA * RA - dz * dz); if (y < ya) return [z, ya] } }
    return [z, y] };
  // indexed loft (smooth normals) through rings of equal point count; flips itself to face outward from the axis line y = yAxis
  const loft = (rings, mat, name, yAxis) => {
    const rows = rings.length, cols = rings[0].length, P = [], UV = [], I = [];
    rings.forEach((r, i) => r.forEach(([x, y, z], j) => { P.push(x, y, z); UV.push(z, y) }));
    for (let i = 0; i < rows - 1; i++) for (let j = 0; j < cols - 1; j++) { const a = i * cols + j, b = a + 1, c = a + cols + 1, d = a + cols; I.push(a, b, c, a, c, d) }
    const geo = new THREE.BufferGeometry(); geo.setAttribute('position', new THREE.Float32BufferAttribute(P, 3)); geo.setAttribute('uv', new THREE.Float32BufferAttribute(UV, 2)); geo.setIndex(I); geo.computeVertexNormals();
    const nn = geo.attributes.normal; let f = 0; for (let k = 0; k < nn.count; k++) f += nn.getX(k) * P[3 * k] + nn.getY(k) * (P[3 * k + 1] - yAxis);
    if (f < 0) { for (let k = 0; k < I.length; k += 3) { const t = I[k + 1]; I[k + 1] = I[k + 2]; I[k + 2] = t } geo.setIndex(I); geo.computeVertexNormals() }
    const me = new THREE.Mesh(geo, mat); me.name = name; me.castShadow = true; me.receiveShadow = true; g.add(me); return me };
  const NS = 130, NC = 48, n = 4.2;
  const ring = (z, k = 1, dz = 0) => { const w = halfW(z) * k, yb = botY(z), yt = topY(z), yc = (yb + yt) / 2, hy = (yt - yb) / 2 * k, out = [];
    for (let j = 0; j <= NC; j++) { const a = 2 * Math.PI * j / NC, c = Math.cos(a), sn = Math.sin(a);
      let x = w * Math.sign(c) * Math.pow(Math.abs(c), 2 / n), y = yc + hy * Math.sign(sn) * Math.pow(Math.abs(sn), 2 / (sn > 0 ? n * 0.8 : n * 1.4));
      if (sn > 0) x *= 1 - 0.06 * Math.pow(sn, 4);   // slight tumblehome at the shoulder
      let zz = z + dz; if (k === 1 && Math.abs(x) > w * 0.55) [zz, y] = arch(z, y); out.push([x, y, zz]) }
    return out };
  const rings = [];
  for (const [k, d] of [[0.3, -0.03], [0.75, -0.026], [0.9, -0.017], [0.97, -0.007]]) rings.push(ring(-h, k, d));   // rounded tail
  for (let i = 0; i <= NS; i++) { const t = i / NS; rings.push(ring(-h + L * (0.5 - 0.5 * Math.cos(Math.PI * t)))) }
  for (const [k, d] of [[0.97, 0.007], [0.9, 0.017], [0.75, 0.026], [0.3, 0.03]]) rings.push(ring(h, k, d));       // rounded nose
  loft(rings, paint, 'body', 0.55);

  // ---- greenhouse: windscreen, side glass, rear screen; roof panel in body colour ----
  const yRoof = H;
  const roofY = z => z > zRoofF ? lerp(yRoof - 0.02, topY(zWs) - 0.01, smooth(zRoofF, zWs, z)) : z > zRoofR ? yRoof - 0.02 * Math.pow((z - (zRoofF + zRoofR) / 2) / ((zRoofF - zRoofR) / 2), 2) : lerp(yRoof - 0.02, topY(zRs) - 0.01, smooth(zRoofR, zRs, z));
  const GS = 80, GC = 24;
  const gring = (z, lift = 0, uMin = 0, uMax = 1) => { const yb = topY(z) - 0.015, yt = roofY(z) + lift, wb = halfW(z) * 0.93 + lift, wt = halfW(z) * 0.7 + lift, out = [];
    for (let j = 0; j <= GC; j++) { const u = uMin + (uMax - uMin) * j / GC, sgn = u < 0.5 ? -1 : 1, s = Math.abs(2 * u - 1); let x, y;
      if (s > 0.36) { const t = (1 - s) / 0.64; x = lerp(wb, wt, t); y = lerp(yb, yt - 0.07, Math.pow(t, 0.9)) } else { const q = s / 0.36; x = wt * q; y = yt - 0.07 * q * q }
      out.push([sgn * x, Math.min(y, yt), z]) }
    return out };
  const grings = []; for (let i = 0; i <= GS; i++) grings.push(gring(lerp(zWs, zRs, i / GS)));
  loft(grings, glass, 'glass', 0.9);
  const rr = []; for (let i = 0; i <= 30; i++) rr.push(gring(lerp(zRoofF - 0.04, zRoofR + 0.04, i / 30), 0.015, 0.22, 0.78));
  loft(rr, paint, 'roof', 0.9);

  // ---- pillars, window chrome, door gaps, handles, mirrors ----
  const blk = [], chr = [], pnt = [];
  const B = (w, hh, d, x, y, z, arr, rx = 0, ry = 0, rz = 0) => { const b = new THREE.BoxGeometry(w, hh, d); b.rotateX(rx); b.rotateY(ry); b.rotateZ(rz); b.translate(x, y, z); arr.push(b) };
  const zB = (zWs + zRs) / 2 + 0.12;   // B-pillar
  for (const s of [-1, 1]) {
    const xb = s * halfW(zB) * 0.9, yb = topY(zB), yt = roofY(zB);
    // chrome window line along the belt
    const zs = [zWs - 0.1, zRs + 0.12]; B(0.012, 0.018, zs[0] - zs[1], s * halfW(0) * 0.945, topY(0) + 0.005, (zs[0] + zs[1]) / 2, chr);
    // door gaps (front door, rear door) and handles
    for (const zz of [zWs - 0.05, zB + 0.02, zB - 0.02, zRs + 0.25]) B(0.004, topY(zz) - 0.32, 0.006, s * (halfW(zz) + 0.001), (topY(zz) + 0.32) / 2 + 0.02, zz, blk);
    for (const zz of [zB + 0.12, zB - 0.82]) B(0.02, 0.025, 0.16, s * (halfW(zz) + 0.008), topY(zz) - 0.1, zz, pnt);
    // mirror on the front door
    B(0.2, 0.11, 0.09, s * (W / 2 + 0.08), topY(zWs) + 0.08, zWs - 0.12, pnt, 0, s * 0.15); B(0.08, 0.04, 0.05, s * (W / 2 + 0.01), topY(zWs) + 0.04, zWs - 0.1, blk);
  }
  // ---- front: grille with the chrome bar, slim LED headlamps, lower intake, plate ----
  B(halfW(h) * 1.45, 0.014, 0.02, 0, topY(h) - 0.035, h + 0.03, chr);
  const lampsW = [], lampsR = [];
  { const wF = halfW(h) * 0.8, wR = halfW(-h) * 0.8, yF = topY(h) - 0.07, yRr = topY(-h) - 0.07;
    for (const sg of [-1, 1]) { const lw = wF - 0.3; lampsW.push(new THREE.BoxGeometry(lw, 0.06, 0.03).translate(sg * (0.3 + lw / 2), yF, h + 0.022));
      const rw = wR - 0.2; lampsR.push(new THREE.BoxGeometry(rw, 0.085, 0.03).translate(sg * (0.2 + rw / 2), yRr, -h - 0.022)) }
    lampsR.push(new THREE.BoxGeometry(0.4, 0.025, 0.03).translate(0, yRr + 0.02, -h - 0.032)) }   // light bar across the boot lid
  B(W * 0.5, 0.11, 0.04, 0, 0.36, h + 0.02, blk);                 // lower intake
  for (const s of [-1, 1]) B(0.14, 0.05, 0.04, s * (halfW(h) * 0.72), 0.38, h + 0.005, blk);   // fog lamp bezels
  // ---- rear: tail lamps joined across the boot lid, plate recess, diffuser ----
  B(W * 0.5, 0.1, 0.04, 0, 0.36, -h - 0.02, blk);
  const plates = []; B(0.52, 0.12, 0.012, 0, 0.5, h + 0.034, plates); B(0.52, 0.12, 0.012, 0, 0.66, -h - 0.034, plates);
  mesh(THREE, mergeGeometries, blk, black, 'trim', g); mesh(THREE, mergeGeometries, chr, chrome, 'chrome', g); mesh(THREE, mergeGeometries, pnt, paint, 'mirrors and handles', g);
  mesh(THREE, mergeGeometries, lampsW, lampW, 'headlamps', g); mesh(THREE, mergeGeometries, lampsR, lampR, 'tail lamps', g); mesh(THREE, mergeGeometries, plates, plateM, 'number plates', g);
  mesh(THREE, mergeGeometries, [new THREE.BoxGeometry(W * 0.42, 0.09, 0.03).translate(0, topY(h) - 0.075, h + 0.028)], gloss, 'grille', g);
  // dark arch liners so the arches read as openings
  for (const zc of [zF, zR]) for (const s of [-1, 1]) { const al = new THREE.CylinderGeometry(R + 0.05, R + 0.05, 0.3, 28, 1, true, 0, Math.PI); al.rotateZ(Math.PI / 2); al.rotateX(-Math.PI / 2); al.translate(s * (W / 2 - 0.2), R, zc);
    mesh(THREE, mergeGeometries, [al], new THREE.MeshStandardMaterial({ color: '#0b0b0c', roughness: 0.95, side: THREE.DoubleSide }), 'arch liner', g) }

  // ---- wheels: steer + spin groups ----
  const wheels = {}, steer = {};
  const mkWheel = (x, z, side) => { const spin = new THREE.Group(); spin.name = 'wheel spin';
    mesh(THREE, mergeGeometries, [tyre(THREE, R, 0.205)], rubber, 'tyre', spin);
    mesh(THREE, mergeGeometries, alloy(THREE, 0.2, 0.18, 10, side), alloyM, 'alloy wheel', spin);
    const disc = new THREE.CylinderGeometry(0.15, 0.15, 0.02, 24); disc.rotateZ(Math.PI / 2); disc.translate(-side * 0.04, 0, 0);
    mesh(THREE, mergeGeometries, [disc], new THREE.MeshStandardMaterial({ color: '#6d6f72', roughness: 0.4, metalness: 0.8 }), 'brake disc', spin);
    return spin };
  const track = W / 2 - 0.17;
  for (const [key, x, z, s] of [['fl', track, zF, 1], ['fr', -track, zF, -1], ['rl', track, zR, 1], ['rr', -track, zR, -1]]) {
    const sp = mkWheel(x, z, s);
    if (key[0] === 'f') { const st = new THREE.Group(); st.name = 'steer ' + key; st.position.set(x, R, z); st.add(sp); g.add(st); steer[key] = st }
    else { sp.position.set(x, R, z); g.add(sp) }
    wheels[key] = sp }
  g.userData.wheels = wheels; g.userData.steer = steer; g.userData.dims = { length: L, width: W, height: H };
  return g;
}

// ===================================================== two-wheelers =====================================================
function bikeShell(THREE, name) {
  const g = new THREE.Group(); g.name = name;
  const lean = new THREE.Group(); lean.name = 'lean'; g.add(lean);
  return { g, lean };
}
function bikeWheel(THREE, mergeGeometries, R, w, spokes, mats, parent, z) {
  const spin = new THREE.Group(); spin.position.set(0, R, z); parent.add(spin);
  mesh(THREE, mergeGeometries, [tyre(THREE, R, w, 36)], mats.rubber, 'tyre', spin);
  const rim = R - Math.min(0.11, R * 0.38);
  mesh(THREE, mergeGeometries, [...alloy(THREE, rim, w * 0.7, spokes, 1)], mats.alloy, 'alloy wheel', spin);
  const disc = new THREE.CylinderGeometry(rim * 0.62, rim * 0.62, 0.006, 24); disc.rotateZ(Math.PI / 2); disc.translate(-w * 0.42, 0, 0);
  mesh(THREE, mergeGeometries, [disc], mats.steel, 'brake disc', spin);
  return spin;
}
// steering group about a raked axis through the head point (rake measured from vertical, leaning back)
function steerGroup(THREE, parent, head, rake) {
  const axis = new THREE.Group(); axis.position.set(0, head[1], head[0]); axis.rotation.x = -rake; parent.add(axis);
  const st = new THREE.Group(); st.name = 'steer'; axis.add(st); return st;
}
const tube = (THREE, pts, r, seg = 24) => new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts.map(p => new THREE.Vector3(...p))), seg, r, 8, false);
const box = (THREE, w, h, d, x, y, z, rx = 0, ry = 0, rz = 0) => { const b = new THREE.BoxGeometry(w, h, d); b.rotateX(rx); b.rotateY(ry); b.rotateZ(rz); b.translate(x, y, z); return b };
const cyl = (THREE, r1, r2, len, x, y, z, rx = 0, rz = 0, seg = 16) => { const c = new THREE.CylinderGeometry(r1, r2, len, seg); c.rotateX(rx); c.rotateZ(rz); c.translate(x, y, z); return c };
function finishBike(THREE, g, lean, stand, steer, wheels, dims) {
  // move steer children (built in bike coordinates) into the steering frame, keeping where they are
  g.updateMatrixWorld(true);
  for (const o of [...steer.userData.pending]) steer.attach(o);
  delete steer.userData.pending;
  lean.rotation.z = -0.085;   // ~5 deg onto the side stand (vehicle's left, +X)
  g.userData.lean = lean; g.userData.stand = stand; g.userData.steer = steer; g.userData.wheels = wheels; g.userData.dims = dims;
  return g;
}

// ------------------------------------------------ Royal Enfield Hunter 350 ------------------------------------------------
export function createHunter350(THREE, mergeGeometries, opts = {}) {
  const { g, lean } = bikeShell(THREE, 'Royal Enfield Hunter 350');
  const R = 0.31, zf = 0.66, zr = -0.71, head = [0.45, 0.93], rake = 0.44;
  const mats = { rubber: new THREE.MeshStandardMaterial({ color: '#19191b', roughness: 0.92 }), alloy: new THREE.MeshStandardMaterial({ color: '#2a2b2e', roughness: 0.35, metalness: 0.7 }),
    steel: new THREE.MeshStandardMaterial({ color: '#8e9296', roughness: 0.35, metalness: 0.9 }) };
  const paint = new THREE.MeshPhysicalMaterial({ color: opts.color ?? '#2c4a6e', roughness: 0.3, metalness: 0.35, clearcoat: 1, clearcoatRoughness: 0.08 });
  const paint2 = new THREE.MeshPhysicalMaterial({ color: '#e9e6df', roughness: 0.3, metalness: 0.2, clearcoat: 1 });
  const black = new THREE.MeshStandardMaterial({ color: '#141416', roughness: 0.55, metalness: 0.2 });
  const chrome = new THREE.MeshStandardMaterial({ color: '#dfe2e5', roughness: 0.1, metalness: 1 });
  const alu = new THREE.MeshStandardMaterial({ color: '#b9bcbf', roughness: 0.3, metalness: 0.9 });
  const seatM = new THREE.MeshStandardMaterial({ color: '#2a2420', roughness: 0.75 });
  const wheels = { r: bikeWheel(THREE, mergeGeometries, R, 0.14, 6, mats, lean, zr) };
  const steer = steerGroup(THREE, lean, head, rake); steer.userData.pending = [];
  const front = new THREE.Group(); lean.add(front); steer.userData.pending.push(front);
  wheels.f = bikeWheel(THREE, mergeGeometries, R, 0.11, 6, mats, front, zf);
  // frame: backbone, down tubes, rear subframe (black)
  const frame = [tube(THREE, [[0, head[1] + 0.02, head[0] - 0.02], [0, 0.86, 0.15], [0, 0.78, -0.25], [0, 0.72, -0.65]], 0.024),
    ...[-1, 1].map(s => tube(THREE, [[s * 0.05, head[1] - 0.05, head[0] - 0.03], [s * 0.07, 0.42, 0.33], [s * 0.08, 0.2, 0.1], [s * 0.08, 0.24, -0.2], [s * 0.1, 0.42, -0.3], [s * 0.11, 0.72, -0.62]], 0.016)),
    ...[-1, 1].map(s => box(THREE, 0.03, 0.05, 0.62, s * 0.11, 0.3, -0.46, -0.03)),          // swingarm
    ...[-1, 1].map(s => cyl(THREE, 0.018, 0.018, 0.4, s * 0.115, 0.5, -0.66, 0.35)),         // twin rear shocks
    box(THREE, 0.24, 0.03, 0.3, 0, 0.72, -0.7, -0.15)];
  mesh(THREE, mergeGeometries, frame, black, 'frame, swingarm and shocks', lean);
  mesh(THREE, mergeGeometries, [...[-1, 1].map(s => cyl(THREE, 0.026, 0.026, 0.12, s * 0.115, 0.36, -0.6, 0.35, 0, 10))], new THREE.MeshStandardMaterial({ color: '#c8a23a', roughness: 0.4, metalness: 0.6 }), 'shock springs', lean);
  // engine: crankcase with polished covers, finned barrel, head
  const eng = [box(THREE, 0.2, 0.26, 0.42, 0, 0.37, 0.06)];
  const fins = []; for (let i = 0; i < 7; i++) fins.push(box(THREE, 0.2 - i * 0.004, 0.012, 0.19, 0, 0.53 + i * 0.03, 0.2, 0.18));
  mesh(THREE, mergeGeometries, [...eng, ...fins, box(THREE, 0.17, 0.08, 0.16, 0, 0.75, 0.24, 0.18)], new THREE.MeshStandardMaterial({ color: '#3a3b3e', roughness: 0.5, metalness: 0.6 }), 'engine', lean);
  mesh(THREE, mergeGeometries, [...[-1, 1].map(s => { const c = new THREE.CylinderGeometry(0.11, 0.11, 0.03, 24); c.rotateZ(Math.PI / 2); c.translate(s * 0.115, 0.36, 0.04); return c }),
    (() => { const c = new THREE.CylinderGeometry(0.07, 0.07, 0.03, 20); c.rotateZ(Math.PI / 2); c.translate(0.115, 0.33, 0.2); return c })()], alu, 'engine covers', lean);
  // exhaust: header from the head down the right side to a short silencer
  mesh(THREE, mergeGeometries, [tube(THREE, [[-0.04, 0.68, 0.31], [-0.1, 0.5, 0.38], [-0.14, 0.24, 0.2], [-0.15, 0.22, -0.15], [-0.16, 0.32, -0.42]], 0.022),
    cyl(THREE, 0.045, 0.038, 0.42, -0.16, 0.37, -0.6, Math.PI / 2 - 0.25)], chrome, 'exhaust', lean);
  // teardrop tank (two-tone), side panels, seat, short rear fender, round tail lamp
  const tank = new THREE.SphereGeometry(0.2, 28, 18); tank.scale(0.62, 0.55, 1.12); tank.translate(0, 0.9, 0.18);
  const tank2 = new THREE.SphereGeometry(0.2, 28, 18); tank2.scale(0.635, 0.3, 0.95); tank2.translate(0, 0.86, 0.15);
  mesh(THREE, mergeGeometries, [tank], paint, 'fuel tank', lean); mesh(THREE, mergeGeometries, [tank2], paint2, 'fuel tank band', lean);
  mesh(THREE, mergeGeometries, [box(THREE, 0.24, 0.16, 0.24, 0, 0.62, -0.14)], black, 'side panels', lean);
  mesh(THREE, mergeGeometries, [sideExtrude(THREE, [[0.02, 0.77], [-0.06, 0.8], [-0.62, 0.79], [-0.7, 0.75], [-0.6, 0.74], [-0.02, 0.74]], 0.26, 0.03)], seatM, 'seat', lean);
  mesh(THREE, mergeGeometries, [sideExtrude(THREE, [[-0.66, 0.72], [-0.92, 0.66], [-1.0, 0.56], [-0.97, 0.55], [-0.89, 0.63], [-0.66, 0.69]], 0.16, 0.012)], paint, 'rear fender', lean);
  mesh(THREE, mergeGeometries, [cyl(THREE, 0.045, 0.045, 0.04, 0, 0.66, -0.98, Math.PI / 2)], new THREE.MeshPhysicalMaterial({ color: '#9d0c16', emissive: '#5a0610', emissiveIntensity: 0.3, roughness: 0.1 }), 'tail lamp', lean);
  mesh(THREE, mergeGeometries, [box(THREE, 0.2, 0.11, 0.008, 0, 0.5, -1.0, -0.2)], new THREE.MeshStandardMaterial({ color: '#f3f3ee', roughness: 0.5 }), 'number plate', lean);
  mesh(THREE, mergeGeometries, [...[-1, 1].map(s => box(THREE, 0.08, 0.02, 0.05, s * 0.18, 0.3, -0.05))], black, 'foot pegs', lean);
  // front: forks with gaiters, round headlamp with a chrome ring, mudguard, flat bar, round mirrors
  const fk = [], fkc = [];
  for (const s of [-1, 1]) { fk.push(cyl(THREE, 0.024, 0.024, 0.42, s * 0.08, 0.5, 0.6, -rake)); fkc.push(cyl(THREE, 0.018, 0.018, 0.3, s * 0.08, 0.83, 0.48, -rake)) }
  mesh(THREE, mergeGeometries, fk, black, 'fork gaiters', front); mesh(THREE, mergeGeometries, fkc, chrome, 'fork tubes', front);
  mesh(THREE, mergeGeometries, [cyl(THREE, 0.085, 0.07, 0.12, 0, 0.92, 0.6, Math.PI / 2 - 0.1, 0, 24)], black, 'headlamp shell', front);
  mesh(THREE, mergeGeometries, [(() => { const t = new THREE.TorusGeometry(0.083, 0.008, 8, 28); t.rotateX(-0.1); t.translate(0, 0.92, 0.665); return t })()], chrome, 'headlamp ring', front);
  mesh(THREE, mergeGeometries, [cyl(THREE, 0.078, 0.078, 0.005, 0, 0.92, 0.668, Math.PI / 2 - 0.1, 0, 24)], new THREE.MeshPhysicalMaterial({ color: '#eef2f5', emissive: '#fff4dd', emissiveIntensity: 0.25, roughness: 0.05, clearcoat: 1 }), 'headlamp', front);
  mesh(THREE, mergeGeometries, [(() => { const t = new THREE.TorusGeometry(R + 0.03, 0.05, 6, 20, 1.4); t.scale(1, 1, 1); t.rotateY(Math.PI / 2); t.rotateX(-0.25); t.translate(0, R, zf); return t })()], paint, 'front mudguard', front);
  mesh(THREE, mergeGeometries, [tube(THREE, [[-0.39, 1.0, 0.32], [-0.2, 1.0, 0.36], [0, 1.0, 0.37], [0.2, 1.0, 0.36], [0.39, 1.0, 0.32]], 0.011), ...[-1, 1].map(s => cyl(THREE, 0.016, 0.016, 0.11, s * 0.36, 1.0, 0.33, 0, Math.PI / 2))], black, 'handlebar and grips', front);
  mesh(THREE, mergeGeometries, [...[-1, 1].map(s => cyl(THREE, 0.006, 0.006, 0.16, s * 0.27, 1.0, 0.34, 0, s * 0.3)), ...[-1, 1].map(s => cyl(THREE, 0.045, 0.045, 0.02, s * 0.3, 1.035, 0.34, Math.PI / 2))], chrome, 'mirrors', front);
  mesh(THREE, mergeGeometries, [cyl(THREE, 0.05, 0.05, 0.05, 0, 1.0, 0.45, Math.PI / 2 - 0.4, 0, 20)], black, 'instrument pod', front);
  // side stand (left, +X)
  const stand = new THREE.Group(); lean.add(stand); mesh(THREE, mergeGeometries, [tube(THREE, [[0.12, 0.27, -0.06], [0.2, 0.13, -0.02], [0.26, 0.01, 0.04]], 0.012, 8)], black, 'side stand', stand);
  return finishBike(THREE, g, lean, stand, steer, wheels, { length: 2.055, width: 0.8, height: 1.055 });
}

// ------------------------------------------------------- Ather 450X -------------------------------------------------------
export function createAther450(THREE, mergeGeometries, opts = {}) {
  const { g, lean } = bikeShell(THREE, 'Ather 450X');
  const R = 0.225, zf = 0.62, zr = -0.676, head = [0.5, 0.92], rake = 0.42;
  const mats = { rubber: new THREE.MeshStandardMaterial({ color: '#19191b', roughness: 0.92 }), alloy: new THREE.MeshStandardMaterial({ color: '#202124', roughness: 0.35, metalness: 0.7 }),
    steel: new THREE.MeshStandardMaterial({ color: '#8e9296', roughness: 0.35, metalness: 0.9 }) };
  const paint = new THREE.MeshPhysicalMaterial({ color: opts.color ?? '#5f646b', roughness: 0.35, metalness: 0.4, clearcoat: 0.9, clearcoatRoughness: 0.1 });
  const dark = new THREE.MeshStandardMaterial({ color: '#1b1c1f', roughness: 0.55, metalness: 0.15 });
  const accent = new THREE.MeshStandardMaterial({ color: '#d9dadc', roughness: 0.4 });
  const seatM = new THREE.MeshStandardMaterial({ color: '#232326', roughness: 0.8 });
  const wheels = { r: bikeWheel(THREE, mergeGeometries, R, 0.12, 5, mats, lean, zr) };
  const steer = steerGroup(THREE, lean, head, rake); steer.userData.pending = [];
  const front = new THREE.Group(); lean.add(front); steer.userData.pending.push(front);
  wheels.f = bikeWheel(THREE, mergeGeometries, R, 0.1, 5, mats, front, zf);
  // floorboard, angular rear body, seat, under-seat dark panel, grab rail, tail lamp
  mesh(THREE, mergeGeometries, [sideExtrude(THREE, [[0.42, 0.24], [-0.16, 0.24], [-0.2, 0.33], [0.38, 0.33]], 0.4, 0.02)], dark, 'floorboard', lean);
  mesh(THREE, mergeGeometries, [sideExtrude(THREE, [[-0.12, 0.32], [-0.6, 0.38], [-0.9, 0.58], [-0.92, 0.66], [-0.78, 0.74], [-0.08, 0.74], [-0.02, 0.6]], 0.44, 0.05, 2)], paint, 'rear body', lean);
  mesh(THREE, mergeGeometries, [sideExtrude(THREE, [[-0.6, 0.38], [-0.26, 0.32], [-0.2, 0.5], [-0.62, 0.52]], 0.452, 0.01)], dark, 'side panel', lean);
  mesh(THREE, mergeGeometries, [sideExtrude(THREE, [[-0.06, 0.74], [-0.78, 0.74], [-0.84, 0.77], [-0.74, 0.795], [-0.1, 0.785], [-0.04, 0.76]], 0.34, 0.03)], seatM, 'seat', lean);
  mesh(THREE, mergeGeometries, [sideExtrude(THREE, [[-0.86, 0.6], [-0.93, 0.64], [-0.92, 0.67], [-0.85, 0.64]], 0.3, 0.01)], new THREE.MeshPhysicalMaterial({ color: '#9d0c16', emissive: '#5a0610', emissiveIntensity: 0.35, roughness: 0.1 }), 'tail lamp', lean);
  mesh(THREE, mergeGeometries, [tube(THREE, [[0.17, 0.8, -0.45], [0.18, 0.82, -0.72], [0, 0.83, -0.8], [-0.18, 0.82, -0.72], [-0.17, 0.8, -0.45]], 0.012)], dark, 'grab rail', lean);
  mesh(THREE, mergeGeometries, [sideExtrude(THREE, [[-0.58, 0.36], [-0.86, 0.5], [-0.98, 0.3], [-0.95, 0.27], [-0.86, 0.4], [-0.62, 0.3]], 0.12, 0.01)], dark, 'rear mudguard', lean);
  mesh(THREE, mergeGeometries, [box(THREE, 0.18, 0.1, 0.008, 0, 0.42, -0.97, -0.6)], new THREE.MeshStandardMaterial({ color: '#f3f3ee', roughness: 0.5 }), 'number plate', lean);
  mesh(THREE, mergeGeometries, [cyl(THREE, 0.02, 0.02, 0.32, -0.1, 0.38, -0.5, 0.9)], new THREE.MeshStandardMaterial({ color: '#c8a23a', roughness: 0.4, metalness: 0.6 }), 'mono shock', lean);
  // front: apron with the slim LED headlamp, knee guard, fork, mudguard, bar with the upright dashboard
  mesh(THREE, mergeGeometries, [sideExtrude(THREE, [[0.36, 0.3], [0.62, 0.55], [0.7, 0.86], [0.62, 0.98], [0.5, 1.0], [0.44, 0.7], [0.32, 0.36]], 0.5, 0.05, 2)], paint, 'front apron', lean);
  mesh(THREE, mergeGeometries, [sideExtrude(THREE, [[0.32, 0.36], [0.44, 0.7], [0.48, 0.96], [0.42, 0.97], [0.36, 0.7], [0.26, 0.4]], 0.46, 0.02)], dark, 'knee guard', lean);
  mesh(THREE, mergeGeometries, [sideExtrude(THREE, [[0.69, 0.8], [0.72, 0.86], [0.7, 0.88], [0.665, 0.82]], 0.3, 0.008)], new THREE.MeshPhysicalMaterial({ color: '#eef2f5', emissive: '#fff4dd', emissiveIntensity: 0.3, roughness: 0.05, clearcoat: 1 }), 'LED headlamp', lean);
  mesh(THREE, mergeGeometries, [cyl(THREE, 0.025, 0.025, 0.42, 0.06, 0.45, 0.6, -rake)], mats.steel, 'front fork', front);
  mesh(THREE, mergeGeometries, [sideExtrude(THREE, [[0.42, 0.42], [0.62, 0.48], [0.82, 0.38], [0.84, 0.34], [0.62, 0.43], [0.44, 0.38]], 0.13, 0.01)], paint, 'front mudguard', front);
  mesh(THREE, mergeGeometries, [tube(THREE, [[-0.35, 1.02, 0.47], [0, 1.03, 0.5], [0.35, 1.02, 0.47]], 0.012), ...[-1, 1].map(s => cyl(THREE, 0.017, 0.017, 0.11, s * 0.31, 1.02, 0.47, 0, Math.PI / 2)), box(THREE, 0.24, 0.05, 0.08, 0, 1.01, 0.5)], dark, 'handlebar and grips', front);
  mesh(THREE, mergeGeometries, [box(THREE, 0.2, 0.12, 0.025, 0, 1.08, 0.53, -0.35)], new THREE.MeshPhysicalMaterial({ color: '#0a0c0e', roughness: 0.05, clearcoat: 1, emissive: '#16324a', emissiveIntensity: 0.25 }), 'TFT dashboard', front);
  mesh(THREE, mergeGeometries, [...[-1, 1].map(s => cyl(THREE, 0.006, 0.006, 0.15, s * 0.25, 1.08, 0.46, 0, s * 0.35)), ...[-1, 1].map(s => box(THREE, 0.09, 0.05, 0.015, s * 0.29, 1.12, 0.46))], dark, 'mirrors', front);
  mesh(THREE, mergeGeometries, [box(THREE, 0.5, 0.012, 0.02, 0, 0.87, 0.705)], accent, 'apron trim', lean);
  const stand = new THREE.Group(); lean.add(stand); mesh(THREE, mergeGeometries, [tube(THREE, [[0.15, 0.26, 0.05], [0.21, 0.13, 0.08], [0.25, 0.01, 0.12]], 0.012, 8)], dark, 'side stand', stand);
  return finishBike(THREE, g, lean, stand, steer, wheels, { length: 1.837, width: 0.739, height: 1.114 });
}

export const createCar = createVirtus, createMotorbike = createHunter350, createScooter = createAther450;

// ---------------------------------------------------------------------------------------------------------------------------
// Downloaded car model (Free3D "Compact Car (Generic)", personal-use licence), converted from .blend to .glb with Blender.
// The file's own materials did not survive the conversion, so they are restyled here by name.
// Returns a Group like createVirtus: origin = footprint centre on the ground, front = +Z, scaled to opts.length (default 4.561 m),
// with userData.wheels {fl, fr, rl, rr} (spin .rotation.x) and userData.steer {fl, fr} (steer .rotation.y).
export async function loadCarGLB(THREE, GLTFLoader, url, opts = {}) {
  const gltf = await new GLTFLoader().loadAsync(url);
  const model = gltf.scene;
  for (const nm of (opts.remove ?? ['Cube001'])) { const o = model.getObjectByName(nm); if (o) o.parent.remove(o) }   // stray pole in front of the grille
  const paint = new THREE.MeshPhysicalMaterial({ color: opts.color ?? '#2f5d8c', roughness: 0.28, metalness: 0.55, clearcoat: 1, clearcoatRoughness: 0.05 });
  const M = {
    paint,
    glass: new THREE.MeshPhysicalMaterial({ color: '#1a2026', roughness: 0.04, metalness: 0.1, transparent: true, opacity: 0.82, clearcoat: 1 }),
    black: new THREE.MeshStandardMaterial({ color: '#121314', roughness: 0.5, metalness: 0.2 }),
    trim: new THREE.MeshStandardMaterial({ color: '#202124', roughness: 0.7 }),
    chrome: new THREE.MeshStandardMaterial({ color: '#d9dde1', roughness: 0.12, metalness: 1 }),
    lamp: new THREE.MeshPhysicalMaterial({ color: '#dfe5ea', roughness: 0.05, metalness: 0.5, clearcoat: 1, emissive: '#fff4dd', emissiveIntensity: 0.15 }),
    tail: new THREE.MeshPhysicalMaterial({ color: '#a3101a', roughness: 0.08, metalness: 0.2, clearcoat: 1, emissive: '#5a0610', emissiveIntensity: 0.35 }),
    mirror: new THREE.MeshStandardMaterial({ color: '#c9d1d8', roughness: 0.02, metalness: 1 }),
    tyre: new THREE.MeshStandardMaterial({ color: '#1b1c1e', roughness: 0.92 }),
    alloy: new THREE.MeshStandardMaterial({ color: '#b9bdc2', roughness: 0.28, metalness: 0.9 }),
    hub: new THREE.MeshStandardMaterial({ color: '#5b5e62', roughness: 0.4, metalness: 0.8 }),
  };
  const byName = { 'CARR': M.paint, 'VD': M.glass, 'GRADES': M.black, 'LN': M.tail, 'Material.005': M.trim, 'Material.006': M.lamp, 'Material.007': M.black,
    'Material.008': M.black, 'Material.766': M.chrome, 'Alloy.000': M.chrome, 'Material.004': M.paint, 'Material.883': M.mirror,
    'Material.003': M.tyre, 'Material.002': M.alloy, 'Material.1009': M.hub, ...(opts.materials || {}) };
  model.traverse(o => { if (o.isMesh) { const mm = o.material; o.material = byName[mm.name] || M.trim; o.castShadow = true; o.receiveShadow = true; o.userData.srcMaterial = mm.name } });
  // orient: the file's front is +X; turn it to +Z, scale to length, put the footprint centre at the origin and the tyres on the ground
  const g = new THREE.Group(); g.name = opts.name ?? 'Car';
  const holder = new THREE.Group(); holder.add(model); holder.rotation.y = -Math.PI / 2; g.add(holder);
  g.updateMatrixWorld(true);
  let bb = new THREE.Box3().setFromObject(holder); const size = bb.getSize(new THREE.Vector3());
  const k = (opts.length ?? 4.561) / size.z; holder.scale.setScalar(k); g.updateMatrixWorld(true);
  if (opts.bodyWidth) {   // match the body width (without mirrors) to the real car; the body is the largest paint mesh
    let body = null; model.traverse(o => { if (o.isMesh && o.userData.srcMaterial === 'CARR' && (!body || o.geometry.attributes.position.count > body.geometry.attributes.position.count)) body = o });
    if (body) { const w = new THREE.Box3().setFromObject(body).getSize(new THREE.Vector3()).x; holder.scale.z *= opts.bodyWidth / w; g.updateMatrixWorld(true) } }
  bb = new THREE.Box3().setFromObject(holder); const c = bb.getCenter(new THREE.Vector3());
  holder.position.set(-c.x, -bb.min.y, -c.z); g.updateMatrixWorld(true);
  // wheels: hang each wheel node on a pivot at its centre (axle along X), front ones inside a steer group
  const wheels = {}, steer = {};
  const nodes = []; model.traverse(o => { if (/^roda/i.test(o.name) && !o.isMesh) nodes.push(o) });
  for (const n of nodes) {
    const wb = new THREE.Box3().setFromObject(n), wc = wb.getCenter(new THREE.Vector3());
    const key = (wc.z > 0 ? 'f' : 'r') + (wc.x > 0 ? 'l' : 'r');
    const spin = new THREE.Group(); spin.name = 'wheel spin ' + key;
    if (key[0] === 'f') { const st = new THREE.Group(); st.name = 'steer ' + key; st.position.copy(wc); g.add(st); st.add(spin); steer[key] = st }
    else { spin.position.copy(wc); g.add(spin) }
    g.updateMatrixWorld(true); spin.attach(n); wheels[key] = spin;
  }
  const fb = new THREE.Box3().setFromObject(g).getSize(new THREE.Vector3());
  g.userData = { wheels, steer, dims: { length: fb.z, width: fb.x, height: fb.y }, paint };
  return g;
}

// Downloaded two-wheeler (or any vehicle) model: orient so its front is +Z, level it, scale to opts.length, stand it on the ground.
//   opts.front: '+z' (default) or '+x' — which way the file's front faces;  opts.pitch: small correction (rad) about the vehicle's width axis
//   opts.materials: { srcName: material } overrides; opts.tint: { srcName: '#hex' } recolours
export async function loadGLBVehicle(THREE, GLTFLoader, url, opts = {}) {
  const gltf = await new GLTFLoader().loadAsync(url);
  const model = gltf.scene;
  model.traverse(o => { if (o.isMesh) { o.castShadow = true; o.receiveShadow = true;
    const fix = m => { const nm = m.name; if (opts.materials && opts.materials[nm]) return opts.materials[nm];
      if (opts.tint && opts.tint[nm]) { const c = m.clone(); c.color.set(opts.tint[nm]); return c } return m };
    o.material = Array.isArray(o.material) ? o.material.map(fix) : fix(o.material) } });
  const g = new THREE.Group(); g.name = opts.name ?? 'Vehicle';
  const holder = new THREE.Group(); holder.add(model); g.add(holder);
  if (opts.front === '+x') holder.rotation.y = -Math.PI / 2;
  const tilt = new THREE.Group(); g.remove(holder); tilt.add(holder); g.add(tilt); tilt.rotation.x = opts.pitch || 0;
  g.updateMatrixWorld(true);
  let bb = new THREE.Box3().setFromObject(tilt); const size = bb.getSize(new THREE.Vector3());
  tilt.scale.setScalar((opts.length ?? size.z) / size.z); g.updateMatrixWorld(true);
  bb = new THREE.Box3().setFromObject(tilt); const c = bb.getCenter(new THREE.Vector3());
  tilt.position.set(-c.x, -bb.min.y, -c.z); g.updateMatrixWorld(true);
  const fb = new THREE.Box3().setFromObject(g).getSize(new THREE.Vector3());
  g.userData.dims = { length: fb.z, width: fb.x, height: fb.y };
  return g;
}
