"""Assemble inspected scenes 37–51, preserving native animation and audio.

No generation calls. Requires all 15 successful, visually accepted takes.
Latest delivery instructions prohibit all titles, subtitles, captions and text boxes.
"""
import argparse, hashlib, json, re, subprocess, sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parent
FF=ROOT/'tools/ffmpeg.exe'
W,H,FPS=854,480,24
sys.path.insert(0,str(ROOT))
from render_finale import probe, save

def call(args):
    r=subprocess.run([str(FF),'-hide_banner','-loglevel','error','-nostdin',*map(str,args)],capture_output=True,text=True,encoding='utf-8',errors='replace')
    if r.returncode:raise RuntimeError('Local assembly failed: '+r.stderr[-2000:])
    return r

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--prepare-graphics',action='store_true');args=ap.parse_args()
    work=ROOT/'exports/finale-finishing-v02-no-text';work.mkdir(parents=True,exist_ok=True)
    if args.prepare_graphics:
        print('No graphics used: latest user requested no title, subtitles or text boxes.');return
    p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
    selected=[]
    for c in p['chapters'][36:51]:
        t=next((t for t in c['takes'] if t['id']==c.get('active_take_id')),None)
        if not t or t.get('status')!='succeeded' or not t.get('visual_review',{}).get('inspected') or t['visual_review'].get('requires_repair'):
            raise RuntimeError(c['id']+' needs a successful visually accepted selected take before assembly')
        src=ROOT/t['path'];info=probe(src)
        if (info['width'],info['height'])!=(W,H) or not info['audio'] or info['duration']<c['duration']-.04:
            raise RuntimeError('Source format/runtime mismatch: '+c['id'])
        selected.append((c,t,src))
    normalized=[];manifest=[];offset=0
    for c,t,src in selected:
        target=work/(c['id']+'_'+t['id']+'.mp4')
        if target.exists():raise RuntimeError('Preserve existing local edit; use a new finishing directory/version')
        duration=c['duration'];n=c['chapter_index']
        cmd=['-i',src]
        common=f'fps={FPS},trim=duration={duration},setpts=N/({FPS}*TB),setsar=1'
        cmd+=['-vf',common,'-map','0:v:0','-map','0:a:0']
        cmd+=['-af',f'aresample=48000,atrim=duration={duration},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={duration-.012}:d=0.012','-t',str(duration),'-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),'-fps_mode','cfr','-c:a','aac','-b:a','192k','-ac','2','-movflags','+faststart',target]
        call(cmd);normalized.append(target)
        manifest.append({'chapter_id':c['id'],'scene':n,'source_take_id':t['id'],'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'source_path':src.relative_to(ROOT).as_posix(),'start':offset,'end':offset+duration,'duration':duration,'local_edit_path':target.relative_to(ROOT).as_posix()})
        offset+=duration
        print('Finished',c['id'],flush=True)
    concat=work/'concat.txt';concat.write_text('\n'.join("file '"+f.as_posix().replace("'","'\\''")+"'" for f in normalized)+'\n',encoding='utf-8')
    output=ROOT/'exports/doge-20261016-scenes-37-51-480p-16x9.mp4'
    if output.exists():raise RuntimeError('Never overwrite delivered export; choose next version')
    call(['-f','concat','-safe','0','-i',concat,'-vf',f'setpts=N/({FPS}*TB)','-af',f'aresample=48000,atrim=duration={offset},asetpts=PTS-STARTPTS','-t',str(offset),'-r',str(FPS),'-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',output])
    info=probe(output)
    result=call(['-threads','2','-i',output,'-progress','pipe:1','-f','null','-'])
    counts=re.findall(r'^frame=(\d+)',result.stdout,re.M);frames=int(counts[-1]) if counts else None
    if frames!=offset*FPS or abs(info['duration']-offset)>.05:raise RuntimeError('Final frame/runtime verification failed')
    save(ROOT/'exports/finale-assembly-manifest.json',{'scope':'37–51 ONLY','duration_seconds':offset,'resolution_profile':'480p','requested_aspect_ratio':'16:9','created_at':datetime.now(timezone.utc).isoformat(),'path':output.relative_to(ROOT).as_posix(),'chapters':manifest,'verification':{**info,'decoded_frames':frames,'full_decode_verified':True},'finishing':'Original generated animation/audio only; no title, subtitles, captions, text boxes or graphic overlays. Native 854x480 480p widescreen; no time stretching.'})
    print(output);print(json.dumps({**info,'decoded_frames':frames},indent=2))

if __name__=='__main__':main()
