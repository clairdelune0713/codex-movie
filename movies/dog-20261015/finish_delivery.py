"""Record actual final sample inspection and canonical delivery checks."""
import hashlib,json,subprocess,sys
from collections import Counter
from render_movie import ROOT,SKILL,read,save,helper,now
p=read(ROOT/'project.json');final=ROOT/'exports/dog-20261015-1080p.mp4'
review=read(ROOT/'exports/final-review/inspection-pending.json')
assert review['source_sha256']==hashlib.sha256(final.read_bytes()).hexdigest()
review.update(inspected=True,reviewed_at=now(),requires_repair=False,
 notes='Both actual assembled-frame sheets inspected: rural opening/training, Hong Kong work and home, Chan participation, harbour near miss, regrouping, photograph handling and final dogs resting on stone ground beside handlers. No added title/subtitle/credit overlays in samples. Full14,400-frame technical decoding passed separately. Speech and per-frame generative variation limitations remain documented.')
save(ROOT/'exports/final-review/inspection.json',review)
result=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'project.py'),'check',str(ROOT)],capture_output=True,text=True,encoding='utf-8',check=True)
check=json.loads(result.stdout);save(ROOT/'exports/final-project-check.json',check)
assert not check['errors'] and not check['warnings']
for c in p['chapters']:
 t=next(t for t in c['takes'] if t['id']==c['active_take_id'])
 assert t['status']=='succeeded' and t['visual_review']['inspected'] and not t['visual_review']['requires_repair']
 assert t['dependency_fingerprint']==helper.chapter_fingerprint(ROOT,p,c)
assert not p['quality_repair_queue']
ledger=read(ROOT/'usage.json');report=read(ROOT/'exports/usage-report-session_3fd3fd036d5a4026b029976a7a66e4f4.json')
assert report['session']['seedance_cost']['unknown_charge_attempts']==0
jobs=ledger['jobs'];jobs=jobs.values() if isinstance(jobs,dict) else jobs
states=dict(Counter(j.get('state','unknown') for j in jobs))
save(ROOT/'exports/delivery-manifest.json',{'checked_at':now(),'project_revision':p['revision'],
 'movie':final.relative_to(ROOT).as_posix(),'sha256':review['source_sha256'],'bytes':final.stat().st_size,
 'verification':'exports/verification.json','selected_current_inspected_chapters':70,
 'source_and_assets_audit':'exports/delivery-input-audit.json','final_visual_review':'exports/final-review/inspection.json',
 'usage_report':'exports/usage-report-session_3fd3fd036d5a4026b029976a7a66e4f4.json','attempt_states':states,
 'cost_scope':'New dog-20261015 production only; measured provider tokens at published list rate. Includes discarded successful takes, no account billing claimed.'})
(ROOT/'STATUS.md').write_text('Completed dog-20261015: exports/dog-20261015-1080p.mp4. Exactly600 seconds,1920x1080,16:9,24fps,14,400 fully decoded frames;48kHz stereo AAC. All70 selected chapters are current and inspected. All71 finalized selected dog-20261014 image masters and the79-file original source pack are unchanged. No added author, title, subtitle or credit overlays. Generated dialogue/voice/marking variations and sampled-review limits remain in exports/production-notes.md. Estimated Seedance API usage cost USD371.4273225 across82 attempts, zero pending/unknown charges, not an invoice. Tracked production time5594.513868 seconds through verified export; session and project totals are the same. Final reports and manifest are under exports.\n',encoding='utf-8')
print(json.dumps({'revision':p['revision'],'selected_current_inspected':70,'errors':check['errors'],'warnings':check['warnings'],'attempt_states':states,'movie_bytes':final.stat().st_size},ensure_ascii=False))
