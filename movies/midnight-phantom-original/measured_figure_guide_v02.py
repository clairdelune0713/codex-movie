"""Numeric standing-height diagram using unchanged imagegen pose sprites."""
import json,shutil,hashlib
from PIL import Image,ImageDraw,ImageFont
from project_ops import ROOT,helper,commit,write_json
p=helper.read(ROOT/'project.json');before=p['revision'];receipts=helper.read(ROOT/'exports/continuity-v02-standing-pose-receipts.json')
# Keep the existing approved render inputs for a clearly labeled review cut.
chosen={1:'take_03',2:'take_02',3:'take_03',4:'take_03',5:'take_02',6:'take_03',7:'take_02',8:'take_04',9:'take_04',10:'take_03',11:'take_03',12:'take_02',13:'take_04'}
preview=[]
for ch in p['chapters']:
 t=next(t for t in ch['takes'] if t['id']==chosen[ch['chapter_index']])
 if t['status']!='succeeded':raise RuntimeError('Review clip unavailable '+ch['id'])
 preview.append({'chapter_id':ch['id'],'take_id':t['id'],'path':t['path'],'duration':ch['duration'],'movie_start':ch['movie_start'],'source_revision':t['source_revision'],'dependency_fingerprint':t['dependency_fingerprint']})
write_json(ROOT/'exports/continuity-v02-review-cut-inputs.json',{'source_project_revision':before,'status':'review_candidate_not_final','inputs':preview,'limitations':'Exact1:1:1:4 scale, several actor placements, guard handoff and tower action details remain unresolved. Candidate is for reviewing improvements, not proof of all requested corrections.'})
poses=[]
for j in receipts:
 rel=f'assets/reference/continuity-v02/standing-{j["key"].lower()}-c01.png';dst=ROOT/rel;dst.parent.mkdir(parents=True,exist_ok=True)
 if dst.exists():
  if hashlib.sha256(dst.read_bytes()).digest()!=hashlib.sha256(open(j['source_file'],'rb').read()).digest():raise RuntimeError('Preserve pose original')
 else:shutil.copy2(j['source_file'],dst)
 with Image.open(dst) as im:
  if im.mode!='RGBA':raise RuntimeError('Generated alpha required')
  bounds=im.getchannel('A').point(lambda a:255 if a>=128 else 0).getbbox()
 poses.append({'character':j['key'],'path':rel,'core_alpha_bounds':list(bounds),'prompt':j['prompt'],'reference_path':j['path'].replace('\\','/'),'generation_tool':'built-in image_gen','file_sha256':hashlib.sha256(dst.read_bytes()).hexdigest()})
write_json(ROOT/'exports/continuity-v02-standing-pose-provenance.json',poses)
a=next(a for a in p['asset_list'] if a['tag']=='@ScaleReference')
a['description']='Exact measured standing-height comparison with complete actor figures: Riff,Pip,Guard each1H and Crow4H. Original imagegen full-body sprites laid out on one shared baseline using uniform scaling; no change to drawn anatomy/costume. Highest tuft/cap/crest and lowest sole/claw define height. Diagram guide lines/labels are reference only, not movie content. Separate character sheets remain canonical costume/identity references.'
a['reference_paths']=[o['path'] for o in poses]
diagram=ROOT/'assets/asset_scale_v02/scale_c07.png'
if diagram.exists():raise RuntimeError('Preserve measured diagram candidate')
W,H=3600,1900;floor=1700;unit=360
canvas=Image.new('RGBA',(W,H),'#faf4df');d=ImageDraw.Draw(canvas)
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',60);title=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',77)
d.text((75,55),'Complete standing figures: 1 : 1 : 1 : 4',font=title,fill='#27272f')
for n in range(5):
 y=floor-unit*n;d.line((180,y,3460,y),fill='#a4a49b',width=3);d.text((55,y-36),str(n)+'H',font=font,fill='#45454b')
measurements=[]
for o,center,multiple in zip(poses,[430,900,1370,2740],[1,1,1,4]):
 with Image.open(ROOT/o['path']) as im:
  sprite=im.crop(tuple(o['core_alpha_bounds']))
  height=unit*multiple;width=round(sprite.width*height/sprite.height)
  sprite=sprite.resize((width,height),Image.Resampling.LANCZOS)
  x=center-width//2;y=floor-height;canvas.alpha_composite(sprite,(x,y))
  measurements.append({'character':o['character'],'height_units':multiple,'layout_height_px':height,'top_y':y,'sole_baseline_y':floor,'width_px':width,'source_core_alpha_bounds':o['core_alpha_bounds']})
 d.text((center-130,floor+25),o['character']+' '+str(multiple)+'x',font=font,fill='#27272f')
d.text((110,1815),'One floor plane. Whole models retain this size through every pose and camera cut.',font=font,fill='#45454b')
canvas.convert('RGB').save(diagram)
fp=helper.asset_fingerprint(ROOT,p,a)
a['candidates'].append({'id':'scale_c07','path':diagram.relative_to(ROOT).as_posix(),'prompt':'Exact numeric scale comparison of generated complete standing pose sprites; placement and uniform layout heights360/360/360/1440px on shared y1700sole baseline. No existing character artwork repainted; no storyboard panels.','source_revision':before,'dependency_fingerprint':fp,'generation_tool':'built-in image_gen pose sprites plus exact dimension-diagram layout','dimensions':[W,H],'input_reference_paths':a['reference_paths'],'measurements':measurements,'inspection_status':'numeric_bounds_verified_pending_visual_review'})
a['selected_candidate_id']='scale_c07'
p['continuity_revision']['status']='refining_visual_grounding';p['continuity_revision']['unresolved']='Repeated Seedance generations/edits did not meet strict4x scale; strengthen visual size grounding and post-catch state before further renders.'
p['continuity_revision']['scale_guide_measurements']=measurements
for ch in p['chapters']:ch['prompt_status']='existing_v02_prompts_pending_stronger_reference_review'
commit(p,'Replace abstract scale bounds with measured complete figure guide; preserve review-cut source selection and unresolved audit')
write_json(ROOT/'exports/continuity-v02-measured-figure-guide.json',{'candidate':'scale_c07','source_project_revision':before,'measurements':measurements,'canonical_images_unchanged':True,'reference_image_review_required':True})
print(json.dumps({'guide':str(diagram),'heights':[m['layout_height_px'] for m in measurements],'baseline':floor,'status':'requires_updated_visual_review'}))
