import json
from pathlib import Path
from finish_movie import ROOT, OUT, frame, contact_sheet, read, write

path=OUT/'five-little-friends-golden-star-120s-720p.mp4'
stamps=[3,18,39,51,59,67,82,86.5,95,105,111,119]
frames=[]
for i,stamp in enumerate(stamps):
    output=OUT/'final-frames'/f'frame_{i:02}_{stamp:05.1f}s.jpg'
    frame(path,stamp,output)
    frames.append((output,f'Movie time {stamp:.1f}s'))
contact_sheet(frames,OUT/'final-frame-review.jpg','Final edited film - actual decoded frames',columns=4)
report=read(OUT/'final-verification.json')
report['final_sample_frame_times']=stamps
report['final_contact_sheet']='exports/final-frame-review.jpg'
report['assembly']['framing_edits']={'chapter_06':{'start':13,'end':17,'crop':[480,130,800,450],'purpose':'Clean hero close-up on Lulu and star; duplicated chick in the original full-width close-up is fully out of frame.'}}
write(OUT/'final-verification.json',report)
print(json.dumps({'final_frames_saved':len(stamps),'contact_sheet':str(OUT/'final-frame-review.jpg')}))
