import importlib.util
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('movi_project',r'C:\Users\Admin 3\.codex\skills\movi2\scripts\project.py')
helper=importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
p=helper.read(ROOT/'project.json')
results=helper.read(ROOT/'generation-results.json')
for item in results:
    item['source_file']=item['source_file'].split(' as ')[-1]
(ROOT/'generation-results.json').write_text(helper.encoded(results),encoding='utf-8')
for item in results:
    a=next(a for a in p['asset_list'] if a['id']==item['asset_id'])
    cid=a['id'].replace('asset_','')+'_c01'
    rel=f"assets/{a['id']}/{cid}.png"
    dest=ROOT/rel
    dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists():
        raise RuntimeError('Do not overwrite '+str(dest))
    shutil.copy2(item['source_file'],dest)
    with Image.open(dest) as im:
        im.verify()
    with Image.open(dest) as im:
        dimensions=list(im.size)
    a['candidates'].append({'id':cid,'path':rel,'prompt':item['prompt'],'source_revision':item['source_revision'],'dependency_fingerprint':helper.asset_fingerprint(ROOT,p,a),'created_at':datetime.now(timezone.utc).isoformat(),'dimensions':dimensions,'input_reference_paths':a.get('reference_paths',[]),'generation_tool':'built-in image_gen','requested_style':p['style']['medium'],'inspection_status':'awaiting_visual_inspection'})
    a['selected_candidate_id']=cid
p['production_status']='asset_review_preparation'
(ROOT/'proposal-assets.json').write_text(helper.encoded(p),encoding='utf-8')
(ROOT/'exports').mkdir(exist_ok=True)
font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',26)
small=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',21)
groups={'characters':['character'],'environments':['environment'],'props':['prop']}
for group,categories in groups.items():
    selected=[a for a in p['asset_list'] if a['category'] in categories]
    columns=2 if len(selected)==4 else 1
    cell_w=1000 if columns==1 else 900
    image_h=round(cell_w*2/3)
    cell_h=image_h+76
    rows=(len(selected)+columns-1)//columns
    sheet=Image.new('RGB',(cell_w*columns,cell_h*rows),(248,242,221))
    d=ImageDraw.Draw(sheet)
    for i,a in enumerate(selected):
        c=next(c for c in a['candidates'] if c['id']==a['selected_candidate_id'])
        x=(i%columns)*cell_w;y=(i//columns)*cell_h
        d.text((x+16,y+10),a['name']+' | '+a['tag'],font=font,fill=(28,27,26))
        d.text((x+16,y+43),'Candidate: '+c['id'],font=small,fill=(71,66,56))
        with Image.open(ROOT/c['path']) as im:
            im=im.convert('RGB');im.thumbnail((cell_w-16,image_h-8),Image.Resampling.LANCZOS)
            sheet.paste(im,(x+(cell_w-im.width)//2,y+76+(image_h-im.height)//2))
    sheet.save(ROOT/f'exports/review-{group}.jpg',quality=95)
print(json.dumps({'saved':len(p['asset_list'])-1,'dimensions':{a['tag']:a['candidates'][-1].get('dimensions') for a in p['asset_list'] if a['source']=='generated'}},indent=2))
