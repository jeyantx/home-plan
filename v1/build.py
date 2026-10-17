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
KN={'outer':'9" outer','part':'4½" partition','comp':'4½" compound','para':'4½" parapet','pillar':'9" pillar'}
wall_rows=''
for f,fl in (('G','Ground'),('F','First')):
    for wid,x1,x2,y1,y2,k,h,desc in WALLS[f]:
        L=max(x2-x1,y2-y1)
        wall_rows+=f'<tr><td class="c">{wid}</td><td>{esc(desc)}</td><td>{KN[k]}</td><td>{fmt(L)}</td><td>{fmt(h)}</td></tr>'
TN={'door':'Door','double':'Double door','window':'Window','vent':'Ventilator','arch':'Open arch','gate':'Gate','fold':'Folding glass window'}
op_rows=''
for oid,f,wid,a,b,typ,hinge,swing,h,sill,note in OPENINGS:
    op_rows+=f'<tr><td class="c">{oid}</td><td>{TN[typ]}</td><td>{"front line" if wid=="FRONT" else wid}</td><td>{fmt(b-a)} x {fmt(h)}</td><td>{fmt(sill) if sill else "–"}</td><td>{esc(note)}</td></tr>'
import model as _m
BN=getattr(_m,'BRANCH_NOTES','')
panel=BN+f'''
<section><h2>How to read this plan</h2>
<ul>
<li><b>X</b> is feet from the east boundary, from 0 to 21. <b>Y</b> is feet from the road, from 0 to 106. For example, "GW-05 at Y 50'" names one exact spot.</li>
<li><b>Codes:</b> G- ground-floor room or area, F- first-floor room or area, GW- ground-floor wall, FW- first-floor wall, PW- parapet, BW- boundary wall, D- door, W- window, V- ventilator, O- open arch, GT- gate, ST- staircase.</li>
<li>Room sizes are clear inside the walls. Walls are drawn at true thickness: 9" outer and 4½" partitions, compound walls and parapets.</li>
<li>Use the checkboxes above the plan to hide codes or dimensions when you want a clean view.</li>
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
<tr><td>First floor built-up, bedroom block</td><td class="n">{ffb:,.0f}</td></tr>
<tr class="tot"><td>Total built-up, both floors</td><td class="n">{gf+ffb:,.0f}</td></tr>
<tr><td>Open terrace, terrace corner and balcony 2 (clear)</td><td class="n">{terr:,.0f}</td></tr>
<tr><td>Open terrace alone, for the future hall</td><td class="n">{ra("F","F-02"):,.0f}</td></tr>
<tr><td>Gardens, side and back</td><td class="n">{garden:,.0f}</td></tr>
</table></section>
<section><h2>Staircases</h2>
<ul>
<li><b>ST-1 outside stair</b>, 3'6" wide, 6" risers and 10" treads. ST-1A runs along the west side from Y 4'4" to 16', 15 risers. ST-1L is a 3'6" x 3'6" landing at +7'6". ST-1B turns east, 8 risers over 5'10", and arrives on balcony 2 at +11'6". The car parks under ST-1B.</li>
<li><b>ST-2 spiral stair</b>, 6' across, in the stair hall. It arrives on the first-floor stair landing F-04.</li>
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
<section><h2>Existing on site</h2><ul><li><b>Borewell</b> at X 6', Y {BOREWELL[1]:.1f}', which is 6' from the east boundary and 25' from the back wall, in the side garden G-14.</li></ul></section>
<section><h2>Still open</h2>
<ul><li><b>Neem tree.</b> At the position you gave, the trunk is 4' from staircase 1 and directly in front of the car's spot. Please confirm or correct it.</li></ul></section>
<section><h2>Rooms and areas</h2><table class="t"><tr><th>Code</th><th>Name</th><th>Floor</th><th>Inside size</th><th class="n">sq ft</th></tr>{room_rows}</table></section>
<section><h2>Walls</h2><table class="t"><tr><th>Code</th><th>Where</th><th>Type</th><th>Length</th><th>Height</th></tr>{wall_rows}</table></section>
<section><h2>Doors, windows, ventilators, gates</h2><table class="t"><tr><th>Code</th><th>Type</th><th>Wall</th><th>Width x height</th><th>Sill</th><th>Note</th></tr>{op_rows}</table></section>
'''
page=open('/Users/jeyant-10189/Work/Personal/own/home-plan/homeplan-4-my-reading.html').read()
style=page[page.index('<style>'):page.index('</style>')+8]
script=page[page.index('<script>'):page.index('</script>')+9]
style=style.replace('</style>','''
.layers{display:inline-flex;gap:12px;align-items:center;font-size:13px;color:var(--muted)}
.layers label{display:inline-flex;gap:5px;align-items:center;cursor:pointer}
td.c{font-weight:700;white-space:nowrap;color:var(--accent)}
.hide-L-rooms .L-rooms,.hide-L-walls .L-walls,.hide-L-open .L-open,.hide-L-dims .L-dims{display:none}
</style>''')
script=script.replace('const FULL={x:121.5,y:44.8,w:32.0,h:115.4};','const FULL={x:-5.0,y:-1.0,w:30.0,h:112.0};')
script=script.replace('const h=42, w=h*a;','const h=34, w=h*a;')
script=script[:script.index('const ROOMS=')]+'const ROOMS='+json.dumps({'f0':[{'t':r[1],'x':(min(p[0] for p in r[2])+max(p[0] for p in r[2]))/2-0,'y':107-(min(p[1] for p in r[2])+max(p[1] for p in r[2]))/2} for r in ROOMS['G']],
                                                                      'f1':[{'t':r[1],'x':(min(p[0] for p in r[2])+max(p[0] for p in r[2]))/2,'y':107-(min(p[1] for p in r[2])+max(p[1] for p in r[2]))/2} for r in ROOMS['F']]})+';'+script[script.index(';',script.index('const ROOMS='))+1:]
