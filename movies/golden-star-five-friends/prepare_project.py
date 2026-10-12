import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HELPER = Path(r'C:\Users\admina\.codex\skills\movi2\scripts\project.py')

def run(*args):
    return subprocess.run([sys.executable, str(HELPER), *map(str, args)], check=True, capture_output=True, text=True).stdout

def main():
    project = json.loads((ROOT / 'project.json').read_text(encoding='utf-8'))
    definitions = json.loads((ROOT / 'asset-specifications.json').read_text(encoding='utf-8'))
    ref_dir = ROOT / 'assets' / 'references'
    ref_dir.mkdir(parents=True, exist_ok=True)
    for name in ('ls1.jpg', 'ls2.jpg'):
        shutil.copy2(Path(r'C:\Users\admina\Downloads') / name, ref_dir / name)
    project.update(input_mode='script', language='English', duration_mode='fixed', total_duration_target=120, aspect_ratio='16:9')
    project['source_text'] = (ROOT / 'source-story.md').read_text(encoding='utf-8')
    project['high_level_idea'] = 'Five little plush friends discover that their shared wishes and enduring friendship can return a fallen golden star to the sky.'
    project['style'] = {'medium':'soft 3D plush animation', 'palette':'ivory, apricot, sunshine yellow, sky blue, lavender, honey gold', 'lighting':'soft warm daylight progressing to peach sunset and gentle periwinkle starlight', 'constraints':['Lovely and cute throughout', 'Preserve supplied plush identities', 'No keychains or product tags', 'No titles, subtitles, credits, captions, signs, logos or any on-screen typography', 'No written constellation message', 'No frightening imagery', 'Tactile velvet fibers and embroidered faces', 'Complete living characters in video; reference sheets are technical body and face views']}
    project['script_changes'] = ['Condense introductions and dialogue to fit exactly 120 seconds while retaining all key story beats.', 'The friendship message is spoken as stars twinkle in random patterns, honoring the no-on-screen-text direction.', 'A first golden sunset edge begins the flight; the star reaches its place in the final sliver of sunset, and the night sky brightens immediately afterward.']
    project['asset_list'] = []
    for definition in definitions:
        d = dict(definition)
        d['generation_prompt'] = d.pop('prompt')
        d['id'] = 'asset_' + d['id']
        d.update(source='generated', media_type='Image', status_variants=[], candidates=[], selected_candidate_id=None, reference_paths=['assets/references/ls2.jpg','assets/references/ls1.jpg'] if d['category']=='character' else [])
        project['asset_list'].append(d)
    for name in ('ls1','ls2'):
        project['asset_list'].append({'id':'reference_'+name, 'tag':'@'+name, 'name':'Supplied plush photo '+name, 'category':'reference', 'description':'User-supplied identity reference only; remove keychains, loops and fabric product tags in animation.', 'source':'user', 'media_type':'Image', 'reference_paths':[], 'candidates':[{'id':name+'_original','path':'assets/references/'+name+'.jpg'}], 'selected_candidate_id':name+'_original'})
    beats = [
        ('Sunshine friends',12,'The five friends play together in the garden. Introduce their distinct personalities through brief actions.','Narrator: In Sunshine Valley, Mochi, Tiggy, Pip, Bubbles, and Lulu were the very best of friends.','Short visual character introductions with warm breathing room.',['@Mochi','@Tiggy','@Pip','@Bubbles','@Lulu','@SunshineValley']),
        ('A star needs help',18,'Pip finds the sparkling star under the mossy rock. Tiggy lifts it carefully; the star explains the sunset deadline.','Pip: A golden star! Star: Help! I fell from the sky. Return me before sunset, or tonight the stars will vanish! Mochi: A sky without stars? Oh no!','Discovery, surprise and a speakable plea need separate reactions.',['@Mochi','@Tiggy','@Pip','@Bubbles','@Lulu','@GoldenStar','@SunshineValley']),
        ('Tiggys big plan',16,'Tiggy boasts, spins exactly three times, throws the star straight upward, and gets a soft harmless bonk. His surprised wobble makes everyone giggle; Lulu catches the falling star.','Tiggy: I will throw it back! Lulu: Maybe we need a better plan!','Allow all three spins, a readable arc, the comic bonk and affectionate laughter.',['@Mochi','@Tiggy','@Pip','@Bubbles','@Lulu','@GoldenStar','@SunshineValley']),
        ('Bubbles tries',12,'Lulu hands the star to Bubbles. Bubbles floats upward toward a high tree crown, looks at the unreachable sky and returns safely. Sunset begins.','Bubbles: I can try... Oh. Still too far. Pip: The sun is setting!','A gentle ascent, hopeful pause and descent before the next idea.',['@Mochi','@Tiggy','@Pip','@Bubbles','@Lulu','@GoldenStar','@SunshineValley']),
        ('Five little wishes',15,'Lulu proposes a shared wish. Bubbles places the star on the moss. The friends make a small hand-in-hand circle: Mochi, Tiggy, Pip, Bubbles, Lulu. Each makes a wish; the star warms.','Lulu: Let us wish together. Mochi: Happiness! Tiggy: Courage! Pip: Adventure! Bubbles: Hope! Lulu: I wish we will always be friends.','Distinct voices and a quiet affectionate final wish; the emotional center.',['@Mochi','@Tiggy','@Pip','@Bubbles','@Lulu','@GoldenStar','@SunshineValley']),
        ('A rainbow ride',17,'A soft flash blossoms into a rainbow ribbon. It forms a broad safe cushion beneath all five, lifting them in a gently rising arc. They carry the star above the clouds.','Friends: Wheeee! Narrator: Five little wishes became one wonderful rainbow!','Transformation, lift-off and joyful airborne reactions remain readable.',['@Mochi','@Tiggy','@Pip','@Bubbles','@Lulu','@GoldenStar','@SunshineValley','@CloudSky']),
        ('The sky shines again',18,'During the last peach edge of sunset, the star floats from the rainbow to its place overhead. Sunset ends, thousands of tiny stars awaken, and the rainbow gently carries all five back to the same clearing. No stars form letters.','Star: Friendship makes the world brighter. Lulu: Together, we did it!','Star restoration resolves the deadline, followed by a warm message and safe return.',['@Mochi','@Tiggy','@Pip','@Bubbles','@Lulu','@GoldenStar','@CloudSky','@SunshineValley']),
        ('A cuddle and a wink',12,'All five cuddle in their home clearing under the sparkling sky. Pip asks about tomorrow; Tiggy agrees. Mochi jokes. Gentle laughter; the golden star winks in the final quiet beat.','Pip: Same time tomorrow? Tiggy: Of course! Mochi: Next time, let us find something that does not need to be thrown into space!','Leave two quiet final seconds for the star wink after the closing joke.',['@Mochi','@Tiggy','@Pip','@Bubbles','@Lulu','@GoldenStar','@SunshineValley'])
    ]
    project['chapters'] = []
    script = []
    offset = 0
    for index, (title,duration,summary,dialogue,pacing,tags) in enumerate(beats,1):
        project['chapters'].append({'id':f'chapter_{index:02}', 'chapter_index':index, 'title':title, 'duration':duration, 'high_level_idea':project['high_level_idea'], 'scene_summary':summary, 'rough_dialogue':dialogue, 'pacing_reason':pacing, 'absolute_start':offset, 'absolute_end':offset+duration, 'prompt':'', 'prompt_status':'awaiting_asset_approval', 'tagged_assets':tags, 'linked_asset_ids':[], 'delinked_asset_ids':[], 'shots':[{'start':0,'end':duration,'action':summary,'camera':'To be finalized after asset approval','audio':dialogue,'end_state':'See narrative beat'}], 'materials':[], 'storyboards':[], 'selected_storyboard_id':None, 'takes':[], 'active_take_id':None, 'screenshots':[]})
        script.append(f'{offset:03d}-{offset+duration:03d}s | {title}\n{summary}\n{dialogue}\n')
        offset += duration
    assert offset == 120
    project['detailed_script'] = '\n'.join(script)
    project['master_prompt_raw'] = 'Soft 3D plush animation; exactly five reference-grounded friends and one friendly golden star. English voices, whimsical music and gentle Foley. 16:9, 120 seconds. No visible text. Chapters are rough planning only until assets are approved.'
    project['generation_route'] = {'status':'awaiting_authorized_video_route', 'video_connector_available':False, 'credential_values_read':False}
    proposal = ROOT / 'proposal-initial.json'
    proposal.write_text(json.dumps(project,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT / 'screenplay-draft.md').write_text('# 120-second screenplay draft\n\n'+'\n'.join(script),encoding='utf-8')
    print(run('check',ROOT,'--from',proposal))
    print(run('commit',ROOT,'--from',proposal,'--reason','Create independent 120-second plush adventure, rough timeline and asset definitions'))

if __name__ == '__main__':
    main()
