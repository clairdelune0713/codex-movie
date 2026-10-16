"""Refresh reviewable directed script and verify immutable source/masters locally."""
import hashlib,json
from render_movie import ROOT,read,save,helper,now
p=read(ROOT/'project.json');original=ROOT.parent.parent/'SOMEWHERE_BETWEEN_US_READY'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
before=read(ROOT/'exports/source-integrity-before.json')
after={f.relative_to(original).as_posix():sha(f) for f in original.rglob('*') if f.is_file()}
assert before==after,'Source package changed'
asset_audit=read(ROOT/'exports/finalized-asset-copy-audit.json')
for a in asset_audit['assets']:
 assert sha(ROOT/a['path'])==a['source_sha256']==sha(ROOT.parent/'dog-20261014'/a['path'])
lines=['# dog-20261015 - directed production record','',
 '600 seconds; 1920x1080; 16:9. This document is production material and never appears as on-screen text.','']
for c in p['chapters']:
 lines.extend([f"## {c['chapter_index']:02} {c['id']} | {c['duration']} seconds",'',c['prompt'],''])
(ROOT/'exports/director-script.md').write_text('\n'.join(lines),encoding='utf-8')
save(ROOT/'exports/delivery-input-audit.json',{'checked_at':now(),'revision':p['revision'],
 'source_files_unchanged':len(after),'finalized_selected_asset_files_unchanged':len(asset_audit['assets']),
 'duration_seconds':sum(c['duration'] for c in p['chapters']),
 'chapters':len(p['chapters']),'scope':'File hashes and directed script only; media reviews are recorded separately.'})
print('Verified original source files:',len(after),'and identical finalized masters:',len(asset_audit['assets']))
