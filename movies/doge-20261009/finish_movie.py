"""Local inspection, take registration, and exact-runtime delivery. No credentials."""
import argparse
import io
import json
import re
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageStat

ROOT = Path(__file__).resolve().parent
FF = ROOT/'tools/python-deps/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe'
HELPER = Path('C:/Users/admina/.codex/skills/movi2/scripts/project.py')

def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def save(path, value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')

def run(args, check=True):
    proc = subprocess.run([str(FF),'-hide_banner','-nostdin',*args],capture_output=True)
    if check and proc.returncode:
        raise RuntimeError(proc.stderr.decode('utf-8',errors='replace')[-4000:])
    return proc

def metadata(path):
    data=run(['-i',str(path)],False).stderr.decode('utf-8',errors='replace')
    duration=re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)',data)
    video=next((s for s in data.splitlines() if 'Video:' in s),'')
    dims=re.search(r'[, ](\d{3,5})x(\d{3,5})[ ,\[]',video)
    fps=re.search(r'([\d.]+) fps',video)
    audio=next((s.strip() for s in data.splitlines() if 'Audio:' in s),None)
    if not duration or not dims or not fps:
        raise ValueError('Cannot read video metadata: '+str(path))
    return {'duration':int(duration[1])*3600+int(duration[2])*60+float(duration[3]),
            'width':int(dims[1]),'height':int(dims[2]),'fps':float(fps[1]),'audio_stream':audio}

def decode(path):
    proc=run(['-v','error','-i',str(path),'-map','0:v:0','-map','0:a:0?',
              '-progress','pipe:1','-f','null','-'])
    out=proc.stdout.decode('utf-8',errors='replace')
    frames=re.findall(r'^frame=(\d+)',out,re.M)
    errors=proc.stderr.decode('utf-8',errors='replace').strip()
    if errors: raise ValueError('Decode errors: '+errors[-3000:])
    return {'decode_ok':True,'decoded_frames':int(frames[-1]),'decode_errors':errors}

def frame(path, timestamp, destination):
    run(['-v','error','-ss',str(timestamp),'-i',str(path),'-frames:v','1',
         '-vf','scale=735:315','-q:v','2','-y',str(destination)])

def inspect(chapters):
    project=read(ROOT/'project.json')
    journal=read(ROOT/'exports/task-journal.json')['tasks']
    records=[]
    for chapter in project['chapters']:
        cid=chapter['id']
        if chapters and cid not in chapters: continue
        task=journal.get(cid,{})
        if not task.get('path') or task.get('status')!='succeeded': continue
        path=ROOT/task['path']
        folder=ROOT/'chapters'/cid/'screenshots'
        folder.mkdir(exist_ok=True)
        verify_path=ROOT/'chapters'/cid/'takes/take_01-verification.json'
        if verify_path.exists():
            result=read(verify_path)
        else:
            result={**metadata(path),**decode(path),'path':task['path']}
            if (result['width'],result['height'])!=(1470,630) or not result['audio_stream']:
                raise ValueError(cid+': unexpected output profile')
            screens=[]
            for i,fraction in enumerate((.15,.50,.85),1):
                timestamp=round(min(chapter['duration'],result['duration'])*fraction,3)
                dest=folder/f'take_01-sample_{i:02}.jpg'
                frame(path,timestamp,dest)
                screens.append({'id':f'take_01_sample_{i:02}','path':dest.relative_to(ROOT).as_posix(),
                                'timestamp':timestamp,'source_take_id':'take_01'})
            result['screenshots']=screens
            save(verify_path,result)
        records.append({'chapter':cid,**result})
        print(json.dumps({'chapter':cid,'duration':result['duration'],'fps':result['fps'],
                          'size':[result['width'],result['height']],'decoded_frames':result['decoded_frames']}),flush=True)
    out=ROOT/'exports/video-review'
    out.mkdir(exist_ok=True)
    try: font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',20)
    except OSError: font=ImageFont.load_default()
    for offset in range(0,len(records),4):
        group=records[offset:offset+4]
        sheet=Image.new('RGB',(1800,len(group)*292),(25,25,29))
        draw=ImageDraw.Draw(sheet)
        for row,record in enumerate(group):
            draw.text((12,row*292+6),record['chapter']+'  /  15%, 50%, 85%',font=font,fill='white')
            for col,screenshot in enumerate(record['screenshots']):
                im=Image.open(ROOT/screenshot['path']).convert('RGB').resize((600,257))
                sheet.paste(im,(col*600,row*292+32))
        dest=out/f'review-{offset//4+1:02}.jpg'
        sheet.save(dest,quality=92)
        print(json.dumps({'review_sheet':str(dest)}),flush=True)
    save(out/'manifest.json',records)

