"""Assemble inspected native takes, preserve audio, and verify an exact 10:00 delivery."""
import json
import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from render_movie import ROOT, FF, SKILL, helper, read, save, probe

def run(args):
    result=subprocess.run([str(FF),'-hide_banner','-nostdin','-y',*args],capture_output=True,text=True,encoding='utf-8',errors='replace')
    if result.returncode:raise RuntimeError('FFmpeg failed: '+result.stderr[-1800:])
    return result

def encode_final(args):
    with tempfile.TemporaryFile(mode='w+', encoding='utf-8') as errors:
        process = subprocess.Popen([str(FF), '-hide_banner', '-nostdin', '-y',
            '-progress', 'pipe:1', '-stats_period', '20', '-nostats', *args],
            stdout=subprocess.PIPE, stderr=errors, text=True, encoding='utf-8')
        for line in process.stdout:
            if line.startswith('frame='):
                count = int(line.split('=', 1)[1])
                print('Final encode:', count, '/ 14400 frames;',
                      str(round(count / 14400 * 100, 1)) + '%', flush=True)
        process.stdout.close()
        code = process.wait()
        if code:
            errors.seek(0)
            raise RuntimeError('Final encoding failed: ' + errors.read()[-1800:])

def normalize(c,t):
    cache=ROOT/'exports/assembly';cache.mkdir(parents=True,exist_ok=True)
    # A full encoded-frame audit found the conventional detail crop was one
    # frame short. Pad only an audited short normalization, never all scenes.
    audit_path=ROOT/'exports/normalized-frame-audit.json'
    ordinary='exports/assembly/'+c['id']+'_'+t['id']+'_normalized.mp4'
    exact_tail=bool(audit_path.exists() and any(
        x['path']==ordinary and x['actual']<x['expected']
        for x in read(audit_path).get('mismatches',[])))
    suffix = '_normalized_exact.mp4' if exact_tail else '_normalized.mp4'
    dest=cache/(c['id']+'_'+t['id']+suffix)
    if dest.exists():return dest
    duration=c['duration']
    vf='scale=1920:1080:flags=lanczos,setsar=1,'
    if exact_tail:vf+=f'tpad=stop_mode=clone:stop_duration=0.2,trim=duration={duration},'
    vf+='fps=24,setpts=N/(24*TB),format=yuv420p'
    if c['chapter_index']==70:vf+=f',fade=t=out:st={duration-0.5}:d=0.5'
    af=('apad=pad_dur=0.2,' if exact_tail else '')+f'atrim=duration={duration},asetpts=PTS-STARTPTS,aresample=48000,afade=t=in:st=0:d=0.025,afade=t=out:st={duration-0.025}:d=0.025'
    temp=dest.with_name(dest.stem+'.encoding.mp4')
    inputs=['-v','error','-threads','4','-i',str(ROOT/t['path'])]
    if not t['verification'].get('audio'):
        bed=c.get('post_audio')
        if not bed or hashlib.sha256((ROOT/bed['path']).read_bytes()).hexdigest()!=bed['sha256']:
            raise RuntimeError('Verified local ambience required for silent wordless take: '+c['id'])
        inputs+=['-i',str(ROOT/bed['path']),'-map','0:v:0','-map','1:a:0']
    run([*inputs,'-vf',vf,'-af',af,
        '-c:v','libx264','-preset','fast','-crf','18','-threads','4','-r','24','-fps_mode','cfr',
        '-frames:v',str(duration*24),'-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-t',str(duration),str(temp)])
    temp.replace(dest)
    print(c['id'],'normalized',flush=True)
    return dest

def normalize_ready():
    p=read(ROOT/'project.json');j=read(ROOT/'exports/task-journal.json');reviews=read(ROOT/'exports/visual-reviews.json')
    for c in p['chapters']:
        selected=next((t for t in c['takes'] if t['id']==c.get('active_take_id')),None)
        if (selected and selected['status']=='succeeded' and selected.get('visual_review',{}).get('inspected') and
            not selected['visual_review'].get('requires_repair') and selected['dependency_fingerprint']==helper.chapter_fingerprint(ROOT,p,c)):
            normalize(c,selected)
            continue
        t=j['takes'].get(c['id']);review=reviews.get(c['id'])
        if t and t['status']=='succeeded' and review and review.get('inspected') and not review.get('requires_repair') and review['take_id']==t['id']:
            normalize(c,t)

def audio_mastering(concat):
    analysis=run(['-f','concat','-safe','0','-i',str(concat),'-vn',
        '-af','loudnorm=I=-18:TP=-1.5:LRA=11:print_format=json','-f','null','-'])
    found=re.findall(r'\{\s*"input_i".*?\}',analysis.stderr,re.S)
    if not found:raise RuntimeError('Audio loudness analysis unavailable')
    measured=json.loads(found[-1])
    save(ROOT/'exports/audio-mastering-analysis.json',{'target_integrated_lufs':-18,'target_true_peak_db':-1.5,'target_loudness_range_lu':11,'measured_native_assembly':measured})
    return ('loudnorm=I=-18:TP=-1.5:LRA=11:measured_I='+measured['input_i']+
        ':measured_TP='+measured['input_tp']+':measured_LRA='+measured['input_lra']+
        ':measured_thresh='+measured['input_thresh']+':offset='+measured['target_offset']+
        ':linear=true,aresample=48000,atrim=duration=600,asetpts=PTS-STARTPTS')

