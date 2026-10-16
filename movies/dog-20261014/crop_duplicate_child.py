"""Conventional local reframing: remove duplicate Lok from opening shot only.

Keep source MP4/audio immutable. No AI image editing, extra provider job, new
characters or timing changes. The native shot cut is at frame 137 (5.708333s).
"""
import hashlib,json,subprocess,sys
from render_movie import ROOT,FF,read,save,helper,inspect_technical,now
p=read(ROOT/'project.json');j=read(ROOT/'exports/task-journal.json')
c=next(c for c in p['chapters'] if c['id']=='s09_c01');t=j['takes'][c['id']]
assert t['id']=='take_01' and t['status']=='succeeded'
source=ROOT/t['path'];sha=hashlib.sha256(source.read_bytes()).hexdigest()
full='--crop-all' in sys.argv
edit_id='take_01_crop02' if full else 'take_01_crop01'
target=ROOT/'chapters/s09_c01/takes'/(edit_id+'.mp4')
if target.exists():raise RuntimeError('Preserve existing local edit; inspect it before another version')
graph=('[0:v]split=2[early][late];'
       '[early]trim=end_frame=137,setpts=PTS-STARTPTS,crop=644:362:210:30,scale=854:480:flags=lanczos,setsar=1[close];'
       '[late]trim=start_frame=137,setpts=PTS-STARTPTS,setsar=1[wide];'
       '[close][wide]concat=n=2:v=1:a=0,fps=24[v]')
if full:
    graph='[0:v]crop=594:334:260:20,scale=854:480:flags=lanczos,setsar=1,fps=24[v]'
partial=target.with_name(edit_id+'.encoding.mp4')
result=subprocess.run([str(FF),'-hide_banner','-nostdin','-y','-v','error','-threads','4','-i',str(source),
    '-filter_complex',graph,'-map','[v]','-map','0:a:0','-c:v','libx264','-crf','18','-preset','fast',
    '-threads','4','-c:a','copy','-map_metadata','-1','-movflags','+faststart',str(partial)],capture_output=True,text=True)
if result.returncode:raise RuntimeError(result.stderr[-1000:])
partial.replace(target)
info=inspect_technical(target,t)
edit={**{k:v for k,v in t.items() if k not in ('prior_takes','visual_review','provider_usage','provider_metadata','attempt_id','task_id')},
    'id':edit_id,'path':target.relative_to(ROOT).as_posix(),'created_at':now(),
    'source_video_take_id':t['id'],'source_video_path':t['path'],'source_video_sha256':sha,
    'source_audio_path':t['path'],'source_audio_sha256':sha,
    'dependency_fingerprint':helper.chapter_fingerprint(ROOT,p,c),'verification':info,
    'local_edit':{'type':'conventional_reframe','frames':'all' if full else [0,136],'native_cut_frame':137,
        'crop':[260,20,594,334] if full else [210,30,644,362],'output_dimensions':[854,480],
        'reason':'Original group shot duplicated Lok on mother lap and beside Chan, then repeated two foreground heads. Conventional tighter coverage removes the left-side duplicate across the entire scene, retaining single standing Lok, Chan, Tine and May/photo. No original audio or timing change.' if full else 'Original first group shot duplicated Lok on mother lap and beside Chan. Reframe first shot on single standing Lok, Chan and Tine; resume original wide footage at its actual cut. No original audio or timing change.',
        'audio':'Original AAC packets copied unchanged','additional_seedance_cost':'0'},
    'visual_review':{'inspected':False,'requires_repair':False}}
save(ROOT/'exports/local-edits'/('s09_c01_'+edit_id+'.json'),edit)
frames=ROOT/'chapters/s09_c01/screenshots'
for n,sec in enumerate((0.2,3.0,5.4,6.0,12.0,17.8),1):
    subprocess.run([str(FF),'-v','error','-ss',str(sec),'-i',str(target),'-frames:v','1','-y',str(frames/f'{edit_id}_review_{n:02}.jpg')],check=True)
print({'local_edit':target.relative_to(ROOT).as_posix(),'duration':info['duration'],'native_audio_copied':True,'requires_visual_inspection':True})
