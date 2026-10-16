"""Keep Tine beside Chan's shoe and remove duplicated dog from group coverage."""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as h
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=json.loads(json.dumps(p))
source=next(c for c in p['chapters'] if c['id']=='s13_c04');t=next(t for t in source['takes'] if t['id']==source['active_take_id'])
assert t['visual_review']['inspected'] and not t['visual_review']['requires_repair']
assert t['dependency_fingerprint']==h.chapter_fingerprint(ROOT,p,source)
for c in q['chapters']:
    if c['id']=='s14_c03':
        c['prompt']='本段人物不說話，只有海風、輕微衣服聲及環境聲。Bo用掌心手勢同眼神提議喺呢度等，其他人點頭回應，沒有新增台詞。\n\nGROUND-LEVEL TINE: Brown Tine lowers his chest and belly onto the STONE PAVING beside the OUTSIDE of Chan BLACK SHOE. The shoe sole and dog paws share the same paving plane. Chan hand reaches DOWN from his seated knee to the dog shoulder below. First shot is a LOW CAMERA 25cm above the paving, showing dog, black shoe, trouser shin and vertical bench leg; the bench SEAT surface is above the crop. Dog stays on paving in the group wide too. No dog occupies any human seat or lap.\n\n'+c['prompt']
        c['prompt']=c['prompt'].replace('Four paws on floor except brief scripted attempted lap gag.','Four paws and resting belly on the stone paving throughout this quiet scene.')
        start=c['prompt'].index('@NearerSeatingBay:');end=c['prompt'].index('\n',start)
        c['prompt']=c['prompt'][:start]+'@NearerSeatingBay: Outdoor environment architecture and daylight ONLY. Low planters, stone paving, ordinary bench, harbour railing. Ignore prepopulated subjects; all dog and human identities/positions come from separately bound masters and the timeline.'+c['prompt'][end:]
        c['shots'][0]['camera']='65mm low medium 25cm above paving: dog shoulder beside black shoe, hand reaches down, vertical bench leg behind; seat surface outside upper crop'
        c['shots'][0]['action']+=' Tine whole body and paws remain on the stone paving; shoulder below Chan knee, beside outside of black shoe, not on bench.'
        c['prompt']=c['prompt'].replace('65mm hand/shoulder low medium.','65mm low medium at 25cm above paving: Tine shoulder and whole body beside Chan black shoe, trouser shin and vertical bench leg behind; bench seat above crop.')
        c['prompt']=c['prompt'].replace('Bo asks the group if they would rather meet Ah Ming here.','Bo uses a small open-palm gesture and questioning look to suggest meeting Ah Ming here without speaking.')
        c['continuity_references']=[{'id':'tine_paving_scale_s13_c04','path':f"chapters/s13_c04/screenshots/{t['id']}_review_04.jpg",'media_type':'Image','role':'reference_image','source_chapter_id':source['id'],'source_take_id':t['id'],'source_sha256':hashlib.sha256((ROOT/t['path']).read_bytes()).hexdigest(),'source_timestamp':round(source['duration']-0.2,2),'inspected':True,'reason':'Carry ONLY brown Tine adult scale and paws/body ON STONE PAVING next to human shoes, BELOW bench seat height. Ignore bowl, water, drinking action, May legs identity and prior framing. New action is lying beside the OUTSIDE of Chan black shoe, his hand reaching down to shoulder. No dog on seat or lap. Orange lead remains held by seated May.'}]
        c.setdefault('prompt_refinements',[]).append({'reason':'Actual first take put Tine fully on human bench. Use low shoe-level camera, environment-only plate role and inspected earlier paving-height frame; retain original quiet choice and group nod.'})
    if c['id']=='s16_c07':
        for tag,aid in (('@TartOffDuty','asset_tart_off_duty'),('@TineAdult','asset_tine_adult')):
            c['tagged_assets'].remove(tag);c['linked_asset_ids'].remove(aid)
            c['prompt']='\n'.join(line for line in c['prompt'].split('\n') if not line.startswith(tag+':'))
        c['prompt']='HUMAN CHOICE COVERAGE: Only the original human characters are visible in this chapter. The TWO dogs stay on paving below the camera crop, and the following chapter shows their rest. Shot 1: clear audible soft Cantonese from Chan at 1-3 seconds: 我想坐多陣. Bo listens, then answers at 4-7 seconds: 好，我哋一陣一齊返. Mouths belong to their own voices. Shot 2 is seated HUMANS from WAIST UP only as Chan makes room for the ONE Lok and his ONE mother. Keep all adult dogs outside bottom of frame throughout; no animal appears on a bench or in the human group portrait.\n\n'+c['prompt']
        c['shots'][0]['camera']='65mm Chan/Bo seated two-shot above waist, dogs outside bottom crop'
        c['shots'][0]['action']+=' Chan first line is clearly audible at 1-3s before Bo reply at 4-7s; no overlapped or omitted first line.'
        c['shots'][1]['camera']='65mm seated human waist-up group medium, Chan makes room for single Lok and mother; dogs below crop'
        c['prompt']=c['prompt'].replace('65mm Chan/Bo two-shot.','65mm seated Chan/Bo two-shot above waist; dogs below crop. Chan speaks clearly at 1-3s; Bo replies at 4-7s.')
        c['prompt']=c['prompt'].replace('Hard cut to 40mm inclusive bench wide.','Hard cut to 65mm seated HUMAN WAIST-UP group medium, bench seat and dogs below crop; one Lok and his mother join Chan.')
        c.setdefault('prompt_refinements',[]).append({'reason':'Actual first take duplicates cream Tart in group wide and first Chan line absent from local ASR evidence. Keep group resolution as human waist-up coverage, dogs offscreen on paving, and explicitly schedule both original spoken lines. Next final chapter retains actual two-dog ground-level rest.'})
print(h.save(ROOT,p,q,'Keep Tine at shoe level and frame final human choice without duplicated dogs'))
