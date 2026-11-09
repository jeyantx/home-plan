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
terr=ra('F','F-02')+ra('F','F-01')
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
<li><b>Utility area:</b> the side garden strip under toilet 3 (F-07), from Y 75'9" to 80', is covered. It suits the washing machine and a wash area next to garden door D-05.</li>
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
<li><b>ST-1 outside stair</b>, 3'6" wide inside the west compound wall BW-07, granite treads 10", 27 risers of about 6½" from the gate crest (+6" over the road) to the first floor (+15' over the road). ST-1A runs north to south along BW-07 from Y 2'8" to 16', 17 risers. ST-1L is a 3'6" x 3'6" landing about 7'7" above the parking. ST-1B turns east over the car, 10 risers, onto balcony 2. Open under the high end of ST-1A (no store), clear of the car.</li>
<li><b>ST-2 spiral stair</b>, 5'10" across, in the stair hall. 21 risers of about 6½", 20 oak treads of 25½° and a landing; climbs anticlockwise from the west side and arrives facing east on the first-floor stair landing F-04. 6' round hole in the slab.</li>
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

def _store_tab():   # Store tab: FU-25 front elevation (looking west, north end on the right), every cell named, kadappa cutting list
    S=getattr(_mm,'STORE',None)
    if not S: return ''
    import html as _h
    B={b['id']:b for b in S['bays']};t=S['upright'];Y0,Y1=S['bays'][0]['y1'],S['bays'][-1]['y2'];lz=S['loftz'];D=S['inner']
    def span(c):   # clear width of a cell: bay edges minus the uprights (full at the two ends, half between bays)
        ya,yb=B[c['bays'][0]]['y1'],B[c['bays'][-1]]['y2']
        return ya,yb,(yb-ya)-(t if abs(ya-Y0)<0.01 else t/2)-(t if abs(yb-Y1)<0.01 else t/2)
    k=60;ox,oy=40,34;W=(Y1-Y0)*k;H=S['top']*k
    X=lambda y:ox+(Y1-y)*k; Z=lambda z:oy+(S['top']-z)*k
    KAD='#8f9399'
    e=[f'<svg viewBox="0 0 {W+ox+120:.0f} {H+oy+64:.0f}" style="width:100%;max-width:980px;background:#f7f4ee;border:1px solid var(--line);border-radius:10px" font-family="system-ui,sans-serif">',
       f'<text x="{ox+W/2:.1f}" y="{oy-12}" font-size="12" text-anchor="middle" fill="#5d646d">Front view, shutters removed: {fmt(Y1-Y0)} long, 2\'6" deep, on GW-05, joined to the fridge. Grey = kadappa.</text>',
       f'<rect x="{ox}" y="{oy}" width="{W:.1f}" height="{H:.1f}" fill="#efe5d3" stroke="#6b5a48" stroke-width="2"/>',
       f'<rect x="{ox}" y="{Z(S["plinth"]):.1f}" width="{W:.1f}" height="{S["plinth"]*k:.1f}" fill="#b5ab9c"/>',
       f'<rect x="{ox}" y="{Z(S["plinth"])-3:.1f}" width="{W:.1f}" height="4" fill="{KAD}"/>',
       f'<rect x="{ox}" y="{Z(lz)-4:.1f}" width="{W:.1f}" height="7" fill="{KAD}"/>']
    ups=[]   # upright pieces (y, bottom, top): plinth to loft, broken where a wide cell crosses the line
    for y in [Y0]+[bb['y1'] for bb in S['bays'][1:]]+[Y1]:
        segs=[(S['plinth'],lz)]
        for c in S['cells']:
            if len(c['bays'])>1 and any(abs(B[bb]['y1']-y)<0.01 for bb in c['bays'][1:]):
                segs=[q for a_,b_ in segs for q in ((a_,min(b_,c['z1'])),(max(a_,c['z2']),b_)) if q[1]-q[0]>0.01]
        ups+=[(y,a_,b_) for a_,b_ in segs]
    for y,zb,zt in ups:
        x=X(y);w_=t*k
        x0=x-w_ if abs(y-Y0)<0.01 else (x if abs(y-Y1)<0.01 else x-w_/2)
        e.append(f'<rect x="{x0:.1f}" y="{Z(zt):.1f}" width="{w_:.1f}" height="{(zt-zb)*k:.1f}" fill="{KAD}"/>')
    for L in S['loft']:
        x1,x2=X(L[3]),X(L[2])
        if L[2]>Y0+0.01: e.append(f'<rect x="{x2-3:.1f}" y="{oy}" width="6" height="{(S["top"]-lz)*k:.1f}" fill="{KAD}"/>')
        e.append(f'<text x="{(x1+x2)/2:.1f}" y="{(oy+Z(lz))/2-2:.1f}" font-size="13" font-weight="700" text-anchor="middle" fill="#2f6f4f">{L[0]}</text><text x="{(x1+x2)/2:.1f}" y="{(oy+Z(lz))/2+14:.1f}" font-size="10.5" text-anchor="middle" fill="#3a3b3e">{fmt(L[3]-L[2]-t)} x {fmt(S["top"]-lz-0.125)}</text>')
    for c in S['cells']:
        ya,yb,cw=span(c);x1,x2=X(yb),X(ya);cx=(x1+x2)/2;zc=(Z(c['z1'])+Z(c['z2']))/2
        if c['z2']<lz-0.01:
            if c.get('slab')=='adjustable':
                for xx in (x1+t*k+3,x2-t*k/2-7):
                    e.append(f'<rect x="{xx:.1f}" y="{Z(7.0):.1f}" width="4" height="{6*k:.1f}" fill="#1d1e21"/>'+''.join(f'<rect x="{xx+1:.1f}" y="{Z(1+i/6):.1f}" width="2" height="3" fill="#efe5d3"/>' for i in range(37)))
                e.append(f'<rect x="{x1+t*k:.1f}" y="{Z(c["z2"])-3:.1f}" width="{x2-x1-1.5*t*k:.1f}" height="6" fill="#c9a77f" stroke="#1d1e21" stroke-dasharray="4 3"/><text x="{cx:.1f}" y="{Z(c["z2"])+15:.1f}" font-size="10" text-anchor="middle" fill="#2f6f4f">↕ adjustable shelf, 1\' to 7\'</text>')
            else: e.append(f'<rect x="{x1:.1f}" y="{Z(c["z2"])-3:.1f}" width="{x2-x1:.1f}" height="6" fill="{KAD}"/>')
        pre,_,post=c['use'].partition(':');tt=(post if 'cell' in pre else pre) if _ and len(pre)<22 else c['use'];short=''
        for wd in tt.split(',')[0].split('(')[0].split():
            if len(short)+len(wd)>18: break
            short=(short+' '+wd).strip()
        if short.endswith(' and'): short=short[:-4]
        short=short[:1].upper()+short[1:]
        if c['id'] in ('S-4.1','S-4.2'):
            bat=c['id']=='S-4.1';bw,bh=(53/30.48,27.5/30.48) if bat else (36/30.48,20/30.48);zb=c['z1']+0.04
            e.append(f'<rect x="{cx-bw*k/2:.1f}" y="{Z(zb+bh):.1f}" width="{bw*k:.1f}" height="{bh*k:.1f}" rx="3" fill="{"#3b6ea5" if bat else "#1d1e21"}"/>')
            e.append(f'<text x="{x1+t*k+4:.1f}" y="{Z(c["z2"])+14:.1f}" font-size="10.5" font-weight="700" fill="#2f6f4f">{c["id"]}</text><text x="{cx:.1f}" y="{Z(zb+bh/2)+4:.1f}" font-size="10" text-anchor="middle" fill="#fff">{"Battery" if bat else "Inverter"}</text>')
            continue
        e.append(f'<text x="{x1+t*k+(14 if c.get("slab")=="adjustable" or c["bays"]==("S-3",) else 4):.1f}" y="{Z(c["z2"])+15:.1f}" font-size="11" font-weight="700" fill="#2f6f4f">{c["id"]}</text>')
        e.append(f'<text x="{cx:.1f}" y="{zc+5:.1f}" font-size="10.5" text-anchor="middle" fill="#3a3b3e">{fmt(cw)} x {fmt(c["z2"]-c["z1"]-(S["shelf_t"] if c["z2"]<lz-0.01 else 0))}</text>')
    for bb in S['bays']: e.append(f'<text x="{(X(bb["y1"])+X(bb["y2"]))/2:.1f}" y="{Z(0)+18:.1f}" font-size="13" font-weight="700" text-anchor="middle" fill="#2f6f4f">{bb["id"]}</text><text x="{(X(bb["y1"])+X(bb["y2"]))/2:.1f}" y="{Z(0)+32:.1f}" font-size="10" text-anchor="middle" fill="#5d646d">{fmt(bb["y2"]-bb["y1"])}</text>')
    for z in (0,S['plinth'],lz,S['top']):
        lab={0:'floor',S['plinth']:'3" plinth',lz:"7'6\" loft",S['top']:"9'4\""}[z]
        e.append(f'<text x="{ox+W+8:.1f}" y="{Z(z)+4:.1f}" font-size="11" fill="#5d646d">{lab}</text>')
    e.append(f'<text x="{ox}" y="{oy+H+50:.1f}" font-size="11.5" fill="#5d646d">← stair hall (south)</text><text x="{ox+W:.1f}" y="{oy+H+50:.1f}" font-size="11.5" text-anchor="end" fill="#5d646d">fridge FU-18 (north) →</text></svg>')
    # front view with the shutters on, the fridge bay at the north end of the same unit (as built in 3D)
    FR=S.get('fridge');fy1=FR['y1'] if FR else Y0
    W2=(Y1-fy1)*k;X2=lambda y:ox+(Y1-y)*k
    f=[f'<svg viewBox="0 0 {W2+ox+120:.0f} {H+oy+64:.0f}" style="width:100%;max-width:1060px;background:#f7f4ee;border:1px solid var(--line);border-radius:10px" font-family="system-ui,sans-serif">',
       f'<text x="{ox+W2/2:.1f}" y="{oy-12}" font-size="12" text-anchor="middle" fill="#5d646d">Front view with the shutters: one shutter for every cell (two leaves where the cell is over 3\' wide), the fridge bay at the north end of the same unit. Oak = UPVC wood-look.</text>',
       f'<rect x="{ox}" y="{oy}" width="{W2:.1f}" height="{H:.1f}" fill="#d9c3a3" stroke="#6b5a48" stroke-width="2"/>',
       f'<rect x="{ox}" y="{Z(S["plinth"]):.1f}" width="{X2(Y0)-ox:.1f}" height="{S["plinth"]*k:.1f}" fill="#3b3330"/>']
    for sh in S.get('shutters',[]):
        top=S['top'] if sh['cell'].startswith('L-') else sh['z2'];x1,x2=X2(sh['y2']),X2(sh['y1'])
        f.append(f'<rect x="{x1+1.5:.1f}" y="{Z(top)+1.5:.1f}" width="{x2-x1-3:.1f}" height="{(top-sh["z1"])*k-3:.1f}" fill="#c9a77f" stroke="#6b5a48" stroke-width="1"/>')
        if sh['louvred']:
            f+= [f'<line x1="{x1+6:.1f}" x2="{x2-6:.1f}" y1="{yy:.1f}" y2="{yy:.1f}" stroke="#6b5a48" stroke-width="1.5"/>' for yy in [Z(sh['z2'])+6+i*7 for i in range(int((sh['z2']-sh['z1'])*k/7)-1)]]
        hx=x1+6 if sh['hinge']=='a' else x2-9;hz=Z(min(sh['z2']-0.35,4.2)) if sh['z2']-sh['z1']>1.2 else Z((sh['z1']+sh['z2'])/2)-8
        f.append(f'<rect x="{hx:.1f}" y="{hz:.1f}" width="3" height="{min(40,(sh["z2"]-sh["z1"])*k*0.4):.0f}" fill="#1d1e21"/>')
        f.append(f'<text x="{(x1+x2)/2:.1f}" y="{(Z(top)+Z(sh["z1"]))/2+4:.1f}" font-size="10.5" font-weight="700" text-anchor="middle" fill="#3a2a1c">{sh["cell"]}</text>')
    if FR:
        xa,xb=X2(FR['y2']),X2(FR['y1']);ft=FR['top']
        f.append(f'<rect x="{xa+4:.1f}" y="{Z(ft):.1f}" width="{xb-xa-8:.1f}" height="{ft*k:.1f}" fill="#d8dcdf" stroke="#7d848a"/><text x="{(xa+xb)/2:.1f}" y="{Z(ft/2):.1f}" font-size="11" text-anchor="middle" fill="#3a3b3e">Fridge</text><text x="{(xa+xb)/2:.1f}" y="{Z(ft/2)+14:.1f}" font-size="10" text-anchor="middle" fill="#3a3b3e">67 x 68 x 175 cm</text>')
        f.append(f'<rect x="{xa+12:.1f}" y="{Z(ft+0.45):.1f}" width="{xb-xa-24:.1f}" height="{0.45*k:.1f}" fill="#efe5d3" stroke="#7d848a" stroke-dasharray="3 3"/><text x="{(xa+xb)/2:.1f}" y="{Z(ft+0.2):.1f}" font-size="9.5" text-anchor="middle" fill="#5d646d">1\' stabilizer space</text>')
        f.append(f'<rect x="{xa+1.5:.1f}" y="{oy+1.5:.1f}" width="{xb-xa-3:.1f}" height="{(S["top"]-ft-FR["stab"])*k-3:.1f}" fill="#c9a77f" stroke="#6b5a48"/><text x="{(xa+xb)/2:.1f}" y="{oy+(S["top"]-ft-FR["stab"])*k/2+4:.1f}" font-size="10.5" font-weight="700" text-anchor="middle" fill="#3a2a1c">F-loft</text>')
        f.append(f'<text x="{(xa+xb)/2:.1f}" y="{Z(0)+18:.1f}" font-size="13" font-weight="700" text-anchor="middle" fill="#2f6f4f">Fridge bay</text>')
    for bb in S['bays']: f.append(f'<text x="{(X2(bb["y1"])+X2(bb["y2"]))/2:.1f}" y="{Z(0)+18:.1f}" font-size="13" font-weight="700" text-anchor="middle" fill="#2f6f4f">{bb["id"]}</text>')
    f.append(f'<text x="{ox}" y="{oy+H+50:.1f}" font-size="11.5" fill="#5d646d">← stair hall (south)</text><text x="{ox+W2:.1f}" y="{oy+H+50:.1f}" font-size="11.5" text-anchor="end" fill="#5d646d">GW-13, living-room wall (north) →</text></svg>')
    cr=''.join(f'<tr><td class="c">{c["id"]}</td><td>{fmt(span(c)[2])} wide x {fmt(c["z2"]-c["z1"]-(S["shelf_t"] if c["z2"]<lz-0.01 else 0))} high x {fmt(D)} deep</td><td>{fmt(c["z1"])} to {fmt(c["z2"])}</td></tr>' for c in S['cells'])
    cr+=''.join(f'<tr><td class="c">{L[0]}</td><td>{fmt(L[3]-L[2]-t)} wide x {fmt(S["top"]-lz-0.125)} high x {fmt(D)} deep</td><td>{fmt(lz)} to {fmt(S["top"])}</td></tr>' for L in S['loft'])
    # kadappa cutting list: every slab, its place and cut size (shelves go 1" into the uprights and 1" into the back wall)
    kd=[];n=0
    def add(where,L,Dp,th,q=1,note=''):
        nonlocal n;n+=1;kd.append((f'KD-{n:02d}',where,L,Dp,th,q,note))
    add('Plinth top, full length',Y1-Y0,D+1/12,1/12)
    for y,zb,zt in sorted(ups):
        nm='End upright, north (fridge side)' if abs(y-Y0)<0.01 else ('End upright, south (stair hall)' if abs(y-Y1)<0.01 else f'Upright at Y {fmt(y)}, {fmt(zb)} to {fmt(zt)}')
        add(nm,zt-zb,D+1/12,t,1,'stands on the plinth' if zb<0.3 else 'stands on the slab below it')
    for c in S['cells']:
        if c.get('slab')=='adjustable': continue
        cw=span(c)[2];wide=cw>2.6;loft=c['z2']>=lz-0.01
        add(f'Loft floor over {c["id"]} at 7\'6"' if loft else f'Top of {c["id"]} at {fmt(c["z2"])}',cw+2/12,D+1/12,1.5/12 if wide else 1/12,1,'40 mm, with a 1½" MS angle under the front edge (long span)' if wide else '')
    for L in S['loft'][1:]: add(f'Loft upright at Y {fmt(L[2])}',S['top']-lz,D+1/12,t)
    sq=sum(r[2]*r[3]*r[5] for r in kd)
    kr=''.join(f'<tr><td class="c">{r[0]}</td><td>{_h.escape(r[1])}</td><td>{fmt(r[2])} x {fmt(r[3])}</td><td>{"40 mm" if r[4]>1.2/12 else "25 mm"}</td><td>{_h.escape(r[6])}</td></tr>' for r in kd)
    return ('<section><h2>Store cupboard FU-25 (civil work)</h2><p>Built by the mason: 1½" kadappa uprights, 1" kadappa shelves set 1" into the uprights and the back wall, and a 3" brick plinth with a kadappa top. Every cell has its own code (bay, then cell number from the bottom), so you can ask to change any one. Cells have different heights: tall cells for jars and pots, short ones, and two wide cells across S-1 and S-2: S-1.1 at the bottom and S-1.4 at the top. UPVC wood-look (oak) shutters with black handles; the loft has its own shutters.</p>'
            +''.join(f)+''.join(e)+'</section><section><h2>Cells</h2><table class="t"><tr><th>Cell</th><th>Clear size (wide x high x deep)</th><th>From the floor</th></tr>'+cr+'</table></section>'
            +f'<section><h2>Kadappa cutting list (S-1, S-2, S-4 and the loft)</h2><p>Grey Cuddapah stone, polished on the top face, edges rounded on the front. Cut sizes include 1" into each upright groove and 1" into the back wall. About {sq:.0f} sq ft in all.</p><table class="t"><tr><th>Code</th><th>Where</th><th>Cut size (long x deep)</th><th>Thick</th><th>Note</th></tr>'+kr+'</table></section>'
            +(f'<section><h2>Adjustable shelf (S-3)</h2><p>{_h.escape(S["adjust"])}</p></section>' if S.get('adjust') else '')
            +'<section><h2>Inverter and battery (S-4, bottom)</h2><ul>'+''.join(f'<li>{_h.escape(p)}</li>' for p in S['power'])+f'<li>{_h.escape(S["assumed"])}</li></ul></section>'
            +f'<section><h2>Cost</h2><p>{_h.escape(S["cost"])}</p></section>')

