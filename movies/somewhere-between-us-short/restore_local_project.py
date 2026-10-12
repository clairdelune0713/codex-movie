"""Restore a fresh local production state from the versioned source archive."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'source'
HELPER=ROOT.parents[1]/'skills'/'movi2'/'scripts'/'project.py'

def main():
    if (ROOT/'project.json').exists():
        print('Local project.json already exists; no production state was changed.')
        return
    p=json.loads((SOURCE/'project.json').read_text(encoding='utf-8'))
    references=set()
    for a in p['asset_list']:
        references.update(a.get('reference_paths',[]))
        references.update(c['path'] for c in a.get('candidates',[]) if c.get('path'))
    for c in p['chapters']:
        references.update(m['path'] for m in c.get('materials',[]) if m.get('path'))
    for relative in references:
        src=(SOURCE/relative).resolve()
        dst=(ROOT/relative).resolve()
        if not src.is_relative_to(SOURCE.resolve()) or not dst.is_relative_to(ROOT):
            raise RuntimeError('Escaping media path: '+relative)
        if not src.is_file():
            raise FileNotFoundError(src)
        if dst.exists() and dst.read_bytes()!=src.read_bytes():
            raise RuntimeError('Existing local media differs; preserve it and choose a fresh project directory: '+relative)
        dst.parent.mkdir(parents=True,exist_ok=True)
        if not dst.exists():
            shutil.copy2(src,dst)
    subprocess.run([sys.executable,str(HELPER),'init',str(ROOT),'--name',p['project_name']],check=True)
    fresh=json.loads((ROOT/'project.json').read_text(encoding='utf-8'))
    p.update(id=fresh['id'],revision=fresh['revision'],created_at=fresh['created_at'],updated_at=fresh['updated_at'])
    proposal=ROOT/'proposal-restored-source.json'
    proposal.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    subprocess.run([sys.executable,str(HELPER),'commit',str(ROOT),'--from',str(proposal),'--reason','Initialize local production from versioned creative source'],check=True)
    print('Source restored. Assets still require an explicit visual review before new generation.')

if __name__=='__main__':
    main()
