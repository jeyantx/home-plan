import json, html as H
from model import *
from render import ground, first, svg, fmt, area
S0=svg(ground,'f0'); S1=svg(first,'f1')
def poly_area(P): return area(P)
gf=poly_area(GF_OUTLINE); porch=poly_area(rooms_G_porch()) if False else poly_area([r for r in ROOMS['G'] if r[0]=='G-02'][0][2])
ffb=poly_area(FF_OUTLINE)
land=poly_area(PLOT)
rooms={f:{r[0]:(r[1],r[2]) for r in ROOMS[f]} for f in ROOMS}
def ra(f,i): return poly_area(rooms[f][i][1])
terr=ra('F','F-02')+ra('F','F-03')+ra('F','F-01')
garden=ra('G','G-14')+ra('G','G-15')
def dims(P):
    xs=[p[0] for p in P]; ys=[p[1] for p in P]; return max(xs)-min(xs), max(ys)-min(ys)
def esc(s): return H.escape(s)
room_rows=''
for f,fl in (('G','Ground'),('F','First')):
    for rid,name,P,k in ROOMS[f]:
        w,d=dims(P); a=poly_area(P)
        size=f"{fmt(w)} x {fmt(d)}" if len(P)==4 else 'irregular'
        room_rows+=f'<tr><td class="c">{rid}</td><td>{esc(name)}</td><td>{fl}</td><td>{size}</td><td class="n">{a:.0f}</td></tr>'
KN={'outer':'9" outer','part':'4½" partition','comp':'4½" compound','para':'4½" parapet','pillar':'9" pillar','planter':'1\'6" planter pillar'}
wall_rows=''
for f,fl in (('G','Ground'),('F','First')):
    for wid,x1,x2,y1,y2,k,h,desc in WALLS[f]:
        L=max(x2-x1,y2-y1)
        wall_rows+=f'<tr><td class="c">{wid}</td><td>{esc(desc)}</td><td>{KN[k]}</td><td>{fmt(L)}</td><td>{fmt(h)}</td></tr>'
TN={'door':'Door','double':'Double door','window':'Window','vent':'Ventilator','arch':'Open arch','gate':'Gate','fold':'Folding glass window'}
import model as _mm
op_rows=''
furn_rows=''.join(f'<tr><td class="c">{f[0]}</td><td>{esc(f[2])}</td><td>{"Ground" if f[1]=="G" else "First"}</td><td>{fmt(f[3+1]-f[3])} x {fmt(f[6]-f[5])}</td><td>{esc(f[9])}</td></tr>' for f in getattr(_mm,'FURNITURE',[]))
for oid,f,wid,a,b,typ,hinge,swing,h,sill,note in OPENINGS:
    op_rows+=f'<tr><td class="c">{oid}</td><td>{TN[typ]}</td><td>{"front line" if wid=="FRONT" else wid}</td><td>{fmt(b-a)} x {fmt(h)}</td><td>{fmt(sill) if sill else "–"}</td><td>{esc(note)}<br><span class="lbl">{esc(getattr(_mm,"SPEC",{}).get(oid,""))}</span></td></tr>'
