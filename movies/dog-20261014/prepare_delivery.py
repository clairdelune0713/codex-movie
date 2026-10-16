"""Register the reviewed director script and export current delivery inputs."""
import json,subprocess,sys
from render_movie import ROOT,SKILL,helper,read,save
p=read(ROOT/'project.json')
for c in p['chapters']:
    t=next((t for t in c['takes'] if t['id']==c.get('active_take_id')),None)
    assert t and t['status']=='succeeded' and t['visual_review']['inspected'] and not t['visual_review']['requires_repair'],c['id']
    assert t['dependency_fingerprint']==helper.chapter_fingerprint(ROOT,p,c),c['id']
assert len(p['chapters'])==70 and sum(c['duration'] for c in p['chapters'])==1200
q=json.loads(json.dumps(p))
elapsed=0;parts=[]
for c in q['chapters']:
    parts.append('CHAPTER %02d | %s | %04d-%04d seconds\n\n%s'%(c['chapter_index'],c['id'],elapsed,elapsed+c['duration'],c['prompt']))
    elapsed+=c['duration']
q['detailed_script']='\n\n'.join(parts)
q['production_stage']='assembling'
q['render_status']='awaiting_assembly'
q.setdefault('script_changes',[]).append({'type':'final_camera_and_sound_restaging',
    'reason':'Preserve all 107 supplied dialogue entries in order while using original-cast cabin coverage with child voice offscreen, tight physical-photo recognition coverage, low dog/shoe framing, and conventional duplicate-child reframing. Wordless forecourt uses native same-location harbour ambience/horn instead of an unrequested possible adlib. These are shot and sound choices, not story rewrites.'})
errata=read(ROOT/'exports/provenance-timestamp-errata.json')
q.setdefault('provenance_errata',[]).append(errata)
q.setdefault('production_quality_notes',[]).append('Actual sampled-frame review completed for all 70 selected clips, including local crop and native-ambience edits. Accepted render fingerprints are preserved; one clerical reference timestamp is corrected transparently in exports/provenance-timestamp-errata.json, with independent exact-JPEG verification. Minor generated group wardrobe/pose variation and ASR normalization remain; no claim of frame-perfect animation or word-perfect synthesized voice.')
print(helper.save(ROOT,p,q,'Prepare reviewed 20-minute director script, local edits and transparent provenance errata'))
(ROOT/'exports/director-script-current.md').write_text(q['detailed_script'],encoding='utf-8')
for command in ('check','render-ready','export'):
    result=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'project.py'),command,str(ROOT)],capture_output=True,text=True,encoding='utf-8')
    if result.returncode:raise RuntimeError(command+' failed: '+result.stdout[-1500:])
    if command=='check':
        result_data=json.loads(result.stdout);print({'check_errors':result_data['errors'],'check_warnings':result_data['warnings']})
    else:print(result.stdout[-1000:])
(ROOT/'STATUS.md').write_text('All 70 chapters selected and inspected; exact 1200-second 480p 16:9 movie is being assembled.\nNo final file is claimed until full decoding, dimensions, duration, frame count and audio checks pass.\nSee project.json, exports/task-journal.json, exports/director-script-current.md and usage.json.\n',encoding='utf-8')
