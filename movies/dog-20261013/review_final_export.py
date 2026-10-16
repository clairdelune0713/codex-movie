"""Sample the verified final encode for delivery QA; never a generation input."""
import subprocess
from PIL import Image, ImageDraw, ImageFont
from render_movie import ROOT, FF, read, save

verification = read(ROOT / 'exports/verification.json')
assert verification['decode_verified'] and verification['frame_count'] == 24480
movie = ROOT / verification['file']
folder = ROOT / 'exports/final-review'
folder.mkdir(exist_ok=True)
times = [0.2, 110, 200, 365, 555, 646, 750, 935, 990, 1019.8]
canvas = Image.new('RGB', (2000, 520), '#f3f0e9')
draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype('C:/Windows/Fonts/msyh.ttc', 16)
samples = []
for i, timestamp in enumerate(times):
    target = folder / ('frame-' + str(timestamp).replace('.', '-') + '.jpg')
    if not target.exists():
        subprocess.run([str(FF), '-v', 'error', '-ss', str(timestamp), '-i', str(movie),
                        '-frames:v', '1', '-q:v', '2', str(target)], check=True)
    photo = Image.open(target).convert('RGB').resize((384, 216))
    x, y = (i % 5) * 400 + 8, (i // 5) * 260 + 8
    canvas.paste(photo, (x, y))
    draw.text((x, y + 222), str(timestamp) + ' seconds', font=font, fill='#213b39')
    samples.append({'timestamp_seconds': timestamp, 'path': target.relative_to(ROOT).as_posix()})
gallery = folder / 'final-contact-sheet.jpg'
canvas.save(gallery, quality=94)
save(folder / 'inspection.json', {'file': verification['file'], 'samples': samples,
                                  'gallery_path': gallery.relative_to(ROOT).as_posix(),
                                  'inspected': False})
print(gallery)
