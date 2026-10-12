"""Inspect, normalize and assemble this movie's successful selected takes only.
No title overlays; exact 352 seconds, 1680x720, 30fps, stereo audio.
"""
import argparse, copy, importlib.util, json, re, subprocess
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageStat, ImageFont
ROOT=Path(__file__).resolve().parent
FF=Path('C:/Users/admina/Downloads/project/dog-test/.tools/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe')
def module(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
h=module('h','C:/Users/admina/.codex/skills/movi2/scripts/project.py')
def run(args):
    result=subprocess.run([str(FF),'-hide_banner']+[str(x) for x in args],capture_output=True,text=True,encoding='utf-8',errors='replace')
    if result.returncode:raise RuntimeError(result.stderr[-3000:])
    return result
def probe(file):
    result=subprocess.run([str(FF),'-hide_banner','-i',str(file)],capture_output=True,text=True,encoding='utf-8',errors='replace')
    d=re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)',result.stderr)
    v=next((line.strip() for line in result.stderr.splitlines() if 'Stream #' in line and 'Video:' in line),'')
    a=next((line.strip() for line in result.stderr.splitlines() if 'Stream #' in line and 'Audio:' in line),None)
    dims=re.search(r'(\d{3,5})x(\d{3,5})',v);fps=re.search(r'(\d+(?:\.\d+)?) fps',v)
    if not(d and dims and fps):raise ValueError('Cannot probe media '+str(file))
    return {'duration_seconds':int(d[1])*3600+int(d[2])*60+float(d[3]),'resolution':[int(dims[1]),int(dims[2])],'fps':float(fps[1]),'video_stream':v,'audio_stream':a}
def decode(file):
    r=run(['-v','error','-i',file,'-map','0:v:0','-map','0:a:0?','-progress','pipe:1','-nostats','-f','null','-'])
    frames=re.findall(r'^frame=(\d+)\s*$',r.stdout,re.M)
    if not frames:raise ValueError('No frames decoded')
    return {'decode_verified':True,'frame_count':int(frames[-1])}
def inspect(c,t):
    file=ROOT/t['path'];v=probe(file);v.update(decode(file))
    if v['duration_seconds']<c['duration']-0.05 or not v['audio_stream']:raise ValueError('Incomplete video or audio in '+t['id'])
    if abs(v['resolution'][0]/v['resolution'][1]-21/9)>0.005:raise ValueError('Wrong aspect ratio '+t['id'])
    folder=ROOT/'chapters'/c['id']/'screenshots';folder.mkdir(parents=True,exist_ok=True)
    samples=[];small=[]
    for i,fraction in enumerate([0.03,0.2,0.4,0.6,0.8,0.96],1):
        ts=round(c['duration']*fraction,3);dest=folder/(t['id']+f'_sample{i:02d}.jpg')
        if not dest.exists():run(['-v','error','-ss',ts,'-i',file,'-frames:v','1','-update','1',dest])
        im=Image.open(dest).convert('RGB');small.append(im.resize((210,90)))
        samples.append({'timestamp':ts,'path':dest.relative_to(ROOT).as_posix()})
    diffs=[sum(ImageStat.Stat(ImageChops.difference(a,b)).mean)/3 for a,b in zip(small,small[1:])]
    v.update(samples=samples,motion_sample_mean_absolute_differences=diffs,contains_visual_change=max(diffs)>0.2)
    if not v['contains_visual_change']:raise ValueError('No visible change '+t['id'])
    volume=run(['-v','info','-i',file,'-map','0:a:0','-af','volumedetect','-vn','-f','null','-']).stderr
    for key in ('mean_volume','max_volume'):
        m=re.search(key+r': ([\d.-]+) dB',volume);v[key+'_db']=float(m[1]) if m else None
    if v['max_volume_db'] is None or v['max_volume_db']<-60:raise ValueError('Missing audio signal '+t['id'])
    t['verification']=v
    return v
def galleries(p,j):
    out=ROOT/'exports/visual-review';out.mkdir(exist_ok=True)
    font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',17)
    for group in range(6):
        canvas=Image.new('RGB',(1920,820),'#18202b');draw=ImageDraw.Draw(canvas)
        for row,c in enumerate(p['chapters'][group*5:group*5+5]):
            t=j['takes'].get(c['id'])
            if not t or not t.get('verification'):continue
            for column,sample in enumerate(t['verification']['samples']):
                im=Image.open(ROOT/sample['path']).convert('RGB').resize((320,137))
                x=column*320;y=row*164;canvas.paste(im,(x,y+24))
                draw.text((x+5,y+2),f"{c['id']} {t['id'].split('_')[-1]} {sample['timestamp']}s",font=font,fill='white')
        canvas.save(out/f'act-{group+1:02d}.jpg',quality=94)
