"""Probe, decode, inspect, select and assemble the real generated video takes."""
import argparse
import hashlib
import json
import math
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
FFMPEG=ROOT/'.media-tools'/'ffmpeg.exe'
FFPROBE=ROOT/'.media-tools'/'ffprobe.exe'
HELPER=Path(r'C:\Users\admina\.codex\skills\movi2\scripts\project.py')
OUT=ROOT/'exports'

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def write(path,data):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def run(arguments):
    result=subprocess.run([str(a) for a in arguments],capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr.decode('utf-8',errors='replace')[-2500:])
    return result

def probe(path):
    return json.loads(run([FFPROBE,'-v','error','-count_frames','-show_streams','-show_format','-of','json',path]).stdout)

def frame(path,second,target):
    target.parent.mkdir(parents=True,exist_ok=True)
    run([FFMPEG,'-hide_banner','-loglevel','error','-y','-ss',str(second),'-i',path,'-frames:v','1','-q:v','2',target])
    return target

def full_decode(path):
    result=run([FFMPEG,'-hide_banner','-v','error','-i',path,'-map','0:v:0','-map','0:a:0','-f','null','-'])
    return {'passed':True,'diagnostic':result.stderr.decode(errors='replace').strip()}

def audio_stats(path):
    result=run([FFMPEG,'-hide_banner','-v','info','-i',path,'-vn','-af','volumedetect','-f','null','-'])
    text=result.stderr.decode(errors='replace')
    stats={}
    for name in ('mean_volume','max_volume'):
        match=re.search(name+r':\s+(-?\d+(?:\.\d+)?) dB',text)
        stats[name+'_db']=float(match.group(1)) if match else None
    raw=run([FFMPEG,'-hide_banner','-v','error','-i',path,'-vn','-ac','1','-ar','16000','-f','f32le','-']).stdout
    data=np.frombuffer(raw,dtype=np.float32)
    stats['sample_count']=len(data)
    stats['rms']=float(np.sqrt(np.mean(data.astype(np.float64)**2)))
    stats['peak']=float(np.max(np.abs(data)))
    stats['non_silent_seconds']=int(sum(np.sqrt(np.mean(data[i:i+16000].astype(np.float64)**2))>0.001 for i in range(0,len(data),16000)))
    return stats

