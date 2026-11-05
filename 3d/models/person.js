// A 6' (1.83 m) man walking up the spiral stair ST-2, one foot on each tread, step over step.
// Body: a rigged, textured human (assets/people/man.glb, see ASSETS.md). Arms, spine and head play the model's own
// walk and idle clips; legs are placed by two-bone IK so each foot lands flat on its tread, with heel-lift (toe-off)
// on the trailing foot and a lifted swing that clears the nosing.
// Stair data in feet: c (centre x, y), A0 first tread start angle, A tread angle, N risers, R riser, rw walk-line radius.
// The body and the walk / idle clips come from two files (Mixamo bone names); the clips are renamed onto the body's bones.
export async function loadStairWalker(THREE, GLTFLoader, bodyUrl, clipUrl, st, m, mx) {
  const ld = u => new Promise((res, rej) => new GLTFLoader().load(u, res, undefined, rej));
  const [body, src] = await Promise.all([ld(bodyUrl), ld(clipUrl)]);
  body.animations = ['Walk', 'Idle'].map(n => retarget(THREE, src, body.scene, src.animations.find(a => a.name === n)));
  return build(THREE, body, st, m, mx);
}

// Copy a clip from the source rig to the body: each bone keeps the same turn away from the T-pose, measured in world space,
// so the two rigs may have different bone axes. Baked at 30 frames a second.
export function retarget(THREE, src, dst, clip) {
  const strip = n => n.replace(/^mixamorig:?/, '');
  const sb = {}, db = {};
  src.scene.traverse(o => { if (o.isBone) sb[strip(o.name)] = o; });
  dst.traverse(o => { if (o.isBone) db[strip(o.name)] = o; });
  const names = Object.keys(db).filter(n => sb[n]);
  const mix = new THREE.AnimationMixer(src.scene), wq = o => o.getWorldQuaternion(new THREE.Quaternion());
  const pose = (c, t) => { mix.stopAllAction(); const a = mix.clipAction(c); a.play(); a.time = t; mix.update(0); src.scene.updateMatrixWorld(true); };
  // parents before children
  const depth = o => { let k = 0; while (o.parent) { k++; o = o.parent; } return k; };
  const order = names.slice().sort((a, b) => depth(db[a]) - depth(db[b]));
  const pos = o => o.getWorldPosition(new THREE.Vector3());
  pose(src.animations.find(a => a.name === 'TPose'), 0);
  dst.updateMatrixWorld(true);
  // the two rigs may face opposite ways: turn the source so its left hip points the same way as the body's
  const flat = v => v.setY(0).normalize();
  const C = new THREE.Quaternion().setFromUnitVectors(flat(pos(sb.LeftUpLeg).sub(pos(sb.Hips))), flat(pos(db.LeftUpLeg).sub(pos(db.Hips))));
  const sRest = {}; for (const n of names) sRest[n] = C.clone().multiply(wq(sb[n])).invert();
  // the body may be bound in an A-pose: bend each bone to the source T-pose direction before measuring its rest
  const keep = names.map(n => db[n].quaternion.clone());
  for (const b of order) {
    const kid = db[b].children.find(c => c.isBone && sb[strip(c.name)]);
    if (!kid) continue;
    const want = pos(sb[strip(kid.name)]).sub(pos(sb[b])).applyQuaternion(C).normalize();
    const cur = pos(kid).sub(pos(db[b])).normalize();
    const q = new THREE.Quaternion().setFromUnitVectors(cur, want).multiply(wq(db[b]));
    const pw = db[b].parent.getWorldQuaternion(new THREE.Quaternion()).invert();
    db[b].quaternion.copy(pw.multiply(q)); db[b].updateMatrixWorld(true);
  }
  const dRest = {}; for (const n of names) dRest[n] = wq(db[n]);
  names.forEach((n, i) => db[n].quaternion.copy(keep[i])); dst.updateMatrixWorld(true);
  const fps = 30, n = Math.max(2, Math.round(clip.duration * fps) + 1), times = new Float32Array(n), vals = {};
  for (const b of order) vals[b] = new Float32Array(n * 4);
  for (let i = 0; i < n; i++) {
    const t = Math.min(clip.duration, i / fps); times[i] = t; pose(clip, t);
    const world = {};
    for (const b of order) {
      const want = C.clone().multiply(wq(sb[b])).multiply(sRest[b]).multiply(dRest[b]);   // source turn from rest, applied on the body's rest
      let p = db[b].parent, pw;
      while (p && !(p.isBone && world[strip(p.name)])) p = p.parent;
      if (p && p.isBone) { pw = world[strip(p.name)].clone(); let q = db[b].parent; const chain = []; while (q !== p) { chain.push(q); q = q.parent; } for (const c of chain.reverse()) pw.multiply(c.quaternion); }
      else pw = db[b].parent.getWorldQuaternion(new THREE.Quaternion());
      const local = pw.invert().multiply(want);
      world[b] = want; local.toArray(vals[b], i * 4);
    }
  }
  mix.stopAllAction();
  return new THREE.AnimationClip(clip.name, clip.duration, order.map(b => new THREE.QuaternionKeyframeTrack(db[b].name + '.quaternion', times, vals[b])));
}

