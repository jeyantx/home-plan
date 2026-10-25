// Car route along the east side (owner's sketch): drive out forward in one curve past the scooter by the neem, through GT-01, east along the road;
// come in from the west, stop just past the gate, reverse back along the same curve. Writes 3d/models/car-route.js. Allow the short back-and-forth with ALLOWSW=1.
// Gaps: 3" round the body everywhere, 6" at the east gate leaf, the east pillar and the two-wheelers. Run: node car_route_east.mjs
import fs from 'fs';
process.env.MARGIN='0.25';
const PARKX=+(process.env.PARKX||14.0), XE=+(process.env.XE||12.5), DRY=!!process.env.DRY;   // car spot centre X; east edge of the raised platform by the small gate
let src=fs.readFileSync(new URL('car_route_plan.mjs',import.meta.url),'utf8');src=src.slice(0,src.indexOf('const S2=Math.PI/2;'));
const BW=false;   // (single layout now)
const BIKES=[[0.55,2.96,20.75,27.71],[3.2,5.62,21.67,27.7]];   // TW-1 and TW-2 side by side along BW-01
const PLAT=[[XE,17.125,6.2,11.0],[13.5,17.125,2.667,6.2]];   // raised platform (kerb over 3" high north of Y 11') and the small-gate steps
src+=`
for(const b of ${JSON.stringify([...BIKES,...PLAT])})rects.push([b[0]-0.25,b[1]+0.25,b[2]-0.25,b[3]+0.25]);
for(const c of circles)c[2]+=0.25;
for(const r of rects)if((r[0]===0.8&&r[1]===1.4)||(r[0]===-1&&r[1]===0.75)){r[0]-=0.25;r[1]+=0.25;r[2]-=0.25;r[3]+=0.25}
export {plan,WB,RMIN};`;
const tmp=new URL('./.car_route_east_tmp_'+process.pid+'.mjs',import.meta.url);fs.writeFileSync(tmp,src);
const {plan,WB}=await import(tmp.href);fs.unlinkSync(tmp);
const N2=-Math.PI/2,ang=(a,b)=>Math.abs(Math.atan2(Math.sin(a-b),Math.cos(a-b)));
const park=[PARKX,28.73-3.1,N2];
const r=plan(park,[-40,-8,Math.PI],n=>n.y<-4&&n.x<-20&&ang(n.th,Math.PI)<0.15);
if(!r.n){console.log(JSON.stringify({PARKX,XE,out:'none'}));process.exit(1)}
let sw=0;for(let n=r.n;n&&n.par;n=n.par)if(n.dir!==n.par.dir&&n.par.par)sw++;if(sw){console.log(JSON.stringify({PARKX,XE,switches:sw}));if(!process.env.ALLOWSW)process.exit(1)}
const P=[];for(let n=r.n;n;n=n.par)P.unshift([n.x,n.y,n.th,n.dir]);
// smooth the steering (moving average over 3 steps, within each forward or reverse leg) and re-drive it, so the wheel turns gently
const ks=[],dss=[];for(let i=1;i<P.length;i++){const ds=P[i][3]*Math.hypot(P[i][0]-P[i-1][0],P[i][1]-P[i-1][1]);ks.push(Math.atan2(Math.sin(P[i][2]-P[i-1][2]),Math.cos(P[i][2]-P[i-1][2]))/ds);dss.push(ds)}
const k=ks.map((_,i)=>{let a=ks[i],n=1;for(const j of [i-1,i+1])if(j>=0&&j<ks.length&&Math.sign(dss[j])===Math.sign(dss[i])){a+=ks[j];n++}return a/n});
let [x,y,th]=P[0];const out=[[x,y,th,1]];
for(let i=0;i<k.length;i++){const ds=dss[i],c=k[i];if(Math.abs(c)<1e-9){x+=Math.cos(th)*ds;y+=Math.sin(th)*ds}else{const t2=th+c*ds;x+=(Math.sin(t2)-Math.sin(th))/c;y+=(-Math.cos(t2)+Math.cos(th))/c;th=t2}out.push([x,y,th,Math.sign(ds)])}
const f=p=>[+p[0].toFixed(3),+p[1].toFixed(3),+p[2].toFixed(4),p[3]];
const e=out.at(-1),inn=[];for(let d=64;d>0;d-=0.8)inn.push([e[0]-Math.cos(e[2])*d,e[1]-Math.sin(e[2])*d,e[2],1]);   // along the road from the west
inn.push([e[0],e[1],e[2],1]);for(let i=out.length-2;i>=0;i--)inn.push([out[i][0],out[i][1],out[i][2],-out[i+1][3]]);   // stop, then back along the same path (each leg driven the other way)
if(DRY){console.log(JSON.stringify({PARKX,XE,BW,out:'ok'}));process.exit(0)}
const R={wb:WB,ovr:3.1,ovf:3.16,park:[PARKX,26.63,-1.5708],in:inn.map(f),out:out.map(f)};
R.park=R.in.at(-1).slice(0,3);
fs.writeFileSync(new URL(BW?'../../3d/models/car-route-bw.js':'../../3d/models/car-route.js',import.meta.url),`// Car parking route for the 3D animation, from v1/tools/car_route_east.mjs (hybrid A*, rear-axle bicycle model, steering smoothed).
// VW Virtus: wheelbase 8'8", rear overhang 3'1", front overhang 3'2", rear-axle turning radius 11'7".
// Route along the east side: out forward (one short back-and-forth to clear the low end of ST-1A), through GT-01 near its east leaf, then east along the road;
// in from the west, stop just past the gate, reverse back along the same curve (nose to the gate). Gaps: 6" or more at the gate leaf, the pillar and the bikes.
// Plan feet: x from the east boundary, y from the road; th = heading in plan angle (direction (cos th, sin th)); dir = +1 forward, -1 reverse.
// Poses are of the rear-axle centre.
export const ${BW?'CAR_ROUTE_BW':'CAR_ROUTE'} = ${JSON.stringify(R)};
`);
console.log('in',R.in.length,'out',R.out.length,'park',R.park);
