"""Original procedural wind and soft paw sounds; no recordings or melodies."""
import math, random, struct, subprocess, wave
from pathlib import Path
FF=Path('C:/Users/admina/Downloads/project/dog-test/.tools/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe')

def mux(source, destination, duration):
    if destination.exists():return
    wav=destination.with_name(destination.stem+'_original-ambience.wav')
    rate=48000;generator=random.Random(910928);filtered=[0.0,0.0];data=bytearray()
    steps=[1.1,1.7,2.3,2.9,6.7,7.4]
    for i in range(round((duration+0.15)*rate)):
        t=i/rate;edge=min(1,t/0.06,max(0,(duration+0.15-t)/0.06))
        for side in range(2):
            noise=generator.uniform(-1,1);filtered[side]=0.975*filtered[side]+0.025*noise
            breeze=filtered[side]*0.075*(0.7+0.3*math.sin(2*math.pi*0.13*t+side*0.3))
            paws=0.0
            for at in steps:
                age=t-at
                if 0<=age<0.13:
                    pan=0.7 if (at<6 and side==0) or (at>=6 and side==1) else 0.4
                    paws+=pan*0.042*math.exp(-age*38)*(0.65*math.sin(2*math.pi*105*age)+0.35*noise)
            value=max(-1,min(1,(breeze+paws)*edge));data.extend(struct.pack('<h',round(value*32767)))
    with wave.open(str(wav),'wb') as f:
        f.setnchannels(2);f.setsampwidth(2);f.setframerate(rate);f.writeframes(data)
    temporary=destination.with_name(destination.stem+'_muxing.mp4')
    r=subprocess.run([str(FF),'-hide_banner','-v','error','-i',str(source),'-i',str(wav),'-map','0:v:0','-map','1:a:0',
       '-c:v','copy','-c:a','aac','-b:a','192k','-shortest','-map_metadata','-1','-movflags','+faststart',str(temporary)],capture_output=True,text=True)
    if r.returncode:raise RuntimeError('Original ambience mux failed: '+r.stderr[-2000:])
    temporary.replace(destination)
