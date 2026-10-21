"""Record the operator's actual manual frame review, never infer visual approval."""
import argparse,hashlib
import render_finale_refresh as r

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--chapter',type=int,required=True)
    ap.add_argument('--note',action='append',required=True)
    ap.add_argument('--requires-repair',action='store_true')
    args=ap.parse_args()
    assert 37<=args.chapter<=51
    cid=f'chapter_{args.chapter:02}'
    t=r.journal()['takes'][cid]
    assert t['status']=='succeeded' and t['aspect_ratio']=='16:9'
    digest=hashlib.sha256((r.ROOT/t['path']).read_bytes()).hexdigest()
    frames=r.ROOT/'exports/visual-inspection'/f'{cid}_{t["id"]}_{digest[:10]}'/'frames.json'
    manifest=r.read(frames)
    assert manifest['source_sha256']==digest
    target=r.ROOT/'exports/visual-reviews.json'
    reviews=r.read(target)
    old=reviews.get(cid)
    if old and old.get('source_sha256')!=digest:
        r.save(r.ROOT/'exports/visual-review-history'/f'{cid}_{old["take_id"]}_{old["source_sha256"][:10]}.json',old)
    reviews[cid]={'take_id':t['id'],'source_sha256':digest,'inspected':True,
        'requires_repair':args.requires_repair,'inspected_at':r.now(),
        'method':'Manually viewed actual video contact-sheet pages at one-second intervals, source-shot midpoints and final state; noted full-resolution checks where needed.',
        'frame_manifest_path':frames.relative_to(r.ROOT).as_posix(),
        'notes':args.note,'audio_review':'Native audio fully decoded; local ASR and signal checks saved separately, with recognition limitations.'}
    r.save(target,reviews)
    print(cid,t['id'],'repair needed' if args.requires_repair else 'accepted after actual manual inspection')

if __name__=='__main__':main()
