"""Create an independent ten-minute production from unchanged finalized masters.

Never writes to dog-20261014 or SOMEWHERE_BETWEEN_US_READY. No provider calls.
"""
import copy
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parent / 'dog-20261014'
WORKSPACE = ROOT.parent.parent
SKILL = Path('C:/Users/Admin 3/.codex/skills/movi2/scripts')
sys.path.insert(0, str(SKILL))
import project as helper

def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p, d):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

# Action-led allocations, explicitly protecting natural speech and mechanical
# actions. These are new generations, never sped-up versions of the old takes.
DURATIONS = [
    [9,10,7,11,11], [8,7,10,5], [11,5,6,6], [7,7,6,10,8,4],
    [8,9,8], [10,5,15,13], [7,6,5,4], [6,5,7,6], [9,7,7,19,7],
    [12,10,12,12,8], [12,8], [6,14,5,10], [6,6,6,4],
    [7,10,4,14], [5,12,11,10], [11,8,10,9,17,12,7,11]
]
assert sum(map(sum,DURATIONS)) == 600

old = read(OLD/'project.json')
current = read(ROOT/'project.json')
assert current['revision'] == 0, 'Do not initialize an existing production again'
assert helper.review_state(OLD, old)['status'] == 'approved'
source = WORKSPACE/'SOMEWHERE_BETWEEN_US_READY'
source_before = {p.relative_to(source).as_posix():sha(p) for p in source.rglob('*') if p.is_file()}
shutil.copytree(source,ROOT/'source/SOMEWHERE_BETWEEN_US_READY',dirs_exist_ok=True)
shutil.copytree(OLD/'assets',ROOT/'assets',dirs_exist_ok=True)

p = copy.deepcopy(current)
for key in ['input_mode','language','high_level_idea','style','aspect_ratio','continuity_bible',
            'critical_locks','audio_plan','cast_design_overrides','scene_reference_strategy']:
    if key in old:p[key] = copy.deepcopy(old[key])
p.update(source_text=(source/'00_SCRIPT/Somewhere_Between_Us_Revised_Screenplay.txt').read_text(encoding='utf-8'),
         duration_mode='fixed',total_duration_target=600,production_stage='directed',
         source_archive='source/SOMEWHERE_BETWEEN_US_READY',render_status='prepared',
         user_constraints=['NEW independent movie project dog-20261015','Exactly 600 seconds',
             'Generally follow supplied screenplay; only minor production adaptations',
             'Use all finalized asset selections from dog-20261014 unchanged',
             'Up-inspired original stylized 3D animation; no existing Pixar characters',
             'Hong Kong Chinese cast; original Cantonese dialogue',
             'No author, titles, subtitles, credits or end slogan',
             'Fun, engaging and fast pacing; normal-speed action', '1080p 16:9'],
         render_intent={'provider':'Seedance 2.5','resolution':'1080p','aspect_ratio':'16:9',
             'generate_audio':True,'output_format':'mp4','watermark':False,
             'authorization_text':'use movi2 to generate a 10min video; do it 1080p, 16:9',
             'credentials':'Existing workspace .env route: VOLC_ACCESS_KEY, VOLC_SECRET_KEY_RAW, VOLC_PROJECT_NAME, VOLC_ENDPOINT_SEEDANCE_25; values never persisted',
             'fallback_authorized':False},
         script_changes=[{'type':'explicit_duration_override','change':'Create a brisk 600-second version of the 20-minute source. Preserve all 16 scenes and all 107 original Cantonese dialogue entries. Shorten establishing coverage, repeated waits and transition holds; act at normal speed, never accelerate recorded footage.'},
             {'type':'explicit_text_override','change':'Remove source author credit, opening TITLE, END TITLE and production notes from generated frames and speech. Preserve physical prop captions only where scripted.'},
             {'type':'inherited_visual_production_choices','change':'Retain finalized dog-20261014 cast and corrected guide-dog gear, ferry, route geography, and safe harness blocking. These change visual execution, not the story.'}],
         asset_list=copy.deepcopy(old['asset_list']),chapters=[],tool_availability={'jobs_submitted':0},
         prompt_library={'root':'workspace prompt-library','read':['README.md','TEMPLATE.md','sections/09_dialogue.md','shots/intro-interview/03_an-elderly-japanese-scientist-mic-d-and-standing-i.md','shots/scene-01/14_a-man-crosses-a-small-apartment-pulls-out-the-chai.md']})

# Retain the actual historical approval evidence for the identical image set.
# The current user explicitly chose those finalized designs; no new candidate,
# style, image or supplied material is introduced or auto-approved here.
p['asset_review'] = copy.deepcopy(old['asset_review'])
p['asset_reuse_provenance'] = {'source_project_id':old['id'],'source_project_name':old['project_name'],
    'source_revision':old['revision'],'source_review':copy.deepcopy(old['asset_review']),
    'current_user_instruction':'For all the assets. please directly use the finalized ones in project dog-20261014',
    'unchanged_approval_scope':'Exact selected candidate IDs, definitions, relative paths, bytes and style; verified by complete review fingerprint equality. Historical confirmation is retained as historical evidence, not represented as a new chat reply.'}
