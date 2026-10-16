"""Reuse the verified project-local transport, with this movie's explicit settings."""
import shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parent
OLD=ROOT.parent/'dog-20261013'
if (ROOT/'render_movie.py').exists():
    raise SystemExit('Adapter already exists; preserve current movie-specific fixes instead of overwriting it.')
for name in ['seedance_transport.py','render_movie.py','review_takes.py']:
    text=(OLD/name).read_text(encoding='utf-8-sig')
    if name=='render_movie.py':
        text=text.replace('1080p','480p').replace('1920,1080','854,480').replace('1920x1080','854x480').replace('native_1080p','native_480p')
        text=text.replace("Decimal('11.7')","Decimal('10.70')").replace('USD 11.7/M','USD 10.70/M').replace('checked 2026-10-13','checked 2026-10-15')
        text=text.replace("sys.path.insert(0,str(ROOT/'tools/python-deps'))\nimport imageio_ffmpeg\nFF=Path(imageio_ffmpeg.get_ffmpeg_exe())","FF=ROOT/'tools/ffmpeg.exe'")
        text=text.replace('2026101300','2026101400').replace("len(j['takes'])==55","len(j['takes'])==len(proposal['chapters'])")
        start=text.index("        if old.get('error',{}).get('code')=='InputImageSensitiveContentDetected.PrivacyInformation':")
        end=text.index("            raise RuntimeError('Replacement has no changed prompt or dependencies; no identical retry')",start)
        text=text[:start]+"        if current_fp==old['dependency_fingerprint']:\n"+text[end:]
        text=text.replace("    record={'attempt_id':t['attempt_id']", "    if t['status']=='failed' and t.get('submission_state')=='rejected':\n        cost={'kind':'estimated','currency':'USD','amount':'0','basis':'Provider documents successful video generations only; explicit rejected request has no output charge. https://docs.byteplus.com/en/docs/ModelArk/model-pricing checked 2026-10-15.'}\n    record={'attempt_id':t['attempt_id']")
    if name=='review_takes.py':text=text.replace('dog-20261013','dog-20261014').replace('1080p','480p')
    (ROOT/name).write_text(text,encoding='utf-8')
(ROOT/'tools').mkdir(exist_ok=True)
shutil.copy2(OLD/'tools/python-deps/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe',ROOT/'tools/ffmpeg.exe')
(ROOT/'STATUS.md').write_text('''# dog-20261014

Canonical revision 9: 71 selected designs approved under review_9e59bc0c6dc540739b23b5fffdb5d763 using the actual user confirmation “proceed. res: 480p. aspect ratio: 16:9”. The selected-image fingerprint matches the images already displayed to the user. The unselected outdated populated gangway composite is archived in retired_assets; scene 12 uses approved ferry plates and the corrected blue-sailor cast instead. All original scene actions remain.

All 70 cinematic prompts and exact shot spans are directed, preserving 107 original Cantonese dialogue entries and all 16 scenes. Duration is exactly 1,200 seconds. No title, subtitle, author credit or end credit. Render profile is native 480p, 16:9 with audio. Image generation is built-in image_gen only; no OpenAI image API calls were made.

Production session session_4c7e7838a5184bab82868c8ba6b1cbd8 remains open. Seedance attempts, when submitted, are journaled before POST in exports/task-journal.json and usage.json. New submissions require render-ready for the actual chapter. Successful takes require media inspection before selection. The final full movie is not yet delivered.

Direction: exports/director-script.md. Exact dialogue manifest: exports/dialogue-manifest.json. Original source and all prior candidates remain preserved.
''',encoding='utf-8')
print('Local adapter prepared for 480p; no provider calls made.')
