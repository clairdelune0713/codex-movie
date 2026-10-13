"""Deterministic video editorial fixes; no generated reference images changed."""
import json
from project_ops import ROOT,write_json
from assemble_movie import run,metadata,decode,signal
records=[]
for n,take,seconds in [(6,'take_03',10),(12,'take_02',8)]:
 source=ROOT/f'chapters/chapter_{n:02d}/takes/{take}.mp4'
 suffix='clock-tail-v2' if n==6 else 'crow-dark'
 target=ROOT/f'exports/normalized-v02/chapter_{n:02d}-{take}-{suffix}.mp4';target.parent.mkdir(parents=True,exist_ok=True)
 if not target.exists():
  vf=f'setpts=PTS-STARTPTS,fps=30,trim=duration={seconds},setpts=N/(30*TB),setsar=1'
  audio=f'atrim=duration={seconds},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d=0.02,afade=t=out:st={seconds-0.03}:d=0.03'
  args=['-hide_banner','-v','error','-i',source]
  if n==6:
   still=ROOT/'exports/continuity-v02-inspection/chapter06-clock-tail-9.60.jpg'
   if not still.exists():raise RuntimeError('Inspected original clock frame required')
   args+=['-loop','1','-framerate','30','-i',still]
   graph=f'[0:v]{vf}[base];[base][1:v]overlay=0:0:enable=\'gte(t,9.6)\':shortest=1,format=yuv420p[v]'
   args+=['-filter_complex',graph,'-map','[v]','-map','0:a:0']
  else:
   mask='gt(r(X,Y),140)*gt(r(X,Y),1.8*g(X,Y))*gt(r(X,Y),2*b(X,Y))'
   color='geq='+':'.join(c+"='if("+mask+",0.1*"+c+'(X,Y),'+c+"(X,Y))'" for c in 'rgb')
   graph=f'[0:v]{vf},split[base][eyes];[eyes]crop=160:170:860:40,format=gbrp,{color}[dark];[base][dark]overlay=860:40,format=yuv420p[v]'
   args+=['-filter_complex',graph,'-map','[v]','-map','0:a:0']
  args+=['-af',audio,'-t',seconds,'-r','30','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',target]
  run(args)
 v={**metadata(target),**decode(target),**signal(target)}
 if v['decoded_frames']!=seconds*30 or (v['width'],v['height'])!=(1470,630):raise RuntimeError('Editorial output mismatch')
 rec={'chapter_id':f'chapter_{n:02d}','source_take_id':take,'normalized_path':target.relative_to(ROOT).as_posix(),'verification':v,'change':'End chapter06 on the existing numberless clock close-up; hold its near-static last frame0.4s instead of the invalid empty-machine wide. Original audio retained; no moving action slowed.' if n==6 else 'Darken only red robot-eye glow within fixed eye-region during banter. Use original take02 so no second diamond appears in robot hand. Preserve body, props, native acting and sound.'}
 records.append(rec);write_json(target.with_suffix('.json'),rec)
 # Diagnostic frame of actual processed video, not an image-generation reference.
 frame=target.with_suffix('.jpg')
 if not frame.exists():run(['-hide_banner','-v','error','-ss','9.88' if n==6 else '1.5','-i',target,'-frames:v','1','-q:v','2',frame])
 print(json.dumps({'editorial_fixed':n,'frames':v['decoded_frames'],'preview':str(frame)}),flush=True)
write_json(ROOT/'exports/continuity-v02-editorial-fixes.json',records)
