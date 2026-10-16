"""Track and composite the original supplied emblem as a video layer.

The source PNG is read unchanged. No replacement reference image is generated.
"""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from render_movie import ROOT,FF,read,save,helper,inspect_technical
sys.path.insert(0,str(ROOT/'tools/vision-deps'))
import cv2
import numpy as np

def candidates(frame,roi):
    x0,y0,x1,y1=roi;im=frame[y0:y1,x0:x1]
    hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    white=((hsv[:,:,1]<90)&(hsv[:,:,2]>135)).astype(np.uint8)*255
    white=cv2.morphologyEx(white,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
    contours,_=cv2.findContours(white,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    found=[]
    for co in contours:
        x,y,w,h=cv2.boundingRect(co)
        if min(w,h)<12 or max(w,h)>200 or not .55<w/h<1.65:continue
        rh=hsv[y:y+h,x:x+w]
        red=(((rh[:,:,0]<9)|(rh[:,:,0]>172))&(rh[:,:,1]>85)&(rh[:,:,2]>60)).mean()
        if red<.025:continue
        halo=hsv[max(0,y-7):min(im.shape[0],y+h+7),max(0,x-7):min(im.shape[1],x+w+7)]
        orange=((halo[:,:,0]>3)&(halo[:,:,0]<25)&(halo[:,:,1]>105)).mean()
        if orange<.12:continue
        found.append((x+x0,y+y0,w,h))
    return found

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--chapter',type=int,required=True);ap.add_argument('--seed',required=True);ap.add_argument('--roi',required=True)
    ap.add_argument('--start',type=float,default=0);ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    p=read(ROOT/'project.json');j=read(ROOT/'exports/task-journal.json');c=p['chapters'][args.chapter-1];t=j['takes'][c['id']]
    assert t['status']=='succeeded'
    roi=tuple(map(int,args.roi.split(',')));previous=np.array(list(map(float,args.seed.split(','))))
    source=ROOT/t['path'];a=next(a for a in p['asset_list'] if a['id']=='asset_039');selected=helper.selected_media(a);png=ROOT/selected['path']
    original=cv2.imdecode(np.frombuffer(png.read_bytes(),np.uint8),cv2.IMREAD_COLOR);hh,ww=original.shape[:2]
    # Exact circular detail visible in the approved prop sheet: normalized bounds.
    emblem=original[round(hh*.50):round(hh*.841),round(ww*.713):round(ww*.954)]
    hsv=cv2.cvtColor(emblem,cv2.COLOR_BGR2HSV)
    # Locate outer red rim in the detail tile; preserve all source pixels inside.
    rim=((hsv[:,:,0]<10)|(hsv[:,:,0]>170))&(hsv[:,:,1]>80)
    contours,_=cv2.findContours(rim.astype(np.uint8)*255,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    ring=max(contours,key=cv2.contourArea);(cx,cy),radius=cv2.minEnclosingCircle(ring)
    left=max(0,int(cx-radius));top=max(0,int(cy-radius));side=min(int(radius*2+2),emblem.shape[1]-left,emblem.shape[0]-top)
    emblem=emblem[top:top+side,left:left+side]
    yy,xx=np.mgrid[:side,:side];alpha=np.clip((side/2-1-np.sqrt((xx-side/2)**2+(yy-side/2)**2))/1.5,0,1).astype(np.float32)
    folder=ROOT/'exports/badge-correction';folder.mkdir(parents=True,exist_ok=True)
    duration=min(3,c['duration']) if args.pilot else c['duration']
    dest=folder/f"{c['id']}_{t['id']}_{'pilot' if args.pilot else 'badge'}.mp4"
    if dest.exists():raise RuntimeError('Keep the existing edited media; choose a new version filename before another correction.')
    temp=dest.with_name(dest.stem+'.encoding.mp4')
    dec=subprocess.Popen([str(FF),'-v','error','-threads','2','-i',str(source),'-t',str(duration),'-vf','format=bgr24','-f','rawvideo','pipe:1'],stdout=subprocess.PIPE)
    enc=subprocess.Popen([str(FF),'-v','error','-nostdin','-y','-f','rawvideo','-pixel_format','bgr24','-video_size','1920x1080','-framerate','24','-i','pipe:0','-i',str(source),
        '-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','fast','-crf','18','-threads','4','-c:a','copy','-t',str(duration),str(temp)],stdin=subprocess.PIPE)
    detected=0;required=0;positions=[];frame_no=0
    while True:
        raw=dec.stdout.read(1920*1080*3)
        if not raw:break
        if len(raw)!=1920*1080*3:raise RuntimeError('Incomplete frame')
        frame=np.frombuffer(raw,np.uint8).reshape((1080,1920,3)).copy()
        if frame_no/24>=args.start:
            required+=1;found=candidates(frame,roi)
            found=sorted(found,key=lambda b:np.linalg.norm(np.array([b[0]+b[2]/2,b[1]+b[3]/2])-previous[:2]))
            if found:
                x,y,w,h=found[0];center=np.array([x+w/2,y+h/2])
                if np.linalg.norm(center-previous[:2])<100:
                    size=max(w,h)+6
                    # Source rim remains a circle; a rounded source texture avoids
                    # any newly drawn interpretation of the supplied GD mark.
                    x=int(center[0]-size/2);y=int(center[1]-size/2)
                    if 0<=x and 0<=y and x+size<=1920 and y+size<=1080:
                        layer=cv2.resize(emblem,(size,size),interpolation=cv2.INTER_AREA)
                        mask=cv2.resize(alpha,(size,size))[:,:,None]
                        base=frame[y:y+size,x:x+size]
                        b_hsv=cv2.cvtColor(base,cv2.COLOR_BGR2HSV)
                        whites=base[(b_hsv[:,:,1]<55)&(b_hsv[:,:,2]>130)]
                        if len(whites)>20:
                            balance=np.clip(np.percentile(whites,80,axis=0)/240,.75,1.05)
                            layer=np.clip(layer.astype(np.float32)*balance,0,255).astype(np.uint8)
                        layer=cv2.GaussianBlur(layer,(5,5),1.2)
                        frame[y:y+size,x:x+size]=(layer*mask+base*(1-mask)).astype(np.uint8)
                        previous=center;detected+=1;positions.append([frame_no,x,y,size])
        enc.stdin.write(frame.tobytes());frame_no+=1
    dec.stdout.close();enc.stdin.close()
    if dec.wait() or enc.wait():raise RuntimeError('Video processing failed')
    temp.replace(dest)
    save(dest.with_suffix('.json'),{'chapter':c['id'],'source_take':t['id'],'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'asset_id':'asset_039','source_asset_sha256':hashlib.sha256(png.read_bytes()).hexdigest(),'source_original_unchanged':True,
        'processed_frames':frame_no,'eligible_frames':required,'corrected_frames':detected,'positions':positions,'inspected':False})
    print(dest,'coverage',detected,'/',required,flush=True)

if __name__=='__main__':main()
