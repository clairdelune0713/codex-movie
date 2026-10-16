"""Extract actual assembled movie frames for final visual inspection."""
import hashlib,subprocess
from PIL import Image,ImageDraw,ImageFont,ImageOps
from render_movie import ROOT,FF,read,save
source=ROOT/'exports/dog-20261015-1080p.mp4';assert source.exists()
p=read(ROOT/'project.json');folder=ROOT/'exports/final-review';folder.mkdir(parents=True,exist_ok=True)
times=[5,52,104,173,234,301,371,432,502,561,595]
samples=[]
for i,ts in enumerate(times):
 dest=folder/f'assembled_{i+1:02}_{ts}s.jpg'
 if not dest.exists():
  subprocess.run([str(FF),'-v','error','-ss',str(ts),'-i',str(source),'-frames:v','1','-q:v','2',str(dest)],check=True)
 samples.append({'timestamp':ts,'path':dest.relative_to(ROOT).as_posix()})
font=ImageFont.truetype('C:/Windows/Fonts/msyh.ttc',20);sheets=[]
for offset in range(0,len(samples),6):
 subset=samples[offset:offset+6];canvas=Image.new('RGB',(1480,40+((len(subset)+1)//2)*440),'#f3f0e9');draw=ImageDraw.Draw(canvas)
 draw.text((16,8),'Actual assembled dog-20261015 frames | native1080p source',font=font,fill='#18302c')
 for n,s in enumerate(subset):
  x=16+(n%2)*736;y=48+(n//2)*440
  img=ImageOps.contain(Image.open(ROOT/s['path']).convert('RGB'),(720,405));canvas.paste(img,(x,y))
  draw.text((x,y+407),str(s['timestamp'])+'s',font=font,fill='#18302c')
 dest=folder/f'assembled_sheet_{offset//6+1:02}.jpg';canvas.save(dest,quality=95);sheets.append(dest.relative_to(ROOT).as_posix())
save(folder/'inspection-pending.json',{'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'revision':p['revision'],'samples':samples,'sheets':sheets,'inspected':False,
 'scope':'Actual final assembly samples. Technical full decode is recorded separately.'})
print('\n'.join(sheets))
