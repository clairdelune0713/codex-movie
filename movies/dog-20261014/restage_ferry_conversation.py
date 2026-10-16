"""Compliant original-cast cabin coverage after copyright-related output rejection.

Keep original dialogue and timing; show the approved young adult and Labrador,
with the child seated across the aisle outside the camera crop. No new identity
or copyrighted character is introduced, and provider moderation stays default.
"""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,'C:/Users/Admin 3/.codex/skills/movi2/scripts')
import project as h
p=json.loads((ROOT/'project.json').read_text(encoding='utf-8'));q=json.loads(json.dumps(p))
c=next(c for c in q['chapters'] if c['id']=='s12_c02')
c['tagged_assets']=['@AhMing','@TartWorking','@FerryInterior','@RecordingEquipment']
c['linked_asset_ids']=['asset_ah_ming','asset_tart_working','asset_ferry_interior','asset_recording_equipment']
c['first_frame']='A bright afternoon ferry cabin, camera facing the young adult Ah Ming seated on a teak bench; cream Tart lies beside his outside left shoe. The asking child and father sit across the aisle behind the camera, heard outside the crop.'
c['shots'][0]['camera']='50mm medium facing seated Ah Ming and resting dog from across aisle; asking child remains outside crop'
c['shots'][1]['camera']='65mm seated Ah Ming portrait, listening and replying toward off-screen child'
c['shots'][2]['camera']='65mm seated Ah Ming reaction portrait, gentle amused smile after off-screen greeting'
c['prompt']='''配音：只講自然香港廣東話，逐字用以下「」內對白。狗不說話，沒有旁白。未列明對白的時刻只有現場聲及呼吸。蛋撻用粵語發音。

SCENE CONTEXT
An original young Hong Kong Chinese blind man travels on an afternoon public ferry with his working Labrador. A child, seated beside his father across the aisle and outside the camera crop, politely asks to pet the dog. The man explains working-dog etiquette. The child's innocent morning greeting during the afternoon makes the man smile.

OUTPUT SETTINGS
22 seconds, 16:9, native 480p, normal real-time motion, exactly 3 timed shots.

VISUAL STYLE
Original tactile stylized 3D animation using these approved original character masters: soft dimensional daylight, expressive rounded anatomy, individual Hong Kong faces, textured cloth, teak, painted metal and detailed fur. Gentle understated comedy through the adult's listening pause and amused smile. The shot composition contains only the original young adult and his cream dog in the foreground.

ACTIVE REFERENCES
@AhMing: The one approved young Hong Kong Chinese adult, short dark hair, dark rectangular glasses, textured teal jacket over open white shirt, dark trousers. Exact original face and wardrobe.
@TartWorking: The one approved adult cream Labrador, warm beige ears, natural cream fur, brown guide harness with two-arm silver handle and brown cross-grip. Collar D-ring empty, no flexible collar lead. He lies on the cabin floor beside Ah Ming's OUTSIDE LEFT shoe, with clear space outside both legs.
@FerryInterior: Architecture only: teak slat bench, green steel uprights, cream riveted ceiling, clear aisle, blue daylight harbour through rectangular windows. Practical lamps unlit. The camera faces Ah Ming's bench; the child/father bench is behind the camera and is not in the crop. Use the separately bound original man and dog for their identities.
@RecordingEquipment: Only the plain closed navy bag resting next to Ah Ming. No recorder, phone or headphones in this conversation.

LOCATION MAP
Camera stays on the aisle side facing the one seated young adult and his dog. The child and father remain seated across the aisle behind the camera, speaking from that consistent offscreen position. Ah Ming turns slightly toward their voices. No reverse shot to another character. Tart stays beside the outside shoe, away from the clear aisle.

FIRST FRAME
50mm medium of the seated young adult and floor-level Labrador in the softly moving afternoon cabin. Closed navy bag beside him, hands relaxed on his lap. Daylight gives a gentle rim on the man's teal cloth and dog's cream fur.

TIMELINE
Shot 1 (0-7s): 50mm medium facing seated Ah Ming and floor-level dog. The child asks politely from offscreen across the aisle. Ah Ming lifts his listening face toward the voice; hands remain on his own lap. Tart rests calmly.
EXACT DIALOGUE — CHILD, OFFSCREEN: 「可唔可以摸吓佢？」

Shot 2 (7-17s): Hard cut to 65mm Ah Ming upper-chest portrait with cabin window behind. He explains gently to the child outside the crop, then listens. The child thinks for a brief beat and gives the innocent greeting from that same offscreen position. Let the small comic mismatch of afternoon and morning greeting land through the man's response.
EXACT DIALOGUE — AH MING: 「佢而家做緊嘢。等佢放工先，好唔好？」
EXACT DIALOGUE — CHILD, OFFSCREEN: 「咁……早晨，蛋撻。」

Shot 3 (17-22s): Hard cut to 65mm seated Ah Ming reaction portrait. A tiny amused breath, then his warm permissive reply toward the same offscreen voice. End on his natural smile, with gentle ferry movement continuing.
EXACT DIALOGUE — AH MING: 「呢個可以。」

AUDIO AND FINISH
Only the four exact Cantonese lines above, once each, with original natural conversational voices. Native cabin engine hum, faint water, quiet cloth movement and a soft amused breath; no score in this small conversation. All words finish inside the shot. Physical dog stays silent except natural breathing. Render one full cinematic frame, using sheets as identity references only. No panels, author, title, subtitles, captions, watermark, credits, slogans or other overlays. Normal speed, clean explicit cuts, 22 seconds total. Keep tiny living motion during listening instead of frozen holds.
'''
c.setdefault('prompt_refinements',[]).append({'reason':'A second output was rejected for copyright restrictions without returned footage. Use compliant original young-adult/dog coverage throughout; child remains seated across aisle and speaks offscreen, so no generated child design can resemble a borrowed film character. Exact original four-line conversation, original approved assets, normal moderation and full duration retained. No same-prompt retry.'})
print(h.save(ROOT,p,q,'Use original seated-adult coverage for ferry conversation with offscreen child voice'))
