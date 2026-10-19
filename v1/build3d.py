import json, export3d, time
t=open('living3d_template.html').read()
open('/Users/jeyant-10189/Work/Personal/own/home-plan/3d/living-room.html','w').write(t.replace('__PLAN__',json.dumps(export3d.data)).replace('__BUILD__',str(int(time.time()))))
print('3d/living-room.html written')
