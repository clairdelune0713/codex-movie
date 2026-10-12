"""Assemble reviewed Pip corrections while preserving the original soundtrack."""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime,timezone
import finish_movie as media

ROOT=media.ROOT
FIX=ROOT/'exports'/'pip-fix-20261012'
HELPER=media.HELPER

def normalize(c,t,original):
    target=FIX/'normalized'/f'{c["id"]}-{t["id"]}-30fps.mp4'
    target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():
        return target
    arguments=[media.FFMPEG,'-hide_banner','-v','error','-y','-i',ROOT/t['path']]
    filters='setsar=1,fps=30,trim=duration='+str(c['duration'])+',setpts=N/(30*TB)'
    if c['id']=='chapter_05':
        filters+=',colorbalance=rs=0.035:gs=0.005:bs=-0.035:rm=0.05:gm=0.005:bm=-0.05:rh=0.035:gh=0.003:bh=-0.035,eq=brightness=-0.025:saturation=1.02'
        arguments+=['-map','0:v:0','-vf',filters]
    else:
        arguments+=['-map','0:v:0','-vf',filters]
    arguments+=['-an','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-r','30','-fps_mode','cfr','-t',str(c['duration']),'-movflags','+faststart',target]
    media.run(arguments)
    print(json.dumps({'normalized':c['id'],'take':t['id'],'duration':c['duration']}),flush=True)
    return target

def main():
    p=media.read(ROOT/'project.json')
    baseline=media.read(FIX/'baseline-project.json')
    review=media.read(FIX/'visual-review.json')
    if not review.get('approved_for_assembly'):
        raise RuntimeError('Pip character/count inspection is incomplete.')
    final=FIX/'five-little-friends-golden-star-pip-corrected-v02.mp4'
    if final.exists():
        raise RuntimeError('The versioned final movie already exists; preserve it.')
    technical=media.read(FIX/'technical-review.json')
    inputs=[]
    selected=[]
    for c in p['chapters']:
        old_c=next(x for x in baseline['chapters'] if x['id']==c['id'])
        original=next(t for t in old_c['takes'] if t['id']==old_c['active_take_id'])
        take_id=review['selected_takes'].get(c['id'],original['id'])
        t=next(t for t in c['takes'] if t['id']==take_id)
        if t['status']!='succeeded':
            raise RuntimeError('Selected take is not successful.')
        if c['id'] in p['pip_correction']['affected_chapters']:
            if not technical['takes'][take_id]['full_decode']['passed']:
                raise RuntimeError('Missing technical verification.')
            t['verification']={'technical_report':'exports/pip-fix-20261012/technical-review.json','visual_report':'exports/pip-fix-20261012/visual-review.json','dense_sample_interval':.5,'full_decode_passed':True}
        c['active_take_id']=t['id']
        inputs.append(normalize(c,t,original))
        selected.append(t['id'])
    listing=FIX/'normalized'/'concat.txt'
    listing.write_text('\n'.join("file '"+x.name+"'" for x in inputs)+'\n',encoding='utf-8')
    video=FIX/'visual-track-v02.mp4'
    media.run([media.FFMPEG,'-hide_banner','-v','error','-y','-f','concat','-safe','0','-i',listing,'-an','-vf','setpts=N/(30*TB)','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-r','30','-fps_mode','cfr','-t','120',video])
    original_film=ROOT/baseline['delivery']['path']
    media.run([media.FFMPEG,'-hide_banner','-v','error','-i',video,'-i',original_film,'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','copy','-t','120','-movflags','+faststart',final])
    metadata=media.probe(final)
    v=next(s for s in metadata['streams'] if s['codec_type']=='video')
    audio=next(s for s in metadata['streams'] if s['codec_type']=='audio')
    count=int(v.get('nb_read_frames') or v['nb_frames'])
    if count!=3600 or abs(float(v['duration'])-120)>.001 or v['r_frame_rate']!='30/1':
        raise RuntimeError('Final runtime/fps mismatch.')
    decode=media.full_decode(final)
    def audio_hash(path):
        raw=media.run([media.FFMPEG,'-hide_banner','-v','error','-i',path,'-vn','-acodec','pcm_s16le','-f','s16le','-']).stdout
        return hashlib.sha256(raw).hexdigest(),len(raw)
    old_hash,old_length=audio_hash(original_film)
    new_hash,new_length=audio_hash(final)
    if old_hash!=new_hash:
        raise RuntimeError('Original decoded soundtrack was not preserved exactly.')
    poster=FIX/'movie-preview-v02.jpg'
    media.frame(final,82,poster)
    report={'file':final.relative_to(ROOT).as_posix(),'verified_at':datetime.now(timezone.utc).isoformat(),'duration_seconds':float(metadata['format']['duration']),'video_duration_seconds':float(v['duration']),'frame_count':count,'fps':30,'width':v['width'],'height':v['height'],'audio_channels':audio['channels'],'audio_sample_rate':int(audio['sample_rate']),'full_decode':decode,'size_bytes':final.stat().st_size,'probe':metadata,'selected_take_ids':selected,'original_soundtrack_preserved_exactly':True,'decoded_audio_sha256':new_hash,'decoded_audio_bytes':new_length,'original_movie_preserved':baseline['delivery']['path'],'changed_chapters':p['pip_correction']['affected_chapters'],'chapter_04_visual_replacement_movie_times':[46,58],'chapter_04_full_replacement_reason':'Three-second splice produced cast position and scale jumps. Use the complete reviewed new take.','no_slow_motion_added':True,'no_frame_blending':True,'no_legacy_rainbow_crop':True,'visual_review':'exports/pip-fix-20261012/visual-review.json'}
    media.write(FIX/'final-verification-v02.json',report)
    current=media.read(ROOT/'project.json')
    for c in current['chapters']:
        chosen=next(x for x in p['chapters'] if x['id']==c['id'])
        c['active_take_id']=chosen['active_take_id']
        for t in c['takes']:
            if t['id']==chosen['active_take_id']:
                t.update(next(x for x in chosen['takes'] if x['id']==t['id']))
    current['production_status']='complete'
    current['delivery']={'path':report['file'],'preview_path':poster.relative_to(ROOT).as_posix(),'verification_path':'exports/pip-fix-20261012/final-verification-v02.json','duration':120,'resolution':f"{v['width']}x{v['height']}",'fps':30,'selected_take_ids':selected,'pending_stages':[],'version':2,'original_soundtrack_preserved_exactly':True}
    current['pip_correction']['status']='complete'
    proposal=ROOT/'proposal-pip-corrected-delivery.json'
    media.write(proposal,current)
    media.run([sys.executable,HELPER,'commit',ROOT,'--from',proposal,'--reason','Deliver Pip full-body/count correction, retaining the exact original soundtrack'])
    checked=json.loads(media.run([sys.executable,HELPER,'check',ROOT]).stdout)
    if checked['errors']:
        raise RuntimeError(checked['errors'])
    media.write(FIX/'project-check-v02.json',checked)
    media.run([sys.executable,HELPER,'export',ROOT])
    print(json.dumps({k:report[k] for k in ('file','duration_seconds','frame_count','fps','width','height','original_soundtrack_preserved_exactly','size_bytes')},indent=2),flush=True)

if __name__=='__main__':
    main()
