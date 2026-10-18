import math, json, html as _H
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
def tip(s): return _H.escape(s,quote=True)
def tag(X,Y,s,kind='wall',rot=0,tipText=None):
    x,y=S(X,Y); w=len(s)*0.25+0.3; h=0.5
    col={'col':('#1f2328','#1f2328','#ffffff'),'beam':('#fff1ee','#c0392b','#a12a1d'),'wall':('#ffffff','#5b5b5b','#333'),'door':('#fff4e8','#a35a1b','#7a3e0c'),'win':('#e8f2ff','#2f6fb0','#1f4f86'),'room':('#2f6f4f','#2f6f4f','#fff')}[kind]
    tr=f' transform="rotate({rot} {x:.3f} {y:.3f})"' if rot else ''
    dt=f' data-tip="{tip(tipText)}"' if tipText else ''
    E(f'<g class="tag-{kind}"{tr}{dt}><rect x="{x-w/2:.3f}" y="{y-h/2:.3f}" width="{w:.3f}" height="{h:.3f}" rx="0.12" fill="{col[0]}" stroke="{col[1]}" stroke-width="0.03"/>'
      f'<text x="{x:.3f}" y="{y+0.13:.3f}" font-size="0.36" font-weight="700" fill="{col[2]}" text-anchor="middle">{s}</text></g>')

FILL={'out':'#e9e8e4','porch':'#efe7da','in':'#fbf6ea','bed':'#fbf0dd','wet':'#dcEEF2','kit':'#e9f1fb','garden':'#cfe7bf','terr':'#ecebe6'}
WALLFILL={'planter':'#8a8f86','outer':'url(#hatch)','part':'url(#hatchP)','comp':'url(#hatchC)','para':'url(#hatchC)','pillar':'#6b6b6b'}

def walls_of(fl): return {w[0]:w for w in WALLS[fl]}
def draw_plot(fl):
    E(f'<polygon points="{pts(PLOT)}" fill="{"#e3f0d8" if fl=="G" else "#f6f7f3"}" stroke="#3d6b35" stroke-width="0.07"/>')
    # west existing apartment wall (outside our land)
    E(f'<polygon points="{pts([(21,0),(21.5,0),(21.5,105),(21,105)])}" fill="url(#hatchX)" stroke="#888" stroke-width="0.03"/>')
    # back existing wall (inside line)
    E(f'<polygon points="{pts([(1.0,106.0),(21,105.0),(21,104.625),(1.375,105.6)])}" fill="url(#hatchX)" stroke="#888" stroke-width="0.03"/>')
def draw_rooms(fl,labels=True):
    for rid,name,P,k in ROOMS[fl]:
        xs=[p[0] for p in P]; ys=[p[1] for p in P]
        sz=f"{fmt(max(xs)-min(xs))} x {fmt(max(ys)-min(ys))}" if len(P)==4 else "irregular"
        E(f'<polygon points="{pts(P)}" fill="{FILL[k]}" data-tip="{tip(rid+" · "+name+" · "+sz+" · "+format(area(P),".0f")+" sq ft")}"/>')
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


def draw_walls(fl,ghost=False):
    for wid,x1,x2,y1,y2,k,h,desc in WALLS[fl]:
        if ghost: rect(x1,x2,y1,y2,'#cfcbc2',extra='opacity="0.6"'); continue
        KN={'outer':'9" outer','part':'4½" partition','comp':'4½" compound','para':'4½" parapet','pillar':'pillar','planter':'planter pillar'}
        rect(x1,x2,y1,y2,WALLFILL[k],'#333',0.035,extra=f'data-tip="{tip(wid+" · "+desc+" · "+KN.get(k,k)+" · "+fmt(max(x2-x1,y2-y1)))}"')
        if k=='planter':
            c=S((x1+x2)/2,(y1+y2)/2)
            for dx,dy,col in ((0,0,'#d6336c'),(-0.35,0.25,'#e8590c'),(0.35,0.25,'#ae3ec9'),(0,-0.38,'#f06595')):
                E(f'<circle cx="{c[0]+dx:.3f}" cy="{c[1]+dy:.3f}" r="0.32" fill="{col}" stroke="#2f7d32" stroke-width="0.08" pointer-events="none"/>')