def _elec_tab():   # Electrical tab: each floor drawn sideways (road on the left, east side at the top), every point with its code, then the lists
    P=getattr(_mm,'ELEC_POINTS',None)
    if not P: return ''
    import html as _h
    k=14;ox,oy=26,30
    SYM={'DB':('#c0392b','rect'),'SB':('#1d1e21','rect'),'BS':('#6b4f32','rect'),'S6':('#2f6fb0','circ'),'S16':('#e8590c','circ'),'AC':('#0b7285','circ'),'GY':('#a61e4d','circ'),'EV':('#2b8a3e','bolt'),'IP':('#2b8a3e','ring'),'LO':('#f2b705','star'),'NT':('#7048e8','diam')}
    NAME={'DB':'board','SB':'switchboard','BS':'bedside board','S6':'6 A socket with switch','S16':'16 A socket','AC':'AC socket','GY':'geyser socket','EV':'car charging','IP':'outdoor IP65 socket / isolator','LO':'outdoor light','NT':'bell, data, CCTV, solar'}
    def floor_svg(fl,y0,y1,title):
        W=(y1-y0)*k;H=21*k
        X=lambda y:ox+(y-y0)*k;Yp=lambda x:oy+x*k
        e=[f'<div class="wide"><svg viewBox="0 0 {W+2*ox:.0f} {H+oy+24:.0f}" style="width:{W+2*ox:.0f}px;max-width:none;background:#f7f4ee;border:1px solid var(--line);border-radius:10px" font-family="system-ui,sans-serif">',
           f'<text x="{ox}" y="18" font-size="12.5" font-weight="700" fill="#1f2328">{title}</text><text x="{ox+W:.0f}" y="18" font-size="11" text-anchor="end" fill="#5d646d">road on the left · east side passage at the top · back garden on the right</text>']
        for r in _mm.ROOMS[fl]:
            pts=' '.join(f'{X(py):.1f},{Yp(px):.1f}' for px,py in r[2])
            fill={'wet':'#e3eef5','kit':'#f3ead9','bed':'#efe9df','out':'#eceae6','garden':'#e6efdc','terr':'#f1e4d6','porch':'#efe9df'}.get(r[3],'#f4efe6')
            e.append(f'<polygon points="{pts}" fill="{fill}" stroke="none"/>')
            xs=[p[0] for p in r[2]];ys=[p[1] for p in r[2]]
            e.append(f'<text x="{X((min(ys)+max(ys))/2):.1f}" y="{Yp((min(xs)+max(xs))/2)+3:.1f}" font-size="8.5" text-anchor="middle" fill="#9a8f80">{_h.escape(r[1])}</text>')
        for w in _mm.WALLS[fl]:
            col='#6b6b6b' if w[5] in ('comp','para') else '#3b3b3b'
            e.append(f'<rect x="{X(w[3]):.1f}" y="{Yp(w[1]):.1f}" width="{(w[4]-w[3])*k:.1f}" height="{(w[2]-w[1])*k:.1f}" fill="{col}"/>')
        for o in _mm.OPENINGS:
            if o[1]!=fl or o[2]=='FRONT': continue
            w=next((w for w in _mm.WALLS[fl] if w[0]==o[2]),None)
            if not w: continue
            horiz=(w[2]-w[1])>(w[4]-w[3])
            if horiz: e.append(f'<rect x="{X(w[3])-0.5:.1f}" y="{Yp(o[3]):.1f}" width="{(w[4]-w[3])*k+1:.1f}" height="{(o[4]-o[3])*k:.1f}" fill="#fffdf7"/>')
            else: e.append(f'<rect x="{X(o[3]):.1f}" y="{Yp(w[1])-0.5:.1f}" width="{(o[4]-o[3])*k:.1f}" height="{(w[2]-w[1])*k+1:.1f}" fill="#fffdf7"/>')
        for p in P:
            if p[1]!=fl: continue
            pid,_,px,py,pz,kind,circ,what=p;cx,cy=X(py),Yp(px);col,shape=SYM[kind]
            tip=_h.escape(f'{pid} · {NAME[kind]} · {fmt(pz)} up · {circ} · {what}')
            g=f'<g><title>{tip}</title>'
            if shape=='rect': g+=f'<rect x="{cx-5:.1f}" y="{cy-4:.1f}" width="10" height="8" rx="1.5" fill="{col}"/>'
            elif shape=='circ': g+=f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.2" fill="{col}"/>'
            elif shape=='ring': g+=f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.2" fill="#fff" stroke="{col}" stroke-width="2.2"/>'
            elif shape=='bolt': g+=f'<rect x="{cx-6:.1f}" y="{cy-6:.1f}" width="12" height="12" rx="3" fill="{col}"/><path d="M{cx+1:.1f} {cy-4.5:.1f} L{cx-3:.1f} {cy+0.8:.1f} H{cx:.1f} L{cx-1:.1f} {cy+4.5:.1f} L{cx+3:.1f} {cy-0.8:.1f} H{cx:.1f}Z" fill="#fff"/>'
            elif shape=='star': g+=f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.5" fill="{col}" stroke="#7a5c00" stroke-width="1"/>'
            elif shape=='diam': g+=f'<rect x="{cx-3.5:.1f}" y="{cy-3.5:.1f}" width="7" height="7" transform="rotate(45 {cx:.1f} {cy:.1f})" fill="{col}"/>'
            g+=f'<text x="{cx:.1f}" y="{cy-6.5:.1f}" font-size="8" font-weight="700" text-anchor="middle" fill="{col}" stroke="#f7f4ee" stroke-width="2.2" paint-order="stroke">{pid}</text></g>'
            e.append(g)
        e.append('</svg></div>')
        return ''.join(e)
    leg=''.join(f'<span style="display:inline-flex;align-items:center;gap:5px;margin:0 12px 4px 0;font-size:12.5px"><svg width="14" height="14"><circle cx="7" cy="7" r="5.5" fill="{c}"/></svg>{NAME[kd]}</span>' for kd,(c,_) in SYM.items())
    rows=''.join(f'<tr><td class="c">{p[0]}</td><td>{"Ground" if p[1]=="G" else "First"}</td><td>{NAME[p[5]]}</td><td>{fmt(p[4])}</td><td>{p[6]}</td><td>{_h.escape(p[7])}</td></tr>' for p in P)
    circ=''.join(f'<tr><td class="c">{c[0]}</td><td>{_h.escape(c[1])}</td><td>{c[2]}</td><td>{c[3]}</td><td>{_h.escape(c[4])}</td></tr>' for c in _mm.ELEC_CIRCUITS)
    return ('<section><h2>Electrical plan (AU-03)</h2><p>Plain modular switches (no smart switches), so any electrician can repair them cheaply. Every point has a code. Hover a symbol for its details, or find it in the list below. Lights inside rooms are listed with the switchboard that controls them.</p>'
            +f'<div style="margin:6px 0 10px">{leg}</div>'+floor_svg('G',0,106,'Ground floor')+'<div style="height:12px"></div>'+floor_svg('F',14,99,'First floor and terrace')+'</section>'
            +'<section><h2>Rules used</h2><ul>'+''.join(f'<li>{_h.escape(r)}</li>' for r in _mm.ELEC_RULES)+'</ul></section>'
            +'<section><h2>Circuits</h2><table class="t"><tr><th>Circuit</th><th>What</th><th>Breaker</th><th>Wire</th><th>Note</th></tr>'+circ+'</table></section>'
            +'<section><h2>All points</h2><table class="t"><tr><th>Code</th><th>Floor</th><th>Type</th><th>Height</th><th>Circuit</th><th>What</th></tr>'+rows+'</table></section>'
            +f'<section><h2>Cost</h2><p>{_h.escape(_mm.ELEC_COST)}</p></section>')
