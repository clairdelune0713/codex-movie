"""Reuse the verified local adapter with this movie's explicit settings."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent
source=(ROOT.parent/'little-star-home'/'direct_client.py').read_text(encoding='utf-8')
source=source.replace('import prepare\n','import project_ops as prepare\n')
source=source.replace("ENV=ROOT.parents[2]/'aifx-studio'/'.env'","ENV=ROOT.parents[1]/'.env'")
source=source.replace("'settings_source':'User-authorized sibling environment file; only four named settings read; credentials retained in memory.'","'settings_source':'User-authorized workspace .env; only four named settings read; credentials retained in memory.'")
source=source.replace("elif sys.argv[1]=='submit': submit(client)","elif sys.argv[1]=='submit': submit(client,sys.argv[2:] or None)")
source=source.replace("if counts['succeeded']+counts['failed']==8: break","if counts['succeeded']+counts['failed']==len(prepare.helper.read(ROOT/'project.json')['chapters']): break")
source=source.replace("prepare.write_json(journal,record)\n        register_take(chapter_id,take)\n        try:","prepare.write_json(journal,record)\n        register_take(chapter_id,take)\n        ready=subprocess.run([sys.executable,str(prepare.HELPER),'render-ready',str(ROOT)],capture_output=True,text=True)\n        if ready.returncode: raise RuntimeError('Render readiness changed before submission')\n        try:")
target=ROOT/'seedance_client.py'
if target.exists():raise RuntimeError('Client already exists; preserve existing production code')
target.write_text(source,encoding='utf-8')
print('Prepared workspace-scoped Seedance client; no credentials copied.')