function build(THREE, gltf, st, m, mx) {
  const V = () => new THREE.Vector3(), Q = () => new THREE.Quaternion();
  const UP = new THREE.Vector3(0, 1, 0), d2r = Math.PI / 180;
  const model = gltf.scene, root = new THREE.Group();
  root.add(model);
  model.traverse(o => {
    if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; o.frustumCulled = false; if (/visor/i.test(o.name)) o.visible = false;
      // plain everyday colours: blue top, grey trousers (the texture's weave stays)
      if (/Outfit_Top/.test(o.name)) o.material.color.set('#8da0c4'); if (/Outfit_Bottom/.test(o.name)) o.material.color.set('#9a9aa0'); }
  });
  const B = n => model.getObjectByName('mixamorig' + n) || model.getObjectByName(n);
  const bone = {
    hips: B('Hips'), spine: B('Spine1'), head: B('Head'), top: B('HeadTop_End'),
    L: { up: B('LeftUpLeg'), leg: B('LeftLeg'), foot: B('LeftFoot'), toe: B('LeftToeBase') },
    R: { up: B('RightUpLeg'), leg: B('RightLeg'), foot: B('RightFoot'), toe: B('RightToeBase') },
  };
  // scale to exactly 6' from sole to the top of the head, in the bind pose
  model.updateMatrixWorld(true);
  const sole = Math.min(bone.L.toe.getWorldPosition(V()).y, bone.R.toe.getWorldPosition(V()).y);
  const h0 = bone.top.getWorldPosition(V()).y - sole + 0.012;   // the end bone sits just under the hair
  root.scale.setScalar(m(6.0) / h0);
  model.position.y = -sole;
  root.updateMatrixWorld(true);
  // rest measurements (world, metres, root at origin facing +z)
  const rest = {}, wp = o => o.getWorldPosition(V());
  for (const s of ['L', 'R']) {
    const b = bone[s];
    rest[s] = {
      q: { up: b.up.quaternion.clone(), leg: b.leg.quaternion.clone(), foot: b.foot.quaternion.clone() },
      a: wp(b.up).distanceTo(wp(b.leg)), b: wp(b.leg).distanceTo(wp(b.foot)),
      ah: wp(b.foot).y, bh: wp(b.toe).y, lb: wp(b.toe).z - wp(b.foot).z,
      fq: b.foot.getWorldQuaternion(Q()),
    };
  }
  const hipH = wp(bone.hips).y, hipW = Math.abs(wp(bone.L.up).x - wp(bone.R.up).x);
  // clips without root motion and without the legs (the legs are set by IK)
  const mixer = new THREE.AnimationMixer(model);
  const strip = c => { c = c.clone(); c.tracks = c.tracks.filter(t => !/(UpLeg|Leg|Foot|Toe)/.test(t.name) && !/Hips\.position/.test(t.name)); return c; };
  const clip = n => gltf.animations.find(a => a.name === n);
  const walkClip = clip('Walk'), idleClip = clip('Idle');
  // find the clip time where the right foot is furthest forward (its heel strike), to keep the arms in step with the legs
  let tR = 0;
  { const full = mixer.clipAction(walkClip); full.play(); let best = -1e9;
    for (let i = 0; i < 60; i++) { const t = walkClip.duration * i / 60; full.time = t; mixer.update(0); model.updateMatrixWorld(true);
      const d = wp(bone.R.foot).z - wp(bone.L.foot).z; if (d > best) { best = d; tR = t; } }
    full.stop(); mixer.uncacheAction(walkClip); }
  const walk = mixer.clipAction(strip(walkClip)), idle = mixer.clipAction(strip(idleClip));
  walk.play(); idle.play(); walk.timeScale = idle.timeScale = 0;
  const hipsRest = bone.hips.position.clone();

  // ---- the stair path ----
  const { c: [cx, cy], A0, A, N, R, rw } = st, Ts = st.stepTime || 0.9, tStand = 1.2, tTop = 2.5;
  const angOf = i => i <= 0 ? A0 - 0.6 * A : A0 + (Math.min(i, N) - 0.5) * A;   // plan angle of placement i (0 = floor in front of tread 1)
  const zOf = i => i <= 0 ? 0 : Math.min(i, N) * R;
  const onPath = (a, r) => new THREE.Vector3(mx(cx + r * Math.cos(a * d2r)), 0, m(cy + r * Math.sin(a * d2r)));
  const fwdAt = a => onPath(a + 0.5, rw).sub(onPath(a - 0.5, rw)).normalize();
  const rightAt = a => new THREE.Vector3().crossVectors(fwdAt(a), UP).normalize();
  const footAt = (side, a, z) => onPath(a, rw).addScaledVector(rightAt(a), (side === 'R' ? 1 : -1) * m(0.3)).setY(m(z));
  const sm = (a, b, x) => { x = Math.min(1, Math.max(0, (x - a) / (b - a))); return x * x * (3 - 2 * x); };
  const T = tStand + (N + 1) * Ts + tTop;

  // pose at time t (seconds, loops): foot centres, foot yaw angles, pelvis
  function plan(t) {
    t %= T;
    const s = Math.min(N + 1, Math.max(0, (t - tStand) / Ts));
    const j = Math.min(N + 1, Math.floor(s) + 1), u = s - (j - 1);
    const sw = j % 2 ? 'R' : 'L', stn = sw === 'R' ? 'L' : 'R';
    const feet = {};
    // stance foot on placement j-1; swing foot from j-2 to j (the last, closing step goes to the landing beside it)
    const iTo = Math.min(j, N), iFrom = j === N + 1 ? N - 1 : j - 2;
    feet[stn] = { a: angOf(j - 1), z: zOf(j - 1), pitch: 0 };
    if (s <= 0 || s >= N + 1) { const i = s <= 0 ? 0 : N; feet.L = { a: angOf(i), z: zOf(i), pitch: 0 }; feet.R = { a: angOf(i), z: zOf(i), pitch: 0 }; }
    else {
      const h = sm(0.12, 0.95, u), dz = zOf(iTo) - zOf(iFrom), lift = dz > 0 ? 0.16 : 0.12;
      feet[sw] = { a: angOf(iFrom) + (angOf(iTo) - angOf(iFrom)) * h, z: zOf(iFrom) + dz * sm(0, 0.55, u) + lift * Math.sin(Math.PI * u), swing: u };
    }
    // pelvis leads the stance foot: over it at mid-swing, rising with it
    const p = s <= 0 ? -0.1 : s >= N + 1 ? N : Math.min(N, Math.max(-0.1, j - 1.55 + u));
    const pa = A0 + (p - 0.5) * A;
    const pz = R * Math.min(N, Math.max(0, p));
    const moving = s > 0 && s < N + 1;
    return { s, u, j, feet, pa, pz, moving, stn };
  }

  const tmpQ = Q(), tmpQ2 = Q(), v1 = V(), v2 = V();
  function setWorldQuat(b, q) { b.parent.getWorldQuaternion(tmpQ2); b.quaternion.copy(tmpQ2.invert().multiply(q)); b.updateMatrixWorld(true); }
  function aim(b, child, dir) {
    const cur = child.getWorldPosition(v1).sub(b.getWorldPosition(v2)).normalize();
    const q = Q().setFromUnitVectors(cur, dir.clone().normalize());
    setWorldQuat(b, q.multiply(b.getWorldQuaternion(tmpQ)));
  }
  // ankle position for a foot whose ball stays put and whose heel is lifted by phi (toe-off)
  function ankleToe(flat, f, r, rs, phi) {
    const ball = flat.clone().addScaledVector(f, rs.lb).addScaledVector(UP, rs.bh - rs.ah);
    const off = f.clone().multiplyScalar(-rs.lb).addScaledVector(UP, rs.ah - rs.bh).applyAxisAngle(r, -phi);
    return ball.add(off);
  }
  function legIK(side, ft, bodyF) {
    const b = bone[side], rs = rest[side];
    b.up.quaternion.copy(rs.q.up); b.leg.quaternion.copy(rs.q.leg); b.foot.quaternion.copy(rs.q.foot); b.up.updateMatrixWorld(true);
    const f = fwdAt(ft.a), r = rightAt(ft.a);
    const centre = footAt(side, ft.a, ft.z);
    const flat = centre.clone().addScaledVector(f, -rs.lb * 0.45).addScaledVector(UP, rs.ah);
    const H = b.up.getWorldPosition(V()), reach = (rs.a + rs.b) * 0.995;
    let T = flat, phi = 0;
    if (H.distanceTo(T) > reach) {   // heel lifts, pivoting on the ball of the foot
      let lo = 0, hi = 55 * d2r;
      for (let i = 0; i < 12; i++) { const mid = (lo + hi) / 2; if (H.distanceTo(ankleToe(flat, f, r, rs, mid)) > reach) lo = mid; else hi = mid; }
      phi = hi; T = ankleToe(flat, f, r, rs, phi);
    }
    if (ft.swing != null) { phi = Math.max(phi, 0.35 * Math.sin(Math.PI * Math.min(1, ft.swing / 0.5)) * (ft.swing < 0.5 ? 1 : 0)); }
    let d = H.distanceTo(T);
    if (d > reach) { T = H.clone().add(T.clone().sub(H).setLength(reach)); d = reach; }
    const u = T.clone().sub(H).normalize();
    const pole = bodyF.clone().addScaledVector(u, -bodyF.dot(u)).normalize();
    const cosA = Math.min(1, Math.max(-1, (rs.a * rs.a + d * d - rs.b * rs.b) / (2 * rs.a * d)));
    const K = H.clone().addScaledVector(u, rs.a * cosA).addScaledVector(pole, rs.a * Math.sqrt(1 - cosA * cosA));
    aim(b.up, b.leg, K.clone().sub(H));
    aim(b.leg, b.foot, T.clone().sub(K));
    // foot: flat on the tread, pointing along the stair, heel lifted by phi
    const yaw = Q().setFromUnitVectors(new THREE.Vector3(0, 0, 1), new THREE.Vector3(f.x, 0, f.z).normalize());
    const pitch = Q().setFromAxisAngle(r, -phi);
    setWorldQuat(b.foot, pitch.multiply(yaw).multiply(rs.fq));
  }

  let last = null;
  function update(t) {
    const pl = plan(t);
    // upper body: walk while climbing, idle when standing (shorter arm swing than on flat ground)
    const w = pl.moving ? Math.min(1, Math.min(pl.s, N + 1 - pl.s) * 2) : 0;
    walk.setEffectiveWeight(0.75 * w); idle.setEffectiveWeight(1 - 0.75 * w);
    walk.time = ((tR + (pl.s - 1) / 2 * walkClip.duration) % walkClip.duration + walkClip.duration) % walkClip.duration;
    idle.time = (t % idleClip.duration);
    mixer.update(0);
    bone.hips.position.copy(hipsRest);
    // body: face along the stair at the pelvis angle, sway a little over the stance foot
    const f = fwdAt(pl.pa), pos = onPath(pl.pa, rw);
    const sway = pl.moving ? (pl.stn === 'R' ? 1 : -1) * m(0.08) * Math.sin(Math.PI * pl.u) : 0;
    pos.addScaledVector(rightAt(pl.pa), sway);
    root.position.set(pos.x, m(pl.pz) - hipH * (0.02 + 0.035 * w), pos.z);
    root.quaternion.setFromUnitVectors(new THREE.Vector3(0, 0, 1), f);
    root.updateMatrixWorld(true);
    // lean forward into the climb
    if (pl.moving) { const r = rightAt(pl.pa); const qs = bone.spine.getWorldQuaternion(Q()); setWorldQuat(bone.spine, Q().setFromAxisAngle(r, -10 * d2r * w).multiply(qs)); }
    for (const s of ['L', 'R']) legIK(s, pl.feet[s], f);
    last = pl;
    return pl;
  }
  return {
    root, update, duration: T, headTop: () => bone.top.getWorldPosition(V()).addScaledVector(UP, m(0.04)),
    step: () => last ? Math.max(0, Math.min(N, last.j - 1)) : 0, hipW,
  };
}

