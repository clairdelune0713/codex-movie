"""Integrate approved creative references and freeze a current local package.

This does not submit a replacement for a safety-rejected generation.
"""
import copy,hashlib,json,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
from render_finale import payload,read,save
p=read(ROOT/'project.json');q=copy.deepcopy(p)
assert helper.review_state(ROOT,p)['ready'],'Latest image review must be explicitly approved'
assert p.get('provider_review_required') is True,'Do not silently clear existing provider refusal'
changed={'@Mr-Ko':'cartoon_c01','@granny-wong':'generated_c02','@granny-lee':'generated_c02','@granny-chan':'generated_c02'}
for tag,cid in changed.items():
    a=next(a for a in p['asset_list'] if a['tag']==tag)
    assert a['selected_candidate_id']==cid
affected=[];color_fixes=[]
for c in q['chapters'][36:51]:
    tags={a['tag'] for a in helper.active_assets(q,c)}
    using=sorted(tags&set(changed))
    if using:
        c['approved_character_variant_bindings']={tag:changed[tag] for tag in using}
        affected.append({'scene':c['chapter_index'],'chapter_id':c['id'],'revised_characters':using})
    # Correct a prompt-only mismatch discovered by inspecting the selected toy sheets.
    # Original screenplay and supplied images remain untouched.
    prior=c['prompt']
    c['prompt']=c['prompt'].replace('worn brown platypus plush','worn blue platypus plush').replace('whole brown platypus plush','whole blue platypus plush')
    if c['prompt']!=prior:color_fixes.append(c['chapter_index'])
q['stage']='approved_cartoon_assets_provider_review_required'
q['render_status']='blocked_by_provider_moderation'
q['approved_cartoon_asset_integration']={'at':datetime.now(timezone.utc).isoformat(),'approval_review_id':p['asset_review']['id'],'user_confirmation':p['asset_review']['confirmation'],'candidates':changed,'affected_requested_scenes':affected,'prompt_color_corrections':color_fixes,'current_delivery':'Scenes 37–51 only, 305 seconds, 480p 16:9, no title/subtitle/caption/text box','provider_review_cleared':False,'new_generation_attempts':0}
print(helper.save(ROOT,p,q,'Integrate approved cartoon variants into requested scene bindings; match blue toy reference; retain provider review hold'))
p=read(ROOT/'project.json')
pack=ROOT/'exports/finale-render-package-v03-approved-cartoon';pack.mkdir(parents=True,exist_ok=False)
chapters=[]
for c in p['chapters'][36:51]:
    body,bindings,compiled,size=payload(p,c,'<runtime-verified-seedance-endpoint>')
    f=pack/(c['id']+'-director.txt');f.write_text(c['prompt'],encoding='utf-8')
    cf=pack/(c['id']+'-compiled.txt');cf.write_text(compiled,encoding='utf-8')
    bound={b['tag']:b['candidate_id'] for b in bindings if b.get('tag') in changed}
    assert all(cid==changed[tag] for tag,cid in bound.items())
    assert body['ratio']=='16:9' and body['resolution']=='480p'
    chapters.append({'id':c['id'],'scene':c['chapter_index'],'duration':c['duration'],'prompt_path':f.relative_to(ROOT).as_posix(),'compiled_prompt_path':cf.relative_to(ROOT).as_posix(),'bindings':bindings,'dependency_fingerprint':helper.chapter_fingerprint(ROOT,p,c),'request_bytes':size,'approved_cartoon_candidates':bound})
assert len(chapters)==15 and sum(c['duration'] for c in chapters)==305
all_bindings=[b for c in chapters for b in c['bindings']]
assert all(hashlib.sha256((ROOT/b['path']).read_bytes()).hexdigest()==b['sha256'] for b in all_bindings)
errors,warnings=helper.validate(ROOT,p);assert not errors
scope_warnings=[w for w in warnings if not any('chapter_'+str(n).zfill(2)+':' in w for n in range(1,37))]
assert not scope_warnings
ledger=read(ROOT/'usage.json')
save(pack/'manifest.json',{'status':'prepared_approved_images_provider_review_required','source_revision':p['revision'],'project_id':p['id'],'scope':p['render_scope'],'asset_review':helper.review_state(ROOT,p),'approved_cartoon_candidates':changed,'chapters':chapters,'provider_acceptance_cleared':False,'unresolved_provider_refusals':p['provider_review_notes']['attempts'],'new_generation_attempts':0,'total_prior_attempts':len(ledger['jobs']),'validation':{'errors':errors,'in_scope_warnings':scope_warnings,'references_hash_verified':True}})
rows='\n'.join(f"| {c['scene']} | {p['chapters'][c['scene']-1]['title']} | {c['duration']} s | [{c['id']}]({c['id']}-director.txt) |" for c in chapters)
(pack/'README.md').write_text('''# Current approved finale package

The user approved the four cartoon variants: Mr Ko `cartoon_c01`; Granny Wong, Granny Lee and Granny Chan `generated_c02`. Their current files and hashes are bound to every requested scene where they appear. Forty-four other selected images and all original sources remain preserved.

Scope: **scenes 37–51 only**, **305 seconds (5:05)**, **480p**, **16:9**. No title, subtitles, captions, text boxes or graphic overlays. Keep normal-speed action, original cartoon cast, Mr Leung completely blind, every vehicle with a driver, and buses with driver and passengers. The scene 37 ferry specifies a captain at the wheel and passengers. Puppy references stay the user-supplied originals. Exactly eight ordinary balloons; Sir Squeaks' rear half has only two rear legs. Prompt-only toy color descriptions now match the approved blue plush references.

| Scene | Scene name | Duration | Director prompt |
|---|---|---:|---|
'''+rows+'''

## Generation state

The current image set is explicitly approved and local validation passes. Provider moderation acceptance remains unresolved. The earlier scene 37 image-privacy rejection and scene 50 output-audio refusal are retained in the journal. No replacement generation was submitted using changed references and no review protection was disabled. The paid portrait-library route is unavailable per the user; no KYC, library or subscription purchase was made.

The full video has not been generated. Further video submission remains held pending provider resolution of the refusals. This package is prepared work, not a rendered movie. Its hashes and prompt bindings supersede the earlier local packages for any future authorized provider-cleared production.
''',encoding='utf-8')
print(json.dumps({'revision':p['revision'],'image_approval':'approved','revised_bindings_verified':True,'affected_requested_scenes':[x['scene'] for x in affected],'prompt_color_fixes':color_fixes,'chapters':15,'duration_seconds':305,'validation_errors':0,'in_scope_warnings':0,'provider_review_required':True,'new_generation_attempts':0,'package':str(pack)},indent=2))
