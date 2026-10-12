"""Refresh only this movie's portable creative source after a verified delivery."""
import importlib.util
from finish_movie import ROOT, HELPER, read, write

def main():
    live=read(ROOT/'project.json')
    final=read(ROOT/'exports'/'pip-fix-20261012'/'final-verification-v02.json')
    visual=read(ROOT/'exports'/'pip-fix-20261012'/'final-visual-review.json')
    if not live.get('pip_correction',{}).get('status')=='complete' or visual['status']!='passed':
        raise RuntimeError('Complete verified correction is required.')
    source=ROOT/'source'
    archive=read(source/'project.json')
    screenplay=[]
    for c in archive['chapters']:
        current=next(x for x in live['chapters'] if x['id']==c['id'])
        for key in list(c):
            if key not in ('takes','active_take_id','storyboards','selected_storyboard_id','screenshots') and key in current:
                c[key]=current[key]
        for key in ('reference_priority','generation_seed','generate_audio','prompt_version','refinement_reason'):
            if key in current:
                c[key]=current[key]
        dest=source/'chapters'/c['id']
        (dest/'prompt.txt').write_text(c['prompt']+'\n',encoding='utf-8')
        write(dest/'shots.json',c['shots'])
        screenplay.append(f"{c['absolute_start']:03d}-{c['absolute_end']:03d}s | {c['title']}")
        for shot in c['shots']:
            screenplay.append(f"  {shot['start']}-{shot['end']}s: {shot['action']}\n  {shot.get('audio','')}")
        screenplay.append('')
    archive['detailed_script']='\n'.join(screenplay)
    archive['continuity_notes']=live.get('continuity_notes',[])
    spec=importlib.util.spec_from_file_location('movi_source_validator',HELPER)
    helper=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    errors,warnings=helper.validate(source,archive)
    if errors:
        raise RuntimeError(errors)
    write(source/'project.json',archive)
    (source/'screenplay.md').write_text(archive['detailed_script']+'\n',encoding='utf-8')
    summary=read(source/'delivery-summary.json')
    keys=('duration_seconds','video_duration_seconds','frame_count','fps','width','height','audio_channels','audio_sample_rate','size_bytes','full_decode','original_soundtrack_preserved_exactly')
    checks={key:final[key] for key in keys if key in final}
    checks['version']=2
    checks['local_report']='exports/pip-fix-20261012/final-verification-v02.json'
    summary['observed_delivery_checks']=[x for x in summary['observed_delivery_checks'] if x.get('version')!=2]+[checks]
    write(source/'delivery-summary.json',summary)
    (source/'pip-correction.md').write_text('# Pip correction, version 2\n\nCorrected Pip to one complete chick with a separate yellow torso, two wings and two orange feet. Replaced the introduction, throw, Bubbles attempt, rainbow and return scenes. The full Bubbles take avoids visible cast position and scale jumps at a three-second splice. Original images and original soundtrack retained. Rainbow video is generated silently and combined with the original audio.\n\nReviewed new takes at half-second intervals and the final corrected ranges at one-second intervals plus edit boundaries. Verified 120 seconds, 1280x720, 30 fps, 3600 frames and full decode; decoded audio exactly matches the original delivery. Original movie and takes remain on disk.\n',encoding='utf-8')
    print({'source_archive':'golden-star-five-friends only','errors':errors,'warnings':warnings})

if __name__=='__main__':
    main()
