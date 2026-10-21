"""Record the operator's completed frame inspection, bound to immutable take bytes."""
import argparse,hashlib
from render_finale import ROOT,journal,read,save
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--chapters',required=True);ap.add_argument('--note',required=True);ap.add_argument('--repair',action='store_true');args=ap.parse_args()
    path=ROOT/'exports/visual-reviews.json';reviews=read(path) if path.exists() else {};j=journal()
    for n in args.chapters.split(','):
        cid='scene_'+n.strip();t=j['takes'][cid]
        if t['status']!='succeeded':raise RuntimeError(cid+' is not a successful take')
        source=ROOT/t['path'];sha=hashlib.sha256(source.read_bytes()).hexdigest()
        frames=ROOT/'exports/clip-inspection'/cid/t['id']/'frames.json'
        if not frames.exists() or read(frames)['source_sha256']!=sha:raise RuntimeError(cid+' current frame sheets not extracted')
        reviews[cid]={'take_id':t['id'],'source_sha256':sha,'inspected':True,'requires_repair':args.repair,'notes':args.note,'inspection_method':'Decoded source and inspected labeled real-frame contact sheets throughout each shot; audio presence/decoding verified, words not independently transcribed.'}
        print(cid,t['id'],'repair' if args.repair else 'accepted')
    save(path,reviews)
if __name__=='__main__':main()
