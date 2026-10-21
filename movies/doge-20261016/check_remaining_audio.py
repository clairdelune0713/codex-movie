"""Measure native dialogue/ambience levels without replacing generated audio."""
import hashlib,re,subprocess
import render_remaining as render

j=render.journal();results={}
for cid,t in j['takes'].items():
    if t['status']!='succeeded':continue
    source=render.ROOT/t['path'];digest=hashlib.sha256(source.read_bytes()).hexdigest()
    target=render.ROOT/'exports/audio-inspection'/f'{cid}_{t["id"]}_{digest[:10]}.json'
    if target.exists():results[cid]=render.read(target);continue
    r=subprocess.run([str(render.FF),'-hide_banner','-nostdin','-i',str(source),'-vn',
        '-af','volumedetect,silencedetect=noise=-55dB:d=1.5','-f','null','-'],capture_output=True,text=True,encoding='utf-8',errors='replace')
    assert r.returncode==0
    mean=re.search(r'mean_volume: ([\-\w.]+) dB',r.stderr)
    peak=re.search(r'max_volume: ([\-\w.]+) dB',r.stderr)
    assert mean and peak and mean[1]!='-inf', 'Silent or invalid audio: '+cid
    silences=[float(x) for x in re.findall(r'silence_duration: ([\d.]+)',r.stderr)]
    result={'chapter_id':cid,'take_id':t['id'],'source_sha256':digest,'checked_at':render.now(),
        'mean_dbfs':float(mean[1]),'peak_dbfs':float(peak[1]),'detected_silence_seconds':sum(silences),
        'method':'Native audio fully decoded; ffmpeg volumedetect and silencedetect threshold -55 dBFS / minimum 1.5 s.',
        'limitation':'Signal-level checks do not independently verify words, voice identity or artistic mixing.'}
    render.save(target,result);results[cid]=result
render.save(render.ROOT/'exports/audio-inspection-scenes-01-36-index.json',results)
for cid,r in results.items():print(cid,r['mean_dbfs'],r['peak_dbfs'],'dBFS; long silence',round(r['detected_silence_seconds'],2),'s')
