"""Check rendered edit at every second in corrected ranges and splice edges."""
from finish_movie import ROOT, frame, contact_sheet, read, write

FIX=ROOT/'exports'/'pip-fix-20261012'

def main():
    final=FIX/'five-little-friends-golden-star-pip-corrected-v02.mp4'
    intervals=[(0,12),(30,58),(73,90),(90,108)]
    samples=[]
    for start,end in intervals:
        for stamp in range(start,end):
            time=stamp+.1
            path=FIX/'final-frames'/f'{time:06.2f}s.jpg'
            frame(final,time,path)
            samples.append((path,f'FINAL {time:.1f}s'))
    pages=[]
    for offset in range(0,len(samples),12):
        path=FIX/'galleries'/f'final-v02-page-{offset//12+1:02d}.jpg'
        contact_sheet(samples[offset:offset+12],path,'Final Pip correction - actual exported frames',columns=3,width=640,height=390)
        pages.append(path.relative_to(ROOT).as_posix())
    edges=[]
    for time in (11.9666,12.0,29.9666,30.0,45.9666,46.0,52.9666,53.0,55.9666,56.0,89.9666,90.0):
        path=FIX/'final-frames'/f'edge-{time:07.3f}s.jpg'
        frame(final,time,path)
        edges.append((path,f'FINAL {time:.3f}s boundary'))
    path=FIX/'galleries'/'final-v02-boundaries.jpg'
    contact_sheet(edges,path,'Final edit transition check',columns=3,width=640,height=390)
    pages.append(path.relative_to(ROOT).as_posix())
    write(FIX/'final-visual-review.json',{'status':'awaiting_manual_inspection','corrected_ranges':intervals,'sample_interval_seconds':1,'boundary_samples':12,'gallery_paths':pages,'frame_count':len(samples)+12})
    print('\n'.join(pages))

if __name__=='__main__':
    main()
