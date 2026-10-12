import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
HELPER = Path(r'C:\Users\admina\.codex\skills\movi2\scripts\project.py')

def run(*args):
    result = subprocess.run([sys.executable, str(HELPER), *map(str,args)], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    return result.stdout

def gallery(items, filename, title, columns=2, cell_width=800, cell_height=500):
    rows=(len(items)+columns-1)//columns
    image=Image.new('RGB',(columns*cell_width,rows*cell_height+65),'#f8f4ec')
    draw=ImageDraw.Draw(image)
    font=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',23)
    small=ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf',18)
    draw.text((22,20),title,fill='#503d32',font=font)
    for index,item in enumerate(items):
        x=(index%columns)*cell_width
        y=(index//columns)*cell_height+65
        draw.text((x+18,y+5),f"{item['name']}  {item['tag']}  [{item['candidate_id']}]",fill='#503d32',font=small)
        with Image.open(ROOT/item['path']) as original:
            view=original.convert('RGB')
            view.thumbnail((cell_width-20,cell_height-50),Image.Resampling.LANCZOS)
            image.paste(view,(x+(cell_width-view.width)//2,y+45))
    image.save(ROOT/'exports'/filename)

def main():
    project=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
    records=json.loads((ROOT/'generated-asset-records.json').read_text(encoding='utf-8'))
    now=datetime.now(timezone.utc).isoformat()
    for record in records:
        asset=next(a for a in project['asset_list'] if a['id']=='asset_'+record['id'])
        relative=Path('assets')/asset['id']/(record['candidate_id']+'.png')
        target=ROOT/relative
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():
            raise FileExistsError(target)
        shutil.copy2(record['source_file'],target)
        with Image.open(target) as image:
            image.load()
            size=image.size
        candidate={'id':record['candidate_id'],'path':relative.as_posix(),'prompt':asset['generation_prompt'],'source_revision':record['source_revision'],'created_at':now,'tool':record['tool'],'width':size[0],'height':size[1],'actual_aspect_ratio':size[0]/size[1],'inspection':record['inspection']}
        if 'dependency_fingerprint' in record:
            candidate['dependency_fingerprint']=record['dependency_fingerprint']
        else:
            candidate['fingerprint_note']='No helper fingerprint was captured before generation; freshness remains unknown. Exact submitted prompt and source references retained.'
        asset['candidates'].append(candidate)
        asset['selected_candidate_id']=candidate['id']
        (target.parent/'candidate-c01-metadata.json').write_text(json.dumps(candidate,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    project['production_status']='awaiting_visual_asset_approval'
    proposal=ROOT/'proposal-selected-assets.json'
    proposal.write_text(json.dumps(project,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(run('commit',ROOT,'--from',proposal,'--reason','Select eight generated plush assets and retain two original photo references'))
    manifest=json.loads(run('review-assets',ROOT))
    export_dir=ROOT/'exports'
    export_dir.mkdir(exist_ok=True)
    (export_dir/'asset-review-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    current=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
    items=[]
    for asset in current['asset_list']:
        candidate=next(c for c in asset['candidates'] if c['id']==asset['selected_candidate_id'])
        items.append({'name':asset['name'],'tag':asset['tag'],'category':asset['category'],'candidate_id':candidate['id'],'path':candidate['path']})
    gallery([i for i in items if i['category']=='character'],'review-characters.jpg','Characters - technical body / back / face reference views')
    gallery([i for i in items if i['category']=='environment'],'review-environments.jpg','Environments - empty setting reference plates')
    gallery([i for i in items if i['category']=='prop'],'review-star.jpg','Main prop - the friendly Golden Star',columns=1)
    gallery([i for i in items if i['category']=='reference'],'review-supplied-photos.jpg','Supplied photographs - identity references',cell_height=850)
    check=json.loads(run('check',ROOT))
    (export_dir/'project-check.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'duration':check['duration'],'errors':check['errors'],'warnings':check['warnings'],'asset_review':check['asset_review'],'images':[{'tag':i['tag'],'candidate_id':i['candidate_id'],'path':i['path']} for i in items]},indent=2))
    print(run('export',ROOT))

if __name__=='__main__':
    main()
