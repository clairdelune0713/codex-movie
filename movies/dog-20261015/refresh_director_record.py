"""Commit the complete current direction as reviewable project material."""
import copy
from render_movie import ROOT,read,helper
p=read(ROOT/'project.json');proposal=copy.deepcopy(p)
lines=['dog-20261015 | 600-second directed screenplay | 1080p16:9','']
for c in p['chapters']:
 lines.extend([f"{c['chapter_index']:02}. {c['id']} | {c['duration']} seconds",c['prompt'],''])
proposal['detailed_script']='\n'.join(lines)
resolved=[];remaining=[]
for cid in p.get('quality_repair_queue',[]):
 c=next(c for c in p['chapters'] if c['id']==cid)
 t=next((t for t in c['takes'] if t['id']==c.get('active_take_id')),None)
 if t and t.get('visual_review',{}).get('inspected') and not t['visual_review'].get('requires_repair'):
  resolved.append({'chapter':cid,'selected_take':t['id'],'resolution':'Resolved in recorded sampled visual review; speech limitations retained separately.'})
 else:remaining.append(cid)
proposal['quality_repair_queue']=remaining
if resolved:proposal.setdefault('quality_repair_history',[]).extend(resolved)
print(helper.save(ROOT,p,proposal,'Refresh complete directed screenplay including inspected continuity repairs and local audio decisions'))
