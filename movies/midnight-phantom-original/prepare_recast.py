"""Prepare the user-authorized original-cast revision for visual review."""
import copy
import html
import importlib.util
import json
import shutil
from datetime import datetime,timezone
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent
OLD=ROOT.parent/'midnight-phantom'
HELPER=Path(r'C:\Users\Admin 3\.codex\skills\movi2\scripts\project.py')
spec=importlib.util.spec_from_file_location('movi_project',HELPER);helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
initial=helper.read(ROOT/'project.json');old=helper.read(OLD/'project.json');p=copy.deepcopy(old)
for key in ('id','revision','created_at','updated_at','project_name'):p[key]=initial[key]
for key in ('asset_review','final_output','last_change'):p.pop(key,None)
p['style']['medium']='Original hand-drawn 2D 1930s rubber-hose detective cartoon; bold black ink contours, expressive pie-cut eyes, simple cel colors, warm cream highlights, rich painted indigo/amber city backgrounds, elastic comic acting. Original otter brothers, never ceramic heads, straws or any named franchise.'
p['style']['palette']='cream and black ink; Riff ginger fur, rust waistcoat and forest-green trousers; Pip chocolate fur, teal cardigan and mustard shirt; indigo storm, amber lamps, copper machinery'
p['style']['constraints']=['No slow motion or time-stretched action','Normal-speed jumps and catches','No photorealism or 3D','No gore','Original character designs','Rubber-hose slapstick, funny and thrilling']
p['master_prompt_raw']='Original otter detective brothers Riff and Pip solve the Midnight Phantom mystery. Exact 150 seconds, 21:9 ultrawide, native 720p, English dialogue, brisk normal-speed action, original swing-jazz suspense score and comic Foley. No slow motion. Final director prompts wait for approval of the revised image set.'
replacements=[('@Cuphead','@Riff'),('@Mugman','@Pip'),('Cuphead','Riff'),('Mugman','Pip'),('Inkwell City','Inkbell City'),('ceramic brothers','otter brothers'),('red shorts','forest-green trouser cuffs'),('blue shorts','russet trousers'),('Mugmans','Pips'),('Cupheads','Riffs')]
def recast(text):
    for before,after in replacements:text=text.replace(before,after)
    return text
p['high_level_idea']=recast(p['high_level_idea'])
p['detailed_script']=recast(p['detailed_script']).replace('Approved production screenplay','Recast screenplay awaiting revised asset approval')
p['script_changes'].append('User-authorized recast: original otter detective brothers Riff and Pip replace the named franchise leads; Inkbell City replaces Inkwell City. The plot, jokes, cast roles, runtime, aspect ratio, resolution and normal-speed action are retained.')
p['adaptation_authorization']='Use original detective characters (Recommended)'
p['adapted_source_text']=recast(p['source_text'])
p['production_status']='awaiting_revised_asset_approval';p['production_stage']='asset_review';p['render_status']='not_submitted'
p['asset_list']=[copy.deepcopy(a) for a in old['asset_list'] if a['id'] not in ('asset_cuphead','asset_mugman','asset_reference')]
for a in p['asset_list']:
    a['description']=recast(a['description']);a['reference_paths']=[]
    a['source']='reused'
    c=copy.deepcopy(helper.selected_media(a));a['candidates']=[c]
    dest=ROOT/c['path'];dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists():
        if dest.read_bytes()!=(OLD/c['path']).read_bytes():raise RuntimeError('Existing candidate differs '+str(dest))
    else:shutil.copy2(OLD/c['path'],dest)
    for relative in c.get('input_reference_paths',[]):
        reference=ROOT/relative;reference.parent.mkdir(parents=True,exist_ok=True)
        if not reference.exists():shutil.copy2(OLD/relative,reference)
    c['provenance']={'source_project_id':old['id'],'original_candidate_id':c['id'],'method':'Unchanged original guard, crow, environments and prop images reused; source generation fingerprint retained rather than reassigned.'}
    c['inspection_notes']='Inspected unchanged image for compatibility with original 1930s cartoon cast; artwork has no franchise characters. Full selected set shown in new review.'
    a['selected_candidate_id']=c['id']
for record in helper.read(ROOT/'new-cast.json'):
    aid='asset_'+record['id'];cid=record['id']+'_c01';rel=f'assets/{aid}/{cid}.png';dest=ROOT/rel;dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists():
        if dest.read_bytes()!=Path(record['source_file']).read_bytes():raise RuntimeError('Existing candidate differs '+str(dest))
    else:shutil.copy2(record['source_file'],dest)
    with Image.open(dest) as im:im.verify()
    with Image.open(dest) as im:dimensions=list(im.size)
    a={'id':aid,'tag':record['tag'],'name':record['name'],'category':'character','description':record['description'],'source':'generated','media_type':'Image','status_variants':[],'reference_paths':[],'generation_prompt':record['prompt'],'candidates':[],'selected_candidate_id':cid}
    a['candidates']=[{'id':cid,'path':rel,'prompt':record['prompt'],'source_revision':0,'dependency_fingerprint':helper.asset_fingerprint(ROOT,p,a),'created_at':datetime.now(timezone.utc).isoformat(),'dimensions':dimensions,'input_reference_paths':[],'generation_tool':'built-in image_gen','requested_style':p['style']['medium'],'inspection_status':'inspected','inspection_notes':'Original otter identity, costume, front/back wardrobe and single head portrait inspected; distinct from rejected franchise designs.'}]
    p['asset_list'].insert(0 if record['id']=='riff' else 1,a)
