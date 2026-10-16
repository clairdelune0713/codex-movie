"""Prepare actual generated-frame galleries; inspection is recorded separately."""
import argparse
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
from render_movie import ROOT, FF, read, save

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--chapters',default='all');args=parser.parse_args()
    p=read(ROOT/'project.json');j=read(ROOT/'exports/task-journal.json')
    selected=p['chapters'] if args.chapters=='all' else [p['chapters'][int(n)-1] for n in args.chapters.split(',')]
    items=[]
    for c in selected:
        t=j['takes'].get(c['id'])
        if not t or t['status']!='succeeded':continue
        actual=t['verification']['duration'];d=min(c['duration'],actual)
        times=[0.2,round(d/3,2),round(d*2/3,2),round(max(0,d-0.2),2)]
        samples=[]
        for i,ts in enumerate(times):
            dest=ROOT/'chapters'/c['id']/'screenshots'/f"{t['id']}_review_{i+1:02}.jpg"
            dest.parent.mkdir(parents=True,exist_ok=True)
            if not dest.exists():
                result=subprocess.run([str(FF),'-v','error','-threads','2','-ss',str(ts),'-i',str(ROOT/t['path']),'-frames:v','1','-q:v','2',str(dest)],capture_output=True,text=True)
                if result.returncode:raise RuntimeError('Frame extraction failed '+c['id'])
            samples.append({'path':dest.relative_to(ROOT).as_posix(),'timestamp':ts})
        items.append({'chapter':c['id'],'take':t['id'],'scene':c['source_scene'],'duration':c['duration'],'samples':samples})
    gallery=ROOT/'exports/take-review';gallery.mkdir(parents=True,exist_ok=True)
    font=ImageFont.truetype('C:/Windows/Fonts/msyh.ttc',18)
    small=ImageFont.truetype('C:/Windows/Fonts/msyh.ttc',16)
    sheets=[]
    for offset in range(0,len(items),5):
        rows=items[offset:offset+5]
        canvas=Image.new('RGB',(1840,50+len(rows)*300),'#f3f0e9');draw=ImageDraw.Draw(canvas)
        draw.text((18,12),'dog-20261013 | actual native 1080p generated frames | '+str(offset+1)+'-'+str(offset+len(rows)),font=font,fill='#152526')
        for y,item in enumerate(rows):
            draw.text((18,52+y*300),f"{item['chapter']} | scene {item['scene']:02} | {item['duration']}s",font=small,fill='#213b39')
            for x,s in enumerate(item['samples']):
                img=Image.open(ROOT/s['path']).convert('RGB');img=ImageOps.contain(img,(444,250))
                canvas.paste(img,(18+x*458,80+y*300))
                draw.text((18+x*458,333+y*300),str(s['timestamp'])+'s',font=small,fill='#213b39')
        target=gallery/f'review_{rows[0]["chapter"]}_{rows[-1]["chapter"]}.jpg';canvas.save(target,quality=94)
        sheets.append({'path':target.relative_to(ROOT).as_posix(),'chapters':[x['chapter'] for x in rows]})
    save(gallery/'index.json',{'frames_are_actual_generated_media':True,'inspected':False,'items':items,'sheets':sheets})
    print(json.dumps(sheets,ensure_ascii=False))

if __name__=='__main__':main()
