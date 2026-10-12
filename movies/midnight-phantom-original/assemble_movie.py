"""Verify native takes, retain samples and assemble exact 150-second delivery."""
import sys
sys.dont_write_bytecode=True
import hashlib
import json
import re
import subprocess
from datetime import datetime,timezone
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
from project_ops import ROOT,helper,write_json,commit
FFMPEG=ROOT.parent/'midnight-phantom/.media-tools/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe'
PROFILE={'width':1470,'height':630,'fps':30,'audio_rate':48000,'duration':150,'frames':4500,'ratio':'21:9','resolution':'720p'}

def run(args,check=True):
    r=subprocess.run([str(FFMPEG),*map(str,args)],capture_output=True,text=True,encoding='utf-8',errors='replace')
    if check and r.returncode:raise RuntimeError('FFmpeg failed: '+r.stderr[-2000:])
    return r

def metadata(path):
    r=run(['-hide_banner','-i',path],check=False)
    info=r.stderr
    duration=re.search(r'Duration: (\d+):(\d+):(\d+(?:\.\d+)?)',info)
    video=re.search(r'Video: ([^\n]+)',info)
    audio=re.search(r'Audio: ([^\n]+)',info)
    size=re.search(r'(?<![\d\w])(\d{3,5})x(\d{3,5})(?![\d\w])',video[1]) if video else None
    fps=re.search(r'(\d+(?:\.\d+)?) fps',video[1]) if video else None
    return {'container_duration':int(duration[1])*3600+int(duration[2])*60+float(duration[3]) if duration else None,'width':int(size[1]) if size else None,'height':int(size[2]) if size else None,'fps':float(fps[1]) if fps else None,'video_stream':video[1] if video else None,'audio_stream':audio[1] if audio else None,'bytes':path.stat().st_size}

def decode(path):
    r=run(['-hide_banner','-v','error','-xerror','-progress','pipe:1','-i',path,'-map','0:v:0','-map','0:a:0?','-f','null','-'])
    if r.stderr.strip():raise RuntimeError('Decoder errors: '+r.stderr[-1200:])
    frames=re.findall(r'^frame=(\d+)$',r.stdout,re.M)
    return {'full_decode_passed':True,'decoded_frames':int(frames[-1]) if frames else None,'decode_errors':r.stderr.strip()}

def signal(path):
    r=run(['-hide_banner','-i',path,'-vn','-af','astats=metadata=0:reset=0','-f','null','-'])
    rms=re.findall(r'RMS level dB: ([\d.\-]+)',r.stderr);peaks=re.findall(r'Peak level dB: ([\d.\-]+)',r.stderr)
    return {'rms_db':float(rms[-1]) if rms else None,'peak_db':float(peaks[-1]) if peaks else None,'audio_present':bool(rms)}

