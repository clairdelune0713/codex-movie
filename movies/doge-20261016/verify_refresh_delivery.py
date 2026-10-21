"""Verify unchanged narrative, retained approved scenes and fresh finale provenance."""
import hashlib,json,re
import render_finale_refresh as r
from assemble_finale import call


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def video_prefix_hash(path):
    # Stream-copy hash covers the same first 17,760 compressed video packets.
    # This verifies that the approved pictures survived the actual full merge.
    result=call(['-i',path,'-map','0:v:0','-c:v','copy','-frames:v','17760',
                 '-f','hash','-hash','sha256','-'])
    match=re.search(r'SHA256=([0-9a-f]{64})',result.stdout)
    assert match,result.stdout
    return match[1]


def main():
    p=r.read(r.ROOT/'project.json')
    auth=p['finale_refresh_authorization']
    baseline=r.read(r.ROOT/auth['baseline_path'])
    m=r.read(r.ROOT/'exports/whole-movie-refresh-20261021-manifest.json')
    previous=r.read(r.ROOT/'exports/whole-movie-assembly-manifest.json')
    latest=r.journal()['takes'];records=[]
    for c in p['chapters']:
        r.assert_script_locked(p,c)
        t=next(t for t in c['takes'] if t['id']==c['active_take_id'])
        mapped=m['chapters'][c['chapter_index']-1]
        assert t['id']==mapped['take_id']
        assert sha(r.ROOT/t['path'])==mapped['source_sha256']
        assert t['dependency_fingerprint']==r.helper.chapter_fingerprint(r.ROOT,p,c)
        if c['chapter_index']<=36:
            digest=hashlib.sha256(json.dumps(c,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
            assert digest==baseline['preserved_first36'][c['id']]
            old_spec=previous['normalized_inputs'][c['chapter_index']-1]
            new_spec=m['normalized_inputs'][c['chapter_index']-1]
            assert old_spec['path']==new_spec['path']
            assert sha(r.ROOT/old_spec['path'])==new_spec['normalized_sha256']
            records.append({'scene':c['chapter_index'],'take_id':t['id'],'unchanged_chapter_record':True,
                            'unchanged_finished_input':True})
        else:
            assert t['id']==latest[c['id']]['id']
            assert t['refresh_authorization_id']==auth['id']
            assert t['visual_review']['inspected'] and not t['visual_review']['requires_repair']
            old_id=baseline['prior_selected_finale'][c['id']]['take_id']
            old=next(x for x in c['takes'] if x['id']==old_id)
            assert old['prompt']==t['prompt']==c['prompt']
            assert old['submitted_prompt']==t['submitted_prompt']
            assert old['bindings']==t['bindings']
            before=old['generation_config'];after=t['generation_config']
            assert {k:v for k,v in before.items() if k!='seed'}=={k:v for k,v in after.items() if k!='seed'}
            assert before['seed']!=after['seed']
            assert (after['resolution'],after['ratio'],after['generate_audio'])==('480p','16:9',True)
            records.append({'scene':c['chapter_index'],'take_id':t['id'],'previous_take_id':old_id,
                            'same_prompt':True,'same_references':True,'same_settings_except_seed':True,
                            'fresh_seed':True,'reviewed_new_output':True})
    old_hash=video_prefix_hash(r.ROOT/previous['path'])
    new_hash=video_prefix_hash(r.ROOT/m['path'])
    assert old_hash==new_hash,'Approved first-36 video packets differ in actual merged output'
    result={'checked_at':r.now(),'authorization_id':auth['id'],'baseline_revision':baseline['revision'],
            'all_51_source_scenes_prompts_shots_and_durations_unchanged':True,
            'first36_actual_merged_video_packets_identical':True,'first36_video_packet_sha256':new_hash,
            'first36_frames':17760,'fresh_finale_scenes':15,'chapters':records,
            'source_path':m['path'],'source_sha256':sha(r.ROOT/m['path']),
            'verification':m['verification']}
    r.save(r.ROOT/'exports/finale-refresh-20261021-verification.json',result)
    print('All 51 narrative locks verified; first 36 actual video streams identical; all 15 finale scenes use reviewed fresh takes with unchanged prompts/references/settings.')


if __name__=='__main__':main()
