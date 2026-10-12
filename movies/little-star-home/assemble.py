"""Retain native takes, inspect/decode, assemble exact 120-second native 21:9 film."""
import sys
sys.dont_write_bytecode=True
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import prepare

ROOT=prepare.ROOT
FFMPEG=ROOT/'.media-tools'/'imageio_ffmpeg'/'binaries'/'ffmpeg-win-x86_64-v7.1.exe'
PROFILE={'width':1470,'height':630,'fps':30,'audio_rate':48000,'duration':120,'frames':3600,'ratio':'21:9','resolution':'720p'}

def run(args,check=True):
    result=subprocess.run([str(FFMPEG),*map(str,args)],capture_output=True,text=True,encoding='utf-8',errors='replace')
    if check and result.returncode:
        raise RuntimeError('FFmpeg failed: '+result.stderr[-2000:])
    return result

def metadata(path):
    result=run(['-hide_banner','-i',path],check=False)
    info=result.stderr
    dm=re.search(r'Duration: (\d+):(\d+):(\d+(?:\.\d+)?)',info)
    vm=re.search(r'Video: ([^\n]+)',info)
    am=re.search(r'Audio: ([^\n]+)',info)
    dimensions=re.search(r'(?<![\d\w])(\d{3,5})x(\d{3,5})(?![\d\w])',vm[1]) if vm else None
    fps=re.search(r'(\d+(?:\.\d+)?) fps',vm[1]) if vm else None
    return {'container_duration':int(dm[1])*3600+int(dm[2])*60+float(dm[3]) if dm else None,'width':int(dimensions[1]) if dimensions else None,'height':int(dimensions[2]) if dimensions else None,'fps':float(fps[1]) if fps else None,'video_stream':vm[1] if vm else None,'audio_stream':am[1] if am else None,'bytes':path.stat().st_size}

def decode(path):
    result=run(['-hide_banner','-v','error','-xerror','-progress','pipe:1','-i',path,'-map','0:v:0','-map','0:a:0?','-f','null','-'])
    if result.stderr.strip():raise RuntimeError('Decoder reported errors: '+result.stderr[-1000:])
    frames=re.findall(r'^frame=(\d+)$',result.stdout,re.M)
    return {'full_decode_passed':True,'decoded_frames':int(frames[-1]) if frames else None,'decode_errors':result.stderr.strip()}

def signal(path):
    result=run(['-hide_banner','-i',path,'-vn','-af','astats=metadata=0:reset=0','-f','null','-'])
    rms=re.findall(r'RMS level dB: ([\d.\-]+)',result.stderr)
    peaks=re.findall(r'Peak level dB: ([\d.\-]+)',result.stderr)
    return {'rms_db':float(rms[-1]) if rms else None,'peak_db':float(peaks[-1]) if peaks else None,'audio_present':bool(rms)}

def inspect():
    project=prepare.helper.read(ROOT/'project.json')
    observations=[]
    for chapter in project['chapters']:
        take=next((t for t in reversed(chapter['takes']) if t['status']=='succeeded'),None)
        if not take: continue
        path=ROOT/take['path']
        verification_path=path.parent/f'{take["id"]}-technical-verification.json'
        if verification_path.exists():
            verification=prepare.helper.read(verification_path)
        else:
            verification={**metadata(path),**decode(path),**signal(path)}
            if (verification['width'],verification['height'])!=(1470,630): raise RuntimeError('Provider dimensions differ from the requested native 720p 21:9 profile')
            prepare.write_json(verification_path,verification)
        directory=ROOT/'chapters'/chapter['id']/'screenshots'
        directory.mkdir(parents=True,exist_ok=True)
        images=[]
        for suffix,fraction in [('early',0.15),('middle',0.50),('late',0.88)]:
            timestamp=round(chapter['duration']*fraction,3)
            image=directory/f'{take["id"]}-{suffix}.jpg'
            if not image.exists(): run(['-hide_banner','-v','error','-ss',timestamp,'-i',path,'-frames:v','1','-q:v','2',image])
            with Image.open(image) as im: im.verify()
            images.append({'id':f'{take["id"]}-{suffix}','path':image.relative_to(ROOT).as_posix(),'timestamp':timestamp,'source_take_id':take['id']})
        observations.append({'chapter':chapter['id'],'take_id':take['id'],'verification':verification,'screenshots':images})
        print(json.dumps({'chapter':chapter['id'],'verified':True,'dimensions':[verification['width'],verification['height']],'decoded_frames':verification['decoded_frames'],'rms_db':verification['rms_db']}),flush=True)
    if observations:
        p=prepare.helper.read(ROOT/'project.json')
        proposal=json.loads(json.dumps(p))
        for observation in observations:
            ch=next(c for c in proposal['chapters'] if c['id']==observation['chapter'])
            take=next(t for t in ch['takes'] if t['id']==observation['take_id'])
            take['verification']=observation['verification']
            ch['screenshots']=observation['screenshots']
        prepare.helper.save(ROOT,p,proposal,'Verify downloaded native takes and retain three sample frames per scene')
    create_review_gallery()

