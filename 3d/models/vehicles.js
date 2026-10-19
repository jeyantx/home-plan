// Simple procedural vehicles for checking parking space: a family hatchback/sedan, a scooter and a motorcycle.
//
//   import { createCar, createScooter, createMotorbike } from './models/vehicles.js';
//
// Units: metres, +Y up. Origin = centre of the footprint at ground level. Front of the vehicle = +Z.
// Plain Mesh + merged BufferGeometry per material (no InstancedMesh), so the path tracer can use them.

export function createCar(THREE, mergeGeometries, opts = {}) {
  const L = opts.length ?? 4.3, W = opts.width ?? 1.73, color = opts.color ?? '#d9dcdf';
  const g = new THREE.Group(); g.name = 'Car';
  const flat = x => (x.index ? x.toNonIndexed() : x);
  const ext = (pts, w, bevel = 0.04) => {   // side profile (z along length, y up) extruded across the width
    const sh = new THREE.Shape(pts.map(([z, y]) => new THREE.Vector2(z, y)));
    const geo = new THREE.ExtrudeGeometry(sh, { depth: w - 2 * bevel, bevelEnabled: true, bevelThickness: bevel, bevelSize: bevel, bevelSegments: 2, curveSegments: 8 });
    geo.translate(0, 0, -(w - 2 * bevel) / 2); geo.rotateY(-Math.PI / 2); return flat(geo);   // profile x -> world z (front +Z)
  };
  const h = L / 2;
  // lower body to the belt line, with a sloping bonnet and a short boot
  const body = ext([[-h, 0.32], [h, 0.32], [h, 0.6], [h - 0.18, 0.78], [h - 1.25, 0.9], [-h + 0.5, 0.92], [-h, 0.86]], W);
  // glasshouse: windscreen, roof, rear screen (dark glass)
  const cab = ext([[h - 1.25, 0.88], [h - 1.95, 1.4], [-h + 1.2, 1.44], [-h + 0.4, 0.94], [-h + 0.4, 0.88]], W - 0.16, 0.03);
  const paint = new THREE.MeshPhysicalMaterial({ color, roughness: 0.25, metalness: 0.5, clearcoat: 1, clearcoatRoughness: 0.08 });
  const glass = new THREE.MeshStandardMaterial({ color: '#1d2329', roughness: 0.08, metalness: 0.6 });
  const black = new THREE.MeshStandardMaterial({ color: '#16171a', roughness: 0.7 });
  const chrome = new THREE.MeshStandardMaterial({ color: '#c9cdd1', roughness: 0.25, metalness: 0.9 });
  const add = (geo, mat, name) => { const me = new THREE.Mesh(geo, mat); me.castShadow = true; me.receiveShadow = true; me.name = name; g.add(me); return me };
  add(body, paint, 'body'); add(cab, glass, 'glass');
  // roof panel in body colour over the glass
  const roof = new THREE.BoxGeometry(W - 0.3, 0.04, 1.1); roof.translate(0, 1.44, -0.05); add(flat(roof), paint, 'roof');
  // bumpers, wheel arches (black), lamps, plates, mirrors
  const blk = [];
  for (const z of [h - 0.05, -h + 0.05]) { const b = new THREE.BoxGeometry(W + 0.02, 0.2, 0.14); b.translate(0, 0.42, z); blk.push(flat(b)) }
  for (const s of [-1, 1]) { const m = new THREE.BoxGeometry(0.06, 0.1, 0.18); m.translate(s * (W / 2 + 0.05), 0.98, h - 1.35); blk.push(flat(m)) }
  add(mergeGeometries(blk), black, 'trim');
  const lampW = new THREE.MeshStandardMaterial({ color: '#f4f6f8', emissive: '#fff6e0', emissiveIntensity: 0.3, roughness: 0.1 });
  const lampR = new THREE.MeshStandardMaterial({ color: '#b3121b', emissive: '#7a0a10', emissiveIntensity: 0.3, roughness: 0.2 });
  const lw = [], lr = [], pl = [];
  for (const s of [-1, 1]) { const a = new THREE.BoxGeometry(0.34, 0.1, 0.05); a.translate(s * (W / 2 - 0.28), 0.68, h - 0.02); lw.push(flat(a));
    const b = new THREE.BoxGeometry(0.3, 0.1, 0.05); b.translate(s * (W / 2 - 0.25), 0.8, -h + 0.02); lr.push(flat(b)) }
  for (const z of [h + 0.03, -h - 0.03]) { const p = new THREE.BoxGeometry(0.52, 0.12, 0.02); p.translate(0, 0.45, z); pl.push(flat(p)) }
  add(mergeGeometries(lw), lampW, 'headlamps'); add(mergeGeometries(lr), lampR, 'tail lamps');
  add(mergeGeometries(pl), new THREE.MeshStandardMaterial({ color: '#f5f5f0', roughness: 0.5 }), 'number plates');
  // wheels: tyre + alloy
  const ty = [], rim = [];
  for (const z of [h - 0.85, -h + 0.75]) for (const s of [-1, 1]) {
    const t = new THREE.CylinderGeometry(0.31, 0.31, 0.2, 24); t.rotateZ(Math.PI / 2); t.translate(s * (W / 2 - 0.12), 0.31, z); ty.push(flat(t));
    const r = new THREE.CylinderGeometry(0.2, 0.2, 0.21, 16); r.rotateZ(Math.PI / 2); r.translate(s * (W / 2 - 0.12), 0.31, z); rim.push(flat(r)) }
  add(mergeGeometries(ty), new THREE.MeshStandardMaterial({ color: '#1b1c1e', roughness: 0.9 }), 'tyres'); add(mergeGeometries(rim), chrome, 'wheels');
  return g;
}

