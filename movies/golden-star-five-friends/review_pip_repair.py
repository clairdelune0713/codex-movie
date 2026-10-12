"""Dense actual-video character review; galleries are never generation inputs."""
import json
import math
from pathlib import Path
from finish_movie import ROOT, OUT, FFMPEG, run, frame, contact_sheet, probe, full_decode, audio_stats, write, read

FIX=OUT/'pip-fix-20261012'
BASELINE=read(FIX/'baseline-project.json')
TARGETS=BASELINE.get('pip_correction',{}).get('affected_chapters') or ['chapter_01','chapter_03','chapter_04','chapter_06','chapter_07']

def main():
    p=read(ROOT/'project.json')
    report_file=FIX/'technical-review.json'
    report=read(report_file) if report_file.exists() else {'takes':{}}
    rows=[]
    for c in p['chapters']:
        if c['id'] not in TARGETS:
            continue
        original=next(x for x in BASELINE['chapters'] if x['id']==c['id'])
        old_ids={t['id'] for t in original['takes']}
        candidates=[t for t in c['takes'] if t['id'] not in old_ids and t['status']=='succeeded' and t.get('path')]
        if not candidates:
            continue
        t=candidates[-1]
        if t['id'] in report['takes']:
            continue
        source=ROOT/t['path']
        metadata=probe(source)
        video=next(s for s in metadata['streams'] if s['codec_type']=='video')
        audio=next((s for s in metadata['streams'] if s['codec_type']=='audio'),None)
        if not audio and t.get('generate_audio',True):
            raise RuntimeError('Missing generated audio: '+t['id'])
        if float(video.get('duration',metadata['format']['duration']))<c['duration']-0.15:
            raise RuntimeError('Generated take too short: '+t['id'])
        if audio:
            decode=full_decode(source)
            stats=audio_stats(source)
        else:
            result=run([FFMPEG,'-hide_banner','-v','error','-i',source,'-map','0:v:0','-f','null','-'])
            decode={'passed':True,'diagnostic':result.stderr.decode(errors='replace').strip(),'video_only_by_design':True}
            stats={'generated_audio':False,'delivery_audio_source':'Original verified 120-second movie soundtrack'}
        samples=[]
        for index in range(math.ceil(c['duration']*2)):
            stamp=min(index*.5+.1,c['duration']-.1)
            target=FIX/'frames'/t['id']/f'{index:03d}_{stamp:05.1f}s.jpg'
            frame(source,stamp,target)
            samples.append({'path':target.relative_to(ROOT).as_posix(),'time':stamp,'movie_time':c['absolute_start']+stamp})
        galleries=[]
        for start in range(0,len(samples),12):
            page=samples[start:start+12]
            target=FIX/'galleries'/f'{t["id"]}_page_{start//12+1:02d}.jpg'
            target.parent.mkdir(exist_ok=True,parents=True)
            contact_sheet([(ROOT/x['path'],f"{x['movie_time']:.1f}s movie / {x['time']:.1f}s clip") for x in page],target,'Pip full-body and single-chick check - '+t['id'],columns=3,width=640,height=390)
            galleries.append(target.relative_to(ROOT).as_posix())
        report['takes'][t['id']]={'chapter_id':c['id'],'path':t['path'],'probe':metadata,'full_decode':decode,'audio':stats,'dense_sample_interval_seconds':.5,'frames':samples,'galleries':galleries,'manual_visual_status':'pending'}
        write(report_file,report)
        rows.append({'take':t['id'],'size':[video['width'],video['height']],'duration':metadata['format']['duration'],'galleries':galleries})
    print(json.dumps({'new_reviews':rows,'completed_technical_reviews':list(report['takes'])},indent=2))

if __name__=='__main__':
    main()
