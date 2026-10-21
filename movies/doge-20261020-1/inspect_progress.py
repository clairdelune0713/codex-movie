from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent
files=sorted((ROOT/'assets').glob('*/c01.png'))
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',23)
pages=[]
for page in range((len(files)+7)//8):
    subset=files[page*8:(page+1)*8]
    canvas=Image.new('RGB',(1600,((len(subset)+1)//2)*480),'#eceeee')
    draw=ImageDraw.Draw(canvas)
    for i,p in enumerate(subset):
        with Image.open(p) as img: im=ImageOps.contain(img.convert('RGB'),(790,435))
        x=(i%2)*800+(800-im.width)//2;y=(i//2)*480+(435-im.height)//2
        canvas.paste(im,(x,y));draw.text(((i%2)*800+15,(i//2)*480+440),p.parent.name,font=font,fill='#142d2d')
    path=ROOT/'exports'/'asset-review'/f'progress-{page+1:02d}.jpg'
    canvas.save(path,quality=93);pages.append(str(path))
print('\n'.join(pages))
