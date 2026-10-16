"""Local edit: keep corrected floor video and the fuller original phone dialogue."""
import hashlib
import json
import re
import subprocess
from render_movie import ROOT,FF,read,save,helper,inspect_technical

p=read(ROOT/'project.json');j=read(ROOT/'exports/task-journal.json');c=p['chapters'][38]
video=j['takes'][c['id']];assert video['id']=='take_03' and video['status']=='succeeded'
assert video['dependency_fingerprint']==helper.chapter_fingerprint(ROOT,p,c)
audio=next(t for t in video['prior_takes'] if t['id']=='take_01')
assert audio['status']=='succeeded'
assert re.findall(r'\{([^{}]+)\}',video['prompt'])==re.findall(r'\{([^{}]+)\}',audio['prompt'])
vp=ROOT/video['path'];ap=ROOT/audio['path'];dest=vp.with_name('edit_01.mp4')
if not dest.exists():
    temp=dest.with_name('edit_01.remuxing.mp4')
    subprocess.run([str(FF),'-v','error','-nostdin','-i',str(vp),'-i',str(ap),'-map','0:v:0','-map','1:a:0','-c','copy','-shortest',str(temp)],check=True)
    temp.replace(dest)
verification=inspect_technical(dest,video)
edit={'id':'edit_01','chapter_id':c['id'],'status':'succeeded','path':dest.relative_to(ROOT).as_posix(),
    'duration':c['duration'],'resolution':'1080p','aspect_ratio':'16:9',
    'dependency_fingerprint':helper.chapter_fingerprint(ROOT,p,c),'verification':verification,
    'local_edit':True,'new_provider_generation':False,
    'source_video_take_id':video['id'],'source_video_path':video['path'],'source_video_sha256':hashlib.sha256(vp.read_bytes()).hexdigest(),
    'source_audio_take_id':audio['id'],'source_audio_path':audio['path'],'source_audio_sha256':hashlib.sha256(ap.read_bytes()).hexdigest(),
    'visual_review':{'inspected':True,'sample_count':4,'notes':'Unchanged native take_03 video stream: Tine lies fully on green floor, owner shoes and attached held lead. No face lip-sync in this floor shot.'},
    'audio_review':{'inspected':True,'method':'Local Cantonese ASR comparison of all three retained takes',
        'evidence':'exports/dialogue-audit/chapter_039_take_01_audio-comparison.json',
        'notes':'Earlier audio contains all three Mei sentences before Ching reply; same original expected lines, copied original audio stream without synthesis. ASR is not a guarantee of every syllable.'}}
save(ROOT/'exports/local-edits/chapter_039_edit_01.json',edit)
print('Saved native corrected floor video with fuller original phone dialogue; zero new Seedance calls.')
