"""Fetch verified standalone processing tools into this movie project only."""
import hashlib
import json
import shutil
import urllib.request
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parent
TARGET=ROOT/'.media-tools'
URL='https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-9.0.2-essentials_build.zip'
EXPECTED='60f467265b1e312373dbcd92200c2618a74850f98d3d078e94296bb3fa2047ba'

def main():
    TARGET.mkdir(exist_ok=True)
    if (TARGET/'ffmpeg.exe').is_file() and (TARGET/'ffprobe.exe').is_file():
        print('Media tools already installed locally.')
        return
    archive=TARGET/'ffmpeg-9.0.2-essentials_build.zip'
    if not archive.exists():
        partial=archive.with_suffix('.zip.partial')
        with urllib.request.urlopen(URL,timeout=180) as response, partial.open('wb') as file:
            shutil.copyfileobj(response,file,length=1024*1024)
        partial.replace(archive)
    digest=hashlib.file_digest(archive.open('rb'),'sha256').hexdigest()
    if digest!=EXPECTED:
        raise RuntimeError('FFmpeg archive checksum mismatch; refusing extraction.')
    with zipfile.ZipFile(archive) as package:
        for name in ('ffmpeg.exe','ffprobe.exe','LICENSE'):
            matches=[x for x in package.namelist() if x.endswith('/'+name)]
            if not matches and name=='LICENSE':
                continue
            if len(matches)!=1:
                raise RuntimeError('Unexpected package contents for '+name)
            with package.open(matches[0]) as source, (TARGET/name).open('wb') as output:
                shutil.copyfileobj(source,output)
    (TARGET/'provenance.json').write_text(json.dumps({'download_source':URL,'sha256':digest,'verified':True,'version':'9.0.2'},indent=2),encoding='utf-8')
    print(json.dumps({'media_tools_available':True,'archive_checksum_verified':True,'version':'9.0.2'}))

if __name__=='__main__':
    main()
