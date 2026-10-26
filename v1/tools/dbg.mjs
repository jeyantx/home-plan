import fs from 'fs';
process.env.MARGIN='0.25';
let src=fs.readFileSync(new URL('car_route_plan.mjs',import.meta.url),'utf8');src=src.slice(0,src.indexOf('const S2=Math.PI/2;'));
const BIKES=[[0.55,2.96,20.75,27.71],[3.2,5.62,21.67,27.7]],PLAT=[[12.5,17.125,6.2,11.0],[13.5,17.125,2.667,6.2]];
src+=`for(const b of ${JSON.stringify([...BIKES,...PLAT])})rects.push([b[0]-0.25,b[1]+0.25,b[2]-0.25,b[3]+0.25]);
for(const c of circles)c[2]+=0.25;
for(const r of rects)if((r[0]===0.8&&r[1]===1.4)||(r[0]===-1&&r[1]===0.75)){r[0]-=0.25;r[1]+=0.25;r[2]-=0.25;r[3]+=0.25}
export {plan};`;
const tmp=new URL('./.dbg_tmp.mjs',import.meta.url);fs.writeFileSync(tmp,src);const {plan}=await import(tmp.href);fs.unlinkSync(tmp);
const ang=(a,b)=>Math.abs(Math.atan2(Math.sin(a-b),Math.cos(a-b)));
const park=[14,28.73-3.1,-Math.PI/2];
for(const g1 of [[-40,-8,Math.PI],[-40,-8,-Math.PI/2],[6,-6,-Math.PI/2+0.001],[6,-6,-Math.PI/2],[10,-8,-Math.PI/2],[8,-10,-0.8],[4,-8,-Math.PI/2]]){
 const r1=plan(park,g1,n=>n.y<-2&&ang(n.th,g1[2])<0.4);
 if(!r1.n){console.log(g1,'s1 none',r1.it);continue}
 const r2=plan([r1.n.x,r1.n.y,r1.n.th],[45,-5,0],n=>n.x>26&&n.y<-1&&ang(n.th,0)<0.2);
 let sw=0,c=0;for(const r of [r1,r2])for(let n=r.n;n&&n.par;n=n.par){c++;if(n.dir!==n.par.dir&&n.par.par)sw++}
 console.log(g1,'s1',r1.n.x.toFixed(1),r1.n.y.toFixed(1),'s2',!!r2.n,r2.it,'sw',sw,'steps',c);
}
