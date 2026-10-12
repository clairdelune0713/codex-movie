import sys
sys.dont_write_bytecode=True
import json
import prepare

ROOT=prepare.ROOT
current=prepare.helper.read(ROOT/'project.json')
proposal=json.loads(json.dumps(current))
ch=next(c for c in proposal['chapters'] if c['id']=='chapter_04')
new_sounds=['Quiet felt contact, soft evening breeze. No music, melody or voices.','Soft air movement and felt rustle during the gentle lift. No music, melody or voices.','Soft cloth cuddle and one isolated original unpitched glassy sparkle. No music, melody or voices.']
prompt=ch['prompt']
for shot,sound in zip(ch['shots'],new_sounds):
    prompt=prompt.replace(shot['audio'],sound)
    shot['audio']=sound
prompt=prompt.replace('Its three-note chime is C5–E5–G5.','Its sound is one isolated original non-melodic soft glassy sparkle.')
old=prompt.split('AUDIO\nNative synchronized sound.')[1].split('\n\nIDENTITY SEPARATION LOCK')[0]
prompt=prompt.replace(old,'Native synchronized sound. The complete sound layers are soft evening air, tiny grass/felt Foley and an isolated original non-melodic sparkle for the star pulse. No background score, tune, melodic phrase, song, singer, artist style or audio recording reference. No spoken dialogue, narration, words or lyrics. Fresh original ambience and Foley only.')
ch['prompt']=prompt
ch['audio']='Original ambient/Foley and isolated non-melodic star sparkle; no music or speech.'
ch['prompt_revision_notes'].append('Second take was rejected by the output audio similarity filter; regenerate with original non-melodic ambience/Foley while preserving the white-friend identity correction.')
(ROOT/'chapters'/ch['id']/'prompt-v03.txt').write_text(prompt,encoding='utf-8')
prepare.write_json(ROOT/'proposal.json',proposal)
print(json.dumps(prepare.helper.save(ROOT,current,proposal,'Regenerate lift-scene rejected audio with original ambient and non-melodic Foley')))