asset_audit=[]
for a in p['asset_list']:
    selected=helper.selected_media(a)
    f=selected['path']
    asset_audit.append({'tag':a['tag'],'candidate_id':selected['id'],'path':f,
                        'source_sha256':sha(OLD/f),'copy_sha256':sha(ROOT/f),
                        'unchanged':sha(OLD/f)==sha(ROOT/f)})
assert all(x['unchanged'] for x in asset_audit)

def spoken_chars(text): return len(re.findall(r'[\u3400-\u9fffA-Za-z]',text))

absolute=0
dialogue_manifest=[]
for oc in old['chapters']:
    c=copy.deepcopy(oc)
    number=int(c['id'].split('_c')[1])-1
    duration=DURATIONS[c['source_scene']-1][number]
    c.update(duration=duration,absolute_start=absolute,absolute_end=absolute+duration,
        takes=[],active_take_id=None,screenshots=[],materials=[],storyboards=[],selected_storyboard_id=None,
        resolution='1080p',prompt_status='directed for new 600-second production',
        pacing_reason='Brisk complete action and natural Cantonese speech; shorten transitional holds and redundant establishing coverage, keep every source dialogue line. This action unit is '+str(duration)+' seconds at normal speed.')
    c.pop('continuity_references',None)
    c.pop('prompt_refinements',None)
    blocks={b['source_block_index']:b for b in c['planning_source_blocks']}
    # Speech gets an explicit floor before remaining time is allocated to action.
    # A brisk conversational 4.8 syllables/s is the planning ceiling, never an
    # instruction to accelerate or squeeze speech in the actual generation.
    shots=copy.deepcopy(c['shots'])
    if c['id']=='s10_c05':
        shots=[{'start':0,'end':duration,'camera':'50mm compact listening-group two-shot',
            'action':'Meeting arrangement agreed while Tart rests under the chair; paw twitches in the same frame. '+
                ' '.join('EXACT DIALOGUE — '+b['cue']+': 「'+b['text']+'」' for b in c['planning_source_blocks'] if b['type']=='dialogue'),
            'source_block_indices':list(blocks),'audio':'Natural Cantonese exchange.','end_state':'Arrangement agreed.'}]
    floors=[]
    weights=[]
    for shot in shots:
        spoken=[blocks[i] for i in shot.get('source_block_indices',[]) if i in blocks and blocks[i]['type']=='dialogue']
        floor=max(1.1,sum(spoken_chars(b['text']) for b in spoken)/4.8 + (0.25*len(spoken) if spoken else 0))
        floors.append(floor)
        weights.append(max(0.1,(shot['end']-shot['start'])-floor))
    assert sum(floors)<=duration+0.001,(c['id'],floors,duration)
    remaining=duration-sum(floors)
    lengths=[f+remaining*w/sum(weights) for f,w in zip(floors,weights)]
    t=0.0
    timeline=[]
    for i,(shot,length) in enumerate(zip(shots,lengths)):
        end=duration if i==len(shots)-1 else round(t+length,2)
        shot.update(start=t,end=end)
        timeline.append(f"Shot {i+1} ({t:g}-{end:g}s): "+('Hard cut. ' if i else '')+shot['camera']+'.\n'+shot['action'])
        t=end
    c['shots']=shots
    # Tighten only the especially short montage transitions into readable paired
    # inserts. All underlying source events and dialogue remain archived.
    if c['id']=='s04_c06':
        c['shots']=[{'start':0,'end':2,'camera':'40mm two fast matched inserts',
            'action':'Hard cut from Tart clearing the stroller at normal walking pace to Tine staying beneath the invited hand. Both actions begin already in progress.',
            'audio':'Paws and chair contact; score ends.','end_state':'Tine still under the invited hand.'},
            {'start':2,'end':4,'camera':'65mm reveal within centre',
            'action':'The newspaper rises before Uncle Chan; Tine notices and his wag softens.',
            'audio':'Paper rustle; no dialogue.','end_state':'Wag softens, hard cut into unscored street.'}]
    if c['id']=='s10_c05':
        # Do not spend a separate second on a sleeping-paw reaction while a
        # complete original spoken exchange needs the available eight seconds.
        c['shots']=[{'start':0,'end':8,'camera':'50mm compact listening-group two-shot',
            'action':'Ah Ming and Bo exchange the original meeting arrangement while Tart rests under his chair; one paw twitches in the same composition. '+
                ' '.join('EXACT DIALOGUE — '+b['cue']+': 「'+b['text']+'」' for b in c['planning_source_blocks'] if b['type']=='dialogue'),
            'audio':'Natural Cantonese conversational exchange; quiet room.','end_state':'Meeting arrangement agreed.'}]
    timeline=[f"Shot {i+1} ({s['start']:g}-{s['end']:g}s): "+('Hard cut. ' if i else '')+s['camera']+'.\n'+s['action'] for i,s in enumerate(c['shots'])]
    original=c['prompt']
    # Preserve all demonstrated identity, gear and geography locks from the
    # final source prompt, replacing only the authoritative output/timeline.
    original=original.replace('480p','1080p')
    original=re.sub(r'(OUTPUT SETTINGS\n).*?(?=\n\n)',
        lambda m:m[1]+f"{duration} seconds, 16:9, native 1920x1080, real-time action, {len(c['shots'])} timed shots. Short complete beats and clean cuts. No slow motion or playback acceleration.",original, count=1,flags=re.S)
    assert '\nTIMELINE\n' in original,c['id']
    head=original[:original.index('\nTIMELINE\n')]
    tail=original[original.index('\nPHYSICS'):] if '\nPHYSICS' in original else original[original.index('\nAUDIO AND FINISH'):]
    tail=re.sub(r'\b'+str(oc['duration'])+r' seconds total\b',str(duration)+' seconds total',tail)
    c['prompt']=head+'\nTIMELINE\n'+'\n\n'.join(timeline)+'\n\n'+tail
    c['prompt']+='\nPACING\nEnter actions already prepared. Let foreground action, dialogue and reaction overlap naturally. Keep the original jokes, causality and small reciprocal dog gestures readable. Speech is natural Hong Kong Cantonese, never sped up. No extra scenic hold between beats.'
    c['initial_prompt']=c['prompt']
    c['handoff']={'method':'Unchanged approved references plus explicit written geography; no automatic prior-clip input',
        'previous_end_state':p['chapters'][-1].get('end_state') if p['chapters'] else 'Opening action',
        'next_start_state':c.get('first_frame'),'cut':'Hard cut; preserve native dialogue and action sounds',
        'reason':'New camera/action coverage uses stable approved setting; add an inspected generated frame only if a demonstrated continuity error requires it.'}
    p['chapters'].append(c)
    for b in c['planning_source_blocks']:
        if b['type']=='dialogue':dialogue_manifest.append({'chapter':c['id'],'source_scene':c['source_scene'],**b})
    absolute+=duration
