import math, json
from model import *
TOP=107.0
def S(X,Y): return (X, TOP-Y)
def fmt(v):
    inch=round(v*12*2)/2; f=int(inch//12); r=inch-f*12
    if r==0: return f"{f}'"
    rs=(f'{int(r)}' if int(r) else '')+('½' if r!=int(r) else '')
    return f"{f}'{rs}\""
def area(P): return abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[(i+1)%len(P)][0]*P[i][1] for i in range(len(P))))/2
out=[]
def E(s): out.append(s)
def pts(P): return ' '.join(f'{S(x,y)[0]:.3f},{S(x,y)[1]:.3f}' for x,y in P)
def rect(x1,x2,y1,y2,fill,stroke='none',sw=0.04,cls='',extra=''):
    E(f'<rect class="{cls}" x="{x1:.3f}" y="{TOP-y2:.3f}" width="{x2-x1:.3f}" height="{y2-y1:.3f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')
def line(X1,Y1,X2,Y2,stroke='#333',sw=0.04,cls='',extra=''):
    a=S(X1,Y1); b=S(X2,Y2)
    E(f'<line class="{cls}" x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')
def text(X,Y,s,size=0.5,weight=400,fill='#222',anchor='middle',rot=0,cls=''):
    x,y=S(X,Y); lines=s.split('\n'); n=len(lines)
    tr=f' transform="rotate({rot} {x:.3f} {y:.3f})"' if rot else ''
    E(f'<text class="{cls}" x="{x:.3f}" y="{y:.3f}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{tr}>')
    for i,l in enumerate(lines):
        E(f'<tspan x="{x:.3f}" y="{y+(i-(n-1)/2)*size*1.2+size*0.35:.3f}">{l.replace("&","&amp;")}</tspan>')
    E('</text>')
def tag(X,Y,s,kind='wall',rot=0):
    x,y=S(X,Y); w=len(s)*0.25+0.3; h=0.5
    col={'wall':('#ffffff','#5b5b5b','#333'),'door':('#fff4e8','#a35a1b','#7a3e0c'),'win':('#e8f2ff','#2f6fb0','#1f4f86'),'room':('#2f6f4f','#2f6f4f','#fff')}[kind]
    tr=f' transform="rotate({rot} {x:.3f} {y:.3f})"' if rot else ''
    E(f'<g class="tag-{kind}"{tr}><rect x="{x-w/2:.3f}" y="{y-h/2:.3f}" width="{w:.3f}" height="{h:.3f}" rx="0.12" fill="{col[0]}" stroke="{col[1]}" stroke-width="0.03"/>'
      f'<text x="{x:.3f}" y="{y+0.13:.3f}" font-size="0.36" font-weight="700" fill="{col[2]}" text-anchor="middle">{s}</text></g>')

FILL={'out':'#e9e8e4','porch':'#efe7da','in':'#fbf6ea','bed':'#fbf0dd','wet':'#dcEEF2','kit':'#e9f1fb','garden':'#cfe7bf','terr':'#ecebe6'}
WALLFILL={'outer':'url(#hatch)','part':'url(#hatchP)','comp':'url(#hatchC)','para':'url(#hatchC)','pillar':'#6b6b6b'}

def walls_of(fl): return {w[0]:w for w in WALLS[fl]}
def draw_plot(fl):
    E(f'<polygon points="{pts(PLOT)}" fill="{"#e3f0d8" if fl=="G" else "#f6f7f3"}" stroke="#3d6b35" stroke-width="0.07"/>')
    # west existing apartment wall (outside our land)
    E(f'<polygon points="{pts([(21,0),(21.5,0),(21.5,105),(21,105)])}" fill="url(#hatchX)" stroke="#888" stroke-width="0.03"/>')
    # back existing wall (inside line)
    E(f'<polygon points="{pts([(1.0,106.0),(21,105.0),(21,104.625),(1.375,105.6)])}" fill="url(#hatchX)" stroke="#888" stroke-width="0.03"/>')
def draw_rooms(fl,labels=True):
    for rid,name,P,k in ROOMS[fl]:
        E(f'<polygon points="{pts(P)}" fill="{FILL[k]}"/>')
