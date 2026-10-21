from pathlib import Path
import json, re, sys
from datetime import datetime, timezone
from PIL import Image

ROOT = Path(__file__).resolve().parent
project = json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
script = (ROOT/'source'/'screenplay-readable.md').read_text(encoding='utf-8')
raw = (ROOT/'source'/'doge-script.md').read_text(encoding='utf-8-sig')
jobs = json.loads((ROOT/'asset-generation-jobs.json').read_text(encoding='utf-8'))
jobs += json.loads((ROOT/'additional-asset-jobs.json').read_text(encoding='utf-8'))
mags = json.loads((ROOT/'assets'/'mags'/'c01.json').read_text(encoding='utf-8'))
jobs.append(mags)
source_defs = [
 ('adult-tart','Tart — Collar at Home','Cream Labrador, plush fur, round brown eyes, brown nose, floppy ears, dark-brown leather collar and silver buckle; home state, no harness.'),
 ('adult-tart-harness','Tart — Working Harness','Same Tart, tan leather guide harness, curved silver handle and caramel grip. Working at Mr. Leung\'s left, no play or departure.'),
 ('adult-tart-leash','Tart — Off Duty on Brown Leash','Same Tart in collar with brown leather leash clipped before harness removal; public off-duty state, lead always held by Mr. Leung.'),
 ('adult-tine','Tine','Fox-red fluffy Labrador, expressive eyebrows, orange bandana with circular badge, orange leash clipped to collar beneath bandana, white heart marking above tail. Add approved blue toy tail-half at bandana knot when script requires; sheet has no toy.'),
 ('puppy-tart','Puppy Tart','Tiny round cream Labrador puppy with oversized paws, floppy ears and dark brown nose.'),
 ('puppy-tine','Puppy Tine','Tiny round fluffy fox-red Labrador puppy, white heart-shaped fur patch on lower back above tail.'),
 ('blind-guy','Mr. Leung','Completely blind Hong Kong man, mid-50s, side-parted black hair gray at temples, black sunglasses ALWAYS ON, teal wool zip jacket, cream shirt, charcoal trousers, brown shoes. Responds to sound, scent and touch, never visual tracking. Harness handle in LEFT hand.'),
 ('animal-companion-worker','Kiki','Young Hong Kong woman, mid-20s, black low ponytail, sage overshirt with rolled sleeves, cream tee, tan satchel, navy trousers and white sneakers. Holds Tine\'s orange leash, invites greetings, silver tally counter.'),
 ('lonely-old-man','Mr. Ko','Slim elderly Hong Kong man, early 80s, wispy gray hair, large ears, beige knitted cardigan over light-blue shirt, dark-brown trousers, dark slip-ons and curved wooden cane. Preserve supplied design, not any existing animated widower.'),
 ('barista','Auntie Bo','Plump cheerful Hong Kong woman in her 50s, short curly salt-and-pepper hair, coral blouse, dark-green apron, charcoal trousers.')]
assets=[]
for id,name,desc in source_defs:
    path=f'source/image-ref/{id}.png'
    with Image.open(ROOT/path) as im: dims=list(im.size)
    assets.append({'id':id,'tag':'@'+id,'name':name,'category':'character','description':desc,'source':'user-supplied','media_type':'Image','reference_paths':[], 'candidates':[{'id':'supplied01','path':path,'prompt':'User-provided reference, reused byte-for-byte.','actual_dimensions':dims,'created_at':datetime.now(timezone.utc).isoformat()}],'selected_candidate_id':'supplied01'})
for j in jobs:
    asset={'id':j['id'],'tag':'@'+j['id'],'name':j['name'],'category':j['category'],'description':j['description'],'source':'generated','media_type':'Image','reference_paths':[], 'candidates':[],'selected_candidate_id':None,'image_generation_prompt':j['prompt']}
    if j.get('depends_on'): asset['reference_paths']=[f"assets/{j['depends_on']}/c01.png"] if (ROOT/f"assets/{j['depends_on']}/c01.png").exists() else []
    metadata=ROOT/'assets'/j['id']/'c01.json'
    if metadata.exists():
        candidate=json.loads(metadata.read_text(encoding='utf-8'))
        with Image.open(ROOT/candidate['path']) as im: candidate['actual_dimensions']=list(im.size)
        candidate['id']='c01'
        asset['candidates']=[candidate]
        asset['selected_candidate_id']='c01'
    assets.append(asset)

headers=list(re.finditer(r'^### SCENE (\d+) — (.+?)\s*$',script,re.M))
chapters=[];total_shots=0;elapsed=0
def seconds(t):
    m,s=map(int,t.split(':')); return m*60+s
