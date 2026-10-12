import json
import math
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
p = json.loads((ROOT / 'project.json').read_text(encoding='utf-8'))
out = ROOT / 'exports' / 'asset-review'
out.mkdir(parents=True, exist_ok=True)
font_path = Path('C:/Windows/Fonts/msjh.ttc')
font = ImageFont.truetype(str(font_path), 26)
small = ImageFont.truetype(str(font_path), 22)
groups = [('dogs','狗角色','character',lambda a:a['id'].startswith(('tart_','tine_')),2,840,472),
          ('humans','人類角色','character',lambda a:not a['id'].startswith(('tart_','tine_')),3,640,360),
          ('environments','場景','environment',lambda a:True,2,840,360),
          ('props','主要物件','prop',lambda a:True,3,640,360),
          ('references','使用者原始參考','reference',lambda a:True,2,840,472)]
md = ['# doge-20261009 資產審閱\n',
      '全新項目；預計片長 6:30；720p、21:9；粵語對白與原創音樂；幽默與溫暖並重。沒有片名卡、字幕、署名或片尾名單。\n',
      '此頁是資產審閱，並非已渲染影片。聯絡表只供查看，不作影片生成參考；影片使用個別批准的原始圖片。\n']
for name,title,cat,pred,cols,cw,ch in groups:
    aa = [a for a in p['asset_list'] if a['category']==cat and pred(a)]
    rows = math.ceil(len(aa)/cols)
    margin, band = 18, 76
    canvas = Image.new('RGB',(cols*cw+(cols+1)*margin,rows*(ch+band)+(rows+1)*margin),'#142631')
    draw = ImageDraw.Draw(canvas)
    md.append('## '+title+'\n')
    path = out / (name+'.jpg')
    md.append(f'![{title}]({path.as_posix()})\n')
    for i,a in enumerate(aa):
        cid = a['selected_candidate_id']
        if not cid:
            raise ValueError('Missing selected image: '+a['tag'])
        c = next(c for c in a['candidates'] if c['id']==cid)
        imgpath = ROOT / c['path']
        with Image.open(imgpath) as im:
            thumb = ImageOps.contain(im.convert('RGB'),(cw,ch),Image.Resampling.LANCZOS)
        x,y = margin+(i%cols)*(cw+margin),margin+(i//cols)*(ch+band+margin)
        canvas.paste(thumb,(x+(cw-thumb.width)//2,y+(ch-thumb.height)//2))
        draw.text((x+8,y+ch+5),a['name']+'  '+a['tag'],font=font,fill='#ffffff')
        draw.text((x+8,y+ch+42),'Candidate: '+cid,font=small,fill='#bfdbdf')
        md.append(f"- **{a['name']}** `{a['tag']}` · `{cid}` · [完整原圖]({imgpath.as_posix()})\n")
    canvas.save(path,quality=94,subsampling=0)
    md.append('\n')
md.append('請批准此套資產，或指出需修改的標籤。影片生成提示詞與渲染會於批准後繼續。\n')
(ROOT / 'asset-review.md').write_text('\n'.join(md),encoding='utf-8')
print(json.dumps({'galleries':5,'selected_assets':len(p['asset_list']),'review':str(ROOT/'asset-review.md')},ensure_ascii=False))
