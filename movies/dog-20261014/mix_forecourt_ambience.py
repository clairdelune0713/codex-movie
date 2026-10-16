"""Conventional sound edit for the wordless forecourt transition.

Copy its inspected picture stream unchanged. Use the same movie's native live
harbour ambience/horn, before any speech in the current seating-bay take.
No synthetic replacement voices, muted scene, new generation or image edits.
"""
import hashlib,subprocess
from render_movie import ROOT,FF,read,save,helper,inspect_technical,now
p=read(ROOT/'project.json');j=read(ROOT/'exports/task-journal.json')
c=p['chapters'][50];t=j['takes'][c['id']];a=j['takes']['s14_c02']
assert t['id']=='take_02' and a['id']=='take_02' and t['status']==a['status']=='succeeded'
audit=read(ROOT/'exports/dialogue-audit/s14_c02_take_02.json')
assert audit['actual_segments'] and min(s['start'] for s in audit['actual_segments'])>14
video=ROOT/t['path'];audio=ROOT/a['path']
target=ROOT/'chapters/s13_c01/takes/take_02_mix01.mp4'
if target.exists():raise RuntimeError('Retain prior local edit; no overwrite')
result=subprocess.run([str(FF),'-hide_banner','-nostdin','-y','-v','error','-i',str(video),'-i',str(audio),
    '-map','0:v:0','-map','1:a:0','-c:v','copy','-af','atrim=start=0:end=13,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.025,afade=t=out:st=12.975:d=0.025',
    '-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-t','13','-map_metadata','-1','-movflags','+faststart',str(target)],capture_output=True,text=True)
if result.returncode:raise RuntimeError(result.stderr[-1000:])
info=inspect_technical(target,t)
samples=[]
for n,sec in enumerate((0.2,4.33,8.67,12.8),1):
    frame=ROOT/f'chapters/s13_c01/screenshots/take_02_mix01_review_{n:02}.jpg'
    subprocess.run([str(FF),'-v','error','-threads','2','-ss',str(sec),'-i',str(target),'-frames:v','1','-q:v','2','-y',str(frame)],check=True)
    original=ROOT/f'chapters/s13_c01/screenshots/take_02_review_{n:02}.jpg'
    assert hashlib.sha256(frame.read_bytes()).hexdigest()==hashlib.sha256(original.read_bytes()).hexdigest()
    samples.append(frame.relative_to(ROOT).as_posix())
edit={**{k:v for k,v in t.items() if k not in ('prior_takes','visual_review','provider_usage','provider_metadata','attempt_id','task_id')},
    'id':'take_02_mix01','path':target.relative_to(ROOT).as_posix(),'created_at':now(),
    'source_video_take_id':t['id'],'source_video_path':t['path'],'source_video_sha256':hashlib.sha256(video.read_bytes()).hexdigest(),
    'source_audio_path':a['path'],'source_audio_sha256':hashlib.sha256(audio.read_bytes()).hexdigest(),
    'dependency_fingerprint':helper.chapter_fingerprint(ROOT,p,c),'verification':info,
    'local_edit':{'type':'native_ambience_replacement','audio_source_chapter':'s14_c02','audio_source_take':'take_02','audio_interval_seconds':[0,13],
        'reason':'Wordless forecourt transition: remove potential unrequested voice adlib, retain same-project harbour ambience and motivated live ferry horn before any source dialogue (first speech detected at 14.77s).',
        'video':'Original H.264 packets copied unchanged; four decoded JPEG samples hash-identical to inspected current source.',
        'additional_seedance_cost':'0'},
    'visual_review':{'inspected':True,'requires_repair':False,'take_id':'take_02_mix01','reviewed_at':now(),
        'source_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'sample_paths':samples,
        'scope':'Four exact picture samples already visually inspected from take02; independently re-extracted after sound edit and byte-identical. Native ambience from same setting before source speech, no new voices.',
        'notes':'Dogs are separated in first shared wide and no greeting action occurs. Same original cast/geography. No titles/subtitles/credits visible.'}}
save(ROOT/'exports/local-edits/s13_c01_take_02_mix01.json',edit)
print({'edit':edit['path'],'duration':info['duration'],'picture_samples_exactly_unchanged':True,'native_ambience_source_seconds':[0,13],'additional_seedance_charge':0})
