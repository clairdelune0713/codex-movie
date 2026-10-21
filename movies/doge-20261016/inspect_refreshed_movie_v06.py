"""Inspect the actual stitched output at every edit; no generation requests."""
import hashlib,re,subprocess
from PIL import Image,ImageDraw
import render_finale_refresh as r

manifest=r.read(r.ROOT/'exports/whole-movie-refresh-20261021-v06-manifest.json')
source=r.ROOT/manifest['path'];digest=hashlib.sha256(source.read_bytes()).hexdigest()
folder=r.ROOT/'exports'/('whole-movie-inspection-'+digest[:10]);folder.mkdir(exist_ok=True)
samples=[('OPEN',0.083)]
for c in manifest['chapters']:
    samples.extend([(f"S{c['scene']} start",c['start']+.125),(f"S{c['scene']} end",c['end']-.125)])
samples.extend([('S49 reunion toy',1023.5),('FADE',1044.95)])
for scene,label,within in [(10,'pilot',2),(13,'framing repair',16),(22,'cartoon photo',15.4),(26,'taxi driver',3.3),(35,'obstruction',8),(35,'train driver',11.5),(36,'bus occupants',5.5)]:
    chapter=next(c for c in manifest['chapters'] if c['scene']==scene)
    samples.append((f'S{scene} {label}',chapter['start']+within))
frames=[]
for i,(label,sec) in enumerate(samples):
    target=folder/f'frame-{i:02d}-{sec:.3f}.jpg'
    if not target.exists():
        result=subprocess.run([str(r.FF),'-v','error','-ss',str(sec),'-i',str(source),'-frames:v','1','-q:v','2',str(target)],capture_output=True)
        assert result.returncode==0 and target.exists()
    frames.append({'label':label,'time':sec,'path':target.relative_to(r.ROOT).as_posix()})
pages=[]
for offset in range(0,len(frames),16):
    page=Image.new('RGB',(1360,916),'#1c2025');draw=ImageDraw.Draw(page)
    draw.text((12,10),'Actual final export: all scene boundaries / no overlays in movie',fill='white')
    for i,f in enumerate(frames[offset:offset+16]):
        x=(i%4)*340;y=40+(i//4)*219
        image=Image.open(r.ROOT/f['path']).resize((336,189))
        page.paste(image,(x+2,y));draw.text((x+8,y+193),f"{f['label']} | {f['time']:.3f}s",fill='white')
    target=folder/f'contact-{offset//16+1:02d}.jpg';page.save(target,quality=93);pages.append(target.relative_to(r.ROOT).as_posix())
audio=subprocess.run([str(r.FF),'-hide_banner','-nostdin','-i',str(source),'-vn','-af','volumedetect,silencedetect=noise=-55dB:d=1.5','-f','null','-'],capture_output=True,text=True,encoding='utf-8',errors='replace')
assert audio.returncode==0
mean=re.search(r'mean_volume: ([\-\w.]+) dB',audio.stderr);peak=re.search(r'max_volume: ([\-\w.]+) dB',audio.stderr)
assert mean and mean[1]!='-inf' and peak
silences=[float(x) for x in re.findall(r'silence_duration: ([\d.]+)',audio.stderr)]
streams=re.findall(r'Stream #\d+:\d+[^\n]*',audio.stderr.split('Stream mapping:',1)[0])
assert len(streams)==2 and not any('Subtitle:' in s for s in streams)
report={'source_path':manifest['path'],'source_sha256':digest,'size_bytes':source.stat().st_size,
    'checked_at':r.now(),'frames':frames,'contact_pages':pages,'visual_review_pending':True,
    'audio':{'mean_dbfs':float(mean[1]),'peak_dbfs':float(peak[1]),'long_silence_seconds':sum(silences)},
    'streams':streams,'verification':manifest['verification'],
    'limitation':'Frame sampling and signal checks do not transcribe or verify exact generated dialogue.'}
r.save(r.ROOT/'exports/whole-movie-refresh-20261021-v06-inspection.json',report)
print('Actual export inspection pages:',pages)
print('Audio:',report['audio'],'Streams:',len(streams),'Size MB:',round(source.stat().st_size/1e6,1))
