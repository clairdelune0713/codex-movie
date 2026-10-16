"""Inspect real generated audio levels locally; keep the native tracks immutable."""
import hashlib,re,subprocess
from render_movie import ROOT,FF,read,save
j=read(ROOT/'exports/task-journal.json');dest=ROOT/'exports/audio-levels.json'
levels=read(dest) if dest.exists() else {}
for cid,t in j['takes'].items():
    if t['status']!='succeeded':continue
    source=ROOT/t['path'];digest=hashlib.sha256(source.read_bytes()).hexdigest()
    key=cid+'_'+t['id']
    if levels.get(key,{}).get('sha256')==digest:continue
    r=subprocess.run([str(FF),'-hide_banner','-nostdin','-i',str(source),'-vn','-af','volumedetect','-f','null','-'],capture_output=True,text=True,encoding='utf-8',errors='replace')
    if r.returncode:raise RuntimeError('Audio decode failed '+key)
    values={name:float(value) for name,value in re.findall(r'(mean_volume|max_volume): ([\-\d.]+) dB',r.stderr)}
    levels[key]={'sha256':digest,**values}
save(dest,levels)
print('Measured',len(levels),'native tracks; mean level range',min(v['mean_volume'] for v in levels.values()),max(v['mean_volume'] for v in levels.values()),'dBFS; peak range',min(v['max_volume'] for v in levels.values()),max(v['max_volume'] for v in levels.values()),'dBFS.')