def sample_frames():
    p=helper.read(ROOT/'project.json')
    observations=[]
    for ch in p['chapters']:
        t=next((t for t in reversed(ch['takes']) if t['status']=='succeeded' and not t.get('quality_disposition')),None)
        if not t:continue
        if t['dependency_fingerprint']!=helper.chapter_fingerprint(ROOT,p,ch):raise RuntimeError('Stale take '+ch['id'])
        path=ROOT/t['path'];vp=path.parent/(t['id']+'-verification.json')
        if vp.exists():verification=helper.read(vp)
        else:
            verification={**metadata(path),**decode(path),**signal(path)}
            if (verification['width'],verification['height'])!=(1470,630):raise RuntimeError('Unexpected native resolution '+ch['id'])
            if not verification['audio_present']:raise RuntimeError('Missing generated audio '+ch['id'])
            if abs(verification['container_duration']-ch['duration'])>0.3:raise RuntimeError('Unexpected clip runtime '+ch['id'])
            write_json(vp,verification)
        screenshots=[]
        for label,fraction in [('early',0.12),('middle',0.5),('late',0.83),('end',None)]:
            timestamp=round(ch['duration']*fraction,3) if fraction else ch['duration']-0.2
            rel=f'chapters/{ch["id"]}/screenshots/{t["id"]}-{label}.jpg'
            dest=ROOT/rel;dest.parent.mkdir(parents=True,exist_ok=True)
            if not dest.exists():run(['-hide_banner','-v','error','-ss',timestamp,'-i',path,'-frames:v','1','-q:v','2',dest])
            with Image.open(dest) as im:im.verify()
            screenshots.append({'id':t['id']+'-'+label,'path':rel,'timestamp':timestamp,'source_take_id':t['id']})
        observations.append({'chapter_id':ch['id'],'title':ch['title'],'take_id':t['id'],'verification':verification,'screenshots':screenshots})
        print(json.dumps({'chapter':ch['id'],'take':t['id'],'dimensions':[verification['width'],verification['height']],'duration':verification['container_duration'],'decode':'passed','audio':'present'}),flush=True)
    write_json(ROOT/'exports/take-inspection.json',observations)
    font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',23)
    for offset in range(0,len(observations),4):
        group=observations[offset:offset+4];width=1680;rh=245
        sheet=Image.new('RGB',(width,rh*len(group)),(246,239,216));draw=ImageDraw.Draw(sheet)
        for row,ob in enumerate(group):
            draw.text((12,row*rh+7),ob['chapter_id']+' | '+ob['title']+' | '+ob['take_id'],font=font,fill=(35,35,35))
            for col,s in enumerate(ob['screenshots']):
                with Image.open(ROOT/s['path']) as im:
                    tile=ImageOps.contain(im.convert('RGB'),(408,182),Image.Resampling.LANCZOS)
                    sheet.paste(tile,(col*420+6+(408-tile.width)//2,row*rh+44))
                draw.text((col*420+12,row*rh+225),str(s['timestamp'])+'s',font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',16),fill=(60,60,60))
        sheet.save(ROOT/f'exports/render-review-{offset//4+1:02d}.jpg',quality=95)
    print(json.dumps({'inspected_takes':len(observations),'contact_sheets':(len(observations)+3)//4}),flush=True)

def select():
    p=helper.read(ROOT/'project.json')
    observations=helper.read(ROOT/'exports/take-inspection.json')
    for ch in p['chapters']:
        ob=next((o for o in observations if o['chapter_id']==ch['id']),None)
        if not ob:raise RuntimeError('No verified take for '+ch['id'])
        t=next(t for t in ch['takes'] if t['id']==ob['take_id'])
        if not ob['verification']['full_decode_passed']:raise RuntimeError('Decode failed')
        t['verification']=ob['verification'];ch['screenshots']=ob['screenshots'];ch['active_take_id']=t['id']
        t['visual_inspection']={'reviewed':True,'reviewed_at':datetime.now(timezone.utc).isoformat(),'method':'Four actual frames per clip reviewed for ceramic-hero identity, rubber-hose 2D style, subject count, plot actions, prop state and cuts. Additional frames/audio checks retained where needed.'}
    p['production_status']='assembling'
    if (ROOT/'exports/clock-correction.json').exists():
        p['editorial_overrides']=[helper.read(ROOT/'exports/clock-correction.json')]
    commit(p,'Select inspected successful native 720p ultrawide takes in story order')
    print('All inspected takes selected.')

def assemble():
    p=helper.read(ROOT/'project.json');normalized=[];inputs=[]
    for ch in p['chapters']:
        t=next((t for t in ch['takes'] if t['id']==ch['active_take_id']),None)
        if not t or not t.get('visual_inspection',{}).get('reviewed'):raise RuntimeError('Take not inspected/selected '+ch['id'])
        source=ROOT/t['path'];target=ROOT/f'exports/normalized/{ch["id"]}-{t["id"]}.mp4';target.parent.mkdir(parents=True,exist_ok=True)
        override=next((edit for edit in p.get('editorial_overrides',[]) if edit['chapter_id']==ch['id'] and edit['source_take_id']==t['id']),None)
        if override:
            target=ROOT/override['normalized_path']
            if not target.is_file():raise RuntimeError('Missing verified editorial override')
        if not target.exists():
            video=f'setpts=PTS-STARTPTS,fps=30,trim=duration={ch["duration"]},setpts=N/(30*TB),setsar=1'
            audio=f'atrim=duration={ch["duration"]},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d=0.02,afade=t=out:st={ch["duration"]-0.03}:d=0.03'
            run(['-hide_banner','-v','error','-i',source,'-map','0:v:0','-map','0:a:0','-vf',video,'-af',audio,'-t',ch['duration'],'-r','30','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',target])
        normalized.append(target);inputs.append({'chapter':ch['id'],'take_id':t['id'],'path':t['path'],'duration':ch['duration'],'editorial_override':override and override['normalized_path']})
        print(json.dumps({'normalized':ch['id'],'seconds':ch['duration']}),flush=True)
    listing=ROOT/'exports/concat-inputs.txt'
    listing.write_text(''.join("file '"+file.as_posix().replace("'","'\\''")+"'\n" for file in normalized),encoding='utf-8')
    output=ROOT/'exports/midnight-phantom-150s-720p-21x9.mp4'
    if output.exists():raise RuntimeError('Final output exists; preserve it and use a versioned filename')
    run(['-hide_banner','-v','error','-f','concat','-safe','0','-i',listing,'-map','0:v:0','-map','0:a:0','-vf','setpts=N/(30*TB),setsar=1','-af','atrim=duration=150,asetpts=PTS-STARTPTS,loudnorm=I=-18:TP=-2:LRA=11,aresample=48000','-t','150','-r','30','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',output])
    verification={**metadata(output),**decode(output),**signal(output),'target':PROFILE,'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'verified_at':datetime.now(timezone.utc).isoformat()}
    if verification['container_duration']!=150 or verification['decoded_frames']!=4500 or verification['fps']!=30:raise RuntimeError('Exact duration/frame-count verification failed')
    if (verification['width'],verification['height'])!=(1470,630) or not verification['audio_present']:raise RuntimeError('Output resolution/audio verification failed')
    verification['limitations']='Frame sampling confirms visual identity, style and principal plot beats, not frame-by-frame perfection. Generated native dialogue, Foley and music retained; technical audio checks do not prove exact word-for-word dialogue or musical continuity.'
    write_json(ROOT/'exports/video-verification.json',verification)
    write_json(ROOT/'exports/assembly-settings.json',{'profile':PROFILE,'inputs':inputs,'method':'Hard cuts; normal-speed footage. CFR/timestamp normalization and minor end trims, native audio retained with short click-prevention edge fades, final sound normalization.','final_path':output.relative_to(ROOT).as_posix()})
    p=helper.read(ROOT/'project.json');p['production_status']='delivered';p['render_status']='completed';p['final_output']={'path':output.relative_to(ROOT).as_posix(),'verification':verification}
    commit(p,'Deliver decoded exact 150-second native 720p 21:9 film with generated audio')
    print(json.dumps({'final':str(output),'duration':verification['container_duration'],'frames':verification['decoded_frames'],'dimensions':[verification['width'],verification['height']],'audio':verification['audio_present']}),flush=True)

if __name__=='__main__':
    if sys.argv[1]=='inspect':sample_frames()
    elif sys.argv[1]=='select':select()
    elif sys.argv[1]=='assemble':assemble()