assert absolute==600
assert len(dialogue_manifest)==107
assert helper.review_manifest(ROOT,p)['fingerprint']==helper.review_manifest(OLD,old)['fingerprint']
assert helper.review_state(ROOT,p)['status']=='approved'

write(ROOT/'exports/source-integrity-before.json',source_before)
write(ROOT/'exports/finalized-asset-copy-audit.json',{'assets':asset_audit,'all_71_selected_assets_identical':True,
    'source_review_fingerprint':old['asset_review']['fingerprint'],'new_review_fingerprint':helper.review_manifest(ROOT,p)['fingerprint']})
write(ROOT/'exports/dialogue-manifest.json',dialogue_manifest)
write(ROOT/'exports/director-audit.json',{'chapters':len(p['chapters']),'duration_seconds':600,
    'all_16_scenes_preserved':True,'original_dialogue_entries':107,'dialogue_rewrites':0,
    'titles_credits_excluded':True,'new_generations_required':True,'old_video_takes_reused':False})
source_after={f.relative_to(source).as_posix():sha(f) for f in source.rglob('*') if f.is_file()}
assert source_before==source_after
write(ROOT/'exports/source-integrity-after.json',{'all_original_files_unchanged':True,'file_count':len(source_after)})

lines=['# dog-20261015 - 10:00 production screenplay','',
       'Native 1080p, 16:9. All sixteen source scenes and 107 original dialogue entries. Original source preserved separately. No titles, subtitles, author or credits.','']
for c in p['chapters']:
    lines.extend([f"## {c['absolute_start']//60:02}:{c['absolute_start']%60:02} - {c['absolute_end']//60:02}:{c['absolute_end']%60:02} | {c['id']} | {c['title']}",'',c['prompt'],''])
p['detailed_script']='\n'.join(lines)
(ROOT/'exports/director-script.md').write_text(p['detailed_script'],encoding='utf-8')
write(ROOT/'proposal-directed.json',p)
print(helper.save(ROOT,current,p,'Create independent exact ten-minute 1080p production; reuse identical explicitly chosen finalized masters and their historical approval'))

for name in ['seedance_transport.py','render_movie.py','review_takes.py','record_review.py']:
    text=(OLD/name).read_text(encoding='utf-8-sig')
    if name!='seedance_transport.py':
        text=text.replace('480p','1080p').replace('854,480','1920,1080').replace('854x480','1920x1080').replace('native_480p','native_1080p').replace('2026101400','2026101500')
        text=text.replace("Decimal('10.70')","Decimal('11.70')").replace('USD 10.70/M','USD 11.70/M')
    text=text.replace('dog-20261014 | actual','dog-20261015 | actual')
    (ROOT/name).write_text(text,encoding='utf-8')
(ROOT/'tools').mkdir(exist_ok=True)
shutil.copy2(OLD/'tools/ffmpeg.exe',ROOT/'tools/ffmpeg.exe')
for name in ['provider-asset-bindings.json','pricing-evidence.json']:
    shutil.copy2(OLD/'exports'/name,ROOT/'exports'/name)
print('Prepared 71 unchanged masters, 70 new native 1080p chapters, 107 unchanged dialogue entries, 600 seconds.')
