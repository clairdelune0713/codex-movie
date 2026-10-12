"""Prepare inspected completed clips while the remaining jobs render."""
import json
from assemble_movie import ROOT,helper,run,decode,metadata
p=helper.read(ROOT/'project.json')
observations=helper.read(ROOT/'exports/take-inspection.json')
for ob in observations:
    ch=next(c for c in p['chapters'] if c['id']==ob['chapter_id'])
    take=next(t for t in ch['takes'] if t['id']==ob['take_id'])
    if take.get('quality_disposition') or take['status']!='succeeded':continue
    if take['dependency_fingerprint']!=helper.chapter_fingerprint(ROOT,p,ch):continue
    source=ROOT/take['path'];target=ROOT/f'exports/normalized/{ch["id"]}-{take["id"]}.mp4'
    if target.exists():continue
    target.parent.mkdir(parents=True,exist_ok=True)
    temporary=target.with_name(target.stem+'.partial.mp4')
    video=f'setpts=PTS-STARTPTS,fps=30,trim=duration={ch["duration"]},setpts=N/(30*TB),setsar=1'
    audio=f'atrim=duration={ch["duration"]},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d=0.02,afade=t=out:st={ch["duration"]-0.03}:d=0.03'
    run(['-hide_banner','-v','error','-y','-i',source,'-map','0:v:0','-map','0:a:0','-vf',video,'-af',audio,'-t',ch['duration'],'-r','30','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',temporary])
    info={**metadata(temporary),**decode(temporary)}
    if info['decoded_frames']!=ch['duration']*30:raise RuntimeError('Normalized frame count mismatch '+ch['id'])
    temporary.replace(target)
    print(json.dumps({'normalized_ready':ch['id'],'take_id':take['id'],'frames':info['decoded_frames']}),flush=True)
