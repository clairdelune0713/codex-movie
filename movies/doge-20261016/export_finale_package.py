"""Save a reviewable, credential-free, scope-limited render package."""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
from render_finale import payload,save
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
pack=ROOT/'exports/finale-render-package';pack.mkdir(parents=True,exist_ok=True)
chapters=[]
for c in p['chapters'][36:51]:
    _,bindings,submitted,size=payload(p,c,'<runtime-verified-seedance-endpoint>')
    canonical=pack/(c['id']+'-director.txt');canonical.write_text(c['prompt'],encoding='utf-8')
    compiled=pack/(c['id']+'-compiled.txt');compiled.write_text(submitted,encoding='utf-8')
    chapters.append({'id':c['id'],'scene':c['chapter_index'],'duration':c['duration'],'prompt_path':canonical.relative_to(ROOT).as_posix(),'compiled_prompt_path':compiled.relative_to(ROOT).as_posix(),'bindings':bindings,'request_bytes':size,'dependency_fingerprint':helper.chapter_fingerprint(ROOT,p,c)})
assets={b['asset_id']:b for c in chapters for b in c['bindings']}
save(pack/'manifest.json',{'status':'prepared_awaiting_external_transfer_permission','project_id':p['id'],'source_revision':p['revision'],'scope':{'first_scene':37,'last_scene':51,'duration_seconds':305,'resolution':'480p','aspect_ratio':'21:9'},'asset_review':helper.review_state(ROOT,p),'destination':'https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks','reference_transport':'Selected approved local reference images, inline temporary base64; no public buckets; credentials runtime-only; no signed URLs saved.','chapters':chapters})
save(pack/'pricing-evidence.json',{'checked_date':'2026-10-16','source_uri':'https://docs.byteplus.com/en/docs/ModelArk/2191775','model':'Seedance 2.5','resolution':'480p','reference_video_input':False,'currency':'USD','list_price_per_million_completion_tokens':'10.70','basis':'Published token unit price 0.0107 USD/K for no-video-input 480p/720p. Final estimate uses actual returned completion_tokens; account discounts and tax not verified.','dimension_source_uri':'https://docs.byteplus.com/zh-TW/docs/modelark/seedance-2-5','native_profile_dimensions':[992,432]})
save(pack/'preflight.json',{'asset_review':helper.review_state(ROOT,p),'scenes':len(chapters),'total_seconds':sum(c['duration'] for c in chapters),'selected_reference_count':len(assets),'max_request_bytes':max(c['request_bytes'] for c in chapters),'all_reference_sha256_verified':all(hashlib.sha256((ROOT/b['path']).read_bytes()).hexdigest()==b['sha256'] for b in assets.values()),'generation_attempts':len(json.loads((ROOT/'usage.json').read_text())['jobs']),'empty_project_value':'Explicitly confirmed by user; runtime preserves empty value. No other project/account substituted.','submission_status':'No POST submitted. Default sandbox DNS failed before authentication; escalated network access rejected by automatic approval review pending explicit external-transfer approval.'})
rows='\n'.join(f"| {c['scene']} | {p['chapters'][c['scene']-1]['title']} | {c['duration']} s | [{c['id']} director prompt]({c['id']}-director.txt) |" for c in chapters)
(pack/'README.md').write_text('''# doge-20261016 — scenes 37–51

Prepared video generation package, not a generated video. Exactly fifteen scenes, 305 seconds (5:05), native 480p / 21:9 Seedance profile. Scenes 1–36 are outside this render scope and the adapter rejects them.

The revised assets are approved. Four immutable prop revisions are selected; all supplied character/puppy files remain unchanged. The screenplay is archived unchanged. Current prompts preserve its scene divisions and timing; scene 43 includes its own puppy memory inserts, without separate earlier-scene jobs.

Every visible vehicle must have a driver. Scene 37's ferry has a captain visibly at controls and passengers. The promenade stays pedestrian. Buses, if visible, require driver and passengers. Leung remains completely blind, sunglasses on, and acts by sound/touch/smell/memory. Exactly eight ordinary balloons; toy tail half has rear legs only. No slow motion; original cartoon cast only.

Selected reference images and scene prompts are prepared for temporary transmission to BytePlus Seedance at `https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks`. The user confirmed the workspace project-name value is intentionally empty; preserve it. Credentials are read only at runtime from workspace `.env`, never included here. Automatic approval review currently blocks this external transfer pending explicit destination approval. No generation POST or paid task has occurred.

| Scene | Script scene | Length | Prompt |
|---|---|---:|---|
'''+rows+'''

The scope-limited renderer journals each attempt before POST, checks current approved images immediately before submission, retrieves accepted jobs without duplicate POSTs, decodes native 992×432 clips and tracks returned completion tokens. Actual account charges remain unverified; rate-based costs will be estimates.

The local assembler requires successful visually inspected selected takes. It keeps native animation/audio, trims to original beat durations without slow-motion stretching, adds the screenplay's two captions and animated closing route/title, then encodes one 305-second movie. A full decode and expected 7,320 frames at 24 fps are mandatory before delivery. No movie file is fabricated while generation is blocked.
''',encoding='utf-8')
print(json.dumps({'package':str(pack),'chapters':len(chapters),'duration_seconds':305,'references':len(assets),'asset_review':helper.review_state(ROOT,p)['status'],'generation_attempts':0},indent=2))
