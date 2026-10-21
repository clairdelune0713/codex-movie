"""Preserve failed attempts and prepare accurate resumable review files."""
import copy,hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
import usage
from render_finale import payload,read,save,record
p=read(ROOT/'project.json');q=copy.deepcopy(p)
j=read(ROOT/'exports/task-journal.json')
q['stage']='provider_review_required';q['render_status']='blocked_by_provider_moderation'
q['provider_review_required']=True
q['provider_review_notes']={'checked_at':datetime.now(timezone.utc).isoformat(),'scope':'Scenes 37–51 only, 305 seconds, 480p 16:9; no title/subtitle/caption/text box','attempts':[{'chapter_id':t['chapter_id'],'attempt_id':t['attempt_id'],'task_id':t.get('task_id'),'error':t.get('error'),'status':t['status']} for t in j['takes'].values()],'usable_video_files':0,'further_submissions':'Stopped pending provider review. Do not disable moderation, alter rejected inputs to evade it, or silently change provider/account.','official_review_workflow':'https://docs.byteplus.com/en/docs/modelark/private-virtual-avatar-library-guide-preview','capability_checks':'Current account has AIGC groups, but the previously approved identical Ko resource is not available in this configured account/project. No existing regional staging bucket was available. No assets uploaded to an alternative service and no bucket or authorization-policy changes made.'}
print(helper.save(ROOT,p,q,'Preserve provider moderation failures; halt further POSTs pending provider review'))
p=read(ROOT/'project.json')
pack=ROOT/'exports/finale-render-package-v02-16x9-no-text';pack.mkdir(parents=True,exist_ok=True)
chapters=[]
for c in p['chapters'][36:51]:
    _,bindings,compiled,size=payload(p,c,'<runtime-verified-seedance-endpoint>')
    f=pack/(c['id']+'-director.txt');f.write_text(c['prompt'],encoding='utf-8')
    cf=pack/(c['id']+'-compiled.txt');cf.write_text(compiled,encoding='utf-8')
    chapters.append({'id':c['id'],'scene':c['chapter_index'],'duration':c['duration'],'prompt_path':f.relative_to(ROOT).as_posix(),'compiled_prompt_path':cf.relative_to(ROOT).as_posix(),'bindings':bindings,'dependency_fingerprint':helper.chapter_fingerprint(ROOT,p,c),'request_bytes':size})
save(pack/'manifest.json',{'status':'prepared_provider_review_required_not_generated','source_revision':p['revision'],'scope':p['render_scope'],'no_title_subtitle_text_box':True,'no_captions_or_graphic_overlays':True,'asset_review':helper.review_state(ROOT,p),'external_transfer_authorized':True,'chapters':chapters,'provider_review':p['provider_review_notes']})
rows='\n'.join(f"| {c['scene']} | {p['chapters'][c['scene']-1]['title']} | {c['duration']} s | [{c['id']} prompt]({c['id']}-director.txt) |" for c in chapters)
(pack/'README.md').write_text('''# doge-20261016 — scenes 37–51 — current delivery plan

Prepared render package, not a generated movie. Latest requested settings: **480p, 16:9**. Fifteen scenes total **305 seconds (5:05)**. No titles, subtitles, captions, text boxes or graphic overlays. Scenes 1–36 remain outside the authorized render scope. The earlier 21:9 package and its text-graphics previews are superseded and will not be assembled.

All approved character and prop images remain unchanged. Scene 43 uses the two supplied puppy references within its own memory flashes. Exactly eight ordinary balloons are specified. Toy tail half has only two rear legs. All vehicles have drivers; buses have driver and passengers. Scene 37 specifies a ferry captain at controls and passengers. Leung is blind throughout, with opaque sunglasses and sound/touch/smell/memory acting. Original cartoon cast and normal-speed motion.

Source scene divisions and durations remain unchanged. Per latest user instruction, scene 50 is now nine seconds of moving harbour closing imagery, with no title, map labels, parchment graphics or text. Spoken dialogue and the ranch postcard stinger remain.

| Scene | Scene name | Length | Director prompt |
|---|---|---:|---|
'''+rows+'''

## Current provider result

External transfer was explicitly authorized. Runtime authentication succeeded using the workspace credentials and the intentionally empty project-name value. The configured Seedance 2.5 endpoint matched the accessible running endpoint.

- Scene 37: submission rejected with `InputImageSensitiveContentDetected.PrivacyInformation`; no task was created.
- Scene 50: accepted as `cgt-20261016173437-dr5g1`, then failed with `OutputAudioSensitiveContentDetected.PolicyViolation`.
- No usable video file was returned. Other character-scene jobs were not submitted. The full stitch remains incomplete.

Further POSTs are paused pending provider review. No moderation settings were changed and no rejected content was retried through altered imagery or another account. The official private fictional-portrait approval workflow was investigated, but the current account did not have the earlier byte-identical approved Ko resource or available existing regional staging storage. No new storage or policy was created.

Provider documentation: https://docs.byteplus.com/en/docs/modelark/private-virtual-avatar-library-guide-preview

The script, current fifteen prompts, binding hashes, attempt journal, approved assets and local no-text assembler are retained. The assembler requires successful visually accepted takes before producing a movie; it does not create placeholder output. API usage and charges for failed attempts remain pending because no billing record or usage units were returned. The production session stays open for resumption after provider review.
''',encoding='utf-8')
# All failed attempts remain recorded; no unsupported zero-dollar billing claim.
ledger=read(ROOT/'usage.json');session=next(s['id'] for s in ledger['sessions'] if not s.get('ended_at'))
for t in j['takes'].values():
    rec={'attempt_id':t['attempt_id'],'chapter_id':t['chapter_id'],'take_id':t['id'],'state':t.get('submission_state') if t.get('submission_state')=='rejected' else t['status'],'model':t['model'],'resolution':'480p','duration_seconds':t['duration'],'reference_video_seconds':0,'usage':t.get('provider_usage',{}),'cost':{'kind':'unknown','basis':'Provider rejected/failed the attempt and returned no billing amount or completion usage. No successful output; charge not verified. Awaiting provider billing/review.'}}
    if t.get('task_id'):rec['task_id']=t['task_id']
    f=ROOT/'exports/usage-records'/(t['attempt_id']+'.json');save(f,rec)
    import subprocess
    subprocess.run([sys.executable,'-X','utf8','C:/Users/Admin 3/.codex/skills/movi2/scripts/usage.py','record',str(ROOT),'--session',session,'--from',str(f)],check=True,capture_output=True)
ledger=read(ROOT/'usage.json')
save(ROOT/('exports/usage-report-'+session+'.json'),usage.summary(ledger,session,datetime.now(timezone.utc)))
errors,warnings=helper.validate(ROOT,p)
save(pack/'validation.json',{'errors':errors,'in_scope_warnings':[w for w in warnings if not any('chapter_'+str(n).zfill(2)+':' in w for n in range(1,37))],'outside_scope_planning_warnings':len(warnings),'asset_review':helper.review_state(ROOT,p),'generation_attempts':len(ledger['jobs']),'usable_videos':0,'source_hashes_verified':all(hashlib.sha256((ROOT/b['path']).read_bytes()).hexdigest()==b['sha256'] for c in chapters for b in c['bindings'])})
print(json.dumps({'package':str(pack),'project_revision':p['revision'],'provider_review_required':True,'attempts':len(ledger['jobs']),'usable_videos':0,'validation_errors':len(errors)},indent=2))