def room_labels(fl,skip=()):
    for rid,name,P,k in ROOMS[fl]:
        xs=[p[0] for p in P]; ys=[p[1] for p in P]
        cx=(min(xs)+max(xs))/2; cy=(min(ys)+max(ys))/2
        w=max(xs)-min(xs); d=max(ys)-min(ys); a=area(P)
        pos=LABELPOS.get(rid,(cx,cy)); size=LABELSIZE.get(rid,0.5)
        rect_like=len(P)==4
        dims=f"{fmt(w)} x {fmt(d)}  ·  {a:.0f} sq ft" if rect_like else f"{a:.0f} sq ft"
        x,y=S(*pos)
        if rid=='G-13':
            E(f'<g class="lbl-room" transform="rotate(-90 {x:.3f} {y:.3f})"><text x="{x:.3f}" y="{y-0.15:.3f}" font-size="0.4" font-weight="700" fill="#1f2a24" text-anchor="middle">{rid} SIDE PASSAGE</text><text x="{x:.3f}" y="{y+0.45:.3f}" font-size="0.34" fill="#333" text-anchor="middle">{dims}</text></g>')
            continue
        E(f'<g class="lbl-room"><text x="{x:.3f}" y="{y-size*0.55:.3f}" font-size="{size*0.72:.3f}" font-weight="700" fill="#2f6f4f" text-anchor="middle">{rid}</text>'
          f'<text x="{x:.3f}" y="{y+size*0.35:.3f}" font-size="{size:.3f}" font-weight="700" fill="#1f2a24" text-anchor="middle">{name.upper()}</text>'
          f'<text x="{x:.3f}" y="{y+size*1.3:.3f}" font-size="{size*0.8:.3f}" fill="#333" text-anchor="middle">{dims}</text></g>')
LABELPOS={'G-01':(8.0,23.0),'G-02':(5.6,37.6),'G-03':(6.2,44.6),'G-04':(11.5,55.4),'G-05':(14.8,41.0),'G-06':(11.5,33.6),'G-07':(17.2,33.4),
          'G-08':(8.0,66.6),'G-09':(16.9,66.0),'G-10':(12.8,71.4),'G-11':(6.0,73.0),'G-12':(15.25,88.2),'G-13':(1.55,36.0),'G-14':(5.0,96.0),'G-15':(15.2,100.6),
          'F-01':(7.4,18.6),'F-02':(11.9,47.0),'F-03':(6.3,77.2),'F-04':(13.0,78.0),'F-05':(15.25,91.5),'F-06':(12.05,83.2),'F-07':(17.25,82.4)}
LABELSIZE={'G-13':0.36,'G-06':0.4,'G-07':0.42,'G-11':0.42,'G-03':0.42,'G-02':0.42,'F-06':0.36,'F-07':0.42,'G-10':0.42,'F-04':0.45,'F-03':0.42,'F-01':0.45,'G-09':0.45,'G-01':0.6,'F-02':0.8}
def draw_walls(fl,ghost=False):
    for wid,x1,x2,y1,y2,k,h,desc in WALLS[fl]:
        if ghost: rect(x1,x2,y1,y2,'#cfcbc2',extra='opacity="0.6"'); continue
        rect(x1,x2,y1,y2,WALLFILL[k],'#333',0.035)
def wall_tags(fl):
    for wid,x1,x2,y1,y2,k,h,desc in WALLS[fl]:
        if k=='pillar': continue
        horiz=(x2-x1)>(y2-y1)
        X,Y=TAGPOS.get(wid,((x1+x2)/2,(y1+y2)/2))
        tag(X,Y,wid,'wall',0 if horiz else -90)