def wall_tags(fl):
    for wid,x1,x2,y1,y2,k,h,desc in WALLS[fl]:
        if k in ('pillar','planter'): continue
        horiz=(x2-x1)>(y2-y1)
        X,Y=TAGPOS.get(wid,((x1+x2)/2,(y1+y2)/2))
        tag(X,Y,wid,'wall',0 if horiz else -90,tipText=wid+' · '+desc)

def opening(o,W):
    oid,fl,wid,a,b,typ,hinge,swing,h,sill,note=o
    if wid=='FRONT':
        rect(a,b,0,0.75,'#e3f0d8')
        line(a,0.375,b,0.375,'#2f5d3a',0.12)
        if swing:
            W=dict(W); W['FRONT']=('FRONT',0,21,0,0.75,'comp',6,'front line')
            typ='door' if hinge else 'double'
            if not hinge: hinge=None
        else:
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
    elif typ=='fold':
        n=6; pts_=[]
        for i in range(n+1):
            u=a+i*(b-a)/n; v=v1+(v2-v1)*(0.25 if i%2==0 else 0.75); pts_.append(P(u,v))
        E(f'<polyline points="{pts(pts_)}" fill="none" stroke="#2f6fb0" stroke-width="0.06"/>')
        cv=v1-0.35   # curtain on the living side (lower Y)
        wav=[]
        for i in range(25):
            u=a+i*(b-a)/24; wav.append(P(u,cv+0.12*(1 if i%2 else -1)))
        E(f'<polyline points="{pts(wav)}" fill="none" stroke="#b05a8a" stroke-width="0.04"/>')
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
        tt=oid+' · '+note+' · '+fmt(b-a)+' wide'
        if wid=='FRONT': tag((a+b)/2,2.6 if swing else 1.75,oid,'door',tipText=tt); continue
        _,x1,x2,y1,y2,k,hh,desc=W[wid]; horiz=(x2-x1)>(y2-y1)
        off=OPENTAGOFF.get(oid,0.75)
        if horiz: X,Y=(a+b)/2,(y1+y2)/2+off
        else: X,Y=(x1+x2)/2+off,(a+b)/2
        tag(X,Y,oid,'win' if typ in('window','vent') else 'door',tipText=tt)

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

def spiral(top=False):
    x,y=S(*SPC)
    dash='stroke-dasharray="0.25 0.15"' if top else ''
    E(f'<circle cx="{x}" cy="{y}" r="{SPR}" fill="#c98b5e" stroke="#6b3a1c" stroke-width="0.05" opacity="{0.4 if top else 1}" {dash}/>')
    for k in range(17):
        a=math.radians(-90+k*300/16)
        E(f'<line x1="{x}" y1="{y}" x2="{x+SPR*math.cos(a):.3f}" y2="{y+SPR*math.sin(a):.3f}" stroke="#6b3a1c" stroke-width="0.03" opacity="{0.4 if top else 1}"/>')
    E(f'<circle cx="{x}" cy="{y}" r="0.25" fill="#3a2a1c"/>')
def vehicles():
    import model as _m
    cx1,cx2,cy1,cy2=getattr(_m,'CAR',(11.25,17.25,13.75,28.75))
    rect(cx1,cx2,cy1,cy2,'#fafafa','#555',0.06,extra='rx="1.0"'); rect(cx1+0.5,cx2-0.5,cy1+8.25,cy1+9.75,'#a9bccd','#555',0.03); rect(cx1+0.5,cx2-0.5,cy1+2.25,cy1+3.45,'#a9bccd','#555',0.03)
    text((cx1+cx2)/2,cy1+5.75,'CAR 6\' x 15\'',0.42,weight=600,fill='#666')
    for yc in getattr(_m,'BIKES',(7.0,13.5,20.0)):
        bike(2.0,yc)
    text(2.0,getattr(_m,'BIKES',(7.0,13.5,20.0))[-1]+4.0,'3 two-wheelers',0.34,fill='#555')
