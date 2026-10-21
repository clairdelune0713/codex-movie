from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
import json
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
jobs=json.loads((ROOT/'toon-revision-jobs.json').read_text(encoding='utf-8'))
assets={a['id']:a for a in p['asset_list']}
out=ROOT/'exports'/'asset-review'
f=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',26)
small=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',22)
for page in range(2):
    canvas=Image.new('RGB',(1800,1240),'#e8eceb');d=ImageDraw.Draw(canvas)
    d.text((22,18),f'Refined animated human references | {page+1} of2',font=f,fill='#163434')
    for i,j in enumerate(jobs[page*4:page*4+4]):
        a=assets[j['id']];c=next(c for c in a['candidates'] if c['id']==a['selected_candidate_id'])
        im=Image.open(ROOT/c['path']).convert('RGB');im=ImageOps.contain(im,(880,490))
        x=(i%2)*900+(900-im.width)//2;y=70+(i//2)*580
        canvas.paste(im,(x,y+(490-im.height)//2))
        d.text(((i%2)*900+18,y+497),a['name'],font=f,fill='#172e2e')
        d.text(((i%2)*900+18,y+536),f"{a['tag']} | candidate {c['id']}",font=small,fill='#244f4f')
    canvas.save(out/f'refined-humans-{page+1:02d}.jpg',quality=95)
print('Saved two revised-human review sheets,8 selected candidates.')
