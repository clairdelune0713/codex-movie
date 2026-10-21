"""Extract actual returned video frames for manual continuity/style review.

Contact sheets are review artifacts only and never become generation inputs.
"""
import argparse,hashlib,json,math,subprocess
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
from render_finale import ROOT,FF,read,save

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--chapters',default='all');args=ap.parse_args()
    p=read(ROOT/'project.json');j=read(ROOT/'exports/task-journal.json')
    wanted=set(range(37,52)) if args.chapters=='all' else {int(n) for n in args.chapters.split(',')}
    output=[]
    for c in p['chapters'][36:51]:
        n=c['chapter_index'];t=j['takes'].get(c['id'])
        if n not in wanted or not t or t.get('status')!='succeeded':continue
        source=ROOT/t['path'];sha=hashlib.sha256(source.read_bytes()).hexdigest()
        folder=ROOT/'exports/visual-inspection'/(c['id']+'_'+t['id']+'_'+sha[:10]);folder.mkdir(parents=True,exist_ok=True)
        manifest=folder/'frames.json'
        if manifest.exists():
            m=read(manifest)
            if m['source_sha256']!=sha:raise RuntimeError('Frame review source changed')
            output.append({'scene':n,'take':t['id'],'sheets':m['contact_sheet_paths']});continue
        # Sample at one second plus each script shot's key midpoint and final state.
        times={round(min(c['duration']-.15,.35+k),3) for k in range(c['duration'])}
        times|={round((s['start']+s['end'])/2,3) for s in c['shots']}
        times|={round(c['duration']-.20,3)}
        frames=[]
        for idx,sec in enumerate(sorted(times)):
            dest=folder/f'frame-{idx:03}-{sec:06.2f}s.jpg'
            if not dest.exists():
                r=subprocess.run([str(FF),'-hide_banner','-loglevel','error','-nostdin','-ss',str(sec),'-i',str(source),'-frames:v','1','-q:v','2',str(dest)],capture_output=True,text=True,encoding='utf-8',errors='replace')
                if r.returncode or not dest.exists():raise RuntimeError('Cannot extract actual video frame')
            frames.append({'time':sec,'path':dest.relative_to(ROOT).as_posix()})
        font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',18)
        sheets=[]
        for page in range(math.ceil(len(frames)/16)):
            selected=frames[page*16:(page+1)*16]
            canvas=Image.new('RGB',(1360,916),(28,31,35));d=ImageDraw.Draw(canvas)
            d.text((12,8),f'Scene {n} | {t["id"]} | actual frames | page {page+1}',font=font,fill='white')
            for k,f in enumerate(selected):
                x=(k%4)*340;y=40+(k//4)*219
                im=Image.open(ROOT/f['path']).convert('RGB');im=ImageOps.contain(im,(336,189))
                canvas.paste(im,(x+(340-im.width)//2,y))
                d.text((x+8,y+192),f'{f["time"]:.2f} s',font=font,fill=(238,237,233))
            file=folder/f'contact-{page+1:02}.jpg';canvas.save(file,quality=94)
            sheets.append(file.relative_to(ROOT).as_posix())
        save(manifest,{'chapter_id':c['id'],'take_id':t['id'],'source_path':t['path'],'source_sha256':sha,'frames':frames,'contact_sheet_paths':sheets,'review_status':'awaiting_actual_visual_inspection'})
        output.append({'scene':n,'take':t['id'],'sheets':sheets})
    save(ROOT/'exports/visual-inspection-index.json',output)
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