import model as _m
BN=getattr(_m,'BRANCH_NOTES','')
struct_cols=''.join(f'<tr><td class="c">{c[0]}</td><td>{esc(_mm.COL_SIZE)}</td><td>{"Ground, bars left for the future hall" if c[1]=="G" else ("Ground only, stops at the roof slab" if c[1]=="G0" else "Ground and first")}</td><td>{esc(c[6])}</td></tr>' for c in _mm.COLUMNS)
struct_beams=''.join(f'<tr><td class="c">{b[0]}</td><td>{"Ground-floor roof" if b[1]=="G" else "First-floor roof"}</td><td>9" x {esc(b[6])}</td><td>{fmt(max(b[3]-b[2],b[5]-b[4]))}</td><td>{esc(b[7])}</td></tr>' for b in _mm.BEAMS)
panel=BN+f'''
<section><h2>How to read this plan</h2>
<ul>
<li><b>X</b> is feet from the east boundary, from 0 to 21. <b>Y</b> is feet from the road, from 0 to 106. For example, "GW-05 at Y 50'" names one exact spot.</li>
<li><b>Codes:</b> G- ground-floor room or area, F- first-floor room or area, GW- ground-floor wall, FW- first-floor wall, PW- parapet, BW- boundary wall, D- door, W- window, V- ventilator, O- open arch, GT- gate, ST- staircase, UG- underground tank or pit.</li>
<li>Room sizes are clear inside the walls. Walls are drawn at true thickness: 9" outer and 4½" partitions, compound walls and parapets.</li>
<li>Use <b>Show</b> above the plan to hide codes or dimensions when you want a clean view.</li>
</ul></section>
<section><h2>What I changed from your draft</h2>
<ol>
<li>All building walls are squared to a right-angle grid. The plot boundary stays as it is, with the 1' step and the sloping back wall.</li>
<li>The house is 18'3" wide outside and 16'9" inside, leaving a 2'4½" side passage on the east. Your living room width moves from 16'7" to 16'9".</li>
<li>Toilet 1 is now 6'1½" x 4'6", up from 6' x 4'.</li>
<li>Floor to floor is set at 11'6", down from 11'9½", so staircase 1 gets whole 6" risers: 15 to the landing and 8 more to the balcony.</li>
<li>Door sizes are set: main door 4' double, room doors 3', toilet doors 2'6". Both toilet doors open inward; toilet 2's used to open into the stair hall.</li>
<li>D-05 is now a real door to the side garden instead of an open frame.</li>
<li>I added 11 windows and 2 ventilators, on the east, front and back walls only. The west wall sits on the boundary, so it has no openings.</li>
<li>Bedroom 1 had no outside wall, so it gets W-02 facing the porch, plus the study window W-01 to the front.</li>
<li>Gates: a 14'7" main sliding gate GT-01 and a 4'6" side gate GT-02 that leads straight to staircase 1, on three 9" pillars.</li>
</ol></section>
<section class="ask"><h2>Decisions for your approval</h2>
<ol>
<li><b>Floor height 11'6"</b> floor to floor, so staircase 1 works with 6" risers.</li>
<li><b>Toilet 3 (F-07) has no outside wall.</b> I recommend swapping it with the bedroom 3 lobby so it sits on FW-01 and gets a ventilator. The alternative is an exhaust fan with a duct to the roof.</li>
<li><b>No windows on the west wall</b>, since it is on the boundary next to the apartment.</li>
<li><b>W-02</b>, the bedroom 1 window, looks onto the porch. Fine for privacy, or would you prefer frosted glass?</li>
<li><b>Utility area:</b> the side garden strip under the terrace corner (F-03), from Y 75'9" to 80', is covered. It suits the washing machine and a wash area next to garden door D-05.</li>
</ol></section>
<section><h2>Areas</h2>
<table class="t">
<tr><td>Land</td><td class="n">{land:,.0f} sq ft · {land/435.6:.2f} cents</td></tr>
<tr><td>Ground floor built-up, outer faces</td><td class="n">{gf:,.0f}</td></tr>
<tr><td>Porch, covered by the floor above</td><td class="n">{porch:,.0f}</td></tr>
<tr class="tot"><td>Ground floor including porch (excluding parking)</td><td class="n">{gf+porch:,.0f}</td></tr>
<tr><td>First floor built-up, bedroom block</td><td class="n">{ffb:,.0f}</td></tr>
<tr class="tot"><td>Total built-up, both floors, including porch</td><td class="n">{gf+porch+ffb:,.0f}</td></tr>
<tr><td>Open terrace, terrace corner and balcony 2 (clear)</td><td class="n">{terr:,.0f}</td></tr>
<tr><td>Open terrace alone, for the future hall</td><td class="n">{ra("F","F-02"):,.0f}</td></tr>
<tr><td>Gardens, side and back</td><td class="n">{garden:,.0f}</td></tr>
</table></section>
<section><h2>Staircases</h2>
<ul>
<li><b>ST-1 outside stair</b>, 3'6" wide inside the west compound wall BW-07, granite treads 10", 27 risers of about 6½" from the gate crest (+6" over the road) to the first floor (+15' over the road). ST-1A runs north to south along BW-07 from Y 2'8" to 16', 17 risers. ST-1L is a 3'6" x 3'6" landing about 7'7" above the parking. ST-1B turns east over the car, 10 risers, onto balcony 2. Store FU-56 under the high end of ST-1A.</li>
<li><b>ST-2 spiral stair</b>, 5'10" across, in the stair hall. 18 risers of 7⅔", 17 oak treads of 30° and a landing; climbs anticlockwise from the west side and arrives facing east on the first-floor stair landing F-04. 6' round hole in the slab.</li>
</ul></section>
<section><h2>Furniture I will propose next (for your approval)</h2>
<ul>
<li><b>Bedrooms 1, 2 and 3:</b> queen bed with its head on the west wall, two side tables, and a 6' x 2' wardrobe. Bedroom 3's wardrobe goes in its lobby F-06.</li>
<li><b>Study G-06:</b> 4' desk under W-01 and a bookshelf on GW-10.</li>
<li><b>Living G-04:</b> L-sofa on the east wall under W-04 and W-05, TV unit with shelves on the west wall GW-05.</li>
<li><b>Foyer G-03:</b> shoe cabinet and mirror.</li>
<li><b>Kitchen G-08:</b> L-shaped counter along GW-01 with the sink under W-06, then along GW-14. Tall pantry unit and fridge, overhead shelves.</li>
<li><b>Dining G-09:</b> 4-seat table and a crockery shelf on GW-05.</li>
<li><b>Toilets:</b> WC, wash basin, shower area and geyser in each.</li>
</ul></section>
<section><h2>Existing on site</h2><ul>{''.join(f'<li><b>{b[0]} bore</b> at X {b[1]:.2f}, Y {b[2]:.2f} ({esc(b[3])}).</li>' for b in _mm.BORES)}</ul></section>
<section><h2>Still open</h2>
<ul><li><b>Neem tree.</b> At the position you gave, the trunk is 4' from staircase 1 and directly in front of the car's spot. Please confirm or correct it.</li></ul></section>
<section class="ask"><h2>Structure: pillars and beams (proposal)</h2><ol>{''.join(f'<li>{esc(n)}</li>' for n in _mm.STRUCT_NOTES)}</ol>
<div class="note">Pillars are solid black, beams are dashed red. Untick <b>Pillars and beams</b> above the plan to hide them.</div></section>
<section><h2>Pillars</h2><table class="t"><tr><th>Code</th><th>Size</th><th>Floors</th><th>Where</th></tr>{struct_cols}</table></section>
<section><h2>Beams</h2><table class="t"><tr><th>Code</th><th>Level</th><th>Size</th><th>Length</th><th>Where</th></tr>{struct_beams}</table></section>
<section><h2>Rooms and areas</h2><table class="t"><tr><th>Code</th><th>Name</th><th>Floor</th><th>Inside size</th><th class="n">sq ft</th></tr>{room_rows}</table></section>
<section><h2>Walls</h2><table class="t"><tr><th>Code</th><th>Where</th><th>Type</th><th>Length</th><th>Height</th></tr>{wall_rows}</table></section>
<section><h2>Furniture and fixtures (proposal)</h2><table class="t"><tr><th>Code</th><th>Item</th><th>Floor</th><th>Size</th><th>Where</th></tr>{furn_rows}</table></section>
<section><h2>Doors, windows, ventilators, gates</h2><table class="t"><tr><th>Code</th><th>Type</th><th>Wall</th><th>Width x height</th><th>Sill</th><th>Note and type</th></tr>{op_rows}</table></section>
'''
page=open('/Users/jeyant-10189/Work/Personal/own/home-plan/homeplan-4-my-reading.html').read()
style=page[page.index('<style>'):page.index('</style>')+8]
script=page[page.index('<script>'):page.index('</script>')+9]
style=style.replace('</style>','''
.layers{position:relative;font-size:13px}
.layers summary{list-style:none;cursor:pointer;border:1px solid var(--line);border-radius:8px;padding:7px 12px;background:var(--panel);color:var(--ink)}
.layers summary::-webkit-details-marker{display:none}
.layers summary::after{content:" ▾";color:var(--muted)}
.layers .menu{position:absolute;z-index:30;top:calc(100% + 4px);left:0;display:flex;flex-direction:column;gap:7px;padding:10px 12px;background:var(--panel);border:1px solid var(--line);border-radius:8px;box-shadow:0 6px 18px rgba(0,0,0,.14);white-space:nowrap}
.layers label{display:flex;gap:6px;align-items:center;cursor:pointer;color:var(--ink)}
td.c{font-weight:700;white-space:nowrap;color:var(--accent)}

#tip{position:fixed;z-index:50;pointer-events:none;max-width:320px;background:#1f2328;color:#fff;font-size:12.5px;line-height:1.35;padding:6px 9px;border-radius:7px;box-shadow:0 4px 14px rgba(0,0,0,.25);display:none}
#tip b{color:#9fe0bf}
.fu:hover>*{filter:brightness(1.08)}
.hide-L-garden .L-garden,.hide-L-ug .L-ug,.hide-L-struct .L-struct,.hide-L-carpath .L-carpath,.hide-L-furn .L-furn,.hide-L-rooms .L-rooms,.hide-L-walls .L-walls,.hide-L-open .L-open,.hide-L-dims .L-dims{display:none}
#measure[aria-pressed="true"]{background:var(--accent);color:var(--accent-ink);border-color:var(--accent);font-weight:600}
.mread{font-variant-numeric:tabular-nums;font-size:13px;color:var(--ink);background:var(--chip);border:1px solid var(--line);border-radius:8px;padding:5px 10px;min-height:30px;display:none;align-items:center}
.mread.on{display:inline-flex}
.measuring .sheet{cursor:crosshair}
#stage,#stage *{-webkit-user-select:none;user-select:none}   /* dragging the plan must not select its labels */
</style>''')
script=script.replace('const FULL={x:121.5,y:44.8,w:32.0,h:115.4};','const FULL={x:-5.0,y:-1.0,w:30.0,h:112.0};')
script=script.replace('const h=42, w=h*a;','const h=34, w=h*a;')
script=script[:script.index('const ROOMS=')]+'const ROOMS='+json.dumps({'f0':[{'t':r[1],'x':(min(p[0] for p in r[2])+max(p[0] for p in r[2]))/2-0,'y':107-(min(p[1] for p in r[2])+max(p[1] for p in r[2]))/2} for r in ROOMS['G']],
                                                                      'f1':[{'t':r[1],'x':(min(p[0] for p in r[2])+max(p[0] for p in r[2]))/2,'y':107-(min(p[1] for p in r[2])+max(p[1] for p in r[2]))/2} for r in ROOMS['F']]})+';'+script[script.index(';',script.index('const ROOMS='))+1:]
