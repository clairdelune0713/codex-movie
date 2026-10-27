from pathlib import Path
from fractions import Fraction
import hashlib
import json
import math
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'chapters/chapter_01/takes/take_01.mp4'
FINAL = ROOT / 'exports/xmas-01-30s-720p-16x9.mp4'
FFMPEG = Path('C:/ffmpeg/bin/ffmpeg.exe')
FFPROBE = FFMPEG.with_name('ffprobe.exe')

def run(args):
    result = subprocess.run(list(map(str,args)),capture_output=True,text=True,encoding='utf-8')
    if result.returncode:
        raise RuntimeError(result.stderr[-2000:])
    return result

def probe(path):
    return json.loads(run([FFPROBE,'-v','error','-count_frames','-show_streams','-show_format','-of','json',path]).stdout)

def decode(path):
    result = run([FFMPEG,'-hide_banner','-v','error','-i',path,'-map','0:v:0','-map','0:a:0','-f','null','-'])
    return {'passed':True,'diagnostics':result.stderr.strip()}

def levels(path):
    result = run([FFMPEG,'-hide_banner','-i',path,'-vn','-af','volumedetect','-f','null','-'])
    out={}
    for key in ('mean_volume','max_volume'):
        m=re.search(key+r':\s*([-\w.]+) dB',result.stderr)
        out[key+'_db']=m.group(1) if m else None
    return out

def write_json(path, value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def contact_sheet():
    from PIL import Image,ImageDraw,ImageFont,ImageOps
    folder=ROOT/'chapters/chapter_01/screenshots/source-inspection'
    folder.mkdir(parents=True,exist_ok=True)
    timestamps=[0.2,1.5,3,4.5,6,7.5,9,10.5,12,13.5,15,16.5,18,19.5,21,22.5,24,25.5,27,28.8]
    canvas=Image.new('RGB',(1920,1500),'#131b22')
    draw=ImageDraw.Draw(canvas)
    font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',22)
    screens=[]
    for i,t in enumerate(timestamps):
        path=folder/('frame-'+str(i+1).zfill(2)+'.jpg')
        if not path.exists():
            run([FFMPEG,'-hide_banner','-loglevel','error','-ss',t,'-i',SOURCE,'-frames:v','1','-q:v','2',path])
        with Image.open(path) as im:
            thumb=ImageOps.contain(im.convert('RGB'),(474,267),Image.Resampling.LANCZOS)
            x=(i%4)*480
            y=(i//4)*300
            canvas.paste(thumb,(x+3,y))
            draw.text((x+8,y+270),str(t)+'s',font=font,fill='white')
        screens.append({'id':'source_frame_'+str(i+1).zfill(2),'path':path.relative_to(ROOT).as_posix(),'timestamp':t,'source_take_id':'take_01'})
    destination=ROOT/'exports/source-inspection-contact-sheet.jpg'
    canvas.save(destination,quality=92)
    write_json(ROOT/'exports/source-screenshot-manifest.json',screens)
    return str(destination)

def inspect():
    metadata=probe(SOURCE)
    result={'source':SOURCE.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'probe':metadata,'full_decode':decode(SOURCE),'audio_levels':levels(SOURCE),'inspection_gallery':contact_sheet()}
    write_json(ROOT/'exports/source-technical-verification.json',result)
    print(json.dumps({'streams':[{k:s.get(k) for k in ('codec_type','codec_name','width','height','r_frame_rate','duration','nb_frames','nb_read_frames','sample_rate','channels')} for s in metadata['streams']],'duration':metadata['format']['duration'],'full_decode':result['full_decode'],'audio_levels':result['audio_levels'],'gallery':result['inspection_gallery']},indent=2))

def export():
    if FINAL.exists():
        raise RuntimeError('Immutable final export already exists')
    metadata=probe(SOURCE)
    video=next(s for s in metadata['streams'] if s['codec_type']=='video')
    audio=next(s for s in metadata['streams'] if s['codec_type']=='audio')
    rate=Fraction(video['r_frame_rate'])
    count=round(30*rate)
    source_frames=int(video.get('nb_read_frames') or video.get('nb_frames') or 0)
    if source_frames<count or float(video.get('duration') or metadata['format']['duration'])<29.99:
        raise RuntimeError('Source too short for a native 30-second export; no padding permitted')
    if video['width']!=1280 or video['height']!=720:
        raise RuntimeError('Unexpected requested resolution')
    temp=FINAL.with_name(FINAL.stem+'.partial.mp4')
    command=[str(FFMPEG),'-hide_banner','-loglevel','error','-i',str(SOURCE),'-map','0:v:0','-map','0:a:0','-vf','trim=duration=30,setpts=N/('+str(rate)+'*TB)','-af','atrim=duration=30,asetpts=PTS-STARTPTS','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',str(rate),'-fps_mode','cfr','-frames:v',str(count),'-c:a','aac','-b:a','192k','-ar','48000','-t','30','-movflags','+faststart',str(temp)]
    run(command)
    temp.replace(FINAL)
    final_meta=probe(FINAL)
    final_video=next(s for s in final_meta['streams'] if s['codec_type']=='video')
    if abs(float(final_meta['format']['duration'])-30)>0.001 or int(final_video['nb_read_frames'])!=count:
        raise RuntimeError('Exact runtime/frame verification failed')
    verification={'source_take':SOURCE.relative_to(ROOT).as_posix(),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'output':FINAL.relative_to(ROOT).as_posix(),'output_sha256':hashlib.sha256(FINAL.read_bytes()).hexdigest(),'generation_requests':1,'merged_segments':False,'processing':'Single-source trim to exact 30 seconds with native frame rate; re-encoded for reliable H.264/AAC playback. No slow motion or added video.','command':command,'duration_seconds':float(final_meta['format']['duration']),'frame_count':count,'fps':str(rate),'dimensions':[final_video['width'],final_video['height']],'probe':final_meta,'full_decode':decode(FINAL),'audio_levels':levels(FINAL)}
    write_json(ROOT/'exports/final-technical-verification.json',verification)
    print(json.dumps({k:v for k,v in verification.items() if k not in ('probe','command')},indent=2))

if __name__=='__main__':
    {'inspect':inspect,'export':export}[sys.argv[1]]()
