"""Local contact sheets of unchanged selected masters; never renderer inputs."""
import hashlib,json
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
out=ROOT/'exports/finalized-assets';out.mkdir(parents=True,exist_ok=True)
font=ImageFont.truetype('C:/Windows/Fonts/msyh.ttc',21)
small=ImageFont.truetype('C:/Windows/Fonts/msyh.ttc',17)
lines=['# dog-20261015 finalized masters','',
       'Exact finalized selections from dog-20261014; all 71 selected files and the complete approved visual fingerprint match. These review sheets never enter Seedance payloads.','']
manifest=[]
for category in ['character','environment','prop','reference']:
    items=[a for a in p['asset_list'] if a['category']==category]
    for start in range(0,len(items),8):
        group=items[start:start+8];canvas=Image.new('RGB',(1800,60+((len(group)+1)//2)*365),'#f4f1e9');draw=ImageDraw.Draw(canvas)
        title=category+' | '+str(start+1)+'-'+str(start+len(group))
        draw.text((18,15),'dog-20261015 | unchanged finalized '+title,font=font,fill='#203b3d')
        for i,a in enumerate(group):
            c=next(c for c in a['candidates'] if c['id']==a['selected_candidate_id'])
            img=Image.open(ROOT/c['path']);img.load()
            fitted=ImageOps.contain(img.convert('RGB'),(870,285))
            x=15+(i%2)*890;y=65+(i//2)*365
            canvas.paste(fitted,(x+(870-fitted.width)//2,y))
            draw.text((x,y+290),a['tag'],font=font,fill='#203b3d')
            draw.text((x,y+320),c['id'],font=small,fill='#526264')
            manifest.append({'tag':a['tag'],'candidate_id':c['id'],'path':c['path'],'dimensions':img.size,
                'sha256':hashlib.sha256((ROOT/c['path']).read_bytes()).hexdigest()})
        dest=out/(category+f'-{start//8+1:02}.jpg');canvas.save(dest,quality=92)
        lines.extend(['## '+title,'',f'![{title}](<{dest.as_posix()}> )',''])
        for a in group:
            c=next(c for c in a['candidates'] if c['id']==a['selected_candidate_id'])
            lines.append(f"- {a['tag']} — `{c['id']}` — [original](<{(ROOT/c['path']).as_posix()}>)")
        lines.append('')
(out/'index.md').write_text('\n'.join(lines),encoding='utf-8')
(out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print('All',len(manifest),'selected images decoded; gallery:',out/'index.md')