script=script.replace("'hp4mine-view'","'hpv1-view'")
# smooth pan and zoom on phones: while a finger or the mouse is down the drawing is only moved with a CSS transform; the viewBox (a full redraw) is set once when it lets go, and at most once a frame otherwise
_ap="function apply(){for(const k of visible()) svgs[k].setAttribute('viewBox',`${view.x} ${view.y} ${view.w} ${view.h}`)}"
assert _ap in script
script=script.replace(_ap,"""let committed=null,gesture=false,rafA=0;
function applyNow(){cancelAnimationFrame(rafA);rafA=0;for(const k of ['f0','f1']){svgs[k].style.transform='';if(visible().includes(k))svgs[k].setAttribute('viewBox',`${view.x} ${view.y} ${view.w} ${view.h}`)}committed={...view}}
function apply(){if(rafA)return;rafA=requestAnimationFrame(()=>{rafA=0;if(!gesture||!committed){applyNow();return}
  for(const k of visible()){const el=svgs[k],W=el.clientWidth||el.getBoundingClientRect().width,s1=W/view.w;el.style.transformOrigin='0 0';el.style.transform=`translate(${(committed.x-view.x)*s1}px,${(committed.y-view.y)*s1}px) scale(${committed.w/view.w})`}})}""")
_pd="el.classList.add('drag');"
assert script.count(_pd)==1
script=script.replace(_pd,"el.classList.add('drag');gesture=true;")
_end="if(!pts.size){last=null; el.classList.remove('drag')}"
assert script.count(_end)==1
script=script.replace(_end,"if(!pts.size){last=null; el.classList.remove('drag');gesture=false;applyNow()}")

