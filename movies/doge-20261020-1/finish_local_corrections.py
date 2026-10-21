"""A 1.5-second editorial reframe of the generated paw-promise memory, preserving time/audio."""
import argparse,hashlib,subprocess,sys
from PIL import Image,ImageDraw,ImageFont
from render_finale import ROOT,FF,read,save,journal,inspect_technical
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--approve',action='store_true');args=ap.parse_args()
    p=read(ROOT/'project.json');c=next(c for c in p['chapters'] if c['id']=='scene_43');t=journal()['takes'][c['id']];src=ROOT/t['path'];out=src.with_name(t['id']+'_reframe01.mp4')
    folder=ROOT/'exports/clip-inspection/scene_43/reframe01';folder.mkdir(parents=True,exist_ok=True)
    if not out.exists():
        filt='[0:v]split=3[a][b][c];[a]trim=end=7.5,setpts=PTS-STARTPTS[pre];[b]trim=start=7.5:end=9,setpts=PTS-STARTPTS,crop=466:200:263:20,scale=992:432,setsar=1[mid];[c]trim=start=9:end=23,setpts=PTS-STARTPTS[post];[pre][mid][post]concat=n=3:v=1:a=0,fps=24[v]'
        r=subprocess.run([str(FF),'-hide_banner','-loglevel','error','-nostdin','-i',str(src),'-filter_complex',filt,'-map','[v]','-map','0:a:0','-t','23','-c:v','libx264','-crf','18','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',str(out)],capture_output=True)
        if r.returncode:raise RuntimeError(r.stderr.decode('utf-8','replace')[-1200:])
    verification=inspect_technical(out,t)
    frames=[]
    for i,sec in enumerate([7.4,7.55,8.2,8.85,9.1]):
        f=folder/f'{sec:.2f}.jpg'
        if not f.exists():
            subprocess.run([str(FF),'-hide_banner','-loglevel','error','-nostdin','-ss',str(sec),'-i',str(out),'-frames:v','1','-q:v','2',str(f)],check=True)
        frames.append((sec,f))
    sheet=Image.new('RGB',(1488,488),'#142025');d=ImageDraw.Draw(sheet);font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17)
    for i,(sec,f) in enumerate(frames):
        im=Image.open(f);im.thumbnail((496,216));x=i%3*496;y=i//3*244;sheet.paste(im,(x,y));d.text((x+7,y+219),f'Scene43 reframe01 {sec:.2f}s',font=font,fill='white')
    sheet.save(folder/'contact.jpg',quality=94);print(folder/'contact.jpg')
    if args.approve:
        save(ROOT/'exports/local-edits/scene_43_reframe01.json',{'id':'edit_reframe01','chapter_id':c['id'],'kind':'local_editorial_reframe','status':'succeeded','path':out.relative_to(ROOT).as_posix(),'duration':23,'source_video_take_id':t['id'],'source_video_path':t['path'],'source_video_sha256':sha(src),'source_audio_path':t['path'],'source_audio_sha256':sha(src),'dependency_fingerprint':helper.chapter_fingerprint(ROOT,p,c),'verification':verification,'edit':'Only7.5-9.0s reframed to a tight view of the two touching puppy paws; removes extraneous model-generated human hands below the paws. All other frames retain source framing. Normal speed, same duration and source audio.','visual_review':{'inspected':True,'requires_repair':False,'source_sha256':sha(out),'notes':'Original full clip inspected and five actual edit-boundary/memory frames inspected after reframe; crop excludes extraneous human hands while retaining the two touching puppy paws.'}})
        print('Recorded inspected local reframe')
if __name__=='__main__':main()