def normalized(c,t):
    folder=ROOT/'exports/assembly-v01';folder.mkdir(exist_ok=True)
    dest=folder/(t['id']+'_normalized.mp4')
    if dest.exists():return dest
    length=c['duration'];fade=max(0,length-0.04)
    run(['-v','error','-i',ROOT/t['path'],'-map','0:v:0','-map','0:a:0',
         '-vf',f'scale=1680:720:flags=lanczos,setsar=1,fps=30,trim=duration={length},setpts=N/(30*TB)',
         '-af',f'aresample=48000,atrim=duration={length},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.04,afade=t=out:st={fade}:d=0.04',
         '-t',length,'-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-r','30','-fps_mode','cfr',
         '-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-map_metadata','-1','-movflags','+faststart',dest])
    return dest
def main():
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['inspect','normalize','assemble','verify','gallery']);ap.add_argument('--chapters',default='all');a=ap.parse_args()
    p=h.read(ROOT/'project.json');j=h.read(ROOT/'exports/seedance-journal.json')
    chapters=p['chapters'] if a.chapters=='all' else [p['chapters'][int(i)-1] for i in a.chapters.split(',')]
    if a.command=='inspect':
        for c in chapters:
            t=j['takes'].get(c['id'])
            if not t or t['status']!='succeeded' or t.get('verification',{}).get('decode_verified'):continue
            v=inspect(c,t);h.atomic_write(ROOT/'exports/seedance-journal.json',j)
            print(t['id'],'decoded;',v['duration_seconds'],'seconds;',v['resolution'],'audio and motion present',flush=True)
        h.atomic_write(ROOT/'exports/take-verification.json',{t['id']:t.get('verification') for t in j['takes'].values()})
        galleries(p,j);return
    if a.command=='gallery':galleries(p,j);return
    if a.command=='normalize':
        for c in chapters:
            t=j['takes'].get(c['id'])
            if t and t['status']=='succeeded' and t.get('verification',{}).get('decode_verified'):normalized(c,t);print(c['id'],'normalized',flush=True)
        return
    final=ROOT/'exports/somewhere-between-us-new-short-720p-21x9.mp4'
    total=sum(c['duration'] for c in p['chapters'])
    if a.command=='assemble':
        assert len(chapters)==len(p['chapters']) and total==352
        if final.exists():raise ValueError('Existing final is preserved; verify it or choose a new assembly version')
        files=[];manifest=[]
        for c in chapters:
            t=j['takes'].get(c['id'])
            if not t or t['status']!='succeeded' or not t.get('verification',{}).get('decode_verified'):raise ValueError('Missing inspected take '+c['id'])
            if c.get('active_take_id')!=t['id']:raise ValueError('Canonical selection must match inspected take '+c['id'])
            files.append(normalized(c,t));manifest.append({'chapter_id':c['id'],'take_id':t['id'],'start':c['absolute_start'],'end':c['absolute_end']});print(c['id'],'ready',flush=True)
        listing=ROOT/'exports/assembly-v01/concat.txt';listing.write_text('\n'.join("file '"+f.as_posix()+"'" for f in files)+'\n',encoding='utf-8')
        temp=final.with_name(final.stem+'-assembling.mp4')
        run(['-v','error','-f','concat','-safe','0','-i',listing,'-vf','setpts=N/(30*TB)',
             '-af',f'atrim=duration={total},asetpts=PTS-STARTPTS,loudnorm=I=-20:TP=-1.5:LRA=11',
             '-t',total,'-r','30','-fps_mode','cfr','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p',
             '-c:a','aac','-ar','48000','-ac','2','-b:a','192k','-map_metadata','-1','-movflags','+faststart',temp])
        temp.replace(final)
        h.atomic_write(ROOT/'exports/assembly-manifest.json',{'inputs':manifest,'runtime_goal':total,'output':final.relative_to(ROOT).as_posix(),
            'native_inputs':'720p provider profile, typically 1470x630; originals retained','final_resolution':[1680,720],
            'resizing':'Uniform Lanczos upscale to exact 21:9 at 720 pixels high; no crop or letterbox',
            'titles':False,'credits':False,'cuts':'Hard cuts; no crossfade runtime changes',
            'audio':'Native synchronized audio retained except chapter28 uses locally synthesized original wind and paw sounds; stereo48kHz, 40ms edge fades, integrated target -20 LUFS / true peak -1.5dB'} )
    v=probe(final);v.update(decode(final));v['file_bytes']=final.stat().st_size
    v['passes']=v['resolution']==[1680,720] and abs(v['duration_seconds']-total)<0.02 and v['fps']==30 and v['frame_count']==total*30 and bool(v['audio_stream'])
    if not v['passes']:raise ValueError('Final technical verification failed '+str(v))
    level=run(['-v','info','-i',final,'-map','0:a:0','-af','loudnorm=I=-20:TP=-1.5:LRA=11:print_format=json','-vn','-f','null','-']).stderr
    block=re.findall(r'\{\s*"input_i".*?\}',level,re.S)
    if block:v['audio_loudness']=json.loads(block[-1])
    h.atomic_write(ROOT/'exports/video-verification.json',v)
    print('Final technical verification:',json.dumps(v),flush=True)
if __name__=='__main__':main()
