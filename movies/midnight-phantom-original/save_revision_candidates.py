import json
import shutil
import sys
from datetime import datetime,timezone
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from project_ops import ROOT,helper,commit
p=helper.read(ROOT/'project.json')
receipts=helper.read(ROOT/sys.argv[1])
for item in receipts:
    a=next(a for a in p['asset_list'] if a['id']==item['asset_id'])
    if any(c['id']==item['candidate_id'] for c in a['candidates']):raise RuntimeError('Candidate already recorded')
    relative=f'assets/{a["id"]}/{item["candidate_id"]}.png';destination=ROOT/relative;destination.parent.mkdir(parents=True,exist_ok=True)
    if destination.exists():raise RuntimeError('Preserve existing candidate '+relative)
    shutil.copy2(item['source_file'],destination)
    with Image.open(destination) as im:im.verify()
    with Image.open(destination) as im:dimensions=list(im.size)
    c={'id':item['candidate_id'],'path':relative,'prompt':item['prompt'],'source_revision':item['source_revision'],'dependency_fingerprint':item['dependency_fingerprint'],'created_at':datetime.now(timezone.utc).isoformat(),'dimensions':dimensions,'input_reference_paths':item['reference_paths'],'generation_tool':'built-in image_gen','requested_style':p['style']['medium'],'inspection_status':'awaiting_final_visual_check'}
    a['candidates'].append(c);a['selected_candidate_id']=c['id'];a['source']='generated'
result=commit(p,'Retain proposed continuity v02 candidates without overwriting previous assets')
font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',25);small=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',19)
width=1800;cellw=600;imageh=338;cellh=imageh+65
sheet=Image.new('RGB',(width,cellh*((len(receipts)+2)//3)),(248,242,221));draw=ImageDraw.Draw(sheet)
for i,item in enumerate(receipts):
    a=next(a for a in p['asset_list'] if a['id']==item['asset_id']);c=helper.selected_media(a);x=i%3*cellw;y=i//3*cellh
    draw.text((x+12,y+8),a['name']+' | '+a['tag'],font=font,fill=(30,30,30));draw.text((x+12,y+38),c['id'],font=small,fill=(65,65,65))
    with Image.open(ROOT/c['path']) as im:
        im=im.convert('RGB');im.thumbnail((cellw-14,imageh-6),Image.Resampling.LANCZOS);sheet.paste(im,(x+(cellw-im.width)//2,y+65+(imageh-im.height)//2))
gallery=ROOT/'exports'/(Path(sys.argv[1]).stem+'-inspection.jpg');sheet.save(gallery,quality=95)
print(json.dumps({'revision':result['revision'],'saved':len(receipts),'inspection_gallery':str(gallery)}))
