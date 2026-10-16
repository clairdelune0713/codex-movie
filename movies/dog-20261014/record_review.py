"""Record the coordinator's actual sampled-frame inspection, never auto-review."""
import argparse,hashlib
from render_movie import ROOT,read,save,sync,now
p=argparse.ArgumentParser();p.add_argument('--chapters',required=True);p.add_argument('--notes',required=True);p.add_argument('--repair',action='store_true');a=p.parse_args()
project=read(ROOT/'project.json');j=read(ROOT/'exports/task-journal.json')
dest=ROOT/'exports/visual-reviews.json';reviews=read(dest) if dest.exists() else {}
for n in a.chapters.split(','):
    c=project['chapters'][int(n)-1];t=j['takes'][c['id']]
    assert t['status']=='succeeded'
    frames=sorted((ROOT/'chapters'/c['id']/'screenshots').glob(t['id']+'_review_*.jpg'))
    assert frames
    review={'inspected':True,'requires_repair':a.repair,'take_id':t['id'],'reviewed_at':now(),
            'source_sha256':hashlib.sha256((ROOT/t['path']).read_bytes()).hexdigest(),
            'sample_paths':[f.relative_to(ROOT).as_posix() for f in frames],
            'scope':'Actual sampled frames; not a claim of frame-by-frame motion or word-perfect generated audio. Local ASR is recorded separately.',
            'notes':a.notes}
    t['visual_review']=review;reviews[c['id']]=review
save(ROOT/'exports/task-journal.json',j);save(dest,reviews)
print(sync(j))
