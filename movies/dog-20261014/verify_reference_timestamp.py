"""Verify the exact submitted JPEG; document a clerical timestamp erratum.

No rendered image, prompt, asset binding, accepted attempt, or fingerprint is
rewritten. Historical request provenance remains immutable with explicit errata.
"""
import hashlib,subprocess
from render_movie import ROOT,FF,read,save,now
p=read(ROOT/'project.json');source=p['chapters'][53]
t=next(t for t in source['takes'] if t['id']==source['active_take_id'])
seconds=round(source['duration']-0.2,2)
target=ROOT/'exports/provenance-checks/s13_c04_actual_last_review.jpg'
target.parent.mkdir(parents=True,exist_ok=True)
subprocess.run([str(FF),'-v','error','-threads','2','-ss',str(seconds),'-i',str(ROOT/t['path']),'-frames:v','1','-q:v','2','-y',str(target)],check=True)
actual=hashlib.sha256(target.read_bytes()).hexdigest()
submitted=ROOT/'chapters/s13_c04/screenshots/take_01_review_04.jpg'
assert actual==hashlib.sha256(submitted.read_bytes()).hexdigest()
save(ROOT/'exports/provenance-timestamp-errata.json',{'checked_at':now(),
    'receiving_chapter':'s14_c03','continuity_reference_id':'tine_paving_scale_s13_c04',
    'historically_recorded_source_timestamp':18.8,'correct_source_timestamp':seconds,
    'source_chapter':'s13_c04','source_take':'take_01','source_duration_seconds':source['duration'],
    'submitted_image':submitted.relative_to(ROOT).as_posix(),'submitted_image_sha256':actual,
    'independent_extraction':target.relative_to(ROOT).as_posix(),'exact_image_bytes_match':True,
    'effect':'Clerical provenance timestamp only. The exact correct 7.8-second JPEG was submitted; the numeric source_timestamp field is not sent to Seedance. Accepted prompts, images, takes and their original fingerprints are preserved unchanged.'})
print({'correct_seconds':seconds,'submitted_frame_exactly_verified':True,'creative_inputs_changed':False})
