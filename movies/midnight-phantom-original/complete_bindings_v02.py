import ast,json
from project_ops import ROOT,helper,commit,write_json
from seedance_client import bind
tree=ast.parse((ROOT/'direct_continuity_v02.py').read_text(encoding='utf-8'))
identity=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='identity' for t in n.targets))
p=helper.read(ROOT/'project.json')
for ch in p['chapters']:
 n=ch['chapter_index'];need=set(ch['tagged_assets'])
 if n<=2:need.add('@Museum')
 if n in (3,4):need.add('@Alley')
 if n in (5,6):need.add('@VehicleLayout')
 if n>=6:need|={'@Riff','@Pip','@Crow','@Diamond','@Machine','@TowerLayout'}
 if n>=9:need.add('@Guard')
 additions=[a['tag']+': '+identity[a['tag']] for a in p['asset_list'] if a['tag'] in need and a['tag'] not in ch['tagged_assets']]
 if additions:ch['prompt']=ch['prompt'].replace('Character multi-view sheets','\n'.join(additions)+'\nCharacter multi-view sheets')
 ch['tagged_assets']=[a['tag'] for a in p['asset_list'] if a['tag'] in need]
 write_json(ROOT/f'chapters/{ch["id"]}/director-v02.json',{'prompt':ch['prompt'],'shots':ch['shots'],'handoff':ch['handoff'],'tagged_assets':ch['tagged_assets']})
p['detailed_script']='\n\n'.join(f'{c["movie_start"]}-{c["movie_end"]}s | {c["title"]}\n'+c['prompt'] for c in p['chapters'])
commit(p,'Bind existing approved museum, alley, vehicle geography and all retained tower actors to v02 prompts')
checks=[]
for ch in p['chapters']:
 compiled,bindings,content=bind(p,ch)
 checks.append({'chapter':ch['id'],'references':len(bindings),'images':sum(b['role']=='reference_image' for b in bindings),'audio':sum(b['role']=='reference_audio' for b in bindings),'serialized_content_mb':round(len(json.dumps(content).encode())/1024/1024,2),'fingerprint':helper.chapter_fingerprint(ROOT,p,ch)})
 if '@CrowVoice' in ch['tagged_assets'] and not any(c['type']=='audio_url' for c in content):raise RuntimeError('Voice guide missing')
 if any(x in compiled for x in ('@Riff','@Pip','@CrowVoice')):raise RuntimeError('Uncompiled tag')
write_json(ROOT/'exports/continuity-v02-render-preflight.json',checks)
print(json.dumps({'approval':helper.review_state(ROOT,p)['status'],'chapters':checks}))
