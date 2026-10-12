"""Scoped prompt-only repairs based on actual failed/inspected takes."""
import sys
sys.dont_write_bytecode=True
import json
import prepare
import director

ROOT=prepare.ROOT
current=prepare.helper.read(ROOT/'project.json')
proposal=json.loads(json.dumps(current))
for ch in proposal['chapters']:
    if ch['id']=='chapter_04':
        prompt=ch['prompt']
        for tag in ('@Tora','@Mimi'):
            prompt='\n'.join(line for line in prompt.split('\n') if not line.startswith(tag+': '))
        prompt=prompt.replace('@Tora and @Mimi stay offscreen.','The other friends remain outside this crop.')
        prompt=prompt.replace('Exactly 5 named friends exist in this scene','Exactly 3 named friends exist in this scene')
        prompt=prompt.replace('POSITIVE CONSTRAINTS / CONTINUITY LOCKS','IDENTITY SEPARATION LOCK\n@Mochi is the WHITE friend from its own reference, with WHITE ears with pink interiors, round pink cheeks, curved happy eyes and open pink-tongue smile. @Mochi has NO headphones, gray ears, headband or flower cheeks. There is no headphone-wearing friend in this scene. Do not borrow any features between the white friend, yellow friend and blue friend. Each is one assembled character, not a sheet of pieces.\n\nPOSITIVE CONSTRAINTS / CONTINUITY LOCKS')
        ch['tagged_assets']=[t for t in ch['tagged_assets'] if t not in ('@Tora','@Mimi')]
        ch['prompt']=prompt
        ch['prompt_revision_notes']=['First take gave the white friend headphone-cat features. Remove unused-character inputs and lock white friend anatomy.']
    if ch['id']=='chapter_02':
        prompt=ch['prompt']
        prompt=prompt.replace('a quiet celesta and pizzicato phrase','no background music')
        prompt=prompt.replace('low quiet instrumental continuation','no background music')
        prompt=prompt.replace('instrumental score kept modest','no background music')
        prompt=prompt.replace('one faint C5 bell','one faint original unpitched glassy sparkle')
        old=prompt.split('AUDIO\nNative synchronized sound.')[1].split('\n\nPOSITIVE CONSTRAINTS')[0]
        prompt=prompt.replace(old,'Native synchronized sound. The complete audio layers are soft evening breeze, grass/felt Foley and isolated original non-melodic glassy sparkle sounds for the star pulses. No background music, no identifiable melody, no tune imitation, no artist style, no recording references. No voices, narration, spoken dialogue or sung lyrics. All sound is freshly generated for this original scene.')
        ch['prompt']=prompt
        ch['audio']='Freshly generated original ambient and Foley, isolated non-melodic star sparkles. No music or speech.'
        ch['prompt_revision_notes']=['Provider rejected the generated audio for potential copyright similarity. Replacement requests only original atmosphere and non-melodic Foley.']
    if ch['id'] in ('chapter_02','chapter_04'):
        for take in ch['takes']:
            if ch['id']=='chapter_04': take['quality_disposition']='not_selected_identity_cross_contamination'
        (ROOT/'chapters'/ch['id']/'prompt-v02.txt').write_text(ch['prompt'],encoding='utf-8')
prepare.write_json(ROOT/'proposal.json',proposal)
print(json.dumps(prepare.helper.save(ROOT,current,proposal,'Refine only failed audio scene and white-friend identity error from inspected take')))
