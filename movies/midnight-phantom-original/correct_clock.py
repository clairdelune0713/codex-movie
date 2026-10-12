"""Correct only the static clock insert; retain source animation and audio."""
import hashlib
import shutil
from assemble_movie import ROOT,helper,run,metadata,decode,signal
from project_ops import write_json
record=helper.read(ROOT/'exports/clock-correction-source.json')
image=ROOT/'exports/editorial/clock-1159-c01.png';image.parent.mkdir(parents=True,exist_ok=True)
if not image.exists():shutil.copy2(record['source_file'],image)
source=ROOT/'exports/normalized/chapter_06-take_01.mp4'
target=ROOT/'exports/normalized/chapter_06-take_01-clockfix.mp4'
temporary=target.with_name(target.stem+'.partial.mp4')
if not target.exists():
    filters="[1:v]scale=1470:630,setsar=1[clock];[0:v][clock]overlay=0:0:enable='gte(t,7.7)*lt(t,8.833333)':shortest=1,setsar=1[v]"
    run(['-hide_banner','-v','error','-y','-i',source,'-loop','1','-framerate','30','-i',image,'-filter_complex',filters,'-map','[v]','-map','0:a:0','-t','10','-r','30','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',temporary])
    info={**metadata(temporary),**decode(temporary),**signal(temporary)}
    if info['decoded_frames']!=300 or (info['width'],info['height'])!=(1470,630) or not info['audio_present']:raise RuntimeError('Clock correction verification failed')
    temporary.replace(target)
else:info={**metadata(target),**decode(target),**signal(target)}
edit={'chapter_id':'chapter_06','source_take_id':'take_01','normalized_path':target.relative_to(ROOT).as_posix(),'editorial_image_path':image.relative_to(ROOT).as_posix(),'prompt':record['prompt'],'image_tool':'built-in image_gen','source_window':[7.7,8.833333],'reason':'Generated clock insert incorrectly showed midnight; replacement image shows 11:59 one minute before midnight. Only the existing clock close-up is replaced, with no change to chapter duration, character animation or native audio.','use_as_seedance_input':False,'verification':info,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
write_json(ROOT/'exports/clock-correction.json',edit)
frame=ROOT/'exports/editorial/clock-correction-preview.jpg'
run(['-hide_banner','-v','error','-y','-ss','8.2','-i',target,'-frames:v','1','-q:v','2',frame])
print('Clock insert corrected to 11:59; 10-second chapter and original audio retained.')
