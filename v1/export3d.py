# Exports the approved plan (model.py) as JSON for the 3D page. Units: feet.
import json, model as M
def walls(fl): return [dict(id=w[0],x1=w[1],x2=w[2],y1=w[3],y2=w[4],kind=w[5],h=w[6],desc=w[7]) for w in M.WALLS[fl]]
def rooms(fl): return [dict(id=r[0],name=r[1],pts=r[2],kind=r[3]) for r in M.ROOMS[fl]]
ops=[dict(id=o[0],fl=o[1],wall=o[2],a=o[3],b=o[4],type=o[5],hinge=o[6],swing=o[7],h=o[8],sill=o[9],note=o[10]) for o in M.OPENINGS]
fu=[dict(id=f[0],fl=f[1],name=f[2],x1=f[3],x2=f[4],y1=f[5],y2=f[6],kind=f[7],side=f[8],note=f[9]) for f in getattr(M,'FURNITURE',[])]
data=dict(walls=dict(G=walls('G'),F=walls('F')),rooms=dict(G=rooms('G'),F=rooms('F')),openings=ops,furniture=fu,
          plot=M.PLOT,car=getattr(M,'CAR',None),porchY=getattr(M,'PORCH_STEPS_Y',30.75),underground=getattr(M,'UNDERGROUND',None),kitchen=dict(modules=getattr(M,'KITCHEN_MODULES',[]),notes=getattr(M,'KITCHEN_NOTES',[]),KCH=M.KCH,KTOP=M.KTOP,KPL=M.KPL,KLOW=M.KLOW,KBF=M.KBF,KUP1=M.KUP1,KUP2=M.KUP2,KLOFT2=M.KLOFT2),bikes=getattr(M,'BIKES',None),spiral=dict(c=M.SPC,r=M.SPR,**getattr(M,'ST2',{})),spec=getattr(M,'SPEC',{}),
          columns=[dict(id=c[0],floors=c[1],x1=c[2],x2=c[3],y1=c[4],y2=c[5],note=c[6]) for c in getattr(M,'COLUMNS',[])],
          beams=[dict(id=b[0],level=b[1],x1=b[2],x2=b[3],y1=b[4],y2=b[5],depth=b[6],note=b[7]) for b in getattr(M,'BEAMS',[])],ff=M.FF_LEVEL,backwall=getattr(M,'BACK_WALL',None),platform=getattr(M,'SIDE_PLATFORM',None),levels=getattr(M,'LEVELS',None),ramp=getattr(M,'RAMP',None),plants=[dict(id=c,type=t,x=x,y=y) for c,t,x,y in getattr(M,'PLANTS',[])])
if __name__=='__main__':
    print(json.dumps(data))
