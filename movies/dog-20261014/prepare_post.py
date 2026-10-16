"""Prepare local media review and exact-runtime assembly, no generation."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent
OLD=ROOT.parent/'dog-20261013'
if (ROOT/'check_dialogue.py').exists():
    raise SystemExit('Post-production scripts already exist; preserve local runtime fixes.')
s=(OLD/'check_dialogue.py').read_text(encoding='utf-8')
s=s.replace("sys.path.insert(0,str(ROOT/'tools/asr-deps'))","AUDIT_TOOLS=ROOT.parent/'dog-20261013/tools'\nsys.path.insert(0,str(AUDIT_TOOLS/'asr-deps'))")
s=s.replace("str(ROOT/'tools/asr-models')","str(AUDIT_TOOLS/'asr-models')")
s=s.replace("os.environ['HF_HUB_DISABLE_TELEMETRY']='1'","os.environ['HF_HUB_DISABLE_TELEMETRY']='1'\nos.environ['HF_HUB_OFFLINE']='1'")
s=s.replace("FF=next((ROOT/'tools/python-deps/imageio_ffmpeg/binaries').glob('ffmpeg*.exe'))","FF=ROOT/'tools/ffmpeg.exe'")
s=s.replace('Loading local large-v3 Cantonese speech audit model; first use downloads public weights.','Loading existing local large-v3 Cantonese audit weights; no audio upload.')
s=s.replace("lang='en' if c['id']=='chapter_002' else 'yue'","lang='yue'")
s=s.replace("expected=re.findall(r'\\{([^{}]+)\\}',t['prompt'])","expected=[b['text'] for b in c['planning_source_blocks'] if b['type']=='dialogue']")
(ROOT/'check_dialogue.py').write_text(s,encoding='utf-8')
s=(OLD/'assemble_movie.py').read_text(encoding='utf-8')
s=s.replace('dog-20261013','dog-20261014').replace('1080p','480p').replace('1920:1080','854:480').replace('1920,1080','854,480').replace('1920x1080','854x480')
s=s.replace('17:00','20:00').replace('17-minute','20-minute').replace('1020','1200').replace('24480','28800').replace('native_takes_verified\':55','native_takes_verified\':70')
s=s.replace("exact_tail = c['chapter_index'] in (47, 48, 51, 54)","exact_tail = False")
s=s.replace("c['chapter_index']==55","c['chapter_index']==70")
s=s.replace("'native_1080p'","'native_480p'")
(ROOT/'assemble_movie.py').write_text(s,encoding='utf-8')
print('Local Cantonese audit and exact 20-minute 480p assembly prepared.')