def bike(cx,cy):
    # top view of a two-wheeler, 2'6" x 6', front toward the road
    for wy in (cy-2.35,cy+2.35):
        x,y=S(cx,wy); E(f'<ellipse cx="{x:.3f}" cy="{y:.3f}" rx="0.22" ry="0.75" fill="#2b2b2b"/>')
    x1,y1=S(cx-0.42,cy+1.9); E(f'<rect x="{x1:.3f}" y="{y1:.3f}" width="0.84" height="3.8" rx="0.35" fill="#6d7480" stroke="#333" stroke-width="0.03"/>')
    x2,y2=S(cx-0.3,cy+0.9); E(f'<rect x="{x2:.3f}" y="{y2:.3f}" width="0.6" height="1.6" rx="0.25" fill="#3c4048"/>')
    a=S(cx-1.25,cy-1.75); b=S(cx+1.25,cy-1.75); E(f'<line x1="{a[0]:.3f}" y1="{a[1]:.3f}" x2="{b[0]:.3f}" y2="{b[1]:.3f}" stroke="#333" stroke-width="0.12" stroke-linecap="round"/>')
def tree():
    x,y=S(12.75,4.25)
    E(f'<circle cx="{x}" cy="{y-2.5}" r="6" fill="#2f7d32" opacity="0.07" stroke="#2f7d32" stroke-width="0.05" stroke-dasharray="0.3 0.2"/>')
    E(f'<circle cx="{x}" cy="{y}" r="0.75" fill="#6b4423" stroke="#3b2412" stroke-width="0.05"/>')
    a=S(12.75,5.0); b=S(12.75,7.5); E(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#5b3a1a" stroke-width="0.15" marker-end="url(#arrT)"/>')
    text(12.75,9.0,'NEEM TREE (to confirm)\ntrunk 1\'6", 3\'6" from road, 7\'6" from west',0.34,weight=600,fill='#2b5d2e')
def porch_steps():
    import model as _m
    y0=getattr(_m,'PORCH_STEPS_Y',30.75)
    sx1,sx2=getattr(_m,'PORCH_STEPS_X',(3.0,8.25))
    rect(sx1,sx2,y0,y0+2.5,'#d8cdbb','#7a6a55',0.04)
    for k in (1,2): y=y0+k*2.5/3; line(sx1,y,sx2,y,'#7a6a55',0.03)
    text((sx1+sx2)/2,y0+1.25,'3 steps up',0.32,fill='#5a4a35')
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
    text(10.5,-2.1,'NORTH  ·  ROAD (17\' wide) AND GATES',0.7,weight=700,fill='#2f6f4f')
    text(11,107.9,'SOUTH  ·  BACK (existing wall)',0.6,weight=700,fill='#2f6f4f')
    text(-3.6,53,'EAST  ·  neighbour house',0.6,weight=700,fill='#2f6f4f',rot=-90)
    text(23.0,53,'WEST  ·  apartment (existing wall)',0.6,weight=700,fill='#2f6f4f',rot=90)
    x,y=S(-2.2,-2.2)
    E(f'<g transform="translate({x},{y})"><circle r="1.1" fill="#fff" stroke="#2f6f4f" stroke-width="0.06"/><polygon points="0,1.0 -0.38,-0.55 0,-0.22 0.38,-0.55" fill="#2f6f4f"/><text y="-1.35" font-size="0.5" font-weight="700" text-anchor="middle" fill="#2f6f4f">N ↓</text></g>')

def borewell():
    import model as _m
    for bid,bx,by,desc in getattr(_m,'BORES',[('BR-01',*BOREWELL,'existing')]):
        x,y=S(bx,by)
        E(f'<g class="bore" data-tip="{tip(bid+" · Borewell (existing) · "+desc)}"><circle cx="{x:.3f}" cy="{y:.3f}" r="0.55" fill="#dff1ff" stroke="#1a6ea0" stroke-width="0.08"/><circle cx="{x:.3f}" cy="{y:.3f}" r="0.18" fill="#1a6ea0"/></g>')
        E(f'<g class="L-rooms"><text x="{x:.3f}" y="{y+1.05:.3f}" font-size="0.34" font-weight="700" fill="#1a6ea0" text-anchor="middle">{bid} BORE</text>'
          f'<text x="{x:.3f}" y="{y+1.45:.3f}" font-size="0.26" fill="#1a6ea0" text-anchor="middle">{desc}</text></g>')

def draw_furniture(fl,_late=False):
    import model as _m
    items=[f for f in getattr(_m,'FURNITURE',[]) if f[1]==fl and (f[7]=='store')==bool(_late)]
    if not items: return
    E('<g class="L-furn">')
    for fid,f,name,x1,x2,y1,y2,k,side,note in items:
        w,d=x2-x1,y2-y1
        E(f'<g class="fu" data-tip="{tip(fid+" · "+name+" · "+fmt(w)+" x "+fmt(d)+" · "+note)}">')
        def R_(a1,a2,b1,b2,fill,stroke='#6b5a48',sw=0.035,extra=''): rect(a1,a2,b1,b2,fill,stroke,sw,extra=extra)
        if k=='bed':
            R_(x1,x2,y1,y2,'#ffffff','#555',0.05)
            hd=0.35; pl=1.1
            if side=='x2': R_(x2-hd,x2,y1,y2,'#7a5a43'); R_(x2-hd-pl,x2-hd-0.1,y1+0.25,y1+d/2-0.1,'#f3f3f3','#999',0.03); R_(x2-hd-pl,x2-hd-0.1,y1+d/2+0.1,y2-0.25,'#f3f3f3','#999',0.03); R_(x1+0.1,x2-hd-pl-0.2,y1+0.08,y2-0.08,'#9fb7c9','#7d97ab',0.03)
            if side=='x1': R_(x1,x1+hd,y1,y2,'#7a5a43'); R_(x1+hd+0.1,x1+hd+pl,y1+0.25,y1+d/2-0.1,'#f3f3f3','#999',0.03); R_(x1+hd+0.1,x1+hd+pl,y1+d/2+0.1,y2-0.25,'#f3f3f3','#999',0.03); R_(x1+hd+pl+0.2,x2-0.1,y1+0.08,y2-0.08,'#9fb7c9','#7d97ab',0.03)
            if side=='y2': R_(x1,x2,y2-hd,y2,'#7a5a43'); R_(x1+0.25,x1+w/2-0.1,y2-hd-pl,y2-hd-0.1,'#f3f3f3','#999',0.03); R_(x1+w/2+0.1,x2-0.25,y2-hd-pl,y2-hd-0.1,'#f3f3f3','#999',0.03); R_(x1+0.08,x2-0.08,y1+0.1,y2-hd-pl-0.2,'#9fb7c9','#7d97ab',0.03)
            if side=='y1': R_(x1,x2,y1,y1+hd,'#7a5a43'); R_(x1+0.25,x1+w/2-0.1,y1+hd+0.1,y1+hd+pl,'#f3f3f3','#999',0.03); R_(x1+w/2+0.1,x2-0.25,y1+hd+0.1,y1+hd+pl,'#f3f3f3','#999',0.03); R_(x1+0.08,x2-0.08,y1+hd+pl+0.2,y2-0.1,'#9fb7c9','#7d97ab',0.03)
        elif k=='sofa':
            R_(x1,x2,y1,y2,'#7f97c2','#4f6a96',0.05,extra='rx="0.25"')
            if side=='x1': R_(x1,x1+0.75,y1,y2,'#5d77a5','#4f6a96'); R_(x1+0.75,x2,y1,y1+0.6,'#5d77a5','#4f6a96'); R_(x1+0.75,x2,y2-0.6,y2,'#5d77a5','#4f6a96')
            n=3
            for i in range(1,n): yy=y1+0.6+i*(d-1.2)/n; line(x1+0.8,yy,x2-0.1,yy,'#4f6a96',0.03)
        elif k=='table': R_(x1,x2,y1,y2,'#a07a52','#6b4f32',0.04,extra='rx="0.3"')
        elif k=='chair': R_(x1,x2,y1,y2,'#c9a77f','#6b4f32',0.03,extra='rx="0.2"')
        elif k in ('cab','desk'): R_(x1,x2,y1,y2,'#c9a77f' if k=='cab' else '#b48a5f','#6b4f32',0.04)
        elif k=='ward':
            R_(x1,x2,y1,y2,'#d9c3a3','#6b4f32',0.05); line(x1,y1,x2,y2,'#6b4f32',0.03); line(x1,y2,x2,y1,'#6b4f32',0.03)
        elif k=='shelf':
            R_(x1,x2,y1,y2,'#d9c3a3','#6b4f32',0.04)
            for i in range(1,4): yy=y1+i*d/4; line(x1,yy,x2,yy,'#6b4f32',0.025)
        elif k in ('counter','counter2'):
            R_(x1,x2,y1,y2,'#3b3f45' if k=='counter' else '#6d727a','#222',0.04)
            if side=='sink':
                cy=(y1+y2)/2-0.5; R_(x1+0.3,x2-0.3,cy-1.0,cy+1.0,'#cfe3f2','#9ab',0.03,extra='rx="0.2"')
            if side=='hob':
                cx=(x1+x2)/2
                for dx in (-0.55,0.55):
                    for dy in (-0.45,0.45):
                        a=S(cx+dx,(y1+y2)/2+dy); E(f'<circle cx="{a[0]:.3f}" cy="{a[1]:.3f}" r="0.3" fill="none" stroke="#ddd" stroke-width="0.05"/>')
        elif k=='fridge':
            R_(x1,x2,y1,y2,'#eef2f5','#777',0.04); text((x1+x2)/2,(y1+y2)/2,'FRIDGE',0.32,weight=700,fill='#666')
        elif k=='appl': R_(x1,x2,y1,y2,'#e9ecef','#555',0.035,extra='rx="0.12"')
        elif k=='over': R_(x1,x2,y1,y2,'none','#555',0.04,extra='stroke-dasharray="0.2 0.12"')
        elif k=='tv':
            R_(x1,x2,y1,y2,'#8b6a45','#5a4128',0.04); R_(x1+0.15,x1+0.35,y1+0.6,y2-0.6,'#222','#111',0.02)
        elif k=='wc':
            R_(x1,x2,y1,y2,'none','none',0)
            if side=='y1': R_(x1+0.1,x2-0.1,y1,y1+0.6,'#f4f6f8','#777',0.04); cx,cy,rx,ry=(x1+x2)/2,y1+1.3,0.55,0.65
            elif side=='x2': R_(x2-0.6,x2,y1+0.1,y2-0.1,'#f4f6f8','#777',0.04); cx,cy,rx,ry=x2-1.25,(y1+y2)/2,0.65,0.55
            else: R_(x1,x1+0.6,y1+0.1,y2-0.1,'#f4f6f8','#777',0.04); cx,cy,rx,ry=x1+1.25,(y1+y2)/2,0.65,0.55
            a=S(cx,cy); E(f'<ellipse cx="{a[0]:.3f}" cy="{a[1]:.3f}" rx="{rx}" ry="{ry}" fill="#f4f6f8" stroke="#777" stroke-width="0.04"/>')
        elif k=='basin':
            R_(x1,x2,y1,y2,'#f4f6f8','#777',0.04); a=S((x1+x2)/2,(y1+y2)/2); E(f'<ellipse cx="{a[0]:.3f}" cy="{a[1]:.3f}" rx="{w/2-0.2:.3f}" ry="{d/2-0.2:.3f}" fill="#dceaf3" stroke="#89a" stroke-width="0.03"/>')
        elif k=='shower':
            R_(x1,x2,y1,y2,'url(#hatchW)','#6c8fa8',0.04); a=S((x1+x2)/2,(y1+y2)/2); E(f'<circle cx="{a[0]:.3f}" cy="{a[1]:.3f}" r="0.15" fill="#6c8fa8"/>')
        elif k=='wm':
            R_(x1,x2,y1,y2,'#f4f6f8','#777',0.04); a=S((x1+x2)/2,(y1+y2)/2); E(f'<circle cx="{a[0]:.3f}" cy="{a[1]:.3f}" r="0.65" fill="#dceaf3" stroke="#777" stroke-width="0.04"/>')
        elif k=='tvwall':
            R_(x1,x2,y1,y2,'#a07a52','#5a4128',0.05)
            n=6
            for i in range(1,n):
                yy=y1+i*d/n; line(x1,yy,x2,yy,'#5a4128',0.025)
            R_(x1+0.08,x1+0.3,y1+d*0.33,y1+d*0.67,'#1d1d1d','#000',0.02)
            text((x1+x2)/2-0.05,y1+d*0.15,'shelves',0.26,fill='#3a2a1a',rot=-90); text((x1+x2)/2-0.05,y1+d*0.85,'showcase',0.26,fill='#3a2a1a',rot=-90)
        elif k=='store2':
            R_(x1,x2,y1,y2,'#cfb48f','#5a4128',0.06)
            for i in range(1,4): yy=y1+i*d/4; line(x1,yy,x2,yy,'#5a4128',0.03)
            line(x1,y1,x2,y2,'#5a4128',0.025); line(x1,y2,x2,y1,'#5a4128',0.025)
        elif k=='iwc':
            R_(x1,x2,y1,y2,'#f4f6f8','#777',0.04,extra='rx="0.2"')
            if w>d:   # long along x: user faces west (+x), foot rests at the east end
                a=S((x1+x2)/2+0.2,(y1+y2)/2); E(f'<ellipse cx="{a[0]:.3f}" cy="{a[1]:.3f}" rx="0.7" ry="0.45" fill="#dceaf3" stroke="#777" stroke-width="0.04"/>')
                for dy in (-0.6,0.6):
                    b=S(x1+0.45,(y1+y2)/2+dy); E(f'<rect x="{b[0]-0.3:.3f}" y="{b[1]-0.22:.3f}" width="0.6" height="0.44" rx="0.1" fill="#bfc8cf"/>')
            else:
                a=S((x1+x2)/2,(y1+y2)/2+0.2); E(f'<ellipse cx="{a[0]:.3f}" cy="{a[1]:.3f}" rx="0.45" ry="0.7" fill="#dceaf3" stroke="#777" stroke-width="0.04"/>')
                for dx in (-0.6,0.6):
                    b=S((x1+x2)/2+dx,y1+0.45); E(f'<rect x="{b[0]-0.22:.3f}" y="{b[1]-0.3:.3f}" width="0.44" height="0.6" rx="0.1" fill="#bfc8cf"/>')
        elif k=='acin':
            R_(x1,x2,y1,y2,'#ffffff','#2f6fb0',0.05,extra='rx="0.1"'); line(x1+0.15,y1+0.2,x1+0.15,y2-0.2,'#2f6fb0',0.03)
        elif k=='acout':
            R_(x1,x2,y1,y2,'#e8edf2','#2f6fb0',0.05); a=S((x1+x2)/2,(y1+y2)/2+0.35); E(f'<circle cx="{a[0]:.3f}" cy="{a[1]:.3f}" r="0.5" fill="none" stroke="#2f6fb0" stroke-width="0.05"/>')
            text((x1+x2)/2,(y1+y2)/2-0.75,'AC',0.3,weight=700,fill='#2f6fb0')
        elif k=='sinkbowl':
            R_(x1,x2,y1,y2,'#cfe3f2','#6c8fa8',0.04,extra='rx="0.2"'); a=S((x1+x2)/2,(y1+y2)/2); E(f'<circle cx="{a[0]:.3f}" cy="{a[1]:.3f}" r="0.1" fill="#6c8fa8"/>')
        elif k=='hob':
            R_(x1,x2,y1,y2,'#1f1f1f','#000',0.04)
            for dy in (-0.45,0.45):
                a=S((x1+x2)/2,(y1+y2)/2+dy); E(f'<circle cx="{a[0]:.3f}" cy="{a[1]:.3f}" r="0.33" fill="none" stroke="#e8590c" stroke-width="0.06"/>')
            R_(x1-0.02,x1+0.6,y1,y2,'none','#999',0.04,extra='stroke-dasharray="0.12 0.08"')
        elif k=='bucket':
            a=S((x1+x2)/2,(y1+y2)/2); E(f'<circle cx="{a[0]:.3f}" cy="{a[1]:.3f}" r="0.36" fill="#5aa0d6" stroke="#2f6fb0" stroke-width="0.04"/>')
        elif k=='geyser':
            R_(x1,x2,y1,y2,'#ffffff','#999',0.04); text((x1+x2)/2,(y1+y2)/2,'G',0.3,weight=700,fill='#c0392b')
        elif k=='fan':
            a=S((x1+x2)/2,(y1+y2)/2); E(f'<circle cx="{a[0]:.3f}" cy="{a[1]:.3f}" r="0.45" fill="#fff" stroke="#555" stroke-width="0.04"/>')
            line(x1+0.2,y1+0.2,x2-0.2,y2-0.2,'#555',0.04); line(x1+0.2,y2-0.2,x2-0.2,y1+0.2,'#555',0.04)
        elif k=='curtain':
            if w>d: line(x1,(y1+y2)/2,x2,(y1+y2)/2,'#b05a8a',0.05,extra='stroke-dasharray="0.15 0.08"')
            else: line((x1+x2)/2,y1,(x1+x2)/2,y2,'#b05a8a',0.05,extra='stroke-dasharray="0.15 0.08"')
        elif k=='washpad':
            R_(x1,x2,y1,y2,'#d7dde2','#6c7a86',0.04); a=S((x1+x2)/2,(y1+y2)/2)
            E(f'<rect x="{a[0]-0.2:.3f}" y="{a[1]-0.2:.3f}" width="0.4" height="0.4" fill="#6c7a86"/>')
            text((x1+x2)/2,y2-0.45,'tap',0.28,fill='#334')
        elif k=='store':
            R_(x1,x2,y1,y2,'url(#hatchS)','#5a4128',0.08)
            text((x1+x2)/2,(y1+y2)/2,'STORE',0.4,weight=700,fill='#3a2a1a',rot=-90)
            line(x1,y1+1.5,x1,y2-1.5,'#fff',0.14); line(x1,y1+1.5,x1,y2-1.5,'#8a4b12',0.06,extra='stroke-dasharray="0.2 0.1"')
        # code tag
        cx,cy=(x1+x2)/2,(y1+y2)/2
        if k not in ('fridge','tvwall','store','acout','curtain','geyser','bucket','fan'):
            x,y=S(cx,cy); E(f'<text x="{x:.3f}" y="{y+0.11:.3f}" font-size="0.28" font-weight="700" fill="#2b2b2b" text-anchor="middle" stroke="#fff" stroke-width="0.08" paint-order="stroke">{fid}</text>')
        E('</g>')
    E('</g>')

# structure: pillars (solid) and the beams above them (dashed red), in the L-struct layer
BEAMTAG={'B-01':(7.0,20.125),'B-02':(6.0,30.0),'B-03':(6.0,36.2),'B-04':(6.0,46.5),'B-05':(14.6,58.94),'B-06':(15.0,66.625),'B-07':(6.8,73.375),'B-08':(15.6,80.44),
         'B-09':(14.6,94.75),'B-10':(3.125,25.5),'B-11':(9.875,79.0),'B-12':(20.625,25.5),'B-13':(14.0,73.5),'B-14':(16.0,80.25),'B-15':(14.0,97.0),'B-16':(9.875,86.5),'B-17':(20.625,86.5)}
COLTAG={'C-14':(10.8,74.6),'C-18':(8.95,92.6),'C-20':(5.45,69.0),'C-21':(5.45,72.5)}
def draw_struct(fl):
    import model as _m
    E('<g class="L-struct">')
    for bid,lv,x1,x2,y1,y2,d,note in getattr(_m,'BEAMS',[]):
        if lv!=fl: continue
        span=max(x2-x1,y2-y1)
        rect(x1,x2,y1,y2,'rgba(192,57,43,0.10)','#c0392b',0.05,extra=f'stroke-dasharray="0.3 0.18" data-tip="{tip(bid+" · Beam 9 in wide x "+d+" deep · "+fmt(span)+" long · "+note)}"')
    for cid,fls,x1,x2,y1,y2,note in getattr(_m,'COLUMNS',[]):
        up=fl=='G' or fls=='G+F'
        t=cid+' · Pillar '+_m.COL_SIZE+' · '+note+('' if up else ' · future hall pillar: bars left sticking up at the terrace')
        if up: rect(x1,x2,y1,y2,'#1f2328','#000',0.03,extra=f'data-tip="{tip(t)}"')
        else: rect(x1,x2,y1,y2,'none','#1f2328',0.05,extra=f'stroke-dasharray="0.15 0.1" data-tip="{tip(t)}"')
    for cid,fls,x1,x2,y1,y2,note in getattr(_m,'COLUMNS',[]):
        cx,cy=(x1+x2)/2,(y1+y2)/2
        X=x1-0.55 if x1<5 or abs(x1-9.5)<0.01 else x2+0.55
        X,cy=COLTAG.get(cid,(X,cy))
        tag(X,cy,cid,'col',-90,tipText=cid+' · Pillar '+_m.COL_SIZE+' · '+note)
    for bid,lv,x1,x2,y1,y2,d,note in getattr(_m,'BEAMS',[]):
        if lv!=fl: continue
        X,Y=BEAMTAG.get(bid,((x1+x2)/2,(y1+y2)/2))
        tag(X,Y,bid,'beam',0 if (x2-x1)>(y2-y1) else -90,tipText=bid+' · Beam 9" x '+d+' · '+note)
    E('</g>')

def ground():
    W=walls_of('G')
    draw_plot('G'); draw_rooms('G'); porch_steps(); tree(); vehicles()
    draw_furniture('G')
    stair_A(); stair_L(); stair_B(op=0.45,dash='stroke-dasharray="0.2 0.12"')
    E('<g opacity="0.72">'); draw_furniture('G',_late=True); E('</g>')
    text(14.6,20.6,'flight 1B overhead (+7\'6" to +11\'6")',0.3,fill='#6b3a1c')
    spiral()
    draw_walls('G')
    for o in OPENINGS:
        if o[1]=='G': opening(o,W)
    E('<g class="L-dims">')
    chain('G',-1.3,CH_G_E)
    chain('G',22.6,CH_G_W)
    import model as _m2
    hchain(-0.9,getattr(_m2,'CH_G_FRONT',[0,2.75,3.5,9.25,13.75,14.125,20.25,21.0]))
    hchain(CH_G_BACK_Y,[1.375,9.5,10.25,20.25,21.0])
    E('</g>')
    E('<g class="L-rooms">'); room_labels('G')
    import model as _m
    for X,Y,t,sz in getattr(_m,'EXTRA_TEXT',[]): text(X,Y,t,sz,weight=600,fill='#555')
    text(SPC[0]-2.75,SPC[1]-3.95,'ST-2 spiral stair',0.34,weight=600,fill='#3a1f0c')
    text(19.25,10.2,'ST-1A',0.36,weight=700,fill='#fff'); text(19.25,17.75,'ST-1L',0.32,weight=700,fill='#3a1f0c')
    E('</g>')
    borewell()
    draw_struct('G')
    E('<g class="L-walls">'); wall_tags('G'); E('</g>')
    E('<g class="L-open">'); opening_tags('G',W); E('</g>')
    sides()
def first():
    W=walls_of('F')
    draw_plot('F')
    draw_walls('G',ghost=True)
    draw_rooms('F'); draw_furniture('F')
    stair_A(op=0.35,dash='stroke-dasharray="0.2 0.12"'); stair_L(); stair_B()
    spiral(top=True)
    draw_walls('F')
    for o in OPENINGS:
        if o[1]=='F': opening(o,W)
    E('<g class="L-dims">')
    chain('F',22.6,CH_F_W)
    hchain(14.3,[2.75,3.125,11.667,17.5,21.0])
    hchain(CH_F_BACK_Y,[9.5,10.25,13.875,14.25,20.25,21.0])
    E('</g>')
    E('<g class="L-rooms">'); room_labels('F')
    text(14.6,17.75,'ST-1B',0.36,weight=700,fill='#fff'); text(19.25,17.75,'ST-1L',0.32,weight=700,fill='#3a1f0c')
    text(SPC[0]-3.0,SPC[1]-4.55,'ST-2 arrives',0.32,weight=600,fill='#3a1f0c')
    text(10.5,8.0,'below: parking, gates, neem tree',0.45,fill='#888')
    E('</g>')
    draw_struct('F')
    E('<g class="L-walls">'); wall_tags('F'); E('</g>')
    E('<g class="L-open">'); opening_tags('F',W); E('</g>')
    sides()

DEFS='''<defs>
<pattern id="hatch" width="0.32" height="0.32" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="0.32" height="0.32" fill="#efebe3"/><line x1="0" y1="0" x2="0" y2="0.32" stroke="#444" stroke-width="0.07"/></pattern>
<pattern id="hatchP" width="0.22" height="0.22" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="0.22" height="0.22" fill="#f4f1ea"/><line x1="0" y1="0" x2="0" y2="0.22" stroke="#666" stroke-width="0.04"/></pattern>
<pattern id="hatchC" width="0.28" height="0.28" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><rect width="0.28" height="0.28" fill="#f6f6f1"/><line x1="0" y1="0" x2="0" y2="0.28" stroke="#6b7d63" stroke-width="0.05"/></pattern>
<pattern id="hatchX" width="0.3" height="0.3" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="0.3" height="0.3" fill="#eeeeee"/><line x1="0" y1="0" x2="0" y2="0.3" stroke="#aaa" stroke-width="0.04"/></pattern>
<pattern id="hatchS" width="0.35" height="0.35" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="0.35" height="0.35" fill="#e6d6bd"/><line x1="0" y1="0" x2="0" y2="0.35" stroke="#a8875e" stroke-width="0.05"/></pattern>
<pattern id="hatchW" width="0.3" height="0.3" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="0.3" height="0.3" fill="#e3eef5"/><line x1="0" y1="0" x2="0" y2="0.3" stroke="#a9c1d2" stroke-width="0.04"/></pattern>
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