def _section_tab():   # Section tab: long section A-A through the car ramp, porch steps, house, terrace and bedroom 3 block, heights from the road crown
    import math
    L=_mm.LEVELS;RP=_mm.RAMP;road=L['road'];hump=L['hump'];pk=L['parking'];fl=L['floor'];gd=L['garden']
    FF=fl+_mm.FF_LEVEL;CE=fl+10.0;RF=FF+10.0;RT=RF+1.0;TK=RT+1.0+5.0;PSY=_mm.PORCH_STEPS_Y;PFY=PSY+2.5
    yb,yc,yt,ez=RP['y_hump'],RP['y_crest'],RP['y_top'],RP['ease']
    def ft(v):
        i=int(round(v*12));return f"{i//12}'{i%12}\"" if i%12 else f"{i//12}'0\""
    def ramp_z(y):
        if y<=yb: return road+(hump-road)*max(0,y)/yb
        if y<=yc: return hump
        d=y-yc;m1=ez;m2=yt-yc-ez
        if d<=m1: return hump+d/8
        if d<=m2: return hump+m1/8+(d-m1)/4
        return min(pk,hump+m1/8+(m2-m1)/4+(d-m2)/8)
    def svg(y0,y1,z0,z1,k,inset):
        W=(y1-y0)*k;H=(z1-z0)*k;ox,oy=70,30
        X=lambda y:ox+(y-y0)*k;Z=lambda z:oy+(z1-z)*k
        e=[f'<svg class="pz" viewBox="0 0 {W+ox+150:.0f} {H+oy+70:.0f}" style="width:100%;max-width:{1300 if not inset else 1100}px;background:#f7f4ee;border:1px solid var(--line);border-radius:10px;cursor:grab;touch-action:none" font-family="system-ui,sans-serif">']
        # height axes on both ends (feet above the road), so a height can be read without crossing the drawing
        stp=1 if inset else 2
        for zz in range(int(math.ceil(z0)),int(z1)+1):
            if zz%stp: continue
            for xa,anc,dx in ((ox,'end',-6),(ox+W,'start',6)):
                e.append(f'<line x1="{xa:.1f}" x2="{xa+(-5 if anc=="end" else 5):.1f}" y1="{Z(zz):.1f}" y2="{Z(zz):.1f}" stroke="#5d646d"/>')
                if anc=='end': e.append(f'<text x="{xa+dx:.1f}" y="{Z(zz)+3.5:.1f}" font-size="10" text-anchor="end" fill="#5d646d">{zz}\'</text>')
        e.append(f'<line x1="{ox}" x2="{ox}" y1="{Z(z1):.1f}" y2="{Z(z0):.1f}" stroke="#5d646d"/><line x1="{ox+W:.1f}" x2="{ox+W:.1f}" y1="{Z(z1):.1f}" y2="{Z(z0):.1f}" stroke="#5d646d"/>')
        e.append(f'<text x="{ox-34}" y="{Z(z1)-8:.1f}" font-size="10" fill="#5d646d">height</text>')
        def poly(pts,fill,stroke='#3b3b3b',sw=1.2,op=1):
            e.append(f'<polygon points="{" ".join(f"{X(a):.1f},{Z(b):.1f}" for a,b in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" fill-opacity="{op}"/>')
        def rect(a,b,za,zb,fill,stroke='#3b3b3b'):
            if b<y0 or a>y1: return
            a=max(a,y0);b=min(b,y1);poly([(a,za),(b,za),(b,zb),(a,zb)],fill,stroke)
        BW=' font-weight="700"'
        def lab(y,z,t,anchor='middle',col='#3a3b3e',size=11,bold=False,dy=0):
            if y0-1<=y<=y1+1: e.append(f'<text x="{X(y):.1f}" y="{Z(z)+dy:.1f}" font-size="{size}" text-anchor="{anchor}" fill="{col}"{BW if bold else ""}>{t}</text>')
        for zz in range(int(math.ceil(z0)),int(z1)+1):
            if zz%stp==0: e.append(f'<text x="{ox+W-4:.1f}" y="{Z(zz)+3.5:.1f}" font-size="9" text-anchor="end" fill="#8a9098">{zz}\'</text>')
        last=[None]
        def lev(z,t,col='#c0392b'):   # level tag on the right; tags closer than 13 px are pushed down so they never overlap
            ty=Z(z)+4
            if last[0] is not None and ty<last[0]+13: ty=last[0]+13
            last[0]=ty
            e.append(f'<line x1="{ox}" x2="{ox+W:.1f}" y1="{Z(z):.1f}" y2="{Z(z):.1f}" stroke="{col}" stroke-width="0.6" stroke-dasharray="4 4"/><line x1="{ox+W:.1f}" x2="{ox+W+6:.1f}" y1="{Z(z):.1f}" y2="{ty-4:.1f}" stroke="{col}" stroke-width="0.6"/><text x="{ox+W+8:.1f}" y="{ty:.1f}" font-size="11" fill="{col}">+{ft(z)} {t}</text>')
        # ground: road, gate bevel, crest, ramp, parking, porch steps, house plinth; back garden
        gp=[(y0,road-1.5),(y0,road)]+[(y/10,ramp_z(y/10)) for y in range(int(y0*10) if y0>0 else 0,int(min(yt,y1)*10)+1)]+[(min(PSY,y1),pk)]
        if y1>PSY:
            for i in range(3): gp+= [(PSY+i*2.5/3,pk+(i+1)*0.5),(PSY+(i+1)*2.5/3,pk+(i+1)*0.5)]
            gp+=[(min(95.125,y1),fl)]
            if y1>95.125: gp+=[(95.125,gd),(y1,gd)]
        gp+=[(gp[-1][0],road-1.5)];poly(gp,'#d9cdb8','#7a6a55')
        e.append(f'<rect x="{ox-40}" y="{Z(road):.1f}" width="{X(0)-ox+40:.1f}" height="{1.5*k:.1f}" fill="#8f8f8f"/>')
        lab(-3 if y0<-2 else y0+1,road+0.3,'Road',col='#fff' if False else '#3a3b3e',bold=True)
        # gate pillar and gate
        rect(0.3,0.75,hump,hump+6.5,'#b7c4a5');lab(0.5,hump+6.9,'Gate')
        if inset:
            # dimensions on the ramp: slopes and angles
            segs=[(yc,yc+ez,'1 in 8',8),(yc+ez,yt-ez,'1 in 4',4),(yt-ez,yt,'1 in 8',8)]
            for a,b,t,n in segs:
                za,zb=ramp_z(a),ramp_z(b);ang=math.degrees(math.atan(1/n))
                lab((a+b)/2,(za+zb)/2+0.55,f'{t} · {ang:.1f}°',col='#1d5fa8',size=12,bold=True)
            lab((0+yb)/2,hump-0.9,'bevel 6"',col='#1d5fa8',size=11)
            lab((yb+yc)/2,hump+1.1,'level crest + drain',col='#1d5fa8',size=11)
            lab(yt+3,pk+0.35,'level parking',col='#1d5fa8',size=12,bold=True)
            lab(PSY+1.25,fl+0.9,'3 steps: 6" rise, 10" tread · 31°',col='#1d5fa8',size=12,bold=True)
            for y,z,t in ((yt,pk,'+2\'0"'),(PFY,fl,'+3\'6"')):
                if t: lab(y,z-0.55,t,col='#c0392b',size=11,bold=True)
            # car outline (reversed in) and the porch, house front
            rect(yt+3.0,yt+18.0,pk+0.6,pk+4.8,'#cfd8e3','#5b6b7c');lab(yt+10.5,pk+2.5,'car (VW Virtus, 4\'9" high)',size=11)
            rect(29.0,29.75,pk,fl+10,'#b7c4a5');lab(29.4,fl+10.5,'study wall')
            rect(19.75,40.5,CE,FF,'#c9c9c9');lab(30,CE+0.75,'roof slab over parking and porch (terrace above)',size=11)
            rect(2.0,2.0,0,0,'#fff')
            for z,t in sorted(((road,'road'),(hump,'gate bevel top'),(pk,'parking'),(fl,'house floor and porch'),(CE,'ceiling / slab bottom'),(FF,'terrace floor')),key=lambda q:-q[0]): lev(z,t)
        else:
            # house: floor, ground-floor slab, walls front and back, terrace, parapets, first-floor block, roof, tank, balconies
            rect(19.75,95.125,CE,FF,'#c9c9c9');lab(57,CE+0.8,'ground-floor roof slab (open terrace on top)',size=11)
            rect(29.75,30.5,fl,CE,'#b7c4a5');rect(94.375,95.125,fl,CE,'#b7c4a5')
            rect(19.75,20.125,FF,FF+3,'#b7c4a5');lab(20,FF+3.5,'parapet 3\'')
            rect(15.875,19.75,FF-0.5,FF,'#c9c9c9');lab(17.8,FF+0.5,'balcony 2',size=10)
            rect(73.125,73.875,FF,RF,'#b7c4a5');rect(94.375,95.125,FF,RF,'#b7c4a5')
            rect(73.125,95.125,RF,RT,'#c9c9c9');lab(84,RF+0.45,'roof slab',size=10)
            rect(89.2,94.2,RT,RT+1,'#a9a9a9');rect(89.2,94.2,RT+1,TK,'#2f6f9f','#1d3f5f');lab(91.7,RT+3.5,'tank 2000 L',col='#fff',size=10)
            rect(95.125,98.125,FF-0.5,FF,'#c9c9c9');rect(97.75,98.125,FF,FF+3,'#b7c4a5');lab(96.6,FF+3.5,'balcony 3',size=10)
            lab(52,fl+4.5,'living · kitchen · stair hall',size=12);lab(84,fl+4.5,'bedroom 2',size=12);lab(84,FF+4.5,'bedroom 3',size=12);lab(48,FF+1.2,'open terrace',size=12)
            lab(36,fl+1.0,'porch',size=10);lab(20,pk+3.5,'parking (car)',size=12);lab(100,gd+1.5,'back garden',size=11)
            for z,t in sorted(((road,'road crown'),(pk,'parking'),(gd,'garden'),(fl,'house floor'),(CE,'ground-floor ceiling'),(FF,'terrace / first floor'),(FF+3,'parapet top'),(RF,'first-floor ceiling'),(RT,'roof top'),(TK,'tank top')),key=lambda q:-q[0]): lev(z,t)
        # horizontal scale: feet from the road edge
        step=2 if inset else 10
        for y in range(int(math.ceil(y0/step)*step),int(y1)+1,step):
            e.append(f'<line x1="{X(y):.1f}" x2="{X(y):.1f}" y1="{oy+H:.1f}" y2="{oy+H+6:.1f}" stroke="#5d646d"/><text x="{X(y):.1f}" y="{oy+H+20:.1f}" font-size="10" text-anchor="middle" fill="#5d646d">{y}\'</text>')
        e.append(f'<text x="{ox}" y="{oy+H+40:.1f}" font-size="11" fill="#5d646d">feet from the road edge (north, road) → south (back)</text></svg>')
        return ''.join(e)
    big=svg(-6,106,-1.5,TK+1,11,False);ins=svg(-3,42,-1.5,FF+1.5,30,True)
    st1=_mm.FF_LEVEL+(fl-hump);R=st1/27;ang=math.degrees(math.atan(R/(10/12)))
    rows=[('Road crown (in front of the gate)',road),('Gate bevel top',hump),('Parking floor',pk),('Side and back garden',gd),('House floor, porch',fl),('Ground-floor ceiling (slab bottom)',CE),('Terrace and first-floor floor',FF),('Terrace parapet top',FF+3),('First-floor ceiling',RF),('Roof top',RT),('Water tank top',TK)]
    tr=''.join(f'<tr><td>{n}</td><td>+{ft(z)}</td></tr>' for n,z in rows)
    sl=''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a,b in [('Gate bevel (road to crest)',f'6" rise over {ft(yb)}'),('Car ramp, start',f'1 in 8 ({math.degrees(math.atan(1/8)):.1f}°) for {ft(ez)}'),('Car ramp, middle',f'1 in 4 ({math.degrees(math.atan(1/4)):.1f}°) for {ft(yt-yc-2*ez)}'),('Car ramp, end',f'1 in 8 ({math.degrees(math.atan(1/8)):.1f}°) for {ft(ez)}'),('Porch steps (3)','6" rise, 10" tread, 31° pitch'),('Outside stair ST-1 (27 risers, gate to balcony 2)',f'{R*12:.1f}" rise, 10" tread, {ang:.0f}° pitch'),('Spiral stair ST-2 (21 risers)',f'{_mm.FF_LEVEL/21*12:.1f}" rise')])
    return ('<section><h2>Section A-A (long section, road to back)</h2><p>Cut along the house from the road to the back garden, through the car ramp, the porch steps, the ground floor, the terrace and the bedroom 3 block. Heights are from the road crown in front of the gate, drawn to scale (horizontal and vertical the same).</p>'+big+'</section>'
            +'<section><h2>Detail: gate, car ramp and porch steps</h2><p>Same section, front part enlarged, with the ramp slopes and angles.</p>'+ins+'</section>'
            +'<p style="color:#5d646d;font-size:13px">Scroll or pinch on a drawing to zoom, drag to move it, double-click to reset.</p>'
            +'''<script>document.querySelectorAll('svg.pz').forEach(sv=>{const v0=sv.getAttribute('viewBox').split(' ').map(Number);let v=v0.slice(),drag=null;const set=()=>sv.setAttribute('viewBox',v.join(' '));
 const pt=e=>{const r=sv.getBoundingClientRect();return [v[0]+(e.clientX-r.left)/r.width*v[2],v[1]+(e.clientY-r.top)/r.height*v[3]]};
 sv.addEventListener('wheel',e=>{e.preventDefault();const k=e.deltaY<0?0.85:1/0.85,p=pt(e);v=[p[0]-(p[0]-v[0])*k,p[1]-(p[1]-v[1])*k,v[2]*k,v[3]*k];if(v[2]>v0[2]){v=v0.slice()}set()},{passive:false});
 sv.addEventListener('pointerdown',e=>{drag=[e.clientX,e.clientY,v[0],v[1]];sv.setPointerCapture(e.pointerId);sv.style.cursor='grabbing'});
 sv.addEventListener('pointermove',e=>{if(!drag)return;const r=sv.getBoundingClientRect();v[0]=drag[2]-(e.clientX-drag[0])/r.width*v[2];v[1]=drag[3]-(e.clientY-drag[1])/r.height*v[3];set()});
 sv.addEventListener('pointerup',()=>{drag=null;sv.style.cursor='grab'});sv.addEventListener('dblclick',()=>{v=v0.slice();set()})})</script>'''
            +'<section><h2>Levels</h2><table class="t"><tr><th>Level</th><th>Height from the road</th></tr>'+tr+'</table></section>'
            +'<section><h2>Slopes and steps</h2><table class="t"><tr><th>Where</th><th>Slope / step</th></tr>'+sl+'</table></section>')

_et=_elec_tab()
if _et: _tabs.insert(0,('electrical','Electrical',_et))
_st=_store_tab()
if _st: _tabs.insert(0,('store','Store',_st))
_sc=_section_tab()
if _sc: _tabs.insert(0,('section','Section',_sc))
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
