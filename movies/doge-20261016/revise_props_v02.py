from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,hashlib,datetime,subprocess,sys
ROOT=Path(__file__).resolve().parent
def save(path,data):path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
 p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));assert p['revision']==4
 baseline=json.loads((ROOT/'history/revision-000003.json').read_text(encoding='utf-8'))
 jobs=json.loads((ROOT/'source/prop-revision-requests-v02.json').read_text(encoding='utf-8'));now=datetime.datetime.now(datetime.timezone.utc).isoformat();revised=[]
 for j in jobs:
  a=next(a for a in p['asset_list'] if a['tag']=='@'+j['id']);meta=json.loads((ROOT/f"source/generated-{j['id']}-c02.json").read_text());rel=f"assets/asset_{j['id']}/generated_c02.png";file=ROOT/rel
  with Image.open(file) as im:im.verify()
  candidate={'id':'generated_c02','path':rel,'prompt':meta['prompt'],'source_revision':4,'dependency_fingerprint':meta['dependency_fingerprint'],'created_at':meta['created_at'],'dimensions':list(Image.open(file).size),'tool':'built-in image_gen','sha256':sha(file),'generation_input_paths':meta['reference_paths'],'inspection':{'inspected_at':now,'finding':{'mei-photo':'Mei and Mr. Ko share rounded stylized cartoon facial planes and enlarged expressive eyes.','balloon-bundle':'Eight ordinary oval balloons counted: two coral, two teal, two gold, two lavender.','sir-squeaks-tail':'Exactly two rear webbed feet; no forelegs at torn front edge.','red-taxi':'Roof light clearly reads TAXI in black uppercase letters.'}[j['id']]}}
  assert not any(c['id']==candidate['id'] for c in a['candidates']);a['candidates'].append(candidate);a['selected_candidate_id']=candidate['id'];revised.append(a)
 revised_tags={a['tag'] for a in revised};unchanged=[]
 for old in baseline['asset_list']:
  a=next(x for x in p['asset_list'] if x['id']==old['id'])
  # Every prior candidate file remains byte-identical, including discarded versions.
  for c in old['candidates']:
   if c.get('sha256'):assert sha(ROOT/c['path'])==c['sha256']
  if a['tag'] not in revised_tags:
   assert a['selected_candidate_id']==old['selected_candidate_id'];c=next(x for x in old['candidates'] if x['id']==old['selected_candidate_id']);assert sha(ROOT/c['path'])==sha(ROOT/next(x for x in a['candidates'] if x['id']==a['selected_candidate_id'])['path']);unchanged.append(a['tag'])
 assert len(revised)==4 and len(unchanged)==44
 assert p['chapters']==baseline['chapters'],'Asset edits must not rewrite source chapters.'
 for m in json.loads((ROOT/'source/source-manifest.json').read_text()):assert sha(ROOT/m['copy'])==m['sha256']
 p['stage']='asset_review_awaiting_user';p.setdefault('asset_inspection',{}).setdefault('revisions',[]).append({'inspected_at':now,'candidate_id':'generated_c02','tags':list(revised_tags),'unchanged_selected_assets':44,'scope':'Four user-requested prop corrections only'})
 proposal=ROOT/'exports/prop-selection-proposal-r4.json';save(proposal,p)
 out=ROOT/'exports/asset-review-v02';out.mkdir(exist_ok=True)
 font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',27);small=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',23);title=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',36)
 board=Image.new('RGB',(1800,1290),'#f4f1e9');draw=ImageDraw.Draw(board);draw.text((24,20),'Revised props - candidate generated_c02',font=title,fill='#252a30')
 for n,a in enumerate(revised):
  c=next(x for x in a['candidates'] if x['id']==a['selected_candidate_id']);x=n%2*900;y=90+n//2*600;draw.text((x+20,y+6),a['name'],font=font,fill='#252a30');draw.text((x+20,y+42),a['tag']+' | '+c['id'],font=small,fill='#47515b');im=Image.open(ROOT/c['path']).convert('RGB');im.thumbnail((872,508));board.paste(im,(x+(900-im.width)//2,y+85+(508-im.height)//2))
 board.save(out/'revised-props.jpg',quality=95)
 md=['# doge-20261016 - current complete asset set','','Four revised props use generated_c02. The other 44 selections are unchanged.','']
 selected=[]
 for category in ['character','environment','prop']:
  md+=['## '+category.title()+'s','']
  for a in p['asset_list']:
   if a['category']!=category:continue
   c=next(x for x in a['candidates'] if x['id']==a['selected_candidate_id']);path=(ROOT/c['path']).as_posix();md+=['### '+a['name']+' - '+a['tag']+' - '+c['id'],'',f'![{a["name"]}](<{path}>)',''];selected.append({'id':a['id'],'tag':a['tag'],'name':a['name'],'category':category,'candidate_id':c['id'],'path':c['path'],'sha256':sha(ROOT/c['path'])})
 (out/'full-size-gallery.md').write_text('\n'.join(md),encoding='utf-8');save(out/'selected-assets.json',selected)
 audit={'revised_assets':[a['tag'] for a in revised],'unchanged_selected_assets':len(unchanged),'previous_candidates_preserved':True,'source_archive_sha256_verified':True,'source_scenes_unchanged':True,'scene_count':len(p['chapters']),'runtime_seconds':sum(c['duration'] for c in p['chapters']),'video_attempts':sum(len(c['takes']) for c in p['chapters'])};save(out/'revision-audit.json',audit)
 helper='C:/Users/Admin 3/.codex/skills/movi2/scripts/project.py';cmd=[sys.executable,'-X','utf8',helper]
 result=subprocess.run(cmd+['check',str(ROOT),'--from',str(proposal)],capture_output=True,text=True,encoding='utf-8');check=json.loads(result.stdout);save(out/'project-check.json',check);assert result.returncode==0,check['errors'];print(json.dumps({'errors':check['errors'],'warnings':check['warnings'],'audit':audit}))
 result=subprocess.run(cmd+['commit',str(ROOT),'--from',str(proposal),'--reason','Select four inspected corrected prop candidates; retain previous versions and unchanged 44 assets'],capture_output=True,text=True,encoding='utf-8',check=True);print(result.stdout)
 result=subprocess.run(cmd+['review-assets',str(ROOT)],capture_output=True,text=True,encoding='utf-8',check=True);review=json.loads(result.stdout);save(out/'review-manifest.json',review);print(json.dumps({'review_id':review.get('review_id'),'status':review.get('status'),'revision':review.get('revision')}))
if __name__=='__main__':main()