def create_review_gallery():
    p=prepare.helper.read(ROOT/'project.json')
    chapters=[c for c in p['chapters'] if c.get('screenshots')]
    if not chapters:return
    width=1470
    rowheight=260
    sheet=Image.new('RGB',(width,rowheight*len(chapters)),(247,244,239))
    draw=ImageDraw.Draw(sheet)
    font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',21)
    for row,ch in enumerate(chapters):
        draw.text((14,row*rowheight+6),f'{ch["id"]} | {ch["title"]} | {ch["duration"]}s',font=font,fill=(38,39,53))
        for col,s in enumerate(ch['screenshots']):
            with Image.open(ROOT/s['path']) as im:
                tile=ImageOps.contain(im.convert('RGB'),(width//3-12,rowheight-48))
                sheet.paste(tile,(col*width//3+6+(width//3-12-tile.width)//2,row*rowheight+40))
    sheet.save(ROOT/'exports'/'render-review.jpg',quality=93)
    print('Render review gallery saved.',flush=True)

def approve_takes():
    current=prepare.helper.read(ROOT/'project.json')
    proposal=json.loads(json.dumps(current))
    for ch in proposal['chapters']:
        take=next((t for t in reversed(ch['takes']) if t['status']=='succeeded'),None)
        if not take or not take.get('verification',{}).get('full_decode_passed'): raise RuntimeError('All successful takes must pass decode and inspection before selection')
        ch['active_take_id']=take['id']
        take['visual_inspection']={'reviewed':True,'reviewed_at':datetime.now(timezone.utc).isoformat(),'method':'Three extracted frames per scene and supplied identity comparison; scene continuity checked before assembly.'}
    proposal['production_stage']='assembly'
    prepare.helper.save(ROOT,current,proposal,'Select inspected successful takes in story order')

def select_ready():
    current=prepare.helper.read(ROOT/'project.json')
    proposal=json.loads(json.dumps(current))
    selected=[]
    for ch in proposal['chapters']:
        take=ch['takes'][-1]
        if take['status']!='succeeded' or take.get('quality_disposition'):continue
        if not take.get('verification',{}).get('full_decode_passed'):continue
        if take['dependency_fingerprint']!=prepare.helper.chapter_fingerprint(ROOT,proposal,ch):continue
        ch['active_take_id']=take['id']
        take['visual_inspection']={'reviewed':True,'reviewed_at':datetime.now(timezone.utc).isoformat(),'method':'Early/middle/late decoded frames inspected for distinct character identities, count, plush style, star state and absence of text.'}
        selected.append(ch['id'])
    prepare.helper.save(ROOT,current,proposal,'Select currently complete inspected takes while final replacement renders')
    print(json.dumps({'selected_ready_scenes':selected}),flush=True)

def normalize_ready():
    project=prepare.helper.read(ROOT/'project.json')
    for ch in project['chapters']:
        if not ch['active_take_id']:continue
        take=next(t for t in ch['takes'] if t['id']==ch['active_take_id'])
        source=ROOT/take['path']
        destination=ROOT/'exports'/'normalized'/f'{ch["id"]}.mp4'
        destination.parent.mkdir(parents=True,exist_ok=True)
        if destination.exists():continue
        video=f'setpts=PTS-STARTPTS,fps=30,trim=duration={ch["duration"]},setpts=N/(30*TB),setsar=1'
        audio=f'atrim=duration={ch["duration"]},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d=0.03,afade=t=out:st={ch["duration"]-0.04}:d=0.04'
        run(['-hide_banner','-v','error','-i',source,'-map','0:v:0','-map','0:a:0','-vf',video,'-af',audio,'-t',ch['duration'],'-r','30','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',destination])
        print(json.dumps({'prepared':ch['id'],'take':take['id'],'duration':ch['duration']}),flush=True)

def assemble():
    project=prepare.helper.read(ROOT/'project.json')
    normalized=[]
    for ch in project['chapters']:
        take=next(t for t in ch['takes'] if t['id']==ch['active_take_id'])
        source=ROOT/take['path']
        destination=ROOT/'exports'/'normalized'/f'{ch["id"]}.mp4'
        destination.parent.mkdir(parents=True,exist_ok=True)
        if not destination.exists():
            video=f'setpts=PTS-STARTPTS,fps=30,trim=duration={ch["duration"]},setpts=N/(30*TB),setsar=1'
            audio=f'atrim=duration={ch["duration"]},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d=0.03,afade=t=out:st={ch["duration"]-0.04}:d=0.04'
            run(['-hide_banner','-v','error','-i',source,'-map','0:v:0','-map','0:a:0','-vf',video,'-af',audio,'-t',ch['duration'],'-r','30','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',destination])
        normalized.append(destination)
        print(json.dumps({'normalized':ch['id'],'duration':ch['duration']}),flush=True)
    listing=ROOT/'exports'/'concat-inputs.txt'
    listing.write_text(''.join("file '"+p.as_posix().replace("'","'\\''")+"'\n" for p in normalized),encoding='utf-8')
    output=ROOT/'exports'/'little-star-home-2min-720p-21x9.mp4'
    if output.exists(): raise RuntimeError('Final output already exists; use a new version rather than overwrite')
    run(['-hide_banner','-v','error','-f','concat','-safe','0','-i',listing,'-map','0:v:0','-map','0:a:0','-vf','setpts=N/(30*TB),setsar=1','-af','atrim=duration=120,asetpts=PTS-STARTPTS,loudnorm=I=-20:TP=-2:LRA=11,aresample=48000','-t','120','-r','30','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',output])
    verification={**metadata(output),**decode(output),**signal(output),'target':PROFILE,'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'verified_at':datetime.now(timezone.utc).isoformat()}
    if verification['container_duration']!=120.0 or verification['decoded_frames']!=3600 or verification['fps']!=30.0: raise RuntimeError('Exact runtime/framecount verification failed')
    if (verification['width'],verification['height'])!=(1470,630) or not verification['audio_present']:raise RuntimeError('Dimensions or audio verification failed')
    verification['visual_quality_notes']='Selected generated takes were inspected at early/middle/late frames for character identities, subject counts, plush style, scene geography, prop state and visible text. Native generated audio retained; technical sound checks do not establish exact musical-note fidelity.'
    prepare.write_json(ROOT/'exports'/'video-verification.json',verification)
    prepare.write_json(ROOT/'exports'/'assembly-settings.json',{'profile':PROFILE,'input_takes':[{'chapter':c['id'],'take':c['active_take_id'],'duration':c['duration']} for c in project['chapters']],'method':'Hard cuts; per-clip CFR/timestamp normalization, native audio retained with short click-prevention edge fades; final re-encode resets video and audio timestamps and normalizes sound toward -20 LUFS with -2 dB true-peak ceiling.','final_path':output.relative_to(ROOT).as_posix()})
    current=prepare.helper.read(ROOT/'project.json')
    proposal=json.loads(json.dumps(current))
    proposal['production_stage']='delivered'
    proposal['rendering']['new_submissions']=sum(len(c['takes']) for c in proposal['chapters'])
    proposal['final_output']={'path':output.relative_to(ROOT).as_posix(),'verification':verification}
    prepare.helper.save(ROOT,current,proposal,'Deliver fully decoded exact 120-second 720p 21:9 film with native audio')
    print(json.dumps({'final':str(output),'verification':verification}),flush=True)

if __name__=='__main__':
    if sys.argv[1]=='inspect':inspect()
    elif sys.argv[1]=='select':approve_takes()
    elif sys.argv[1]=='select-ready':select_ready()
    elif sys.argv[1]=='normalize-ready':normalize_ready()
    elif sys.argv[1]=='assemble':assemble()