function twoWheeler(THREE, mergeGeometries, kind, color) {
  const g = new THREE.Group(); g.name = kind;
  const flat = x => (x.index ? x.toNonIndexed() : x);
  const add = (arr, mat, name) => { const me = new THREE.Mesh(mergeGeometries(arr), mat); me.castShadow = true; me.receiveShadow = true; me.name = name; g.add(me) };
  const paint = new THREE.MeshPhysicalMaterial({ color, roughness: 0.3, metalness: 0.3, clearcoat: 0.8 });
  const black = new THREE.MeshStandardMaterial({ color: '#17181a', roughness: 0.75 });
  const metal = new THREE.MeshStandardMaterial({ color: '#b9bdc2', roughness: 0.3, metalness: 0.85 });
  const B = (w, h, d, x, y, z, rx = 0) => { const b = new THREE.BoxGeometry(w, h, d); if (rx) b.rotateX(rx); b.translate(x, y, z); return flat(b) };
  const wheel = (r, w, z) => { const t = new THREE.TorusGeometry(r - 0.04, 0.05, 10, 24); t.rotateY(Math.PI / 2); t.translate(0, r, z); return flat(t) };
  const hub = (r, z) => { const c = new THREE.CylinderGeometry(r * 0.45, r * 0.45, 0.08, 14); c.rotateZ(Math.PI / 2); c.translate(0, r, z); return flat(c) };
  if (kind === 'Scooter') {
    const r = 0.23, zf = 0.64, zr = -0.6;
    add([wheel(r, 0.1, zf), wheel(r, 0.1, zr), B(0.2, 0.08, 0.5, 0, 0.62, 0.42, 0.25)], black, 'tyres and handle grips');
    add([hub(r, zf), hub(r, zr), B(0.62, 0.03, 0.03, 0, 1.08, 0.58), (() => { const s = new THREE.CylinderGeometry(0.025, 0.025, 0.55, 8); s.rotateX(-0.35); s.translate(0, 0.62, 0.62); return flat(s) })()], metal, 'forks and handlebar');
    const rear = new THREE.SphereGeometry(0.36, 16, 12); rear.scale(0.75, 0.75, 1.25); rear.translate(0, 0.55, -0.42);
    add([flat(rear), B(0.34, 0.07, 0.6, 0, 0.3, 0.12), B(0.5, 0.75, 0.14, 0, 0.72, 0.52, -0.25), B(0.3, 0.16, 0.25, 0, 1.08, 0.6)], paint, 'body panels');
    add([B(0.3, 0.09, 0.62, 0, 0.83, -0.32)], new THREE.MeshStandardMaterial({ color: '#2a2622', roughness: 0.85 }), 'seat');
    add([B(0.14, 0.08, 0.03, 0, 1.06, 0.735)], new THREE.MeshStandardMaterial({ color: '#f4f6f8', emissive: '#fff6e0', emissiveIntensity: 0.3 }), 'headlamp');
  } else {
    const r = 0.31, zf = 0.7, zr = -0.66;
    add([wheel(r, 0.12, zf), wheel(r, 0.14, zr), B(0.16, 0.12, 0.42, 0, 0.42, 0.0), B(0.62, 0.035, 0.035, 0, 1.06, 0.48)], black, 'tyres, engine and handlebar');
    add([hub(r, zf), hub(r, zr), (() => { const s = new THREE.CylinderGeometry(0.03, 0.03, 0.75, 8); s.rotateX(-0.45); s.translate(0, 0.68, 0.56); return flat(s) })(), B(0.06, 0.06, 0.8, 0.12, 0.32, -0.2), B(0.24, 0.26, 0.3, 0, 0.42, 0.12)], metal, 'forks, engine and exhaust');
    const tank = new THREE.SphereGeometry(0.22, 16, 12); tank.scale(0.95, 0.7, 1.5); tank.translate(0, 0.86, 0.18);
    add([flat(tank), B(0.2, 0.1, 0.35, 0, 0.82, -0.6)], paint, 'tank and tail');
    add([B(0.26, 0.08, 0.5, 0, 0.84, -0.25)], new THREE.MeshStandardMaterial({ color: '#2a2622', roughness: 0.85 }), 'seat');
    add([(() => { const c = new THREE.CylinderGeometry(0.09, 0.09, 0.08, 16); c.rotateX(Math.PI / 2); c.translate(0, 0.98, 0.66); return flat(c) })()], new THREE.MeshStandardMaterial({ color: '#f4f6f8', emissive: '#fff6e0', emissiveIntensity: 0.3 }), 'headlamp');
  }
  // side stand: lean the bike a little
  g.rotation.z = 0.06;
  return g;
}
export const createScooter = (THREE, mg, opts = {}) => twoWheeler(THREE, mg, 'Scooter', opts.color ?? '#8b1e2b');
export const createMotorbike = (THREE, mg, opts = {}) => twoWheeler(THREE, mg, 'Motorcycle', opts.color ?? '#1f2d4d');
