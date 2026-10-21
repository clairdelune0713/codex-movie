from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,re,shutil,math,hashlib,datetime
ROOT=Path(__file__).resolve().parent
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
 p=json.loads((ROOT/'project.json').read_text(encoding='utf-8')); assets=p['asset_list']; missing=[]
 for a in assets:
  if a['source']!='generated' or a['tag'] in ('@mags','@boss'):continue
  jobs=sorted((ROOT/'source').glob('generated-'+a['tag'][1:]+'-c*.json'))
  if not jobs:missing.append(a['tag']);continue
  for f in jobs:
   meta=json.loads(f.read_text());num=re.search(r'-c(\d+)\.json$',f.name).group(1); cid='generated_c'+num
   source=Path(re.search(r' as (C:.*?\.png) by default',meta['output_hint']).group(1)); dest=ROOT/'assets'/a['id']/(cid+'.png');dest.parent.mkdir(parents=True,exist_ok=True)
   if not dest.exists():shutil.copy2(source,dest)
   with Image.open(dest) as im: im.verify()
   inputs=[Path(s).relative_to(ROOT).as_posix() if Path(s).is_absolute() else s for s in meta.get('reference_paths',[])]
   c={'id':cid,'path':dest.relative_to(ROOT).as_posix(),'prompt':meta['prompt'],'source_revision':meta['source_revision'],'dependency_fingerprint':meta['dependency_fingerprint'],'created_at':meta['created_at'],'dimensions':list(Image.open(dest).size),'tool':'built-in image_gen','sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'generation_input_paths':inputs}
   if not any(x['id']==cid for x in a['candidates']):a['candidates'].append(c)
   a['selected_candidate_id']=cid
 assert not missing,missing
 # Rough chapter asset coverage; final scene prompts intentionally remain empty until review approval.
 G=['granny-wong','granny-lee','granny-chan']; P=['puppy-tart','puppy-tine']; T=['Tine','Kiki']; W=['Tart-working','Mr-Leung']; O=['Tart-off-duty','Mr-Leung'];H=['sir-squeaks-head'];Q=['sir-squeaks-tail'];B=['Mr-Ko','jade','jade-cage'];R=['victoria-harbour']
 mapping={
 1:P+['mags','kookaburra','sunny-hill-ranch','explorer-kit'],2:P+['gertrude','sunny-hill-ranch','explorer-kit'],3:P+['gertrude','kookaburra','sunny-hill-ranch','explorer-kit'],4:P+['mags','kookaburra','sunny-hill-ranch','explorer-kit'],5:P+['mags','ranch-veranda','sir-squeaks-whole']+H+Q,6:P+['mags','ranch-veranda']+H+Q,7:P+['mags','hay-loft']+H+Q,8:P+['mags','sunny-hill-ranch','transport-van']+H+Q,9:P+['mags','kookaburra','sunny-hill-ranch','transport-van']+H+Q,10:P+H+Q,
 11:['Tart-off-duty','Tine','training-yards','victoria-harbour'],12:['Tart-working','training-yards'],13:['Tart-working','Tine','Kiki','training-yards','training-hallway']+H+Q,14:O+['leung-flat']+H,15:O+['Tart-working','leung-flat'],16:W+['sheung-wan-street','green-tram','bo-cafe'],17:W+['Auntie-Bo','boss','bo-cafe'],18:W+['radio-booth'],19:T+G+['elder-centre','smile-counter']+Q,20:T+B+['elder-centre','mei-photo']+Q,21:T+['Mr-Ko','granny-chan','elder-centre']+Q,22:T+B+['elder-centre','mei-photo']+Q,23:T+['Auntie-Bo','boss','bo-cafe']+Q,24:W+['Auntie-Bo','boss','bo-cafe','green-tram'],25:W+['steep-street','orange-cart','red-taxi'],26:W+['steep-street','orange-cart','red-taxi'],27:W+['steep-street','orange-cart','red-taxi','bo-cafe','Auntie-Bo','boss'],28:T+B+G+['elder-centre','mei-photo','smile-counter']+Q,29:T+B+G+['elder-centre','mei-photo']+Q,30:T+W+['jade','market-street','sheung-wan-street','green-tram']+Q,31:['Tine','jade','black-kite','rooftops']+Q,32:T+G+['Mr-Ko','jade','black-kite','rooftops']+Q,33:T+G+['Mr-Ko','jade','rooftops','smile-counter']+Q,34:T+G+['Mr-Ko','jade','rooftops']+Q,
 35:W+O+T+['sheung-wan-street','victoria-harbour','mtr-interior','leung-flat','kiki-flat']+H+Q,36:W+O+['Tine','red-taxi','sheung-wan-street','leung-flat','kiki-flat']+H+Q,37:W+T+B+G+R+Q,38:W+T+R+Q,39:W+['Tart-off-duty']+R,40:['Tart-off-duty']+T+R+Q,41:['Tart-off-duty','Mr-Leung']+T+G+R+['balloon-bundle']+Q,42:['Tart-off-duty']+T+['Mr-Ko']+G+R+['balloon-bundle']+Q,43:['Tart-off-duty']+T+R+P+['gertrude','mags']+Q,44:['Tart-off-duty','Mr-Leung']+T+R+Q,45:['Tart-off-duty','Mr-Leung']+T+R+Q,46:['Tart-off-duty','Mr-Leung','Mr-Ko']+T+R+Q,47:['Mr-Leung','Mr-Ko']+R,48:['Tart-off-duty','Mr-Leung','Mr-Ko']+T+G+R+['smile-counter']+Q,49:['Tart-leash','Mr-Leung','Mr-Ko','jade','jade-cage','Auntie-Bo','boss','cat-backpack']+T+G+R+H+Q,50:R,51:['mags','gertrude','kookaburra','sunny-hill-ranch']}
 known={a['tag']:a['id'] for a in assets}
 for c in p['chapters']:
  tags=list(dict.fromkeys('@'+x for x in mapping[c['source_scene']]));assert all(t in known for t in tags)
  c['tagged_assets']=tags;c['linked_asset_ids']=[known[t] for t in tags]
  if c['source_scene'] in [10,50]:c['assembly_mode']='local motion graphics per source, with selected original source visuals as needed'
  if c['source_scene'] in [11,13,36]:c['split_screen_plan']='Generate independent left/right source performances and composite exact source split-screen sections locally; preserve scene timeline.'
  if c['source_scene']==43:c['memory_plan']='Use normal-speed selected excerpts from source scenes 1-7 for source shot 43.2, 4 x 1.5s; warm grade only, no slowing.'
  if c['source_scene'] in [6,15,20,26,27,34,44,45,46,47,48]:c['handoff_plan']='Inspect previous selected take end before deriving a first frame. Preserve shared-set anchors, wardrobe, toy ownership and light. Choose supported first-frame mode or narrow end-state reference without discarding necessary identity refs.'
 p['stage']='assets_selected_pending_visual_review';save(ROOT/'exports/asset-selection-proposal.json',p)
 used={t for c in p['chapters'] for t in c['tagged_assets']};assert used==set(known),(used^set(known))
 selected=[]
 for a in assets:
  c=next(x for x in a['candidates'] if x['id']==a['selected_candidate_id']);selected.append({'id':a['id'],'tag':a['tag'],'name':a['name'],'category':a['category'],'candidate_id':c['id'],'path':c['path'],'dimensions':c.get('dimensions'),'source':a['source'],'sha256':hashlib.sha256((ROOT/c['path']).read_bytes()).hexdigest()})
 save(ROOT/'exports/selected-assets.json',selected)
 out=ROOT/'exports/asset-review';out.mkdir(exist_ok=True)
 font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',24);small=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',20);title=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',32)
 groups=[('characters-supplied','Supplied characters - unchanged',[a for a in selected if a['category']=='character' and a['source']=='supplied']),('characters-new','New supporting characters',[a for a in selected if a['category']=='character' and a['source']=='generated']),('environments-1','Locations - ranch and everyday Hong Kong',[a for a in selected if a['category']=='environment'][:8]),('environments-2','Locations - action and harbour',[a for a in selected if a['category']=='environment'][8:]),('props-1','Main props',[a for a in selected if a['category']=='prop'][:7]),('props-2','Main props and toy halves',[a for a in selected if a['category']=='prop'][7:])]
 contacts=[]
 for slug,label,items in groups:
  width=1560;cellw=780;cellh=510;rows=math.ceil(len(items)/2);board=Image.new('RGB',(width,rows*cellh+88),'#f4f1e9');d=ImageDraw.Draw(board);d.text((22,21),label,fill='#252a30',font=title)
  for n,a in enumerate(items):
   col=n%2;row=n//2;x=col*cellw;y=88+row*cellh;d.text((x+18,y+8),a['name'],fill='#252a30',font=font);d.text((x+18,y+40),a['tag']+' | '+a['candidate_id'],fill='#47515b',font=small)
   im=Image.open(ROOT/a['path']).convert('RGB');im.thumbnail((cellw-26,cellh-90));board.paste(im,(x+(cellw-im.width)//2,y+80+(cellh-90-im.height)//2))
  dest=out/(slug+'.jpg');board.save(dest,quality=94);contacts.append({'path':dest.relative_to(ROOT).as_posix(),'label':label,'assets':[a['id'] for a in items]})
 save(out/'contact-sheet-manifest.json',contacts)
 md=['# doge-20261016 — full-size asset review','','Every selected asset is listed below. Contact sheets are for review only and never go into video inputs.','']
 for cat in ['character','environment','prop']:
  md+=['## '+cat.title()+'s','']
  for a in selected:
   if a['category']!=cat:continue
   path=(ROOT/a['path']).as_posix();md+=['### '+a['name']+' — '+a['tag']+' — '+a['candidate_id'],'',f'![{a["name"]}](<{path}>)','']
 (out/'full-size-gallery.md').write_text('\n'.join(md),encoding='utf-8')
 save(ROOT/'exports/asset-file-audit.json',{'selected_count':len(selected),'categories':{k:sum(a['category']==k for a in selected) for k in ['character','environment','prop']},'all_selected_files_decode':True,'all_assets_linked':True,'supplied_selected_unchanged':all(hashlib.sha256((ROOT/a['path']).read_bytes()).hexdigest()==a['sha256'] for a in selected if a['source']=='supplied'),'dimensions':{a['tag']:a['dimensions'] for a in selected},'notes':['Cat backpack returned 1536x1024; preserve actual aspect as a prop reference. Movie framing remains 16:9.','Training-yard candidate c02 includes the mock open hole required by source scene 12.','Generated puppy candidates remain unselected in history; supplied puppies selected unchanged.']})
 print(json.dumps({'selected':len(selected),'contacts':contacts,'missing':missing},indent=2))
if __name__=='__main__':main()
