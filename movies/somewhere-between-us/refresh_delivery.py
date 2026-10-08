"""Refresh screenplay/export/audit against the canonical selected final takes."""
import importlib.util,json,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('h','C:/Users/admina/.codex/skills/movi2/scripts/project.py');h=importlib.util.module_from_spec(s);s.loader.exec_module(h)
p=h.read(ROOT/'project.json');q=json.loads(json.dumps(p))
lines=['# SOMEWHERE BETWEEN US｜我們之間','10:00｜Seedance原生720p設定｜1470×630｜21:9｜30fps','改編來源：使用者提供的劇情PDF。狗不說話；人類對白以廣東話指導。作者姓名不出現在影片中。']
for c in q['chapters']:
    start=c['movie_start'];end=c['movie_end']
    lines.extend([f"## {start//60:02d}:{start%60:02d}–{end//60:02d}:{end%60:02d}　{c['title']}",c['scene_summary']])
    for shot in c['shots']:
        lines.append(f"- {start+shot['start']:03d}–{start+shot['end']:03d}秒：{shot['action']}\n  鏡頭：{shot['camera']}。聲音：{shot['audio']}。")
q['detailed_script']='\n\n'.join(lines)+'\n'
q['master_prompt_raw']=q['high_level_idea']+'\n'+'\n'.join(c['scene_summary'] for c in q['chapters'])
h.save(ROOT,p,q,'Refresh final screenplay and production metadata after bounded continuity and audio corrections')
p=h.read(ROOT/'project.json');(ROOT/'screenplay.md').write_text(p['detailed_script'],encoding='utf-8')
for c in p['chapters']:
    (ROOT/'chapters'/c['id']/f"prompt-r{p['revision']:06d}.txt").write_text(c['prompt'],encoding='utf-8')
report=h.report(ROOT,p);h.atomic_write(ROOT/'exports/project-check.json',report)
if report['errors'] or report['warnings']:raise RuntimeError('Final project validation failed')
selected=[]
for c in p['chapters']:
    t=next((t for t in c['takes'] if t['id']==c['active_take_id']),None)
    if not t or t['status']!='succeeded' or not t.get('verification',{}).get('decode_verified'):raise RuntimeError('Missing selected inspected take '+c['id'])
    if t['dependency_fingerprint']!=h.chapter_fingerprint(ROOT,p,c):raise RuntimeError('Selected take stale '+c['id'])
    selected.append({'chapter':c['id'],'take':t['id'],'contact_path':t['verification']['contact_path'],'frames_reviewed':len(t['verification']['samples']),'dependency_current':True})
texts='\n'.join(t['prompt'] for c in p['chapters'] for t in c['takes'] if t['id']==c['active_take_id'])+'\n'+json.dumps(h.read(ROOT/'exports/end-titles.json'),ensure_ascii=False)
assert 'irene' not in texts.lower()
review={'method':'Human-like model visual review of six extracted source frames per selected take, plus extra van-crossing samples and post-composite title previews. Technical full decode of each selected take. Not an every-frame or speech-transcription audit.','selected_takes':selected,'technical_checks':{'requested_api_profile':'720p','native_dimensions':[1470,630],'aspect_ratio':'21:9','source_audio_present':True,'reference_storyboards_sent':0,'author_name_in_selected_prompts_or_titles':False},'corrections':['Replaced ferry take that prematurely placed both dogs together; reduced active references to Tine, handler and empty pier.','Replaced confirmed audio-filter failures in chapters 6,13,21 with location ambience/Foley.','Covered unsolicited generated closing-footer lettering with a dark lower band; native dimensions retained.'],'observed_limits':['Vest lettering, harness shape, heart-patch placement and minor body/costume details vary between some shots.','Opening Hong Kong establishing montage shifts from morning to night before the daytime work scenes.','Human dialogue was directed in Cantonese; exact spoken wording has not been independently transcribed.','Native scene audio and music may vary in tone across cuts; final loudness normalized, with short edge fades.']}
h.atomic_write(ROOT/'exports/visual-review.json',review)
audit=h.read(ROOT/'exports/adaptation-audit.json')
initial=ROOT/'exports/adaptation-audit-initial.json'
if not initial.exists():shutil.copy2(ROOT/'exports/adaptation-audit.json',initial)
audit.update(output_goal=p['output_profile'],author_name_on_screen=False,dialogue_verification='Source dialogue preserved in screenplay and generation directions; no independent speech transcription.',ferry_adjustment='Chapter16 shows Tart leaving; chapter17 then shows Tine on the ferry and an empty pier, preserving the near miss without mixing dog identities.',source_revision=p['revision'])
h.atomic_write(ROOT/'exports/adaptation-audit.json',audit)
print(json.dumps({'revision':p['revision'],'errors':len(report['errors']),'warnings':len(report['warnings']),'selected_inspected_takes':len(selected),'current_dependencies':True}))
