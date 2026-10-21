"""Stitch ONLY inspected selected source scenes37-51; no generation calls."""
from pathlib import Path
import argparse,hashlib,json,math,re,subprocess,sys
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent
FF=ROOT/'tools/ffmpeg.exe'
sys.path.insert(0,str(ROOT))
from render_finale import probe,save,scene_number,scope_chapters
SKILL=Path('C:/Users/Admin 3/.codex/skills/movi2/scripts')
sys.path.insert(0,str(SKILL))
import project as helper
FPS=24

def ff(args):
    r=subprocess.run([str(FF),'-hide_banner','-loglevel','error','-nostdin',*map(str,args)],capture_output=True,text=True,encoding='utf-8',errors='replace')
    if r.returncode:raise RuntimeError('Assembly failed: '+r.stderr[-1800:])
    return r
def font(size,bold=False):return ImageFont.truetype('C:/Windows/Fonts/'+('arialbd.ttf' if bold else 'arial.ttf'),size)
def centered(draw,xy,text,f,fill):
    box=draw.textbbox((0,0),text,font=f);draw.text((xy[0]-(box[2]-box[0])/2,xy[1]),text,font=f,fill=fill)
def graphics(w,h,folder):
    folder.mkdir(parents=True,exist_ok=True)
    s=w/992
    for name,text in [('harbour-caption','Victoria Harbour. Friday.'),('friday-caption','Next Friday.')]:
        im=Image.new('RGBA',(w,h),(0,0,0,0));d=ImageDraw.Draw(im)
        f=font(round(23*s),True);box=d.textbbox((0,0),text,font=f);tw=box[2]-box[0]
        d.rounded_rectangle((w/2-tw/2-20*s,h-67*s,w/2+tw/2+20*s,h-22*s),radius=12*s,fill=(20,39,45,180))
        centered(d,(w/2,h-58*s),text,f,(255,245,223,255));im.save(folder/(name+'.png'))
    base=Image.new('RGB',(w,h),'#f3e3bd');d=ImageDraw.Draw(base)
    d.rounded_rectangle((14*s,14*s,w-14*s,h-14*s),radius=20*s,outline='#9c7952',width=round(2*s))
    # Equal horizontal/vertical angular scale keeps the hand-drawn landforms recognizable.
    def xy(lon,lat):
        unit=(h-70*s)/95
        return ((lon-125)*unit+w*.47,(45-lat)*unit+35*s)
    asia=[(85,45),(148,45),(142,35),(132,31),(125,28),(122,20),(115,20),(110,13),(106,7),(100,11),(95,22),(85,25)]
    aus=[(113,-22),(114,-26),(114,-29),(115,-31),(115,-34),(118,-35),(122,-34),(125,-32),(129,-31),(132,-32),(134,-34),(136,-35),(138,-35),(140,-38),(145,-39),(147,-38),(150,-37),(151,-34),(153,-29),(153,-25),(150,-22),(146,-19),(145,-16),(144,-11),(142,-10),(141,-13),(142,-16),(140,-17),(138,-17),(137,-15),(136,-12),(133,-12),(130,-12),(129,-15),(127,-15),(125,-14),(123,-16),(122,-18),(119,-20),(116,-20),(114,-21)]
    for land in (asia,aus):d.polygon([xy(*pt) for pt in land],fill='#c4c58a',outline='#74866a',width=round(3*s))
    cx,cy=w*.18,h*.55
    d.line((cx,cy-48*s,cx,cy+48*s),fill='#b89d73',width=round(2*s));d.line((cx-40*s,cy,cx+40*s,cy),fill='#b89d73',width=round(2*s))
    d.polygon([(cx,cy-36*s),(cx-8*s,cy+9*s),(cx,cy+3*s),(cx+8*s,cy+9*s)],fill='#9c5142')
    centered(d,(cx,cy-72*s),'N',font(round(18*s),True),'#8e7454')
    d.ellipse((xy(145,-41)[0]-4*s,xy(145,-41)[1]-3*s,xy(145,-41)[0]+4*s,xy(145,-41)[1]+4*s),fill='#c4c58a',outline='#74866a')
    v=xy(144.96,-37.81);hk=xy(114.17,22.30);control=(w*.86,h*.30)
    route=[]
    for i in range(50):
        t=i/49;route.append(((1-t)**2*v[0]+2*(1-t)*t*control[0]+t*t*hk[0],(1-t)**2*v[1]+2*(1-t)*t*control[1]+t*t*hk[1]))
    for point in [v,hk]:d.ellipse((point[0]-5*s,point[1]-5*s,point[0]+5*s,point[1]+5*s),fill='#9c5142')
    d.text((v[0]-150*s,v[1]+12*s),'VICTORIA, AUSTRALIA',font=font(round(15*s),True),fill='#344d4b')
    d.text((hk[0]-90*s,hk[1]-28*s),'VICTORIA HARBOUR, HONG KONG',font=font(round(15*s),True),fill='#344d4b')
    for frame in range(84):
        im=base.copy();draw=ImageDraw.Draw(im);progress=min(1,(frame+1)/65)
        for i,(x,y) in enumerate(route):
            if i/49<=progress and i%2==0:draw.ellipse((x-3*s,y-3*s,x+3*s,y+3*s),fill='#ae4c3c')
        if progress>=1:
            for delta in (0,18*s):
                x=hk[0]+15*s+delta;y=hk[1]+16*s
                draw.ellipse((x,y,x+10*s,y+12*s),fill='#7a5946')
                for dx,dy in [(-2,-4),(3,-8),(9,-7),(13,-2)]:draw.ellipse((x+dx*s,y+dy*s,x+(dx+4)*s,y+(dy+4)*s),fill='#7a5946')
        im.save(folder/f'map-{frame:04d}.png')
    title=Image.new('RGB',(w,h),'#f3e3bd');td=ImageDraw.Draw(title)
    centered(td,(w/2,h*.28),'TART & TINE',font(round(69*s),True),'#3b5350')
    centered(td,(w/2,h*.54),'From Victoria to Victoria',font(round(30*s)),'#93684a')
    td.line((w*.28,h*.72,w*.72,h*.72),fill='#ba956a',width=round(2*s));title.save(folder/'title.png')
    return folder

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--prepare-graphics',action='store_true');ap.add_argument('--version',default='v01');args=ap.parse_args()
    if args.prepare_graphics:
        print(graphics(992,432,ROOT/'exports/finishing-graphics'));return
    p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));chapters=scope_chapters(p);selected=[]
    for c in chapters:
        t=next((t for t in c['takes'] if t['id']==c.get('active_take_id')),None)
        if not t or t.get('status')!='succeeded' or not t.get('visual_review',{}).get('inspected') or t['visual_review'].get('requires_repair'):
            raise RuntimeError(c['id']+' needs an inspected successful selected take')
        if t.get('dependency_fingerprint')!=helper.chapter_fingerprint(ROOT,p,c):raise RuntimeError(c['id']+' selected take is stale')
        src=ROOT/t['path'];info=probe(src)
        if not info['audio'] or info['duration']<c['duration']-.04:raise RuntimeError(c['id']+' source duration/audio invalid')
        selected.append((c,t,src,info))
    assert sum(c['duration'] for c in chapters)==305
    w,h=selected[0][3]['width'],selected[0][3]['height']
    if any((i['width'],i['height'])!=(w,h) for _,_,_,i in selected):raise RuntimeError('Native dimensions differ')
    if (w,h)!=(992,432):raise RuntimeError('Unexpected native480p21:9 profile; inspect before assembly')
    g=graphics(w,h,ROOT/'exports/finishing-graphics');work=ROOT/'exports'/('finishing-'+args.version);work.mkdir(parents=True,exist_ok=True)
    manifest=[];normalized=[];offset=0
    for c,t,src,info in selected:
        n=scene_number(c);duration=c['duration'];target=work/(c['id']+'_'+t['id']+'.mp4')
        if target.exists():raise RuntimeError('Preserve existing edit; use a new finishing version')
        cmd=['-i',src]
        v=f'fps={FPS},trim=duration={duration},setpts=N/({FPS}*TB),setsar=63/62'
        if n in (37,49):
            caption=g/('harbour-caption.png' if n==37 else 'friday-caption.png');cmd+=['-loop','1','-i',caption]
            cmd+=['-filter_complex',f'[0:v]{v}[base];[base][1:v]overlay=0:0:enable=\'between(t,0.5,4.5)\'[v]','-map','[v]','-map','0:a:0']
        elif n==50:
            # Use the real upward camera move, then cover its held end entirely with graphics.
            v=f'trim=start=3.5:end=6,setpts=PTS-STARTPTS,fps={FPS},tpad=stop_mode=clone:stop_duration=6.5,trim=duration=9,setsar=63/62'
            cmd+=['-framerate',str(FPS),'-i',g/'map-%04d.png','-loop','1','-i',g/'title.png']
            filt=f'[0:v]{v}[base];[1:v]setpts=PTS-STARTPTS+2.5/TB[map];[base][map]overlay=0:0:enable=\'between(t,2.5,6)\'[mapped];[mapped][2:v]overlay=0:0:enable=\'gte(t,6)\'[v]'
            cmd+=['-filter_complex',filt,'-map','[v]','-map','0:a:0']
        else:
            if n==41:
                # A modest first-shot reframe excludes the model's unsolicited subtitle.
                v+=",scale=w='if(lt(t,4),1140,992)':h='if(lt(t,4),496,432)':eval=frame,crop=992:432:(iw-992)/2:0,setsar=63/62"
            if n==48:
                match="lt(t,4.95)+between(t,16.08,20.05)"
                v+=f",colorbalance=rs=-0.05:bs=0.08:rm=-0.12:gm=-0.03:bm=0.18:rh=-0.45:gh=-0.25:bh=0.3:enable='{match}',eq=brightness=-0.03:gamma=0.98:saturation=0.85:enable='{match}'"
            if n==51:v+=",drawbox=x=0:y=0:w=iw:h=ih:color=black:t=fill:enable='gte(t,5.958333)'"
            cmd+=['-vf',v,'-map','0:v:0','-map','0:a:0']
        cmd+=['-af',f'aresample=48000,atrim=duration={duration},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={duration-.012}:d=0.012','-t',str(duration),'-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),'-fps_mode','cfr','-aspect','21:9','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',target]
        ff(cmd);normalized.append(target)
        manifest.append({'chapter_id':c['id'],'source_scene_number':n,'source_take_id':t['id'],'source_path':t['path'],'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'start':offset,'end':offset+duration,'duration':duration,'edit_path':target.relative_to(ROOT).as_posix(),'video_filter':v,'finishing':{37:'Scripted harbour caption',41:'First4s modest reframe to exclude unsolicited generated subtitle',48:'Two warm shots color-matched to surrounding night shots at actual cut boundaries',49:'Scripted Next Friday caption',50:'Moving aerial from source3.5-6.0s, then animated map2.5-6s and title6-9s',51:'One-frame final cut to black'}.get(n,'Normal-speed trim and native-canvas normalization')});offset+=duration
        print('Finished',c['id'],flush=True)
    concat=work/'concat.txt';concat.write_text('\n'.join("file '"+x.as_posix().replace("'","'\\''")+"'" for x in normalized)+'\n',encoding='utf-8')
    output=ROOT/'exports'/f'doge-20261020-1-scenes-37-51-480p-21x9-{args.version}.mp4'
    if output.exists():raise RuntimeError('Never overwrite delivered video')
    ff(['-f','concat','-safe','0','-i',concat,'-vf',f'setpts=N/({FPS}*TB),setsar=63/62','-af','aresample=48000,atrim=duration=305,asetpts=PTS-STARTPTS','-t','305','-r',str(FPS),'-fps_mode','cfr','-aspect','21:9','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',output])
    info=probe(output);r=ff(['-threads','2','-i',output,'-progress','pipe:1','-f','null','-']);counts=re.findall(r'^frame=(\d+)',r.stdout,re.M);frames=int(counts[-1]) if counts else None
    if frames!=7320 or abs(info['duration']-305)>.05:raise RuntimeError('Final duration/frame check failed')
    save(ROOT/'exports/finale-assembly-manifest.json',{'scope':'source scenes37-51 ONLY','duration_seconds':305,'requested_profile':'480p21:9','native_dimensions':[w,h],'display_aspect_ratio':'21:9','square_pixel_resampling':False,'chapters':manifest,'path':output.relative_to(ROOT).as_posix(),'verification':{**info,'decoded_frames':frames,'full_decode_verified':True},'editing':'Hard cuts, normal-speed action, source-script map/title/captions composited locally; original generated audio retained.'})
    print(output);print(json.dumps({**info,'frames':frames},indent=2))
if __name__=='__main__':main()
