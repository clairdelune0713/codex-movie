"""Inspect genuine rendered takes, assemble exactly 600 seconds, verify decode."""
import argparse, importlib.util, json, math, re, subprocess, wave
from pathlib import Path
from PIL import Image, ImageChops, ImageFont, ImageDraw, ImageStat
ROOT=Path(__file__).resolve().parent
FF=Path('C:/Users/admina/Downloads/project/dog-test/.tools/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe')
def mod(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
h=mod('movi2','C:/Users/admina/.codex/skills/movi2/scripts/project.py')
def run(args):
    p=subprocess.run([str(FF),'-hide_banner']+[str(a) for a in args],capture_output=True,text=True,encoding='utf-8',errors='replace')
    if p.returncode:raise RuntimeError(p.stderr[-4000:])
    return p
def probe(file):
    p=subprocess.run([str(FF),'-hide_banner','-i',str(file)],capture_output=True,text=True,encoding='utf-8',errors='replace')
    duration=re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)',p.stderr)
    video=next((s.strip() for s in p.stderr.splitlines() if 'Stream #' in s and 'Video:' in s),'')
    audio=next((s.strip() for s in p.stderr.splitlines() if 'Stream #' in s and 'Audio:' in s),None)
    dims=re.search(r'(\d{3,5})x(\d{3,5})',video);fps=re.search(r'(\d+(?:\.\d+)?) fps',video)
    if not (duration and dims and fps):raise RuntimeError('Cannot probe '+str(file))
    return {'duration_seconds':int(duration[1])*3600+int(duration[2])*60+float(duration[3]),'resolution':[int(dims[1]),int(dims[2])],'fps':float(fps[1]),'video_stream':video,'audio_stream':audio}
def decode(file):
    p=run(['-v','error','-i',file,'-map','0:v:0','-map','0:a:0?','-progress','pipe:1','-nostats','-f','null','-'])
    frames=re.findall(r'^frame=(\d+)\s*$',p.stdout,re.M)
    if not frames:raise RuntimeError('No decoded frames')
    return {'decode_verified':True,'frame_count':int(frames[-1])}
