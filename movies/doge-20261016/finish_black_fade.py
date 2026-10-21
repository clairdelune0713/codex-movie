"""Complete the native epilogue fade without extending runtime or adding text."""
import copy,hashlib
from datetime import datetime,timezone
import assemble_finale as a
import render_finale as r

m=r.read(r.ROOT/'exports/finale-assembly-manifest.json')
assert m['verification']['decoded_frames']==7320 and m['duration_seconds']==305
old=r.ROOT/m['path'];output=old.with_name(old.stem+'-v02.mp4')
assert old.exists() and not output.exists()
r.save(r.ROOT/'exports/finale-assembly-manifest-v01.json',m)
concat=r.ROOT/'exports/finale-finishing-v02-no-text/concat.txt'
a.call(['-f','concat','-safe','0','-i',concat,'-vf','setpts=N/(24*TB),fade=t=out:st=304.5:d=0.45',
    '-af','aresample=48000,atrim=duration=305,asetpts=PTS-STARTPTS','-t','305','-r','24','-fps_mode','cfr',
    '-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k',
    '-ar','48000','-ac','2','-movflags','+faststart',output])
info=r.probe(output)
decoded=a.call(['-threads','2','-i',output,'-progress','pipe:1','-f','null','-'])
counts=a.re.findall(r'^frame=(\d+)',decoded.stdout,a.re.M)
assert int(counts[-1])==7320 and info['duration']==305
m['prior_export']={'path':old.relative_to(r.ROOT).as_posix(),'sha256':hashlib.sha256(old.read_bytes()).hexdigest(),
    'reason':'Native generated fade was still partially visible on final frame; preserved assembly v01.'}
m.update(path=output.relative_to(r.ROOT).as_posix(),created_at=r.now(),
    finishing='Generated animation and native audio; completed final 0.45-second fade to black. No title, subtitles, captions, text boxes or graphic overlays; no time stretching.',
    verification={**info,'decoded_frames':7320,'full_decode_verified':True})
r.save(r.ROOT/'exports/finale-assembly-manifest.json',m)
print('Completed ending fade:',output)