for idx,h in enumerate(headers):
    body=script[h.end():headers[idx+1].start() if idx+1<len(headers) else script.find('## 6. Music',h.end())].strip()
    tm=re.search(r'⏱ (\d+:\d+)–(\d+:\d+) · \*\*(\d+)s\*\* · (.+?)\*',body)
    assert tm,(h.group(1),'no timing')
    n=int(h.group(1)); duration=int(tm.group(3))
    assert seconds(tm.group(1))==elapsed
    assert seconds(tm.group(2))-elapsed==duration
    shot_headers=list(re.finditer(r'\*\*(\d+)\.(\d+)\*\* · (\d+)–(\d+)s · (.+?)(?=\n|$)',body))
    source_shots=[]
    for si,s in enumerate(shot_headers):
        shot_text=body[s.start():shot_headers[si+1].start() if si+1<len(shot_headers) else body.find('\n---',s.end()) if '\n---' in body[s.end():] else len(body)].strip()
        source_shots.append({'id':f'{n}.{s.group(2)}','start':int(s.group(3)),'end':int(s.group(4)),'source_text':shot_text})
    assert source_shots[0]['start']==0 and source_shots[-1]['end']==duration
    assert all(a['end']==b['start'] for a,b in zip(source_shots,source_shots[1:]))
    total_shots+=len(source_shots)
    cast=re.search(r'\*Cast: (.+?) · Music: (.+?)\*',body)
    chapters.append({'id':f'scene_{n:02d}','chapter_index':n,'title':h.group(2),'duration':duration,'high_level_idea':'Two service-dog brothers from Victoria follow different lives in Hong Kong and reunite by sound, scent and destiny at Victoria Harbour.','scene_summary':h.group(2),'prompt':'','initial_prompt':'','prompt_status':'awaiting_asset_approval','source_scene':body,'source_shots':source_shots,'source_cast':cast.group(1) if cast else '', 'music_cue':cast.group(2) if cast else '', 'location':tm.group(4),'absolute_start':elapsed,'absolute_end':elapsed+duration,'pacing_reason':f'Preserve supplied scene {n}: {len(source_shots)} timed story beats in {duration}s; real-time action and comic anticipation, no slow motion.','tagged_assets':[],'linked_asset_ids':[],'delinked_asset_ids':[],'shots':[],'materials':[],'continuity_references':[],'storyboards':[],'takes':[],'active_take_id':None,'screenshots':[]})
    elapsed+=duration
assert len(chapters)==51 and elapsed==1045 and total_shots==232,(len(chapters),elapsed,total_shots)
project.update({'source_text':raw,'input_mode':'script','language':'English','high_level_idea':chapters[0]['high_level_idea'],'detailed_script':script,'master_prompt_raw':'Preserve supplied screenplay scene and shot timings. Fast-paced, funny, energetic, adventurous and cute. No slow motion. Original characters only. Mr. Leung is completely blind. Optimize using Movi2 golden prompt-library grammar after asset approval.','style':{'medium':"Warm rounded stylized 3D feature animation inspired by Pixar's Up; original supplied characters only",'palette':'Gentle saturated warm colors, teal and cream Hong Kong interiors, gold ranch and harbour light, blue-hour reunion.','lighting':'Soft warm global illumination, painterly skies, motivated lighting, tactile materials and shallow cinematic depth.','constraints':['No Pixar/Disney characters','No slow motion, speed ramps or time stretching','Animals never speak human language or lip-sync','Mr. Leung is completely blind; sunglasses always on; sound/touch/smell cues only','Adult service-dog manners and held slack leads','One main action and at most three featured characters per shot; crowd as soft background','Reference sheets represent single identities, not duplicate actors']},'aspect_ratio':'16:9','duration_mode':'fixed','total_duration_target':1045,'chapter_limits':{'min':4,'max':30},'asset_list':assets,'chapters':chapters,'source_paths':['source/doge-script.md','source/manifest.json'],'script_changes':[],'production_stage':'asset_atelier','production_notes':['51 original scenes, 232 original shot timing ranges preserved. Scene prompts intentionally await explicit asset approval.','The referenced script.md is present as doge-material/doge-script.md. Original copied unchanged.','Source Bible line likening Mr Ko to Carl is treated only as broad shape-language; supplied original Mr Ko design is authoritative.','Captions, map labels and scripted final title are edit-layer graphics, not generated scene text.','Split-screen sequences are separate left/right sub-renders composited within original scene timing.','Scene 43 memory flashes reuse selected original ranch footage at normal speed.','Same-set chains use minimal supported inspected end-state/frame references where useful; unsupported first-frame/reference combinations will not be mixed.','English human dialogue, natural animal sounds, original score cues following script.'],'continuity_bible':{'direction':'Tart travels left to right; Tine right to left. At reunion Tart waits beside seated Leung, Kiki approaches from right with Tine.','blindness':'Never direct Leung to see/look at/visually track anything. Sunglasses stay on in all shots. Left hand holds harness handle; orient to sound, identify by touch, carry bag in free hand.','tart_states':'Harness in scene12,13.3-4,15.3-18,24-27,30.4-5,35.1-3,36.1-3,37-39.3. Collar-only at home. In39.4 clip held brown leash BEFORE removing harness; off duty on held lead39.4-49.','tine_states':'Orange bandana from13.3, lead clipped beneath to collar and held by Kiki in all public scenes. Tail-half in knot until37.5; dropped41.2, recovered42.1-2, between paws43.1 and used44.1-2.','toy':'Head-half orange bill belongs to Tart, tail-half flat blue tail belongs to Tine. High SQUEAK and low HONK; reunited SQUEE-HONK.','bird':'Worn latch misses catch28.3, Jade flies to enclosed garden. Tine never chases or mouths her. Kiki closes/checks latch32.3. Feather on Tine nose32.2 through sneeze33.4.','geography':'Hong Kong left-side road traffic. Clear curb refuge at crossing; no bodily collision. Garden high parapet, stair/lift only. Harbour bench alcove set back from flow, drain at bench end.','reunion':'Both leads slack, held and separated. Harness rests on bench after39.4. Balloon seller holds all balloons; everyone stays on paving.','complexity':'Treat featured speaker/action as foreground focal plane; remaining ensemble soft or offscreen. No tangled multi-agent choreography.'}})
(ROOT/'proposal.json').write_text(json.dumps(project,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'exports'/'scene-breakdown.json').write_text(json.dumps({'runtime_seconds':elapsed,'scene_count':len(chapters),'shot_count':total_shots,'scenes':[{k:c[k] for k in ['id','title','duration','absolute_start','absolute_end','source_cast','source_shots']} for c in chapters]},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'assets':len(assets),'scenes':len(chapters),'shots':total_shots,'seconds':elapsed,'candidates_present':sum(bool(a['candidates']) for a in assets)}))
