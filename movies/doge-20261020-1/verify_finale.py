"""Final-export checks and actual-frame sheets for the stitched movie."""
import hashlib,json,re,subprocess,sys
from PIL import Image,ImageDraw,ImageFont,ImageStat
from render_finale import ROOT,FF,read,save,probe,scope_chapters
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as helper
def main():
    p=read(ROOT/'project.json');m=read(ROOT/'exports/finale-assembly-manifest.json');video=ROOT/m['path'];folder=ROOT/'exports/final-inspection'/video.stem;folder.mkdir(parents=True,exist_ok=True)
    assert len(scope_chapters(p))==15 and sum(c['duration'] for c in scope_chapters(p))==305
    selections=[]
    for c in scope_chapters(p):
        t=next(t for t in c['takes'] if t['id']==c['active_take_id'])
        assert t['dependency_fingerprint']==helper.chapter_fingerprint(ROOT,p,c),c['id']
        assert t['visual_review']['inspected'] and not t['visual_review']['requires_repair'],c['id']
        selections.append({'scene':c['source_scene_number'],'take_id':t['id'],'current':True,'source_sha256':hashlib.sha256((ROOT/t['path']).read_bytes()).hexdigest()})
    targets=[(c['start']+c['duration']/2,'Scene '+str(c['source_scene_number'])+' midpoint') for c in m['chapters']]
    targets += [(2,'Harbour caption'),(98,'Balloon reframe, no generated subtitle'),(225.8,'Night-show start'),(227,'Night dialogue'),(249.5,'Night-matched dogs'),(266.75,'Night-matched paw promise'),(274,'Next Friday caption'),(291,'Moving aerial'),(294.5,'Animated route'),(297,'Title'),(304.9,'Postcard stinger'),(304.94,'Final black frame')]
    frames=[]
    for i,(sec,label) in enumerate(targets):
        f=folder/f'frame-{i:02}-{sec:07.3f}.jpg'
        if not f.exists():
            r=subprocess.run([str(FF),'-hide_banner','-loglevel','error','-nostdin','-ss',str(sec),'-i',str(video),'-frames:v','1','-q:v','2',str(f)],capture_output=True)
            if r.returncode:raise RuntimeError('Export-frame extraction failed')
        frames.append({'time':sec,'label':label,'path':f.relative_to(ROOT).as_posix()})
    font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17);sheets=[]
    for page in range((len(frames)+11)//12):
        group=frames[page*12:(page+1)*12];im=Image.new('RGB',(1488,((len(group)+2)//3)*244),'#142025');d=ImageDraw.Draw(im)
        for i,f in enumerate(group):
            pic=Image.open(ROOT/f['path']);pic.thumbnail((496,216));x=i%3*496;y=i//3*244;im.paste(pic,(x,y));d.text((x+7,y+219),f"{f['time']:.2f}s  {f['label']}",font=font,fill='white')
        out=folder/f'contact-{page+1:02}.jpg';im.save(out,quality=94);sheets.append(out.relative_to(ROOT).as_posix());print(out,flush=True)
    audio=subprocess.run([str(FF),'-hide_banner','-nostdin','-i',str(video),'-vn','-af','volumedetect,silencedetect=noise=-45dB:d=2','-f','null','-'],capture_output=True,text=True,encoding='utf-8',errors='replace')
    if audio.returncode:raise RuntimeError('Audio decode failed')
    mean=re.search(r'mean_volume: ([-.\d]+) dB',audio.stderr);peak=re.search(r'max_volume: ([-.\d]+) dB',audio.stderr)
    container=subprocess.run([str(FF),'-hide_banner','-i',str(video)],capture_output=True,text=True,encoding='utf-8',errors='replace').stderr
    assert 'SAR 63:62 DAR 7:3' in container,'Display-aspect metadata mismatch'
    last=Image.open(ROOT/frames[-1]['path']).convert('RGB');black=max(v[1] for v in last.getextrema())<=2
    assert black,'Final frame is not black'
    info=probe(video)
    save(ROOT/'exports/final-verification.json',{'path':m['path'],'sha256':hashlib.sha256(video.read_bytes()).hexdigest(),'bytes':video.stat().st_size,'technical':info,'display_aspect_ratio':'21:9','sample_aspect_ratio':'63:62','decoded_frames':m['verification']['decoded_frames'],'full_decode_verified':m['verification']['full_decode_verified'],'source_scope':[37,51],'selected_scenes':selections,'audio':{'mean_volume_db':float(mean[1]) if mean else None,'peak_volume_db':float(peak[1]) if peak else None,'silence_periods':re.findall(r'silence_(?:start|end|duration): [\d.]+',audio.stderr),'dialogue_independently_transcribed':False},'last_frame_black':black,'frames':frames,'contact_sheets':sheets,'export_visual_inspection':'awaiting_inspection'})
    print(json.dumps({'sha256':hashlib.sha256(video.read_bytes()).hexdigest(),'duration':info['duration'],'mean_db':mean[1] if mean else None,'peak_db':peak[1] if peak else None,'final_black':black},indent=2))
if __name__=='__main__':main()
