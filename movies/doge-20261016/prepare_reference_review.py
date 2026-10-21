"""Read-only visual diagnosis and provider-review packet; no generation or edits."""
import hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
j=json.loads((ROOT/'exports/task-journal.json').read_text(encoding='utf-8'))
take=j['takes']['chapter_37']
folder=ROOT/'exports/scene-37-reference-review';folder.mkdir(parents=True,exist_ok=True)
notes={
'@Mr-Ko':('Higher realism','Dense fine wrinkles, realistic skin shading and individual grey hairs; facial proportions closer to a natural human than the younger cartoon cast.'),
'@granny-wong':('Higher realism','Fine skin creases, age spots/freckles, individual flyaway grey hairs and physically detailed hands/clothing, despite enlarged cartoon eyes.'),
'@granny-lee':('Higher realism','Very detailed skin wrinkles and individual curly hair strands, although round proportions and eyes remain stylized.'),
'@granny-chan':('Higher realism','Fine wrinkles, realistic hair flyaways and hand shading; cartoon proportions are present but surface realism is strong.'),
'@Mr-Leung':('More stylized','Smoother face, simplified nose and cheeks, opaque oversized sunglasses; still detailed hair and cloth. Preserve blindness and glasses.'),
'@Kiki':('More stylized','Large expressive eyes, simplified smooth face and softly rounded features; still detailed hair/cloth. No visual confirmation of provider acceptance.')}
records=[]
for b in take['bindings']:
    a=next(a for a in p['asset_list'] if a['id']==b['asset_id'])
    f=ROOT/b['path'];sha=hashlib.sha256(f.read_bytes()).hexdigest()
    assert sha==b['sha256'],'Submitted source changed: '+b['tag']
    rec={'tag':b['tag'],'name':a['name'],'category':a['category'],'source_path':b['path'],'candidate_id':b['candidate_id'],'submitted_sha256':sha,'provider_binding':b['provider_tag'],'visually_inspected':b['tag'] in notes}
    if b['tag'] in notes:rec.update(visual_realism=notes[b['tag']][0],visual_observations=notes[b['tag']][1])
    records.append(rec)
order=['@Mr-Ko','@granny-wong','@granny-lee','@granny-chan','@Mr-Leung','@Kiki']
font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',24)
small=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',18)
sheet=Image.new('RGB',(1560,1144),(244,240,232));draw=ImageDraw.Draw(sheet)
draw.text((20,12),'Scene 37 — visual comparison only; not a Seedance input',font=font,fill=(46,43,40))
for idx,tag in enumerate(order):
    b=next(b for b in take['bindings'] if b['tag']==tag)
    im=Image.open(ROOT/b['path']).convert('RGB');w,h=im.size
    portrait=im.crop((int(w*.61),0,w,h))
    portrait=ImageOps.contain(portrait,(492,477))
    x=(idx%3)*520;y=56+(idx//3)*544
    sheet.paste(portrait,(x+(520-portrait.width)//2,y))
    draw.text((x+15,y+479),tag,font=font,fill=(46,43,40))
    draw.text((x+15,y+513),notes[tag][0]+' (visual assessment)',font=small,fill=(85,76,65))
sheet.save(folder/'character-realism-comparison.jpg',quality=94)
audit={'created_at':datetime.now(timezone.utc).isoformat(),'project_revision':p['revision'],'scene':37,'provider_error':take.get('error'),'attempt_id':take['attempt_id'],'submitted_at':take['created_at'],'provider_identified_image':None,'findings':'Mr Ko and three grannies have higher naturalistic surface detail than Kiki/Leung. This is an art-direction observation, not proof of which image the provider rejected. All six appear to be original rendered character sheets; no identity/real-person assertion is made.','resolution_policy':'Preserve original selected files and fingerprints. Seek standard provider review of unchanged fictional portraits. No generation retries, image alterations to evade checks, filter disabling or alternate-account submission.','official_error_reference':'https://docs.byteplus.com/th/docs/modelark/error-codes','official_review_workflow':'https://docs.byteplus.com/en/docs/modelark/private-virtual-avatar-library-guide-preview','review_ui':'https://ai.byteplus.com/ark/region:ap-southeast-1/overview','review_ui_status':'Browser signed out; user sign-in and agreement step required before console review controls are accessible.','comparison_image_path':(folder/'character-realism-comparison.jpg').relative_to(ROOT).as_posix(),'assets':records,'source_files_unchanged':True,'new_api_attempts':0,'asset_review':helper.review_state(ROOT,p)}
(folder/'review-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# Scene 37 reference-image review','','The original twelve submitted reference files are unchanged. No new video jobs or image edits were made during this diagnosis.','','## Visual diagnosis','','The strongest visual realism mismatch is Mr Ko and the three grannies. Their skin, hair and wrinkles are rendered more naturally than Kiki and Mr Leung. Seedance did not identify the offending image; these are visual observations, not a confirmed moderation diagnosis.','','![Visual comparison](character-realism-comparison.jpg)','','This contact sheet is for human review only. It must not be submitted as a model input.','','| Character | Visual detail | Original selected image |','|---|---|---|']
for tag in order:
    r=next(r for r in records if r['tag']==tag)
    lines.append('| '+tag+' | '+r['visual_observations']+' | [Unchanged source]('+ (ROOT/r['source_path']).as_posix().replace(' ','%20') +') |')
lines+=['','## Provider review','','The error was `InputImageSensitiveContentDetected.PrivacyInformation`, returned before a task ID was created. The request used twelve references together, so the error cannot be attributed to one image from the returned evidence.','','BytePlus documents a private virtual-portrait library with standard security review and an `Active` status for approved fictional references. The current browser is signed out; sign-in and the visible agreement need to be completed by the user before the console upload/review interface can be used. No moderation settings will be weakened.','','Official workflow: https://docs.byteplus.com/en/docs/modelark/private-virtual-avatar-library-guide-preview','','A separate output-audio refusal on scene 50 remains unresolved and is not explained by character realism.','','## Current production constraints','','Generate only scenes 37–51; 480p, 16:9; no title, subtitles, captions or text boxes. Every vehicle has a driver; buses also passengers. Mr Leung cannot see. Supplied puppy identities unchanged. Exactly eight ordinary balloons, and toy tail half with only rear legs.']
(folder/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({'review_packet':str(folder),'submitted_references':len(records),'human_character_sheets_inspected':len(notes),'sources_unchanged':True,'new_video_attempts':0,'existing_asset_review':helper.review_state(ROOT,p)['status']},indent=2))
