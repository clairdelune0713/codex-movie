from pathlib import Path
import json, math
from PIL import Image, ImageOps, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
project=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
out=ROOT/'exports'/'asset-review'; out.mkdir(parents=True,exist_ok=True)
titlefont=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',28)
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',21)
groups=[('supplied-characters','Primary character designs', [a for a in project['asset_list'] if a['source']=='user-supplied'],10),('new-characters','Additional characters and states',[a for a in project['asset_list'] if a['source']!='user-supplied' and a['category']=='character'],10),('environments','Empty locations',[a for a in project['asset_list'] if a['category']=='environment'],8),('props','Main props',[a for a in project['asset_list'] if a['category']=='prop'],8)]
pages=[];md=['# doge-20261020-1 — asset review','', 'Active finale: 5:05, source scenes37-51,480p21:9. Original source files and earlier candidates are retained unchanged. Eight selected human sheets have refined stylized surface rendering. Each sheet represents one character, one location or the stated prop/state. These contact sheets are review files, never video references.','']
manifest=[]
for slug,title,assets,limit in groups:
    for part in range(math.ceil(len(assets)/limit)):
        subset=assets[part*limit:(part+1)*limit]
        cell_w,cell_h=900,580
        rows=math.ceil(len(subset)/2)
        canvas=Image.new('RGB',(1800,rows*cell_h+70),'#e8eceb')
        draw=ImageDraw.Draw(canvas)
        draw.text((24,18),f'{title} | {part+1} of {math.ceil(len(assets)/limit)}',font=titlefont,fill='#163434')
        for idx,a in enumerate(subset):
            selected=next(c for c in a['candidates'] if c['id']==a['selected_candidate_id'])
            path=ROOT/selected['path']
            with Image.open(path) as img:
                im=ImageOps.contain(img.convert('RGB'),(880,490))
            x=(idx%2)*cell_w+(cell_w-im.width)//2;y=70+(idx//2)*cell_h
            canvas.paste(im,(x,y+(490-im.height)//2))
            lx=(idx%2)*cell_w+18
            draw.text((lx,y+497),a['name'],font=titlefont,fill='#172e2e')
            draw.text((lx,y+534),f"{a['tag']}  |  candidate {selected['id']}",font=font,fill='#244f4f')
            entry={'name':a['name'],'tag':a['tag'],'candidate_id':selected['id'],'path':selected['path'],'category':a['category'],'source':a['source']}
            manifest.append(entry)
        page=out/f'{slug}-{part+1:02d}.jpg'
        canvas.save(page,quality=95)
        pages.append(str(page))
        md += [f'## {title} — {part+1}', '', f'![{title}]({page.as_posix()})','']
        for a in subset:
            selected=next(c for c in a['candidates'] if c['id']==a['selected_candidate_id'])
            md.append(f"- {a['name']} — `{a['tag']}` — candidate `{selected['id']}` — [full-size original]({(ROOT/selected['path']).as_posix()})")
        md.append('')
(out/'gallery.md').write_text('\n'.join(md),encoding='utf-8')
(out/'gallery-manifest.json').write_text(json.dumps({'selected_asset_count':len(manifest),'pages':pages,'assets':manifest},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'selected_assets':len(manifest),'pages':pages},indent=2))
