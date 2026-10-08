"""Inspect final-file frames and measure delivered sound, without another render."""
import importlib.util,json,re,shutil,hashlib
from pathlib import Path
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('a',ROOT/'assemble_movie.py');a=importlib.util.module_from_spec(s);s.loader.exec_module(a)
final=ROOT/'exports/somewhere-between-us-10min-720p-21x9.mp4'
v=a.h.read(ROOT/'exports/video-verification.json');assert v['passes']
folder=ROOT/'exports/final-review';folder.mkdir(exist_ok=True)
times=[12,24,47,72,94,114,134,154,174,186,213,234,254,274,294,314,324,345,375,392,414,434,456,474,495,513,535,550,573,598]
contact=Image.new('RGB',(1470,630),'#061220');draw=ImageDraw.Draw(contact)
frames=[]
for i,ts in enumerate(times):
    dest=folder/f'chapter_{i+1:02d}_final.jpg'
    a.run(['-v','error','-ss',ts,'-i',final,'-frames:v',1,'-update',1,dest])
    with Image.open(dest) as im:small=im.convert('RGB').resize((245,105))
    x=(i%6)*245;y=(i//6)*126;contact.paste(small,(x,y));draw.text((x+4,y+108),f'{i+1:02d}  {ts//60:02d}:{ts%60:02d}',fill='white')
    frames.append({'chapter':i+1,'timestamp':ts,'path':dest.relative_to(ROOT).as_posix()})
contact.save(folder/'final-overview.jpg',quality=92)
shutil.copy2(folder/'chapter_23_final.jpg',ROOT/'exports/poster.jpg')
output=a.run(['-v','info','-i',final,'-map','0:a:0','-af','loudnorm=I=-23:TP=-1.5:LRA=11:print_format=json','-vn','-f','null','-']).stderr
matches=re.findall(r'\{\s*"input_i".*?\}',output,re.S)
if not matches:raise RuntimeError('Loudness measurement missing')
measurement=json.loads(matches[-1]);measurement={k:float(value) for k,value in measurement.items() if k.startswith('input_')}
assert -26<=measurement['input_i']<=-20 and measurement['input_tp']<0
v.update(audio_loudness_measured=measurement,final_frame_samples=frames,final_overview_path=(folder/'final-overview.jpg').relative_to(ROOT).as_posix(),poster_path='exports/poster.jpg',sha256=hashlib.sha256(final.read_bytes()).hexdigest())
a.h.atomic_write(ROOT/'exports/video-verification.json',v)
manifest=a.h.read(ROOT/'exports/assembly-manifest.json');manifest['closing_footer_cover']={'movie_start':593,'movie_end':600,'rectangle':[0,563,1470,67],'purpose':'Cover unsolicited generated footer lettering; preserve native frame dimensions'};a.h.atomic_write(ROOT/'exports/assembly-manifest.json',manifest)
p=a.h.read(ROOT/'project.json');report=a.h.report(ROOT,p);a.h.atomic_write(ROOT/'exports/project-check.json',report)
assert not report['errors'] and not report['warnings']
plan=a.h.read(ROOT/'exports/submission-plan.json');plan.update(status='prepared_payload_plan',generation_state=p['render_state']['status'],actual_submission_journal='exports/seedance-journal.json');a.h.atomic_write(ROOT/'exports/submission-plan.json',plan)
print(json.dumps({'duration':v['duration_seconds'],'frames':v['frame_count'],'native_dimensions':v['resolution'],'sound_loudness':measurement,'project_errors':report['errors'],'project_warnings':report['warnings'],'file_bytes':v['file_bytes']}))
