"""Save creative cartoon variants for human asset review; no video submission."""
import copy,hashlib,json,shutil,sys
from datetime import datetime,timezone
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
specs=json.loads((ROOT/'exports/cartoon-style-revision-specs.json').read_text(encoding='utf-8'))
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=copy.deepcopy(p)
old_manifest=helper.review_manifest(ROOT,p)
folder=ROOT/'exports/asset-review-v03-cartoon';folder.mkdir(parents=True,exist_ok=True)
changes=[]
now=datetime.now(timezone.utc).isoformat()
for spec in specs:
    a=next(a for a in q['asset_list'] if a['tag']==spec['tag'])
    old=helper.selected_media(a)
    old_hash=hashlib.sha256((ROOT/old['path']).read_bytes()).hexdigest()
    dest=ROOT/'assets'/a['id']/(spec['candidate']+'.png');dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists():raise RuntimeError('Keep immutable candidate; file exists: '+dest.name)
    shutil.copyfile(spec['source'],dest)
    digest=hashlib.sha256(dest.read_bytes()).hexdigest()
    assert digest==hashlib.sha256(Path(spec['source']).read_bytes()).hexdigest()
    im=Image.open(dest);im.verify();im=Image.open(dest)
    paths=[Path(f).relative_to(ROOT).as_posix() for f in spec['input_paths']]
    candidate={'id':spec['candidate'],'path':dest.relative_to(ROOT).as_posix(),'created_at':now,'source_revision':p['revision'],'prompt':spec['prompt'],'generator':'built-in image_gen','reference_paths':paths,'generation_inputs':[{'path':f,'sha256':hashlib.sha256((ROOT/f).read_bytes()).hexdigest()} for f in paths],'dimensions':list(im.size),'sha256':digest,'dependency_provenance':'Exact submission prompt and reference hashes retained. Helper dependency fingerprint not captured at image submission; no retrospective freshness claim.','inspection':{'inspected':True,'single_character_three_views':True,'only_one_face':True,'wardrobe_palette_and_accessories_preserved':True,'more_stylized_face':True,'no_text':True,'notes':'Larger designed eyes, smoother skin and simpler broad age folds; senior identity, original costume, hairstyle, spectacles and walking stick/handbag where applicable remain recognizable.'}}
    (dest.with_suffix('.prompt.txt')).write_text(spec['prompt'],encoding='utf-8')
    (dest.with_suffix('.metadata.json')).write_text(json.dumps(candidate,ensure_ascii=False,indent=2),encoding='utf-8')
    a['candidates'].append(candidate)
    a['selected_candidate_id']=spec['candidate']
    a['prior_description']=a['description']
    if spec['tag']=='@Mr-Ko':
        a['description']='Original slender elderly Hong Kong man Mr Ko, long gentle face, high forehead, swept messy silver hair, large soft ears, beige cardigan, pale blue shirt, dark brown trousers and dark slip-on shoes. User-requested creative style revision: clear rounded cartoon 3D anatomy, larger expressive eyes, simplified smooth skin and a few broad age folds; retain identity and wardrobe from supplied image.'
    else:
        a['description']+=' User-requested creative style revision: clearer rounded cartoon 3D anatomy, larger designed expressive eyes, simplified smooth skin, a few broad age folds, sculpted hair shapes and simplified hands. Keep original costume, color, hairstyle, eyewear and accessories.'
    a['style_revision_purpose']='Creative art-direction consistency only. No provider moderation acceptance or successful video generation claimed.'
    changes.append({'tag':a['tag'],'asset_id':a['id'],'old_candidate':old['id'],'old_path':old['path'],'old_sha256':old_hash,'new_candidate':spec['candidate'],'new_path':candidate['path'],'new_sha256':digest})