script=script.replace("'hp4mine-view'","'hpv1-view'")
script=script.replace("b.textContent=rm.t.replace(/\\n/g,' ').toLowerCase().replace(/(^|\\s)\\S/g,c=>c.toUpperCase());","b.textContent=rm.t;")
script=script.replace('</script>','''
for(const cb of document.querySelectorAll('.layers input')){
  const k='hpv1-'+cb.dataset.layer; try{ if(localStorage.getItem(k)==='0') cb.checked=false }catch(e){}
  const ap=()=>{document.body.classList.toggle('hide-'+cb.dataset.layer,!cb.checked); try{localStorage.setItem(k,cb.checked?'1':'0')}catch(e){}};
  cb.addEventListener('change',ap); ap();
}
</script>''')
import subprocess as _sp
BRANCH=_sp.run(['git','rev-parse','--abbrev-ref','HEAD'],capture_output=True,text=True).stdout.strip() or 'main'
out=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Home Plan v1</title>
{style}</head><body>
<header>
 <div><h1>Home plan · {BRANCH}</h1><div class="sub">Clean 2D plan with named walls, rooms and openings. Road and gates face north, at the bottom.</div></div>
 <div class="seg" role="group" aria-label="View">
  <button data-view="f0">Ground floor</button><button data-view="f1">First floor</button><button data-view="both">Side by side</button>
 </div>
 <div class="layers">
  <label><input type="checkbox" data-layer="L-rooms" checked>Rooms</label>
  <label><input type="checkbox" data-layer="L-walls" checked>Wall codes</label>
  <label><input type="checkbox" data-layer="L-open" checked>Door and window codes</label>
  <label><input type="checkbox" data-layer="L-dims" checked>Dimensions</label>
 </div>
 <div class="tools" role="group" aria-label="Zoom">
  <button id="zin" title="Zoom in" aria-label="Zoom in">+</button><button id="zout" title="Zoom out" aria-label="Zoom out">&minus;</button><button id="fit" title="Fit whole plan">Fit</button><button id="theme" title="Toggle light or dark" aria-label="Toggle theme">◐</button>
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
