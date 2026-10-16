"""Preserve inspected local video edits as distinct takes, zero extra API calls."""
import hashlib
import subprocess
from render_movie import ROOT,FF,helper,read,save,inspect_technical

p=read(ROOT/'project.json');j=read(ROOT/'exports/task-journal.json')
for n in [47,48,51,54]:
    c=p['chapters'][n-1];t=j['takes'][c['id']];src=ROOT/t['path']
    assert t['id']=='take_02' and t['dependency_fingerprint']==helper.chapter_fingerprint(ROOT,p,c)
    if n==54:
        dest=ROOT/'chapters/chapter_054/takes/edit_01.mp4'
        if not dest.exists():
            temp=dest.with_name('edit_01.encoding.mp4')
            subprocess.run([str(FF),'-v','error','-nostdin','-i',str(src),'-filter_complex',
                '[0:v]trim=start=0:end=8,setpts=PTS-STARTPTS[a];[0:v]trim=start=12:end=16,setpts=2*(PTS-STARTPTS),fps=24[b];[a][b]concat=n=2:v=1:a=0,format=yuv420p[v]',
                '-map','[v]','-map','0:a:0','-c:v','libx264','-preset','fast','-crf','18','-threads','4','-c:a','copy','-t','16',str(temp)],check=True)
            temp.replace(dest)
        inspected=False
        notes='Local hard cut at 8s removes unintended empty-bench dissolve; uses own inspected ferry shot at 12-16s at half speed, preserving native dialogue/ambience and planned 16s.'
    else:
        dest=ROOT/'exports/badge-correction'/f"{c['id']}_{t['id']}_badge.mp4"
        meta=read(dest.with_suffix('.json'))
        assert meta['eligible_frames']==meta['corrected_frames']
        inspected=True
        notes='Four actual corrected frames inspected; original supplied circular GD emblem tracked on bandana in every eligible frame, native audio unchanged. Puppies unchanged in chapter 51.'
    verification=inspect_technical(dest,t);digest=hashlib.sha256(src.read_bytes()).hexdigest()
    edit={'id':'edit_01','chapter_id':c['id'],'status':'succeeded','path':dest.relative_to(ROOT).as_posix(),
        'duration':c['duration'],'resolution':'1080p','aspect_ratio':'16:9',
        'dependency_fingerprint':helper.chapter_fingerprint(ROOT,p,c),'verification':verification,
        'local_edit':True,'new_provider_generation':False,
        'source_video_take_id':t['id'],'source_video_path':t['path'],'source_video_sha256':digest,
        'source_audio_take_id':t['id'],'source_audio_path':t['path'],'source_audio_sha256':digest,
        'visual_review':{'inspected':inspected,'sample_count':4 if inspected else 0,'notes':notes}}
    if n!=54:
        edit['asset_layer']={'asset_id':'asset_039','source_sha256':meta['source_asset_sha256'],'original_unchanged':True,
            'tracking_frames':meta['corrected_frames'],'eligible_frames':meta['eligible_frames'],'metadata':dest.with_suffix('.json').relative_to(ROOT).as_posix()}
    save(ROOT/'exports/local-edits'/f"{c['id']}_edit_01.json",edit)
    print(c['id'],'registered local edit, inspected:',inspected,flush=True)
