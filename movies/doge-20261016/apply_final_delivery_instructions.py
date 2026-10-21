import copy,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=copy.deepcopy(p)
q['aspect_ratio']='16:9';q['render_scope']['aspect_ratio']='16:9'
q['external_transfer_authorization']={'confirmed_at':datetime.now(timezone.utc).isoformat(),'user_confirmation':'yes please proceed. also please note: no title, no subtitle, no text box','context':'In direct reply to request to upload selected reference images and prompts to BytePlus Seedance using workspace credentials and generate scenes 37–51.','destination':'https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks','latest_aspect_ratio':'16:9','empty_project_value_user_confirmed':True}
q['render_constraints']=[s.replace('21:9','16:9') for s in q['render_constraints']]+['No title, subtitles, captions, text boxes or graphic overlays. Native moving video only.']
q.setdefault('script_changes',[]).append('Latest user instruction: remove all title/subtitle/caption/text-box overlays. Scene 50 remains nine seconds of moving harbour closing imagery; omit its map/lettering/title. Preserve scene numbers and other story beats. Latest aspect ratio 16:9 supersedes 21:9.')
for c in q['chapters'][36:51]:
    c['prompt']=c['prompt'].replace('21:9 ultrawide','16:9 widescreen').replace('21:9','16:9').replace('**— THE END —**','')
    c['prompt']+='\nFINAL DELIVERY LOCK\nMoving cinematic 3D animation fills the entire 16:9 frame. No opening title, ending title, subtitles, captions, text boxes, speech bubbles, watermarks, reference-sheet labels or graphic overlays. Dialogue is heard only. No lettering over the scene. This latest delivery instruction overrides source editorial caption/title directions.'
    if c['chapter_index']==50:
        c['shots']=[{'start':0,'end':6,'action':'Camera rises and pulls away from the small reunion group beside the harbour bench to show the glowing waterfront and skyline. Continuous normal-speed camera movement; people/dogs remain tiny background figures.','camera':'24mm aerial crane rise','status':'directed'},{'start':6,'end':9,'action':'Continue the moving aerial view over golden harbour water and painterly sky. Water ripples and flags flutter naturally. No graphic transition, map, title, subtitle, caption or text box.','camera':'24mm gentle forward aerial movement','status':'directed'}]
        c['prompt']='''SCENE CONTEXT
Scene 50, the nine-second closing harbour vista after the brothers’ next-Friday reunion, before the ranch postcard stinger.

OUTPUT / FORMAT
Exactly 9 seconds, native 480p, 16:9, normal-speed animated cinematic movement. One continuous aerial crane shot. Warm rounded feature-film-quality original 3D animation, tactile materials, pink-and-gold painterly sunset, teal water, gentle cinematic depth. Original cast only; no franchise characters or costumes.

ACTIVE APPROVED REFERENCE
@victoria-harbour defines Tsim Sha Tsui promenade, Clock Tower at landward left, silver horizontal rail, wooden bench, terracotta paving, Hong Kong Island skyline across water and warm sky. Adapt cinematic framing, never show a reference plate or white studio. The reunion group is tiny distant original human/dog silhouettes by the bench, no new close-up identities.

LOCATION / FIRST FRAME
Begin above and behind the little reunion group beside the landward bench, cream and fox-red dogs side by side at people’s feet, water beyond the rail. Keep horizon level and physically stable.

TIMELINE
SHOT 1 (0–6s). Continuous 24mm crane rise and pullback from tiny group to the harbour and twinkling skyline; real moving scene, rippling water, fluttering foliage, ordinary strolling visitors.
SHOT 2 (6–9s). Seamlessly continue the normal-speed aerial glide over sunset harbour and painterly pink clouds. Continue water movement; maintain geography and light. No graphic transition or frozen padding.

AUDIO
Original warm orchestral waltz resolves quietly with the SQUEE-HONK motif, harbour breeze and water. No dialogue or voice-over. No copied film recording. Preserve natural-speed motion, no slow motion or speed ramps.

LOCKS / END
Full-frame moving harbour only. No title, subtitle, captions, map labels, text boxes, speech bubbles, credits, logos or overlay lettering of any kind. No map or parchment transition. Do not introduce road vehicles or close boats; any visible distant vessel must have a human captain at controls and passengers. End still moving over the glowing harbour for a clean cut to the six-second ranch stinger.'''
        c['assembly_mode']='native_video'
    for s in c['shots']:s['action']=s['action'].replace('**— THE END —**','').strip()
print(helper.save(ROOT,p,q,'Record explicit BytePlus transfer approval; final 16:9 and no title/subtitle/caption/text-box instructions'))
# Runtime code is task-local; preserve old generated graphics separately but never use them.
r=ROOT/'render_finale.py';s=r.read_text(encoding='utf-8').replace('21:9','16:9').replace('(992,432)','(854,480)').replace('992x432','854x480').replace('native_480p_21x9','native_480p_16x9')
r.write_text(s,encoding='utf-8')
a=ROOT/'assemble_finale.py';s=a.read_text(encoding='utf-8')
s=s.replace('W,H,FPS=992,432,24','W,H,FPS=854,480,24')
s=s.replace("work=ROOT/'exports/finale-finishing-v01'","work=ROOT/'exports/finale-finishing-v02-no-text'")
s=s.replace('    graphics(work)\n','')
s=s.replace("        print('Prepared local screenplay captions, animated map/title graphics; no movie rendered.');return","        print('No graphics used: latest user requested no title, subtitles or text boxes.');return")
start=s.index('        if n in (37,49):');end=s.index("        cmd+=['-af'",start)
s=s[:start]+"        cmd+=['-vf',common,'-map','0:v:0','-map','0:a:0']\n"+s[end:]
s=s.replace('480p-21x9.mp4','480p-16x9.mp4').replace("'requested_aspect_ratio':'21:9'","'requested_aspect_ratio':'16:9'")
s=s.replace('Original generated animation/audio; exact script captions and animated map/title composited locally. Native 992x432 is provider 480p ultrawide profile; no time stretching.','Original generated animation/audio only; no title, subtitles, captions, text boxes or graphic overlays. Native 854x480 480p widescreen; no time stretching.')
a.write_text(s,encoding='utf-8')
