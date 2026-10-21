"""Assemble approved new 1–36 takes and preserve the delivered 37–51 finale."""
import argparse,hashlib,json,re,subprocess,sys
from pathlib import Path
import render_remaining as r
import assemble_finale as legacy

W,H,FPS=854,480,24

def call(args):return legacy.call(args)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--fit-finale',choices=['preserve','crop'],default='preserve');ap.add_argument('--prepare-only',action='store_true');args=ap.parse_args()
    p=r.read(r.ROOT/'project.json');work=r.ROOT/'exports/whole-movie-finishing-v01';work.mkdir(exist_ok=True)
    out=r.ROOT/'exports/doge-20261016-whole-movie-01-51-480p-16x9-v03.mp4'
    if out.exists():raise RuntimeError('Never overwrite a prior export; choose a new export version.')
    score_manifest=r.read(r.ROOT/'exports/original-local-score-v01/manifest.json')
    sources=[];chapter_map=[];offset=0
    for c in p['chapters'][:36]:
        t=next((t for t in c['takes'] if t['id']==c.get('active_take_id')),None)
        if not t or t['status']!='succeeded' or not t.get('visual_review',{}).get('inspected') or t['visual_review'].get('requires_repair'):
            if args.prepare_only:continue
            raise RuntimeError(c['id']+' needs an inspected successful current take')
        assert t['dependency_fingerprint']==r.helper.chapter_fingerprint(r.ROOT,p,c)
        src=r.ROOT/t['path'];info=r.probe(src)
        assert t.get('aspect_ratio')=='16:9' and (info['width'],info['height'])==(W,H)
        assert info['audio'] and info['duration']>=c['duration']-.04
        cue=dict(score_manifest[c['id']]) if c.get('audio_finishing') else None
        if cue:cue['mute_native_audio']=c['id'] in p.get('assembly_profile',{}).get('audio_overrides',{})
        sources.append((c['id'],src,c['duration'],'preserve',cue))
        chapter_map.append({'chapter_id':c['id'],'scene':c['chapter_index'],'take_id':t['id'],'source_path':t['path'],'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'start':offset,'end':offset+c['duration'],'duration':c['duration']})
        offset+=c['duration']
    if not args.prepare_only:assert offset==740
    old=r.read(r.ROOT/'exports/finale-assembly-manifest.json');finale=r.ROOT/old['path']
    assert old['duration_seconds']==305 and old['verification']['decoded_frames']==7320
    old_inspect=r.read(r.ROOT/'exports/final-export-inspection.json')
    assert old_inspect['source_sha256']==hashlib.sha256(finale.read_bytes()).hexdigest()
    assert old_inspect.get('visual_review',{}).get('inspected')
    for record,c in zip(old['chapters'],p['chapters'][36:]):
        assert record['source_take_id']==c['active_take_id']
        t=next(t for t in c['takes'] if t['id']==c['active_take_id'])
        assert t['dependency_fingerprint']==r.helper.chapter_fingerprint(r.ROOT,p,c)
        assert record['source_sha256']==hashlib.sha256((r.ROOT/t['path']).read_bytes()).hexdigest()
        chapter_map.append({'chapter_id':c['id'],'scene':c['chapter_index'],'take_id':t['id'],'source_path':t['path'],'source_sha256':record['source_sha256'],'start':740+record['start'],'end':740+record['end'],'duration':c['duration'],'finishing_source_path':old['path']})
    sources.append(('finale_37_51',finale,305,args.fit_finale,None));offset+=305
    if not args.prepare_only:assert len(chapter_map)==51 and offset==1045
    normalized=[];sources_meta=[]
    for name,src,duration,fit,cue in sources:
        reset_origin=name in ('chapter_13','finale_37_51')
        sha=hashlib.sha256(src.read_bytes()).hexdigest();target=work/(name+'_'+sha[:10]+'_'+fit+('_score'+cue['sha256'][:8] if cue else '')+('_exactframes' if reset_origin else '')+'.mp4');sidecar=target.with_suffix('.json')
        filters=(f'scale={W}:{H}:force_original_aspect_ratio=decrease:force_divisible_by=2,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:black' if fit=='preserve' else f'scale={W}:{H}:force_original_aspect_ratio=increase:force_divisible_by=2,crop={W}:{H}')
        vf=filters+f',fps={FPS},trim=duration={duration},setpts=N/({FPS}*TB),setsar=1'
        if reset_origin:vf=f'setpts=PTS-STARTPTS,'+filters+f',fps={FPS}:start_time=0,trim=end_frame={duration*FPS},setpts=N/({FPS}*TB),setsar=1'
        spec={'source_sha256':sha,'duration':duration,'vf':vf,'source_path':src.relative_to(r.ROOT).as_posix(),'path':target.relative_to(r.ROOT).as_posix()}
        if reset_origin:spec['video_frame_limit']=duration*FPS
        if cue:
            score=r.ROOT/cue['path'];assert cue['sha256']==hashlib.sha256(score.read_bytes()).hexdigest()
            spec['original_score']={k:cue[k] for k in ('path','sha256','provenance')}
            spec['mute_native_audio']=cue['mute_native_audio']
        if target.exists():
            if not sidecar.exists() or r.read(sidecar)!=spec:raise RuntimeError('Existing finishing artifact needs reconciliation: '+target.name)
        else:
            audio_finish=f'aresample=48000,atrim=duration={duration},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={duration-.012}:d=0.012'
            command=['-i',src]
            if cue:
                voice_gain='volume=0,' if cue['mute_native_audio'] else ''
                command+=['-i',score,'-filter_complex',f'[0:a]{voice_gain}aresample=48000,asplit=2[voice][key];[1:a][key]sidechaincompress=threshold=0.025:ratio=5:attack=10:release=250[ducked];[voice][ducked]amix=inputs=2:duration=first:normalize=0,{audio_finish}[mixed]','-map','0:v:0','-map','[mixed]']
            else:command+=['-map','0:v:0','-map','0:a:0','-af',audio_finish]
            limit=['-frames:v',str(duration*FPS)] if reset_origin else ['-t',str(duration)]
            command+=['-vf',vf,*limit,'-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),'-fps_mode','cfr','-c:a','aac','-b:a','192k','-ac','2','-movflags','+faststart',target]
            call(command)
            r.save(sidecar,spec)
        normalized.append(target);sources_meta.append(spec);print('Prepared',name,flush=True)
    if args.prepare_only:
        print('Prepared reviewed sources only; no full movie export claimed.',flush=True);return
    concat=work/'concat.txt';concat.write_text('\n'.join("file '"+f.as_posix().replace("'","'\\''")+"'" for f in normalized)+'\n',encoding='utf-8')
    call(['-f','concat','-safe','0','-i',concat,'-vf','setpts=N/(24*TB)','-af','aresample=48000,atrim=duration=1045,asetpts=PTS-STARTPTS','-frames:v','25080','-r','24','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',out])
    info=r.probe(out);decoded=call(['-threads','2','-i',out,'-progress','pipe:1','-f','null','-'])
    counts=re.findall(r'^frame=(\d+)',decoded.stdout,re.M);frames=int(counts[-1])
    assert frames==25080 and abs(info['duration']-1045)<.05 and (info['width'],info['height'])==(W,H)
    r.save(r.ROOT/'exports/whole-movie-assembly-manifest.json',{'path':out.relative_to(r.ROOT).as_posix(),'created_at':r.now(),'source_revision':p['revision'],'scope':'Scenes 1–51 in original order','duration_seconds':1045,'chapters':chapter_map,'normalized_inputs':sources_meta,'existing_finale_fit':args.fit_finale,'verification':{**info,'decoded_frames':frames,'full_decode_verified':True},'finishing':'All scenes generated at native 480p 16:9, matching 854x480 delivery canvas. Native animation and dialogue/foley preserved; original locally synthesized score cues ducked beneath voices where generated music was omitted. Constant 24fps without time stretching. No titles, subtitles or text boxes.'})
    print('WHOLE MOVIE',out);print(json.dumps({**info,'frames':frames},indent=2))

if __name__=='__main__':main()
