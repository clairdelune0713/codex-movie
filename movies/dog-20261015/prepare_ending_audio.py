"""Retain finalized original performance locally for a picture-only repair."""
import copy,hashlib,subprocess,wave
from render_movie import ROOT,FF,read,save,helper,now
p=read(ROOT/'project.json');oldroot=ROOT.parent/'dog-20261014';old=read(oldroot/'project.json')
cid='s16_c06';oc=next(c for c in old['chapters'] if c['id']==cid)
ot=next(t for t in oc['takes'] if t['id']==oc['active_take_id'])
source=oldroot/ot['path'];dest=ROOT/'source/finalized_audio/s16_c06_original_performance_12s.wav'
if not dest.exists():
 subprocess.run([str(FF),'-v','error','-nostdin','-ss','4.9','-i',str(source),'-t','12','-vn','-c:a','pcm_s16le','-ar','48000','-ac','2',str(dest)],check=True)
with wave.open(str(dest)) as w:assert w.getnframes()==576000
provenance={'source_project':'dog-20261014','source_chapter':cid,'source_take':ot['id'],
 'source_path':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'source_interval_seconds':[4.9,16.9],'destination_duration_seconds':12,
 'path':dest.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
 'scope':'Finalized existing original character performance reused only in local edit. No audio reference is uploaded. New picture remains native 1080p.'}
save(ROOT/'source/finalized_audio/s16_c06_provenance.json',provenance)
proposal=copy.deepcopy(p);c=next(c for c in proposal['chapters'] if c['id']==cid)
c['generate_audio']=False;c['post_audio']={k:provenance[k] for k in ['path','sha256']}
c['post_audio']['provenance_file']='source/finalized_audio/s16_c06_provenance.json'
c['prompt']='PICTURE-ONLY REPAIR\nGenerate visual action only. Existing finalized original scene audio will be conformed locally; do not generate any audio. Retain listed exact dialogue as speaking performance cues only. May describes photo in shot1; Ah Ming reacts and speaks near10.2-11.7 seconds in shot2. No on-screen text.\n\n'+c['prompt']
print(helper.save(ROOT,p,proposal,'Use finalized original ending performance locally after rejected generated audio; request new native1080p picture only'))