def contact_sheet(frames,path,title,columns=4,width=440,height=280):
    rows=math.ceil(len(frames)/columns)
    image=Image.new('RGB',(columns*width,55+rows*height),'#fbf6ee')
    draw=ImageDraw.Draw(image)
    font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',18)
    draw.text((14,16),title,fill='#463d33',font=font)
    for i,(file,label) in enumerate(frames):
        x=(i%columns)*width
        y=55+(i//columns)*height
        draw.text((x+10,y+3),label,fill='#463d33',font=font)
        with Image.open(file) as source:
            view=source.convert('RGB')
            view.thumbnail((width-12,height-35),Image.Resampling.LANCZOS)
            image.paste(view,(x+(width-view.width)//2,y+30))
    image.save(path)

def normalize_one(c,t,width,height):
    normalized=OUT/'normalized'
    normalized.mkdir(exist_ok=True)
    target=normalized/(c['id']+'-30fps.mp4')
    source=ROOT/t['path']
    filters=f'scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30,trim=duration={c["duration"]},setpts=N/(30*TB)'
    if c['id']=='chapter_05':
        filters+=',colorbalance=rs=0.035:gs=0.005:bs=-0.035:rm=0.05:gm=0.005:bm=-0.05:rh=0.035:gh=0.003:bh=-0.035,eq=brightness=-0.025:saturation=1.02'
    duration=c['duration']
    af=f'aresample=48000,atrim=duration={duration},asetpts=PTS-STARTPTS,apad,atrim=duration={duration},afade=t=in:st=0:d=0.012,afade=t=out:st={duration-0.012}:d=0.012'
    stamp={'source_sha256':hashlib.file_digest(source.open('rb'),'sha256').hexdigest(),'take_id':t['id'],'duration':duration,'vf':filters,'af':af,'profile':'libx264-fast-crf18-aac192k'}
    framing=None
    if c['id']=='chapter_06':
        framing=f'[0:v]split=2[a][b];[a]trim=start=0:end=13,setpts=PTS-STARTPTS[x];[b]trim=start=13:end=17,setpts=PTS-STARTPTS,crop=800:450:480:130,scale={width}:{height}[y];[x][y]concat=n=2:v=1:a=0,{filters}[v]'
        stamp['framing_edit']=framing
    sidecar=target.with_suffix('.json')
    if target.exists() and sidecar.exists() and read(sidecar)==stamp:
        return target
    arguments=[FFMPEG,'-hide_banner','-loglevel','error','-y','-i',source]
    arguments+=['-filter_complex',framing,'-map','[v]'] if framing else ['-map','0:v:0','-vf',filters]
    arguments+=['-map','0:a:0','-af',af,'-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-r','30','-fps_mode','cfr','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-t',duration,'-movflags','+faststart',target]
    run(arguments)
    write(sidecar,stamp)
    print(json.dumps({'normalized':c['id'],'duration':duration,'speed_factor':1.0}),flush=True)
    return target

def normalize_available():
    p=read(ROOT/'project.json')
    technical=read(OUT/'takes-technical-verification.json')
    review=read(OUT/'visual-review.json')
    for c in p['chapters']:
        take_id=review['selected_takes'].get(c['id'])
        t=next((t for t in c['takes'] if t['id']==take_id and t['status']=='succeeded' and t.get('path')),None)
        if t is None or take_id not in technical['takes']:
            continue
        video=next(s for s in technical['takes'][take_id]['probe']['streams'] if s['codec_type']=='video')
        normalize_one(c,t,video['width'],video['height'])

def inspect_available():
    p=read(ROOT/'project.json')
    report_path=OUT/'takes-technical-verification.json'
    report=read(report_path) if report_path.exists() else {'takes':{},'audio_fidelity_note':'Native generated dialogue and music. Technical signal checks alone do not prove every spoken line or speaker identity.'}
    overview=[]
    for c in p['chapters']:
        takes=[t for t in c['takes'] if t['status']=='succeeded' and t.get('path')]
        if not takes:
            continue
        t=takes[-1]
        path=ROOT/t['path']
        if t['id'] not in report['takes']:
            metadata=probe(path)
            video=next(s for s in metadata['streams'] if s['codec_type']=='video')
            audio=next((s for s in metadata['streams'] if s['codec_type']=='audio'),None)
            if not audio:
                raise RuntimeError('Generated take lacks audio: '+t['id'])
            if float(video.get('duration',metadata['format']['duration']))<c['duration']-0.15:
                raise RuntimeError('Generated take is too short: '+t['id'])
            decode=full_decode(path)
            stats=audio_stats(path)
            if stats['rms']<0.001:
                raise RuntimeError('Silent or near-silent generated take: '+t['id'])
            stamps=[0.3,c['duration']*.2,c['duration']*.4,c['duration']*.6,c['duration']*.8,c['duration']-0.3]
            selected=[]
            for index,stamp in enumerate(stamps):
                saved=ROOT/'chapters'/c['id']/'screenshots'/f"{t['id']}_qa_{index:02}.jpg"
                frame(path,stamp,saved)
                selected.append((saved,f"{c['id']}  {stamp:.1f}s"))
            sheet=ROOT/'chapters'/c['id']/'screenshots'/(t['id']+'_review.jpg')
            contact_sheet(selected,sheet,c['title']+' - actual generated frames',columns=3)
            motion=[]
            previous=None
            for file,label in selected:
                with Image.open(file) as source:
                    data=np.asarray(source.convert('L').resize((160,90)),dtype=np.float64)
                if previous is not None:
                    motion.append(float(np.mean(np.abs(data-previous))))
                previous=data
            report['takes'][t['id']]={'chapter_id':c['id'],'path':t['path'],'probe':metadata,'full_decode':decode,'audio':stats,'sampled_motion_mean_absolute_differences':motion,'review_contact_sheet':sheet.relative_to(ROOT).as_posix(),'sample_frames':[{'path':file.relative_to(ROOT).as_posix(),'timestamp':stamp} for (file,label),stamp in zip(selected,stamps)],'speed_handling':'Source real-time timestamps retained; no time stretching or frame blending. Semantic pace assessed separately through generated-frame sequence review.'}
            write(report_path,report)
            print(json.dumps({'inspected':t['id'],'duration':metadata['format']['duration'],'video_duration':video.get('duration'),'size':[video['width'],video['height']],'fps':video.get('r_frame_rate'),'audio_rms':stats['rms'],'review_contact_sheet':str(sheet)}),flush=True)
        item=report['takes'][t['id']]
        for selected in item['sample_frames'][::2]:
            overview.append((ROOT/selected['path'],f"{c['id']} {selected['timestamp']:.1f}s"))
    if overview:
        contact_sheet(overview,OUT/'render-overview.jpg','Actual Seedance frames - chronological story overview',columns=4)
    print(json.dumps({'verified_take_count':len(report['takes']),'expected_chapters':8}),flush=True)

def select_and_assemble():
    p=read(ROOT/'project.json')
    technical=read(OUT/'takes-technical-verification.json')
    visual=read(OUT/'visual-review.json')
    if not visual.get('approved_for_assembly'):
        raise RuntimeError('Actual generated-frame visual inspection is required before selection.')
    selected=[]
    for c in p['chapters']:
        candidate=visual['selected_takes'].get(c['id'])
        if not candidate:
            raise RuntimeError('Missing visual take selection for '+c['id'])
        t=next(t for t in c['takes'] if t['id']==candidate)
        info=technical['takes'][t['id']]
        if t['status']!='succeeded' or not info['full_decode']['passed']:
            raise RuntimeError('Take is not verified for assembly.')
        t['verification']={'technical_report':'exports/takes-technical-verification.json','visual_report':'exports/visual-review.json','full_decode_passed':True}
        c['active_take_id']=t['id']
        c['screenshots']=[{'id':t['id']+f'_qa_{i:02}','path':x['path'],'timestamp':x['timestamp'],'source_take_id':t['id']} for i,x in enumerate(info['sample_frames'])]
        selected.append((c,t,info))
    proposal=ROOT/'proposal-selected-takes.json'
    write(proposal,p)
    run([sys.executable,HELPER,'commit',ROOT,'--from',proposal,'--reason','Select technically verified and visually inspected generated takes'])
    first_video=next(s for s in selected[0][2]['probe']['streams'] if s['codec_type']=='video')
    width,height=first_video['width'],first_video['height']
    normalized=OUT/'normalized'
    normalized.mkdir(exist_ok=True)
    normalized_files=[]
    for c,t,info in selected:
        target=normalize_one(c,t,width,height)
        normalized_files.append(target)
    listing=normalized/'concat.txt'
    listing.write_text('\n'.join("file '"+file.name+"'" for file in normalized_files)+'\n',encoding='utf-8')
    final=OUT/'five-little-friends-golden-star-120s-720p.mp4'
    run([FFMPEG,'-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',listing,'-map','0:v:0','-map','0:a:0','-vf','setpts=N/(30*TB)','-af','atrim=duration=120,asetpts=PTS-STARTPTS','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-r','30','-fps_mode','cfr','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-t','120','-movflags','+faststart',final])
    metadata=probe(final)
    video=next(s for s in metadata['streams'] if s['codec_type']=='video')
    audio=next(s for s in metadata['streams'] if s['codec_type']=='audio')
    frames=int(video.get('nb_read_frames') or video['nb_frames'])
    assert frames==3600,frames
    assert video['r_frame_rate']=='30/1'
    assert abs(float(video['duration'])-120)<0.001
    assert abs(float(metadata['format']['duration'])-120)<0.05
    decode=full_decode(final)
    stats=audio_stats(final)
    poster=OUT/'movie-preview.jpg'
    frame(final,83,poster)
    report={'file':final.relative_to(ROOT).as_posix(),'verified_at':datetime.now(timezone.utc).isoformat(),'duration_seconds':float(metadata['format']['duration']),'video_duration_seconds':float(video['duration']),'frame_count':frames,'fps':30,'width':width,'height':height,'audio_channels':audio['channels'],'audio_sample_rate':int(audio['sample_rate']),'full_decode':decode,'audio':stats,'size_bytes':final.stat().st_size,'probe':metadata,'assembly':{'selected_take_ids':[t['id'] for c,t,info in selected],'chapter_durations':[c['duration'] for c,t,info in selected],'cuts':'hard cuts','playback_speed_factor':1.0,'no_slow_motion_added':True,'no_frame_blending':True,'no_titles_or_subtitle_tracks':True,'source_audio_preserved':True,'audio_edge_fades_seconds':0.012,'color_match':'Subtle warm grade on chapter_05 to connect early sunset and rainbow flight.'},'visual_review':'exports/visual-review.json'}
    report['assembly']['framing_edits']={'chapter_06':{'start':13,'end':17,'crop':[480,130,800,450],'purpose':'Clean hero close-up on Lulu and star; duplicated chick in the original full-width close-up is fully out of frame.'}}
    write(OUT/'final-verification.json',report)
    current=read(ROOT/'project.json')
    current['production_status']='complete'
    current['delivery']={'path':report['file'],'preview_path':poster.relative_to(ROOT).as_posix(),'verification_path':'exports/final-verification.json','duration':120,'resolution':f'{width}x{height}','fps':30,'selected_take_ids':report['assembly']['selected_take_ids'],'pending_stages':[]}
    write(ROOT/'proposal-final-delivery.json',current)
    run([sys.executable,HELPER,'commit',ROOT,'--from',ROOT/'proposal-final-delivery.json','--reason','Deliver verified exact two-minute energetic Golden Star film'])
    checked=json.loads(run([sys.executable,HELPER,'check',ROOT]).stdout)
    if checked['errors']:
        raise RuntimeError(checked['errors'])
    write(OUT/'project-check-final.json',checked)
    run([sys.executable,HELPER,'export',ROOT])
    print(json.dumps({k:report[k] for k in ('file','duration_seconds','frame_count','fps','width','height','audio_channels','audio_sample_rate','size_bytes')},indent=2),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['inspect','assemble','normalize-available'])
    args=parser.parse_args()
    if args.mode=='inspect':
        inspect_available()
    elif args.mode=='normalize-available':
        normalize_available()
    else:
        select_and_assemble()
