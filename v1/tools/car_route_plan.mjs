// hybrid A* for a car (rear-axle bicycle model), plan feet; X west, Y south; heading th: direction (sin th, cos th)?? use (cos th, sin th) in plan axes
const WB=8.7, OVR=3.1, OVF=14.96-8.7-3.1, HW=5.75/2+0.06;   // wheelbase, rear and front overhang, half width + ¾" margin
const RMIN=11.6;   // rear-axle turning radius (VW Virtus ~5.05 m kerb-to-kerb)
const bikes=process.argv[2]==='bikes';
const rects=[[17.125,20.625,2.667,16.2],[12,13.5,-0.2,1.5],[-1,0.75,-0.2,0.75],[13.5,22,-0.2,0.75],[2.75,21,30.75,40],[0.375,1.125,19.75,20.75],[-5,0.375,0.75,40],[20.625,30,0.75,40],[3.5,8.25,30.75,33.25],
  [0.8,1.4,0.3,3.2],[11.35,11.95,0.3,3.2],   // GT-01 leaves folded open at their hinges
  [-60,80,-30,-16.5],[-60,-0.01,-0.01,0.01],[21,80,-0.01,0.01]];   // far kerb of the road; boundary line either side of our gate
if(bikes) rects.push([1.29,3.91,12.75,19.49],[1.39,3.81,20.25,26.3]);
const circles=[[12.75,4.25,2.75]];
function corners(x,y,th){const c=Math.cos(th),s=Math.sin(th);const pts=[];for(const [a,b] of [[-OVR,-HW],[WB+OVF,-HW],[WB+OVF,HW],[-OVR,HW]])pts.push([x+c*a-s*b,y+s*a+c*b]);return pts}
function collide(x,y,th){const P=corners(x,y,th);const c=Math.cos(th),s=Math.sin(th);
  for(const [x1,x2,y1,y2] of rects){ // SAT
    let sep=false;const R=[[x1,y1],[x2,y1],[x2,y2],[x1,y2]];
    for(const [ax,ay] of [[1,0],[0,1],[c,s],[-s,c]]){let a1=1e9,a2=-1e9,b1=1e9,b2=-1e9;for(const [px,py] of P){const v=px*ax+py*ay;a1=Math.min(a1,v);a2=Math.max(a2,v)}for(const [px,py] of R){const v=px*ax+py*ay;b1=Math.min(b1,v);b2=Math.max(b2,v)}if(a2<b1||b2<a1){sep=true;break}}
    if(!sep)return true}
  for(const [cx,cy,r] of circles){const dx=cx-x,dy=cy-y,lu=dx*c+dy*s,lv=-dx*s+dy*c;const qu=Math.max(-OVR,Math.min(WB+OVF,lu)),qv=Math.max(-HW,Math.min(HW,lv));if(Math.hypot(lu-qu,lv-qv)<r)return true}
  return false}
const STEP=0.8, ST=[-1,-0.5,0,0.5,1];
function key(x,y,th){return Math.round(x*2)+','+Math.round(y*2)+','+(((Math.round(th/(Math.PI/24))%48)+48)%48)}
function plan(start,goal,goalTol){
  const open=[],seen=new Map();const h=(x,y,th)=>Math.hypot(goal[0]-x,goal[1]-y)+2*Math.abs(Math.atan2(Math.sin(goal[2]-th),Math.cos(goal[2]-th)));
  const push=n=>{open.push(n);let i=open.length-1;while(i>0){const p=(i-1)>>1;if(open[p].f<=open[i].f)break;[open[p],open[i]]=[open[i],open[p]];i=p}};
  const pop=()=>{const t=open[0],l=open.pop();if(open.length){open[0]=l;let i=0;for(;;){const a=2*i+1,b=a+1;let m=i;if(a<open.length&&open[a].f<open[m].f)m=a;if(b<open.length&&open[b].f<open[m].f)m=b;if(m===i)break;[open[m],open[i]]=[open[i],open[m]];i=m}}return t};
  push({x:start[0],y:start[1],th:start[2],g:0,f:0,dir:1,par:null});let it=0;
  while(open.length&&it<6000000){it++;const n=pop();const k=key(n.x,n.y,n.th);if(seen.has(k)&&seen.get(k)<=n.g)continue;seen.set(k,n.g);
    if(goalTol(n))return {n,it};
    for(const dir of [1,-1])for(const sv of ST){const curv=sv/RMIN;let x=n.x,y=n.y,th=n.th,ok=true;const sub=4;
      for(let j=0;j<sub;j++){const ds=dir*STEP/sub;if(Math.abs(curv)<1e-9){x+=Math.cos(th)*ds;y+=Math.sin(th)*ds}else{const th2=th+curv*ds;x+=(Math.sin(th2)-Math.sin(th))/curv;y+=(-Math.cos(th2)+Math.cos(th))/curv;th=th2}
        if(collide(x,y,th)){ok=false;break}}
      if(!ok)continue;
      const g=n.g+STEP*(dir<0?1.6:1)+(dir!==n.dir?+(process.env.SW||6):0)+Math.abs(sv)*0.05;
      push({x,y,th,g,f:g+h(x,y,th)*1.2,dir,sv,par:n})}}
  return {n:null,it}}
const S2=Math.PI/2;
// in: from the road (driving west along the far lane) to the spot, nose south
const park=[+(process.argv[3]||13),29.73-WB-OVF,S2];   // rear axle so the front sits 1' from the wall
const rin=plan([-35,-10,0],park,n=>Math.hypot(n.x-park[0],n.y-park[1])<0.35&&Math.abs(Math.atan2(Math.sin(n.th-S2),Math.cos(n.th-S2)))<0.05);
const trace=n=>{const out=[];while(n){out.push([+n.x.toFixed(3),+n.y.toFixed(3),+n.th.toFixed(4),n.dir]);n=n.par}return out.reverse()};
const segs=t=>{let c=0;for(let i=1;i<t.length;i++)if(t[i][3]!==t[i-1][3])c++;return c};
if(!rin.n){console.log('IN: no path',rin.it);process.exit(0)}
const tin=trace(rin.n);
// out: from the spot back onto the road, then away west along the road
const rout=plan([rin.n.x,rin.n.y,rin.n.th],[40,-8,0],n=>n.y<-4&&n.x>20&&Math.abs(Math.atan2(Math.sin(n.th),Math.cos(n.th)))<0.15);
const tout=rout.n?trace(rout.n):null;
console.log(JSON.stringify({bikes,inSteps:tin.length,inSwitch:segs(tin),outSteps:tout&&tout.length,outSwitch:tout&&segs(tout)}));
import fs from 'fs';fs.writeFileSync('route'+(bikes?'-bikes':'')+'.json',JSON.stringify({in:tin,out:tout,WB,OVR,OVF}));