// The same 6' man walking on flat or gently sloped ground along a path of plan points [x, y, z] (feet), there and back.
// The walk clip drives the whole body (legs included); the body moves along the path at a normal walking pace.
export async function loadPathWalker(THREE, GLTFLoader, bodyUrl, clipUrl, path, m, mx) {
  const ld = u => new Promise((res, rej) => new GLTFLoader().load(u, res, undefined, rej));
  const [body, src] = await Promise.all([ld(bodyUrl), ld(clipUrl)]);
  const walkClip = retarget(THREE, src, body.scene, src.animations.find(a => a.name === 'Walk'));
  walkClip.tracks = walkClip.tracks.filter(t => !/Hips\.position/.test(t.name));
  const model = body.scene, root = new THREE.Group(), V = () => new THREE.Vector3();
  root.add(model);
  model.traverse(o => { if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; o.frustumCulled = false; if (/visor/i.test(o.name)) o.visible = false;
    if (/Outfit_Top/.test(o.name)) o.material.color.set('#8da0c4'); if (/Outfit_Bottom/.test(o.name)) o.material.color.set('#9a9aa0'); } });
  const B = n => model.getObjectByName('mixamorig' + n) || model.getObjectByName(n);
  model.updateMatrixWorld(true);
  const sole = Math.min(B('LeftToeBase').getWorldPosition(V()).y, B('RightToeBase').getWorldPosition(V()).y);
  root.scale.setScalar(m(6.0) / (B('HeadTop_End').getWorldPosition(V()).y - sole + 0.012));
  model.position.y = -sole;
  const mixer = new THREE.AnimationMixer(model), act = mixer.clipAction(walkClip); act.play();
  const P = path.map(([x, y, z]) => new THREE.Vector3(mx(x), m(z), m(y)));
  const seg = [], speed = 1.25; let L = 0;   // metres a second
  for (let i = 1; i < P.length; i++) { const d = P[i].distanceTo(P[i - 1]); seg.push([L, d]); L += d; }
  const stride = speed * walkClip.duration, T = 2 * L / speed;
  function at(s) { let i = seg.findIndex(([a, d]) => s <= a + d); if (i < 0) i = seg.length - 1; const [a, d] = seg[i];
    return { p: P[i].clone().lerp(P[i + 1], d ? (s - a) / d : 0), f: P[i + 1].clone().sub(P[i]).setY(0).normalize() }; }
  function update(t) {
    t %= T; let s = t * speed, back = s > L; if (back) s = 2 * L - s;
    const { p, f } = at(s); if (back) f.negate();
    root.position.copy(p); root.quaternion.setFromUnitVectors(new THREE.Vector3(0, 0, 1), f);
    act.time = ((t * speed) % stride) / speed; mixer.update(0); root.updateMatrixWorld(true);
    return { s, L, back };
  }
  return { root, update, duration: T, headTop: () => B('HeadTop_End').getWorldPosition(V()) };
}
