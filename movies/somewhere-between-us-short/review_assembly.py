import importlib.util, json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('a',ROOT/'assemble_movie.py');a=importlib.util.module_from_spec(s);s.loader.exec_module(a)
v=json.loads((ROOT/'exports/video-verification.json').read_text(encoding='utf-8'));assert v['passes']
final=ROOT/'exports/somewhere-between-us-new-short-720p-21x9.mp4'
times=[0.4,26,53,102,155,195,237,260,283,309,320,350.5]
out=ROOT/'exports/visual-review/final';out.mkdir(exist_ok=True)
canvas=Image.new('RGB',(1680,1064),'#18202b');draw=ImageDraw.Draw(canvas)
font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',18)
for i,t in enumerate(times):
 dest=out/f'frame-{i+1:02d}.jpg'
 if not dest.exists():a.run(['-v','error','-ss',t,'-i',final,'-frames:v','1','-update','1',dest])
 x=(i%3)*560;y=(i//3)*266
 im=Image.open(dest).convert('RGB').resize((560,240));canvas.paste(im,(x,y+26))
 draw.text((x+6,y+2),f'Final movie {t:.1f}s',font=font,fill='white')
canvas.save(out/'final-sample-review.jpg',quality=94)
print(out/'final-sample-review.jpg')
