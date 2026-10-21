from pathlib import Path
import hashlib, json, re, shutil
from PIL import Image, ImageOps, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent.parent
SOURCE = WORKSPACE / 'doge-material'
(ROOT / 'source' / 'image-ref').mkdir(parents=True, exist_ok=True)
(ROOT / 'exports' / 'asset-review').mkdir(parents=True, exist_ok=True)
manifest = []
for src in [SOURCE / 'doge-script.md', *sorted((SOURCE / 'image-ref').glob('*.png'))]:
    rel = src.relative_to(SOURCE)
    dst = ROOT / 'source' / rel
    if not dst.exists():
        shutil.copy2(src, dst)
    source_hash = hashlib.sha256(src.read_bytes()).hexdigest()
    assert source_hash == hashlib.sha256(dst.read_bytes()).hexdigest()
    manifest.append({'path': str(rel).replace('\\', '/'), 'sha256': source_hash, 'bytes': src.stat().st_size})
(ROOT / 'source' / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
raw = (SOURCE / 'doge-script.md').read_text(encoding='utf-8-sig')
normalized = re.sub(r'\\([#*_.!>=\-])', r'\1', raw)
(ROOT / 'source' / 'screenplay-readable.md').write_text(normalized, encoding='utf-8')
files = sorted((ROOT / 'source' / 'image-ref').glob('*.png'))
canvas = Image.new('RGB', (1600, 5*390), '#e8eceb')
draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 24)
for i,p in enumerate(files):
    im = Image.open(p).convert('RGB')
    im.thumbnail((780,340))
    x=(i%2)*800+(800-im.width)//2
    y=(i//2)*390
    canvas.paste(im,(x,y))
    draw.text(((i%2)*800+15,y+350),p.stem,font=font,fill='#172e2e')
canvas.save(ROOT/'exports'/'asset-review'/'supplied-references.jpg', quality=94)
print(json.dumps({'source_files':len(manifest),'contact_sheet':str(ROOT/'exports'/'asset-review'/'supplied-references.jpg')}, indent=2))
