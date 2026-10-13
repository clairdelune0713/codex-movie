"""Assemble inspected historical footage without claiming continuity is resolved."""
import hashlib
import json
from datetime import datetime, timezone
from project_ops import ROOT, helper, write_json, commit
from assemble_movie import run, metadata, decode, signal, PROFILE

manifest = helper.read(ROOT/'exports/continuity-v02-review-cut-inputs.json')
fixes = helper.read(ROOT/'exports/continuity-v02-editorial-fixes.json')
output = ROOT/'exports/midnight-phantom-review-cut-v02-150s-720p-21x9.mp4'
if output.exists():
    raise RuntimeError('Preserve existing review export')
project = helper.read(ROOT/'project.json')
normalized = []
inputs = []
for item in manifest['inputs']:
    chapter = next(c for c in project['chapters'] if c['id'] == item['chapter_id'])
    take = next(t for t in chapter['takes'] if t['id'] == item['take_id'])
    if take['status'] != 'succeeded' or take['path'] != item['path']:
        raise RuntimeError('Historical input mismatch')
    source = ROOT/item['path']
    fix = next((f for f in fixes if f['chapter_id'] == item['chapter_id'] and f['source_take_id'] == item['take_id']), None)
    target = ROOT/f'exports/normalized-review-v02/{item["chapter_id"]}-{item["take_id"]}.mp4'
    if fix:
        target = ROOT/fix['normalized_path']
        if not target.is_file():
            raise RuntimeError('Missing verified editorial clip')
    elif not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        duration = item['duration']
        video = f'setpts=PTS-STARTPTS,fps=30,trim=duration={duration},setpts=N/(30*TB),setsar=1'
        audio = f'atrim=duration={duration},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d=0.02,afade=t=out:st={duration-0.03}:d=0.03'
        run(['-hide_banner','-v','error','-i',source,'-map','0:v:0','-map','0:a:0','-vf',video,'-af',audio,'-t',duration,'-r','30','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',target])
    normalized.append(target)
    inputs.append({**item, 'assembly_path':target.relative_to(ROOT).as_posix(), 'editorial_change':fix['change'] if fix else None})
    print(json.dumps({'normalized':item['chapter_id']}), flush=True)

listing = ROOT/'exports/concat-inputs-review-v02.txt'
listing.write_text(''.join("file '"+p.as_posix().replace("'","'\\''")+"'\n" for p in normalized), encoding='utf-8')
run(['-hide_banner','-v','error','-f','concat','-safe','0','-i',listing,'-map','0:v:0','-map','0:a:0','-vf','setpts=N/(30*TB),setsar=1','-af','atrim=duration=150,asetpts=PTS-STARTPTS,loudnorm=I=-18:TP=-2:LRA=11,aresample=48000','-t','150','-r','30','-fps_mode','cfr','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',output])
verification = {**metadata(output), **decode(output), **signal(output), 'target':PROFILE, 'sha256':hashlib.sha256(output.read_bytes()).hexdigest(), 'verified_at':datetime.now(timezone.utc).isoformat()}
if verification['container_duration'] != 150 or verification['decoded_frames'] != 4500 or verification['fps'] != 30 or (verification['width'],verification['height']) != (1470,630) or not verification['audio_present']:
    raise RuntimeError('Review export verification failed')
write_json(ROOT/'exports/review-cut-v02-verification.json', verification)
write_json(ROOT/'exports/review-cut-v02-assembly.json', {'status':'review_candidate_not_final','inputs':inputs,'output':output.relative_to(ROOT).as_posix(),'limitations':manifest['limitations'],'method':'Normal speed hard cuts, native 21:9 720p, original generated dialogue and sound, stereo loudness normalization. Historical inspected footage; newer scale-reference changes are not represented.'})
notes = '''# Continuity v02 review cut

This is a 150-second review candidate, not a claim that every requested revision is complete. The previous export and all source takes remain available.

The selected footage improves the collar, numberless fixed clocks, feather removal, paired attached bin lids, held pistol, Pip's bin exit, separate NPC truck driver, nearby ramp, downward rope catch, stationary cable clue, forward-facing guard feet, pendulum kick, and Crow's complete body in the ending. The clock insert replaces an invalid empty-machine shot; the banter shot uses a local eye-darkening correction and retains the single recovered diamond.

Material gaps remain:

- Throughout shared shots: Crow does not consistently meet the exact 4x ratio; Riff, Pip and Guard are not consistently equal in height.
- 01:09-01:36: tower blocking and actor positions still drift between clips, particularly Pip's side of Riff at the warning-to-trap transition.
- 02:02-02:21: the guard ends near the left window and changes position in the following banter shot. Machine placement is improved but does not remain pixel-exact across all tower cuts.
- 02:21-02:30: Crow retains a full body, but character scale shifts as the brothers approach the camera.

The same Crow voice guide was supplied to speaking generations. Exact voice matching and every spoken line have not been independently verified by listening.

Delivery checks: 150.00 seconds, 4,500 frames, 30 fps, 1470x630 (native provider 720p at 21:9), stereo AAC 48 kHz, full decode passed. No moving action was slowed. Generation has stopped in response to the request to wrap up.
'''
(ROOT/'exports/review-cut-v02-known-gaps.md').write_text(notes, encoding='utf-8')
project = helper.read(ROOT/'project.json')
project['continuity_revision']['status'] = 'review_cut_ready_with_known_gaps'
project['continuity_review_output'] = {'path':output.relative_to(ROOT).as_posix(),'status':'review_candidate_not_final','verification':verification,'known_gaps':'exports/review-cut-v02-known-gaps.md','limitations':manifest['limitations']}
commit(project, 'Record exact150second review cut with unresolved continuity gaps; preserve original final output')
print(json.dumps({'review_cut':str(output),'verification':verification}), flush=True)