def inspect_one(t):
    f=ROOT/t['path'];v=probe(f)
    if v['duration_seconds']<20:raise RuntimeError('Take shorter than required '+t['id'])
    if not v['audio_stream']:raise RuntimeError('Missing native audio '+t['id'])
    v.update(decode(f));v['native_request_resolution']='720p';v['native_request_ratio']='21:9'
    directory=ROOT/'chapters'/t['chapter_id']/'screenshots';directory.mkdir(exist_ok=True)
    files=[];small=[]
    for i,ts in enumerate([0.5,4,8,12,16,19],1):
        dest=directory/(t['id']+f'_sample{i:02d}.jpg')
        if not dest.exists():run(['-v','error','-ss',ts,'-i',f,'-frames:v','1','-update','1',dest])
        with Image.open(dest) as img:
            img.load();small.append(img.convert('RGB').resize((192,82)))
        files.append({'timestamp':ts,'path':dest.relative_to(ROOT).as_posix()})
    diffs=[sum(ImageStat.Stat(ImageChops.difference(a,b)).mean)/3 for a,b in zip(small,small[1:])]
    v['motion_sample_mean_absolute_differences']=diffs
    v['contains_visual_change']=max(diffs)>0.2
    if not v['contains_visual_change']:raise RuntimeError('Take is visually static '+t['id'])
    canvas=Image.new('RGB',(960,500),'#151a23');draw=ImageDraw.Draw(canvas)
    for i,item in enumerate(files):
        with Image.open(ROOT/item['path']) as img:im=img.convert('RGB').resize((480,206))
        x=(i%2)*480;y=(i//2)*164
        im=im.resize((384,164));canvas.paste(im,(x,y));draw.text((x+4,y+4),f'{t["chapter_id"]} {item["timestamp"]}s',fill='white')
    contact=directory/(t['id']+'_contact.jpg');canvas.save(contact,quality=88)
    v.update(samples=files,contact_path=contact.relative_to(ROOT).as_posix())
    signal=run(['-v','info','-i',f,'-map','0:a:0','-af','volumedetect','-vn','-f','null','-']).stderr
    for key in ['mean_volume','max_volume']:
        m=re.search(key+r': ([\d.-]+) dB',signal);v[key+'_db']=float(m[1]) if m else None
    t['verification']=v
    return v
def overlay(name,lines,fontsize=34,top=90):
    folder=ROOT/'exports/titles';folder.mkdir(exist_ok=True)
    dest=folder/(name+'.png')
    im=Image.new('RGBA',(1470,630),(0,0,0,0));d=ImageDraw.Draw(im)
    font=ImageFont.truetype('C:/Windows/Fonts/msjh.ttc',fontsize)
    spacing=fontsize+14;height=len(lines)*spacing+30
    d.rounded_rectangle((180,top-15,1290,top+height),radius=16,fill=(6,18,32,160))
    for i,line in enumerate(lines):
        box=d.textbbox((0,0),line,font=font);w=box[2]-box[0]
        d.text(((1470-w)/2,top+i*spacing),line,font=font,fill=(255,241,211,255),stroke_width=1,stroke_fill=(10,20,30,180))
    im.save(dest);return dest
def normalized(c,t):
    folder=ROOT/'exports/assembly-v01';folder.mkdir(exist_ok=True)
    dest=folder/(t['id']+'_normalized.mp4')
    if dest.exists():return dest
    # User expressly accepted Seedance's native output: never resize the video.
    if probe(ROOT/t['path'])['resolution'] != [1470,630]:raise RuntimeError('Unexpected source dimensions; native delivery requires matching takes')
    vf='setsar=1,fps=30,trim=duration=20,setpts=N/(30*TB)'
    af='aresample=48000,atrim=duration=20,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.04,afade=t=out:st=19.96:d=0.04'
    command=['-v','error','-i',ROOT/t['path']]
    title=None;enable=None
    i=c['chapter_index']
    if i==2:
        title=overlay('opening',['SOMEWHERE BETWEEN US','我們之間'],42,80);enable='between(t,3,8)'
    if i==25:
        title=overlay('shared-origin',['Tart — Victoria, Australia','Tine — Victoria, Australia','同一間犬舍 · Same dog farm'],32,55);enable='between(t,13,18)'
    if i==30:
        # Cover unsolicited synthetic footer lettering without resizing/cropping.
        vf+=",drawbox=x=0:y=563:w=iw:h=67:color=0x061220:t=fill:enable='gte(t,13)'"
        title=overlay('closing',['From Victoria to Victoria Harbour.','Different paths. Different gifts.','Some paths are meant to cross.','我們之間 · AI動畫改編'],30,80);enable='between(t,13,20)'
    if title:
        command+=['-loop','1','-i',title,'-filter_complex',f"[0:v]{vf}[v];[v][1:v]overlay=0:0:enable='{enable}'[out]",'-map','[out]','-map','0:a:0','-af',af]
    else:command+=['-map','0:v:0','-map','0:a:0','-vf',vf,'-af',af]
    command+=['-t','20','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-r','30','-fps_mode','cfr','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',dest]
    run(command);return dest
def main():
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['inspect','prepare-edit','assemble','verify']);ap.add_argument('--chapters',default='all');args=ap.parse_args()
    p=h.read(ROOT/'project.json');j=h.read(ROOT/'exports/seedance-journal.json')
    chapters=p['chapters'] if args.chapters=='all' else [p['chapters'][int(i)-1] for i in args.chapters.split(',')]
    if args.command=='inspect':
        inspected=[]
        for c in chapters:
            t=j['takes'].get(c['id'])
            if not t or t['status']!='succeeded' or t.get('verification',{}).get('decode_verified'):continue
            v=inspect_one(t);inspected.append(t['id']);h.atomic_write(ROOT/'exports/seedance-journal.json',j)
            print(t['id'],'verified',v['resolution'],v['duration_seconds'],'seconds',flush=True)
        h.atomic_write(ROOT/'exports/take-verification.json',{t['id']:t.get('verification') for t in j['takes'].values() if t.get('verification')})
        print('Newly inspected',len(inspected));return
    if args.command=='prepare-edit':
        for c in chapters:
            t=j['takes'].get(c['id'])
            if t and t['status']=='succeeded' and t.get('verification',{}).get('decode_verified'):
                normalized(c,t);print(c['id'],'ready for edit',flush=True)
        return
    final=ROOT/'exports/somewhere-between-us-10min-720p-21x9.mp4'
    if args.command=='assemble':
        if len(chapters)!=30:raise RuntimeError('Final assembly requires all 30 chapters')
        if final.exists():raise RuntimeError('Preserve existing final; choose a new version for reassembly')
        files=[]
        for c in chapters:
            t=j['takes'].get(c['id'])
            if not t or t['status']!='succeeded' or not t.get('verification',{}).get('decode_verified'):raise RuntimeError('Missing inspected success '+c['id'])
            files.append(normalized(c,t));print(c['id'],'normalized',flush=True)
        listing=ROOT/'exports/assembly-v01/concat.txt';listing.write_text('\n'.join("file '"+f.as_posix()+"'" for f in files)+'\n',encoding='utf-8')
        temp=final.with_name(final.stem+'-assembling.mp4')
        run(['-v','error','-f','concat','-safe','0','-i',listing,'-vf','setpts=N/(30*TB)','-af','atrim=duration=600,asetpts=PTS-STARTPTS,loudnorm=I=-23:TP=-1.5:LRA=11','-t','600','-r','30','-fps_mode','cfr','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-ar','48000','-ac','2','-b:a','192k','-map_metadata','-1','-movflags','+faststart',temp])
        temp.replace(final)
        h.atomic_write(ROOT/'exports/assembly-manifest.json',{'inputs':[{'chapter_id':c['id'],'take_id':j['takes'][c['id']]['id'],'movie_start':c['movie_start'],'movie_end':c['movie_end']} for c in chapters],'runtime_goal':600,'output':final.relative_to(ROOT).as_posix(),'title_timing':{'opening':[23,28],'origin':[493,498],'closing':[593,600]},'audio':'Native generated audio preserved, stereo48kHz with 40ms edge fades and final integrated loudness target -23 LUFS / true peak -1.5dB','cuts':'Hard cuts; no crossfade-induced runtime changes','resizing':False,'author_name_on_screen':False})
    v=probe(final);v.update(decode(final));v['file_bytes']=final.stat().st_size
    v['passes']=v['resolution']==[1470,630] and abs(v['duration_seconds']-600)<0.02 and v['fps']==30 and v['frame_count']==18000 and bool(v['audio_stream'])
    if not v['passes']:raise RuntimeError('Final verification failed '+str(v))
    h.atomic_write(ROOT/'exports/video-verification.json',v)
    p=h.read(ROOT/'project.json');proposal=json.loads(json.dumps(p));proposal['render_state'].update(status='complete',video_takes_generated=30,actual_video_runtime_seconds=v['duration_seconds'],final_video_path=final.relative_to(ROOT).as_posix(),verification_path='exports/video-verification.json',pending_stages=[])
    result=h.save(ROOT,p,proposal,'Deliver fully decoded 600-second native 1470x630 movie with 18000 frames and native sound')
    print('Verified final:',json.dumps(v), 'revision',result['revision'],flush=True)
if __name__=='__main__':main()
