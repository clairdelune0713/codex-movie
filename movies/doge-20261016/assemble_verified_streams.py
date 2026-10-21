"""Join inspected exact-frame streams without a final video re-encode."""
import hashlib,re,subprocess
import render_remaining as r
from assemble_finale import call

def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def count(f):
    result=call(['-i',f,'-map','0:v:0','-c:v','copy','-progress','pipe:1','-f','null','-'])
    return int(re.findall(r'^frame=(\d+)',result.stdout,re.M)[-1])

def main():
    p=r.read(r.ROOT/'project.json');work=r.ROOT/'exports/whole-movie-finishing-v02';work.mkdir(exist_ok=True)
    out=r.ROOT/'exports/doge-20261016-whole-movie-01-51-480p-16x9-v04.mp4'
    assert not out.exists()
    cues=r.read(r.ROOT/'exports/original-local-score-v01/manifest.json')
    normalized=[];sources=[];chapters=[];offset=0
    for c in p['chapters'][:36]:
        t=next(t for t in c['takes'] if t['id']==c['active_take_id'])
        assert t['status']=='succeeded' and t['visual_review']['inspected'] and not t['visual_review']['requires_repair']
        assert t['dependency_fingerprint']==r.helper.chapter_fingerprint(r.ROOT,p,c)
        src=r.ROOT/t['path'];digest=sha(src)
        if c['chapter_index']==13:
            # This inspected local crop already contains the same 24fps images;
            # its exact-frame encode has 504 packets and a verified 21s clock.
            video=r.ROOT/'exports/local-edits/chapter_13_framecount_check_v02.mp4'
            assert count(video)==504 and r.probe(video)['duration']==21
            cue=r.ROOT/cues[c['id']]['path'];assert sha(cue)==cues[c['id']]['sha256']
            target=work/'chapter_13_exact_stream.mp4'
            if not target.exists():
                call(['-i',video,'-i',src,'-i',cue,'-filter_complex','[1:a]aresample=48000,asplit=2[voice][key];[2:a][key]sidechaincompress=threshold=0.025:ratio=5:attack=10:release=250[ducked];[voice][ducked]amix=inputs=2:duration=first:normalize=0,aresample=48000,atrim=duration=21,asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st=20.988:d=0.012[mixed]','-map','0:v:0','-map','[mixed]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',target])
            spec={'source_path':t['path'],'source_sha256':digest,'path':target.relative_to(r.ROOT).as_posix(),'duration':21,'video_stream_source_path':video.relative_to(r.ROOT).as_posix(),'video_stream_source_sha256':sha(video),'original_score':cues[c['id']],'operation':'Copy verified 504-frame local-crop video stream; mix original cue beneath native source dialogue/foley. No duration stop or video re-encoding.'}
            r.save(target.with_suffix('.json'),spec)
        else:
            candidates=list((r.ROOT/'exports/whole-movie-finishing-v01').glob(c['id']+'_'+digest[:10]+'_preserve*.json'))
            assert len(candidates)==1,(c['id'],candidates)
            spec=r.read(candidates[0]);target=r.ROOT/spec['path']
            assert spec['source_sha256']==digest and spec['duration']==c['duration']
        frames=count(target);assert frames==c['duration']*24,(c['id'],frames)
        normalized.append((target,c['duration']));sources.append(spec)
        chapters.append({'chapter_id':c['id'],'scene':c['chapter_index'],'take_id':t['id'],'source_path':t['path'],'source_sha256':digest,'start':offset,'end':offset+c['duration'],'duration':c['duration']})
        offset+=c['duration']
    assert offset==740
    old=r.read(r.ROOT/'exports/finale-assembly-manifest.json');finale=r.ROOT/old['path']
    assert sha(finale)==r.read(r.ROOT/'exports/final-export-inspection.json')['source_sha256']
    target=work/'finale_37_51_exact_stream.mp4'
    if not target.exists():
        call(['-i',finale,'-map','0:v:0','-map','0:a:0','-c:v','copy','-af','aresample=48000,atrim=duration=305,asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st=304.988:d=0.012','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',target])
    assert count(target)==7320
    normalized.append((target,305));sources.append({'source_path':old['path'],'source_sha256':sha(finale),'path':target.relative_to(r.ROOT).as_posix(),'duration':305,'operation':'Copy original delivered 7320-frame video stream; normalize only audio.'})
    for record,c in zip(old['chapters'],p['chapters'][36:]):
        t=next(t for t in c['takes'] if t['id']==c['active_take_id'])
        assert record['source_take_id']==t['id'] and record['source_sha256']==sha(r.ROOT/t['path'])
        assert t['dependency_fingerprint']==r.helper.chapter_fingerprint(r.ROOT,p,c)
        chapters.append({'chapter_id':c['id'],'scene':c['chapter_index'],'take_id':t['id'],'source_path':t['path'],'source_sha256':record['source_sha256'],'start':740+record['start'],'end':740+record['end'],'duration':c['duration'],'finishing_source_path':old['path']})
    concat=work/'concat.txt'
    concat.write_text('\n'.join("file '"+f.as_posix().replace("'","'\\''")+"'\nduration "+str(d) for f,d in normalized)+'\n',encoding='utf-8')
    call(['-f','concat','-safe','0','-i',concat,'-map','0:v:0','-map','0:a:0','-c:v','copy','-af','aresample=48000,atrim=duration=1045,asetpts=PTS-STARTPTS','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',out])
    info=r.probe(out);decoded=call(['-threads','2','-i',out,'-progress','pipe:1','-f','null','-'])
    frames=int(re.findall(r'^frame=(\d+)',decoded.stdout,re.M)[-1])
    assert frames==25080 and abs(info['duration']-1045)<.05 and (info['width'],info['height'])==(854,480),(frames,info)
    r.save(r.ROOT/'exports/whole-movie-assembly-manifest.json',{'path':out.relative_to(r.ROOT).as_posix(),'created_at':r.now(),'source_revision':p['revision'],'scope':'Scenes 1–51 in original order','duration_seconds':1045,'chapters':chapters,'normalized_inputs':sources,'verification':{**info,'decoded_frames':frames,'full_decode_verified':True},'finishing':'All selected sources native 480p 16:9. Reviewed normal-speed animation and native dialogue/foley; original local score ducked beneath voices where generation omitted music. Unscripted scene-10 pilot chatter muted. Scene-13 framing repair retained. Exact-frame video-stream join with explicit scene durations, no video time stretching or frozen padding. No titles, subtitles or text boxes.'})
    print('WHOLE MOVIE',out,info,'decoded frames',frames,flush=True)

if __name__=='__main__':main()