def main():
    p=read(ROOT/'project.json')
    takes=[]
    for c in p['chapters']:
        t=next((t for t in c['takes'] if t['id']==c.get('active_take_id')),None)
        if not t or t['status']!='succeeded' or not t.get('visual_review',{}).get('inspected') or t.get('visual_review',{}).get('requires_repair'):
            raise RuntimeError('Inspected successful take required: '+c['id'])
        if t['dependency_fingerprint']!=helper.chapter_fingerprint(ROOT,p,c):
            raise RuntimeError('Selected take is outdated: '+c['id'])
        if not t['verification'].get('native_1080p'):raise RuntimeError('Native 1080p required')
        takes.append((c,t))
    cache=ROOT/'exports/assembly';cache.mkdir(parents=True,exist_ok=True)
    normalized=[]
    for c,t in takes:
        normalized.append(normalize(c,t))
    concat=cache/'concat.txt'
    concat.write_text('\n'.join("file '"+f.as_posix().replace("'","'\\''")+"'" for f in normalized)+'\n',encoding='utf-8')
    mastered_audio=audio_mastering(concat)
    final=ROOT/'exports/dog-20261015-1080p.mp4'
    copy_normalized = '--copy-normalized' in sys.argv
    partial=ROOT/('exports/dog-20261015-1080p.assembling-exact.mp4' if copy_normalized else 'exports/dog-20261015-1080p.assembling.mp4')
    if final.exists():raise RuntimeError('Preserve the existing final delivery; choose a new version for a revision')
    if copy_normalized:
        # All normalized clips share native H.264 profile/dimensions and exact
        # 24fps timestamps. Preserve those encoded frames without another pass.
        run(['-v','error','-f','concat','-safe','0','-i',str(concat),
            '-map','0:v:0','-map','0:a:0','-c:v','copy',
            '-af',mastered_audio,
            '-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-t','600',
            '-avoid_negative_ts','disabled','-map_metadata','-1','-movflags','+faststart',str(partial)])
        print('Exact normalized frames assembled; verifying full file',flush=True)
    else:
        encode_final(['-v','error','-f','concat','-safe','0','-i',str(concat),
            '-vf','setpts=N/(24*TB),setsar=1','-af',mastered_audio,
            '-c:v','libx264','-preset','fast','-crf','18','-threads','4','-r','24','-fps_mode','cfr','-frames:v','14400',
            '-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-t','600','-map_metadata','-1','-movflags','+faststart',str(partial)])
    info=probe(partial)
    decoded=run(['-v','error','-threads','4','-i',str(partial),'-progress','pipe:1','-nostats','-f','null','-'])
    if decoded.stderr.strip():raise RuntimeError('Final video decode errors: '+decoded.stderr[-1500:])
    frames=[int(x) for x in re.findall(r'^frame=(\d+)$',decoded.stdout,re.M)]
    if not frames or frames[-1]!=14400:raise RuntimeError('Final frame count mismatch')
    if abs(info['duration']-600)>0.02 or (info['width'],info['height'])!=(1920,1080) or info['fps']!=24:
        raise RuntimeError('Final output profile mismatch: '+json.dumps(info))
    audio=run(['-i',str(partial),'-vn','-af','volumedetect','-f','null','-'])
    levels={name:float(value) for name,value in re.findall(r'(mean_volume|max_volume): ([\-\d.]+) dB',audio.stderr)}
    if levels.get('mean_volume',-100)<-60:raise RuntimeError('Final audio appears silent')
    partial.replace(final)
    save(ROOT/'exports/verification.json',{**info,'frame_count':14400,'runtime_exact_seconds':600,
        'decode_verified':True,'audio_levels_db':levels,'native_takes_verified':70,
        'limitations':['Visual review uses four actual sampled frames per take; technical audio checks do not prove word-perfect generated speech or voice consistency.'],
        'file':final.relative_to(ROOT).as_posix()})
    save(ROOT/'exports/assembly-settings.json',{'input_takes':[{'chapter':c['id'],'take':t['id'],'path':t['path'],'duration':c['duration']} for c,t in takes],
        'video':'1920x1080, H.264 yuv420p, 24fps CFR, CRF18','audio':'Native generated tracks plus verified local original-performance/ambience edits as recorded per chapter, whole-movie measured loudness pass targeting -18 LUFS / -1.5 dBTP, stereo AAC 192kb/s 48kHz, 25ms edge fades',
        'edit':'Hard cuts, no titles/subtitles/credits, final 0.5s fade to black','duration_seconds':600})
    current=read(ROOT/'project.json');proposal=json.loads(json.dumps(current))
    proposal.update(production_stage='delivered',render_status='completed',delivery={'path':final.relative_to(ROOT).as_posix(),'verification_path':'exports/verification.json','duration_seconds':600,'resolution':'1920x1080','aspect_ratio':'16:9'})
    print(helper.save(ROOT,current,proposal,'Register technically verified exact 10-minute 1080p full movie'))
    ledger=read(ROOT/'usage.json');session=next(s['id'] for s in ledger['sessions'] if not s.get('ended_at'))
    subprocess.run([sys.executable,'-X','utf8',str(SKILL/'usage.py'),'finish',str(ROOT),'--session',session,'--outcome','delivered'],check=True)
    report=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'usage.py'),'report',str(ROOT),'--session',session],capture_output=True,text=True,encoding='utf-8',check=True)
    save(ROOT/'exports'/f'usage-report-{session}.json',json.loads(report.stdout))
    print(report.stdout);print('Final movie:',final,flush=True)

if __name__=='__main__':
    if '--normalize-ready' in sys.argv:normalize_ready()
    else:main()
