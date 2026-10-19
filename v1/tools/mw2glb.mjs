// microwave: drop the stray piece, scale each axis to a real 20 L solo microwave (46 wide x 28 high x 36 deep cm), front stays on -X, sit on the ground, centred
import * as THREE from 'three';
import {TDSLoader} from 'three/addons/loaders/TDSLoader.js';
import {GLTFExporter} from 'three/addons/exporters/GLTFExporter.js';
import fs from 'fs';
globalThis.FileReader=class{readAsArrayBuffer(b){b.arrayBuffer().then(r=>{this.result=r;this.onloadend&&this.onloadend()})}readAsDataURL(b){b.arrayBuffer().then(r=>{this.result='data:application/octet-stream;base64,'+Buffer.from(r).toString('base64');this.onloadend&&this.onloadend()})}};
THREE.TextureLoader.prototype.load=function(){return new THREE.Texture()};
const [inp,out]=process.argv.slice(2);const buf=fs.readFileSync(inp);
const grp=new TDSLoader().parse(buf.buffer.slice(buf.byteOffset,buf.byteOffset+buf.byteLength),'');
grp.traverse(o=>{if(o.isMesh)(Array.isArray(o.material)?o.material:[o.material]).forEach(m=>{m.map=null;m.bumpMap=null;m.specularMap=null;m.alphaMap=null;m.normalMap=null})});
const stray=[];grp.traverse(o=>{if(o.isMesh&&['microwave0','microwave1','microwave2'].includes(o.name))stray.push(o)});stray.forEach(o=>o.parent.remove(o));
grp.rotation.x=-Math.PI/2;grp.updateMatrixWorld(true);
const b0=new THREE.Box3().setFromObject(grp),sz=b0.getSize(new THREE.Vector3());
grp.scale.set(0.36/sz.x,0.46/sz.z,0.28/sz.y);   // local axes before the -90 deg turn: local x = world x (depth), local y = world -z (width), local z = world y (height)
grp.updateMatrixWorld(true);const b1=new THREE.Box3().setFromObject(grp),c=b1.getCenter(new THREE.Vector3());grp.position.set(-c.x,-b1.min.y,-c.z);grp.updateMatrixWorld(true);
// the downloaded door parts are scattered (glass outside the box, handle floating), so they are dropped and a clean door is built here:
// black frame, dark glass window and a vertical handle, over the oven opening; the control panel (microwave3, microwave6 and the knobs) stays on its side
{const all=new THREE.Box3().setFromObject(grp),ctl=new THREE.Box3(),body=new THREE.Box3();grp.traverse(o=>{if(o.isMesh&&['microwave3','microwave6'].includes(o.name))ctl.expandByObject(o);if(o.isMesh&&o.name==='microwave_')body.expandByObject(o)});
 console.log('body x',body.min.x.toFixed(3),body.max.x.toFixed(3),'ctl x',ctl.min.x.toFixed(3),ctl.max.x.toFixed(3),'ctl z',ctl.min.z.toFixed(3),ctl.max.z.toFixed(3));
 const fx=ctl.isEmpty()?body.min.x:ctl.max.x+0.003,H=all.max.y,z1=all.min.z+0.006,z2=(ctl.isEmpty()?all.min.z+0.33:ctl.min.z)-0.012,T=0.022,M=(n,c)=>new THREE.MeshStandardMaterial({name:n,color:c});
 const door=new THREE.Group();door.name='door';
 const fr=new THREE.Shape([[z1,0.012],[z2,0.012],[z2,H-0.012],[z1,H-0.012]].map(([a,b])=>new THREE.Vector2(a,b)));fr.holes.push(new THREE.Path([[z1+0.04,0.045],[z1+0.04,H-0.045],[z2-0.05,H-0.045],[z2-0.05,0.045]].map(([a,b])=>new THREE.Vector2(a,b))));
 const fm=new THREE.Mesh(new THREE.ExtrudeGeometry(fr,{depth:T,bevelEnabled:false}),M('door_frame','#161718'));fm.name='door_frame';fm.rotation.y=-Math.PI/2;fm.position.x=fx;door.add(fm);   // shape in the z-y plane, extruded toward -x
 const gl=new THREE.Mesh(new THREE.BoxGeometry(0.006,H-0.09,(z2-0.05)-(z1+0.04)),M('door_glass','#2b3a44'));gl.name='door_glass';gl.position.set(fx-T/2,H/2,(z1+0.04+z2-0.05)/2);door.add(gl);
 const hd=new THREE.Mesh(new THREE.CylinderGeometry(0.008,0.008,H-0.1,16),M('door_handle','#c9ccd0'));hd.name='door_handle';hd.position.set(fx-T-0.022,H/2,z2-0.025);door.add(hd);
 for(const y of [0.06,H-0.06]){const st=new THREE.Mesh(new THREE.BoxGeometry(0.024,0.014,0.014),M('door_handle','#c9ccd0'));st.name='door_handle';st.position.set(fx-T-0.011,y,z2-0.025);door.add(st)}
 // a full body behind the door and the controls (the downloaded shell is only the back half), a control panel with a display and two knobs; the shell, turntable and rack inside are hidden by it
 const bx=new THREE.Mesh(new THREE.BoxGeometry(all.max.x-fx,H,all.max.z-all.min.z),M('mw_body','#2b2c2e'));bx.name='mw_body';bx.position.set((fx+all.max.x)/2,H/2,(all.min.z+all.max.z)/2);door.add(bx);
 const pz1=z2+0.006,pz2=all.max.z-0.004,pn=new THREE.Mesh(new THREE.BoxGeometry(0.004,H-0.024,pz2-pz1),M('mw_panel','#161718'));pn.name='mw_panel';pn.position.set(fx-0.002,H/2,(pz1+pz2)/2);door.add(pn);
 const dp=new THREE.Mesh(new THREE.BoxGeometry(0.003,0.026,(pz2-pz1)*0.7),M('mw_display','#0b0c0d'));dp.name='mw_display';dp.position.set(fx-0.0045,H-0.05,(pz1+pz2)/2);door.add(dp);
 for(const y of [0.13,0.06]){const kn=new THREE.Mesh(new THREE.CylinderGeometry(0.017,0.019,0.014,24),M('mw_knob','#c9ccd0'));kn.name='mw_knob';kn.rotation.z=Math.PI/2;kn.position.set(fx-0.011,y,(pz1+pz2)/2);door.add(kn)}
 const hide=[];grp.traverse(o=>{if(o.isMesh&&['microwave_','microwave4','microwave5'].includes(o.name))hide.push(o)});hide.forEach(o=>o.parent.remove(o));
 grp.parent?grp.parent.add(door):0;globalThis.__door=door;console.log('door z',z1.toFixed(3),z2.toFixed(3),'front x',fx.toFixed(3),'H',H.toFixed(3))}
const bb=new THREE.Box3().setFromObject(grp);console.log('removed',stray.length,'bbox',bb.min.toArray().map(v=>+v.toFixed(3)),bb.max.toArray().map(v=>+v.toFixed(3)));
const root=new THREE.Group();root.add(grp);root.add(globalThis.__door);const glb=await new GLTFExporter().parseAsync(root,{binary:true});fs.writeFileSync(out,Buffer.from(glb));console.log('written',fs.statSync(out).size);
