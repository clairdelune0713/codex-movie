from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
ids=['blind-guy','animal-companion-worker','lonely-old-man','barista','mags','granny-wong','granny-lee','granny-chan']
jobs=[]
for a in p['asset_list']:
    if a['id'] not in ids:continue
    c=next(c for c in a['candidates'] if c['id']==a['selected_candidate_id'])
    index=1+max([int(x['id'][1:]) for x in a['candidates'] if x['id'].startswith('c') and x['id'][1:].isdigit()] or [0])
    prompt=("Use case: identity-preserve, style-transfer. Refine this ORIGINAL FICTIONAL ANIMATED character reference sheet for a warm rounded 3D feature film. Preserve the same character identity, facial structure, hairstyle, age, skin tone, outfit colors, footwear, accessories, front/back/portrait sheet composition and neutral studio backdrop. Make only a small rendering refinement: noticeably smooth hand-painted/clay-like skin, broad sculpted color planes, simplified graphic facial creases instead of fine skin wrinkles or pores, softly simplified hair clumps, clean expressive designed eyes and eyebrows, and slightly more visibly cartoon surface shading. Keep a dimensional 3D animated look and the existing warm lighting; no flat2D replacement, no photorealistic skin, no photographic texture, no realistic camera skin detail. Do not create a new identity, change clothing or add characters. Keep the original panel structure including headless wardrobe views and the one head portrait. No labels, lettering, logos, watermarks or existing Pixar/Disney characters. Character continuity: "+a['description'])
    jobs.append({'id':a['id'],'name':a['name'],'candidate_id':f'c{index:02d}','input':c['path'],'prompt':prompt,'source_revision':p['revision']})
(ROOT/'toon-revision-jobs.json').write_text(json.dumps(jobs,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(jobs,ensure_ascii=False))
