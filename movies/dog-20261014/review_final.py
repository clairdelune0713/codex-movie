"""Inspect actual assembled movie samples and write factual delivery notes."""
import json,subprocess
from PIL import Image,ImageDraw,ImageFont,ImageOps
from render_movie import ROOT,FF,read
p=read(ROOT/'project.json');v=read(ROOT/'exports/verification.json')
assert p['render_status']=='completed' and v['frame_count']==28800 and v['decode_verified']
movie=ROOT/v['file'];folder=ROOT/'exports/final-review';folder.mkdir(parents=True,exist_ok=True)
chosen={1:0.3,12:8,15:12,48:10,63:12,70:8};elapsed=0;items=[]
for c in p['chapters']:
    if c['chapter_index'] in chosen:
        seconds=elapsed+chosen[c['chapter_index']];dest=folder/(c['id']+'.jpg')
        subprocess.run([str(FF),'-v','error','-ss',str(seconds),'-i',str(movie),'-frames:v','1','-q:v','2','-y',str(dest)],check=True)
        items.append((c['id'],seconds,dest))
    elapsed+=c['duration']
canvas=Image.new('RGB',(1290,810),'#f3f0e9');draw=ImageDraw.Draw(canvas)
font=ImageFont.truetype('C:/Windows/Fonts/msyh.ttc',18)
for n,(cid,sec,path) in enumerate(items):
    x=10+(n%2)*640;y=10+(n//2)*267
    draw.text((x,y),cid+' | '+str(sec)+'s in actual assembled movie',font=font,fill='#213b39')
    frame=Image.open(path).convert('RGB');frame=ImageOps.contain(frame,(625,235));canvas.paste(frame,(x,y+27))
canvas.save(folder/'actual-movie-samples.jpg',quality=94)
ledger=read(ROOT/'usage.json');session=ledger['sessions'][-1]
report=read(ROOT/'exports'/('usage-report-'+session['id']+'.json'))
cost=report['project_total']['seedance_cost']['currencies']['USD']['estimated']
seconds=int(report['project_total']['elapsed_seconds']);h,rem=divmod(seconds,3600);m,s=divmod(rem,60)
notes=f'''# dog-20261014 production notes

Movie: `dog-20261014-480p.mp4` (about {movie.stat().st_size/1000000:.1f} MB).

The video stream is exactly 20:00: 28,800 frames at 24 fps, 854×480, 16:9 display, H.264. Stereo AAC audio is 48 kHz. The MP4 container reports {v['duration']:.2f} seconds due to audio packet rounding. Full decoding passed. No author, opening/end title, subtitle, credit or final slogan was added; metadata was stripped.

All 70 selected chapters were sampled for visual review. All 107 supplied dialogue entries remain in order in the directed prompts. Native speech was checked with local Cantonese ASR; that check cannot establish word-perfect speech or stable voices. Minor generated group wardrobe/pose variations and occasional natural adlibs remain. This is a completed generated movie cut, with the retained takes available for further iteration.

The approved Bo, mother/Lok, street/ferry cast, car door, green/cream tram, single crossing signal and harness-guidance revisions are retained. The ferry conversation uses original adult/dog coverage with the child's original lines offscreen after the provider rejected earlier outputs for copyright restrictions. Photo recognition uses close human/physical-photo coverage. A conventional local crop removes a duplicated child, and a wordless forecourt shot uses native harbour ambience from this project. No external image-generation API was used.

Four unchanged approved PNGs were registered in BytePlus through user-approved one-hour Litterbox links. BytePlus default moderation remained enabled. Active asset bindings and exact source hashes are saved. Temporary staging expires according to the host; private registered references are retained for reproducible future renders.

Seedance generation estimate: **USD {float(cost):.2f}**, across {report['project_total']['seedance_cost']['attempts']} recorded attempts including discarded/failed attempts, using returned completion tokens and the published 480p list rate. This is not an invoice. No unknown-charge attempts remain. Wall-clock production session: **{h}h {m}m {s}s**, including queues and approval waits; session and project totals are equal.

The initial assembly was one frame short in the local child crop. That clip was corrected by extending its final frame by 1/24 second, and the corrected full movie passed the frame-count/decode checks. The first export is retained separately as `assembly-attempt-01-28799frames.mp4`.

One clerical continuity-frame timestamp is corrected transparently in `provenance-timestamp-errata.json`; independent extraction confirms the exact correct JPEG bytes were sent. Original accepted prompts, picture inputs and attempt fingerprints were not rewritten.

Evidence: `verification.json`, `assembly-settings.json`, `audio-mastering-analysis.json`, `visual-reviews.json`, `task-journal.json`, `director-script-current.md`, `provenance-timestamp-errata.json`, and the session usage report. Source materials remain under `source/SOMEWHERE_BETWEEN_US_READY`; immutable assets, takes and history remain in the project.
'''
(ROOT/'exports/PRODUCTION-NOTES.md').write_text(notes,encoding='utf-8')
(ROOT/'STATUS.md').write_text('Completed: exports/dog-20261014-480p.mp4\n20-minute video stream, 854x480, 16:9, 24fps, stereo audio; 28,800 frames and full decoding verified.\nAll 70 chapters have inspected current selections. See exports/PRODUCTION-NOTES.md and exports/verification.json.\n',encoding='utf-8')
print({'final_samples':str(folder/'actual-movie-samples.jpg'),'cost_estimate_usd':round(float(cost),2),'elapsed':f'{h}h {m}m {s}s'})
