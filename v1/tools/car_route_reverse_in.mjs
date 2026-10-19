import fs from 'fs';
let src=fs.readFileSync('car_route_plan.mjs','utf8');src=src.slice(0,src.indexOf('const S2=Math.PI/2;'));
src='import fs from "fs";\n'+src+`const S2=Math.PI/2;const N2=-Math.PI/2;
const trace=n=>{const out=[];while(n){out.push([+n.x.toFixed(3),+n.y.toFixed(3),+n.th.toFixed(4),n.dir]);n=n.par}return out.reverse()};
const segs=t=>{let c=0;for(let i=1;i<t.length;i++)if(t[i][3]!==t[i-1][3])c++;return c};
for(const X of [12.125]){ for(const st of [[-35,-10,0],[45,-6,Math.PI]]){
 const g=[X,29.73-(OVR-MARGIN),N2];
 const r=plan(st,g,n=>Math.hypot(n.x-g[0],n.y-g[1])<0.35&&Math.abs(Math.atan2(Math.sin(n.th-N2),Math.cos(n.th-N2)))<0.05);
 if(!r.n){console.log('X',X,'start',st[0],'none');continue}
 const tin=trace(r.n);const o=plan(g,[-40,-8,Math.PI],n=>n.y<-4&&((n.x>20&&Math.abs(Math.atan2(Math.sin(n.th),Math.cos(n.th)))<0.15)||(n.x<-20&&Math.abs(Math.atan2(Math.sin(n.th-Math.PI),Math.cos(n.th-Math.PI)))<0.15)));const tout=o.n?trace(o.n):null;
 console.log('X',X,'start',st[0],'in switches',segs(tin),'out',tout?segs(tout):'none');
 fs.writeFileSync('/private/tmp/claude-502/-Users-jeyant-10189-Work-Personal-own-home-plan/a6a05a08-bd66-45fc-af13-b4dc4af51ba5/scratchpad/route6-rev-'+X+'-'+(st[0]<0?'E':'W')+'.json',JSON.stringify({in:tin,out:tout,WB,OVR:OVR-MARGIN,OVF:OVF-MARGIN,margin:MARGIN}))}}
`;fs.writeFileSync('/private/tmp/claude-502/-Users-jeyant-10189-Work-Personal-own-home-plan/a6a05a08-bd66-45fc-af13-b4dc4af51ba5/scratchpad/rev6_run.mjs',src);
