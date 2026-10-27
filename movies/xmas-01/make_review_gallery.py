from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import json
import sys

root = Path(__file__).resolve().parent
project = json.loads((root / 'project.json').read_text(encoding='utf-8'))
canvas = Image.new('RGB', (1920, 1380), '#151c22')
draw = ImageDraw.Draw(canvas)
font_path = Path('C:/Windows/Fonts/arial.ttf')
font = ImageFont.truetype(str(font_path), 27)
small = ImageFont.truetype(str(font_path), 22)
big = ImageFont.truetype(str(font_path), 35)
draw.text((35, 20), 'xmas-01  |  Asset review', font=big, fill='white')
draw.text((35, 67), 'One 30-second generation  |  16:9  |  Louis : Kooloo : ccbug = 6 : 3 : 1', font=font, fill='#eec879')
boxes = [(25,130,605,650), (660,130,605,650), (1295,130,600,650), (25,815,920,455), (975,815,920,455)]
for asset, (x,y,w,h) in zip(project['asset_list'], boxes):
    candidate = next(c for c in asset['candidates'] if c['id'] == asset['selected_candidate_id'])
    draw.text((x,y-5), asset['tag'], font=font, fill='white')
    draw.text((x,y+32), candidate['id'], font=small, fill='#b8c8d5')
    with Image.open(root / candidate['path']) as source:
        contained = ImageOps.contain(source.convert('RGB'), (w, h-75), Image.Resampling.LANCZOS)
        panel = Image.new('RGB', (w, h-75), '#f8f7f5')
        panel.paste(contained, ((w-contained.width)//2, (h-75-contained.height)//2))
        canvas.paste(panel, (x,y+70))
draw.text((35,1305), 'ccbug: center RED variant only. Images above are separate references; their display sizes do not indicate movie scale.', font=small, fill='#eec879')
draw.text((35,1340), 'Review gallery only: this combined sheet is excluded from all video generation inputs.', font=small, fill='#b8c8d5')
destination = root / 'exports' / ('asset-review-gallery-' + (sys.argv[1] if len(sys.argv) > 1 else 'v01') + '.jpg')
destination.parent.mkdir(exist_ok=True)
if destination.exists():
    raise RuntimeError('Review gallery already exists: ' + str(destination))
canvas.save(destination, quality=93)
print(destination)
