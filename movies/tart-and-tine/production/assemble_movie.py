"""Assemble only successful Seedance takes, retaining audio and exact runtime."""
import argparse
import json
import re
import subprocess
from pathlib import Path
from PIL import Image, ImageChops, ImageStat

ROOT = Path(__file__).resolve().parents[1]
FFMPEG = Path('C:/Users/admina/Downloads/project/dog-test/.tools/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe')


def run(command):
    result = subprocess.run([str(FFMPEG), '-hide_banner'] + command, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr[-3000:])
    return result


def probe(file):
    result = subprocess.run([str(FFMPEG), '-hide_banner', '-i', str(file)], capture_output=True, text=True)
    text = result.stderr
    duration = re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)', text)
    video = next((line for line in text.splitlines() if 'Video:' in line and 'Stream #' in line), '')
    resolution = re.search(r'(\d{3,5})x(\d{3,5})', video)
    fps = re.search(r'(\d+(?:\.\d+)?) fps', video)
    audio = next((line.strip() for line in text.splitlines() if 'Audio:' in line and 'Stream #' in line), None)
    if not duration or not resolution or not fps:
        raise RuntimeError('Could not inspect video metadata: ' + str(file))
    return {'duration_seconds': int(duration[1])*3600 + int(duration[2])*60 + float(duration[3]), 'resolution': [int(resolution[1]), int(resolution[2])], 'fps': float(fps[1]), 'video_stream': video.strip(), 'audio_stream': audio}


def decode(file):
    result = run(['-v', 'error', '-i', str(file), '-map', '0:v:0', '-map', '0:a:0?', '-progress', 'pipe:1', '-nostats', '-f', 'null', '-'])
    frames = re.findall(r'^frame=(\d+)\s*$', result.stdout, flags=re.M)
    if not frames:
        raise RuntimeError('Decode produced no frame count: ' + str(file))
    return {'decode_verified': True, 'frame_count': int(frames[-1])}


def extract(file, timestamp, target):
    if not target.exists():
        run(['-ss', str(timestamp), '-i', str(file), '-frames:v', '1', '-update', '1', str(target)])
    with Image.open(target) as img:
        img.load()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=('inspect','assemble'))
    args = parser.parse_args()
    journal = json.loads((ROOT / 'exports/seedance-journal.json').read_text(encoding='utf-8'))
    takes = list(journal['takes'].values())
    if len(takes) != 6 or any(t['status'] != 'succeeded' or not t.get('path') for t in takes):
        raise RuntimeError('Assembly requires six successful downloaded takes.')
    project = json.loads((ROOT / 'project.json').read_text(encoding='utf-8'))
    takes = [journal['takes'][chapter['id']] for chapter in project['chapters']]
    verification = []
    for take in takes:
        file = ROOT / take['path']
        metadata = probe(file)
        metadata.update(decode(file))
        if abs(metadata['duration_seconds'] - 10) > 0.15:
            raise RuntimeError('Material duration differs substantially from plan; review before assembly: ' + take['chapter_id'])
        if not metadata['audio_stream']:
            raise RuntimeError('Native audio is missing; review before creating silent output.')
        volume=run(['-i',str(file),'-vn','-af','volumedetect','-f','null','-'])
        maximum=re.search(r'max_volume: ([\-\d.]+) dB',volume.stderr)
        if not maximum:
            raise RuntimeError('Native audio appears silent; review before assembly.')
        metadata['audio_max_volume_db']=float(maximum[1])
        folder = ROOT / 'chapters' / take['chapter_id'] / 'screenshots'
        folder.mkdir(parents=True, exist_ok=True)
        frames = []
        for number, timestamp in enumerate((0.25, 3.25, 6.25, 9.5), 1):
            target = folder / (take['take_id'] + f'_sample{number:02d}.png')
            extract(file, timestamp, target)
            frames.append(target.relative_to(ROOT).as_posix())
        images = [Image.open(ROOT / path).convert('RGB') for path in frames]
        differences = [sum(ImageStat.Stat(ImageChops.difference(images[0], image)).mean) for image in images[1:]]
        if max(differences) < 1:
            raise RuntimeError('No significant visual motion in take: ' + take['chapter_id'])
        contact = folder / (take['take_id'] + '_contact.jpg')
        sheet = Image.new('RGB', (1280,720))
        for i, image in enumerate(images):
            image.thumbnail((640,360))
            sheet.paste(image, ((i%2)*640,(i//2)*360))
        sheet.save(contact, quality=92)
        metadata.update(chapter_id=take['chapter_id'], take_id=take['take_id'], samples=frames, contact_sheet=contact.relative_to(ROOT).as_posix(), motion_difference=differences)
        verification.append(metadata)
        print(take['chapter_id'], json.dumps({k:metadata[k] for k in ('duration_seconds','resolution','fps','frame_count')}), flush=True)
    (ROOT / 'exports/take-verification.json').write_text(json.dumps(verification, indent=2)+'\n', encoding='utf-8')
    if args.command == 'inspect':
        return
    normalized = []
    staging = ROOT / 'exports/assembly-v01'
    staging.mkdir(exist_ok=True)
    for take in takes:
        target = staging / (take['take_id'] + '_normalized.mp4')
        if not target.exists():
            run(['-i', str(ROOT / take['path']), '-map', '0:v:0', '-map', '0:a:0', '-vf', 'scale=854:480:flags=lanczos,fps=30,setsar=1', '-af', 'aresample=48000,apad,atrim=duration=10,afade=t=in:st=0:d=0.04,afade=t=out:st=9.96:d=0.04', '-t', '10', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', '-movflags', '+faststart', str(target)])
        normalized.append(target)
    # Paths resolve inside a known local staging directory; no shell interpolation.
    manifest = staging / 'concat.txt'
    manifest.write_text(''.join("file '" + item.name + "'\n" for item in normalized), encoding='utf-8')
    output = ROOT / 'exports/tart-and-tine-60s-v02.mp4'
    if output.exists():
        raise RuntimeError('Final movie already exists; use a versioned output for new assembly.')
    # The concat demuxer offsets video by AAC priming (~21 ms). Reset both
    # streams explicitly so the delivered container also lasts exactly 60 s.
    run(['-f', 'concat', '-safe', '1', '-i', str(manifest), '-map', '0:v:0', '-map', '0:a:0', '-vf', 'setpts=PTS-STARTPTS', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-af', 'atrim=duration=60,asetpts=PTS-STARTPTS', '-t', '60', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', '-movflags', '+faststart', str(output)])
    result = probe(output)
    result.update(decode(output))
    if result['frame_count'] != 1800 or result['fps'] != 30 or result['resolution'] != [854,480] or abs(result['duration_seconds']-60) > 0.05:
        raise RuntimeError('Final movie does not satisfy exact delivery profile.')
    result.update(path=output.relative_to(ROOT).as_posix(), input_take_ids=[t['take_id'] for t in takes], transitions='Hard video cuts; 40 ms per-chapter audio edge fades; native music/Foley preserved', native_take_profiles=verification)
    (ROOT / 'exports/video-verification.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('path','duration_seconds','resolution','fps','frame_count','decode_verified')}))


if __name__ == '__main__':
    main()