def sync(select):
    project=read(ROOT/'project.json')
    journal=read(ROOT/'exports/task-journal.json')['tasks']
    for chapter in project['chapters']:
        cid=chapter['id']
        task=journal.get(cid)
        if not task or not task.get('task_id'): continue
        status={'queued':'pending','running':'processing','succeeded':'succeeded',
                'failed':'failed','cancelled':'failed','expired':'failed'}.get(task['status'],'pending')
        take={'id':'take_01','take_number':1,'status':status,'task_id':task['task_id'],
              'prompt':chapter['prompt'],
              'submitted_prompt':(ROOT/'chapters'/cid/'submitted-prompt.txt').read_text(encoding='utf-8'),
              'bindings':task['bindings'],'duration':task['duration'],'resolution':'720p',
              'model':'Seedance 2.5','source_revision':task['source_revision'],
              'dependency_fingerprint':task['dependency_fingerprint'],'created_at':task['submitted_at']}
        for key in ('path','last_frame_path','provider_duration','provider_resolution','provider_ratio',
                    'provider_usage','completed_at','error_code'):
            if key in task: take[key]=task[key]
        verified=ROOT/'chapters'/cid/'takes/take_01-verification.json'
        if verified.exists():
            take['verification']=read(verified)
            chapter['screenshots']=take['verification']['screenshots']
            if select and status=='succeeded': chapter['active_take_id']='take_01'
        # A clip may finish during an inspection pass. Register it without selecting
        # until its own inspection is complete; final assembly requires every selection.
        previous=next((t for t in chapter.get('takes',[]) if t['id']=='take_01'),None)
        if previous: chapter['takes'][chapter['takes'].index(previous)]=take
        else: chapter.setdefault('takes',[]).append(take)
    proposal=ROOT/'take-proposal.json'
    save(proposal,project)
    proc=subprocess.run([sys.executable,str(HELPER),'check',str(ROOT),'--from',str(proposal)],capture_output=True,text=True,encoding='utf-8')
    if proc.returncode: raise ValueError(proc.stdout)
    proc=subprocess.run([sys.executable,str(HELPER),'commit',str(ROOT),'--from',str(proposal),
                         '--reason','Register provider tasks and inspected successful video takes'],capture_output=True,text=True,encoding='utf-8')
    print(proc.stdout,flush=True)
    if proc.returncode: raise ValueError(proc.stderr)

def assemble(partial=False):
    project=read(ROOT/'project.json')
    work=ROOT/'exports/assembly'
    work.mkdir(exist_ok=True)
    inputs=[]
    for chapter in project['chapters']:
        take=next((t for t in chapter.get('takes',[]) if t['id']==chapter.get('active_take_id')),None)
        if not take or take['status']!='succeeded':
            if partial: continue
            raise ValueError('No selected successful take: '+chapter['id'])
        seconds=chapter['duration']
        dest=work/(chapter['id']+'.mp4')
        if not dest.exists():
            vf=f'scale=1470:630:flags=lanczos,setsar=1,fps=30,tpad=stop_mode=clone:stop_duration=1,trim=duration={seconds},setpts=N/(30*TB)'
            if chapter['chapter_index']==24: vf+=f',fade=t=out:st={seconds-1.2}:d=1.2'
            af=f'aresample=48000,apad,atrim=duration={seconds},asetpts=PTS-STARTPTS'
            if chapter['chapter_index']==24: af+=f',afade=t=out:st={seconds-2}:d=2'
            run(['-v','error','-i',str(ROOT/take['path']),'-map','0:v:0','-map','0:a:0',
                 '-vf',vf,'-af',af,'-c:v','libx264','-preset','fast','-crf','18',
                 '-pix_fmt','yuv420p','-fps_mode','cfr','-r','30','-c:a','aac','-b:a','192k',
                 '-ar','48000','-ac','2','-t',str(seconds),'-movflags','+faststart','-y',str(dest)])
        inputs.append({'chapter_id':chapter['id'],'take_id':take['id'],'input_path':take['path'],
                       'normalized_path':dest.relative_to(ROOT).as_posix(),'duration':seconds})
        print(json.dumps({'normalized':chapter['id']}),flush=True)
    if partial:
        return
    total=sum(i['duration'] for i in inputs)
    listing=work/'inputs.txt'
    listing.write_text(''.join("file '"+(ROOT/i['normalized_path']).as_posix()+"'\n" for i in inputs),encoding='utf-8')
    output=ROOT/'exports/doge-20261009-720p-21x9.mp4'
    run(['-v','error','-f','concat','-safe','0','-i',str(listing),'-map','0:v:0','-map','0:a:0',
         '-vf','setpts=N/(30*TB)','-af',f'aresample=48000,loudnorm=I=-18:TP=-1.5:LRA=11,aresample=48000,atrim=duration={total},asetpts=PTS-STARTPTS',
         '-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-fps_mode','cfr','-r','30',
         '-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-t',str(total),'-movflags','+faststart','-y',str(output)])
    result={**metadata(output),**decode(output),'path':output.relative_to(ROOT).as_posix(),
            'planned_duration':total,'expected_frames':total*30,'chapter_count':len(inputs),
            'assembly':'Hard cuts; CFR timestamp reset; generated audio preserved and normalized to -18 LUFS; final fade to black',
            'bytes':output.stat().st_size}
    if result['decoded_frames']!=total*30 or abs(result['duration']-total)>.04:
        raise ValueError('Final runtime/frame count mismatch')
    last_frame=ROOT/'exports/final-frame.jpg'
    frame(output,total-1/30-.001,last_frame)
    mean=ImageStat.Stat(Image.open(last_frame).convert('RGB')).mean
    result['last_frame_mean_rgb']=mean
    result['ending_fades_to_black']=max(mean)<3
    if not result['ending_fades_to_black']: raise ValueError('Ending fade did not reach black')
    frame(output,total-7,ROOT/'exports/movie-poster.jpg')
    save(ROOT/'exports/video-verification.json',result)
    save(ROOT/'exports/assembly-manifest.json',{'source_revision':project['revision'],'inputs':inputs,'output':result})
    print(json.dumps(result),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('command',choices=['inspect','sync','normalize','assemble'])
    parser.add_argument('--chapters',nargs='*')
    parser.add_argument('--select',action='store_true')
    args=parser.parse_args()
    if args.command=='inspect': inspect(args.chapters)
    elif args.command=='sync': sync(args.select)
    else: assemble(args.command=='normalize')