TAGPOS={'GW-01':(3.125,53.6),'GW-05':(20.625,51.0),'GW-07':(9.875,91.0),'BW-01':(0.19,50.0),'GW-04':(19.0,31.125),'GW-13':(6.2,60.94),'GW-12':(17.6,46.56),
        'GW-03':(8.875,33.6),'GW-02':(3.6,40.875),'GW-11':(19.0,36.19),'GW-08':(11.0,94.625),'GW-06':(8.2,75.375),'PW-02':(2.94,40.0),'PW-04':(20.81,40.0),
        'FW-01':(9.875,94.0),'FW-03':(20.625,92.0),'FW-02':(18.4,73.375),'FW-04':(19.0,96.875),'FW-05':(18.0,79.94),'PW-03':(19.4,19.94),'PW-01':(5.0,15.69),'PW-05':(6.0,80.19),
        'GW-15':(18.4,80.31),'GW-14':(5.0,69.81),'GW-10':(13.94,34.6),'GW-09':(9.06,43.0),'BW-03':(1.19,98.0),'BW-02':(0.6,89.19)}
def opening(o,W):
    oid,fl,wid,a,b,typ,hinge,swing,h,sill,note=o
    if wid=='FRONT':
        rect(a,b,0,0.75,'#e3f0d8')
        line(a,0.375,b,0.375,'#2f5d3a',0.12)
        line(a+0.3,1.1,b-0.3,1.1,'#2f5d3a',0.03,extra='stroke-dasharray="0.25 0.15"')
        return
    _,x1,x2,y1,y2,k,hh,desc=W[wid]
    horiz=(x2-x1)>(y2-y1)
    # gap
    if horiz: rect(a,b,y1-0.01,y2+0.01,'#fffdf7')
    else: rect(x1-0.01,x2+0.01,a,b,'#fffdf7')
    def P(u,v): return (u,v) if horiz else (v,u)   # u along wall, v across
    v1,v2=(y1,y2) if horiz else (x1,x2)
    for u in (a,b): 
        p,q=P(u,v1),P(u,v2); line(p[0],p[1],q[0],q[1],'#333',0.05)
    if typ=='window':
        for f in (0.3,0.5,0.7):
            v=v1+(v2-v1)*f; p,q=P(a,v),P(b,v); line(p[0],p[1],q[0],q[1],'#2f6fb0',0.045)
    elif typ=='vent':
        for f in (0.35,0.65):
            v=v1+(v2-v1)*f; p,q=P(a,v),P(b,v); line(p[0],p[1],q[0],q[1],'#2f6fb0',0.035,extra='stroke-dasharray="0.15 0.1"')
    elif typ=='arch':
        for v in (v1,v2): p,q=P(a,v),P(b,v); line(p[0],p[1],q[0],q[1],'#777',0.03,extra='stroke-dasharray="0.2 0.12"')
    else:
        face=v2 if swing=='+' else v1; sg=1 if swing=='+' else -1
        leaves=[(a,b-a,1),(b,b-a,-1)] if typ=='door' else [(a,(b-a)/2,1),(b,(b-a)/2,-1)]
        if typ=='door': leaves=[leaves[0]] if hinge=='a' else [leaves[1]]
        for hu,L,dirn in leaves:
            h0=P(hu,face); e=P(hu,face+sg*L); o2=P(hu+dirn*L,face)
            line(h0[0],h0[1],e[0],e[1],'#8a4b12',0.07)
            se,so,sh=S(*e),S(*o2),S(*h0)
            cross=(se[0]-sh[0])*(so[1]-sh[1])-(se[1]-sh[1])*(so[0]-sh[0])
            E(f'<path d="M{se[0]:.3f},{se[1]:.3f} A{L:.3f},{L:.3f} 0 0 {1 if cross>0 else 0} {so[0]:.3f},{so[1]:.3f}" fill="none" stroke="#8a4b12" stroke-width="0.035" stroke-dasharray="0.15 0.1"/>')
def opening_tags(fl,W):
    for o in OPENINGS:
        oid,f,wid,a,b,typ,hinge,swing,h,sill,note=o
        if f!=fl: continue
        if wid=='FRONT': tag((a+b)/2,1.75,oid,'door'); continue
        _,x1,x2,y1,y2,k,hh,desc=W[wid]; horiz=(x2-x1)>(y2-y1)
        off=OPENTAGOFF.get(oid,0.75)
        if horiz: X,Y=(a+b)/2,(y1+y2)/2+off
        else: X,Y=(x1+x2)/2+off,(a+b)/2
        tag(X,Y,oid,'win' if typ in('window','vent') else 'door')