script=script.replace("b.textContent=rm.t.replace(/\\n/g,' ').toLowerCase().replace(/(^|\\s)\\S/g,c=>c.toUpperCase());","b.textContent=rm.t;")
script=script.replace('</script>',"\n// ---------- hover names ----------\n(function(){\n  const t=document.createElement('div'); t.id='tip'; document.body.appendChild(t);\n  const stage=document.getElementById('stage');\n  stage.addEventListener('mousemove',e=>{\n    const el=e.target.closest('[data-tip]');\n    if(!el||!stage.contains(el)){t.style.display='none';return}\n    const s=el.getAttribute('data-tip'); const i=s.indexOf(' · ');\n    t.innerHTML=i>0?'<b>'+s.slice(0,i)+'</b> · '+s.slice(i+3).replace(/ · /g,'<br>'):s;\n    t.style.display='block';\n    const pad=14, w=t.offsetWidth, h=t.offsetHeight;\n    let x=e.clientX+pad, y=e.clientY+pad;\n    if(x+w>innerWidth-8) x=e.clientX-w-pad; if(y+h>innerHeight-8) y=e.clientY-h-pad;\n    t.style.left=x+'px'; t.style.top=y+'px';\n  });\n  stage.addEventListener('mouseleave',()=>t.style.display='none');\n  stage.addEventListener('pointerdown',()=>t.style.display='none');\n})();\n</script>")
script=script.replace('</script>','\n// ---------- measuring tool ----------\n(function(){\n  const btn=document.getElementById(\'measure\'), out=document.getElementById(\'mread\');\n  let on=false, M=null;            // M = {k, a:{x,y}, b:{x,y}, fixed}\n  const NS=\'http://www.w3.org/2000/svg\';\n  function fmtIn(ft){ let t=Math.round(Math.abs(ft)*12*2)/2; let f=Math.floor(t/12), i=t-f*12;\n    if(i>=12){f++;i-=12}\n    const ii=Number.isInteger(i)?String(i):(Math.floor(i)?Math.floor(i):\'\')+\'½\';\n    return i===0?`${f}\'`:`${f}\' ${ii}"`; }\n  function toSvg(svg,e){ const p=svg.createSVGPoint(); p.x=e.clientX; p.y=e.clientY; return p.matrixTransform(svg.getScreenCTM().inverse()); }\n  function upp(k){ const r=sheets[k].getBoundingClientRect(); return view.w/r.width; }   // svg units per screen px\n  function wallRects(svg){\n    if(svg._wr) return svg._wr;\n    svg._wr=[...svg.querySelectorAll(\'rect\')].filter(r=>{const f=r.getAttribute(\'fill\')||\'\'; return f.startsWith(\'url(#hatch\')||f===\'#6b6b6b\'})\n      .map(r=>({x:+r.getAttribute(\'x\'),y:+r.getAttribute(\'y\'),w:+r.getAttribute(\'width\'),h:+r.getAttribute(\'height\')}));\n    return svg._wr;\n  }\n  function snap(k,p,e){\n    if(e.altKey) return {x:p.x,y:p.y,s:false};\n    const R=10*upp(k); let best=null, bd=R;\n    for(const r of wallRects(svgs[k])){\n      const xs=[r.x,r.x+r.w], ys=[r.y,r.y+r.h];\n      for(const x of xs) for(const y of ys){ const d=Math.hypot(p.x-x,p.y-y); if(d<bd*1.3){bd=d/1.3;best={x,y,s:true}} }\n    }\n    if(best) return best;\n    bd=R*0.8;\n    for(const r of wallRects(svgs[k])){\n      const xs=[r.x,r.x+r.w], ys=[r.y,r.y+r.h];\n      if(p.y>=r.y-bd&&p.y<=r.y+r.h+bd) for(const x of xs){const d=Math.abs(p.x-x); if(d<bd&&p.y>=r.y&&p.y<=r.y+r.h){bd=d;best={x,y:p.y,s:true}}}\n      if(p.x>=r.x-bd&&p.x<=r.x+r.w+bd) for(const y of ys){const d=Math.abs(p.y-y); if(d<bd&&p.x>=r.x&&p.x<=r.x+r.w){bd=d;best={x:p.x,y,s:true}}}\n    }\n    return best||{x:p.x,y:p.y,s:false};\n  }\n  function constrain(a,p,e){ if(!e.shiftKey||!a) return p; return Math.abs(p.x-a.x)>=Math.abs(p.y-a.y)?{...p,y:a.y}:{...p,x:a.x}; }\n  function layer(k){ let g=svgs[k].querySelector(\'#mlayer-\'+k); if(!g){g=document.createElementNS(NS,\'g\'); g.id=\'mlayer-\'+k; svgs[k].appendChild(g)} return g; }\n  function clearAll(){ for(const k of [\'f0\',\'f1\']){const g=svgs[k].querySelector(\'#mlayer-\'+k); if(g) g.innerHTML=\'\'} }\n  function el(tag,attrs,parent){ const n=document.createElementNS(NS,tag); for(const a in attrs) n.setAttribute(a,attrs[a]); parent.appendChild(n); return n; }\n  function draw(hover){\n    clearAll(); if(!M) { out.textContent=on?\'Click the first point\':\'\'; return; }\n    const k=M.k, u=upp(k), g=layer(k), a=M.a, b=M.b||hover;\n    const dot=(p,s)=>{ el(\'circle\',{cx:p.x,cy:p.y,r:4.5*u,fill:\'#fff\',stroke:s?\'#d1495b\':\'#1f6fb2\',\'stroke-width\':2*u},g); };\n    if(b){\n      el(\'line\',{x1:a.x,y1:a.y,x2:b.x,y2:b.y,stroke:\'#fff\',\'stroke-width\':5*u,\'stroke-linecap\':\'round\'},g);\n      el(\'line\',{x1:a.x,y1:a.y,x2:b.x,y2:b.y,stroke:\'#d1495b\',\'stroke-width\':2.2*u,\'stroke-dasharray\':M.b?\'none\':`${6*u} ${4*u}`},g);\n      const d=Math.hypot(b.x-a.x,b.y-a.y), dx=Math.abs(b.x-a.x), dy=Math.abs(b.y-a.y);\n      const txt=fmtIn(d);\n      const mx=(a.x+b.x)/2, my=(a.y+b.y)/2, fs=14*u;\n      const t=el(\'text\',{x:mx,y:my-8*u,\'font-size\':fs,\'font-weight\':700,\'text-anchor\':\'middle\',fill:\'#1f2328\'},g); t.textContent=txt;\n      const bb=t.getBBox(); const bg=el(\'rect\',{x:bb.x-5*u,y:bb.y-3*u,width:bb.width+10*u,height:bb.height+6*u,rx:4*u,fill:\'#fff\',stroke:\'#d1495b\',\'stroke-width\':1.2*u},g);\n      g.insertBefore(bg,t);\n      dot(a,a.s); dot(b,b.s);\n      out.innerHTML=`<b>${txt}</b>&nbsp; across ${fmtIn(dx)} · along ${fmtIn(dy)}${M.b?\'\':\' · click to fix\'}`;\n    } else { dot(a,a.s); out.textContent=\'Move and click the second point\'; }\n  }\n  function setOn(v){ on=v; btn.setAttribute(\'aria-pressed\',v); document.body.classList.toggle(\'measuring\',v); out.classList.toggle(\'on\',v); if(!v){M=null; clearAll(); out.textContent=\'\'} else draw(); }\n  btn.addEventListener(\'click\',()=>setOn(!on));\n  document.addEventListener(\'keydown\',e=>{\n    if(e.target.matches(\'input,textarea\')) return;\n    if(e.key===\'m\'||e.key===\'M\') setOn(!on);\n    if(e.key===\'Escape\'){ if(M){M=null;draw()} else setOn(false) }\n  });\n  for(const k of [\'f0\',\'f1\']){\n    const sh=sheets[k]; let down=null;\n    sh.addEventListener(\'pointerdown\',e=>{ down={x:e.clientX,y:e.clientY} });\n    sh.addEventListener(\'pointerup\',e=>{\n      if(!on||!down) return; const moved=Math.hypot(e.clientX-down.x,e.clientY-down.y); down=null;\n      if(moved>4) return;                       // it was a pan, not a click\n      let p=snap(k,toSvg(svgs[k],e),e);\n      if(!M||M.b||M.k!==k){ M={k,a:p,b:null}; }\n      else { p=constrain(M.a,p,e); M.b=p; }\n      draw();\n    });\n    sh.addEventListener(\'pointermove\',e=>{\n      if(!on||!M||M.b||M.k!==k) return;\n      let p=snap(k,toSvg(svgs[k],e),e); p=constrain(M.a,p,e); draw(p);\n    });\n  }\n  const _apply=apply; apply=function(){ _apply(); if(on&&M&&M.b) draw(); };\n})();\n</script>')
script=script.replace('</script>','''
for(const cb of document.querySelectorAll('.layers input')){
  const k='hpv1-'+cb.dataset.layer; try{ const v=localStorage.getItem(k); if(v==='0') cb.checked=false; if(v==='1') cb.checked=true }catch(e){}
  const ap=()=>{document.body.classList.toggle('hide-'+cb.dataset.layer,!cb.checked); try{localStorage.setItem(k,cb.checked?'1':'0')}catch(e){}};
  cb.addEventListener('change',ap); ap();
}
// share: the floor and the Show layers go into the link (?floor=f0&hide=dims,furn&show=carpath), so the same plan opens for someone else; it always opens fitted to the screen
(function(){
  const Q=new URLSearchParams(location.search),cbs=[...document.querySelectorAll('.layers input')],nm=cb=>cb.dataset.layer.slice(2).toLowerCase();
  const hide=(Q.get('hide')||'').split(',').filter(Boolean),show=(Q.get('show')||'').split(',').filter(Boolean);
  if(Q.has('hide')||Q.has('show'))for(const cb of cbs){const n=nm(cb);cb.checked=hide.includes(n)?false:show.includes(n)?true:cb.defaultChecked;cb.dispatchEvent(new Event('change'))}
  const fl=Q.get('floor');if(['f0','f1','both'].includes(fl))setMode(fl);
  let t=0;
  function write(){clearTimeout(t);t=setTimeout(()=>{const P=new URLSearchParams(),H=cbs.filter(cb=>cb.defaultChecked&&!cb.checked).map(nm),S=cbs.filter(cb=>!cb.defaultChecked&&cb.checked).map(nm);
    if(mode!=='both')P.set('floor',mode);if(H.length)P.set('hide',H.join(','));if(S.length)P.set('show',S.join(','));
    const q=P.toString().replace(/%2C/g,','),qs=q?'?'+q:location.pathname;history.replaceState(null,'',qs+location.hash);
    try{if(parent!==window){const pl=parent.location,PP=new URLSearchParams(pl.search);for(const k of ['floor','hide','show'])PP.delete(k);for(const [k,v] of P)PP.set(k,v);const pq=PP.toString().replace(/%2C/g,',');parent.history.replaceState(null,'',pl.pathname+(pq?'?'+pq:'')+pl.hash)}}catch(e){}},300)}   // the app page shows the same link
  cbs.forEach(cb=>cb.addEventListener('change',write));
  const _sm=setMode;setMode=function(m){_sm(m);write()};
})();
</script>''')
import subprocess as _sp
BRANCH=_sp.run(['git','rev-parse','--abbrev-ref','HEAD'],capture_output=True,text=True).stdout.strip() or 'main'
out=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Home Plan v1</title>
<link rel="icon" type="image/png" href="favicon.png">
{style}</head><body>
<header>
 <div><h1>Home plan · {BRANCH}</h1></div>
 <div class="seg" role="group" aria-label="View">
  <button data-view="f0">Ground floor</button><button data-view="f1">First floor</button><button data-view="both">Side by side</button>
 </div>
 <details class="layers"><summary>Show</summary><div class="menu">
  <label><input type="checkbox" data-layer="L-rooms" checked>Rooms</label>
  <label><input type="checkbox" data-layer="L-walls" checked>Wall codes</label>
  <label><input type="checkbox" data-layer="L-open" checked>Door and window codes</label>
  <label><input type="checkbox" data-layer="L-dims" checked>Dimensions</label>
  <label><input type="checkbox" data-layer="L-furn" checked>Furniture</label>
  <label><input type="checkbox" data-layer="L-garden" checked>Garden</label>
  <label><input type="checkbox" data-layer="L-struct" checked>Pillars and beams</label>
  <label><input type="checkbox" data-layer="L-carpath">Car path</label>
  <label><input type="checkbox" data-layer="L-ug" checked>Tanks and pits (underground)</label>
 </div></details>
 <div id="mread" class="mread" aria-live="polite"></div>
 <div class="tools" role="group" aria-label="Zoom">
  <button id="zin" title="Zoom in" aria-label="Zoom in">+</button><button id="zout" title="Zoom out" aria-label="Zoom out">&minus;</button><button id="measure" title="Measure distance (M). Click start, click end. Shift = straight line, Alt = no snap, Esc = clear" aria-pressed="false">Measure</button><button id="fit" title="Fit whole plan">Fit</button><button id="theme" title="Toggle light or dark" aria-label="Toggle theme">◐</button>
 </div>
