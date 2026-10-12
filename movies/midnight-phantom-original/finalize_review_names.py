import importlib.util
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('movi_project',r'C:\Users\Admin 3\.codex\skills\movi2\scripts\project.py');helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
current=helper.read(ROOT/'project.json');p=helper.read(ROOT/'project.json')
for a in p['asset_list']:a['name']=a['name'].replace('Inkwell','Inkbell')
helper.save(ROOT,current,p,'Align location display names with original Inkbell City adaptation')
page=ROOT/'exports/asset-review.html';page.write_text(page.read_text(encoding='utf-8').replace('Inkwell','Inkbell'),encoding='utf-8')
assets=[a for a in p['asset_list'] if a['category']=='environment'];cw=1000;ih=round(cw*9/16);ch=ih+76
sheet=Image.new('RGB',(cw,ch*len(assets)),(248,242,221));draw=ImageDraw.Draw(sheet);font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',26);small=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',21)
for i,a in enumerate(assets):
    c=helper.selected_media(a);y=i*ch;draw.text((16,y+10),a['name']+' | '+a['tag'],font=font,fill=(28,27,26));draw.text((16,y+43),'Candidate: '+c['id'],font=small,fill=(71,66,56))
    with Image.open(ROOT/c['path']) as im:
        im=im.convert('RGB');im.thumbnail((cw-16,ih-8),Image.Resampling.LANCZOS);sheet.paste(im,((cw-im.width)//2,y+76+(ih-im.height)//2))
sheet.save(ROOT/'exports/review-environments.jpg',quality=95)
print('Revised gallery uses original city name consistently.')
