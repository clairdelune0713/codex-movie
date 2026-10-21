"""Adapt the previously verified transport, enforcing the requested narrow scope."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent
src=(ROOT.parent/'dog-20261015/render_movie.py').read_text(encoding='utf-8')
src=src.replace('Journaled native 1080p','Journaled native 480p ultrawide')
src=src.replace("Decimal('11.70')","Decimal('10.70')")
src=src.replace('1080p image-only list rate USD 11.70/M tokens','480p no-input-video list rate USD 10.70/M tokens')
src=src.replace('https://ai.byteplus.com/ark/region:ap-southeast-1/docs/model-pricing checked 2026-10-15','https://docs.byteplus.com/en/docs/ModelArk/2191775 checked 2026-10-16')
src=src.replace("'resolution':'1080p'","'resolution':'480p'").replace("'aspect_ratio':'16:9'","'aspect_ratio':'21:9'")
src=src.replace("'ratio':'16:9'","'ratio':'21:9'")
src=src.replace('(1920,1080)','(992,432)').replace('native_1080p=True','native_480p_21x9=True')
src=src.replace('native 1920x1080','native 992x432').replace('s, 1080p 16:9','s, 480p 21:9')
start=src.index('def payload(');end=src.index('\n\ndef download(',start)
src=src[:start]+'''def payload(p,c,endpoint):
    if not 37<=c['chapter_index']<=51:raise RuntimeError('Scene outside explicitly authorized 37–51 scope')
    bindings=[];images=[]
    for a in helper.active_assets(p,c):
        selected=helper.selected_media(a);f=ROOT/selected['path'];raw=f.read_bytes()
        if len(raw)>=30*1024*1024:raise ValueError('Oversize reference '+a['id'])
        token='@Image'+str(len(bindings)+1)
        bindings.append({'tag':a['tag'],'provider_tag':token,'asset_id':a['id'],'candidate_id':selected['id'],
            'path':selected['path'],'role':'reference_image','sha256':hashlib.sha256(raw).hexdigest()})
        mime=mimetypes.guess_type(f.name)[0] or 'image/png'
        images.append({'type':'image_url','image_url':{'url':'data:'+mime+';base64,'+base64.b64encode(raw).decode()},'role':'reference_image'})
    mapping={b['tag'].casefold():b['provider_tag'] for b in bindings}
    pattern=re.compile(r'@[^\\W\\s][\\w-]*',re.UNICODE)
    text=pattern.sub(lambda m:mapping[m[0].casefold()],c['prompt'])
    for ref in c.get('continuity_references',[]):
        if ref.get('media_type')!='Image' or ref.get('role')!='reference_image':
            raise RuntimeError('Only explicitly inspected omni-image continuity supported')
        raw=(ROOT/ref['path']).read_bytes();mime=mimetypes.guess_type(ref['path'])[0] or 'image/jpeg'
        token='@Image'+str(len(images)+1)
        images.append({'type':'image_url','image_url':{'url':'data:'+mime+';base64,'+base64.b64encode(raw).decode()},'role':'reference_image'})
        bindings.append({'continuity_reference_id':ref['id'],'provider_tag':token,'path':ref['path'],
            'role':'reference_image','sha256':hashlib.sha256(raw).hexdigest(),
            'source_chapter_id':ref['source_chapter_id'],'source_take_id':ref['source_take_id'],'source_sha256':ref['source_sha256']})
        text+='\\nINSPECTED CONTINUITY FRAME '+token+': '+ref['reason']+' New timing/actions/dialogue follow this chapter only.'
    assert 1<=len(images)<=30
    body={'model':endpoint,'content':[{'type':'text','text':text}]+images,
        'duration':c['duration'],'ratio':'21:9','resolution':'480p','generate_audio':True,
        'watermark':False,'return_last_frame':True,'output_format':'mp4',
        'omni_reference_task_type':'reference','seed':2026101600+c['chapter_index']}
    size=len(json.dumps(body,ensure_ascii=False,separators=(',',':')).encode('utf-8'))
    if size>64*1024*1024:raise ValueError('Payload exceeds 64MB')
    return body,bindings,text,size
'''+src[end:]
# Never use an alternate provider/private-asset route or automatic moderation retry.
start=src.index("        if current_fp==old['dependency_fingerprint']:")
end=src.index("        take_number=",start)
src=src[:start]+"        if current_fp==old['dependency_fingerprint']:\n            raise RuntimeError('Replacement requires reviewed changed prompt or dependencies; no identical retry')\n"+src[end:]
src=src.replace("    p=read(ROOT/'project.json')\n    c=next", "    p=read(ROOT/'project.json')\n    if not 37<=c['chapter_index']<=51:raise RuntimeError('Unrequested scene rejected before POST')\n    c=next")
src=src.replace("    proposal['render_status']='awaiting_assembly' if len(j['takes'])==len(proposal['chapters'])", "    proposal['render_status']='awaiting_assembly' if len(j['takes'])==15")
src=src.replace("    proposal['tool_availability']['jobs_submitted']", "    proposal.setdefault('tool_availability',{})['jobs_submitted']")
src=src.replace("        for c in p['chapters']:\n            _,bindings", "        for c in p['chapters'][36:51]:\n            _,bindings")
src=src.replace("chosen=p['chapters'] if args.chapters=='all'", "chosen=p['chapters'][36:51] if args.chapters=='all'")
src=src.replace("    chosen_ids={c['id']", "    chosen_ids={c['id']")
src=src.replace("    if args.command=='submit':", "    if any(not 37<=c['chapter_index']<=51 for c in chosen):raise RuntimeError('Only scenes 37–51 authorized')\n    if args.command=='submit':")
(ROOT/'render_finale.py').write_text(src,encoding='utf-8')
print('Installed scope-limited 480p 21:9 renderer; no secret values stored.')
