"""Author the approved source into an exact-duration cinematic proposal. No network."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
P = json.loads((ROOT/'project.json').read_text(encoding='utf-8-sig'))
if P['revision']!=8:
    raise SystemExit('Initial direction already completed; preserve subsequent refinements and takes.')
A = {a['tag'][1:]: a for a in P['asset_list']}

# Last source-block index in each shot, shot length, camera and concrete staging.
# Different lengths follow the performance, rather than dividing runtime evenly.
PLAN = {}
def add(cid, tags, location, first, beats):
    PLAN[cid] = dict(tags=tags.split(), location=location, first=first, beats=beats)

add('s01_c01','TartPuppy TinePuppy TrainingCast VictoriaPuppyYard PuppyBenchAndCrates SqueakyToy',
    'Victoria ranch. Low timber bench centre; gate and distant handler rear left; open pasture behind fence. Toy under bench; wider side gap camera right. Preserve bench leg positions between cuts.',
    'Low wide at puppy eye height: cream Tart left studies the bench, brown Tine entering right; worn teal-and-yellow toy under it.',
    [(1,4,'28mm low wide, short lateral dolly','Establish the bench, toy and two puppy personalities.'),(3,7,'50mm side medium, locked','Tine squeezes under, hindquarters stop at the turn, reverses on two shuffling paws; folded ear is the punch line.'),(4,5,'65mm low three-quarter close shot','Tart goes around the leg and reaches through the wider gap; one paw slides the toy toward Tine, not through solid wood.')])
add('s01_c02','TartPuppy TinePuppy VictoriaPuppyYard PuppyBenchAndCrates SqueakyToy',
    'Same bench axis and grass. Tart screen left, Tine screen right, one worn two-ended toy between them. Each puppy keeps his own body and markings.',
    'The toy has just slid clear of the bench toward Tine; Tart has withdrawn his paw.',
    [(7,5,'50mm low two-shot','Pounce causes one squeak, both hop back; two investigating noses nearly meet.'),(9,4,'65mm low two-shot','Tart presses once for the second squeak; broad and precise play bows contrast.'),(12,7,'40mm full-body two-shot, small track','Both grip opposite ends; Tine shuffles too far and sits, Tart wins, considers leaving, then offers the free end back.')])
add('s01_c03','TartPuppy TinePuppy VictoriaPuppyYard PuppyBenchAndCrates PuppyWaterBowl SqueakyToy',
    'Same yard. Bench centre, shallow bowl at the outside right bend. Tart takes the tight inside route; Tine the wider arc, safely away from the handler.',
    'Tart offers the toy end; Tine springs up on all four paws.',
    [(13,6,'28mm puppy-height tracking arc','Normal-speed chase around bench; paws touch ground, bowl splashes from Tine stepping through it.'),(14,8,'55mm medium, camera settles','Tine examines one wet paw, shakes it, tries the other; Tart waits with toy, then Tine remembers and returns. Keep active comic thought, not a frozen hold.')])
add('s01_c04','TartPuppy TinePuppy TrainingCast VictoriaPuppyYard VictoriaRainShelter PuppyBenchAndCrates SqueakyToy PuppyPhotograph',
    'Same bench in a light shower, shelter behind left with open door. Dry patch is under the right side. One female ranch handler approaches from the gate; other puppies remain distant soft background.',
    'First drops mark the timber; the two named puppies duck beneath the bench.',
    [(16,5,'40mm under-bench two-shot','Tine leans, Tart shifts a paw width, Tine follows.'),(19,7,'65mm intimate side shot','Two separate drops tap Tart nose; he returns to the dry patch, turns once and settles with chin across Tine forelegs; toy between paws.'),(21,6,'50mm handler-side medium, then motivated photo insert','Handler crouches and photographs the settled pair, reaches to gather them; match cut to that same physical archive print. Only its small diegetic archive caption may be legible.')])
add('s01_c05','GrowingDogs TrainingCast VictoriaDepartureYard PuppyBenchAndCrates PuppyTransportVehicles PuppyPhotograph',
    'Covered departure yard after a months-long ellipsis. Adolescent cream Tart left, chestnut Tine right, separate open crates facing handlers, two separate vehicles beyond. Same ranch gate, rain beyond roof.',
    'The archive print rests in a kennel file; cut immediately to the now larger dogs beside their separate crates. No date card.',
    [(23,7,'50mm two-shot at adolescent shoulder height','Tine leans and Tart stays; handlers allow this contact before guiding onward.'),(24,7,'35mm wide with readable hands and crate doors','One dog enters each crate, doors close calmly, each crate secured in a different vehicle.'),(27,7,'65mm alternating vent details, then 35mm gate wide','Separate noses at separate vents; one vehicle departs while the other stays. Rain occupies the gap; ranch wind bridges toward harbour wind, without overlay text.')])
add('s02_c01','GrowingDogs TartWorking TrainingCast GuideTrainingPath',
    'Victoria guide training path, obstacle central. Tart left of his trainer, narrow opening straight ahead and wider route around right. Age progresses across a clear training-session cut, never by body morphing.',
    'Young cream Tart approaches the obstacle beside the trainer, both fully visible.',
    [(0,4,'35mm moving wide','Establish training and shared pace in one complete approach.'),(1,14,'40mm lateral wide, short cut to reward detail','Show gap fits dog but not human; Tart stops, selects wider route, clears both bodies and receives reward. Finish on successful partnership, adult working identity after session ellipsis.')])
add('s02_c02','GrowingDogs TineAdult TrainingCast HKPracticeRoom',
    'Hong Kong practice room: blue moulded chairs, one low chair with loose cream cushion. Seated female volunteer right, handler left, Tine between with open retreat space.',
    'Tine enters beside handler; cushion sits loose at tail height on the low chair.',
    [(2,10,'40mm full-body three-shot','Tail knocks cushion down; Tine investigates then notices withdrawn hands and stops; handler allows quiet settling.'),(3,6,'65mm volunteer-hand and dog-shoulder medium','Small later-session cut: offered hand lowers, dog chooses shoulder contact with four paws grounded.')])
add('s02_c03','TartWorking TineAdult AhMing May TrainingCast HKPracticeRoom',
    'Two distinct introductions separated by a clean cut in the blue-chair practice room. First Ah Ming seated left and Tart right; second May seated right and Tine left. Never put both pairs into the same session frame.',
    'Ah Ming introduces his hand at Tart shoulder height, palm relaxed; Tart has room to choose approach.',
    [(4,9,'65mm hand-and-shoulder medium, then 40mm side track','Gentle touch and voluntary step closer; brief later-session cut shows Ah Ming and Tart falling into pace.'),(5,9,'50mm seated full-body two-shot','Tine tries climbing onto May lap, she redirects onto floor, he compromises by laying chin on her knee; affectionate comic release.')])
add('s02_c04','May TrainingCast HKPracticeRoom PuppyPhotograph TartWorking GuideTrainingPath',
    'Practice room handover at left, May tan bag open on her lap. The one captioned puppy print enters its flat inner pocket. End on a low paw match, not a flight montage.',
    'Staff member holds out the same captioned puppy print toward seated May.',
    [(6,5,'65mm over-hand medium, short insert','May studies print and puts it safely flat into bag pocket.'),(7,3,'85mm paw detail match cut','Young cream paw on training path cuts to adult cream paw at Hong Kong doorstep; no morphing or text.')])
add('s03_c01','AhMing TartHome TartWorking AhMingFlat AhMingCup AhMingRadio AhMingKeys FoldingCane RecordingEquipment TartHarness',
    'Monday morning Ah Ming flat, use DAY view: oatmeal armchair, mustard cushion, side table with cream/teal cup. Plain wood entrance door, no internal gate. Dog on clear floor outside his legs. Bag on chair beside keys/radio.',
    'Ah Ming beside usual side table, collar-only Tart resting on floor left of chair.',
    [(0,5,'50mm hands and familiar objects, fluid insert sequence','Radio lowered, keys checked by touch, folded white/red cane and recorder packed in navy bag.'),(2,6,'50mm medium two-shot','Buckle sound lifts Tart head, Ah Ming speaks his amused line; dog anticipates.'),(4,9,'40mm seated-side full-body shot','Fit and check harness with dog beside him; collar lead remains packed. Working cue ends the beat; only tail tip disobeys stillness.')])
add('s03_c02','AhMing TartWorking StreetAndFerryCast ResidentialLiftLobby NeighbourTrolley',
    'Residential lift lobby. Tart at Ah Ming left, both outside doorway; maroon plaid shopping trolley partly across opening. Elderly grey-haired neighbour owns trolley. Keep path wide enough for person and dog.',
    'Tart has stopped safely before the trolley wheels; neighbour reaches to straighten them.',
    [(6,6,'35mm doorway wide','Neighbour notices obstruction, apologises and straightens wheels.'),(8,8,'50mm two-shot into 35mm lateral exit','Ah Ming replies without impatience; doorway clears before guide pair travels through together.')])
add('s03_c03','AhMing TartWorking CentralTram RecordingEquipment StreetAndFerryCast StreetObstructions',
    'Central public pavement recess safely inland from kerb. Deep green and cream double-decker tram behind, single trolley pole. Ah Ming stationary, Tart left beside him; deliveryman/trolley passes along foreground walking line.',
    'Guide pair stops fully inside recess, handle lowered before recorder comes out.',
    [(9,5,'40mm pavement wide into 65mm recorder detail','Set recording while stationary, unobstructed public path remains open.'),(11,8,'50mm two-shot, trolley crossing foreground','Ding-ding, then rattling trolley intrudes audibly; Ah Ming delivers dry joke as cart rolls past.'),(12,5,'65mm hands to 40mm medium','Save recording and pack device, then take guide handle; preserve the practical order.')])
add('s03_c04','AhMing TartWorking CentralTram LanKee RecordingEquipment',
    'Same Central recess with Lan Kee green canopy down the pavement right. Ah Ming stops before speaking phone reply; Tart stands left, harness handle at rest.',
    'Phone reminder has just sounded; Ah Ming remains stationary in recess.',
    [(14,9,'50mm medium, shallow background tram colour','Notification is a short natural device sound, then exact Cantonese reply; no invented spoken notification text.'),(17,9,'40mm two-shot, gentle reframe toward cafe','Phone away, cup sounds motivate turn; breakfast line, nose lift, dog waits for cue. End ready to move.')])
add('s04_c01','AhMing TartWorking May TineAdult CentreMorning CentreFurniture StreetAndFerryCast CentralTram StreetObstructions',
    'Parallel montage, hard cuts between Central pavement and Kowloon centre; never a combined location. Tart left of Ah Ming travelling screen right. Centre May left, Tine beside her, invited seated person right, withdrawing woman farther rear.',
    'Low Central view of crossing shoes, guide pair approaches trolley crossing their line.',
    [(1,9,'35mm dog-height lateral track','Tart slows, trolley passes, guide pair clears opening together.'),(2,9,'50mm dog-height centre medium','Match footsteps to Tine; May follows invited contact while Tine passes the withdrawing woman without intruding. Both dogs finish separate useful actions.')])
add('s04_c02','AhMing TartWorking StationLift PassengerSuitcase StreetAndFerryCast May TineAdult LokAndMother CentreMorning CentreFurniture',
    'Separate locations linked by a cut: station lift doors front on, then centre blue-blouse mother chair foreground with mustard-shirt Lok behind it. Lok and mother are the revised designs.',
    'Lift opens onto guide pair, traveller and teal suitcase exiting first.',
    [(3,8,'40mm lift wide','Wait for traveller and case to clear; both dog and Ah Ming enter; reflection closes with doors.'),(4,8,'50mm playful centre two-shot, head-height matched to child','Lok peeks from one side, hides, peeks other side; Tine stays beside May, ears swing with head, shy smile escapes Lok.')])
add('s04_c03','AhMing TartWorking AuntieLan LanKee LanKeeBreakfast May TineAdult CentreMorning CentreFurniture LokAndMother StreetObstructions',
    'Montage cut from cream laminate cafe table to sage centre chair. Tart working under table away from Ah Ming feet; child hand only at table edge. Tine on mat beside May in second location.',
    'Toast corner lands near Tart straight forepaws beneath cafe table.',
    [(6,8,'65mm low paw/nose detail with Auntie Lan hand entering','Tart sniffs but stays; Auntie Lan picks up toast before child offers it and says line.'),(7,6,'65mm low centre medium','Biscuit crumb attracts Tine, May quiet nonverbal cue redirects his eyes, person clears crumb, untidy hind leg settles.')])
add('s04_c04','AhMing TartWorking AuntieLan LanKee LanKeeBreakfast',
    'Earlier cafe payment at same Monday breakfast, preserve counter/green-canopy doorway. Auntie Lan behind counter left, Ah Ming right, Tart safely to his left clear of doorway.',
    'Ah Ming finishes paying while Auntie Lan looks at cream dog brown harness.',
    [(10,9,'50mm counter two-shot, dog visible lower edge','Name confusion and polite correction, allow comic listening reaction.'),(12,10,'40mm doorway wide, locked after pair exits','Auntie Lan corrects herself, Tart guides Ah Ming away; hold doorway only long enough for order clearance and slight daylight shift to establish minutes passing.')])
add('s04_c05','May TineAdult AuntieLan LanKee PetFriendlyCar StreetAndFerryCast',
    'Minutes later same doorway, Ah Ming/Tart already out of sight. May and Tine on public pavement, prearranged pet car at legal pickup farther right. Hong Kong right-hand-drive, all passenger doors conventional forward hinges at B-pillar for rear doors.',
    'May receives takeaway at outside collection shelf, Tine beside her on orange collar lead.',
    [(15,8,'50mm doorway medium','Auntie Lan jokes with both dog drink names, Tine wags immediately, May smiles.'),(16,7,'35mm pavement-to-car wide','May walks dog toward car; if loading is visible rear door swings FORWARD from front/B-pillar hinge, front door stays closed, grey-capped driver at right-hand driving seat. No simultaneous view or recognition of Tart.')])
add('s04_c06','AhMing TartWorking CentralTram StreetObstructions May TineAdult CentreMorning CentreFurniture CentreMembers UncleChan Newspaper',
    'Three short matched beats in separate places: clear public pavement; invited centre hand; centre far-right window chair with Chan behind newspaper. Guide pair travels right, visiting pair remains beside invited person.',
    'Oncoming stroller narrows pavement while Tart pauses with Ah Ming behind him.',
    [(17,3,'40mm low pavement wide, cut to centre shoulder medium','Stroller passes; invited older hand reaches Tine.'),(18,2,'50mm matched moving/resting pair of shots','Tart moves into cleared space; Tine stays under offered hand.'),(20,3,'65mm centre long-lens reveal','Newspaper rises before Chan face at far end; Tine notices and wag softens; music ends on cut to street.')])
add('s05_c01','AhMing TartWorking CentralCrossing CrossingVehicles',
    'Same modest Central junction. Camera on near pavement, opposite kerb beyond stripes. Exactly ONE pedestrian signal at FAR RIGHT opposite kerb. Grey van left-to-right already blocks stripes, blue queued car beyond. Tart left half-step ahead of Ah Ming, paws behind near kerb.',
    'Wide explicitly shows near-kerb guide pair, blocked crossing, queued van and the single opposite signal.',
    [(2,5,'28mm kerb-height establishing wide','Approach, stop, align, listen; audible phase changes though van still obstructs.'),(6,6,'50mm side two-shot with paws and handle visible','Two cues, dog declines without stepping; Ah Ming stays behind and feels absence of motion.'),(8,5,'85mm wheel/paw matched inserts, return wide','Brake light releases, van creeps then stops, Tart grounded behind kerb. Suspense is quiet competence, no near-collision.')])
add('s05_c02','AhMing TartWorking CentralCrossing CrossingVehicles StreetAndFerryCast StreetObstructions',
    'Identical crossing geography and single far-right opposite signal. Rust-jacket curly-haired pedestrian draws level on near pavement; guide pair stays behind same kerb. Van queued beyond until it can clear.',
    'Pedestrian about to pass notices van and stops beside guide pair.',
    [(12,9,'50mm three-shot with road in depth','Pedestrian explains; van tyres/engine now audible; Ah Ming replies and gives no extra forward cue.'),(15,7,'40mm side wide','Van clears as pedestrian phase expires; Ah Ming elects next cycle and briefly touches Tart shoulder.'),(16,4,'35mm same-axis short time-cut wide','Traffic phase passes, bag rustles; ordinary wait compresses in one clean time cut, without heroic score.')])
add('s05_c03','AhMing TartWorking CentralCrossing CrossingVehicles',
    'Same near kerb and ONLY far-right opposite signal. Striped path is now fully clear, vehicles stopped safely beyond. Tart left of Ah Ming; travel from foreground to opposite kerb.',
    'Fresh pedestrian phase sounds; Ah Ming reassesses before taking handle.',
    [(18,5,'50mm side medium with clear road visible','Listen, align, cue only after fresh phase.'),(19,9,'35mm lateral track then opposite-kerb wide','Complete normal-paced crossing for both bodies, step up and stop beyond other pedestrians walking line.'),(21,5,'65mm shoulder touch, widen into onward travel','Exact praise, shoulder rub, tail response, new direction; understated satisfaction.')])
add('s06_c01','May TineAdult UncleChan CentreMorning CentreFurniture Newspaper TineMatAndMayBag TineBowl UncleChanBag',
    'Monday centre ground-floor corner: glass front, right-hand street windows. Chan in separate wooden window armchair right; May takes sage chair left across open floor, exit remains clear. Tine mat beside May, orange lead slack and held.',
    'Members leave in soft background while Chan reads and May gathers mat/bowl at respectful distance.',
    [(3,7,'35mm room wide into 65mm Chan medium','Tine turns, newspaper lifts, refusal spoken clearly.'),(5,5,'50mm May response, maintain open space','May stops and sits across room; acknowledge without pushing contact.'),(7,6,'50mm low dog/May two-shot','Tine chooses mat rather than doorway farewell, faces slightly away; water, drink, settle, gentle exhale.')])
add('s06_c02','May TineAdult UncleChan CentreMorning CentreFurniture Newspaper OutingPapers TineMatAndMayBag',
    'Same two chairs and open distance, Chan right window and May/Tine left. Flyer on Chan lap, mat remains several feet away, no closing distance.',
    'Chan looks over lowered newspaper toward resting Tine.',
    [(9,6,'65mm Chan lap and dog in depth','Flyer slips naturally down, man reaches, dog lifts head and shifts one paw.'),(11,10,'50mm quiet two-plane shot','Chan hand pauses, Tine stops, Chan retrieves flyer himself and sits back; dog lowers head. Small reciprocal movements keep beat alive.')])
add('s06_c03','May TineAdult UncleChan CentreMorning CentreFurniture Newspaper TineMatAndMayBag',
    'Same spatial separation. Chan newspaper descends from face to lap, May seated across open floor, Tine relaxed on mat with one untidy hind leg.',
    'Chan looks across at Tine resting, curiosity replaces the paper barrier.',
    [(15,10,'65mm conversational shot/reverse shot, respect common axis','First four lines about rest and work, light dry timing.'),(19,9,'50mm Chan medium with dog foreground, reverse to May','Name question and answer, amused final naming observation, no exaggerated grimace.'),(20,3,'85mm hand and dog eyeline detail','Chan leaves open hand beside chair; Tine notices yet stays, ending on invitation possibility.')])
add('s06_c04','May TineAdult UncleChan Bo CentreMorning CentreFurniture Newspaper TineMatAndMayBag TineBowl',
    'Chan window chair right, May chair left, mat beside May. Bo appears in glass doorway background. Tine collar orange lead remains held loosely by May, approach path straight and open.',
    'Chan open hand hangs beside chair; Tine remains on mat awaiting permission.',
    [(23,11,'50mm shared wide into shoulder-contact medium','Invitation and confirming nod, dog slow approach stops in reach, turns shoulder, tentative touch becomes stroke; tail once, paws still.'),(26,8,'50mm three-shot with Bo in doorway','Bo quietly signals time; bowl packing motivates reluctant goodbye exchange.'),(27,5,'65mm farewell reverse toward doorway','Two fingers raised from paper, Tine looks back beside May and wags once before leaving.')])
add('s07_c01','AhMing TartWorking TartHome AhMingFlat HomeFurniture AhMingKeys TartHarness SqueakyToy',
    'Monday evening flat, NIGHT view. Plain wood doorway, harness hook nearby; oatmeal chair/mustard cushion and side table clear of tail. Collar-only home Tart after harness comes off, no attached lead.',
    'Ah Ming arrives, keys in usual place, Tart beside his left leg, harness still on.',
    [(1,5,'40mm full-body doorway shot','Harness fully removed and hung, off-duty cue.'),(3,8,'50mm chair-side two-shot','Whole-body shake; newer two-ended toy delivered to knee before Ah Ming finishes sitting, water request is gently amused.')])
add('s07_c02','AhMing TartHome AhMingFlat HomeFurniture SqueakyToy',
    'Same evening chair axis, glass is in Ah Ming hand then safely on side table away from toy and wagging tail. Tart on open floor in front-left of chair, outside legs.',
    'Toy against one knee; Ah Ming takes first sip.',
    [(5,6,'65mm knee/glass/dog medium','Toy transferred to other knee; sip then squeak comic punctuation.'),(8,11,'40mm seated full-body two-shot','Glass set down safely, hand finds toy end, controlled tug at floor level, dog plants paws, man yields a little and says line.')])
add('s07_c03','AhMing TartHome AhMingFlat HomeFurniture SqueakyToy',
    'Same chair and side table. Loose mustard floor cushion behind Tart at left, not a moving chair. Toy between hand and dog initially, glass remains safe.',
    'Tart braces at toy end while seated Ah Ming holds the other end.',
    [(9,8,'40mm full-body two-shot','Man lets go, dog weight shifts back, rump lands abruptly on soft floor cushion; look at cushion while holding toy.'),(10,7,'65mm expressive dog to seated-man medium','Soft thump makes Ah Ming laugh; dog returns and presses toy into hand. Cushion stays on floor.')])
add('s07_c04','AhMing TartHome AhMingFlat HomeFurniture SqueakyToy RecordingEquipment',
    'Later evening same flat. Ah Ming seated editing at familiar table, headphones now on only here; Tart beside chair outside feet, toy on floor. Editing sounds private, dog responds to visible hand.',
    'Moving editing hand above Tart nose, man securely seated.',
    [(11,5,'50mm hand/dog medium','Nudge to moving hand earns distracted ear rub; no reaction to private headphone sounds.'),(13,5,'65mm low side shot','Dog curls, toy across forepaws, shifts flank until foot contact; hand settles naturally on fur.')])
add('s08_c01','AhMing TartWorking May TineAdult PublicStationExit CentreWalkingRoute StreetObstructions',
    'Thursday Tsim Sha Tsui PUBLIC pavement. MTR exit left with solid side wall centre. Ah Ming/Tart emerge left then travel right behind wall; May/Tine outside only on wall other side near public bench. Centre is on nearby same street, never inside railway.',
    'High wide clearly maps both pairs several metres apart with solid wall blocking dog-height view.',
    [(1,7,'28mm high oblique establishing then 40mm exit medium','Guide pair emerges, stops to orient, receives direction.'),(3,9,'50mm low bench-side shot then brief high wide','Tine investigates leaf while May waits; upper angle explains proximity and physical wall occlusion without recognition.')])
add('s08_c02','AhMing TartWorking May TineAdult PublicStationExit StreetAndFerryCast',
    'Same wall and public routes. Tart/Ah Ming moving right beyond wall; May/Tine round its outer end later. Pedestrian flow naturally hides cream shoulder, never duplicate dogs.',
    'Low Tart profile as a faint collar-to-bench scrape comes from hidden far side.',
    [(4,4,'65mm dog ear/profile tracking','Ear briefly turns but working line continues.'),(6,6,'50mm Tine-side reveal around wall','Tine looks up, rounds wall; fleeting cream shoulder between legs vanishes. No confirmed sight or recognition.'),(7,4,'50mm May/Tine medium','Time check, one last look, willing follow toward centre; keep Tine outside station.')])
add('s08_c03','UncleChan May TineAdult CentreAfternoon CentreFurniture Newspaper UncleChanBag',
    'Thursday centre: same ground-floor glassfront/right street windows, afternoon daylight. Chan window armchair right, spare chair next to him; empty metal umbrella stand beside entry initially within tail sweep.',
    'Chan glances at clock, moves grocery bag off spare chair and takes unopened paper.',
    [(8,5,'65mm Chan chair medium','Show small preparations without dialogue.'),(9,8,'50mm doorway low full-dog shot','Tine enters, tail hits stand once, turns to inspect; pause, turns back, tail hits same stand again. Two discrete clongs.'),(10,3,'50mm May hand/dog medium','May shifts stand fully out of tail reach; dog remains untroubled.')])
add('s08_c04','UncleChan May TineAdult CentreAfternoon CentreFurniture',
    'Same Thursday window chair and doorway. Chan settles right, May/Tine left approaching across open floor on held slack lead.',
    'Chan turns from window chair toward arriving dog, hand available beside chair.',
    [(13,7,'65mm Chan call then dog full-body response','Name triggers rib-to-tail wag, dog starts forward then sees man lowering into seat and eases pace.'),(15,7,'50mm side two-shot at seated shoulder height','Second invitation, May brings dog alongside; finish within reach of waiting hand.')])
add('s09_c01','UncleChan May TineAdult LokAndMother CentreAfternoon CentreFurniture TineMatAndMayBag SqueakyToy PuppyPhotograph',
    'Thursday same window area. Chan right hand on Tine shoulder, May left with tan bag and sage mat, revised Lok beside revised mother behind left. One captioned print in flat bag pocket.',
    'Tine standing under Chan hand eyes soft; Lok watches close to his mother.',
    [(2,6,'50mm warm group medium','Lok observes recognition, Chan returns observation with a smile.'),(5,8,'65mm over-bag and child eyeline shot','May spreads mat, retrieves toy and print to prevent bending; Lok asks, May answers.'),(6,4,'85mm physical photo insert, return medium','Point to right-rump heart on Tine puppy, cream Tart alongside, caption below; print immediately back into bag. No investigation yet.')])
add('s09_c02','UncleChan May TineAdult LokAndMother CentreAfternoon CentreFurniture SqueakyToy TineMatAndMayBag',
    'Same window chair, Tine in open patch before Chan, May holds slack orange lead left; Lok half hidden behind mother chair. One visiting toy on floor.',
    'Tine sets toy in reach then prepares to pick it back up.',
    [(8,8,'50mm hand/toy/dog medium','Two offer-withdraw attempts with readable contact; Chan playful complaint.'),(10,8,'40mm dog full-body plus child reaction','May waits; toy finally stays in Chan hand, small squeak, broad bow; Lok laughs and steps out from chair.')])
add('s09_c03','May TineAdult LokAndMother UncleChan CentreAfternoon CentreFurniture',
    'Same open centre floor, Lok mustard shirt beside blue-blouse mother, May by dog collar lead. Dog shoulder at easy child reach, retreat path clear.',
    'Lok has stepped out but keeps his hands to himself before asking.',
    [(12,7,'65mm child/May conversational medium','Question, permission contingent on calm dog sitting.'),(13,9,'50mm shoulder-level three-shot','Tine settles first, May guides one gentle shoulder stroke, then child withdraws freely; cute shy confidence in revised Lok design.')])
add('s09_c04','UncleChan May TineAdult CentreAfternoon CentreFurniture UncleChanPhotograph UncleChanEffects',
    'Window chair close conversational area. Chan holds a small worn wife-and-yellow-village-dog photo from wallet, physically distinct from May puppy print, which stays in her bag. Tine beside Chan shoe.',
    'Chan opens wallet and carefully draws out worn family photograph.',
    [(16,10,'65mm worn-photo insert then Chan/May reverse medium','Old dog named Ah Wong and May asks if he played; lines conversational with time to listen.'),(19,10,'65mm Chan face/hands, warm street-window light','Slipper story, thumb smooths bent corner, wife/towel recollection. Quiet emotion stays in small hand movement.'),(20,4,'85mm low shoe/chin detail','May leaves brief silence; Tine chin settles against shoe, no flashback.')])
add('s09_c05','May UncleChan Bo TineAdult CentreAfternoon CentreFurniture OutingPapers UncleChanEffects',
    'Same table by window armchair. Bo places Saturday outing flyer between May and Chan; old photograph returns to Chan wallet, puppy print stays in May bag.',
    'Flyer slides onto table, May turns invitation to Chan.',
    [(23,8,'50mm three-person medium','May invites and Chan leaves choice open in short reply.'),(24,3,'85mm hands/pocket detail','Old photo away, flyer folded into same pocket, understated possibility.')])
add('s10_c01','AhMing TartWorking Bo UncleChan LokAndMother CentreMembers CentreAfternoon CentreFurniture RecordingEquipment OutingPapers',
    'Friday15:00 small listening gathering. Six sage stackable chairs around charcoal cylindrical speaker, no stage. Ah Ming beside Bo, Tart harness on below chair but outside feet. Chan window side, Lok and mother opposite. May/Tine absent.',
    'Compact semicircle, speaker on low table; Ah Ming finger on familiar playback control.',
    [(3,7,'35mm intimate group wide into 65mm control detail','Invite guesses; play ONLY recorded tram bell followed by delivery trolley.'),(6,9,'50mm Lok/Ah Ming reverse shots, dog ear detail','Two exact conversational lines, small group laugh, one ear lifts and rests.'),(7,5,'65mm Ah Ming medium','Introduce second clip, finger ready on control, do not invent a third recording.')])
add('s10_c02','AhMing TartWorking Bo UncleChan LokAndMother CentreMembers CentreAfternoon CentreFurniture RecordingEquipment OutingPapers',
    'Identical Friday semicircle, dog harness on/no collar lead beneath Ah Ming chair clear of feet. Speaker controls audio. No May/Tine.',
    'Ah Ming presses second playback control, room listens to earlier ferry ambience.',
    [(10,6,'50mm listening faces, speaker foreground','Short recorded water/horn/footsteps, Chan identifies Star Ferry, Ah Ming confirms.'),(13,9,'65mm control stop then Chan medium to dog detail','Playback visibly stops BEFORE work-memory line; flyer edge rub, dog adjusts, collar ring softly ticks chair leg; Chan looks down.')])
add('s10_c03','AhMing TartWorking Bo UncleChan LokAndMother CentreAfternoon CentreFurniture OutingPapers',
    'Same Friday circle with stopped speaker. Lok faces composed working Tart under Ah Ming chair; Bo can address Chan window side.',
    'Chan has just looked toward Tart; Lok follows gaze with a new question.',
    [(16,8,'50mm child/Ah Ming medium reverse','Question and home-toy joke; mother smiles at contrast.'),(18,10,'65mm Bo then Chan, shared axis','Invitation then wife-loss line, allow natural short breath; dog remains quiet under chair.')])
add('s10_c04','AhMing TartWorking Bo UncleChan LokAndMother CentreAfternoon CentreFurniture OutingPapers',
    'Same Friday chairs, Chan holds flyer across knee; Bo has pen and small attendance list. Dog comfortable beneath chair, no crowding.',
    'Invitation hangs briefly, Chan flyer in his hands, Bo waits without pressure.',
    [(21,9,'65mm Chan/Bo two-shot','One natural pause, Tart sigh, Chan asks about Tine and Bo answers.'),(24,13,'65mm flyer/hands then 50mm shared medium','Chan smooths flyer, chooses to sign up; Bo writes name without ceremony. Keep visible preparation/action, no long frozen hold.')])
add('s10_c05','AhMing TartWorking Bo UncleChan LokAndMother CentreAfternoon CentreFurniture OutingPapers',
    'Same Friday circle, meeting conclusion; flyer/list near Bo, sleeping working Tart beneath chair outside feet.',
    'Ah Ming turns toward Bo to agree tomorrow ferry arrival.',
    [(26,11,'50mm Ah Ming/Bo conversational reverse','Exact two planning lines at speakable pace, no displayed itinerary overlay.'),(27,3,'65mm low dog paw with child in depth','Lok leans for a look but keeps hands off; one sleeping paw twitch buttons scene.')])
add('s11_c01','UncleChan Bo UncleChanFlat UncleChanKettle UncleChanBag UncleChanEffects UncleChanPhotograph OutingPapers RecordingEquipment',
    'Friday evening Chan own home: plain dark wood chairs, russet sofa, wife photo beside dining table, cream/teal kettle in kitchen. Navy tote on table with flyer, hat from cupboard. Independent household routine.',
    'Chan unlocks door carrying groceries, sets them on kitchen counter.',
    [(1,10,'40mm home wide, 65mm purposeful object inserts','Kettle on, hat brushed, water/tissues/wallet checked into navy tote beside flyer.'),(4,10,'50mm phone conversation medium','Stationary phone call, Bo audio only; Chan hat reply with dry humour.'),(5,4,'40mm kitchen medium','Phone away and dinner preparation resumes naturally; no lonely montage or excessive pause.')])
add('s11_c02','UncleChan May TineAdult CentreAfternoon CentreFurniture UncleChanBag UncleChanEffects',
    'Saturday afternoon same centre, ground-floor step-free corner entrance. Clock around13:00 if visible. Chan hat on head entering front glass door; May and Tine inside left with clear welcoming floor.',
    'Match cut from hat at home to SAME hat worn through centre doorway, no date card.',
    [(7,10,'40mm doorway wide, low dog reaction','Tine starts exuberant greeting but stops to let Chan put tote down and settle.'),(9,11,'65mm Chan/dog medium','Exact early greeting line; hand reaches shoulder, dog leans just enough, affectionate comic restraint.')])
add('s12_c01','Bo May TineAdult UncleChan LokAndMother CentreMembers CentreAfternoon CentreWalkingRoute CentreFurniture OutingPapers TineBowl TineMatAndMayBag UncleChanBag UncleChanEffects',
    'Saturday13:00 centre departure. Bo near glassfront checking list, second colleague slate polo, elder members behind; Lok beside mother. Ground-floor planned walking route leads through public TST streets to harbour. No dogs inside railway.',
    'Small group ready near step-free glass exit, Bo checks attendance.',
    [(1,8,'35mm group wide with Bo medium','Check group, exact reassuring walk line.'),(2,7,'65mm bowl clip/lead detail then 35mm side track','May clips teal collapsible bowl to tan bag, checks collar lead; all set off together along short route.')])
add('s12_c02','AhMing TartWorking StreetAndFerryCast FerryInterior FerryExterior RecordingEquipment',
    'Saturday bright afternoon aboard green/cream ferry from Central. Wooden bench seats, aisle clear, practical lights OFF. Ah Ming seated left, Tart close at outside left foot away from aisle. Green-top boy and beige father opposite. Navy bag CLOSED.',
    'Ferry rocks gently, working dog lies beside seated handler; curious boy turns to father then addresses Ah Ming.',
    [(5,7,'40mm aisle-side group medium','Child asks permission; father quietly attends, no reaching for dog.'),(7,10,'65mm Ah Ming then boy reverse','Working explanation and boy tentative MORNING greeting despite afternoon; let innocent comic timing land.'),(8,5,'50mm Ah Ming reaction and father smile','Short permissive reply and smiles; never let boy touch working dog.')])
add('s12_c03','AhMing TartWorking StreetAndFerryCast FerryInterior FerryExterior May TineAdult UncleChan CentreWalkingRoute StreetObstructions',
    'Cut between ferry bench and public shore walk, clearly distinct. Working Tart left foot inside ferry, Tine beside Chan on shore with May holding orange lead. Bright Saturday afternoon both.',
    'Boy and father smiling across aisle, Tart still lying down.',
    [(9,6,'65mm dog eyelid then ferry window medium','One eye opens, settles, pier approaches outside; no on-board practical lights.'),(10,7,'50mm low shoreline lateral track','Leaf skitters, Tine briefly follows with nose then matches Chan pace; lead remains slack, no dragging.')])
add('s12_c04','AhMing TartWorking Bo StreetAndFerryCast FerryInterior FerryExterior RecordingEquipment',
    'Moored TST ferry: Ah Ming seated aboard until call ends. Wooden aisle leads toward side exit and short gently sloped gangway with simple navy/green rails to public forecourt. Crew blue sailor-collar shirts/navy trousers/soft navy caps. Use ferry geometry/cast masters, no old populated composite.',
    'Ah Ming seated on moored ferry bench, closed bag on lap, dog beside feet, phone at ear.',
    [(13,9,'50mm seated phone medium','Bo voice only then Ah Ming reply; boat stationary, gangway being readied off frame.'),(14,11,'40mm readable full-body track from bench to gangway','Phone packed BEFORE standing/taking handle; calm travelling cue, Tart guides down clear aisle and stable non-slip gangway with other passengers. Blue sailor crew stands aside, no grabbing handler or harness.')])
add('s13_c01','AhMing TartWorking May TineAdult Bo UncleChan LokAndMother CentreMembers FerryForecourt FerryExterior HarbourGeography NearerSeatingBay FartherMeetingBench StreetAndFerryCast',
    'Public TST ferry forecourt. Terminal back-left, main promenade continues EAST screen-right, original curved meeting bench farther east. Nearer stone seating bay a few metres inland behind planters at upper-right. Group crossing forecourt toward promenade; Tine always outside terminal.',
    'High wide maps terminal arrivals, centre group crossing, two paths about to intersect.',
    [(1,5,'28mm elevated geography wide','Read both routes, harbour, separate original east bench and inland near bay.'),(3,8,'40mm wide lowering to dog height','Tart/Ah Ming exit terminal, May/Tine with group few metres away, both adult dogs in ONE frame for first time. Horn causes tiny ear/head response only.')])
add('s13_c02','AhMing TartWorking May TineAdult Bo FerryForecourt PassengerSuitcase StreetAndFerryCast',
    'Same forecourt axis. Guide pair approaching from back-left toward screen-right; May/Tine near group crossing their path, stop to yield. Navy traveller and teal suitcase pass in intermediate depth, then case owner pauses.',
    'Group pauses, gap between two cases briefly reveals cream shoulder/brown harness to Tine.',
    [(5,6,'65mm low view through suitcase gap','Tine one tentative step within slack lead, May stops with him.'),(7,7,'50mm guide pair full-body and traveller foreground','Tart turns nose slightly then waits safely for stopped case, gap closes with passing travellers.'),(8,4,'65mm Bo medium oriented toward inland bay','Exact practical direction from Bo; no recognition or chase.')])
add('s13_c03','AhMing TartWorking May TineAdult Bo UncleChan LokAndMother CentreMembers FerryForecourt HarbourGeography NearerSeatingBay FartherMeetingBench PassengerSuitcase StreetAndFerryCast',
    'Same map: centre group angles INLAND to nearer seating bay behind planter screen; Ah Ming/Tart proceed EAST right along main promenade toward original farther curved bench, passing screened outer side of nearer bay.',
    'Bo leads group inland while suitcase owner begins rolling case clear.',
    [(10,7,'35mm ground-level wide maintaining two directions','Group turns into rest bay; clear case allows guide pair to resume safely east.'),(12,5,'65mm Tine looking back through people','Too late, cream dog faces forward again; neither handler notices other dog.'),(13,5,'28mm high oblique map, short moving shot','Show simple divergence: one pair east, group few metres inland. No teleportation or confirmed recognition.')])
add('s13_c04','May TineAdult NearerSeatingBay TineBowl MayWaterBottle',
    'Nearer inland seating bay clear patch beside stone bench. Harbour railing beyond main walking path, not immediately behind dog. May beside Tine with lead held.',
    'May sets teal collapsible bowl on level paving, opens cream bottle teal cap.',
    [(14,8,'65mm low bowl/dog medium, gently settle','Water pours into bowl, Tine drinks, May keeps lead slack; end at last lapping sound to carry into next scene.')])
add('s14_c01','May TineAdult UncleChan Bo LokAndMother CentreMembers NearerSeatingBay TineBowl MayWaterBottle UncleChanEffects',
    'Broad level inland bay. Group on fixed stone benches, main path passes entrance behind, harbour rail farther beyond. Tine drinks clear of bags, May left, Lok with mother right, Chan nearby with tissues.',
    'Last lap from bowl, ears lift and skin begins shake ripple.',
    [(2,6,'50mm low full-dog plus group wide','May guides dog into clear patch, Lok anticipates and steps back.'),(4,12,'50mm child/dog two-plane shot','Exact child line, one whole-body shake; single drop hits shoe, Chan offers tissue, Lok wipes with exaggerated care; Chan almost laughs.')])
add('s14_c02','May TineAdult UncleChan Bo LokAndMother CentreMembers NearerSeatingBay UncleChanBag UncleChanEffects',
    'Same bay, Chan seated right with navy bag, May/Tine beside him left. Group prepares to move toward original east meeting bench. Open clear path outside bay; lead held slack.',
    'Bo checks group as bags lift to shoulders; Chan looks across harbour.',
    [(6,6,'65mm Chan medium with harbour depth','Live fuller horn changes smile; hand rests on wallet within bag, no flashback.'),(10,8,'40mm full-body May/dog/Chan triangle','May and dog rise, one step toward path; dog sees Chan still seated, slows wag, returns within slack, May notices and stops.'),(12,8,'65mm Chan then May seated-height medium','Chan offers to stay behind; May chooses to sit with him. Perform small, sincere, no melodramatic tears.')])
add('s14_c03','May TineAdult UncleChan Bo LokAndMother CentreMembers NearerSeatingBay UncleChanBag',
    'Same bay. Chan seated, dog lies by outside of shoe; May sits left holding slack lead. Others comfortable nearby, Bo can see entire group.',
    'May lowers into seat while Tine folds down beside Chan shoe.',
    [(15,8,'65mm hand/shoulder low medium','Grip loosens, dog gently turns shoulder into reach, one stroke stops and resumes at man pace.'),(16,4,'40mm inclusive group wide','Bo quiet nonverbal question about meeting here gets nods, colleague sits with members; no new unscripted speech needed.')])
add('s14_c04','Bo AhMing May TineAdult UncleChan NearerSeatingBay FartherMeetingBench MayWaterBottle RecordingEquipment',
    'Stationary phone conversation with clear cuts between TWO locations: Bo stands at nearer bay entrance, group in her view; Ah Ming at original farther curved bench east, Tart out of crop if no dog reference needed. No walking while on phone.',
    'Bo at bay entrance raises phone, Chan and resting Tine behind her; call connects.',
    [(19,11,'65mm Bo then Ah Ming phone reverse, stable support','First two exact lines establish nearer bay and original bench; no new scene overlays.'),(21,8,'65mm matching phone reverse','Second two exact lines give return route and fixed entrance landmark.'),(23,4,'50mm bay group medium','Bo stays at entrance, May caps bottle, Chan open hand on dog shoulder; meeting changed causally because dog turned back.')])
add('s15_c01','AhMing TartWorking FartherMeetingBench HarbourGeography RecordingEquipment',
    'Original curved meeting bench farther EAST of nearer inland bay. Main promenade returns WEST screen-left on same path. Ah Ming stationary until phone packed, Tart left at his side.',
    'Call just ended at farther bench; phone in Ah Ming hand and working dog waiting beside him.',
    [(1,6,'50mm stationary full-body medium','Phone pocketed, orientation and exact direction cue.'),(2,6,'35mm lateral track west','Guide pair turns together and returns normal pace along established route.')])
add('s15_c02','AhMing TartWorking Bo NearerSeatingBay FerryForecourt PassengerSuitcase StreetObstructions StreetAndFerryCast',
    'Nearer bay entrance at main path. Stroller moving along path and traveller parked teal case temporarily narrow opening. Bo just inside entrance, guide pair outside, Tart left of Ah Ming. No one takes his arm or harness.',
    'Tart stops before opening too narrow for both bodies, Ah Ming safely behind stop.',
    [(6,8,'40mm entrance wide then conversational medium','Bo calls, Ah Ming asks obstruction question; keep obstacle visible.'),(8,7,'35mm wide with owner hands and stroller','Bo indicates case owner to move case, stroller continues away, owner rolls case fully clear, Bo confirms.'),(9,7,'40mm side track across widened opening','Ah Ming direction/quiet nonverbal forward cue, dog checks width then clears both bodies including shoulder.')])
add('s15_c03','AhMing TartWorking May TineAdult UncleChan Bo NearerSeatingBay',
    'Inside nearer bay open patch. Chan and May left bench, Tine beside Chan under held lead. Ah Ming approaches empty section of stone bench to right guided by Tart on his left; no blocked path or leash between them.',
    'Tine raises head as cream dog enters; Tart nose turns then returns to task.',
    [(13,9,'50mm dog reactions then two-handler medium','Single tail movement only; Ah Ming asks about dog, May identifies and keeps Tine beside Chan.'),(16,10,'40mm full-body seated approach, hands/bench readable','Bo gives bench direction, Ah Ming directs and locates seat with hand, sits securely, praises Tart.'),(17,3,'65mm waiting Tine and Chan hand detail','Tine stands but stays with May, Chan lifts hand to release contact.')])
add('s15_c04','AhMing TartWorking TartOffDuty TineAdult May NearerSeatingBay TartHarness',
    'Ah Ming SECURELY SEATED on stone bench, Tart standing OUTSIDE his left knee, never underneath or between legs. Working harness brown handle initially upright, separate brown collar lead in Ah Ming hand unattached. Tine several feet away beside May, orange lead held.',
    'Wide readable side view of seated handler and standing dog at outside left leg, hands at harness buckle.',
    [(18,13,'50mm fixed side full-dog and hands, one continuous action','Calm hand at shoulder, unbuckle, slide harness completely off, fold handle, put harness safely on bench; ONLY THEN clip separate brown lead to collar D-ring and take loop securely.'),(21,6,'50mm same axis, slight wider reframe','Click, exact off-duty line, collar-lead-only Tart shakes; Tine tail gives tentative answer. Both dogs stay outside human legs.')])
add('s16_c01','AhMing TartOffDuty May TineAdult UncleChan NearerSeatingBay',
    'Same bay open patch before seated handlers. Tart left on held brown collar lead, Tine right on May held orange collar lead. Removed folded harness stays on bench behind Ah Ming. Leads slack, separate, never crossed; only two dogs.',
    'May and Tine a few steps from Ah Ming/Tart, both dogs held close with loose leads.',
    [(2,6,'50mm seated-handler two-shot with dogs in lower frame','Permission question and calm agreement.'),(5,10,'50mm low full-body two-shot, gentle lateral arc without crossing axis','Handlers allow shallow curved approach, Tine stops short, Tart measured step, reciprocal shoulder/neck sniffs, half-step apart.'),(6,2,'65mm close two-dog profile','Small tail pause and softened mouth; brief readable adjustment, no flashback.')])
add('s16_c02','AhMing TartOffDuty May TineAdult NearerSeatingBay TineMatAndMayBag SqueakyToy',
    'Same open patch and separate held leads. One toy comes from May tan bag. Tart home toy remains at home; this is May visiting toy. Dogs left/right maintained.',
    'Tine leans toward Tart; Tart about to make a little space by shifting away.',
    [(9,6,'50mm low two-shot','Tart shifts, Tine starts to follow then chooses to wait, looks toward May; Tart looks back.'),(11,5,'65mm May bag to Tine mouth medium','May sits and produces single familiar two-ended toy, Tine takes it with soft squeak; Tart ears lift.'),(13,5,'65mm two muzzles and full toy, shallow field','Tine holds still, Tart noses free end, Tine lowers it, Tart takes end; no duplicate toy or impossible fused mouths.')])
add('s16_c03','AhMing TartOffDuty May TineAdult NearerSeatingBay SqueakyToy',
    'Same clear paving in front of seated handlers, separate slack brown/orange leads held. Tart left/Tine right; gentle tug within short safe radius, no circling around people or lead entanglement.',
    'Both adult dogs grip opposite ends of one toy, paws neatly grounded.',
    [(16,8,'40mm low full-body two-shot','Brief gentle tug, Tine adjusts paws and sits accidentally, toy ends in Tart mouth; tail sweeps paving once.'),(18,7,'50mm shared dog medium','Tart holds prize then returns free end without cue; Tine broad play bow, Tart precise reply, echo original puppy movements.'),(19,5,'65mm shoulders/head two-shot','Few light steps, shoulder bump, Tine folded ear briefly stays inverted; Tart noses it, Tine shakes ear right. No flashback or slow motion.')])
add('s16_c04','AhMing TartOffDuty May TineAdult NearerSeatingBay SqueakyToy',
    'Same bay. Handlers remain seated with held separate slack leads, dogs playing gently in lower foreground, folded harness on bench. Dialogue comments on sound, not visual sight by Ah Ming.',
    'Toy squeaks below frame, Ah Ming head turns toward playful paw sounds.',
    [(22,9,'50mm handlers two-shot with dogs visible foreground','Exact question and May answer, dogs keep gentle toy play underneath.'),(24,6,'65mm Ah Ming amused medium then low dogs','Final home-joke line, small shared laugh without interrupting dogs.')])
add('s16_c05','AhMing TartOffDuty May TineAdult NearerSeatingBay TineMatAndMayBag PuppyPhotograph',
    'Same seated arrangement. May retrieves SAME flat captioned kennel puppy print from inner tan bag pocket. Dogs adult in foreground; no imagined puppy cutaway. Behaviour recognition has already happened.',
    'May sees Tine lean toward cream Tart and suddenly connects familiar shape to photo.',
    [(27,10,'65mm May recognition and physical print retrieval, reverse Ah Ming','May reads archive names and asks Tart name; Ah Ming confirms Cantonese nickname.'),(29,14,'65mm photo/hands with handlers reverse','May exact Victoria kennel explanation then Ah Ming origin reply, natural Cantonese with English names/place. Keep diegetic archive caption only, no on-screen text overlays.')])
add('s16_c06','AhMing TartOffDuty May TineAdult NearerSeatingBay TineMatAndMayBag PuppyPhotograph',
    'Same bench, print in May hands. Adult dogs calm in open patch, Tart within Ah Ming reach. Tine right-rump heart consistent if visible. One puppy print, no family-tree/microchip inference.',
    'May looks from print markings to adult dogs, turns her explanation toward Ah Ming.',
    [(31,10,'65mm May photo description, focus passes from print to speaker','Exact line describes puppy sleeping pose, no flashback.'),(34,10,'65mm hand on cream back then shared handler medium','Ah Ming feels relaxed dog, realization line; May puts print back into bag, confirmation follows behaviour.')])
add('s16_c07','UncleChan Bo LokAndMother May TineAdult AhMing TartOffDuty NearerSeatingBay UncleChanEffects',
    'Same group bay bench. Chan hat loose in hands, Bo beside seating area, Lok beside mother. Dogs remain nearby without new toy action foreground stealing dialogue.',
    'Bo checks group return preference quietly, Chan watches relaxed dogs.',
    [(37,8,'65mm Chan/Bo two-shot','Exact wish to stay longer, Bo agrees to return together.'),(38,5,'40mm inclusive bench wide','Chan makes room for Lok and mother; they settle, no photo passed around or extra speech.')])
add('s16_c08','AhMing TartOffDuty May TineAdult UncleChan Bo LokAndMother CentreMembers NearerSeatingBay HarbourGeography SqueakyToy',
    'Same sheltered inland bay, harbour visible across main path beyond group. Tart left, Tine right on level paving, single toy between paws; two leads held slack separately. Handlers seated behind within easy touch, removed harness remains on bench.',
    'Tine sits close and leans, Tart makes a fractional shift; both are adult dogs throughout.',
    [(41,7,'50mm low two-shot','Tine follows fraction then waits; Tart considers empty other side but shifts forepaws to open room; Tine folds down.'),(45,9,'65mm intimate settled pair then handlers medium','Tart lowers alongside, shoulders touch, chin across Tine forelegs, toy between paws; two exact quiet lines.'),(49,8,'40mm widening to 28mm inclusive harbour wide, short final fade','Hands rest lightly, one tail movement, relaxed paw contact; music eases into live harbour with people/water still moving. Brief fade at very end; no titles, slogans, subtitles or credits.')])

ROLES = {
 'AhMing':'ONE Hong Kong Chinese blind adult man, exact approved face/clothes; self-directed mobility, eyes natural, recorder/phone only while stopped, headphones only seated home editing.',
 'May':'ONE Hong Kong Chinese visiting-dog handler; approved May face, sage shirt and tan bag. Keep distinct from Bo, mother and other women.',
 'Bo':'ONE centre worker Ah Bo, revised mature broad face, short pixie hair, smaller almond eyes, teal polo. Distinct from May.',
 'LokAndMother':'Revised cute Hong Kong Chinese boy Lok: soft cheeks, neat black fringe, warm almond eyes, mustard clothes; mother: oval face, burgundy rectangular glasses, low bun, blue blouse. One of each only.',
 'StreetAndFerryCast':'CAST LIBRARY, not a group to reproduce. Use only the roles explicitly needed in this shot: grey-haired plum-clothes trolley neighbour; grey-capped deliveryman/car driver; mature long-face auburn-curled rust-jacket pedestrian; navy traveller/teal suitcase; green-top boy with beige father; ferry crew in BLUE sailor-collar work shirt, navy trousers and soft round navy cap, no pilot shirt/epaulettes.',
 'TrainingCast':'CAST LIBRARY: use only needed handler/trainer/volunteer; one identity per depicted role, no lineup. Ranch female handler in ranch scenes, Hong Kong Chinese staff/volunteer in Hong Kong.',
 'CentreMembers':'CAST LIBRARY: slate-polo male colleague and two older members only when needed; never reproduce lineup or duplicate people.',
 'UncleChan':'ONE independent older Hong Kong Chinese widower, exact approved cardigan/face. Ordinary independent movement; emotion through small hands/looks.',
 'AuntieLan':'ONE Hong Kong cafe proprietor, exact approved face/wardrobe, expressive dry Cantonese humour.',
 'TartPuppy':'ONE cream Labrador puppy Tart/蛋撻; no heart patch. Multi-view sheet is ONE dog, never several.',
 'TinePuppy':'ONE chestnut Labrador puppy Tine/阿華田, cream heart patch on anatomical RIGHT rump, never left/mirrored. Multi-view sheet is ONE dog.',
 'GrowingDogs':'AGE reference only: adolescent cream Tart top, adolescent brown Tine bottom; reproduce only named dogs in timeline, basic collars, no visiting bandanna or harness until training state explicitly says so.',
 'TartWorking':'Same ONE cream adult Labrador Tart, brown collar plus brown working guide harness, silver upright handle/brown grip. NO collar lead while working. At Ah Ming LEFT outside leg, full clearance for person.',
 'TartHome':'Same ONE cream adult Tart, brown collar ONLY, no harness/attached lead at home. Separate coiled lead displayed on sheet is a prop diagram, not in every frame.',
 'TartOffDuty':'Same ONE cream adult Tart, brown collar with separate attached BROWN collar lead held by Ah Ming; harness entirely OFF and folded on bench. Never under or between human legs.',
 'TineAdult':'Same ONE chestnut adult Tine, cream anatomical RIGHT-rump heart; orange emblem bandanna and distinct collar, ORANGE lead clipped to collar and held by May in public. No guide harness. Four paws on floor except brief scripted attempted lap gag.',
 'PuppyPhotograph':'ONE physical kennel archive print: exact two puppy pose/bench/toy and small caption Tart and Tine - Victoria, Australia. Diegetic printed object only; no full-screen title card or new genealogy claims.',
 'UncleChanPhotograph':'SEPARATE worn old family photo: younger Chan, wife and yellow village dog Ah Wong, not the kennel puppy print. Wallet-sized, tactile edges.',
 'SqueakyToy':'ONE physical soft two-ended teal/yellow squeaky toy at a time; worn puppy version in ranch, newer home version at Ah Ming flat, May visiting version at centre/harbour. Show only intended object from sheet; no labels/diagrams.',
 'PetFriendlyCar':'Geometry and corrected conventional door hinges only. HK RIGHT-HAND DRIVE. Rear door front/B-pillar hinge opens forward; front door closed during rear loading. Use approved grey-capped man as driver; ignore people pictured on car sheet.',
 'CentralTram':'Environment/vehicle geometry: authentic deep green panels and window surrounds, cream bands/roof, ONE trolley pole; no second pantograph or recolouring.',
 'CentralCrossing':'Environment geometry with exactly ONE pedestrian signal at far-right OPPOSITE kerb. Preserve stripes, curb lines, sight lines; never duplicate signal beside near-side handler.',
 'FerryInterior':'Wooden bench/aisle/window architecture and bright-day lighting only. Ignore prepopulated people/dog identities; bind actual cast separately. All practical lights OFF in afternoon.',
 'FerryExterior':'ONE green-and-cream Hong Kong ferry, same hull/window/rail geometry from multiple views. Daytime all practical lights OFF; moored stationary during boarding/disembarkation.',
 'RecordingEquipment':'PROP LIBRARY only: select recorder/phone/small charcoal speaker/navy bag/headphones as explicitly scripted. No headphones while travelling or field recording, no screens/text floating on frame.',
 'TartHarness':'State/hand mechanics reference only, not a second dog: brown harness fully removed and folded before separate brown lead is clipped for reunion.',
 'HarbourGeography':'GEOGRAPHY reference only: terminal west/back-left, main promenade east/right, nearer seating bay inland, original farther meeting bench east; do not show map labels or split panels.',
 'AhMingFlat':'Geometry/day-night variant only: choose explicitly scripted view; one plain wooden door, oatmeal armchair/mustard cushion, clear dog floor area; no internal security gate.',
 'CentreMorning':'ONE ground-floor TST corner centre: front glass entrance, right-hand windows facing ordinary street. Morning variant only. No duplicate centre opposite street.',
 'CentreAfternoon':'SAME ground-floor TST centre in afternoon, same door/window/chair geometry; use exact identities separately, ignore any depicted people.',
}

COMMON = '''VISUAL STYLE AND PERFORMANCE
Warm expressive feature-quality stylized 3D animation matching the approved original masters: rounded appealing anatomy, tactile fur and cloth, dimensional soft light, warm/cool colour contrast and elastic but weight-bearing comic acting. Original designs throughout; no existing Pixar characters. Hong Kong Chinese human identities and natural Hong Kong Cantonese performances. Normal-speed action with lively causal timing, short reactions and no speed ramps or slow motion. Dog behaviour carries personality without speaking or narration.
REFERENCE RULES
Character turnarounds are single identities, environment plates are geometry/light, prop sheets are objects: render one full cinematic scene, never sheets, panels, labels, comparison grids or annotations. Do not duplicate subjects from multi-view references. Use only roles explicitly present in timed action, not every character in a cast library. Keep faces distinct, especially May/Bo/mother/street woman. Cream Tart has no heart; chestnut Tine has one cream heart on anatomical RIGHT rump. Fur, limbs and physical props retain contact, weight and scale.
'''
LOCKS = '''AUDIO AND FINISH
Generate synchronized native scene audio. Only the exact quoted Cantonese dialogue in the timeline, spoken once by the identified speaker at an unhurried conversational pace within its shot. No added dialogue, dog speech or narrator. Dogs may breathe/pant and make normal paw/collar sounds. Diegetic physical sounds occur at the actual contacts: toy squeaks, trolley wheels, clinks, footsteps, traffic, water or ferry ambience as scripted. Quiet playful acoustic/pizzicato/woodwind score supports comic motion and warm reunion, ducks beneath speech; no triumphant danger music, no lyrics. Honour explicit unscored street and recorded-playback passages. Dialogue/real ambience lead; do not fill brief emotion with a swell. Cuts have clean audio handles, no mid-word cut.
Only diegetic print/signage expressly named in action may appear as readable objects. No author, opening title, end title, subtitles, captions, location/date cards, watermarks, credits or final slogan. Exact duration and full-frame 16:9 480p. End on the specified complete action, maintaining tiny breathing/blinking/ambient life; no padded frozen hold.
'''

rebalance = {'s09_c01':18,'s09_c02':16,'s09_c03':16,'s09_c04':24,'s09_c05':11,
             's10_c02':15,'s10_c05':14,'s12_c03':13,'s12_c04':20,'s15_c01':12,'s15_c03':22}
cursor=0
director=[]
dialogues=[]
for c in P['chapters']:
    spec=PLAN[c['id']]
    if c['id'] in rebalance:c['duration']=rebalance[c['id']]
    c['absolute_start']=cursor;c['absolute_end']=cursor+c['duration'];cursor+=c['duration']
    c['tagged_assets']=['@'+t for t in spec['tags']]
    c['linked_asset_ids']=[A[t]['id'] for t in spec['tags']]
    c['reference_roles']={ '@'+t:ROLES.get(t, A[t]['description']+' Use only the object/location required in timeline; ignore diagrams, duplicate views and annotations.') for t in spec['tags']}
    c['location_map']=spec['location'];c['first_frame']=spec['first']
    c['prompt_library_examples']=['references/prompt-library/shots/scene-02/12_extreme-tight-profile-shot-hands-only.md','references/prompt-library/shots/scene-11/20_close-up-on-the-woman-seated-on-the-edge-of-the-be.md']
    blocks=c['planning_source_blocks'];used=[];shots=[];start=0
    for n,(last,length,camera,direction) in enumerate(spec['beats'],1):
        group=[b for b in blocks if b['source_block_index']<=last and b['source_block_index'] not in used]
        assert group,(c['id'],n)
        used.extend(b['source_block_index'] for b in group)
        action=[]
        for b in group:
            if b['type']=='dialogue':
                action.append('EXACT DIALOGUE — '+b['cue']+': 「'+b['text']+'」')
                dialogues.append((c['source_scene'],b['source_block_index'],b['cue'],b['text']))
            else:action.append(b['text'])
        shots.append({'start':start,'end':start+length,'camera':camera,'action':direction+'\n'+'\n'.join(action),
                      'audio':'Exact quoted dialogue if present; motivated physical sounds and restrained score according to audio rules.',
                      'end_state':direction,'source_block_indices':[b['source_block_index'] for b in group]})
        start+=length
    assert start==c['duration'],(c['id'],start,c['duration'])
    assert used==[b['source_block_index'] for b in blocks],(c['id'],used)
    c['shots']=shots
    timeline='\n\n'.join('Shot '+str(i)+' ('+str(s['start'])+'-'+str(s['end'])+'s): '+('Hard cut to ' if i>1 else '')+s['camera']+'.\n'+s['action'] for i,s in enumerate(shots,1))
    prompt=('SCENE CONTEXT\n'+c['scene_summary']+'. '+c['high_level_idea']+'\n\nOUTPUT SETTINGS\n'+str(c['duration'])+' seconds, 16:9, native 480p, real time, '+str(len(shots))+' timed shots, clean explicit cuts only. The TIMELINE is the complete action order.\n\n'+COMMON+'\nACTIVE REFERENCES\n'+ '\n'.join(t+': '+role for t,role in c['reference_roles'].items())+'\n\nLOCATION MAP\n'+spec['location']+'\n\nFIRST FRAME\n'+spec['first']+'\n\nTIMELINE\n'+timeline+'\n\nPHYSICS AND LIGHT\nSoft motivated daylight consistent with approved location, or warm practical evening light when explicitly at home at night. Feet/paws planted before weight transfer, hands actually grasp handles/buckles/objects, cloth follows bodies. No limb intersections, object teleportation, mirrored markings or lead/harness duplication. Preserve camera axis and entrance/exit directions across cuts. Dialogue close/medium shots keep the speaking face readable.\n\n'+LOCKS)
    c['prompt']=prompt;c['initial_prompt']=prompt;c['prompt_status']='directed; approved assets bound; exact source dialogue preserved'
    c['pacing_reason']+=' Dialogue-heavy beats have been locally rebalanced within scene totals; complete actions and brief reactions govern shot lengths.'
    c['end_state']=shots[-1]['end_state']
    director.append('## '+c['id']+' | '+str(c['absolute_start'])+'–'+str(c['absolute_end'])+' seconds\n\n'+prompt)

assert cursor==1200,cursor
assert len(dialogues)==107,len(dialogues)
assert len(PLAN)==len(P['chapters'])==70
P['detailed_script']='\n\n'.join(director)
P['render_status']='directed_ready_for_seedance'
P['render_intent']['submission_state']='ready_after_per_chapter_render_preflight'
P.setdefault('tool_availability',{})['jobs_submitted']=0
P['director_audit']={'chapters':70,'duration_seconds':1200,'source_dialogue_entries':107,'source_blocks_assigned_once':True,
                     'all_scenes_preserved':True,'dialogue_rewrites':0,'title_credit_blocks_excluded':True,
                     'notes':'Locally redistributed seconds within scenes 9,10,12,15 to protect spoken exchanges and gangway mechanics. All scene totals unchanged. No storyboard or guidance sheet is a generation input.'}
(ROOT/'proposal-directed.json').write_text(json.dumps(P,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'exports/director-script.md').write_text('# Production direction — 20:00 / 480p / 16:9\n\n'+'\n\n'.join(director),encoding='utf-8')
(ROOT/'exports/dialogue-manifest.json').write_text(json.dumps(dialogues,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(P['director_audit'],ensure_ascii=False,indent=2))
