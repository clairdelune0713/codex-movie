"""Register the inspected conventional hand/eye inserts, preserving native audio."""
import hashlib,subprocess
from render_movie import ROOT,FF,read,save,helper,now,probe
p=read(ROOT/'project.json');j=read(ROOT/'exports/task-journal.json')
c=next(c for c in p['chapters'] if c['id']=='s06_c03');t=j['takes'][c['id']]
dest=ROOT/'chapters/s06_c03/takes/take_01_detailcrop03.mp4'
result=subprocess.run([str(FF),'-v','error','-i',str(dest),'-f','null','-'],capture_output=True,text=True)
assert not result.returncode and not result.stderr.strip()
v=probe(dest);assert (v['width'],v['height'],v['fps'])==(1920,1080,24)
v.update(decode_verified=True,native_1080p=True,digital_detail_reframe=True)
digest=hashlib.sha256((ROOT/t['path']).read_bytes()).hexdigest()
edit={'id':'take_01_detailcrop03','take_number':1,'status':'succeeded','created_at':now(),
 'duration':15,'resolution':'1080p','model':'Local conventional detail edit of original Seedance take; no API job',
 'path':dest.relative_to(ROOT).as_posix(),'dependency_fingerprint':helper.chapter_fingerprint(ROOT,p,c),
 'source_video_take_id':t['id'],'source_video_path':t['path'],'source_video_sha256':digest,
 'source_audio_path':t['path'],'source_audio_sha256':digest,'verification':v,
 'video_edit':{'unchanged_frames':[0,321],'hand_insert_frames':[321,336],'eye_insert_frames':[336,360],
 'hand_crop_xywh':[0,450,960,540],'eye_crop_xywh':[720,0,960,540],
 'reason':'Preserve Chan open-hand invitation and dog eye reaction while excluding contradictory late seated-body reveal. Original audio stream copied; brief detail crops digitally enlarged.'},
 'visual_review':{'inspected':True,'requires_repair':False,'reviewed_at':now(),
 'scope':'Original four samples and actual edited hand at13.6s and eyes at14.7s inspected. Full derivative decoded. No claim of word-perfect generated dialogue.',
 'notes':'Close inserts show hand and attentive dog eyes. No dog seat/paws or misplaced shoulder marking visible in edited final inserts.'}}
save(ROOT/'exports/local-edits/s06_c03_detailcrop03.json',edit)
print('Registered inspected conventional detail edit',dest)
