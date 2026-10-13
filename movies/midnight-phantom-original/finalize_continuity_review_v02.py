import html,json,hashlib
from datetime import datetime,timezone
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from project_ops import ROOT,helper,commit,write_json
p=helper.read(ROOT/'project.json')
a=next(a for a in p['asset_list'] if a['tag']=='@TowerLayout')
for item in helper.read(ROOT/'exports/continuity-v02-receipts-tower-layout.json'):
 path=ROOT/f'assets/{a["id"]}/{item["candidate_id"]}.png'
 if not path.exists() or hashlib.sha256(path.read_bytes()).digest()!=hashlib.sha256(Path(item['source_file']).read_bytes()).digest():raise RuntimeError('Copied reference mismatch')
 refs=item['reference_paths']
 if item['candidate_id']=='tower_layout_c02':refs=['assets/asset_tower_layout_v02/tower_layout_c01.png','assets/asset_riff/riff_c03.png','assets/asset_pip/pip_c01.png']
 if item['candidate_id']=='tower_layout_c03':refs=['assets/asset_tower_layout_v02/tower_layout_c02.png']
 with Image.open(path) as im: dimensions=list(im.size)
 a['candidates'].append({'id':item['candidate_id'],'path':path.relative_to(ROOT).as_posix(),'prompt':item['prompt'],'source_revision':item['source_revision'],'dependency_fingerprint':item['dependency_fingerprint'],'created_at':datetime.now(timezone.utc).isoformat(),'dimensions':dimensions,'input_reference_paths':refs,'generation_tool':'built-in image_gen','inspection_status':'rejected_hero_scale' if item['candidate_id']!='tower_layout_c03' else 'visually_inspected_fixed_stage_full_crow'})
a['selected_candidate_id']='tower_layout_c03'
a['description']='Single continuous fixed 21:9 tower stage derived from supplied screenshot: machine rear-center, clockwork rear, rope left-center beside closed trapdoor, complete Crow fixed right, stationary clamped red cable to simple right-curtain controller. No heroes are painted into this spatial plate: separate character sheets and exact numeric ScaleReference determine their 1H size versus Crow4H. No panels, storyboard, measurement labels in film. Crow world anchor, machine and console placement remain fixed across cuts.'
a['reference_paths']=['assets/reference/continuity-v02/user-tower-layout.png','assets/asset_tower/tower_c03.png','assets/asset_machine/machine_c01.png']
for asset in p['asset_list']:
 c=helper.selected_media(asset)
 if c and asset.get('media_type','Image')=='Image' and c.get('inspection_status') not in ('verified_geometry_165_165_165_660','visually_inspected_fixed_stage_full_crow'):
  c['inspection_status']='visually_inspected_for_v02_review'
p['continuity_revision']['status']='awaiting_revised_asset_approval'
p['continuity_revision']['scale_reference_method']='Exact numeric 1:1:1:4 height diagram; drifting illustrative chart candidates rejected. Tower stage excludes heroes to avoid incorrect scale baked into layout.'
p['continuity_revision']['new_video_jobs_submitted']=0
commit(p,'Prepare inspected continuity v02 reference set for mandatory visual review; preserve all prior media')
manifest=helper.review_manifest(ROOT,p)
write_json(ROOT/'exports/continuity-v02-selected-assets.json',manifest)
groups=[('characters','Characters'),('environments','Environments'),('props','Main props'),('references','Spatial references and supplied source')]
font=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',25);small=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',23)
htmlparts=['<!doctype html><meta charset="utf-8"><title>Continuity v02 reference review</title><style>body{background:#faf3df;color:#24242a;font-family:Arial;margin:30px} img{max-width:95vw;max-height:85vh}figure{margin:30px 0}a{color:#155f80}</style><h1>Continuity v02 reference review</h1><p>Prepared references only. Revised movie has not been generated. Scale diagram governs dimensions, separate character sheets govern designs. Supplied screenshot governs set placement.</p>']
for slug,title in groups:
 cat={'characters':'character','environments':'environment','props':'prop','references':'reference'}[slug]
 rows=[r for r in manifest['images'] if r['category']==cat]
 cellw=900;ih=490;cellh=565;cols=2
 sheet=Image.new('RGB',(cellw*cols,cellh*((len(rows)+cols-1)//cols)),(250,243,223));d=ImageDraw.Draw(sheet)
 for i,r in enumerate(rows):
  x=i%cols*cellw;y=i//cols*cellh
  d.text((x+15,y+8),r['name'],font=font,fill='#24242a');d.text((x+15,y+39),r['tag']+' | '+r['candidate_id'],font=small,fill='#40404b')
  with Image.open(ROOT/r['path']) as im:
   im=im.convert('RGB');im.thumbnail((cellw-20,ih-12),Image.Resampling.LANCZOS);sheet.paste(im,(x+(cellw-im.width)//2,y+75+(ih-im.height)//2))
  label=html.escape(r['name']+' | '+r['tag']+' | '+r['candidate_id']);link='../'+r['path']
  htmlparts.append(f'<figure><figcaption>{label}</figcaption><a href="{link}"><img src="{link}"></a></figure>')
 sheet.save(ROOT/f'exports/continuity-v02-review-{slug}.jpg',quality=96)
htmlparts.append('<h2>Crow voice guide</h2><p>@CrowVoice | crow_voice_later_v02. Native excerpt with background music; use voice timbre as guide.</p><audio controls src="../assets/reference/continuity-v02/crow-voice-from-later-scene.wav"></audio>')
(ROOT/'exports/continuity-v02-full-size-review.html').write_text('\n'.join(htmlparts),encoding='utf-8')
print(json.dumps({'image_count':len(manifest['images']),'missing':manifest['missing'],'review_page':str(ROOT/'exports/continuity-v02-full-size-review.html')}))
