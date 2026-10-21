"""Compose a new instrumental score from synthesized tones, without recordings.

No source track, sampled instrument, quoted tune, network or paid API is used.
The score is deliberately quiet; finishing ducks it beneath native dialogue.
"""
import hashlib,math,sys,wave
from pathlib import Path
import render_remaining as r
sys.path.insert(0,str(r.ROOT/'tools/asr-runtime'))
import numpy as np

SR=48000
ACTION={3,4,25,26,28,29,30,31,32,35,36}
TENDER={6,7,8,9,12,20,22,27,33,34}

def compose(c,target):
    n=c['chapter_index'];duration=c['duration'];rng=np.random.default_rng(20261016000+n)
    out=np.zeros((duration*SR,2),np.float32)
    bpm=132 if n in ACTION else 96 if n in TENDER else 116
    beat=60/bpm;bar=3*beat;scale=[0,2,4,7,9]
    roots=[60,65,57,67] if n not in TENDER else [60,57,65,67]
    events=[]
    def note(start,midi,length,gain,kind,pan=0):
        start=max(0,start);first=round(start*SR);count=min(round(length*SR),len(out)-first)
        if count<=0:return
        t=np.arange(count,dtype=np.float32)/SR;f=440*2**((midi-69)/12)
        if kind=='bass':
            signal=np.sin(2*np.pi*f*t)+.19*np.sin(4*np.pi*f*t)
            envelope=(1-np.exp(-t*100))*np.exp(-t*4)
        elif kind=='pluck':
            signal=sum(np.sin(2*np.pi*f*h*t+(.02*h))*math.exp(-.65*(h-1))/h for h in range(1,7))
            envelope=(1-np.exp(-t*700))*np.exp(-t*(7 if n in ACTION else 5))
        else:
            signal=np.sin(2*np.pi*f*t)+.22*np.sin(2*np.pi*f*2.756*t)+.08*np.sin(2*np.pi*f*5.404*t)
            envelope=(1-np.exp(-t*900))*np.exp(-t*7)
        signal=(signal*envelope*gain).astype(np.float32)
        out[first:first+count,0]+=signal*math.sqrt((1-pan)/2)
        out[first:first+count,1]+=signal*math.sqrt((1+pan)/2)
        events.append({'start':round(start,3),'midi':midi,'instrument':kind})
    degree=0
    for b,start in enumerate(np.arange(.15,duration,bar)):
        root=roots[b%4]
        note(start,root-24,beat*.95,.022,'bass')
        for pulse in [1,2]:
            for offset,pitch in enumerate([root,root+4,root+7]):
                note(start+pulse*beat+offset*.012,pitch,beat*.8,.007,'pluck',-.35)
        for pulse in ([.5,1.5,2.5] if n in ACTION else [.5,2]):
            degree=int(np.clip(degree+int(rng.choice([-2,-1,1,2])),0,9))
            pitch=72+scale[degree%5]+12*(degree//5)
            if b%4==3 and pulse>=2:pitch=72
            note(start+pulse*beat,pitch,beat*.8,.010 if n in TENDER else .013,'bell',.28)
    fade=min(.6,duration/8);samples=round(fade*SR)
    out[:samples]*=np.linspace(0,1,samples)[:,None]
    out[-samples:]*=np.linspace(1,0,samples)[:,None]
    peak=float(np.max(np.abs(out)));assert peak<.12
    pcm=(np.clip(out,-1,1)*32767).astype('<i2')
    with wave.open(str(target),'wb') as w:
        w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes(pcm.tobytes())
    return {'chapter_id':c['id'],'duration':duration,'sample_rate':SR,'channels':2,
        'bpm':bpm,'meter':'3/4','peak_dbfs':20*math.log10(peak),'events':events,
        'provenance':'Original deterministic composition from synthesized sine partials and exponential plucks. No recordings, audio references, songs, sampled instruments or external service.'}

def main():
    p=r.read(r.ROOT/'project.json');folder=r.ROOT/'exports/original-local-score-v01';folder.mkdir(exist_ok=True)
    manifest={}
    for c in p['chapters'][:36]:
        if not c.get('audio_finishing'):continue
        dest=folder/(c['id']+'.wav');meta=dest.with_suffix('.json')
        if dest.exists():record=r.read(meta)
        else:
            record=compose(c,dest);record['path']=dest.relative_to(r.ROOT).as_posix()
            record['sha256']=hashlib.sha256(dest.read_bytes()).hexdigest();r.save(meta,record)
        assert record['duration']==c['duration']
        manifest[c['id']]={k:v for k,v in record.items() if k!='events'}
    r.save(folder/'manifest.json',manifest)
    print('Composed',len(manifest),'original local score cues, no API calls.')

if __name__=='__main__':main()
