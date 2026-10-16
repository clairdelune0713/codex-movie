"""Replace an unrequested speech interval with original same-flat room ambience.

Preserves the generated video stream and the original take. No provider calls.
"""
import hashlib,subprocess
from render_movie import ROOT,FF,read,save,helper,now,probe

p=read(ROOT/'project.json');j=read(ROOT/'exports/task-journal.json')
c=next(c for c in p['chapters'] if c['id']=='s07_c03')
original=j['takes'][c['id']];ambience=j['takes']['s07_c04']
assert original['status']==ambience['status']=='succeeded'
assert not [b for b in c['planning_source_blocks'] if b['type']=='dialogue']
reviews=read(ROOT/'exports/visual-reviews.json')
assert reviews['s07_c04']['inspected'] and not reviews['s07_c04']['requires_repair']
dest=ROOT/'chapters/s07_c03/takes/take_01_roomtone01.mp4'
assert not dest.exists(),'Preserve immutable local edit'
filters=(
 '[0:a]atrim=start=0:end=2.25,asetpts=PTS-STARTPTS,afade=t=out:st=2.20:d=0.05[a0];'
 '[1:a]atrim=start=0.3:end=2.7,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.05,afade=t=out:st=2.35:d=0.05[a1];'
 '[0:a]atrim=start=4.65:end=5,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.05[a2];'
 '[a0][a1][a2]concat=n=3:v=0:a=1[outa]')
cmd=[str(FF),'-v','error','-nostdin','-i',str(ROOT/original['path']),'-i',str(ROOT/ambience['path']),
 '-filter_complex',filters,'-map','0:v:0','-map','[outa]','-c:v','copy','-c:a','aac','-b:a','192k',
 '-ar','48000','-ac','2','-t','5','-map_metadata','-1','-movflags','+faststart',str(dest)]
subprocess.run(cmd,check=True)
result=subprocess.run([str(FF),'-v','error','-i',str(dest),'-f','null','-'],capture_output=True,text=True)
assert not result.returncode and not result.stderr.strip()
verification=probe(dest);assert (verification['width'],verification['height'])==(1920,1080)
verification.update(decode_verified=True,native_1080p=True)
sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
edit={'id':'take_01_roomtone01','take_number':1,'status':'succeeded','created_at':now(),
 'duration':5,'resolution':'1080p','model':'Local conventional audio edit of original Seedance take; no new API job',
 'path':dest.relative_to(ROOT).as_posix(),'dependency_fingerprint':helper.chapter_fingerprint(ROOT,p,c),
 'source_video_take_id':original['id'],'source_video_path':original['path'],
 'source_video_sha256':sha(ROOT/original['path']),'source_audio_path':ambience['path'],
 'source_audio_sha256':sha(ROOT/ambience['path']),'verification':verification,
 'audio_edit':{'reason':'Wordless source beat contains an ASR-flagged unrequested adlib at 2.48-4.48s. Preserve first 2.25s toy/cushion sounds and final 0.35s; use inspected same-flat native ambience across the middle with 50ms edge fades.',
 'original_asr_interval':[2.48,4.48],'replacement_interval':[2.25,4.65]},
 'visual_review':{'inspected':True,'requires_repair':False,'reviewed_at':now(),
 'scope':'Original four sampled frames inspected; video stream copied unchanged through the exact five-second trim. Full derivative decoding passed. Only the noted audio interval changes.',
 'notes':'Original home tug/cushion images retained, unrequested speech interval replaced with own same-location ambience.'}}
save(ROOT/'exports/local-edits/s07_c03_roomtone01.json',edit)
print('Saved immutable local audio edit:',dest)