</header>
<main>
 <aside>
  <section><h2>Jump to a room</h2>
   <div class="note">Ground floor</div><div class="roomlinks" id="list-f0"></div>
   <div class="note" style="margin-top:8px">First floor</div><div class="roomlinks" id="list-f1"></div>
  </section>
  {panel}
 </aside>
 <div id="stage">
  <div class="sheet" id="sheet-f0"><div class="tag">Ground floor</div>{S0}</div>
  <div class="sheet" id="sheet-f1"><div class="tag">First floor</div>{S1}</div>
 </div>
</main>
{script}
</body></html>'''
import subprocess
br=subprocess.run(['git','rev-parse','--abbrev-ref','HEAD'],capture_output=True,text=True).stdout.strip() or 'main'
open(f'/Users/jeyant-10189/Work/Personal/own/home-plan/home-plan-{br}.html','w').write(out)
print(len(out)//1024,'KB', 'land',round(land),'gf',round(gf),'ffb',ffb,'terr',round(terr),'garden',round(garden))

# ---------------- app: one page with tabs (3D, 2D, and the details), index.html at the repo root ----------------
import re as _re
ROOT='/Users/jeyant-10189/Work/Personal/own/home-plan/'
_secs=_re.findall(r'<section.*?</section>',panel,_re.S)
_title=lambda s:(_re.search(r'<h2>(.*?)</h2>',s) or [None,''])[1]
_how=next(s for s in _secs if _title(s).startswith('How to read'))
# 2D tab: the plan with only the room list and the reading guide beside it
open(ROOT+'plan-2d.html','w').write(out.replace(panel,_how).replace(f'<div><h1>Home plan · {BRANCH}</h1></div>',''))   # the app's tab already names it
GROUPS=[('overview','Overview',lambda t:t.startswith(('Areas','Staircases','Existing on site','Still open','How to read'))),
        ('details','Details',lambda t:t.startswith(('Garden plan','Modular kitchen','Side garden utility','Water and drainage','Parking plan','Outside windows','Raised site levels','Tree pit','Rooms and areas','Walls','Doors, windows','Structure','Pillars','Beams','Furniture')))]
_tidy=lambda s:_re.sub(r' \((branch [\w-]+|approved), ?(from [\w-]+)?[^)]*\)','',s)
_slug=lambda t:'d-'+_re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-')[:40]
_used=set();_tabs=[]
for key,name,test in GROUPS:
    picked=[_tidy(s) for i,s in enumerate(_secs) if i not in _used and test(_title(s)) and not _used.add(i)]
    if key=='details':   # one page, in a sensible order, with short jump links to each part
        ORDER=[('Garden plan','Garden'),('Modular kitchen','Modular kitchen'),('Side garden utility','Utility and window'),('Water and drainage','Water and drainage'),('Parking plan','Parking'),('Outside windows','Outside windows'),('Raised site levels','Site levels'),('Tree pit','Tree pit'),('Rooms and areas','Rooms'),('Walls','Walls'),
               ('Doors, windows','Doors and windows'),('Structure','Structure'),('Pillars','Pillars'),('Beams','Beams'),('Furniture I will','Furniture plan'),('Furniture and fixtures','Furniture list')]
        rank=lambda s:next((i for i,(p,_) in enumerate(ORDER) if _title(s).startswith(p)),99)
        chip=lambda s:next((c for p,c in ORDER if _title(s).startswith(p)),_title(s))
        picked=sorted(picked,key=rank)
        picked=[s.replace('<section',f'<section id="{_slug(_title(s))}"',1) for s in picked]
        body='<nav class="jump">'+''.join(f'<a href="#{_slug(_title(s))}">{chip(s)}</a>' for s in picked)+'</nav>'+''.join(picked)
    else: body=''.join(picked)
    _tabs.append((key,name,body))
def _md(md):   # small Markdown to HTML for the credits tab (headings, tables, lists, paragraphs, `code`, links)
    import html as _h
    def inl(t):
        t=_h.escape(t);t=_re.sub(r'`([^`]+)`',r'<code>\1</code>',t)
        return _re.sub(r'(https?://[^\s|<)]+)',r'<a href="\1" target="_blank" rel="noopener">\1</a>',t)
    out,sec,rows,lst=[],[],[],[]
    def flush():
        nonlocal rows,lst
        if rows:
            hd,*bd=[r for r in rows if not _re.match(r'^\|[-| ]+\|$',r)]
            cells=lambda r:[c.strip() for c in r.strip('|').split('|')]
            sec.append('<table class="t"><tr>'+''.join(f'<th>{inl(c)}</th>' for c in cells(hd))+'</tr>'+''.join('<tr>'+''.join(f'<td>{inl(c)}</td>' for c in cells(r))+'</tr>' for r in bd)+'</table>');rows=[]
        if lst: sec.append('<ul>'+''.join(f'<li>{inl(x)}</li>' for x in lst)+'</ul>');lst=[]
    for line in md.split('\n'):
        if line.startswith('# '): continue
        if line.startswith('## '):
            flush()
            if sec and sec[0].startswith('<h2>'): out.append('<section>'+''.join(sec)+'</section>')
            sec=[f'<h2>{inl(line[3:])}</h2>'];continue
        if line.startswith('|'): rows.append(line.strip());continue
        if line.startswith('- '): lst.append(line[2:]);continue
        flush()
        if line.strip(): sec.append(f'<p class="note">{inl(line)}</p>')
    flush()
    if sec: out.append('<section>'+''.join(sec)+'</section>')
    return ''.join(out)
_tabs.append(('credits','Credits','<section><h2>Credits</h2><p>Libraries, textures, the sky image and the downloaded 3D models used by this plan, with their sources and licences. Everything else (the plan, the drawings and the code-made models) was made for this house.</p></section>'+_md(open(ROOT+'3d/ASSETS.md').read())))
def _btn(k,n): return f'<button role="tab" data-tab="{k}" aria-selected="false">{n}</button>'
app=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Home Plan</title>
<link rel="icon" type="image/png" href="favicon.png"><link rel="apple-touch-icon" href="favicon.png">
<meta name="description" content="Every good gift and every perfect present is from above, coming down from the Father of the celestial lights - James 1:17">
<meta property="og:title" content="Home Plan"><meta property="og:description" content="Every good gift and every perfect present is from above, coming down from the Father of the celestial lights - James 1:17"><meta property="og:type" content="website"><meta property="og:site_name" content="Home Plan"><meta property="og:url" content="https://jeyantx.github.io/home-plan/">
<meta property="og:image" content="https://jeyantx.github.io/home-plan/og-image-2.png"><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Home Plan: house icon and James 1:17">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="https://jeyantx.github.io/home-plan/og-image-2.png">

<style>
:root{{--bg:#f4f2ee;--panel:#ffffff;--ink:#1f2328;--muted:#5d646d;--line:#dcd8d0;--accent:#2f6f4f;--accent-ink:#fff;--chip:#eef3ef}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#16181b;--panel:#1f2226;--ink:#e8e6e1;--muted:#a3a8ae;--line:#33373c;--accent:#5fb08a;--accent-ink:#0d1a13;--chip:#23302a}}}}
:root[data-theme="dark"]{{--bg:#16181b;--panel:#1f2226;--ink:#e8e6e1;--muted:#a3a8ae;--line:#33373c;--accent:#5fb08a;--accent-ink:#0d1a13;--chip:#23302a}}
*{{box-sizing:border-box}}html,body{{height:100%;margin:0}}
body{{background:var(--bg);color:var(--ink);font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;display:flex;flex-direction:column}}
header{{display:flex;align-items:center;gap:14px;padding:8px 16px 0;background:var(--panel);border-bottom:1px solid var(--line)}}
h1{{font-size:16px;margin:0 6px 8px 0;font-weight:650;white-space:nowrap}}
nav{{display:flex;gap:2px;overflow-x:auto;scrollbar-width:none}}nav::-webkit-scrollbar{{display:none}}
nav button{{border:0;background:transparent;color:var(--muted);font:inherit;font-weight:550;padding:8px 12px 10px;cursor:pointer;white-space:nowrap;border-bottom:2px solid transparent}}
nav button:hover{{color:var(--ink)}}
nav button[aria-selected="true"]{{color:var(--accent);border-bottom-color:var(--accent)}}
main{{flex:1;min-height:0;position:relative}}
.pane{{position:absolute;inset:0;display:none;overflow:auto}}
.pane.on{{display:block}}
.pane iframe{{border:0;width:100%;height:100%;display:block;background:var(--bg)}}
.doc{{max-width:980px;margin:0 auto;padding:20px 16px 48px}}
.doc section{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 18px;margin:0 0 14px}}
.doc section.ask{{background:var(--chip)}}
.doc section{{overflow-x:auto}}
.doc h2{{font-size:15px;margin:0 0 8px}}
.doc ul,.doc ol{{margin:0;padding-left:20px}}.doc li{{margin:4px 0}}
.t{{width:100%;border-collapse:collapse;font-size:13px}}
.t th{{text-align:left;font-weight:600;color:var(--muted);border-bottom:1px solid var(--line);padding:5px 6px}}
.t td{{border-bottom:1px solid var(--line);padding:5px 6px;vertical-align:top}}
.t .n{{text-align:right;font-variant-numeric:tabular-nums}}.t .lbl{{color:var(--muted)}}.t tr.tot td{{font-weight:650}}
td.c{{font-weight:700;white-space:nowrap;color:var(--accent)}}
.note{{color:var(--muted);font-size:12.5px;margin:6px 0 0}}\n.doc code{{font:12px ui-monospace,Menlo,monospace;background:var(--chip);padding:1px 4px;border-radius:4px}}\n.doc a{{color:var(--accent)}}\n.jump{{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 14px}}.jump a{{font-size:12.5px;text-decoration:none;border:1px solid var(--line);background:var(--panel);border-radius:999px;padding:4px 10px;color:var(--ink)}}.jump a:hover{{border-color:var(--accent);color:var(--accent)}}\n.doc section{{scroll-margin-top:12px}}.doc p{{margin:6px 0}}
.wide{{overflow-x:auto}}
.keys{{margin-left:auto;display:flex;flex-wrap:wrap;justify-content:flex-end;gap:3px 12px;font-size:11.5px;color:var(--muted);padding:4px 0 6px;min-width:0}}
.keys[hidden]{{display:none}}
.keys span{{white-space:nowrap}}
nav{{flex:none}}
kbd{{display:inline-block;min-width:18px;text-align:center;font:600 11px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-bottom-width:2px;border-radius:5px;padding:0 4px;margin-right:2px}}
@media (max-width:1000px){{.keys{{display:none!important}}}}
@media (max-width:640px){{header{{flex-direction:column;align-items:stretch;gap:0}}h1{{margin:0 0 4px}}.doc{{padding:12px 10px 40px}}}}
</style></head><body>
<header><h1>Home Plan</h1><nav role="tablist">{_btn('3d','3D view')}{_btn('2d','2D plan')}{_btn('kitchen','Kitchen')}{''.join(_btn(k,n) for k,n,b in _tabs if b)}</nav>
<div class="keys" id="keys-3d" hidden><span><kbd>↑</kbd><kbd>↓</kbd> walk</span><span><kbd>←</kbd><kbd>→</kbd> turn</span><span><kbd>A</kbd><kbd>D</kbd> step sideways</span><span><kbd>W</kbd><kbd>S</kbd> look up / down</span><span><kbd>Q</kbd><kbd>E</kbd> lower / raise</span><span><kbd>Shift</kbd> faster</span><span>drag: look round</span><span>scroll: walk</span><span>right-drag: slide</span></div>
<div class="keys" id="keys-kitchen" hidden><span>click a door or drawer: open / close</span><span><kbd>↑</kbd><kbd>↓</kbd> walk</span><span><kbd>←</kbd><kbd>→</kbd> turn</span><span><kbd>A</kbd><kbd>D</kbd> step sideways</span><span><kbd>W</kbd><kbd>S</kbd> look up / down</span><span><kbd>Q</kbd><kbd>E</kbd> lower / raise</span><span><kbd>Shift</kbd> faster</span><span>drag: turn round</span><span>scroll: zoom</span></div></header>
<main>
<div class="pane" id="p-3d"><iframe data-src="3d/living-room.html" title="3D view" allow="fullscreen"></iframe></div>
<div class="pane" id="p-2d"><iframe data-src="plan-2d.html" title="2D plan"></iframe></div>
<div class="pane" id="p-kitchen"><iframe data-src="3d/kitchen.html" title="Modular kitchen"></iframe></div>
{''.join(f'<div class="pane" id="p-{k}"><div class="doc wide">{b}</div></div>' for k,n,b in _tabs if b)}
</main>
<script>
const tabs=[...document.querySelectorAll('nav button')];
function show(k){{if(!document.getElementById('p-'+k))k='3d';
  tabs.forEach(b=>b.setAttribute('aria-selected',b.dataset.tab===k));
  document.querySelectorAll('.pane').forEach(p=>p.classList.toggle('on',p.id==='p-'+k));
  const f=document.querySelector('#p-'+k+' iframe');if(f&&!f.src)f.src=f.dataset.src+(k==='2d'||k==='3d'?location.search:'');   // the 2D plan and the 3D view read their settings from the link
  if(f){{const fo=()=>{{try{{f.contentWindow.focus()}}catch(e){{}}}};fo();f.addEventListener('load',fo,{{once:true}})}}   // give the keyboard to the page shown, so the arrow keys work without a click first
  document.getElementById('keys-3d').hidden=k!=='3d';document.getElementById('keys-kitchen').hidden=k!=='kitchen';   // key help for the 3D tabs, top right   // load the 2D and 3D pages the first time they are opened
  if(location.hash!=='#'+k)history.replaceState(null,'','#'+k);try{{localStorage.setItem('hp-tab',k)}}catch(e){{}}}}
tabs.forEach(b=>b.onclick=()=>show(b.dataset.tab));
document.querySelectorAll('.jump a').forEach(a=>a.onclick=e=>{{e.preventDefault();document.querySelector(a.getAttribute('href')).scrollIntoView({{behavior:'smooth',block:'start'}})}});
window.addEventListener('hashchange',()=>show(location.hash.slice(1)));
let first=location.hash.slice(1);if(!first){{try{{first=localStorage.getItem('hp-tab')||''}}catch(e){{}}}}show(first||'3d');
</script></body></html>'''
open(ROOT+'index.html','w').write(app)
print('app tabs:',[(k,len(b)) for k,n,b in _tabs])
