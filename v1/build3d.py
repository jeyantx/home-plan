import json, export3d, time
t=open('living3d_template.html').read()
# cache token = hash of the models and assets: a plan-only rebuild keeps it, so browsers reuse the downloaded files
import hashlib,os
_h=hashlib.md5()
for _d in ('3d/models','3d/assets'):
    for _r,_ds,_fs in sorted(os.walk('/Users/jeyant-10189/Work/Personal/own/home-plan/'+_d)):
        _ds.sort()
        for _f in sorted(_fs):
            _h.update(_f.encode());_h.update(open(os.path.join(_r,_f),'rb').read())
BUILD=_h.hexdigest()[:10]
open('/Users/jeyant-10189/Work/Personal/own/home-plan/3d/living-room.html','w').write(t.replace('__PLAN__',json.dumps(export3d.data)).replace('__BUILD__',BUILD))
print('3d/living-room.html written')
k=open('kitchen_template.html').read()
open('/Users/jeyant-10189/Work/Personal/own/home-plan/3d/kitchen.html','w').write(k.replace('__PLAN__',json.dumps(export3d.data)).replace('__BUILD__',BUILD))
print('3d/kitchen.html written')
