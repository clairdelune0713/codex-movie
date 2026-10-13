"""Actual footage sampling and technical verification, never a generation input."""
import json,sys
from PIL import Image,ImageDraw,ImageFont,ImageOps
from project_ops import ROOT,helper,write_json
from assemble_movie import run,metadata,decode,signal
p=helper.read(ROOT/'project.json');observations=[]
folder=ROOT/'exports/continuity-v02-inspection';folder.mkdir(parents=True,exist_ok=True)
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',20)
for ch in p['chapters']:
 t=next((t for t in reversed(ch['takes']) if t.get('continuity_revision')=='v02' and t['status']=='succeeded' and not t.get('quality_disposition') and t['dependency_fingerprint']==helper.chapter_fingerprint(ROOT,p,ch)),None)
 if not t:continue
 path=ROOT/t['path'];vp=folder/f'{ch["id"]}-{t["id"]}-technical.json'
 if vp.exists():v=helper.read(vp)
 else:
  v={**metadata(path),**decode(path),**signal(path)}
  if (v['width'],v['height'])!=(1470,630) or not v['audio_present'] or abs(v['container_duration']-ch['duration'])>0.3:raise RuntimeError('Technical take mismatch '+ch['id'])
  write_json(vp,v)
 times=[round(i+0.5,2) for i in range(int(ch['duration']))]
 times += [ch['duration']-0.12]
 dest=folder/f'{ch["id"]}-{t["id"]}';dest.mkdir(parents=True,exist_ok=True)
 frames=[]
 for stamp in times:
  frame=dest/f'{stamp:05.2f}.jpg'
  if not frame.exists():run(['-hide_banner','-v','error','-ss',stamp,'-i',path,'-frames:v','1','-q:v','2',frame])
  frames.append({'time':stamp,'movie_time':ch['movie_start']+stamp,'path':frame.relative_to(ROOT).as_posix()})
 cw=490;rh=238;cols=3;rows=(len(frames)+2)//3
 sheet=Image.new('RGB',(cw*cols,rh*rows+40),'#f8f0da');draw=ImageDraw.Draw(sheet)
 draw.text((10,8),ch['id']+' | '+ch['title']+' | '+t['id'],font=font,fill='#202025')
 for i,f in enumerate(frames):
  x=i%cols*cw;y=i//cols*rh+40
  with Image.open(ROOT/f['path']) as im:sheet.paste(ImageOps.contain(im.convert('RGB'),(480,206)),(x+5,y+2))
  draw.text((x+8,y+211),f'clip {f["time"]:.2f}s | movie {f["movie_time"]:.2f}s',font=font,fill='#34343d')
 gallery=folder/f'{ch["id"]}-{t["id"]}-gallery.jpg';sheet.save(gallery,quality=94)
 observations.append({'chapter_id':ch['id'],'take_id':t['id'],'path':t['path'],'fingerprint':t['dependency_fingerprint'],'technical':v,'frames':frames,'gallery':gallery.relative_to(ROOT).as_posix(),'visual_review':'pending'})
 print(json.dumps({'chapter':ch['id'],'take':t['id'],'decode':'passed','duration':v['container_duration'],'gallery':str(gallery)}),flush=True)
write_json(ROOT/'exports/continuity-v02-take-inspection.json',observations)
print(json.dumps({'ready_for_visual_review':len(observations)}),flush=True)
