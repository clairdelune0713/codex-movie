"""Audit actual encoded frame counts after the first assembly mismatch."""
import concurrent.futures,re,subprocess
from render_movie import ROOT,FF,read,save
p=read(ROOT/'project.json')
def count(c):
    t=next(t for t in c['takes'] if t['id']==c['active_take_id'])
    path=ROOT/'exports/assembly'/(c['id']+'_'+t['id']+'_normalized.mp4')
    result=subprocess.run([str(FF),'-v','error','-i',str(path),'-map','0:v:0','-c:v','copy','-an','-progress','pipe:1','-nostats','-f','null','-'],capture_output=True,text=True)
    frames=[int(x) for x in re.findall(r'^frame=(\d+)$',result.stdout,re.M)]
    return {'chapter':c['id'],'path':path.relative_to(ROOT).as_posix(),'expected':c['duration']*24,'actual':frames[-1] if frames else None}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:items=list(pool.map(count,p['chapters']))
result={'expected_total':28800,'actual_total':sum(x['actual'] or 0 for x in items),'mismatches':[x for x in items if x['actual']!=x['expected']],'clips':items}
save(ROOT/'exports/normalized-frame-audit.json',result)
print({k:v for k,v in result.items() if k!='clips'})