OPENTAGOFF={'W-01':-0.75,'V-01':-0.75,'W-02':0.9,'W-03':-1.0,'W-04':-1.0,'W-05':-1.0,'W-06':-1.0,'V-02':-1.0,'W-07':-1.0,'W-08':0.8,'D-01':-1.4,'D-02':-2.2,'D-03':-1.6,
            'O-01':-0.8,'D-04':-2.6,'D-05':-1.5,'D-06':1.7,'D-07':1.7,'D-08':1.6,'D-09':-1.6,'W-09':-0.8,'W-10':-1.0,'W-11':0.8}
# stairs
A0,A1=4.333,16.0; AX1,AX2=17.5,21.0; LY1,LY2=16.0,19.5; BX1,BX2=11.667,17.5
def stair_A(op=1,dash=''):
    E(f'<g opacity="{op}">'); rect(AX1,AX2,A0,A1,'#c98b5e','#6b3a1c',0.05,extra=dash)
    n=14
    for i in range(1,n): y=A0+i*(A1-A0)/n; line(AX1,y,AX2,y,'#6b3a1c',0.03)
    a=S((AX1+AX2)/2,A0+0.4); b=S((AX1+AX2)/2,A1-0.4)
    E(f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" stroke="#fff" stroke-width="0.08" marker-end="url(#arrW)"/></g>')
def stair_L(op=1,dash=''): rect(AX1,AX2,LY1,LY2,'#d9a37a','#6b3a1c',0.05,extra=f'opacity="{op}" '+dash)
def stair_B(op=1,dash=''):
    E(f'<g opacity="{op}">'); rect(BX1,BX2,LY1,LY2,'#c98b5e','#6b3a1c',0.05,extra=dash)
    n=7
    for i in range(1,n): x=BX2-i*(BX2-BX1)/n; line(x,LY1,x,LY2,'#6b3a1c',0.03)
    a=S(BX2-0.4,(LY1+LY2)/2); b=S(BX1+0.4,(LY1+LY2)/2)
    E(f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" stroke="#fff" stroke-width="0.08" marker-end="url(#arrW)"/></g>')
SPC=(17.0,76.75); SPR=3.0
def spiral(top=False):
    x,y=S(*SPC)
    dash='stroke-dasharray="0.25 0.15"' if top else ''
    E(f'<circle cx="{x}" cy="{y}" r="{SPR}" fill="#c98b5e" stroke="#6b3a1c" stroke-width="0.05" opacity="{0.4 if top else 1}" {dash}/>')
    for k in range(17):
        a=math.radians(-90+k*300/16)
        E(f'<line x1="{x}" y1="{y}" x2="{x+SPR*math.cos(a):.3f}" y2="{y+SPR*math.sin(a):.3f}" stroke="#6b3a1c" stroke-width="0.03" opacity="{0.4 if top else 1}"/>')
    E(f'<circle cx="{x}" cy="{y}" r="0.25" fill="#3a2a1c"/>')
def vehicles():
    rect(11.25,17.25,13.75,28.75,'#fafafa','#555',0.06,extra='rx="1.0"'); rect(11.75,16.75,22.0,23.5,'#a9bccd','#555',0.03); rect(11.75,16.75,16.0,17.2,'#a9bccd','#555',0.03)
    text(14.25,19.5,'CAR 6\' x 15\'',0.42,weight=600,fill='#666')
    for yc in (8.0,14.5,21.0):
        rect(1.6,2.6,yc-3,yc+3,'#7a7f88','#333',0.03,extra='rx="0.4"')
    text(2.1,25.4,'3 bikes',0.36,fill='#555')
def tree():
    x,y=S(12.75,4.25)
    E(f'<circle cx="{x}" cy="{y-2.5}" r="6" fill="#2f7d32" opacity="0.07" stroke="#2f7d32" stroke-width="0.05" stroke-dasharray="0.3 0.2"/>')
    E(f'<circle cx="{x}" cy="{y}" r="0.75" fill="#6b4423" stroke="#3b2412" stroke-width="0.05"/>')
    a=S(12.75,5.0); b=S(12.75,7.5); E(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#5b3a1a" stroke-width="0.15" marker-end="url(#arrT)"/>')
    text(12.75,9.0,'NEEM TREE (to confirm)\ntrunk 1\'6", 3\'6" from road, 7\'6" from west',0.34,weight=600,fill='#2b5d2e')
def porch_steps():
    rect(3.0,8.25,30.75,33.25,'#d8cdbb','#7a6a55',0.04)
    for k in (1,2): y=30.75+k*2.5/3; line(3.0,y,8.25,y,'#7a6a55',0.03)
    text(5.6,32.0,'3 steps up',0.32,fill='#5a4a35')
def chain(fl,X,ys,labels=True,cls='dim'):
    E(f'<g class="{cls}">')
    line(X,ys[0],X,ys[-1],'#555',0.03)
    for y in ys:
        a=S(X-0.2,y-0.2); b=S(X+0.2,y+0.2); E(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#555" stroke-width="0.05"/>')
    for y1,y2 in zip(ys,ys[1:]):
        if y2-y1>=1.8: text(X-0.3,(y1+y2)/2,fmt(y2-y1),0.4,fill='#333',rot=-90)
    E('</g>')
def hchain(Y,xs,cls='dim'):
    E(f'<g class="{cls}">'); line(xs[0],Y,xs[-1],Y,'#555',0.03)
    for x in xs:
        a=S(x-0.2,Y-0.2); b=S(x+0.2,Y+0.2); E(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#555" stroke-width="0.05"/>')
    for x1,x2 in zip(xs,xs[1:]):
        if x2-x1>=1.6: text((x1+x2)/2,Y+0.35,fmt(x2-x1),0.4,fill='#333')
    E('</g>')
def sides():
    text(10.5,-2.1,'NORTH  ·  ROAD AND GATES',0.7,weight=700,fill='#2f6f4f')
    text(11,107.9,'SOUTH  ·  BACK (existing wall)',0.6,weight=700,fill='#2f6f4f')
    text(-3.6,53,'EAST  ·  neighbour house',0.6,weight=700,fill='#2f6f4f',rot=-90)
    text(23.0,53,'WEST  ·  apartment (existing wall)',0.6,weight=700,fill='#2f6f4f',rot=90)
    x,y=S(-2.2,-2.2)
    E(f'<g transform="translate({x},{y})"><circle r="1.1" fill="#fff" stroke="#2f6f4f" stroke-width="0.06"/><polygon points="0,1.0 -0.38,-0.55 0,-0.22 0.38,-0.55" fill="#2f6f4f"/><text y="-1.35" font-size="0.5" font-weight="700" text-anchor="middle" fill="#2f6f4f">N ↓</text></g>')

def ground():
    W=walls_of('G')
    draw_plot('G'); draw_rooms('G'); porch_steps(); tree(); vehicles()
    stair_A(); stair_L(); stair_B(op=0.45,dash='stroke-dasharray="0.2 0.12"')
    text(14.6,20.6,'flight 1B overhead (+7\'6" to +11\'6")',0.3,fill='#6b3a1c')
    spiral()
    draw_walls('G')
    for p in ((0,0.75),(15.0,15.75),(20.25,21.0)): rect(p[0],p[1],0,0.75,'#6b6b6b')
    for o in OPENINGS:
        if o[1]=='G': opening(o,W)
    E('<g class="L-dims">')
    chain('G',-1.3,[0,30.75,40.5,41.25,46.75,60.75,61.125,69.625,70.0,75.0,75.75,89.0,106.0])
    chain('G',22.6,[0,4.333,16.0,19.5,30.75,31.5,36.0,36.375,46.375,46.75,60.75,61.125,70.0,80.125,80.5,94.25,95.0,105.0])
    hchain(-0.9,[0,2.75,3.5,9.25,13.75,14.125,20.25,21.0])
    hchain(104.0,[1.375,9.5,10.25,20.25,21.0])
    E('</g>')
    E('<g class="L-rooms">'); room_labels('G')
    text(14.25,72.8,'ST-2 spiral stair',0.34,weight=600,fill='#3a1f0c')
    text(19.25,10.2,'ST-1A',0.36,weight=700,fill='#fff'); text(19.25,17.75,'ST-1L',0.32,weight=700,fill='#3a1f0c')
    E('</g>')
    E('<g class="L-walls">'); wall_tags('G'); E('</g>')
    E('<g class="L-open">'); opening_tags('G',W); E('</g>')
    sides()
def first():
    W=walls_of('F')
    draw_plot('F')
    draw_walls('G',ghost=True)
    draw_rooms('F'); 
    stair_A(op=0.35,dash='stroke-dasharray="0.2 0.12"'); stair_L(); stair_B()
    spiral(top=True)
    draw_walls('F')
    for o in OPENINGS:
        if o[1]=='F': opening(o,W)
    E('<g class="L-dims">')
    chain('F',22.6,[15.5,20.125,73.0,73.75,79.75,80.125,84.375,84.75,96.5,97.25])
    hchain(14.3,[2.75,3.125,11.667,17.5,21.0])
    hchain(98.6,[9.5,10.25,13.875,14.25,20.25,21.0])
    E('</g>')
    E('<g class="L-rooms">'); room_labels('F')
    text(14.6,17.75,'ST-1B',0.36,weight=700,fill='#fff'); text(19.25,17.75,'ST-1L',0.32,weight=700,fill='#3a1f0c')
    text(14.0,72.2,'ST-2 arrives',0.32,weight=600,fill='#3a1f0c')
    text(10.5,8.0,'below: parking, gates, neem tree',0.45,fill='#888')
    E('</g>')
    E('<g class="L-walls">'); wall_tags('F'); E('</g>')
    E('<g class="L-open">'); opening_tags('F',W); E('</g>')
    sides()

DEFS='''<defs>
<pattern id="hatch" width="0.32" height="0.32" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="0.32" height="0.32" fill="#efebe3"/><line x1="0" y1="0" x2="0" y2="0.32" stroke="#444" stroke-width="0.07"/></pattern>
<pattern id="hatchP" width="0.22" height="0.22" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="0.22" height="0.22" fill="#f4f1ea"/><line x1="0" y1="0" x2="0" y2="0.22" stroke="#666" stroke-width="0.04"/></pattern>
<pattern id="hatchC" width="0.28" height="0.28" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><rect width="0.28" height="0.28" fill="#f6f6f1"/><line x1="0" y1="0" x2="0" y2="0.28" stroke="#6b7d63" stroke-width="0.05"/></pattern>
<pattern id="hatchX" width="0.3" height="0.3" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="0.3" height="0.3" fill="#eeeeee"/><line x1="0" y1="0" x2="0" y2="0.3" stroke="#aaa" stroke-width="0.04"/></pattern>
<marker id="arrW" markerWidth="6" markerHeight="6" refX="3" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L6,3 L0,6 z" fill="#fff"/></marker>
<marker id="arrT" markerWidth="5" markerHeight="5" refX="2.5" refY="2.5" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L5,2.5 L0,5 z" fill="#5b3a1a"/></marker>
</defs>'''
VB=(-5.0,-1.0,30.0,112.0)
def svg(fn,fid):
    global out; out=[]; fn()
    return f'<svg id="svg-{fid}" xmlns="http://www.w3.org/2000/svg" viewBox="{VB[0]} {VB[1]} {VB[2]} {VB[3]}" preserveAspectRatio="xMidYMid meet" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">{DEFS}{"".join(out)}</svg>'
if __name__=='__main__':
    S0=svg(ground,'f0'); S1=svg(first,'f1')
    json.dump({'S0':S0,'S1':S1},open('svgs.json','w'))
    for k,v in (('f0',S0),('f1',S1)): open(f'/private/tmp/claude-502/-Users-jeyant-10189-Work-Personal-own-home-plan/4060cb9c-77fe-4496-bb7d-f3edc22652fc/scratchpad/v1-{k}.svg','w').write(v.replace('<svg ','<svg width="1200" height="4480" ',1))
    print('ok')
