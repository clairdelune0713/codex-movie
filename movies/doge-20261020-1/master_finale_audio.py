"""Master soundtrack loudness while stream-copying the verified movie's exact video packets."""
import hashlib,json,re,subprocess
from render_finale import ROOT,FF,read,save,probe
def run(args):
    r=subprocess.run([str(FF),'-hide_banner','-nostdin',*map(str,args)],capture_output=True,text=True,encoding='utf-8',errors='replace')
    if r.returncode:raise RuntimeError(r.stderr[-1600:])
    return r
def vh(path):
    r=run(['-v','error','-i',path,'-map','0:v:0','-c','copy','-f','hash','-hash','sha256','-']);return r.stdout.strip()
def main():
    m=read(ROOT/'exports/finale-assembly-manifest.json');src=ROOT/m['path'];out=src.with_name(src.name.replace('-v01.mp4','-v02.mp4'))
    if src==out or out.exists():raise RuntimeError('Preserve existing master; reconcile before another edit')
    filt='loudnorm=I=-18:TP=-1.5:LRA=11:measured_I=-25.40:measured_TP=-1.75:measured_LRA=10.00:measured_thresh=-36.07:offset=1.27:linear=false:print_format=json'
    r=run(['-i',src,'-map','0:v:0','-map','0:a:0','-c:v','copy','-af',filt,'-t','305','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',out])
    video_hash_source=vh(src);video_hash_final=vh(out)
    if video_hash_source!=video_hash_final:raise RuntimeError('Video stream must remain identical during audio mastering')
    check=run(['-v','error','-threads','2','-i',out,'-progress','pipe:1','-f','null','-']);counts=re.findall(r'^frame=(\d+)',check.stdout,re.M);frames=int(counts[-1]);info=probe(out)
    if frames!=7320 or info['duration']!=305:raise RuntimeError('Master runtime/frame validation failed')
    master={'source_path':m['path'],'path':out.relative_to(ROOT).as_posix(),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'final_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'video_stream_identical':True,'video_packet_sha256':video_hash_final,'loudness_target_lufs':-18,'true_peak_target_dbtp':-1.5,'source_measurement':{'integrated_lufs':-25.4,'true_peak_dbtp':-1.75,'range_lu':10,'threshold_lufs':-36.07},'filter':filt,'normalizer_log':r.stderr[r.stderr.rfind('{'):r.stderr.rfind('}')+1],'verification':{**info,'decoded_frames':frames,'full_decode_verified':True}}
    save(ROOT/'exports/audio-mastering.json',master)
    m['previous_picture_master_path']=m['path'];m['path']=master['path'];m['audio_mastering']=master;m['verification']=master['verification'];save(ROOT/'exports/finale-assembly-manifest.json',m)
    print(json.dumps({'path':master['path'],'video_stream_identical':True,'frames':frames,'duration':info['duration'],'normalizer_log':master['normalizer_log']},indent=2))
if __name__=='__main__':main()