q['stage']='awaiting_cartoon_asset_review'
q['render_status']='awaiting_asset_review_and_provider_review'
q.setdefault('creative_style_revisions',[]).append({'created_at':now,'purpose':'Correct four human characters that had more realistic surface detail than the original cartoon art direction. Independent creative asset revision; provider moderation status remains unresolved.','tags':[c['tag'] for c in changes],'previous_candidates_preserved':True,'new_video_attempts':0,'paid_library_route':'Unavailable per user; no library, KYC or subscription purchase performed.'})
assert q.get('provider_review_required') is True
out=folder/'selection-proposal.json';out.write_text(json.dumps(q,ensure_ascii=False,indent=2),encoding='utf-8')
errors,warnings=helper.validate(ROOT,q)
if errors:raise RuntimeError('\n'.join(errors))
print(helper.save(ROOT,p,q,'Select four more cartoon-styled creative character variants for user review; retain provider hold and original files'))
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',24)
small=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',18)
sheet=Image.new('RGB',(1672,1030),(246,242,233));d=ImageDraw.Draw(sheet)
for i,change in enumerate(changes):
    x=(i%2)*836;y=(i//2)*515
    im=Image.open(ROOT/change['new_path']).convert('RGB');im=ImageOps.contain(im,(828,466))
    sheet.paste(im,(x+(836-im.width)//2,y))
    d.text((x+12,y+468),change['tag']+' / '+change['new_candidate'],font=font,fill=(46,41,34))
sheet.save(folder/'revised-characters.jpg',quality=94)
assets=p['asset_list']
pages=[]
for page in range(4):
    chosen=assets[page*12:(page+1)*12]
    canvas=Image.new('RGB',(1440,1132),(246,242,233));draw=ImageDraw.Draw(canvas)
    for i,a in enumerate(chosen):
        x=(i%3)*480;y=(i//3)*283
        media=helper.selected_media(a)
        im=Image.open(ROOT/media['path']).convert('RGB');im=ImageOps.contain(im,(472,227))
        canvas.paste(im,(x+(480-im.width)//2,y))
        draw.text((x+10,y+229),a['tag'],font=font,fill=(46,41,34))
        draw.text((x+10,y+257),media['id'],font=small,fill=(86,76,64))
    file=folder/f'full-gallery-{page+1}.jpg';canvas.save(file,quality=92);pages.append(file.relative_to(ROOT).as_posix())
full=['# Current selected asset set — cartoon revision review','','Four revised characters are proposed. The other forty-four selected images are unchanged. These review contact sheets never become video inputs.','','| Revised tag | Candidate | Full-size original file |','|---|---|---|']
for c in changes:full.append('| '+c['tag']+' | '+c['new_candidate']+' | [Open revised sheet](../../'+c['new_path']+') |')
for page in pages:full+=['','![Current selected set]('+Path(page).name+')']
full+=['','## Every selected full-size image','']
for a in assets:
    m=helper.selected_media(a)
    full+=['### '+a['name']+' — '+a['tag']+' — '+m['id'],'','![Selected reference](../../'+m['path']+')','']
full+=['## State','','The current scene 37–51 plan remains 480p, 16:9 with no title/subtitles/captions/text boxes. Asset approval is pending after this design revision. Separately, existing Seedance input-privacy and output-audio refusals are unresolved. No new video submissions were made and no safety settings were changed.']
(folder/'full-size-gallery.md').write_text('\n'.join(full)+'\n',encoding='utf-8')
before={a['asset_id']:a for a in old_manifest['images']}
after=helper.review_manifest(ROOT,p)
new_tags={c['tag'] for c in changes}
unchanged=[a for a in after['images'] if a['tag'] not in new_tags and a['sha256']==before[a['asset_id']]['sha256'] and a['candidate_id']==before[a['asset_id']]['candidate_id']]
assert len(unchanged)==44
for c in changes:assert hashlib.sha256((ROOT/c['old_path']).read_bytes()).hexdigest()==c['old_sha256']
(folder/'revision-audit.json').write_text(json.dumps({'changes':changes,'unchanged_selected_assets':len(unchanged),'old_candidates_and_source_files_preserved':True,'overall_style_unchanged':p['style']==q['style'],'image_inspection':'All four generated sheets directly inspected before registration; saved copies decoded and hash-verified.','new_video_attempts':0,'provider_review_required':p['provider_review_required'],'errors':errors,'warnings_outside_requested_render_scope':warnings},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'four_revised':changes,'unchanged_selected_assets':len(unchanged),'review_gallery':str(folder/'full-size-gallery.md'),'provider_hold_preserved':True},ensure_ascii=False,indent=2))