for chapter in p['chapters']:
    chapter['high_level_idea']=p['high_level_idea'];chapter['scene_summary']=recast(chapter['scene_summary']);chapter['title']=recast(chapter['title'])
    for line in chapter['dialogue']:line['speaker']=recast(line['speaker']);line['text']=recast(line['text'])
    chapter['tagged_assets']=[recast(t) for t in chapter['tagged_assets'] if t!='@UserReference']
    chapter.update(linked_asset_ids=[],delinked_asset_ids=[],prompt='',initial_prompt='',shots=[],materials=[],storyboards=[],selected_storyboard_id=None,takes=[],active_take_id=None,screenshots=[],prompt_status='rough_plan_pending_revised_asset_approval')
    chapter.pop('handoff',None)
p['visual_review_notes']=['Two newly generated original otter detectives inspected.','Nine unchanged generic guard/crow/location/prop images retained and included in revised review.','No Cuphead/Mugman character sheets or user franchise reference are included in the new render set.','The original script remains source material, never a provider image or submitted prompt.','All previous Seedance take records remain in the first project.','Reused candidates retain their original dependency fingerprints and may report stale after the style-bible change; visual approval verifies the actual selected unchanged image bytes.']
shutil.copy2(OLD/'source-script.md',ROOT/'source-script.md')
(ROOT/'screenplay.md').write_text(p['detailed_script'],encoding='utf-8')
(ROOT/'proposal-recast.json').write_text(helper.encoded(p),encoding='utf-8')
helper.save(ROOT,initial,p,'Prepare user-authorized original otter detective cast and unchanged generic references for review')
(ROOT/'exports').mkdir(exist_ok=True)
font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',26);small=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',21)
for category,group in [('character','characters'),('environment','environments'),('prop','props')]:
    assets=[a for a in p['asset_list'] if a['category']==category]
    columns=2 if len(assets)==4 else 1;cell_w=900 if columns==2 else 1000;image_h=round(cell_w*9/16);cell_h=image_h+76
    sheet=Image.new('RGB',(cell_w*columns,cell_h*((len(assets)+columns-1)//columns)),(248,242,221));draw=ImageDraw.Draw(sheet)
    for i,a in enumerate(assets):
        c=helper.selected_media(a);x=i%columns*cell_w;y=i//columns*cell_h
        draw.text((x+16,y+10),a['name']+' | '+a['tag'],font=font,fill=(28,27,26));draw.text((x+16,y+43),'Candidate: '+c['id'],font=small,fill=(71,66,56))
        with Image.open(ROOT/c['path']) as im:
            im=im.convert('RGB');im.thumbnail((cell_w-16,image_h-8),Image.Resampling.LANCZOS);sheet.paste(im,(x+(cell_w-im.width)//2,y+76+(image_h-im.height)//2))
    sheet.save(ROOT/f'exports/review-{group}.jpg',quality=95)
body=['<!doctype html><html lang="en"><meta charset="utf-8"><title>Original Detective Cast Review</title><style>body{font:18px system-ui;background:#f9f1d9;max-width:1300px;margin:32px auto;padding:24px}img{max-width:100%}article{margin-bottom:36px}</style><h1>Riff &amp; Pip: revised asset review</h1><p>150-second mystery, 21:9, 720p, no slow motion. New original otter detectives; generic locations and props retained. Awaiting visual approval.</p>']
for category in ['character','environment','prop']:
    body.append('<h2>'+category.capitalize()+'</h2>')
    for a in p['asset_list']:
        if a['category']!=category:continue
        c=helper.selected_media(a);url='../'+c['path'];body.append('<article><h3>'+html.escape(a['name']+' | '+a['tag']+' | '+c['id'])+'</h3><a href="'+url+'"><img src="'+url+'" alt="'+html.escape(a['name'])+'"></a></article>')
body.append('</html>');(ROOT/'exports/asset-review.html').write_text('\n'.join(body),encoding='utf-8')
prompt_lines=['# Original-cast image prompts','Tool: built-in image_gen.','']
for record in helper.read(ROOT/'new-cast.json'):prompt_lines.extend(['## '+record['tag'],'',record['prompt'],''])
(ROOT/'exports/asset-prompts.md').write_text('\n'.join(prompt_lines),encoding='utf-8')
print(json.dumps({'project':str(ROOT),'new_characters':2,'reused_images':9,'duration':150,'ratio':'21:9','resolution':'720p'}))
