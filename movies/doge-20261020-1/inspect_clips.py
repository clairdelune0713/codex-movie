"""Extract real frames and make labeled inspection sheets; never alter source takes."""
from pathlib import Path
import argparse, hashlib, json, math, subprocess
from PIL import Image, ImageDraw, ImageFont
from render_finale import ROOT, FF, read, save, journal

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--chapters',default='all');args=ap.parse_args()
    j=journal();p=read(ROOT/'project.json');cs={c['id']:c for c in p['chapters']}
    wanted=set(j['takes']) if args.chapters=='all' else {'scene_'+x.strip() for x in args.chapters.split(',')}
    for cid,t in j['takes'].items():
        if cid not in wanted or t['status']!='succeeded':continue
        src=ROOT/t['path'];sha=hashlib.sha256(src.read_bytes()).hexdigest()
        folder=ROOT/'exports/clip-inspection'/cid/t['id'];folder.mkdir(parents=True,exist_ok=True)
        stamp=folder/'frames.json'
        if stamp.exists() and read(stamp)['source_sha256']==sha:
            print(cid,'existing sheets',folder,flush=True);continue
        times={.2,t['duration']-.2}
        times.update(float(x)+.5 for x in range(0,t['duration'],2) if x+.5<t['duration'])
        for s in cs[cid].get('shots',[]):
            start=s.get('start',s.get('start_time'));end=s.get('end',s.get('end_time'))
            if isinstance(start,(int,float)) and isinstance(end,(int,float)):times.add((start+end)/2)
        frames=[]
        for i,sec in enumerate(sorted(times)):
            dest=folder/f'frame-{i:02d}-{sec:05.2f}.jpg'
            if not dest.exists():
                r=subprocess.run([str(FF),'-hide_banner','-loglevel','error','-nostdin','-ss',str(sec),'-i',str(src),'-frames:v','1','-q:v','2',str(dest)],capture_output=True)
                if r.returncode:raise RuntimeError('Frame extraction failed '+cid)
            frames.append({'time':sec,'path':dest.relative_to(ROOT).as_posix()})
        font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17)
        sheets=[]
        for page in range(math.ceil(len(frames)/12)):
            group=frames[page*12:(page+1)*12];sheet=Image.new('RGB',(1488,math.ceil(len(group)/3)*244),'#142025');d=ImageDraw.Draw(sheet)
            for i,f in enumerate(group):
                im=Image.open(ROOT/f['path']).convert('RGB');im.thumbnail((496,216))
                x=i%3*496;y=i//3*244;sheet.paste(im,(x,y));d.text((x+7,y+219),f"{cid} {t['id']}   {f['time']:.2f}s",font=font,fill='white')
            out=folder/f'contact-{page+1:02}.jpg';sheet.save(out,quality=93);sheets.append(out.relative_to(ROOT).as_posix())
            print(out,flush=True)
        save(stamp,{'chapter_id':cid,'take_id':t['id'],'source_path':t['path'],'source_sha256':sha,'frames':frames,'sheets':sheets,'inspection_status':'awaiting_visual_inspection'})
if __name__=='__main__':main()
