"""Versioned exact-runtime assembly of visually reviewed v02 motion takes."""
import json,hashlib,sys
from datetime import datetime,timezone
from project_ops import ROOT,helper,commit,write_json
from assemble_movie import run,metadata,decode,signal,PROFILE

def select():
 p=helper.read(ROOT/'project.json');review=helper.read(ROOT/'exports/continuity-v02-visual-review.json')
 if len(review['chapters'])!=13:raise RuntimeError('All chapters need actual visual review')
 for ch in p['chapters']:
  ob=next(o for o in review['chapters'] if o['chapter_id']==ch['id'])
  t=next(t for t in ch['takes'] if t['id']==ob['take_id'])
  if ob['decision']!='select' or t['status']!='succeeded' or t['dependency_fingerprint']!=helper.chapter_fingerprint(ROOT,p,ch):raise RuntimeError('Unreviewed/outdated take '+ch['id'])
  t['visual_inspection']=ob;t['verification']=helper.read(ROOT/ob['technical_path']);ch['active_take_id']=t['id']
  ch['screenshots']=ob['frames']
 p['production_status']='assembling_v02';p['continuity_revision']['status']='assembly'
 commit(p,'Select actually reviewed continuity v02 takes and retain prior take choices in history')

def assemble():
 p=helper.read(ROOT/'project.json');normalized=[];inputs=[]
 out=ROOT/'exports/midnight-phantom-v02-150s-720p-21x9.mp4'
 if out.exists():raise RuntimeError('Preserve existing versioned film')
 for ch in p['chapters']:
  t=next(t for t in ch['takes'] if t['id']==ch['active_take_id'])
  if t.get('continuity_revision')!='v02' or t['visual_inspection']['decision']!='select' or t['dependency_fingerprint']!=helper.chapter_fingerprint(ROOT,p,ch):raise RuntimeError('Take selection mismatch')
  source=ROOT/t['path'];target=ROOT/f'exports/normalized-v02/{ch["id"]}-{t["id"]}.mp4';target.parent.mkdir(parents=True,exist_ok=True)
  if not target.exists():
   video=f'setpts=PTS-STARTPTS,fps=30,trim=duration={ch["duration"]},setpts=N/(30*TB),setsar=1'
   audio=f'atrim=duration={ch["duration"]},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d=0.02,afade=t=out:st={ch["duration"]-0.03}:d=0.03'
   run(['-hide_banner','-v','error','-i',source,'-map','0:v:0','-map','0:a:0','-vf',video,'-af',audio,'-t',ch['duration'],'-r','30','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',target])
  normalized.append(target);inputs.append({'chapter':ch['id'],'take_id':t['id'],'path':t['path'],'duration':ch['duration']})
  print(json.dumps({'normalized':ch['id'],'take':t['id']}),flush=True)
 listing=ROOT/'exports/concat-inputs-v02.txt';listing.write_text(''.join("file '"+f.as_posix().replace("'","'\\''")+"'\n" for f in normalized),encoding='utf-8')
 run(['-hide_banner','-v','error','-f','concat','-safe','0','-i',listing,'-map','0:v:0','-map','0:a:0','-vf','setpts=N/(30*TB),setsar=1','-af','atrim=duration=150,asetpts=PTS-STARTPTS,loudnorm=I=-18:TP=-2:LRA=11,aresample=48000','-t','150','-r','30','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',out])
 verification={**metadata(out),**decode(out),**signal(out),'target':PROFILE,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'verified_at':datetime.now(timezone.utc).isoformat(),'visual_review_path':'exports/continuity-v02-visual-review.json'}
 if verification['container_duration']!=150 or verification['decoded_frames']!=4500 or verification['fps']!=30 or (verification['width'],verification['height'])!=(1470,630) or not verification['audio_present']:raise RuntimeError('Final exact media verification failed')
 write_json(ROOT/'exports/video-verification-v02.json',verification)
 write_json(ROOT/'exports/assembly-settings-v02.json',{'profile':PROFILE,'inputs':inputs,'method':'Normal speed hard cuts;30fps native720p21:9 normalization with stereo generated audio. Previous v01 clock overlays excluded.','final_path':out.relative_to(ROOT).as_posix()})
 p=helper.read(ROOT/'project.json');p['production_status']='delivered_v02';p['render_status']='completed';p['continuity_revision']['status']='delivered';p['final_output']={'path':out.relative_to(ROOT).as_posix(),'verification':verification,'continuity_revision':'v02'}
 commit(p,'Deliver separately versioned decoded exact150second continuity v02 movie')
 print(json.dumps({'final':str(out),'duration':150,'frames':4500,'dimensions':[1470,630]}),flush=True)

if __name__=='__main__':
 if sys.argv[1]=='select':select()
 elif sys.argv[1]=='assemble':assemble()
