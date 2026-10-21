"""Keep the approved first 36 scenes and join 15 inspected fresh finale takes."""
import argparse, hashlib, json, re
import render_finale_refresh as r
from assemble_finale import call


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def count(path):
    result=call(['-i',path,'-map','0:v:0','-c:v','copy','-progress','pipe:1','-f','null','-'])
    return int(re.findall(r'^frame=(\d+)',result.stdout,re.M)[-1])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--prepare-only',action='store_true')
    args=ap.parse_args()
    p=r.read(r.ROOT/'project.json')
    baseline=r.read(r.ROOT/p['finale_refresh_authorization']['baseline_path'])
    previous=r.read(r.ROOT/'exports/whole-movie-assembly-manifest.json')
    prior_report=r.read(r.ROOT/'exports/whole-movie-inspection.json')
    assert sha(r.ROOT/previous['path'])==prior_report['source_sha256']
    normalized=[]; sources=[]; chapters=[]; offset=0
    work=r.ROOT/'exports/whole-movie-finishing-refresh-20261021'
    work.mkdir(exist_ok=True)
    output=r.ROOT/'exports/doge-20261016-whole-movie-01-51-480p-16x9-v06.mp4'
    manifest_path=r.ROOT/'exports/whole-movie-refresh-20261021-v06-manifest.json'
    reviewed=r.read(r.ROOT/'exports/visual-reviews.json')
    latest=r.journal()['takes']
    for c in p['chapters']:
        r.assert_script_locked(p,c)
        n=c['chapter_index']; duration=c['duration']
        if args.prepare_only and n>=37:
            t=latest.get(c['id'],{})
            review=reviewed.get(c['id'],{})
            if (t.get('status')!='succeeded' or review.get('take_id')!=t.get('id') or
                    not review.get('inspected') or review.get('requires_repair')):continue
            t={**t,'visual_review':review}
        else:
            t=next(t for t in c['takes'] if t['id']==c['active_take_id'])
        assert t['status']=='succeeded'
        assert t['visual_review']['inspected'] and not t['visual_review']['requires_repair']
        assert t['dependency_fingerprint']==r.helper.chapter_fingerprint(r.ROOT,p,c)
        src=r.ROOT/t['path']; digest=sha(src)
        if n<=36:
            chapter_digest=hashlib.sha256(json.dumps(c,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
            assert chapter_digest==baseline['preserved_first36'][c['id']], ('Approved first 36 changed',c['id'])
            old=previous['chapters'][n-1]
            assert old['take_id']==t['id'] and old['source_sha256']==digest
            spec=previous['normalized_inputs'][n-1]
            assert spec['source_path']==t['path'] and spec['source_sha256']==digest
            target=r.ROOT/spec['path']
            spec={**spec,'preserved_from_manifest':'exports/whole-movie-assembly-manifest.json',
                  'normalized_sha256':sha(target)}
        else:
            current=r.journal()['takes'][c['id']]
            assert current['id']==t['id'] and current['path']==t['path']
            assert current['refresh_authorization_id']==p['finale_refresh_authorization']['id']
            assert t['id']!=baseline['prior_selected_finale'][c['id']]['take_id']
            assert t['visual_review']['source_sha256']==digest
            audio_src=src
            if n==41:
                # Both were generated in this revision with identical shot timing.
                # Keep the clearer native scripted dialogue from the first refresh
                # while using the replacement's clearer leash-catch animation.
                audio_take=next(x for x in c['takes'] if x['id']=='take_03')
                assert audio_take['status']=='succeeded'
                assert audio_take['refresh_authorization_id']==p['finale_refresh_authorization']['id']
                assert audio_take['prompt']==t['prompt']
                audio_src=r.ROOT/audio_take['path']
            grade=r.read(r.ROOT/'exports/evening-grade-review-20261021/grade-v02.json')['filter'] if n in (47,48) else None
            suffix='_evening' if grade else ''
            video=work/f'{c["id"]}_{t["id"]}_{digest[:10]}{suffix}_video.mp4'
            target=work/f'{c["id"]}_{t["id"]}_{digest[:10]}{suffix}_finished.mp4'
            if not video.exists():
                # Encode only the existing planned frames, without a duration-stop
                # interacting with audio or dropping the last video frame.
                vf=f'fps=24,trim=end_frame={duration*24},setpts=N/(24*TB),setsar=1'
                if grade:vf+=','+grade
                if n==51:
                    # The screenplay ends on a hard cut to black. The generated
                    # stinger kept its picture to the end, so finish the last two
                    # planned frames locally without adding runtime.
                    vf+=f",drawbox=x=0:y=0:w=iw:h=ih:color=black:t=fill:enable='gte(n,{duration*24-2})'"
                call(['-i',src,'-map','0:v:0','-an','-vf',
                      vf,
                      '-frames:v',duration*24,'-r','24','-fps_mode','cfr',
                      '-c:v','libx264','-preset','medium','-crf','18',
                      '-pix_fmt','yuv420p','-movflags','+faststart',video])
            assert count(video)==duration*24
            if not target.exists():
                call(['-i',video,'-i',audio_src,'-map','0:v:0','-map','1:a:0',
                      '-c:v','copy','-af',
                      f'aresample=48000,atrim=duration={duration},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={duration-.012}:d=0.012',
                      '-c:a','aac','-b:a','192k','-ar','48000','-ac','2',
                      '-movflags','+faststart',target])
            spec={'source_path':t['path'],'source_sha256':digest,
                  'path':target.relative_to(r.ROOT).as_posix(),'normalized_sha256':sha(target),
                  'duration':duration,'video_stream_source_path':video.relative_to(r.ROOT).as_posix(),
                  'video_stream_source_sha256':sha(video),
                  'operation':'Retain planned native 24fps frames at normal speed; copy exact video stream while resampling native audio to 48kHz and applying 12ms edge fades. No padding or time stretching.'}
            if audio_src!=src:
                spec.update(audio_source_path=audio_src.relative_to(r.ROOT).as_posix(),
                            audio_source_sha256=sha(audio_src),
                            audio_reason='Clearer native scripted dialogue and matching shot-timed score/foley from the other new scene-41 refresh take, with unchanged screenplay and timing.')
            if grade:spec['evening_grade']={'filter':grade,'reason':'Match evening continuity after harbour light show while retaining readable faces, unchanged animation, framing, timing and dialogue.'}
            if n==51:spec['operation']+=' Screenplay hard cut to black on the final two existing frames.'
            r.save(target.with_suffix('.json'),spec)
        assert count(target)==duration*24,(c['id'],count(target),duration*24)
        info=r.probe(target)
        assert (info['width'],info['height'],info['fps'])==(854,480,24)
        assert info['audio']['sample_rate']==48000
        assert abs(info['duration']-duration)<.05
        normalized.append((target,duration));sources.append(spec)
        chapters.append({'chapter_id':c['id'],'scene':n,'take_id':t['id'],
                         'source_path':t['path'],'source_sha256':digest,
                         'start':offset,'end':offset+duration,'duration':duration,
                         'finishing_source_path':spec['path'],
                         'unchanged_approved_scene':n<=36,'fresh_generation':n>=37})
        offset+=duration
        print('Prepared',c['id'],t['id'],duration,'seconds',flush=True)
    if args.prepare_only:
        print('Available reviewed sources prepared; no full export written.');return
    assert offset==1045 and len(chapters)==51
    assert not output.exists(), 'Preserve existing output; use a new export version'
    concat=work/'concat-v06.txt'
    concat.write_text('\n'.join("file '"+f.as_posix().replace("'","'\\''")+"'\nduration "+str(d) for f,d in normalized)+'\n',encoding='utf-8')
    partial=work/'whole-movie-v06.partial.mp4'
    assert not partial.exists(), 'Inspect and retain interrupted output before restarting'
    call(['-f','concat','-safe','0','-i',concat,'-map','0:v:0','-map','0:a:0',
          '-c:v','copy','-af','aresample=48000,atrim=duration=1045,asetpts=PTS-STARTPTS',
          '-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',partial])
    info=r.probe(partial)
    decoded=call(['-threads','2','-i',partial,'-progress','pipe:1','-f','null','-'])
    assert not decoded.stderr.strip(),decoded.stderr
    frames=int(re.findall(r'^frame=(\d+)',decoded.stdout,re.M)[-1])
    assert frames==25080 and abs(info['duration']-1045)<.05
    assert (info['width'],info['height'],info['fps'])==(854,480,24)
    partial.rename(output)
    r.save(manifest_path,{'path':output.relative_to(r.ROOT).as_posix(),
           'created_at':r.now(),'source_revision':p['revision'],
           'scope':'Scenes 1-51; approved scenes 1-36 retained, fresh scenes 37-51',
           'duration_seconds':1045,'chapters':chapters,'normalized_inputs':sources,
           'verification':{**info,'decoded_frames':frames,'full_decode_verified':True},
           'source_sha256':sha(output),'prior_delivery_path':previous['path'],
           'finishing':'Approved first-36 finished streams retained. Refreshed finale uses unchanged screenplay, timing and references with fresh generation seeds. Exact-frame stream join, native audio, no time stretching, frozen padding, titles, subtitles or text boxes.'})
    print('WHOLE MOVIE',output,info,'decoded frames',frames,flush=True)


if __name__=='__main__':
    main()
