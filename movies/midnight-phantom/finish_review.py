import importlib.util
import html
import shutil
from datetime import datetime,timezone
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('movi_project',r'C:\Users\Admin 3\.codex\skills\movi2\scripts\project.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
p=helper.read(ROOT/'proposal-assets.json')
refinement=helper.read(ROOT/'museum-refinement.json')
a=next(a for a in p['asset_list'] if a['tag']=='@Museum')
relative='assets/asset_museum/museum_c02.png'
dest=ROOT/relative
if not dest.exists():
    shutil.copy2(refinement['source_file'],dest)
with Image.open(dest) as im:
    im.verify()
with Image.open(dest) as im:
    dimensions=list(im.size)
a['candidates'].append({'id':'museum_c02','path':relative,'prompt':refinement['prompt'],'source_revision':1,'dependency_fingerprint':helper.asset_fingerprint(ROOT,p,a),'created_at':datetime.now(timezone.utc).isoformat(),'dimensions':dimensions,'input_reference_paths':['assets/asset_museum/museum_c01.png','assets/asset_guard/guard_c01.png'],'generation_tool':'built-in image_gen','requested_style':p['style']['medium'],'inspection_status':'inspected'})
a['selected_candidate_id']='museum_c02'
p['detailed_script']=p['detailed_script'].replace('Worlds greatest detective!',"World's greatest detective!")
for chapter in p['chapters']:
    for line in chapter['dialogue']:
        line['text']=line['text'].replace('Worlds greatest detective!',"World's greatest detective!")
for a in p['asset_list']:
    if a['source']=='generated':
        for c in a['candidates']:
            c['inspection_status']='inspected'
            c['inspection_notes']='Reviewed selected artwork for subject identity, panel composition, environment emptiness, prop design and story continuity.'
p['production_status']='awaiting_asset_approval'
p['visual_review_notes']=['All eleven generated assets and the supplied reference inspected.','Museum c02 replaces c01 to match guard boot tread and show open empty case.','Supplied reference is identity/style guidance; galleries are review-only, excluded from all video payloads.','Clock inserts must show exact story times in final chapter prompts; reference analog clock face is guidance.','Crow green-eye scrap state is a narrative state of the approved base design.']
(ROOT/'screenplay.md').write_text(p['detailed_script'],encoding='utf-8')
(ROOT/'proposal-reviewed.json').write_text(helper.encoded(p),encoding='utf-8')
font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',26);small=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',21)
for category,group in [('character','characters'),('environment','environments'),('prop','props')]:
    selected=[a for a in p['asset_list'] if a['category']==category]
    columns=2 if len(selected)==4 else 1
    cell_w=1000 if columns==1 else 900;image_h=round(cell_w*9/16);cell_h=image_h+76
    sheet=Image.new('RGB',(cell_w*columns,cell_h*((len(selected)+columns-1)//columns)),(248,242,221));d=ImageDraw.Draw(sheet)
    for i,a in enumerate(selected):
        c=helper.selected_media(a);x=(i%columns)*cell_w;y=(i//columns)*cell_h
        d.text((x+16,y+10),a['name']+' | '+a['tag'],font=font,fill=(28,27,26));d.text((x+16,y+43),'Candidate: '+c['id'],font=small,fill=(71,66,56))
        with Image.open(ROOT/c['path']) as im:
            im=im.convert('RGB');im.thumbnail((cell_w-16,image_h-8),Image.Resampling.LANCZOS);sheet.paste(im,(x+(cell_w-im.width)//2,y+76+(image_h-im.height)//2))
    sheet.save(ROOT/f'exports/review-{group}.jpg',quality=95)
body=['<!doctype html><html lang="en"><meta charset="utf-8"><title>Midnight Phantom Asset Review</title><style>body{font:18px system-ui;background:#f9f1d9;color:#28241e;max-width:1300px;margin:32px auto;padding:24px}img{max-width:100%;height:auto}article{margin-bottom:38px}a{color:#0e4c82}</style><h1>Midnight Phantom: asset review</h1><p>150 seconds planned. These are image references, not rendered video. Final scene prompts and video submissions await approval.</p><p><a href="../screenplay.md">Timed screenplay</a></p>']
for category in ['character','environment','prop','reference']:
    body.append('<h2>'+category.capitalize()+'</h2>')
    for a in p['asset_list']:
        if a['category']!=category:continue
        c=helper.selected_media(a);url='../'+c['path']
        body.append('<article><h3>'+html.escape(a['name']+' | '+a['tag']+' | '+c['id'])+'</h3><a href="'+url+'"><img src="'+url+'" alt="'+html.escape(a['name'])+'"></a><p><a href="'+url+'">Full-size original</a></p></article>')
body.append('</html>')
(ROOT/'exports/asset-review.html').write_text('\n'.join(body),encoding='utf-8')
print('Reviewed proposal and gallery saved.')
