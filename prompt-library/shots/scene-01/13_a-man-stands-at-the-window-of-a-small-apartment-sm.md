# scene-01-13 · A man stands at the window of a small apartment, smoking, his back to the room.

[← Index](../../INDEX.md) · Scene: **SCENE 01**

| | |
|---|---|
| Shot size | Wide |
| Camera | Locked-off |
| Format | Single take · 10s · 21:9 · 1080p |
| Sound | Dialogue · No music |
| Model | seedance_2_5 |
| Characters | char_captain, char_wife |
| Location | loc_apt_cap |
| Props | — |
| Iterations | 12 prompt version(s), 14 generation(s) total |

**Sections:** SCENE CONTEXT → ACTIVE REFERENCES → DEVICE SCALE — CRITICAL → LOCATION MAP → FIRST FRAME AND SPATIAL BLOCKING → FORMAT MODE → OPTICS → CAMERA → HER MICRO-LIFE — 0:00 TO 0:05.6 → ACTION TIMING — 10 SECONDS → DIALOGUE → AUDIO — FOLEY ONLY, ZERO MUSIC, ZERO VOICE, ZERO AMBIENCE → NO MUSIC. THIS IS THE FIRST AND MOST IMPORTANT AUDIO INSTRUCTION. → PHYSICS → LIGHTING → POSITIVE CONSTRAINTS → NEGATIVE — LOCAL LOCKS

## Final prompt (latest version)

_Element IDs replaced with names. Original with IDs: [063_20260906_101357_11d33bce.md](../../../prompts/04_FOOTAGE/SCENE%2001/063_20260906_101357_11d33bce.md)_

````text
SCENE CONTEXT
A man stands at the window of a small apartment, smoking, his back to the room. The woman is seated at the table on the other side of the room, head held high but her eyes cast down, a small orange handheld device lying on the table in front of her. He turns — head and body — to face her. Nothing is said. She leans forward, brings her second arm onto the table and raises her eyes to him. One continuous 10-second take, entirely without dialogue and entirely without music.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. Standing at the window on the LEFT of frame, back to camera, shoulders low, weight settled on one leg, a lit cigarette in his right hand held low at his side. He is a silent character in this shot — he never speaks. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair pulled back into a low loose knot with fine strands escaping at the temple and the nape. White wrap vest with a wide shawl collar over a black t-shirt, dark trousers. A plain thin silver ring on one finger of the right hand. Seated at the round table on the RIGHT of frame, angled roughly three-quarters away from camera. She is a silent character in this shot — she never speaks. She is a living body throughout, never a still figure. 100% matches the reference.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, large window with a dark metal frame and a deep pale sill running the full width of the left and centre of frame, cold grey residential tower block filling the glass, heavy dark red curtain hanging as a vertical band at the right edge of the window, dark leafy plant against the wall behind her, round pale table. Geography, materials and atmosphere only. Nothing in the room beyond what is listed here and the device below.
<<<image_2>>> — THE ONE OBJECT ON THE TABLE. A SMALL flat handheld device, roughly the size of a phone but thicker and more solid — a palm-sized object. Matte burnt-orange plastic body with softly rounded corners and a visible seam running around the middle of the casing. The top face is a flush black glass panel, dark and inert, carrying one small pale line-drawn icon near its centre — a simple stylised animal head, a few thin white strokes, no more. A circular camera lens sits in the middle of the front edge, recessed behind a brushed metal ring, dark glass, catching one small cold specular from the window. A small orange loop lug protrudes at one corner of the top edge. No buttons, no ports, no lettering, no branding, no logo, no readable text anywhere on it. 100% matches the reference.

<<<image_1>>> — MASTER FRAMING AND BLOCKING REFERENCE. This image gives the exact camera position, focal length, shot size, horizon, headroom, and the exact screen positions of both characters, the table, the window, the curtain and the plant. Reproduce it precisely as the first frame of this shot:
— <<<char_captain>>> stands in the LEFT third of frame, seen from behind, body squared to the window plane, head level, looking out. His cigarette is in his right hand, held low and away from his body at hip height, ember live, a thin ribbon of smoke rising past his arm.
— The window wall fills the left and centre of frame, running parallel to the sensor. The dark red curtain hangs as a vertical band at the right edge of the window.
— <<<char_wife>>> sits in the RIGHT third of frame, in clean left profile, back against her chair, head high, eyes lowered. Her right arm extends forward onto the tabletop, forearm flat, palm down, fingers straight and together, silver ring visible.
— The round pale table enters from the bottom of frame and occupies the lower right quadrant, its far edge curving across.
— The plant sits against the wall directly behind her.
— Empty floor and empty table surface separate the two figures across the width of the frame.
Reproduce this framing, these positions, this camera height and this shot size exactly.
DO NOT reproduce the size of the device shown in <<<image_1>>>. In that image the device is rendered too large. Its correct scale is given separately below and by <<<image_1>>>. Everything else in <<<image_1>>> is correct and is to be matched.

<<<image_1>>> — DEVICE DESIGN, SCALE AND POSITION REFERENCE ONLY. Shows <<<image_2>>> lying flat on the scratched pale tabletop, screen face up, its lens edge facing outward across the table. Use for the device's design, ITS SIZE RELATIVE TO THE TABLE, and its orientation. The device's proportion to the tabletop in <<<image_1>>> is the governing reference and must be reproduced exactly. Do NOT inherit its framing, focal length, shallow depth of field or camera height.

DEVICE SCALE — CRITICAL
<<<image_2>>> is SMALL. Its scale relative to the table must match <<<image_1>>>, NOT <<<image_1>>>. In <<<image_1>>> the device occupies roughly one fifth of the visible width of the tabletop — a compact palm-sized object on a large table. The table dwarfs it.
In the wide frame of this shot the device is genuinely small — a modest orange rectangle on the pale tabletop, legible as a saturated colour accent but never prominent. That smallness is correct and intended and must not be compensated for by scaling it up. Do NOT let it read as a tablet, a book, a large box or an object that dominates the tabletop. Its footprint is a small rectangle and its thickness is low — it sits close to the surface, not standing tall on it.
Its position: lying flat on the table between the two figures, screen up, lens edge facing outward, roughly at the centre of the visible tabletop and clear of her hand. It is never touched.

LOCATION MAP
Wide shot of the room, camera position and framing exactly as <<<image_1>>>.
Background: the window wall running parallel to the sensor — flat on, squared, transom horizontal, mullions vertical, no perspective skew, no diagonal convergence. The grey tower block fills the glass, soft, pale, heavily diffused. The pale sill runs straight across beneath it.
LEFT third: <<<char_captain>>> standing at the window, close to the glass, seen from behind, body parallel to the window plane.
CENTRE: the window, the sill, the dark red curtain band at its right edge, empty wall.
RIGHT third: <<<char_wife>>> seated at the round table in clean left profile, the plant on the wall behind her.
LOWER RIGHT: the round pale table entering from the bottom of frame, its far edge curving across. <<<image_2>>> lying flat on it at its correct small scale — the only object on the table.
Camera: tripod, chest height, squared to the window wall, at the exact position given by <<<image_1>>>. Mechanically still for the full duration.

FIRST FRAME AND SPATIAL BLOCKING
First frame: exactly <<<image_1>>>, with <<<image_2>>> reduced to its correct small scale.
<<<char_captain>>> in the left third, seen from behind, dark against the pale window field, cigarette low in his right hand, smoke rising in a thin ribbon.
<<<char_wife>>> in the right third in clean left profile: back against the chair, shoulders level, HEAD HIGH with the neck long and the chin clear of the chest, EYES LOWERED to the tabletop under heavy half-closed lids. Her head is up and her gaze is down — that contradiction is the pose and must be visible. Right forearm flat on the table, palm down, fingers straight and together, silver ring catching the light. Left arm down at her side, below the table line, out of view.
She does not look defeated; she looks composed and withheld. She is already breathing in the first frame — the chest and shoulder line are mid-cycle, not held.
<<<image_2>>> small on the table between them. Nothing else on the table. Nothing on the sill.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:10.

FORMAT MODE
Single continuous wide take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. Tripod — mechanically still, zero movement. Two figures held in one frame, far apart, for the whole shot. No dialogue and no music anywhere in the shot.

OPTICS
Focal length and field of view exactly as <<<image_1>>> — the full geometry of the room legible: the window wall, both figures in their relative positions, her arm on the table, the device. Deep enough focus that both figures, her hands and the device all read clearly; the tower block beyond the glass is soft. Fixed focal length. No focus pull, no rack focus between them, no rack onto the device or onto her hands, no lens breathing, no zoom.

CAMERA
Tripod, head fully clamped, chest height, squared to the window wall.
Zero camera movement for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when he turns and does not react when she leans in.
The window transom, mullions, sill, curtain edge, table position and the device's position on the table remain in identical screen positions from first frame to last, which is the test of whether the lock held.

HER MICRO-LIFE — 0:00 TO 0:05.6
For the first five and a half seconds she does not move her position, but she is never still. The pose holds; the body inside it is alive and working. All of this must be visible at this shot size — it is played in the torso, the shoulders and the throat, where it reads across a room, not in the face.

BREATHING — the primary and most visible sign of life. Her breath is CONTROLLED BUT NOT SUPPRESSED: shallow, a little high in the chest, and irregular in rhythm even though each breath is small. The chest and upper ribcage lift and settle visibly under the white vest with each cycle, and the near shoulder rises and falls a centimetre or two with it. The collar of the vest shifts against her collarbone as the chest expands.
The rhythm is uneven and never metronomic: two ordinary shallow breaths, then a slightly longer and deeper one that lifts the shoulders a fraction more and releases slowly, then a shorter one. One breath around 0:02.5 catches very slightly at the top — a half-second hesitation before it releases — and the shoulders hold marginally high through it. This is a person managing themselves, not a person at rest.

THE THROAT AND JAW — she swallows once, around 0:03.5, the movement travelling visibly up the throat in profile. The muscles under the jaw tighten and release once, independently of the swallow. The jaw carries a faint standing tension at the hinge that comes and goes.

POSTURAL DRIFT — the constant micro-corrections of a seated body holding an upright position. Her weight redistributes fractionally on the seat twice across the five seconds, the torso settling a few millimetres and finding balance again. The spine lengthens marginally and eases. The near shoulder drops a centimetre once and comes back. None of these move her out of the pose; they are the pose staying alive.

THE HEAD — never locked to the neck. It drifts by millimetres with the breathing and makes the involuntary corrections of a real neck holding a head upright. It settles one or two millimetres lower across the five seconds. Every one of these is small enough that the head stays high and the chin stays clear of the chest.

THE EYES — lowered, but not dead. Under the heavy half-closed lids the pupils make small involuntary drifts across the tabletop, settling and resettling on nothing. She blinks three or four times across the five seconds, irregularly spaced — one slow heavy blink, a long gap, a fast one. The lids never open fully and the gaze never rises before its moment.

THE RIGHT HAND — flat on the table and in contact with it throughout, but the hand is not a prop. The fingers register her breathing very slightly, and once across the five seconds the whole hand settles a millimetre as her weight shifts. It does not lift, slide, curl, spread, tap or tense.

HAIR AND CLOTH — the loose strands at her temple and nape hang as weighted mass and shift very slightly with her head movement and with the air of her own breath. The white vest creases and releases at the shoulder and across the ribs with each breath cycle.

AMPLITUDE — every movement above is small. Millimetres and single centimetres. Nothing reads as a gesture, a fidget, a shift of position or a reaction. A viewer should register her as motionless and alive at the same time.
SHE IS NEVER FROZEN. There is no frame in the first five and a half seconds in which nothing about her is moving.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window in the left third, back to the room, body parallel to the glass. Smoke rises past his arm in an unbroken ribbon. One slow shallow breath — the shoulder line barely moves.
She sits at the table in the right third in the <<<image_1>>> posture: head high, eyes down, right hand flat on the table, running the micro-life described above — two shallow breaths lifting the chest and near shoulder, one small postural settle, one slow blink. Her head does not drop and her eyes do not come up.
The width of the frame separates them. Nothing else in the room moves.

0:02–0:03.8 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward her across the frame to screen-right. Roughly 160 to 180 degrees of rotation, unhurried, no snap, no aggression. The cigarette stays in his right hand and swings passively with his arm. When the turn completes he is facing her across the room, his front now toward camera and lit only by the window behind him — his face reading as a darker shape against the bright glass, features soft but legible, not a black cut-out. His eyeline runs across the empty floor toward her, passing over the table and the device.
She does not react to the turn and does not look. But her body registers it without her permission: the breath around 0:02.5 catches slightly at the top and the shoulders hold marginally high through it, and she swallows once at 0:03.5. Nothing else changes. She knows he has turned.

0:03.8–0:05.6 — THE SILENCE. He is facing her and he says nothing. His mouth stays closed and completely still. He does not step toward her, does not gesture, does not raise a hand. His arms stay down.
Her head is still up and her eyes are still down. She does not acknowledge him. The micro-life continues underneath — the breathing settling back toward its earlier rhythm but not quite reaching it, one more blink, one small weight shift on the seat, the jaw tightening and releasing once.
This is the longest still beat in the shot and it is entirely empty of event. Hold it in full. It is not filled with a line, a sound, a music cue, a gesture or a camera move.

0:05.6–0:08.6 — HER RESPONSE. One continuous movement, unhurried, in this order. She begins it on her own — nothing has been said to her and no gesture has been made. It grows out of the micro-life rather than interrupting it: the first thing that moves is the breath deepening slightly, and the lean starts on that breath.
First her weight comes off the chair back: the pelvis stays where it is and the torso hinges forward from the hips, a small lean of ten or fifteen centimetres toward the table. The white vest shifts against her shoulders as she comes forward. Her right forearm stays exactly where it is, flat on the table, and simply takes some of the new weight — the hand does not slide, lift or curl. Her head stays high through the lean; it does not dip.
As she leans, her left arm comes up from her side and settles onto the tabletop: shoulder, elbow, then forearm arriving flat on the surface, the hand finding its own resting place near the right — not mirrored, not symmetrical, not placed with intent. A body opening up and bracing itself because it is about to face someone.
Last, THE EYES COME UP. Because the head is already high, this is not a head lift — it is the gaze rising inside a head that is already raised. The lids open, the pupils travel up off the tabletop and across the empty floor to him, and only then does the head turn a few degrees toward him to follow the eyeline. The eyes lead, the head follows a fraction behind. It is unhurried and unsurprised. She does not startle, does not snap her head up, and does not double-take.
Neither hand ever touches the device.

0:08.6–0:10 — Both hold. He stands facing her across the empty floor, she sits leaning forward with both forearms on the table, looking back at him. Neither of them speaks, then or at any earlier point. A long slow exhale from him; smoke drifts forward into the room and rises through the window light. His shoulder line lowers two or three centimetres.
She keeps breathing, and now that she is leaning on the table the breath reads differently — the movement travels down through the forearms into the tabletop rather than up through the shoulders. Two shallow cycles across this beat, and one blink. She does not settle into stillness at the end.
The shot ends with the two of them looking at each other across the distance, in silence, the device untouched between them, the room still. No music enters at the end.

DIALOGUE
THERE IS NO DIALOGUE IN THIS SHOT. Not one word is spoken by anyone at any point in the 10 seconds.
<<<char_captain>>> does not speak. His lips stay completely closed and completely still for the entire duration, including through the turn, through the silence after it, and through her response. He does not mouth anything, does not part his lips as if about to speak, does not murmur, does not sigh audibly, does not clear his throat.
<<<char_wife>>> does not speak. Her lips stay completely closed and completely still for the entire duration. Her breathing is nasal throughout and never opens the mouth.
No voice-over. No offscreen voices. No whisper. No vocalisation of any kind from either character. No subtitles, no captions, no on-screen text.

AUDIO — FOLEY ONLY, ZERO MUSIC, ZERO VOICE, ZERO AMBIENCE

NO MUSIC. THIS IS THE FIRST AND MOST IMPORTANT AUDIO INSTRUCTION.
There is no music anywhere in this shot, at any point, at any volume, under any name. Not at the head, not at the tail, not under the turn, not under the silence, not under her lean, not under the final hold. Not faint, not distant, not "barely audible", not buried in the mix.
Specifically forbidden, in every form: score, soundtrack, underscore, cue, theme, motif, melody, harmony, chord, sustained tone, drone, pad, hum, swell, riser, sting, hit, impact, boom, braam, whoosh, sub-bass pulse, heartbeat pulse, ticking, tension bed, suspense bed, emotional bed, ambient music, atmospheric music, cinematic music, trailer sound design, orchestral element, string tone, piano note, synth tone, bass note, choir, vocal pad, reverb tail used as a musical texture, and any pitched sustained sound of any kind.
Do not add music to make the silence feel intentional. Do not add music to support the emotion of the scene. Do not add music because the shot is long and quiet. The absence of music IS the intended effect. The scene must play completely dry.

THE SOUNDTRACK CONTAINS EXACTLY ONE ELEMENT: close-mic foley generated by the two bodies. There is no voice track, no music track, and no ambience track. When no foley event is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.

The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry
2. Her breath — shallow, controlled, nasal, irregular in rhythm, present throughout; the slight catch at the top of one inhale around 0:02.5; the deeper intake as she begins to lean at 0:05.6
3. Cloth — the shift of linen shirt fabric as his shoulder line settles; one soft rustle through the turn; the light creasing of her white vest with her breathing, and its drag across her shoulders as she leans forward and her left arm comes up
4. Cigarette — a faint dry crackle of burning tobacco; fingers adjusting on the paper
5. Feet — the muted shift of shoe on floor through the turn, very quiet: no hard heel strike, no scuff, no tail
6. Her arm — one soft, low contact sound as her left forearm settles onto the tabletop, dull and dry, no knock, no thud, no scrape
7. Body — one dry swallow from her at 0:03.5, and one from him, close-mic level only

No spoken word, no vocal sound, no breath shaped like a word, no hum, no sigh with voice in it.
The device makes no sound at all. No chime, no beep, no notification, no vibration, no buzz, no hum, no synthetic voice, no processing tone, no click, no electronic sound of any kind at any point.
No chair sound. Her chair does not creak, scrape, shift or move when she breathes or when she leans forward.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No foley for objects not present.
Despite the wide framing, the mix stays close and dry: no room reverb, no distance perspective, no reflections off the walls, no spatialization.

PHYSICS
NEITHER FIGURE IS EVER FROZEN. Both bodies obey real anatomy, real joint limits, real muscle sequencing and real speed, and both are breathing and micro-adjusting continuously from the first frame to the last. Stillness in this shot means restrained, never motionless. No mannequin pose, no held still-image moment, no waxwork figure, no locked torso on either character.

The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
Standing posture: weight on one leg, pelvis tilted, opposite shoulder marginally lower. Continuous micro-postural sway and the small balance corrections of a man standing in one place. No rocking, no swaying, no pacing.
His face after the turn: still and closed. The jaw does not move, the lips do not part, the mouth does not shape anything. Whatever is happening is happening behind the face. Blinking is irregular and natural.

HER BREATHING: shallow and controlled but genuinely visible at this shot size. The chest and upper ribcage lift and settle under the vest, the near shoulder rising and falling a centimetre or two with each cycle, the vest creasing and releasing at the shoulder and across the ribs. The rhythm is irregular — the intervals between breaths are never equal, the depth varies cycle to cycle, and one inhale catches slightly at the top. Nasal throughout; the mouth never opens. The breathing continues through the turn, through the silence, through the lean and through the final hold — it never stops and never becomes regular.
HER POSTURAL LIFE: continuous small corrections of a seated body — the weight redistributing on the seat, the spine lengthening and easing, the near shoulder dropping and returning, the head drifting by millimetres on the neck. All in millimetres and single centimetres, none of it reading as a gesture.
Her head carriage: the head stays high for the entire 10 seconds. The cervical spine is long and the chin stays clear of the chest at all times. She never drops her head, never tucks her chin, never lets the head sink toward the table. The only deliberate head movement in the shot is a small turn of a few degrees toward him at the very end, following the eyes.
Her gaze: for the first 5.6 seconds the eyes are lowered inside that raised head — lids heavy and half-closed, pupils down toward the tabletop, drifting slightly and unfocused, blinking irregularly. This is a downward gaze, not a downward head. When the eyes come up they travel first, the lids opening as the pupils rise, and the head turns a beat later to follow.
Her lean: a hip hinge, not a slide forward on the seat. It begins on a deeper inhale, growing out of the breathing rather than starting from stillness. The lumbar spine stays long, the shoulders come forward with the ribcage, the head stays up on top of the spine, and the weight transfers from the chair back onto the forearms on the table. Real human speed, with a small settle at the end as the weight finds the table. She does not slump, does not lurch, does not push the chair back, does not stand.
Her right arm and hand: flat on the table, palm down, fingers straight and together, in contact with the surface from the first frame to the last. It registers her breathing very slightly and settles once with a weight shift, but it does not lift, slide, curl, spread, tap or tense at any point — it only takes weight as she leans in.
Her left arm: comes up from below the table with real weight and real joint limits — shoulder, elbow, wrist in sequence. The forearm makes contact with the tabletop and settles, the hand finding its own resting position rather than being placed. Slight asymmetry with the right arm. No slap, no slam, no deliberate placement, no gesture.
Sequencing: breath, then torso, then arm, then eyes, then a small head turn — overlapping rather than separate beats, so it reads as one continuous natural movement and not five actions in a row.
Her hair: the loose strands at temple and nape hang as weighted mass, shifting slightly with her head movement and with her own breath, and settling after the lean.
Cigarette burn: visibly shorter by the end. Ash accumulates and curls but does not fall within the 10 seconds. The ember does not brighten — there is no drag in this shot.
Smoke: real physical smoke, and the only large moving element in a locked frame. Laminar ribbon from the resting cigarette, breaking into slow turbulence above the tip. The turn disturbs the standing smoke column slightly — it bends and re-forms with real inertia. Slow, heavy. Genuine physical volume, never CG particles, never faster than still indoor air allows. Smoke never reaches the table or drifts across the device.
The device: a SMALL solid inert object with real weight, resting flat on the tabletop and in contact with it, at the scale given by <<<image_1>>>. Absolutely motionless for all 10 seconds — it does not slide, tip, rotate, vibrate, wake, glow, flicker or change state. Its screen stays dark and dead throughout, showing only the small pale icon as a printed-looking mark, never as a lit display. Nobody touches it, picks it up, points at it or looks at it. It casts a small soft contact shadow onto the table and its metal lens ring holds one steady cold specular from the window; both stay constant.

LIGHTING
Cold grey-green ambient from the window wall — the primary and only light source, backlighting the whole room. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change when he turns, no change when her eyes come up.
The window is the brightest zone of the frame, a soft luminous field across the left and centre. The tower block behind the glass is pale, flat, heavily diffused, its window grid barely legible.
Standing at the glass on the left, he reads as a dark shape against that field from behind. After the turn his front faces camera and is lit only by the room's weak bounce off the plaster walls — his face is a darker, softer shape, legible but low-contrast. Do not add a fill or a key for the turn: his face must not brighten when he turns around. Do not crush it to pure black either — the face must stay readable, because it is carrying the shot now that there is no line.
Her side of the room, screen-right, falls into the same cold falloff — she is lit by window light raking in from screen-left across the table, sitting a stop or so darker than him. Because her head is up rather than tipped down, that raking light catches the length of her throat, her jawline, her cheekbone and the bridge of her nose in clean profile from the first frame, while her lowered eyes sit in shadow under the brow. The same raking light catches the rise and fall of her chest and shoulder as she breathes, and the shifting creases in the white vest — this is what makes her breathing legible at this shot size. As she leans forward she moves marginally further into the light and the profile sharpens a fraction. Do not add a key or a fill for this — the change comes from her moving through the existing falloff, not from the lighting changing.
That same light picks out the loose strands at her temple, the scratches in the tabletop, the flat of her right hand with its thin silver ring, and, once it arrives, her left forearm.
<<<image_2>>> is lit only by that window light. Its orange body is the single point of saturated colour in an otherwise cold grey-green frame, but it is small and stays low-key and desaturated by the ambient cast — muted burnt orange, not vivid. Its black glass panel reads as a small dark rectangle with a soft sheen. The device emits no light of its own: it is not a practical, it casts no glow onto the table, onto her hands, or into the room, and it never lights her face.
The dark red curtain at the window edge is deeply desaturated — closer to brown-grey than red, low saturation.
Plant, plaster walls and floor: dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass against the pale field.
The cigarette ember is a small warm point only. It does not illuminate his face or hand. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
FRAMING AND BLOCKING MATCH <<<image_1>>> EXACTLY — camera position, focal length, shot size, headroom, and the screen positions of both characters, the table, the window, the curtain and the plant. <<<char_captain>>> in the LEFT third, seen from behind at the window. <<<char_wife>>> in the RIGHT third, seated in clean left profile. The table entering from the bottom right. Do not flip these positions. Do not swap them at any point.
<<<image_2>>> IS SMALL — its size relative to the tabletop matches <<<image_1>>>, NOT <<<image_1>>>. The device in <<<image_1>>> is too large and its scale there is explicitly not to be reproduced. It occupies roughly one fifth of the visible width of the tabletop. It is never enlarged for visibility and never reads as a tablet, a book or a large box.
BOTH CHARACTERS ARE ALIVE IN EVERY FRAME. She is breathing visibly and micro-adjusting continuously from 0:00, not only from 0:05.6 when she moves. There is no frame in which she is a still image.
Her breathing is legible at this shot size: the chest and near shoulder rise and fall, the vest creases and releases, the rhythm is irregular.
THE SHOT HAS NO MUSIC AND NO VOICE. The only sound in the entire 10 seconds is body foley — breath from both of them, cloth, cigarette, one footstep shift, one forearm settling, two swallows. Everything between those events is silence.
NOBODY SPEAKS. Both characters keep their lips closed and still throughout.
Head high and gaze low is the pose. Her head is never tipped down, never bowed, never sunk toward the table at any point. The lowered look comes entirely from the eyes.
She begins her response on her own, unprompted — no line and no gesture triggers it. The turn is the only thing that has happened. The lean grows out of a deeper breath rather than starting from stillness.
When she responds, the eyes rise first inside the already-raised head; the head only turns a few degrees afterward to follow. There is no head lift, because the head is already up.
Her RIGHT forearm is flat on the table with the palm down, fingers straight and together, from the first frame to the last. It never leaves the table.
Her LEFT arm starts down at her side, out of view below the table, and comes up onto the tabletop once only, during her lean. It does not come up earlier, does not come up twice, and does not go back down.
She leans forward from the hips once, during 0:05.6 to 0:08.6, and stays leaning to the end. She does not sit back again.
The device's screen is dark and inert for the entire 10 seconds. It never wakes, never glows, never displays an image, never shows readable text, never blinks, never notifies.
Zero camera movement for the full 10 seconds — framing pixel-identical from first frame to last, including through the turn.
The window wall runs perfectly parallel to the sensor — transom horizontal, mullions vertical, no perspective skew, no diagonal convergence, no dutch.
He begins with his back to camera, standing at the window. He turns once, head and body together, and remains facing her until the end. He never turns back to the window. He never walks toward her. He never touches her, never touches the device, never touches the glass, never opens the window, never draws the curtain, never sits.
She stays seated at the table for all 10 seconds. She does not stand, does not turn her chair, does not reach for the device, does not touch him. She holds nothing.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass or in the device's screen.
Nothing exists in the room that is not listed in <<<loc_apt_cap>>> plus <<<image_2>>>: no second screen, no phone, no monitor, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock, no television. Nothing else on the table. Nothing on the sill. No props invented anywhere in frame.
No visible brand marks, logos or legible lettering anywhere, including on the device.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
The cigarette is in his right hand for the entire shot. No drag in this shot. He does not stub it out, does not put it down, does not tap ash, does not flick it away.
Apart from the single turn and her lean, arm and eye movement, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin, fabric or the device.

NEGATIVE — LOCAL LOCKS
NO OVERSIZED DEVICE. <<<image_2>>> is never scaled up, never enlarged for legibility, never rendered at the size shown in <<<image_1>>>. It stays palm-sized, matching <<<image_1>>>'s proportion to the tabletop.
NO FROZEN FIGURE. She is not a still image, a photograph, a mannequin or a statue at any point, including the first five seconds. No held frame, no motionless body, no suspended breathing, no waxwork stillness, no paused figure waiting for her cue.
No suppressed or invisible breathing. Her breath must be legible in the chest and shoulder, not implied.
No metronomic breathing. No even, mechanical, looping respiratory cycle. No animation loop of any kind on her body.
No fidgeting either: no tapping fingers, no jiggling leg, no touching her hair or face, no adjusting her clothes, no shifting in the chair as a visible action, no looking around the room.
NO MUSIC OF ANY KIND, ANYWHERE, AT ANY VOLUME. No score, no underscore, no cue, no theme, no drone, no pad, no sustained tone, no swell, no riser, no sting, no impact, no pulse, no tension bed, no ambient or atmospheric music, no orchestral or synth element, no piano, no strings, no choir. No music at the head or tail of the shot. No music faded in under the silence. No musical reverb tail as texture.
No ambience, no room tone, no atmosphere bed of any kind.
NO DIALOGUE OF ANY KIND. No line, no word, no whisper, no murmur, no name spoken, no vocalisation, no voice-over, no offscreen voice, no subtitle.
NO MOUTH MOVEMENT. Neither character opens their mouth, parts their lips, mouths silently, or shapes a word at any point. Her breathing is nasal and never opens the mouth. No lip-sync of any kind is generated.
No sound shaped like speech: no voiced sigh, no groan, no throat clearing, no intake that reads as the start of a line.
No gesture substituting for the missing line: he does not beckon, does not point, does not raise a hand, does not tilt his head at her, does not shrug.
No chair creak, no device sound, no exterior sound, no building sound.
No camera movement. No push in on either face. No rack focus between them.
No second person beyond the two characters. No reflection of a third figure in the glass.
No screen light, no glow, no wake, no notification on the device.
No head bow, no chin tuck, no slump, no head lift, no startle, no double-take.
No warm light, no coloured practicals, no lens flare, no rim light.
No CG gloss on skin, fabric, smoke or device. No CG particle smoke.
````

### Generated videos

- 2026-09-06 10:13:57 · [video](https://d8j0ntlcm91z4.cloudfront.net/user_38JDnD2aJxtjnkHGSvDeUpDsT5p/hf_20260906_101357_11d33bce-cb01-40df-bbd7-6408c1249f9f.mp4)

## Earlier versions

Oldest first. Compare against the final to see what the author changed between attempts.

<details><summary>v1 · 2026-08-28 14:06:47 · 1 generation(s) · 023_20260828_140647_f17ca790.md</summary>

````text
```text
SCENE CONTEXT
A man stands at the window of a small apartment, smoking, his back to the room. The woman is seated at the table on the other side of the room, an orange handheld device lying on the table in front of her. He lifts his eyes to the sky, then turns and speaks two words to her. She raises her head to him and brings her second arm up onto the table. One continuous 10-second take.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. Standing at the window on the LEFT of frame, back to camera, shoulders low, weight settled on one leg, a lit cigarette in his right hand. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair loosely pulled back into a low knot with loose strands at the temple. White wrap vest with a wide shawl collar over a black t-shirt, dark trousers. A plain thin silver ring on one finger of the right hand. Seated at the round table on the RIGHT of frame, angled roughly three-quarters away from camera. 100% matches the reference.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, large window with a dark metal frame and a deep pale sill, cold grey residential tower block filling the glass, heavy dark red curtain hanging at one edge of the window, dark leafy plant against the wall, white radiator low under the window, round pale table with two chairs. Geography, materials and atmosphere only. Nothing in the room beyond what is listed here and the device below.
<<<prop_device>>> — THE ONE OBJECT ON THE TABLE. A small flat handheld device, roughly the size of a phone but thicker and more solid. Matte burnt-orange plastic body with softly rounded corners and a visible seam running around the middle of the casing. The top face is a flush black glass panel, dark and inert, carrying one small pale line-drawn icon near its centre — a simple stylised animal head, a few thin white strokes, no more. A circular camera lens sits in the middle of the front edge, recessed behind a brushed metal ring, dark glass, catching one small cold specular from the window. A small orange loop lug protrudes at one corner of the top edge. No buttons, no ports, no lettering, no branding, no logo, no readable text anywhere on it. 100% matches the reference.
<<<image_2>>> — DEVICE POSITION REFERENCE ONLY. Shows <<<prop_device>>> lying flat on the scratched pale tabletop, screen face up, lens edge facing outward across the table, near the centre of the table surface and slightly toward the near edge. Use for the device's design, orientation and position only. Do NOT inherit its framing, focal length, shallow depth of field or camera height — this is a wide room shot, not a tabletop close-up.
<<<image_3>>> — ARM AND HAND POSITION REFERENCE for <<<char_wife>>>'s RIGHT arm. Read from it, and reproduce exactly: her right arm is extended forward from the shoulder and laid along the tabletop, the forearm resting flat on the table surface with the elbow off the near edge and the upper arm relaxed. The right hand is flat, palm down, fingers straight and together, lying fully in contact with the table. The thin silver ring is visible on that hand. The arm is relaxed, not braced, not gripping, not clenched. Use this image for the right arm and hand pose only. Do NOT inherit its framing, its camera height, its lens or its shot size — this is a wide room shot from the far side of the apartment, not a profile medium.
<<<image_1>>> — BLOCKING REFERENCE ONLY. The location with the two character positions marked: the RED marker is <<<char_captain>>>, standing at the window on the LEFT of frame; the YELLOW marker is <<<char_wife>>>, seated at the table on the RIGHT of frame. Use for camera position, room geography and the two standing/seated positions only. The coloured markers are annotations, not objects and not costume — no coloured shape, overlay, line, dot or drawing appears anywhere in the render, and neither character wears red or yellow.

LOCATION MAP
Wide shot of the whole room, seen from the far side of the apartment looking toward the window wall, matching the camera position of <<<image_1>>>.
Background: the window wall, running parallel to the sensor — flat on, squared, transom horizontal, mullions vertical, no perspective skew, no diagonal convergence. The grey tower block fills the glass, soft, pale, heavily diffused. The pale sill runs straight across. The white radiator sits low beneath it. The heavy dark red curtain hangs as a vertical band at one edge of the window.
Midground-LEFT: <<<char_captain>>> standing at the window, close to the glass, seen from behind — his back to camera, his body squared to the window plane, parallel to it.
Midground-RIGHT: the round pale table with two chairs. <<<char_wife>>> seated at it, angled roughly three-quarters away from camera, her right arm laid flat along the table as in <<<image_3>>>, her left arm down at her side and out of view below the table line. On the table, and nothing else on the table, <<<prop_device>>> lies flat — screen up, lens edge facing outward, near the centre of the surface and slightly toward the near edge, clear of her right hand and never touched. It reads as one small hard orange rectangle against the pale scratched tabletop — the only saturated colour in the frame.
Side wall: plaster, the dark leafy plant against it.
Foreground: bare floor and open room. Empty.
Camera: tripod, chest height, standing back from both figures, squared to the window wall. Mechanically still for the full duration.

FIRST FRAME AND SPATIAL BLOCKING
First frame: the whole room readable in one wide frame. The window wall fills the background across the width of the picture. <<<char_captain>>> stands at the window on the LEFT side of frame, seen from behind, his silhouette dark against the pale glass, body parallel to the window plane, head level, looking out. The lit cigarette is in his right hand at his side, ember live, a thin ribbon of smoke rising past his shoulder into the window light. <<<char_wife>>> sits at the table in the RIGHT half of frame, midground, head tipped down, her right arm extended and flat on the table with the palm down exactly as in <<<image_3>>>, her left arm hanging at her side out of frame below the table. <<<prop_device>>> lies flat on the table, small in frame but immediately legible as a hard orange shape against the pale wood. The two figures are separated by several metres of empty floor. Curtain band at the window edge; plant against the wall; radiator low under the sill. Nothing else on the table, nothing on the sill.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:10.

FORMAT MODE
Single continuous wide take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. Tripod — mechanically still, zero movement. Two figures held in one frame, far apart, for the whole shot.

OPTICS
Wide room shot, roughly 55° diagonal field of view — the full geometry of the room legible: floor, walls, the window wall, both figures in their relative positions, her arms on the table, the device. Deep enough focus that both figures, her hands and the device all read clearly; the tower block beyond the glass is soft. Fixed focal length. No focus pull, no rack focus between them, no rack onto the device or onto her hands, no lens breathing, no zoom.

CAMERA
Tripod, head fully clamped, chest height, squared to the window wall.
Zero camera movement for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when he looks up, does not react when he turns, and does not react when he speaks.
The window transom, mullions, sill, curtain edge, table position and the device's position on the table remain in identical screen positions from first frame to last, which is the test of whether the lock held.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window on the left, back to the room, body parallel to the glass. Smoke rises past his shoulder in an unbroken ribbon. One slow shallow breath — the shoulder line barely moves. She sits at the table on the right, head tipped down, right hand flat on the table, motionless apart from her breath. Several metres of empty floor between them. Nothing else in the room moves.
0:02–0:03.5 — HE LOOKS UP. Without turning his body, he tips his head back and lifts his eyes to the sky above the tower block. The movement is slow and small — the head rolling back 15 to 20 degrees on the neck, the chin lifting, the nape shortening, the shoulder line staying where it is. Read entirely from behind: the back of the skull tilts back, the hair shifts against the collar. He holds it there, looking up at nothing.
0:03.5–0:04.2 — The head comes back down to level. A short pause.
0:04.2–0:05.8 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward her across the frame to screen-right. Roughly 160 to 180 degrees of rotation, unhurried, no snap, no aggression. The cigarette stays in his right hand and swings passively with his arm. When the turn completes he is facing her across the room, his front now toward camera and lit only by the window behind him — his face reading as a darker shape against the bright glass, features soft but legible, not a black cut-out. His eyeline runs across the empty floor toward her.
0:05.8–0:07 — THE LINE. Facing her, he says two words: "Look at me." Quiet, level, flat — not raised, not pleading, not an order. Mouth movement is clear and readable at this wide scale, matching the phonemes and the short length of the line, with no exaggeration. He does not step toward her. He does not gesture. His arms stay down.
0:07–0:09 — HER RESPONSE. She raises her head and her eyes to him. The head comes up off the chest first, the chin lifting, the neck lengthening, the face turning slightly toward him across the room until her eyeline meets his. It is unhurried and unsurprised.
As she lifts her head she changes position: her left arm comes up from her side and settles onto the tabletop beside the right. The forearm arrives flat on the surface, the hand coming to rest naturally near the right hand — not mirrored, not symmetrical, not placed with intent, just a body settling into a more open, more braced posture as it turns to face someone. Her right arm stays exactly where it was, flat, palm down, unmoved. The device is not touched by either hand.
0:09–0:10 — Both hold. He stands facing her across the empty floor, she sits looking back at him, both forearms now on the table. Neither speaks again. A long slow exhale from him; smoke drifts forward into the room and rises through the window light. His shoulder line lowers two or three centimetres. The shot ends with the two of them looking at each other across the distance, the device untouched between them.

DIALOGUE
Exactly one spoken line in the whole shot, spoken by <<<char_captain>>>, at 0:05.8: "Look at me."
Male, 40s, quiet, low, level. Delivered plainly, without emphasis or emotional colour, at conversational volume across a room. Two words and nothing more.
No other words at any point. No ad-libs, no muttering, no filler, no breath vocalisations, no repeat of the line. <<<char_wife>>> says nothing at all and her lips stay completely still for the entire 10 seconds. No voice-over. No offscreen voices. No subtitles, no captions.
His lips are completely still except during the line itself.

AUDIO — VOICE AND FOLEY ONLY, ZERO AMBIENCE
The soundtrack contains exactly two elements and nothing else: his single line, and close-mic foley generated by the two bodies. There is no third layer. There is no bed underneath. When no foley event and no voice is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.
The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry, ducked out under the line
2. Cloth — the shift of linen shirt fabric as his shoulder line settles; one soft rustle through the turn; the light drag of her white vest as her left arm comes up
3. Cigarette — a faint dry crackle of burning tobacco; fingers adjusting on the paper
4. Feet — the muted shift of shoe on floor through the turn, very quiet: no hard heel strike, no scuff, no tail
5. Her arm — one soft, low contact sound as her left forearm settles onto the tabletop, dull and dry, no knock, no thud, no scrape
6. Body — a single dry swallow, close-mic level only
7. The spoken line "Look at me."
The device makes no sound at all. No chime, no beep, no notification, no vibration, no buzz, no hum, no synthetic voice, no click, no electronic sound of any kind at any point.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No music, score, drone, pad, tension bed, sting, swell, riser, whoosh, sub-bass hit or reverb tail used as texture — nothing under the look up, nothing under the turn, nothing under the line, nothing at the head or tail of the shot. No foley for objects not present. No chair movement.
Despite the wide framing, the mix stays close and dry: no room reverb, no distance perspective on the voice, no reflections off the walls, no spatialization.

PHYSICS
Looking up: the head rolls back on the neck alone. The shoulders, hips and feet do not move. The chin lifts, the throat opens, the nape shortens. It is slow and small, not a throwback, not a stretch, not a sigh performance.
The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
Standing posture: weight on one leg, pelvis tilted, opposite shoulder marginally lower. No rocking, no swaying, no pacing.
Her head lift: the movement comes from the neck and upper spine, the chin rising as the eyes come up, the shoulders staying settled. Real cervical anatomy, no snap, no jerk, no double take.
Her left arm: it comes up from below the table with real weight and real joint limits — shoulder, elbow, wrist in sequence. The forearm makes contact with the tabletop and settles, the hand finding its own resting position rather than being placed. Slight asymmetry with the right arm. No slap, no slam, no deliberate placement, no gesture. Once settled it stays still.
Her right arm and hand: absolutely unmoved for the full 10 seconds. Flat on the table, palm down, fingers straight and together, exactly as in <<<image_3>>>, from the first frame to the last. It does not lift, slide, curl, spread or tense at any point.
Cigarette burn: visibly shorter by the end. Ash accumulates and curls but does not fall within the 10 seconds. The ember does not brighten — there is no drag in this shot.
Smoke: real physical smoke, and the only large moving element in a locked frame. Laminar ribbon from the resting cigarette, breaking into slow turbulence above the tip. The turn disturbs the standing smoke column slightly — it bends and re-forms with real inertia. Slow, heavy. Genuine physical volume, never CG particles, never faster than still indoor air allows. Smoke never reaches the table or drifts across the device.
The device: a solid inert object with real weight, resting flat on the tabletop and in contact with it. Absolutely motionless for all 10 seconds — it does not slide, tip, rotate, vibrate, wake, glow, flicker or change state. Its screen stays dark and dead throughout, showing only the small pale icon as a printed-looking mark, never as a lit display. Nobody touches it, picks it up, points at it or looks at it. It casts a small soft contact shadow onto the table and its metal lens ring holds one steady cold specular from the window; both stay constant.

LIGHTING
Cold grey-green ambient from the window wall — the primary and only light source, backlighting the whole room. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change when he looks up, no change when he turns, no change when she lifts her head.
The window is the brightest zone of the frame, a soft luminous field across the background. The tower block behind the glass is pale, flat, heavily diffused, its window grid barely legible.
Standing at the glass on the left, he reads as a dark shape against that field from behind. After the turn his front faces camera and is lit only by the room's weak bounce off the plaster walls — his face is a darker, softer shape, legible but low-contrast. Do not add a fill or a key for the turn: his face must not brighten when he turns around. Do not crush it to pure black either — the mouth must stay readable for the line.
Her side of the room, screen-right, falls into the same cold falloff — she is lit by window light raking in from screen-left across the table, sitting a stop or so darker than him. When she lifts her head that raking light catches the bridge of her nose, her cheekbone and her brow as a thin cold edge, the far side of her face staying in shadow. That same light picks out the scratches in the tabletop, the flat of her right hand and, once it arrives, her left forearm.
<<<prop_device>>> is lit only by that window light. Its orange body is the single point of saturated colour in an otherwise cold grey-green frame, but it stays low-key and desaturated by the ambient cast — muted burnt orange, not vivid. Its black glass panel reads as a dark rectangle with a soft sheen. The device emits no light of its own: it is not a practical, it casts no glow onto the table, onto her hands, or into the room, and it never lights her face.
The dark red curtain at the window edge is deeply desaturated — closer to brown-grey than red, low saturation.
Plant, plaster walls, radiator and floor: dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass across the pale field.
The cigarette ember is a small warm point only. It does not illuminate his face or hand. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
Blocking follows <<<image_1>>>: <<<char_captain>>> standing at the window on the LEFT of frame, <<<char_wife>>> seated at the table on the RIGHT of frame. Do not flip these positions. Do not swap them at any point.
Her RIGHT arm and hand follow <<<image_3>>> exactly — forearm flat along the table, palm down, fingers straight and together, ring visible — and stay in that position, unmoved, for the entire 10 seconds.
Her LEFT arm starts down at her side, out of view below the table, and comes up onto the tabletop once only, during 0:07–0:09, settling naturally beside the right. It does not come up earlier, does not come up twice, and does not go back down.
<<<image_3>>> supplies the arm and hand pose only. Its framing, camera height, lens and shot size must not be reproduced. This shot stays wide.
<<<prop_device>>> sits on the table in the position given by <<<image_2>>>. It is the only object on the table and is never touched by either character.
The device's screen is dark and inert for the entire 10 seconds. It never wakes, never glows, never displays an image, never shows readable text, never blinks, never notifies.
The coloured markers in the blocking reference are annotations only. No red or yellow shape, dot, line, arrow, circle or overlay appears anywhere in the render. Neither character wears red or yellow — costume comes from the character references: he in grey linen over dark, she in a white wrap vest over black. The orange of the device is the only orange in the frame.
Exactly one line of dialogue, "Look at me.", spoken once by <<<char_captain>>> after he has completed the turn. No other speech from anyone.
Wide shot of the room, tripod, chest height, squared to the window wall — the full geometry of the room and the distance between the two figures legible in one frame for the entire shot.
Zero camera movement for the full 10 seconds — framing pixel-identical from first frame to last, including through the turn.
The window wall runs perfectly parallel to the sensor — transom horizontal, mullions vertical, no perspective skew, no diagonal convergence, no dutch.
He begins with his back to camera, standing at the window, body parallel to the glass. He looks up once, comes back to level, turns once — head and body together — and remains facing her until the end. He never turns back to the window. He never walks toward her. He never touches her, never touches the device, never touches the glass, never opens the window, never draws the curtain, never sits.
She stays seated at the table for all 10 seconds. She does not stand, does not turn her chair, does not answer, does not reach for the device, does not touch him. She holds nothing. She lifts her head once and keeps her eyes on him to the end.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass or in the device's screen.
Nothing exists in the room that is not listed in <<<loc_apt_cap>>> plus <<<prop_device>>>: no second screen, no phone, no monitor, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock, no television. Nothing else on the table. Nothing on the sill. No props invented anywhere in frame.
No visible brand marks, logos or legible lettering anywhere, including on the device.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
The cigarette is in his right hand for the entire shot. No drag in this shot. He does not stub it out, does not put it down, does not tap ash, does not flick it away.
Apart from the look up, the single turn and her head lift and left arm, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin, fabric or the device.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_140647_f17ca790-f5d3-41b2-a87c-1c898ce7007f.mp4)

</details>

<details><summary>v2 · 2026-08-28 14:19:29 · 1 generation(s) · 024_20260828_141929_2088e652.md</summary>

````text
SCENE CONTEXT
A man stands at the window of a small apartment, smoking, his back to the room. The woman is seated at the table on the other side of the room, an orange handheld device lying on the table in front of her. He speaks once without turning. Then he turns — head and body — to face her, and speaks again.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. Standing at the window on the LEFT of frame, back to camera, shoulders low, weight settled on one leg, a lit cigarette in his right hand. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair loosely pulled back. White wrap vest over black t-shirt, dark trousers. Seated at the round table on the RIGHT of frame, angled roughly three-quarters away from camera, her head tipped down. She holds nothing. Her hands rest still on the table. She does not speak. 100% matches the reference.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, large window with a dark metal frame and a deep pale sill, cold grey residential tower block filling the glass, heavy dark red curtain hanging at one edge of the window, dark leafy plant against the wall, white radiator low under the window, round pale table with two chairs. Geography, materials and atmosphere only. Nothing in the room beyond what is listed here and the device below.
<<<prop_device>>> — THE ONE OBJECT ON THE TABLE. A small flat handheld device, roughly the size of a phone but thicker and more solid. Matte burnt-orange plastic body with softly rounded corners and a visible seam running around the middle of the casing. The top face is a flush black glass panel, dark and inert, carrying one small pale line-drawn icon near its centre — a simple stylised animal head, a few thin white strokes, no more. A circular camera lens sits in the middle of the front edge, recessed behind a brushed metal ring, dark glass, catching one small cold specular from the window. A small orange loop lug protrudes at one corner of the top edge. No buttons, no ports, no lettering, no branding, no logo, no readable text anywhere on it. 100% matches the reference.
<<<image_1>>> — DEVICE POSITION REFERENCE ONLY. Shows <<<prop_device>>> lying flat on the scratched pale tabletop, screen face up, its lens edge facing outward across the table, roughly at the centre of the table surface and slightly toward the near edge. Use this image for the device's design, its orientation and its position on the table only. Do NOT inherit its framing, its focal length, its shallow depth of field, or its camera height — this is a wide room shot from the far side of the apartment, not a tabletop close-up. In the final shot the device is a small object in the midground on the right, not a hero close-up.
 — BLOCKING REFERENCE ONLY. A photograph of the location with the two character positions marked on it: the RED marker is <<<char_captain>>>, standing at the window on the LEFT of frame; the YELLOW marker is <<<char_wife>>>, seated at the table on the RIGHT of frame. Use this image for camera position, room geography and the two standing/seated positions only. The coloured markers are annotations, not objects and not costume — no coloured shape, overlay, line, dot or drawing appears anywhere in the render, and neither character wears red or yellow. Costume comes from the character references.
AUDIO REFERENCE — ElevenLabs_2026-08-26T14_11_50__s0_v3: the supplied voiceover recording of <<<char_captain>>>'s dialogue. This file is the sole source of the spoken voice. Do not synthesize, replace, re-time, pitch-shift, or regenerate the voice.

LOCATION MAP
Wide shot of the whole room, seen from the far side of the apartment looking toward the window wall, matching the camera position of .
Background: the window wall, running parallel to the sensor — flat on, squared, transom horizontal, mullions vertical, no perspective skew, no diagonal convergence. The grey tower block fills the glass, soft, pale, heavily diffused. The pale sill runs straight across. The white radiator sits low beneath it. The heavy dark red curtain hangs as a vertical band at one edge of the window.
Midground-LEFT: <<<char_captain>>> standing at the window, close to the glass, seen from behind — his back to camera, his body squared to the window plane, parallel to it.
Midground-RIGHT: the round pale table with two chairs. <<<char_wife>>> seated at it, angled roughly three-quarters away from camera, head down, hands resting still on the table. On the table, and the only thing on the table, <<<prop_device>>> lies flat — screen up, lens edge facing outward, near the centre of the surface and slightly toward the near edge, within reach of her resting hands but never touched. It reads as one small hard orange rectangle against the pale scratched tabletop — the only saturated colour in the frame.
Side wall: plaster, the dark leafy plant against it.
Foreground: bare floor and open room. Empty.
Camera: tripod, chest height, standing back from both figures, squared to the window wall. Mechanically still for the full duration.

FIRST FRAME AND SPATIAL BLOCKING
First frame: the whole room readable in one wide frame. The window wall fills the background across the width of the picture. <<<char_captain>>> stands at the window on the LEFT side of frame, seen from behind, his silhouette dark against the pale glass, body parallel to the window plane. The lit cigarette is in his right hand at his side, ember live, a thin ribbon of smoke rising past his shoulder into the window light. <<<char_wife>>> sits at the table in the RIGHT half of frame, midground, head tipped down, hands still on the table. <<<prop_device>>> lies flat on the table in front of her, small in frame at this wide scale but immediately legible as a hard orange shape against the pale wood. The two are separated by several metres of empty floor. Curtain band at the window edge; plant against the wall; radiator low under the sill. Nothing else on the table, nothing on the sill.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:20.

FORMAT MODE
Single continuous wide take. 20 seconds. No cuts. Real-time motion, no slow motion. Tripod — mechanically still, zero movement. Dialogue driven by the supplied audio file, not generated. The soundtrack is voice and close foley only — no ambience whatsoever. Two figures held in one frame, far apart, for the whole shot.

OPTICS
Wide room shot, roughly 55° diagonal field of view — the full geometry of the room legible: floor, walls, the window wall, both figures in their relative positions, the device on the table. Deep enough focus that both figures and the device read clearly; the tower block beyond the glass is soft. Fixed focal length. No focus pull, no rack focus between them, no rack onto the device, no lens breathing, no zoom.

CAMERA
Single continuous take, 20 seconds. Tripod, head fully clamped, chest height, squared to the window wall.
Zero camera movement for the full duration: no push, no pull, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when he speaks and does not react when he turns.
The window transom, mullions, sill, curtain edge, table position and the device's position on the table remain in identical screen positions from first frame to last, which is the test of whether the lock held.

ACTION TIMING
0:00–0:03.5 He stands at the window on the left, back to the room, body parallel to the glass, looking out. Smoke rises past his shoulder in an unbroken ribbon. Two slow shallow breaths — the shoulder line barely moves. She sits at the table on the right, head down, motionless apart from her breath, the orange device lying inert on the table in front of her. Several metres of empty floor between them. Nothing else in the room moves.
0:03.5–0:04.6 His right hand lifts the cigarette to his mouth: the forearm rises, the elbow staying close to the body, the movement visible from behind as the shoulder and upper arm rotate. He does not turn.
0:04.6–0:06.0 First drag, read from behind: the shoulder line lifts fractionally on the intake, the head stays level, a small brightening of the ember visible at the edge of his silhouette. She does not move. The device does not move.
0:06.0–0:06.5 The hand lowers back to his side, cigarette between the fingers. He holds the smoke.
0:06.5–0:08.0 He exhales. Two streams of smoke appear past both sides of his head, spreading and rising brightly against the pale window. The shoulder line settles 2–3cm as the breath releases.
0:08.0–0:09.6 Stillness. At 0:09.2 a small weight shift — the standing hip transfers to the other leg, the shoulder line rocking slightly and settling. Nothing else in the room moves.
0:09.6 First line. He speaks the first line of ElevenLabs_2026-08-26T14_11_50__s0_v3 — "Honey, it takes longer when there's room." He says it to the window, back still turned, body unmoved. From this angle no mouth is visible; the line reads as coming from a man facing away. She does not react. The device does not react — it does not wake, light up, blink or change.
Between the two lines Long silence, exactly as recorded in the supplied file. He waits. She does not answer, does not move, does not lift her head, does not touch the device. He stays facing the glass. No filler movement anywhere in the frame.
The turn, 1.2–1.5 seconds before the second line He turns — head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward her across the frame to screen-right. Roughly 160–180° of rotation, unhurried, no snap, no aggression. The cigarette stays in his hand and swings with his arm. When the turn completes he is facing her across the room, his front now toward camera and lit only by the window behind him — his face reading as a darker shape against the bright glass, features soft but legible, not a black cut-out. His eyeline runs across the empty floor toward her on the right, passing over the table and the device.
Second line He speaks the second line of the supplied recording — "Look at me." Now facing her. Lip movement is driven by and locked to the supplied recording, matching its exact phonemes, phrasing, stress and duration, readable at this wide scale as clear mouth movement, no exaggeration. He does not step toward her. He does not raise his voice. His arms stay down.
After the last word, 3–4 seconds Nothing. He stands facing her across the empty floor. She does not lift her head. Neither of them moves. The device lies untouched between them on the table. The distance between them, left to right across the frame, is the whole content of the shot.
Final block, to 0:20 A long slow exhale; smoke drifts forward from him into the room and rises through the window light. His shoulder line lowers 2–3cm. His head lowers 2–3cm — but he keeps facing her. The cigarette hand hangs lower against his side. Ash holds on the cigarette, curling. The shot ends with him turned toward her, her head still down, the device still on the table, the room still.

AUDIO — VOICE AND FOLEY ONLY, ZERO AMBIENCE
Dialogue source: ElevenLabs_2026-08-26T14_11_50__s0_v3. This file supplies the entire spoken performance — both lines and the silence between them. Use it as-is. Do not generate a new voice. Do not re-perform, re-time, stretch, compress, pitch-shift, add reverb, or alter the delivery. Do not add breaths, sighs, or vocalizations that are not in the file.
Lip-sync: for the second line, mouth movement matches the supplied audio frame-accurately. During the first line his back is to camera and no lip movement is visible. Lips are completely still whenever the file is silent.
The soundtrack contains exactly two elements and nothing else: the supplied voice file, and close-mic foley generated by his body. There is no third layer. There is no bed underneath. When no foley event and no voice is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or "made natural."
The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 20 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry, ducked out wherever the dialogue file is playing
2. Cloth — the shift of linen shirt fabric as his shoulder line settles after each exhale; one soft rustle of fabric through the turn; the rub of sleeve against his torso as the forearm lifts and lowers
3. Cigarette — fingers adjusting on the paper; a faint dry crackle of burning tobacco on the drag; the soft contact of lips on the filter
4. Feet — the muted shift of shoe on floor at the weight change, and one small step through the turn, both very quiet: no hard heel strike, no scuff, no tail
5. Body — a single dry swallow, close-mic level only
6. The supplied voice file
The device makes no sound at all. No chime, no beep, no notification, no vibration, no buzz, no hum, no synthetic voice, no processing tone, no click, no electronic sound of any kind at any point.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No music, score, drone, pad, tension bed, sting, swell, riser, whoosh, sub-bass hit or reverb tail used as texture — nothing under the turn, nothing under either line, nothing at the head or tail of the shot. No foley for objects not present.
Despite the wide framing, the mix stays close and dry: no room reverb, no distance perspective on the voice, no reflections off the walls, no spatialization.
<<<char_wife>>> makes no sound at all — no breath, no sigh, no sniff, no cry, no reply, no chair movement, no cloth. No offscreen voices of any kind. No subtitles, no captions.

PHYSICS
The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
Standing posture: weight on one leg, pelvis tilted, opposite shoulder marginally lower. One weight transfer before the turn. No rocking, no swaying, no pacing.
Cigarette burn: visibly shorter by the end. The ember brightens as airflow increases during the drag, then dims within 0.5 seconds. Paper and ash edge consumed by 3–4mm. Ash accumulates and curls but does not fall within the 20 seconds.
Smoke: real physical smoke, and the only large moving element in a locked frame. Laminar ribbon from the resting cigarette, breaking into slow turbulence above the tip. Exhaled smoke falls, spreads horizontally, then rises. The turn disturbs the standing smoke column slightly — it bends and re-forms with real inertia. Slow, heavy. Genuine physical volume, never CG particles, never faster than still indoor air allows. Smoke never reaches the table or drifts across the device.
The device: a solid inert object with real weight, resting flat on the tabletop and in contact with it. It is absolutely motionless for all 20 seconds — it does not slide, tip, rotate, vibrate, wake, glow, flicker or change state. Its screen stays dark and dead throughout, showing only the small pale icon as a printed-looking mark, never as a lit display. Nobody touches it, picks it up, points at it or looks at it. It casts a small soft contact shadow onto the table and its metal lens ring holds one steady cold specular highlight from the window; both stay constant.
Her stillness: breathing only, for the full 20 seconds. Shoulder rise and fall of a few millimetres. She does not turn, does not lift her head, does not gesture, does not stand, does not reach for the device, does not react to either line or to the turn.
Speech articulation: driven by the audio file only. No head emphasis, no arm gesture synchronized to speech.

LIGHTING
Cold grey-green ambient from the window wall — the primary and only light source, backlighting the whole room. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 20 seconds — no change in level, colour or direction, and no change when he turns.
The window is the brightest zone of the frame, a soft luminous field across the background. The tower block behind the glass is pale, flat, heavily diffused, its window grid barely legible.
Standing at the glass on the left, he reads as a dark shape against that field from behind. After the turn his front faces camera and is lit only by the room's weak bounce off the plaster walls — his face is a darker, softer shape, legible but low-contrast. Do not add a fill or a key for the turn: his face must not brighten when he turns around. Do not crush it to pure black either — the mouth must stay readable for the line.
Her side of the room, screen-right, falls into the same cold falloff — she is lit by window light raking across the table, sitting a stop or so darker than him. That same raking light picks out the scratches in the tabletop and lands on the top and near face of the device.
<<<prop_device>>> is lit only by that window light. Its orange body is the single point of saturated colour in an otherwise cold grey-green frame, but it stays low-key and desaturated by the ambient cast — muted burnt orange, not vivid. Its black glass panel reads as a dark rectangle with a soft sheen. The lens ring holds one small cold specular. The device emits no light of its own: it is not a practical, it casts no glow onto the table, onto her hands, or into the room, and it never lights her face.
The dark red curtain at the window edge is deeply desaturated — closer to brown-grey than red, low saturation.
Plant, plaster walls, radiator and floor: dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass across the pale field.
The cigarette ember is a small warm point only. It does not illuminate his face or hand. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
Blocking follows : <<<char_captain>>> standing at the window on the LEFT of frame, <<<char_wife>>> seated at the table on the RIGHT of frame. Do not flip these positions. Do not swap them at any point in the shot.
<<<prop_device>>> sits on the table in the position given by <<<image_1>>> — flat, screen up, lens edge outward, near the centre of the table and slightly toward the near edge. It is the only object on the table.
<<<image_1>>> supplies the device's design and placement only. Its close-up framing, low camera height and shallow depth of field must not be reproduced. This shot stays wide, and the device stays small in the midground.
The coloured markers in the blocking reference are annotations only. No red or yellow shape, dot, line, arrow, circle or overlay appears anywhere in the render. Neither character wears red or yellow — costume comes from the character references: he in grey linen over dark, she in a white wrap vest over black. The orange of the device is the only orange in the frame and is never mistaken for a marker.
The device's screen is dark and inert for the entire 20 seconds. It never wakes, never glows, never displays an image, never shows readable text, never blinks, never notifies. The only marking on it is the small pale line-drawn animal icon, which is printed, not lit.
The soundtrack is voice plus close foley and nothing else. Zero ambience, zero room tone, zero exterior sound, zero music, zero room reverb, zero device sound. Silence between events is absolute digital silence.
Wide shot of the room, tripod, chest height, squared to the window wall — the full geometry of the room and the distance between the two figures legible in one frame for the entire shot.
Zero camera movement for the full 20 seconds — framing pixel-identical from first frame to last, including through the turn.
The window wall runs perfectly parallel to the sensor — transom horizontal, mullions vertical, no perspective skew, no diagonal convergence, no dutch.
He begins with his back to camera, standing at the window, body parallel to the glass, and stays that way through the first line and the entire silence. He turns only once, head and body together, immediately before the second line, and remains facing her until the end. He never turns back to the window. He never walks toward her. He never touches her, never touches the device, never touches the glass, never opens the window, never draws the curtain, never sits.
She stays seated at the table with her head down for all 20 seconds. She does not turn, does not lift her head, does not stand, does not answer, does not react to the turn, does not touch or look at the device. She holds nothing.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass or in the device's screen.
Nothing exists in the room that is not listed in <<<loc_apt_cap>>> plus <<<prop_device>>>: no second screen, no phone, no monitor, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock, no television. Nothing else on the table. Nothing on the sill. No props invented anywhere in frame.
No visible brand marks, logos or legible lettering anywhere, including on the device.
Single continuous take, exactly 20 seconds, no cuts, real-time motion.
Dialogue comes only from ElevenLabs_2026-08-26T14_11_50__s0_v3. No generated voice, no added words, no ad-libs, no muttering in the silences, no reply from her.
Lip movement is locked to the supplied audio for the second line and completely still whenever that audio is silent.
The cigarette is in his right hand for the entire shot. Exactly one drag, at the scripted moment, never during the dialogue and never during the turn. He does not stub it out, does not put it down, does not tap ash, does not flick it away.
Apart from the single turn and one weight shift, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin, fabric or the device.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_141929_2088e652-3c94-4562-a531-7bf0006befc5.mp4)

</details>

<details><summary>v3 · 2026-08-28 14:33:11 · 2 generation(s) · 025_20260828_143311_e01642db.md</summary>

````text
SCENE CONTEXT
A man stands at the window of a small apartment, smoking, his back to the room. The woman is seated at the table on the other side of the room, an orange handheld device lying on the table in front of her. He turns — head and body — to face her, and says two words. She leans forward, brings her second arm onto the table and raises her eyes to him. One continuous 10-second take.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. Standing at the window on the LEFT of frame, back to camera, shoulders low, weight settled on one leg, a lit cigarette in his right hand. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair loosely pulled back. White wrap vest over black t-shirt, dark trousers. Seated at the round table on the RIGHT of frame, angled roughly three-quarters away from camera. 100% matches the reference.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, large window with a dark metal frame and a deep pale sill, cold grey residential tower block filling the glass, heavy dark red curtain hanging at one edge of the window, dark leafy plant against the wall, white radiator low under the window, round pale table with two chairs. Geography, materials and atmosphere only. Nothing in the room beyond what is listed here and the device below.
<<<prop_device>>> — THE ONE OBJECT ON THE TABLE. A small flat handheld device, roughly the size of a phone but thicker and more solid. Matte burnt-orange plastic body with softly rounded corners and a visible seam running around the middle of the casing. The top face is a flush black glass panel, dark and inert, carrying one small pale line-drawn icon near its centre — a simple stylised animal head, a few thin white strokes, no more. A circular camera lens sits in the middle of the front edge, recessed behind a brushed metal ring, dark glass, catching one small cold specular from the window. A small orange loop lug protrudes at one corner of the top edge. No buttons, no ports, no lettering, no branding, no logo, no readable text anywhere on it. 100% matches the reference.
<<<image_1>>> — DEVICE POSITION REFERENCE ONLY. Shows <<<prop_device>>> lying flat on the scratched pale tabletop, screen face up, its lens edge facing outward across the table, roughly at the centre of the table surface and slightly toward the near edge. Use for the device's design, orientation and position on the table only. Do NOT inherit its framing, focal length, shallow depth of field or camera height — this is a wide room shot from the far side of the apartment, not a tabletop close-up.
<<<image_1>>> — BLOCKING REFERENCE ONLY. A photograph of the location with the two character positions marked on it: the RED marker is <<<char_captain>>>, standing at the window on the LEFT of frame; the YELLOW marker is <<<char_wife>>>, seated at the table on the RIGHT of frame. Use this image for camera position, room geography and the two standing/seated positions only. The coloured markers are annotations, not objects and not costume — no coloured shape, overlay, line, dot or drawing appears anywhere in the render, and neither character wears red or yellow. Costume comes from the character references.

LOCATION MAP
Wide shot of the whole room, seen from the far side of the apartment looking toward the window wall, matching the camera position of <<<image_1>>>.
Background: the window wall, running parallel to the sensor — flat on, squared, transom horizontal, mullions vertical, no perspective skew, no diagonal convergence. The grey tower block fills the glass, soft, pale, heavily diffused. The pale sill runs straight across. The white radiator sits low beneath it. The heavy dark red curtain hangs as a vertical band at one edge of the window.
Midground-LEFT: <<<char_captain>>> standing at the window, close to the glass, seen from behind — his back to camera, his body squared to the window plane, parallel to it.
Midground-RIGHT: the round pale table with two chairs. <<<char_wife>>> seated at it, angled roughly three-quarters away from camera, sitting back from the table with her weight settled into the chair. Her RIGHT arm is already forward: the forearm laid flat along the tabletop, the hand flat, palm down, fingers straight and together, fully in contact with the surface. Her LEFT arm is down at her side, below the table line, out of view. On the table, and the only thing on the table, <<<prop_device>>> lies flat — screen up, lens edge facing outward, near the centre of the surface and slightly toward the near edge, clear of her hand and never touched. It reads as one small hard orange rectangle against the pale scratched tabletop — the only saturated colour in the frame.
Side wall: plaster, the dark leafy plant against it.
Foreground: bare floor and open room. Empty.
Camera: tripod, chest height, standing back from both figures, squared to the window wall. Mechanically still for the full duration.

FIRST FRAME AND SPATIAL BLOCKING
First frame: the whole room readable in one wide frame. The window wall fills the background across the width of the picture. <<<char_captain>>> stands at the window on the LEFT side of frame, seen from behind, his silhouette dark against the pale glass, body parallel to the window plane, head level, looking out. The lit cigarette is in his right hand at his side, ember live, a thin ribbon of smoke rising past his shoulder into the window light. <<<char_wife>>> sits at the table in the RIGHT half of frame, midground, head tipped down, right forearm flat on the table with the palm down, left arm out of view at her side, her back resting against the chair. <<<prop_device>>> lies flat on the table in front of her, small in frame at this wide scale but immediately legible as a hard orange shape against the pale wood. The two are separated by several metres of empty floor. Curtain band at the window edge; plant against the wall; radiator low under the sill. Nothing else on the table, nothing on the sill.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:10.

FORMAT MODE
Single continuous wide take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. Tripod — mechanically still, zero movement. Two figures held in one frame, far apart, for the whole shot.

OPTICS
Wide room shot, roughly 55° diagonal field of view — the full geometry of the room legible: floor, walls, the window wall, both figures in their relative positions, her arms on the table, the device. Deep enough focus that both figures, her hands and the device all read clearly; the tower block beyond the glass is soft. Fixed focal length. No focus pull, no rack focus between them, no rack onto the device or onto her hands, no lens breathing, no zoom.

CAMERA
Tripod, head fully clamped, chest height, squared to the window wall.
Zero camera movement for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when he turns, does not react when he speaks, does not react when she leans in.
The window transom, mullions, sill, curtain edge, table position and the device's position on the table remain in identical screen positions from first frame to last, which is the test of whether the lock held.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window on the left, back to the room, body parallel to the glass. Smoke rises past his shoulder in an unbroken ribbon. One slow shallow breath — the shoulder line barely moves. She sits at the table on the right, head tipped down, right hand flat on the table, motionless apart from her breath. Several metres of empty floor between them. Nothing else in the room moves.
0:02–0:03.8 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward her across the frame to screen-right. Roughly 160 to 180 degrees of rotation, unhurried, no snap, no aggression. The cigarette stays in his right hand and swings passively with his arm. When the turn completes he is facing her across the room, his front now toward camera and lit only by the window behind him — his face reading as a darker shape against the bright glass, features soft but legible, not a black cut-out. His eyeline runs across the empty floor toward her, passing over the table and the device.
0:03.8–0:04.4 — A short beat. He is facing her. She has not moved.
0:04.4–0:05.6 — THE LINE. Facing her, he says two words: "Look at me." Quiet, level, flat — not raised, not pleading, not an order. Mouth movement is clear and readable at this wide scale, matching the phonemes and the short length of the line, with no exaggeration. He does not step toward her. He does not gesture. His arms stay down.
0:05.6–0:08.6 — HER RESPONSE. One continuous movement, unhurried, in this order.
First her weight comes off the chair back: the pelvis stays where it is and the torso hinges forward from the hips, a small lean of ten or fifteen centimetres toward the table. The white vest shifts against her shoulders as she comes forward. Her right forearm stays exactly where it is, flat on the table, and simply takes some of the new weight — the hand does not slide, lift or curl.
As she leans, her left arm comes up from her side and settles onto the tabletop: shoulder, elbow, then forearm arriving flat on the surface, the hand finding its own resting place near the right — not mirrored, not symmetrical, not placed with intent. A body opening up and bracing itself because it is about to face someone.
Last, her head comes up. The chin lifts off the chest, the neck lengthens, and her face turns slightly toward him across the room until her eyeline meets his. It is unhurried and unsurprised. She does not startle, does not snap her head up, and does not double-take.
Neither hand ever touches the device.
0:08.6–0:10 — Both hold. He stands facing her across the empty floor, she sits leaning forward with both forearms on the table, looking back at him. Neither speaks again. A long slow exhale from him; smoke drifts forward into the room and rises through the window light. His shoulder line lowers two or three centimetres. The shot ends with the two of them looking at each other across the distance, the device untouched between them, the room still.

DIALOGUE
Exactly one spoken line in the whole shot, spoken by <<<char_captain>>> at 0:04.4: "Look at me."
Male, 40s, quiet, low, level. Delivered plainly, without emphasis or emotional colour, at conversational volume across a room. Two words and nothing more.
No other words at any point. No ad-libs, no muttering, no filler, no breath vocalisations, no repeat of the line. <<<char_wife>>> says nothing at all and her lips stay completely still for the entire 10 seconds. No voice-over. No offscreen voices. No subtitles, no captions.
His lips are completely still except during the line itself.

AUDIO — VOICE AND FOLEY ONLY, ZERO AMBIENCE
The soundtrack contains exactly two elements and nothing else: his single line, and close-mic foley generated by the two bodies. There is no third layer. There is no bed underneath. When no foley event and no voice is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.
The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry, ducked out under the line
2. Cloth — the shift of linen shirt fabric as his shoulder line settles; one soft rustle through the turn; the light drag of her white vest as she leans forward and her left arm comes up
3. Cigarette — a faint dry crackle of burning tobacco; fingers adjusting on the paper
4. Feet — the muted shift of shoe on floor through the turn, very quiet: no hard heel strike, no scuff, no tail
5. Her arm — one soft, low contact sound as her left forearm settles onto the tabletop, dull and dry, no knock, no thud, no scrape
6. Body — a single dry swallow, close-mic level only
7. The spoken line "Look at me."
The device makes no sound at all. No chime, no beep, no notification, no vibration, no buzz, no hum, no synthetic voice, no processing tone, no click, no electronic sound of any kind at any point.
No chair sound. Her chair does not creak, scrape, shift or move when she leans forward.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No music, score, drone, pad, tension bed, sting, swell, riser, whoosh, sub-bass hit or reverb tail used as texture — nothing under the turn, nothing under the line, nothing under her move, nothing at the head or tail of the shot. No foley for objects not present.
Despite the wide framing, the mix stays close and dry: no room reverb, no distance perspective on the voice, no reflections off the walls, no spatialization.

PHYSICS
The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
Standing posture: weight on one leg, pelvis tilted, opposite shoulder marginally lower. No rocking, no swaying, no pacing.
Her lean: the movement is a hip hinge, not a slide forward on the seat. The lumbar spine stays long, the shoulders come forward with the ribcage, and the weight transfers from the chair back onto the forearms on the table. It happens at real human speed, with a small settle at the end as the weight finds the table. She does not slump, does not lurch, does not push the chair back, does not stand.
Her right arm and hand: flat on the table, palm down, fingers straight and together, in contact with the surface from the first frame to the last. It does not lift, slide, curl, spread or tense at any point — it only takes weight as she leans in.
Her left arm: comes up from below the table with real weight and real joint limits — shoulder, elbow, wrist in sequence. The forearm makes contact with the tabletop and settles, the hand finding its own resting position rather than being placed. Slight asymmetry with the right arm. No slap, no slam, no deliberate placement, no gesture. Once settled it stays still.
Her head lift: the movement comes from the neck and upper spine, the chin rising as the eyes come up, the shoulders staying settled. Real cervical anatomy, no snap, no jerk, no double take. The head is the last thing to move, arriving after the lean and after the arm.
Sequencing: torso, then arm, then head — overlapping rather than separate beats, so it reads as one continuous natural movement and not three actions in a row.
Cigarette burn: visibly shorter by the end. Ash accumulates and curls but does not fall within the 10 seconds. The ember does not brighten — there is no drag in this shot.
Smoke: real physical smoke, and the only large moving element in a locked frame. Laminar ribbon from the resting cigarette, breaking into slow turbulence above the tip. The turn disturbs the standing smoke column slightly — it bends and re-forms with real inertia. Slow, heavy. Genuine physical volume, never CG particles, never faster than still indoor air allows. Smoke never reaches the table or drifts across the device.
The device: a solid inert object with real weight, resting flat on the tabletop and in contact with it. Absolutely motionless for all 10 seconds — it does not slide, tip, rotate, vibrate, wake, glow, flicker or change state. Its screen stays dark and dead throughout, showing only the small pale icon as a printed-looking mark, never as a lit display. Nobody touches it, picks it up, points at it or looks at it. It casts a small soft contact shadow onto the table and its metal lens ring holds one steady cold specular from the window; both stay constant.

LIGHTING
Cold grey-green ambient from the window wall — the primary and only light source, backlighting the whole room. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change when he turns, no change when she lifts her head.
The window is the brightest zone of the frame, a soft luminous field across the background. The tower block behind the glass is pale, flat, heavily diffused, its window grid barely legible.
Standing at the glass on the left, he reads as a dark shape against that field from behind. After the turn his front faces camera and is lit only by the room's weak bounce off the plaster walls — his face is a darker, softer shape, legible but low-contrast. Do not add a fill or a key for the turn: his face must not brighten when he turns around. Do not crush it to pure black either — the mouth must stay readable for the line.
Her side of the room, screen-right, falls into the same cold falloff — she is lit by window light raking in from screen-left across the table, sitting a stop or so darker than him. As she leans forward she moves marginally further into that raking light, so her face and the tops of her forearms pick up a fraction more of it. When she lifts her head the light catches the bridge of her nose, her cheekbone and her brow as a thin cold edge, the far side of her face staying in shadow. Do not add a key or a fill for this — the change comes from her moving through the existing falloff, not from the lighting changing.
That same light picks out the scratches in the tabletop, the flat of her right hand and, once it arrives, her left forearm.
<<<prop_device>>> is lit only by that window light. Its orange body is the single point of saturated colour in an otherwise cold grey-green frame, but it stays low-key and desaturated by the ambient cast — muted burnt orange, not vivid. Its black glass panel reads as a dark rectangle with a soft sheen. The device emits no light of its own: it is not a practical, it casts no glow onto the table, onto her hands, or into the room, and it never lights her face.
The dark red curtain at the window edge is deeply desaturated — closer to brown-grey than red, low saturation.
Plant, plaster walls, radiator and floor: dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass across the pale field.
The cigarette ember is a small warm point only. It does not illuminate his face or hand. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
Blocking follows <<<image_1>>>: <<<char_captain>>> standing at the window on the LEFT of frame, <<<char_wife>>> seated at the table on the RIGHT of frame. Do not flip these positions. Do not swap them at any point.
Her RIGHT forearm is flat on the table with the palm down, fingers straight and together, from the first frame to the last. It never leaves the table.
Her LEFT arm starts down at her side, out of view below the table, and comes up onto the tabletop once only, during her lean, settling naturally beside the right. It does not come up earlier, does not come up twice, and does not go back down.
She leans forward from the hips once, during 0:05.6 to 0:08.6, and stays leaning to the end. She does not sit back again.
She lifts her head once, last in the sequence, and keeps her eyes on him to the end.
<<<prop_device>>> sits on the table in the position given by <<<image_1>>>. It is the only object on the table and is never touched by either character.
The device's screen is dark and inert for the entire 10 seconds. It never wakes, never glows, never displays an image, never shows readable text, never blinks, never notifies.
The coloured markers in the blocking reference are annotations only. No red or yellow shape, dot, line, arrow, circle or overlay appears anywhere in the render. Neither character wears red or yellow — costume comes from the character references: he in grey linen over dark, she in a white wrap vest over black. The orange of the device is the only orange in the frame.
Exactly one line of dialogue, "Look at me.", spoken once by <<<char_captain>>> after he has completed the turn. No other speech from anyone.
Wide shot of the room, tripod, chest height, squared to the window wall — the full geometry of the room and the distance between the two figures legible in one frame for the entire shot.
Zero camera movement for the full 10 seconds — framing pixel-identical from first frame to last, including through the turn.
The window wall runs perfectly parallel to the sensor — transom horizontal, mullions vertical, no perspective skew, no diagonal convergence, no dutch.
He begins with his back to camera, standing at the window, body parallel to the glass. He turns once, head and body together, and remains facing her until the end. He never turns back to the window. He never walks toward her. He never touches her, never touches the device, never touches the glass, never opens the window, never draws the curtain, never sits.
She stays seated at the table for all 10 seconds. She does not stand, does not turn her chair, does not answer, does not reach for the device, does not touch him. She holds nothing.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass or in the device's screen.
Nothing exists in the room that is not listed in <<<loc_apt_cap>>> plus <<<prop_device>>>: no second screen, no phone, no monitor, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock, no television. Nothing else on the table. Nothing on the sill. No props invented anywhere in frame.
No visible brand marks, logos or legible lettering anywhere, including on the device.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
The cigarette is in his right hand for the entire shot. No drag in this shot. He does not stub it out, does not put it down, does not tap ash, does not flick it away.
Apart from the single turn and her lean, arm and head lift, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin, fabric or the device.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_143311_e01642db-14a8-41d7-94ea-f11698199daf.mp4)
- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_143951_b7cf0e97-5270-4a90-90f7-277a94785bec.mp4)

</details>

<details><summary>v4 · 2026-08-28 14:43:33 · 1 generation(s) · 026_20260828_144333_cbbd052a.md</summary>

````text
SCENE CONTEXT
A man stands at the window of a small apartment, smoking, his back to the room. The woman is seated at the table on the other side of the room, an orange handheld device lying on the table in front of her. He turns — head and body — to face her, and says two words. She leans forward, brings her second arm onto the table and raises her eyes to him. One continuous 10-second take.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. Standing at the window on the LEFT of frame, back to camera, shoulders low, weight settled on one leg, a lit cigarette in his right hand. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair loosely pulled back. White wrap vest over black t-shirt, dark trousers. Seated at the round table on the RIGHT of frame, angled roughly three-quarters away from camera. 100% matches the reference.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, large window with a dark metal frame and a deep pale sill, cold grey residential tower block filling the glass, heavy dark red curtain hanging at one edge of the window, dark leafy plant against the wall, white radiator low under the window, round pale table with two chairs. Geography, materials and atmosphere only. Nothing in the room beyond what is listed here and the device below.
<<<prop_device>>> — THE ONE OBJECT ON THE TABLE. A small flat handheld device, roughly the size of a phone but thicker and more solid. Matte burnt-orange plastic body with softly rounded corners and a visible seam running around the middle of the casing. The top face is a flush black glass panel, dark and inert, carrying one small pale line-drawn icon near its centre — a simple stylised animal head, a few thin white strokes, no more. A circular camera lens sits in the middle of the front edge, recessed behind a brushed metal ring, dark glass, catching one small cold specular from the window. A small orange loop lug protrudes at one corner of the top edge. No buttons, no ports, no lettering, no branding, no logo, no readable text anywhere on it. 100% matches the reference.
<<<image_2>>> — DEVICE POSITION REFERENCE ONLY. Shows <<<prop_device>>> lying flat on the scratched pale tabletop, screen face up, its lens edge facing outward across the table, roughly at the centre of the table surface and slightly toward the near edge. Use for the device's design, orientation and position on the table only. Do NOT inherit its framing, focal length, shallow depth of field or camera height — this is a wide room shot from the far side of the apartment, not a tabletop close-up.
<<<image_2>>> — BLOCKING REFERENCE ONLY. A photograph of the location with the two character positions marked on it: the RED marker is <<<char_captain>>>, standing at the window on the LEFT of frame; the YELLOW marker is <<<char_wife>>>, seated at the table on the RIGHT of frame. Use this image for camera position, room geography and the two standing/seated positions only. The coloured markers are annotations, not objects and not costume — no coloured shape, overlay, line, dot or drawing appears anywhere in the render, and neither character wears red or yellow. Costume comes from the character references.

LOCATION MAP
Wide shot of the whole room, seen from the far side of the apartment looking toward the window wall, matching the camera position of <<<image_2>>>.
Background: the window wall, running parallel to the sensor — flat on, squared, transom horizontal, mullions vertical, no perspective skew, no diagonal convergence. The grey tower block fills the glass, soft, pale, heavily diffused. The pale sill runs straight across. The white radiator sits low beneath it. The heavy dark red curtain hangs as a vertical band at one edge of the window.
Midground-LEFT: <<<char_captain>>> standing at the window, close to the glass, seen from behind — his back to camera, his body squared to the window plane, parallel to it.
Midground-RIGHT: the round pale table with two chairs. <<<char_wife>>> seated at it, angled roughly three-quarters away from camera, sitting back from the table with her weight settled into the chair. Her RIGHT arm is already forward: the forearm laid flat along the tabletop, the hand flat, palm down, fingers straight and together, fully in contact with the surface. Her LEFT arm is down at her side, below the table line, out of view. On the table, and the only thing on the table, <<<prop_device>>> lies flat — screen up, lens edge facing outward, near the centre of the surface and slightly toward the near edge, clear of her hand and never touched. It reads as one small hard orange rectangle against the pale scratched tabletop — the only saturated colour in the frame.
Side wall: plaster, the dark leafy plant against it.
Foreground: bare floor and open room. Empty.
Camera: tripod, chest height, standing back from both figures, squared to the window wall. Mechanically still for the full duration.

FIRST FRAME AND SPATIAL BLOCKING
First frame: the whole room readable in one wide frame. The window wall fills the background across the width of the picture. <<<char_captain>>> stands at the window on the LEFT side of frame, seen from behind, his silhouette dark against the pale glass, body parallel to the window plane, head level, looking out. The lit cigarette is in his right hand at his side, ember live, a thin ribbon of smoke rising past his shoulder into the window light. <<<char_wife>>> sits at the table in the RIGHT half of frame, midground, head tipped down, right forearm flat on the table with the palm down, left arm out of view at her side, her back resting against the chair. <<<prop_device>>> lies flat on the table in front of her, small in frame at this wide scale but immediately legible as a hard orange shape against the pale wood. The two are separated by several metres of empty floor. Curtain band at the window edge; plant against the wall; radiator low under the sill. Nothing else on the table, nothing on the sill.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:10.

FORMAT MODE
Single continuous wide take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. Tripod — mechanically still, zero movement. Two figures held in one frame, far apart, for the whole shot.

OPTICS
Wide room shot, roughly 55° diagonal field of view — the full geometry of the room legible: floor, walls, the window wall, both figures in their relative positions, her arms on the table, the device. Deep enough focus that both figures, her hands and the device all read clearly; the tower block beyond the glass is soft. Fixed focal length. No focus pull, no rack focus between them, no rack onto the device or onto her hands, no lens breathing, no zoom.

CAMERA
Tripod, head fully clamped, chest height, squared to the window wall.
Zero camera movement for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when he turns, does not react when he speaks, does not react when she leans in.
The window transom, mullions, sill, curtain edge, table position and the device's position on the table remain in identical screen positions from first frame to last, which is the test of whether the lock held.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window on the left, back to the room, body parallel to the glass. Smoke rises past his shoulder in an unbroken ribbon. One slow shallow breath — the shoulder line barely moves. She sits at the table on the right, head tipped down, right hand flat on the table, motionless apart from her breath. Several metres of empty floor between them. Nothing else in the room moves.
0:02–0:03.8 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward her across the frame to screen-right. Roughly 160 to 180 degrees of rotation, unhurried, no snap, no aggression. The cigarette stays in his right hand and swings passively with his arm. When the turn completes he is facing her across the room, his front now toward camera and lit only by the window behind him — his face reading as a darker shape against the bright glass, features soft but legible, not a black cut-out. His eyeline runs across the empty floor toward her, passing over the table and the device.
0:03.8–0:04.4 — A short beat. He is facing her. She has not moved.
0:04.4–0:05.6 — THE LINE. Facing her, he says two words: "Look at me." Quiet, level, flat — not raised, not pleading, not an order. Mouth movement is clear and readable at this wide scale, matching the phonemes and the short length of the line, with no exaggeration. He does not step toward her. He does not gesture. His arms stay down.
0:05.6–0:08.6 — HER RESPONSE. One continuous movement, unhurried, in this order.
First her weight comes off the chair back: the pelvis stays where it is and the torso hinges forward from the hips, a small lean of ten or fifteen centimetres toward the table. The white vest shifts against her shoulders as she comes forward. Her right forearm stays exactly where it is, flat on the table, and simply takes some of the new weight — the hand does not slide, lift or curl.
As she leans, her left arm comes up from her side and settles onto the tabletop: shoulder, elbow, then forearm arriving flat on the surface, the hand finding its own resting place near the right — not mirrored, not symmetrical, not placed with intent. A body opening up and bracing itself because it is about to face someone.
Last, her head comes up. The chin lifts off the chest, the neck lengthens, and her face turns slightly toward him across the room until her eyeline meets his. It is unhurried and unsurprised. She does not startle, does not snap her head up, and does not double-take.
Neither hand ever touches the device.
0:08.6–0:10 — Both hold. He stands facing her across the empty floor, she sits leaning forward with both forearms on the table, looking back at him. Neither speaks again. A long slow exhale from him; smoke drifts forward into the room and rises through the window light. His shoulder line lowers two or three centimetres. The shot ends with the two of them looking at each other across the distance, the device untouched between them, the room still.

DIALOGUE
Exactly one spoken line in the whole shot, spoken by <<<char_captain>>> at 0:04.4: "Look at me."
Male, 40s, quiet, low, level. Delivered plainly, without emphasis or emotional colour, at conversational volume across a room. Two words and nothing more.
No other words at any point. No ad-libs, no muttering, no filler, no breath vocalisations, no repeat of the line. <<<char_wife>>> says nothing at all and her lips stay completely still for the entire 10 seconds. No voice-over. No offscreen voices. No subtitles, no captions.
His lips are completely still except during the line itself.

AUDIO — VOICE AND FOLEY ONLY, ZERO AMBIENCE
The soundtrack contains exactly two elements and nothing else: his single line, and close-mic foley generated by the two bodies. There is no third layer. There is no bed underneath. When no foley event and no voice is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.
The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry, ducked out under the line
2. Cloth — the shift of linen shirt fabric as his shoulder line settles; one soft rustle through the turn; the light drag of her white vest as she leans forward and her left arm comes up
3. Cigarette — a faint dry crackle of burning tobacco; fingers adjusting on the paper
4. Feet — the muted shift of shoe on floor through the turn, very quiet: no hard heel strike, no scuff, no tail
5. Her arm — one soft, low contact sound as her left forearm settles onto the tabletop, dull and dry, no knock, no thud, no scrape
6. Body — a single dry swallow, close-mic level only
7. The spoken line "Look at me."
The device makes no sound at all. No chime, no beep, no notification, no vibration, no buzz, no hum, no synthetic voice, no processing tone, no click, no electronic sound of any kind at any point.
No chair sound. Her chair does not creak, scrape, shift or move when she leans forward.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No music, score, drone, pad, tension bed, sting, swell, riser, whoosh, sub-bass hit or reverb tail used as texture — nothing under the turn, nothing under the line, nothing under her move, nothing at the head or tail of the shot. No foley for objects not present.
Despite the wide framing, the mix stays close and dry: no room reverb, no distance perspective on the voice, no reflections off the walls, no spatialization.

PHYSICS
The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
Standing posture: weight on one leg, pelvis tilted, opposite shoulder marginally lower. No rocking, no swaying, no pacing.
Her lean: the movement is a hip hinge, not a slide forward on the seat. The lumbar spine stays long, the shoulders come forward with the ribcage, and the weight transfers from the chair back onto the forearms on the table. It happens at real human speed, with a small settle at the end as the weight finds the table. She does not slump, does not lurch, does not push the chair back, does not stand.
Her right arm and hand: flat on the table, palm down, fingers straight and together, in contact with the surface from the first frame to the last. It does not lift, slide, curl, spread or tense at any point — it only takes weight as she leans in.
Her left arm: comes up from below the table with real weight and real joint limits — shoulder, elbow, wrist in sequence. The forearm makes contact with the tabletop and settles, the hand finding its own resting position rather than being placed. Slight asymmetry with the right arm. No slap, no slam, no deliberate placement, no gesture. Once settled it stays still.
Her head lift: the movement comes from the neck and upper spine, the chin rising as the eyes come up, the shoulders staying settled. Real cervical anatomy, no snap, no jerk, no double take. The head is the last thing to move, arriving after the lean and after the arm.
Sequencing: torso, then arm, then head — overlapping rather than separate beats, so it reads as one continuous natural movement and not three actions in a row.
Cigarette burn: visibly shorter by the end. Ash accumulates and curls but does not fall within the 10 seconds. The ember does not brighten — there is no drag in this shot.
Smoke: real physical smoke, and the only large moving element in a locked frame. Laminar ribbon from the resting cigarette, breaking into slow turbulence above the tip. The turn disturbs the standing smoke column slightly — it bends and re-forms with real inertia. Slow, heavy. Genuine physical volume, never CG particles, never faster than still indoor air allows. Smoke never reaches the table or drifts across the device.
The device: a solid inert object with real weight, resting flat on the tabletop and in contact with it. Absolutely motionless for all 10 seconds — it does not slide, tip, rotate, vibrate, wake, glow, flicker or change state. Its screen stays dark and dead throughout, showing only the small pale icon as a printed-looking mark, never as a lit display. Nobody touches it, picks it up, points at it or looks at it. It casts a small soft contact shadow onto the table and its metal lens ring holds one steady cold specular from the window; both stay constant.

LIGHTING
Cold grey-green ambient from the window wall — the primary and only light source, backlighting the whole room. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change when he turns, no change when she lifts her head.
The window is the brightest zone of the frame, a soft luminous field across the background. The tower block behind the glass is pale, flat, heavily diffused, its window grid barely legible.
Standing at the glass on the left, he reads as a dark shape against that field from behind. After the turn his front faces camera and is lit only by the room's weak bounce off the plaster walls — his face is a darker, softer shape, legible but low-contrast. Do not add a fill or a key for the turn: his face must not brighten when he turns around. Do not crush it to pure black either — the mouth must stay readable for the line.
Her side of the room, screen-right, falls into the same cold falloff — she is lit by window light raking in from screen-left across the table, sitting a stop or so darker than him. As she leans forward she moves marginally further into that raking light, so her face and the tops of her forearms pick up a fraction more of it. When she lifts her head the light catches the bridge of her nose, her cheekbone and her brow as a thin cold edge, the far side of her face staying in shadow. Do not add a key or a fill for this — the change comes from her moving through the existing falloff, not from the lighting changing.
That same light picks out the scratches in the tabletop, the flat of her right hand and, once it arrives, her left forearm.
<<<prop_device>>> is lit only by that window light. Its orange body is the single point of saturated colour in an otherwise cold grey-green frame, but it stays low-key and desaturated by the ambient cast — muted burnt orange, not vivid. Its black glass panel reads as a dark rectangle with a soft sheen. The device emits no light of its own: it is not a practical, it casts no glow onto the table, onto her hands, or into the room, and it never lights her face.
The dark red curtain at the window edge is deeply desaturated — closer to brown-grey than red, low saturation.
Plant, plaster walls, radiator and floor: dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass across the pale field.
The cigarette ember is a small warm point only. It does not illuminate his face or hand. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
Blocking follows <<<image_2>>>: <<<char_captain>>> standing at the window on the LEFT of frame, <<<char_wife>>> seated at the table on the RIGHT of frame. Do not flip these positions. Do not swap them at any point.
Her RIGHT forearm is flat on the table with the palm down, fingers straight and together, from the first frame to the last. It never leaves the table.
Her LEFT arm starts down at her side, out of view below the table, and comes up onto the tabletop once only, during her lean, settling naturally beside the right. It does not come up earlier, does not come up twice, and does not go back down.
She leans forward from the hips once, during 0:05.6 to 0:08.6, and stays leaning to the end. She does not sit back again.
She lifts her head once, last in the sequence, and keeps her eyes on him to the end.
<<<prop_device>>> sits on the table in the position given by <<<image_2>>>. It is the only object on the table and is never touched by either character.
The device's screen is dark and inert for the entire 10 seconds. It never wakes, never glows, never displays an image, never shows readable text, never blinks, never notifies.
The coloured markers in the blocking reference are annotations only. No red or yellow shape, dot, line, arrow, circle or overlay appears anywhere in the render. Neither character wears red or yellow — costume comes from the character references: he in grey linen over dark, she in a white wrap vest over black. The orange of the device is the only orange in the frame.
Exactly one line of dialogue, "Look at me.", spoken once by <<<char_captain>>> after he has completed the turn. No other speech from anyone.
Wide shot of the room, tripod, chest height, squared to the window wall — the full geometry of the room and the distance between the two figures legible in one frame for the entire shot.
Zero camera movement for the full 10 seconds — framing pixel-identical from first frame to last, including through the turn.
The window wall runs perfectly parallel to the sensor — transom horizontal, mullions vertical, no perspective skew, no diagonal convergence, no dutch.
He begins with his back to camera, standing at the window, body parallel to the glass. He turns once, head and body together, and remains facing her until the end. He never turns back to the window. He never walks toward her. He never touches her, never touches the device, never touches the glass, never opens the window, never draws the curtain, never sits.
She stays seated at the table for all 10 seconds. She does not stand, does not turn her chair, does not answer, does not reach for the device, does not touch him. She holds nothing.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass or in the device's screen.
Nothing exists in the room that is not listed in <<<loc_apt_cap>>> plus <<<prop_device>>>: no second screen, no phone, no monitor, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock, no television. Nothing else on the table. Nothing on the sill. No props invented anywhere in frame.
No visible brand marks, logos or legible lettering anywhere, including on the device.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
The cigarette is in his right hand for the entire shot. No drag in this shot. He does not stub it out, does not put it down, does not tap ash, does not flick it away.
Apart from the single turn and her lean, arm and head lift, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin, fabric or the device.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_144333_cbbd052a-ae0d-46fa-b234-46b2d2b56087.mp4)

</details>

<details><summary>v5 · 2026-08-28 15:05:48 · 1 generation(s) · 027_20260828_150548_4a522be9.md</summary>

````text
SCENE CONTEXT
A man stands at the window of a small apartment, smoking, his back to the room. The woman is seated at the table on the other side of the room, an orange handheld device lying on the table in front of her. He turns — head and body — to face her, and says two words. She leans forward, brings her second arm onto the table and raises her eyes to him. One continuous 10-second take.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. Standing at the window on the LEFT of frame, back to camera, shoulders low, weight settled on one leg, a lit cigarette in his right hand. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair loosely pulled back. White wrap vest over black t-shirt, dark trousers. Seated at the round table on the RIGHT of frame, angled roughly three-quarters away from camera. 100% matches the reference.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, large window with a dark metal frame and a deep pale sill, cold grey residential tower block filling the glass, heavy dark red curtain hanging at one edge of the window, dark leafy plant against the wall, white radiator low under the window, round pale table with two chairs. Geography, materials and atmosphere only. Nothing in the room beyond what is listed here and the device below.
<<<prop_device>>> — THE ONE OBJECT ON THE TABLE. A small flat handheld device, roughly the size of a phone but thicker and more solid. Matte burnt-orange plastic body with softly rounded corners and a visible seam running around the middle of the casing. The top face is a flush black glass panel, dark and inert, carrying one small pale line-drawn icon near its centre — a simple stylised animal head, a few thin white strokes, no more. A circular camera lens sits in the middle of the front edge, recessed behind a brushed metal ring, dark glass, catching one small cold specular from the window. A small orange loop lug protrudes at one corner of the top edge. No buttons, no ports, no lettering, no branding, no logo, no readable text anywhere on it. 100% matches the reference.
<<<image_1>>> — DEVICE POSITION REFERENCE ONLY. Shows <<<prop_device>>> lying flat on the scratched pale tabletop, screen face up, its lens edge facing outward across the table, roughly at the centre of the table surface and slightly toward the near edge. Use for the device's design, orientation and position on the table only. Do NOT inherit its framing, focal length, shallow depth of field or camera height — this is a wide room shot from the far side of the apartment, not a tabletop close-up.
<<<image_2>>> — BLOCKING REFERENCE ONLY. A photograph of the location with the two character positions marked on it: the RED marker is <<<char_captain>>>, standing at the window on the LEFT of frame; the YELLOW marker is <<<char_wife>>>, seated at the table on the RIGHT of frame. Use this image for camera position, room geography and the two standing/seated positions only. The coloured markers are annotations, not objects and not costume — no coloured shape, overlay, line, dot or drawing appears anywhere in the render, and neither character wears red or yellow. Costume comes from the character references.

LOCATION MAP
Wide shot of the whole room, seen from the far side of the apartment looking toward the window wall, matching the camera position of <<<image_1>>>.
Background: the window wall, running parallel to the sensor — flat on, squared, transom horizontal, mullions vertical, no perspective skew, no diagonal convergence. The grey tower block fills the glass, soft, pale, heavily diffused. The pale sill runs straight across. The white radiator sits low beneath it. The heavy dark red curtain hangs as a vertical band at one edge of the window.
Midground-LEFT: <<<char_captain>>> standing at the window, close to the glass, seen from behind — his back to camera, his body squared to the window plane, parallel to it.
Midground-RIGHT: the round pale table with two chairs. <<<char_wife>>> seated at it, angled roughly three-quarters away from camera, sitting back from the table with her weight settled into the chair. Her RIGHT arm is already forward: the forearm laid flat along the tabletop, the hand flat, palm down, fingers straight and together, fully in contact with the surface. Her LEFT arm is down at her side, below the table line, out of view. On the table, and the only thing on the table, <<<prop_device>>> lies flat — screen up, lens edge facing outward, near the centre of the surface and slightly toward the near edge, clear of her hand and never touched. It reads as one small hard orange rectangle against the pale scratched tabletop — the only saturated colour in the frame.
Side wall: plaster, the dark leafy plant against it.
Foreground: bare floor and open room. Empty.
Camera: tripod, chest height, standing back from both figures, squared to the window wall. Mechanically still for the full duration.

FIRST FRAME AND SPATIAL BLOCKING
First frame: the whole room readable in one wide frame. The window wall fills the background across the width of the picture. <<<char_captain>>> stands at the window on the LEFT side of frame, seen from behind, his silhouette dark against the pale glass, body parallel to the window plane, head level, looking out. The lit cigarette is in his right hand at his side, ember live, a thin ribbon of smoke rising past his shoulder into the window light. <<<char_wife>>> sits at the table in the RIGHT half of frame, midground, head tipped down, right forearm flat on the table with the palm down, left arm out of view at her side, her back resting against the chair. <<<prop_device>>> lies flat on the table in front of her, small in frame at this wide scale but immediately legible as a hard orange shape against the pale wood. The two are separated by several metres of empty floor. Curtain band at the window edge; plant against the wall; radiator low under the sill. Nothing else on the table, nothing on the sill.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:10.

FORMAT MODE
Single continuous wide take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. Tripod — mechanically still, zero movement. Two figures held in one frame, far apart, for the whole shot.

OPTICS
Wide room shot, roughly 55° diagonal field of view — the full geometry of the room legible: floor, walls, the window wall, both figures in their relative positions, her arms on the table, the device. Deep enough focus that both figures, her hands and the device all read clearly; the tower block beyond the glass is soft. Fixed focal length. No focus pull, no rack focus between them, no rack onto the device or onto her hands, no lens breathing, no zoom.

CAMERA
Tripod, head fully clamped, chest height, squared to the window wall.
Zero camera movement for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when he turns, does not react when he speaks, does not react when she leans in.
The window transom, mullions, sill, curtain edge, table position and the device's position on the table remain in identical screen positions from first frame to last, which is the test of whether the lock held.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window on the left, back to the room, body parallel to the glass. Smoke rises past his shoulder in an unbroken ribbon. One slow shallow breath — the shoulder line barely moves. She sits at the table on the right, head tipped down, right hand flat on the table, motionless apart from her breath. Several metres of empty floor between them. Nothing else in the room moves.
0:02–0:03.8 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward her across the frame to screen-right. Roughly 160 to 180 degrees of rotation, unhurried, no snap, no aggression. The cigarette stays in his right hand and swings passively with his arm. When the turn completes he is facing her across the room, his front now toward camera and lit only by the window behind him — his face reading as a darker shape against the bright glass, features soft but legible, not a black cut-out. His eyeline runs across the empty floor toward her, passing over the table and the device.
0:03.8–0:04.4 — A short beat. He is facing her. She has not moved.
0:04.4–0:05.6 — THE LINE. Facing her, he says two words: "Look at me." Quiet, level, flat — not raised, not pleading, not an order. Mouth movement is clear and readable at this wide scale, matching the phonemes and the short length of the line, with no exaggeration. He does not step toward her. He does not gesture. His arms stay down.
0:05.6–0:08.6 — HER RESPONSE. One continuous movement, unhurried, in this order.
First her weight comes off the chair back: the pelvis stays where it is and the torso hinges forward from the hips, a small lean of ten or fifteen centimetres toward the table. The white vest shifts against her shoulders as she comes forward. Her right forearm stays exactly where it is, flat on the table, and simply takes some of the new weight — the hand does not slide, lift or curl.
As she leans, her left arm comes up from her side and settles onto the tabletop: shoulder, elbow, then forearm arriving flat on the surface, the hand finding its own resting place near the right — not mirrored, not symmetrical, not placed with intent. A body opening up and bracing itself because it is about to face someone.
Last, her head comes up. The chin lifts off the chest, the neck lengthens, and her face turns slightly toward him across the room until her eyeline meets his. It is unhurried and unsurprised. She does not startle, does not snap her head up, and does not double-take.
Neither hand ever touches the device.
0:08.6–0:10 — Both hold. He stands facing her across the empty floor, she sits leaning forward with both forearms on the table, looking back at him. Neither speaks again. A long slow exhale from him; smoke drifts forward into the room and rises through the window light. His shoulder line lowers two or three centimetres. The shot ends with the two of them looking at each other across the distance, the device untouched between them, the room still.

DIALOGUE
Exactly one spoken line in the whole shot, spoken by <<<char_captain>>> at 0:04.4: "Look at me."
Male, 40s, quiet, low, level. Delivered plainly, without emphasis or emotional colour, at conversational volume across a room. Two words and nothing more.
No other words at any point. No ad-libs, no muttering, no filler, no breath vocalisations, no repeat of the line. <<<char_wife>>> says nothing at all and her lips stay completely still for the entire 10 seconds. No voice-over. No offscreen voices. No subtitles, no captions.
His lips are completely still except during the line itself.

AUDIO — VOICE AND FOLEY ONLY, ZERO AMBIENCE
The soundtrack contains exactly two elements and nothing else: his single line, and close-mic foley generated by the two bodies. There is no third layer. There is no bed underneath. When no foley event and no voice is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.
The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry, ducked out under the line
2. Cloth — the shift of linen shirt fabric as his shoulder line settles; one soft rustle through the turn; the light drag of her white vest as she leans forward and her left arm comes up
3. Cigarette — a faint dry crackle of burning tobacco; fingers adjusting on the paper
4. Feet — the muted shift of shoe on floor through the turn, very quiet: no hard heel strike, no scuff, no tail
5. Her arm — one soft, low contact sound as her left forearm settles onto the tabletop, dull and dry, no knock, no thud, no scrape
6. Body — a single dry swallow, close-mic level only
7. The spoken line "Look at me."
The device makes no sound at all. No chime, no beep, no notification, no vibration, no buzz, no hum, no synthetic voice, no processing tone, no click, no electronic sound of any kind at any point.
No chair sound. Her chair does not creak, scrape, shift or move when she leans forward.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No music, score, drone, pad, tension bed, sting, swell, riser, whoosh, sub-bass hit or reverb tail used as texture — nothing under the turn, nothing under the line, nothing under her move, nothing at the head or tail of the shot. No foley for objects not present.
Despite the wide framing, the mix stays close and dry: no room reverb, no distance perspective on the voice, no reflections off the walls, no spatialization.

PHYSICS
The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
Standing posture: weight on one leg, pelvis tilted, opposite shoulder marginally lower. No rocking, no swaying, no pacing.
Her lean: the movement is a hip hinge, not a slide forward on the seat. The lumbar spine stays long, the shoulders come forward with the ribcage, and the weight transfers from the chair back onto the forearms on the table. It happens at real human speed, with a small settle at the end as the weight finds the table. She does not slump, does not lurch, does not push the chair back, does not stand.
Her right arm and hand: flat on the table, palm down, fingers straight and together, in contact with the surface from the first frame to the last. It does not lift, slide, curl, spread or tense at any point — it only takes weight as she leans in.
Her left arm: comes up from below the table with real weight and real joint limits — shoulder, elbow, wrist in sequence. The forearm makes contact with the tabletop and settles, the hand finding its own resting position rather than being placed. Slight asymmetry with the right arm. No slap, no slam, no deliberate placement, no gesture. Once settled it stays still.
Her head lift: the movement comes from the neck and upper spine, the chin rising as the eyes come up, the shoulders staying settled. Real cervical anatomy, no snap, no jerk, no double take. The head is the last thing to move, arriving after the lean and after the arm.
Sequencing: torso, then arm, then head — overlapping rather than separate beats, so it reads as one continuous natural movement and not three actions in a row.
Cigarette burn: visibly shorter by the end. Ash accumulates and curls but does not fall within the 10 seconds. The ember does not brighten — there is no drag in this shot.
Smoke: real physical smoke, and the only large moving element in a locked frame. Laminar ribbon from the resting cigarette, breaking into slow turbulence above the tip. The turn disturbs the standing smoke column slightly — it bends and re-forms with real inertia. Slow, heavy. Genuine physical volume, never CG particles, never faster than still indoor air allows. Smoke never reaches the table or drifts across the device.
The device: a solid inert object with real weight, resting flat on the tabletop and in contact with it. Absolutely motionless for all 10 seconds — it does not slide, tip, rotate, vibrate, wake, glow, flicker or change state. Its screen stays dark and dead throughout, showing only the small pale icon as a printed-looking mark, never as a lit display. Nobody touches it, picks it up, points at it or looks at it. It casts a small soft contact shadow onto the table and its metal lens ring holds one steady cold specular from the window; both stay constant.

LIGHTING
Cold grey-green ambient from the window wall — the primary and only light source, backlighting the whole room. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change when he turns, no change when she lifts her head.
The window is the brightest zone of the frame, a soft luminous field across the background. The tower block behind the glass is pale, flat, heavily diffused, its window grid barely legible.
Standing at the glass on the left, he reads as a dark shape against that field from behind. After the turn his front faces camera and is lit only by the room's weak bounce off the plaster walls — his face is a darker, softer shape, legible but low-contrast. Do not add a fill or a key for the turn: his face must not brighten when he turns around. Do not crush it to pure black either — the mouth must stay readable for the line.
Her side of the room, screen-right, falls into the same cold falloff — she is lit by window light raking in from screen-left across the table, sitting a stop or so darker than him. As she leans forward she moves marginally further into that raking light, so her face and the tops of her forearms pick up a fraction more of it. When she lifts her head the light catches the bridge of her nose, her cheekbone and her brow as a thin cold edge, the far side of her face staying in shadow. Do not add a key or a fill for this — the change comes from her moving through the existing falloff, not from the lighting changing.
That same light picks out the scratches in the tabletop, the flat of her right hand and, once it arrives, her left forearm.
<<<prop_device>>> is lit only by that window light. Its orange body is the single point of saturated colour in an otherwise cold grey-green frame, but it stays low-key and desaturated by the ambient cast — muted burnt orange, not vivid. Its black glass panel reads as a dark rectangle with a soft sheen. The device emits no light of its own: it is not a practical, it casts no glow onto the table, onto her hands, or into the room, and it never lights her face.
The dark red curtain at the window edge is deeply desaturated — closer to brown-grey than red, low saturation.
Plant, plaster walls, radiator and floor: dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass across the pale field.
The cigarette ember is a small warm point only. It does not illuminate his face or hand. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
Blocking follows <<<image_2>>>: <<<char_captain>>> standing at the window on the LEFT of frame, <<<char_wife>>> seated at the table on the RIGHT of frame. Do not flip these positions. Do not swap them at any point.
Her RIGHT forearm is flat on the table with the palm down, fingers straight and together, from the first frame to the last. It never leaves the table.
Her LEFT arm starts down at her side, out of view below the table, and comes up onto the tabletop once only, during her lean, settling naturally beside the right. It does not come up earlier, does not come up twice, and does not go back down.
She leans forward from the hips once, during 0:05.6 to 0:08.6, and stays leaning to the end. She does not sit back again.
She lifts her head once, last in the sequence, and keeps her eyes on him to the end.
<<<prop_device>>> sits on the table in the position given by <<<image_1>>>. It is the only object on the table and is never touched by either character.
The device's screen is dark and inert for the entire 10 seconds. It never wakes, never glows, never displays an image, never shows readable text, never blinks, never notifies.
The coloured markers in the blocking reference are annotations only. No red or yellow shape, dot, line, arrow, circle or overlay appears anywhere in the render. Neither character wears red or yellow — costume comes from the character references: he in grey linen over dark, she in a white wrap vest over black. The orange of the device is the only orange in the frame.
Exactly one line of dialogue, "Look at me.", spoken once by <<<char_captain>>> after he has completed the turn. No other speech from anyone.
Wide shot of the room, tripod, chest height, squared to the window wall — the full geometry of the room and the distance between the two figures legible in one frame for the entire shot.
Zero camera movement for the full 10 seconds — framing pixel-identical from first frame to last, including through the turn.
The window wall runs perfectly parallel to the sensor — transom horizontal, mullions vertical, no perspective skew, no diagonal convergence, no dutch.
He begins with his back to camera, standing at the window, body parallel to the glass. He turns once, head and body together, and remains facing her until the end. He never turns back to the window. He never walks toward her. He never touches her, never touches the device, never touches the glass, never opens the window, never draws the curtain, never sits.
She stays seated at the table for all 10 seconds. She does not stand, does not turn her chair, does not answer, does not reach for the device, does not touch him. She holds nothing.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass or in the device's screen.
Nothing exists in the room that is not listed in <<<loc_apt_cap>>> plus <<<prop_device>>>: no second screen, no phone, no monitor, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock, no television. Nothing else on the table. Nothing on the sill. No props invented anywhere in frame.
No visible brand marks, logos or legible lettering anywhere, including on the device.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
The cigarette is in his right hand for the entire shot. No drag in this shot. He does not stub it out, does not put it down, does not tap ash, does not flick it away.
Apart from the single turn and her lean, arm and head lift, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin, fabric or the device.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_150548_4a522be9-ee33-4da3-95ae-8bdf92e06190.mp4)

</details>

<details><summary>v6 · 2026-08-28 15:20:10 · 1 generation(s) · 028_20260828_152010_d3f9be7f.md</summary>

````text
SCENE CONTEXT
A man stands at the window of a small apartment, smoking, his back to the room. The woman is seated at the table on the other side of the room, head held high but her eyes cast down, an orange handheld device lying on the table in front of her. He turns — head and body — to face her, and says two words. She leans forward, brings her second arm onto the table and raises her eyes to him. One continuous 10-second take.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. Standing at the window on the LEFT of frame, back to camera, shoulders low, weight settled on one leg, a lit cigarette in his right hand. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair pulled back into a low loose knot with fine strands escaping at the temple and the nape. White wrap vest with a wide shawl collar over a black t-shirt, dark trousers. A plain thin silver ring on one finger of the right hand. Seated at the round table on the RIGHT of frame, angled roughly three-quarters away from camera. 100% matches the reference.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, large window with a dark metal frame and a deep pale sill, cold grey residential tower block filling the glass, heavy dark red curtain hanging at one edge of the window, dark leafy plant against the wall, white radiator low under the window, round pale table with two chairs. Geography, materials and atmosphere only. Nothing in the room beyond what is listed here and the device below.
<<<prop_device>>> — THE ONE OBJECT ON THE TABLE. A small flat handheld device, roughly the size of a phone but thicker and more solid. Matte burnt-orange plastic body with softly rounded corners and a visible seam running around the middle of the casing. The top face is a flush black glass panel, dark and inert, carrying one small pale line-drawn icon near its centre — a simple stylised animal head, a few thin white strokes, no more. A circular camera lens sits in the middle of the front edge, recessed behind a brushed metal ring, dark glass, catching one small cold specular from the window. A small orange loop lug protrudes at one corner of the top edge. No buttons, no ports, no lettering, no branding, no logo, no readable text anywhere on it. 100% matches the reference.
<<<image_1>>> — DEVICE POSITION REFERENCE ONLY. Shows <<<prop_device>>> lying flat on the scratched pale tabletop, screen face up, its lens edge facing outward across the table, roughly at the centre of the table surface and slightly toward the near edge. Use for the device's design, orientation and position on the table only. Do NOT inherit its framing, focal length, shallow depth of field or camera height — this is a wide room shot from the far side of the apartment, not a tabletop close-up.
<<<image_3>>> — WOMAN'S STARTING POSITION REFERENCE. This is her exact posture in the first frame. Read from it and reproduce it:
— She sits upright and settled, back against the chair, shoulders level and relaxed, no slump.
— HEAD HIGH. The head is NOT tipped down toward the table. The neck is long, the chin level or fractionally raised, the head carried upright and composed on top of the spine. The jawline is clear of the chest. Her face is held in clean profile, turned away from camera toward the window side of the room.
— EYES DOWN. Inside that raised head, the gaze is lowered — the eyelids heavy and half-lowered, the pupils cast down toward the tabletop in front of her. She is not looking at anything. The eyes are down, the head is up. That contradiction is the whole point of the pose and must be visible: a woman holding her head up while refusing to look.
— Her RIGHT arm is extended forward from the shoulder and laid along the tabletop, the forearm resting flat on the surface with the elbow off the near edge and the upper arm relaxed. The right hand is flat, palm down, fingers straight and together, lying fully in contact with the table. The thin silver ring is visible on that hand. The arm is relaxed, not braced, not gripping, not clenched.
— Her LEFT arm is down at her side, below the table line, out of view.
Use this image for her posture, head carriage, eye direction and right arm and hand pose only. Do NOT inherit its framing, its camera height, its lens or its shot size — this is a wide room shot from the far side of the apartment, not a profile medium.
<<<image_2>>> — BLOCKING REFERENCE ONLY. A photograph of the location with the two character positions marked on it: the RED marker is <<<char_captain>>>, standing at the window on the LEFT of frame; the YELLOW marker is <<<char_wife>>>, seated at the table on the RIGHT of frame. Use this image for camera position, room geography and the two standing/seated positions only. The coloured markers are annotations, not objects and not costume — no coloured shape, overlay, line, dot or drawing appears anywhere in the render, and neither character wears red or yellow. Costume comes from the character references.

LOCATION MAP
Wide shot of the whole room, seen from the far side of the apartment looking toward the window wall, matching the camera position of <<<image_2>>>.
Background: the window wall, running parallel to the sensor — flat on, squared, transom horizontal, mullions vertical, no perspective skew, no diagonal convergence. The grey tower block fills the glass, soft, pale, heavily diffused. The pale sill runs straight across. The white radiator sits low beneath it. The heavy dark red curtain hangs as a vertical band at one edge of the window.
Midground-LEFT: <<<char_captain>>> standing at the window, close to the glass, seen from behind — his back to camera, his body squared to the window plane, parallel to it.
Midground-RIGHT: the round pale table with two chairs. <<<char_wife>>> seated at it, angled roughly three-quarters away from camera, in the posture given by <<<image_3>>> — upright, back against the chair, head high, eyes down, right forearm flat on the table, left arm out of view at her side. On the table, and the only thing on the table, <<<prop_device>>> lies flat — screen up, lens edge facing outward, near the centre of the surface and slightly toward the near edge, clear of her hand and never touched. It reads as one small hard orange rectangle against the pale scratched tabletop — the only saturated colour in the frame.
Side wall: plaster, the dark leafy plant against it.
Foreground: bare floor and open room. Empty.
Camera: tripod, chest height, standing back from both figures, squared to the window wall. Mechanically still for the full duration.

FIRST FRAME AND SPATIAL BLOCKING
First frame: the whole room readable in one wide frame. The window wall fills the background across the width of the picture. <<<char_captain>>> stands at the window on the LEFT side of frame, seen from behind, his silhouette dark against the pale glass, body parallel to the window plane, head level, looking out. The lit cigarette is in his right hand at his side, ember live, a thin ribbon of smoke rising past his shoulder into the window light.
<<<char_wife>>> sits at the table in the RIGHT half of frame, midground, exactly as in <<<image_3>>>: back against the chair, shoulders level, HEAD HIGH and neck long with the chin clear of the chest, EYES LOWERED to the tabletop under heavy half-closed lids, right forearm flat on the table with the palm down and fingers together, left arm out of view at her side. Her head is up and her gaze is down. She does not look defeated; she looks composed and withheld.
<<<prop_device>>> lies flat on the table in front of her, small in frame at this wide scale but immediately legible as a hard orange shape against the pale wood. The two are separated by several metres of empty floor. Curtain band at the window edge; plant against the wall; radiator low under the sill. Nothing else on the table, nothing on the sill.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:10.

FORMAT MODE
Single continuous wide take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. Tripod — mechanically still, zero movement. Two figures held in one frame, far apart, for the whole shot.

OPTICS
Wide room shot, roughly 55° diagonal field of view — the full geometry of the room legible: floor, walls, the window wall, both figures in their relative positions, her arms on the table, the device. Deep enough focus that both figures, her hands and the device all read clearly; the tower block beyond the glass is soft. Fixed focal length. No focus pull, no rack focus between them, no rack onto the device or onto her hands, no lens breathing, no zoom.

CAMERA
Tripod, head fully clamped, chest height, squared to the window wall.
Zero camera movement for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when he turns, does not react when he speaks, does not react when she leans in.
The window transom, mullions, sill, curtain edge, table position and the device's position on the table remain in identical screen positions from first frame to last, which is the test of whether the lock held.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window on the left, back to the room, body parallel to the glass. Smoke rises past his shoulder in an unbroken ribbon. One slow shallow breath — the shoulder line barely moves. She sits at the table on the right in the <<<image_3>>> posture: head high, eyes down, right hand flat on the table, motionless apart from her breath. Her head does not drop and her eyes do not come up. Several metres of empty floor between them. Nothing else in the room moves.
0:02–0:03.8 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward her across the frame to screen-right. Roughly 160 to 180 degrees of rotation, unhurried, no snap, no aggression. The cigarette stays in his right hand and swings passively with his arm. When the turn completes he is facing her across the room, his front now toward camera and lit only by the window behind him — his face reading as a darker shape against the bright glass, features soft but legible, not a black cut-out. His eyeline runs across the empty floor toward her, passing over the table and the device.
0:03.8–0:04.4 — A short beat. He is facing her. She has not moved. Her head is still up and her eyes are still down — she knows he has turned and does not acknowledge it.
0:04.4–0:05.6 — THE LINE. Facing her, he says two words: "Look at me." Quiet, level, flat — not raised, not pleading, not an order. Mouth movement is clear and readable at this wide scale, matching the phonemes and the short length of the line, with no exaggeration. He does not step toward her. He does not gesture. His arms stay down.
0:05.6–0:08.6 — HER RESPONSE. One continuous movement, unhurried, in this order.
First her weight comes off the chair back: the pelvis stays where it is and the torso hinges forward from the hips, a small lean of ten or fifteen centimetres toward the table. The white vest shifts against her shoulders as she comes forward. Her right forearm stays exactly where it is, flat on the table, and simply takes some of the new weight — the hand does not slide, lift or curl. Her head stays high through the lean; it does not dip.
As she leans, her left arm comes up from her side and settles onto the tabletop: shoulder, elbow, then forearm arriving flat on the surface, the hand finding its own resting place near the right — not mirrored, not symmetrical, not placed with intent. A body opening up and bracing itself because it is about to face someone.
Last, THE EYES COME UP. Because the head is already high, this is not a head lift — it is the gaze rising inside a head that is already raised. The lids open, the pupils travel up off the tabletop and across the empty floor to him, and only then does the head turn a few degrees toward him to follow the eyeline. The eyes lead, the head follows a fraction behind. It is unhurried and unsurprised. She does not startle, does not snap her head up, and does not double-take.
Neither hand ever touches the device.
0:08.6–0:10 — Both hold. He stands facing her across the empty floor, she sits leaning forward with both forearms on the table, looking back at him. Neither speaks again. A long slow exhale from him; smoke drifts forward into the room and rises through the window light. His shoulder line lowers two or three centimetres. The shot ends with the two of them looking at each other across the distance, the device untouched between them, the room still.

DIALOGUE
Exactly one spoken line in the whole shot, spoken by <<<char_captain>>> at 0:04.4: "Look at me."
Male, 40s, quiet, low, level. Delivered plainly, without emphasis or emotional colour, at conversational volume across a room. Two words and nothing more.
No other words at any point. No ad-libs, no muttering, no filler, no breath vocalisations, no repeat of the line. <<<char_wife>>> says nothing at all and her lips stay completely still for the entire 10 seconds. No voice-over. No offscreen voices. No subtitles, no captions.
His lips are completely still except during the line itself.

AUDIO — VOICE AND FOLEY ONLY, ZERO AMBIENCE
The soundtrack contains exactly two elements and nothing else: his single line, and close-mic foley generated by the two bodies. There is no third layer. There is no bed underneath. When no foley event and no voice is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.
The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry, ducked out under the line
2. Cloth — the shift of linen shirt fabric as his shoulder line settles; one soft rustle through the turn; the light drag of her white vest as she leans forward and her left arm comes up
3. Cigarette — a faint dry crackle of burning tobacco; fingers adjusting on the paper
4. Feet — the muted shift of shoe on floor through the turn, very quiet: no hard heel strike, no scuff, no tail
5. Her arm — one soft, low contact sound as her left forearm settles onto the tabletop, dull and dry, no knock, no thud, no scrape
6. Body — a single dry swallow, close-mic level only
7. The spoken line "Look at me."
The device makes no sound at all. No chime, no beep, no notification, no vibration, no buzz, no hum, no synthetic voice, no processing tone, no click, no electronic sound of any kind at any point.
No chair sound. Her chair does not creak, scrape, shift or move when she leans forward.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No music, score, drone, pad, tension bed, sting, swell, riser, whoosh, sub-bass hit or reverb tail used as texture — nothing under the turn, nothing under the line, nothing under her move, nothing at the head or tail of the shot. No foley for objects not present.
Despite the wide framing, the mix stays close and dry: no room reverb, no distance perspective on the voice, no reflections off the walls, no spatialization.

PHYSICS
The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
Standing posture: weight on one leg, pelvis tilted, opposite shoulder marginally lower. No rocking, no swaying, no pacing.
Her head carriage: the head stays high for the entire 10 seconds. The cervical spine is long and the chin stays clear of the chest at all times. She never drops her head, never tucks her chin, never lets the head sink toward the table. The only head movement in the shot is a small turn of a few degrees toward him at the very end, following the eyes.
Her gaze: for the first 5.6 seconds the eyes are lowered inside that raised head — lids heavy and half-closed, pupils down toward the tabletop, unfocused. This is a downward gaze, not a downward head. When the eyes come up they travel first, the lids opening as the pupils rise, and the head turns a beat later to follow. Real ocular and cervical sequencing.
Her lean: the movement is a hip hinge, not a slide forward on the seat. The lumbar spine stays long, the shoulders come forward with the ribcage, the head stays up on top of the spine, and the weight transfers from the chair back onto the forearms on the table. It happens at real human speed, with a small settle at the end as the weight finds the table. She does not slump, does not lurch, does not push the chair back, does not stand.
Her right arm and hand: flat on the table, palm down, fingers straight and together, in contact with the surface from the first frame to the last. It does not lift, slide, curl, spread or tense at any point — it only takes weight as she leans in.
Her left arm: comes up from below the table with real weight and real joint limits — shoulder, elbow, wrist in sequence. The forearm makes contact with the tabletop and settles, the hand finding its own resting position rather than being placed. Slight asymmetry with the right arm. No slap, no slam, no deliberate placement, no gesture. Once settled it stays still.
Sequencing: torso, then arm, then eyes, then a small head turn — overlapping rather than separate beats, so it reads as one continuous natural movement and not four actions in a row.
Cigarette burn: visibly shorter by the end. Ash accumulates and curls but does not fall within the 10 seconds. The ember does not brighten — there is no drag in this shot.
Smoke: real physical smoke, and the only large moving element in a locked frame. Laminar ribbon from the resting cigarette, breaking into slow turbulence above the tip. The turn disturbs the standing smoke column slightly — it bends and re-forms with real inertia. Slow, heavy. Genuine physical volume, never CG particles, never faster than still indoor air allows. Smoke never reaches the table or drifts across the device.
The device: a solid inert object with real weight, resting flat on the tabletop and in contact with it. Absolutely motionless for all 10 seconds — it does not slide, tip, rotate, vibrate, wake, glow, flicker or change state. Its screen stays dark and dead throughout, showing only the small pale icon as a printed-looking mark, never as a lit display. Nobody touches it, picks it up, points at it or looks at it. It casts a small soft contact shadow onto the table and its metal lens ring holds one steady cold specular from the window; both stay constant.

LIGHTING
Cold grey-green ambient from the window wall — the primary and only light source, backlighting the whole room. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change when he turns, no change when her eyes come up.
The window is the brightest zone of the frame, a soft luminous field across the background. The tower block behind the glass is pale, flat, heavily diffused, its window grid barely legible.
Standing at the glass on the left, he reads as a dark shape against that field from behind. After the turn his front faces camera and is lit only by the room's weak bounce off the plaster walls — his face is a darker, softer shape, legible but low-contrast. Do not add a fill or a key for the turn: his face must not brighten when he turns around. Do not crush it to pure black either — the mouth must stay readable for the line.
Her side of the room, screen-right, falls into the same cold falloff — she is lit by window light raking in from screen-left across the table, sitting a stop or so darker than him. Because her head is up rather than tipped down, that raking light catches the length of her throat, her jawline, her cheekbone and the bridge of her nose in clean profile from the first frame, while her lowered eyes sit in shadow under the brow. As she leans forward she moves marginally further into the light and the profile sharpens a fraction. Do not add a key or a fill for this — the change comes from her moving through the existing falloff, not from the lighting changing.
That same light picks out the loose strands at her temple, the scratches in the tabletop, the flat of her right hand with its thin silver ring, and, once it arrives, her left forearm.
<<<prop_device>>> is lit only by that window light. Its orange body is the single point of saturated colour in an otherwise cold grey-green frame, but it stays low-key and desaturated by the ambient cast — muted burnt orange, not vivid. Its black glass panel reads as a dark rectangle with a soft sheen. The device emits no light of its own: it is not a practical, it casts no glow onto the table, onto her hands, or into the room, and it never lights her face.
The dark red curtain at the window edge is deeply desaturated — closer to brown-grey than red, low saturation.
Plant, plaster walls, radiator and floor: dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass across the pale field.
The cigarette ember is a small warm point only. It does not illuminate his face or hand. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
Her starting posture follows <<<image_3>>> exactly: upright, back to the chair, HEAD HIGH with the chin clear of the chest, EYES LOWERED to the tabletop, right forearm flat on the table with the palm down and fingers together, left arm out of view at her side.
Head high and gaze low is the pose. Her head is never tipped down, never bowed, never sunk toward the table at any point in the 10 seconds. The lowered look comes entirely from the eyes.
When she responds, the eyes rise first inside the already-raised head; the head only turns a few degrees afterward to follow. There is no head lift, because the head is already up.
Her RIGHT forearm is flat on the table with the palm down, fingers straight and together, from the first frame to the last. It never leaves the table.
Her LEFT arm starts down at her side, out of view below the table, and comes up onto the tabletop once only, during her lean, settling naturally beside the right. It does not come up earlier, does not come up twice, and does not go back down.
She leans forward from the hips once, during 0:05.6 to 0:08.6, and stays leaning to the end. She does not sit back again.
<<<image_3>>> supplies her posture, head carriage, eye direction and right arm pose only. Its framing, camera height, lens and shot size must not be reproduced. This shot stays wide.
Blocking follows <<<image_2>>>: <<<char_captain>>> standing at the window on the LEFT of frame, <<<char_wife>>> seated at the table on the RIGHT of frame. Do not flip these positions. Do not swap them at any point.
<<<prop_device>>> sits on the table in the position given by <<<image_1>>>. It is the only object on the table and is never touched by either character.
The device's screen is dark and inert for the entire 10 seconds. It never wakes, never glows, never displays an image, never shows readable text, never blinks, never notifies.
The coloured markers in the blocking reference are annotations only. No red or yellow shape, dot, line, arrow, circle or overlay appears anywhere in the render. Neither character wears red or yellow — costume comes from the character references: he in grey linen over dark, she in a white wrap vest over black. The orange of the device is the only orange in the frame.
Exactly one line of dialogue, "Look at me.", spoken once by <<<char_captain>>> after he has completed the turn. No other speech from anyone.
Wide shot of the room, tripod, chest height, squared to the window wall — the full geometry of the room and the distance between the two figures legible in one frame for the entire shot.
Zero camera movement for the full 10 seconds — framing pixel-identical from first frame to last, including through the turn.
The window wall runs perfectly parallel to the sensor — transom horizontal, mullions vertical, no perspective skew, no diagonal convergence, no dutch.
He begins with his back to camera, standing at the window, body parallel to the glass. He turns once, head and body together, and remains facing her until the end. He never turns back to the window. He never walks toward her. He never touches her, never touches the device, never touches the glass, never opens the window, never draws the curtain, never sits.
She stays seated at the table for all 10 seconds. She does not stand, does not turn her chair, does not answer, does not reach for the device, does not touch him. She holds nothing.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass or in the device's screen.
Nothing exists in the room that is not listed in <<<loc_apt_cap>>> plus <<<prop_device>>>: no second screen, no phone, no monitor, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock, no television. Nothing else on the table. Nothing on the sill. No props invented anywhere in frame.
No visible brand marks, logos or legible lettering anywhere, including on the device.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
The cigarette is in his right hand for the entire shot. No drag in this shot. He does not stub it out, does not put it down, does not tap ash, does not flick it away.
Apart from the single turn and her lean, arm and eye movement, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin, fabric or the device.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_152010_d3f9be7f-1022-4dec-bf70-03744a87448a.mp4)

</details>

<details><summary>v7 · 2026-08-28 15:33:35 · 2 generation(s) · 029_20260828_153335_9c4a5958.md</summary>

````text
SCENE CONTEXT
A man stands at the window of a small apartment, smoking, his back to the room. The woman is seated at the table on the other side of the room, head held high but her eyes cast down, a small orange handheld device lying on the table in front of her. He turns — head and body — to face her, and says two words. She leans forward, brings her second arm onto the table and raises her eyes to him. One continuous 10-second take.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. Standing at the window on the LEFT of frame, back to camera, shoulders low, weight settled on one leg, a lit cigarette in his right hand. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair pulled back into a low loose knot with fine strands escaping at the temple and the nape. White wrap vest with a wide shawl collar over a black t-shirt, dark trousers. A plain thin silver ring on one finger of the right hand. Seated at the round table on the RIGHT of frame, angled roughly three-quarters away from camera. 100% matches the reference.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, large window with a dark metal frame and a deep pale sill, cold grey residential tower block filling the glass, heavy dark red curtain hanging at one edge of the window, dark leafy plant against the wall, white radiator low under the window, round pale table with two chairs. Geography, materials and atmosphere only. Nothing in the room beyond what is listed here and the device below.
<<<prop_device>>> — THE ONE OBJECT ON THE TABLE. A small flat handheld device with a matte burnt-orange plastic body, softly rounded corners and a visible seam running around the middle of the casing. The top face is a flush black glass panel, dark and inert, carrying one small pale line-drawn icon near its centre — a simple stylised animal head, a few thin white strokes, no more. A circular camera lens sits in the middle of the front edge, recessed behind a brushed metal ring, dark glass, catching one small cold specular from the window. A small orange loop lug protrudes at one corner of the top edge. No buttons, no ports, no lettering, no branding, no logo, no readable text anywhere on it. 100% matches the reference for design, proportion and material.
SCALE — CRITICAL. The device is SMALLER THAN HER HAND. Its full length is shorter than the length of her flat right hand from wrist to fingertips, and its width is narrower than her palm. If her open hand were laid over it, the hand would cover it completely and overhang it on every side. Think of a small pocket camera or a matchbox-plus, not a phone, not a tablet, not a remote control. On the round tabletop it occupies only a small fraction of the surface. In this wide room shot it reads as a tiny hard orange marker on the pale wood — noticeable because of its colour, not because of its size.
<<<image_1>>> — DEVICE POSITION REFERENCE ONLY. Shows <<<prop_device>>> lying flat on the scratched pale tabletop, screen face up, its lens edge facing outward across the table, roughly at the centre of the table surface and slightly toward the near edge. Use for the device's design, orientation and position on the table only. Do NOT inherit its framing, focal length, shallow depth of field or camera height — this is a wide room shot from the far side of the apartment, not a tabletop close-up. Above all, do NOT inherit its apparent size: that reference is a macro close-up which makes the device look large. In this shot it is a small object, smaller than her hand.
<<<image_3>>> — WOMAN'S STARTING POSITION REFERENCE. This is her exact posture in the first frame. Read from it and reproduce it:
— She sits upright and settled, back against the chair, shoulders level and relaxed, no slump.
— HEAD HIGH. The head is NOT tipped down toward the table. The neck is long, the chin level or fractionally raised, the head carried upright and composed on top of the spine. The jawline is clear of the chest. Her face is held in clean profile, turned away from camera toward the window side of the room.
— EYES DOWN. Inside that raised head, the gaze is lowered — the eyelids heavy and half-lowered, the pupils cast down toward the tabletop in front of her. She is not looking at anything. The eyes are down, the head is up. That contradiction is the whole point of the pose and must be visible: a woman holding her head up while refusing to look.
— Her RIGHT arm is extended forward from the shoulder and laid along the tabletop, the forearm resting flat on the surface with the elbow off the near edge and the upper arm relaxed. The right hand is flat, palm down, fingers straight and together, lying fully in contact with the table. The thin silver ring is visible on that hand. The arm is relaxed, not braced, not gripping, not clenched.
— Her LEFT arm is down at her side, below the table line, out of view.
This hand is also the scale reference for the device: whatever size her flat right hand reads at on the table, <<<prop_device>>> must read smaller.
Use this image for her posture, head carriage, eye direction and right arm and hand pose only. Do NOT inherit its framing, its camera height, its lens or its shot size — this is a wide room shot from the far side of the apartment, not a profile medium.
<<<image_2>>> — BLOCKING REFERENCE ONLY. A photograph of the location with the two character positions marked on it: the RED marker is <<<char_captain>>>, standing at the window on the LEFT of frame; the YELLOW marker is <<<char_wife>>>, seated at the table on the RIGHT of frame. Use this image for camera position, room geography and the two standing/seated positions only. The coloured markers are annotations, not objects and not costume — no coloured shape, overlay, line, dot or drawing appears anywhere in the render, and neither character wears red or yellow. Costume comes from the character references.

LOCATION MAP
Wide shot of the whole room, seen from the far side of the apartment looking toward the window wall, matching the camera position of <<<image_2>>>.
Background: the window wall, running parallel to the sensor — flat on, squared, transom horizontal, mullions vertical, no perspective skew, no diagonal convergence. The grey tower block fills the glass, soft, pale, heavily diffused. The pale sill runs straight across. The white radiator sits low beneath it. The heavy dark red curtain hangs as a vertical band at one edge of the window.
Midground-LEFT: <<<char_captain>>> standing at the window, close to the glass, seen from behind — his back to camera, his body squared to the window plane, parallel to it.
Midground-RIGHT: the round pale table with two chairs. <<<char_wife>>> seated at it, angled roughly three-quarters away from camera, in the posture given by <<<image_3>>> — upright, back against the chair, head high, eyes down, right forearm flat on the table, left arm out of view at her side. On the table, and the only thing on the table, <<<prop_device>>> lies flat — screen up, lens edge facing outward, near the centre of the surface and slightly toward the near edge, well clear of her hand and never touched. It is small: shorter than her flat hand and narrower than her palm, a tiny hard orange rectangle on a large pale scratched tabletop, dwarfed by the table around it. It is the only saturated colour in the frame.
Side wall: plaster, the dark leafy plant against it.
Foreground: bare floor and open room. Empty.
Camera: tripod, chest height, standing back from both figures, squared to the window wall. Mechanically still for the full duration.

FIRST FRAME AND SPATIAL BLOCKING
First frame: the whole room readable in one wide frame. The window wall fills the background across the width of the picture. <<<char_captain>>> stands at the window on the LEFT side of frame, seen from behind, his silhouette dark against the pale glass, body parallel to the window plane, head level, looking out. The lit cigarette is in his right hand at his side, ember live, a thin ribbon of smoke rising past his shoulder into the window light.
<<<char_wife>>> sits at the table in the RIGHT half of frame, midground, exactly as in <<<image_3>>>: back against the chair, shoulders level, HEAD HIGH and neck long with the chin clear of the chest, EYES LOWERED to the tabletop under heavy half-closed lids, right forearm flat on the table with the palm down and fingers together, left arm out of view at her side. Her head is up and her gaze is down. She does not look defeated; she looks composed and withheld.
<<<prop_device>>> lies flat on the table in front of her — a small object, visibly smaller than her nearby flat hand, reading at this wide scale as a little hard orange mark on the pale wood. It is legible only because of its colour, never because it dominates the table.
The two are separated by several metres of empty floor. Curtain band at the window edge; plant against the wall; radiator low under the sill. Nothing else on the table, nothing on the sill.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:10.

FORMAT MODE
Single continuous wide take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. Tripod — mechanically still, zero movement. Two figures held in one frame, far apart, for the whole shot.

OPTICS
Wide room shot, roughly 55° diagonal field of view — the full geometry of the room legible: floor, walls, the window wall, both figures in their relative positions, her arms on the table, the device. Deep enough focus that both figures, her hands and the device all read clearly; the tower block beyond the glass is soft. Fixed focal length. No focus pull, no rack focus between them, no rack onto the device or onto her hands, no lens breathing, no zoom.

CAMERA
Tripod, head fully clamped, chest height, squared to the window wall.
Zero camera movement for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when he turns, does not react when he speaks, does not react when she leans in.
The window transom, mullions, sill, curtain edge, table position and the device's position on the table remain in identical screen positions from first frame to last, which is the test of whether the lock held.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window on the left, back to the room, body parallel to the glass. Smoke rises past his shoulder in an unbroken ribbon. One slow shallow breath — the shoulder line barely moves. She sits at the table on the right in the <<<image_3>>> posture: head high, eyes down, right hand flat on the table, motionless apart from her breath. Her head does not drop and her eyes do not come up. Several metres of empty floor between them. Nothing else in the room moves.
0:02–0:03.8 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward her across the frame to screen-right. Roughly 160 to 180 degrees of rotation, unhurried, no snap, no aggression. The cigarette stays in his right hand and swings passively with his arm. When the turn completes he is facing her across the room, his front now toward camera and lit only by the window behind him — his face reading as a darker shape against the bright glass, features soft but legible, not a black cut-out. His eyeline runs across the empty floor toward her, passing over the table and the device.
0:03.8–0:04.4 — A short beat. He is facing her. She has not moved. Her head is still up and her eyes are still down — she knows he has turned and does not acknowledge it.
0:04.4–0:05.6 — THE LINE. Facing her, he says two words: "Look at me." Quiet, level, flat — not raised, not pleading, not an order. Mouth movement is clear and readable at this wide scale, matching the phonemes and the short length of the line, with no exaggeration. He does not step toward her. He does not gesture. His arms stay down.
0:05.6–0:08.6 — HER RESPONSE. One continuous movement, unhurried, in this order.
First her weight comes off the chair back: the pelvis stays where it is and the torso hinges forward from the hips, a small lean of ten or fifteen centimetres toward the table. The white vest shifts against her shoulders as she comes forward. Her right forearm stays exactly where it is, flat on the table, and simply takes some of the new weight — the hand does not slide, lift or curl. Her head stays high through the lean; it does not dip.
As she leans, her left arm comes up from her side and settles onto the tabletop: shoulder, elbow, then forearm arriving flat on the surface, the hand finding its own resting place near the right — not mirrored, not symmetrical, not placed with intent. A body opening up and bracing itself because it is about to face someone. As both hands come to rest on the table near the device, the size difference is plainly readable: each hand is larger than the whole object.
Last, THE EYES COME UP. Because the head is already high, this is not a head lift — it is the gaze rising inside a head that is already raised. The lids open, the pupils travel up off the tabletop and across the empty floor to him, and only then does the head turn a few degrees toward him to follow the eyeline. The eyes lead, the head follows a fraction behind. It is unhurried and unsurprised. She does not startle, does not snap her head up, and does not double-take.
Neither hand ever touches the device.
0:08.6–0:10 — Both hold. He stands facing her across the empty floor, she sits leaning forward with both forearms on the table, looking back at him. Neither speaks again. A long slow exhale from him; smoke drifts forward into the room and rises through the window light. His shoulder line lowers two or three centimetres. The shot ends with the two of them looking at each other across the distance, the small device untouched between them, the room still.

DIALOGUE
Exactly one spoken line in the whole shot, spoken by <<<char_captain>>> at 0:04.4: "Look at me."
Male, 40s, quiet, low, level. Delivered plainly, without emphasis or emotional colour, at conversational volume across a room. Two words and nothing more.
No other words at any point. No ad-libs, no muttering, no filler, no breath vocalisations, no repeat of the line. <<<char_wife>>> says nothing at all and her lips stay completely still for the entire 10 seconds. No voice-over. No offscreen voices. No subtitles, no captions.
His lips are completely still except during the line itself.

AUDIO — VOICE AND FOLEY ONLY, ZERO AMBIENCE
The soundtrack contains exactly two elements and nothing else: his single line, and close-mic foley generated by the two bodies. There is no third layer. There is no bed underneath. When no foley event and no voice is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.
The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry, ducked out under the line
2. Cloth — the shift of linen shirt fabric as his shoulder line settles; one soft rustle through the turn; the light drag of her white vest as she leans forward and her left arm comes up
3. Cigarette — a faint dry crackle of burning tobacco; fingers adjusting on the paper
4. Feet — the muted shift of shoe on floor through the turn, very quiet: no hard heel strike, no scuff, no tail
5. Her arm — one soft, low contact sound as her left forearm settles onto the tabletop, dull and dry, no knock, no thud, no scrape
6. Body — a single dry swallow, close-mic level only
7. The spoken line "Look at me."
The device makes no sound at all. No chime, no beep, no notification, no vibration, no buzz, no hum, no synthetic voice, no processing tone, no click, no electronic sound of any kind at any point.
No chair sound. Her chair does not creak, scrape, shift or move when she leans forward.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No music, score, drone, pad, tension bed, sting, swell, riser, whoosh, sub-bass hit or reverb tail used as texture — nothing under the turn, nothing under the line, nothing under her move, nothing at the head or tail of the shot. No foley for objects not present.
Despite the wide framing, the mix stays close and dry: no room reverb, no distance perspective on the voice, no reflections off the walls, no spatialization.

PHYSICS
The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
Standing posture: weight on one leg, pelvis tilted, opposite shoulder marginally lower. No rocking, no swaying, no pacing.
Her head carriage: the head stays high for the entire 10 seconds. The cervical spine is long and the chin stays clear of the chest at all times. She never drops her head, never tucks her chin, never lets the head sink toward the table. The only head movement in the shot is a small turn of a few degrees toward him at the very end, following the eyes.
Her gaze: for the first 5.6 seconds the eyes are lowered inside that raised head — lids heavy and half-closed, pupils down toward the tabletop, unfocused. This is a downward gaze, not a downward head. When the eyes come up they travel first, the lids opening as the pupils rise, and the head turns a beat later to follow. Real ocular and cervical sequencing.
Her lean: the movement is a hip hinge, not a slide forward on the seat. The lumbar spine stays long, the shoulders come forward with the ribcage, the head stays up on top of the spine, and the weight transfers from the chair back onto the forearms on the table. It happens at real human speed, with a small settle at the end as the weight finds the table. She does not slump, does not lurch, does not push the chair back, does not stand.
Her right arm and hand: flat on the table, palm down, fingers straight and together, in contact with the surface from the first frame to the last. It does not lift, slide, curl, spread or tense at any point — it only takes weight as she leans in.
Her left arm: comes up from below the table with real weight and real joint limits — shoulder, elbow, wrist in sequence. The forearm makes contact with the tabletop and settles, the hand finding its own resting position rather than being placed. Slight asymmetry with the right arm. No slap, no slam, no deliberate placement, no gesture. Once settled it stays still.
Sequencing: torso, then arm, then eyes, then a small head turn — overlapping rather than separate beats, so it reads as one continuous natural movement and not four actions in a row.
Cigarette burn: visibly shorter by the end. Ash accumulates and curls but does not fall within the 10 seconds. The ember does not brighten — there is no drag in this shot.
Smoke: real physical smoke, and the only large moving element in a locked frame. Laminar ribbon from the resting cigarette, breaking into slow turbulence above the tip. The turn disturbs the standing smoke column slightly — it bends and re-forms with real inertia. Slow, heavy. Genuine physical volume, never CG particles, never faster than still indoor air allows. Smoke never reaches the table or drifts across the device.
The device: a small, solid, inert object with real weight, resting flat on the tabletop and in contact with it. Its scale is consistent for the entire shot — smaller than her hand, never growing, never shrinking, never changing proportion relative to the table or to her hands. Absolutely motionless for all 10 seconds — it does not slide, tip, rotate, vibrate, wake, glow, flicker or change state. Its screen stays dark and dead throughout, showing only the small pale icon as a printed-looking mark, never as a lit display. Nobody touches it, picks it up, points at it or looks at it. It casts a small soft contact shadow onto the table and its metal lens ring holds one steady cold specular from the window; both stay constant and both are scaled to its small size.

LIGHTING
Cold grey-green ambient from the window wall — the primary and only light source, backlighting the whole room. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change when he turns, no change when her eyes come up.
The window is the brightest zone of the frame, a soft luminous field across the background. The tower block behind the glass is pale, flat, heavily diffused, its window grid barely legible.
Standing at the glass on the left, he reads as a dark shape against that field from behind. After the turn his front faces camera and is lit only by the room's weak bounce off the plaster walls — his face is a darker, softer shape, legible but low-contrast. Do not add a fill or a key for the turn: his face must not brighten when he turns around. Do not crush it to pure black either — the mouth must stay readable for the line.
Her side of the room, screen-right, falls into the same cold falloff — she is lit by window light raking in from screen-left across the table, sitting a stop or so darker than him. Because her head is up rather than tipped down, that raking light catches the length of her throat, her jawline, her cheekbone and the bridge of her nose in clean profile from the first frame, while her lowered eyes sit in shadow under the brow. As she leans forward she moves marginally further into the light and the profile sharpens a fraction. Do not add a key or a fill for this — the change comes from her moving through the existing falloff, not from the lighting changing.
That same light picks out the loose strands at her temple, the scratches in the tabletop, the flat of her right hand with its thin silver ring, and, once it arrives, her left forearm.
<<<prop_device>>> is lit only by that window light. Its orange body is the single point of saturated colour in an otherwise cold grey-green frame, but it is small and it stays low-key and desaturated by the ambient cast — muted burnt orange, not vivid, a small mark rather than a block of colour. Its black glass panel reads as a tiny dark rectangle with a soft sheen. The device emits no light of its own: it is not a practical, it casts no glow onto the table, onto her hands, or into the room, and it never lights her face.
The dark red curtain at the window edge is deeply desaturated — closer to brown-grey than red, low saturation.
Plant, plaster walls, radiator and floor: dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass across the pale field.
The cigarette ember is a small warm point only. It does not illuminate his face or hand. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
<<<prop_device>>> is SMALLER THAN HER HAND. Its length is shorter than her flat right hand from wrist to fingertips and its width is narrower than her palm. Her open hand would completely cover it. This proportion holds in every frame.
The device is a small object on a large table. It never reads as phone-sized, tablet-sized or remote-control-sized, and it never becomes a hero prop.
<<<image_1>>> supplies the device's design, orientation and placement only. Its macro close-up framing, low camera height and shallow depth of field must not be reproduced, and its apparent size in that image must not be inherited.
Her starting posture follows <<<image_3>>> exactly: upright, back to the chair, HEAD HIGH with the chin clear of the chest, EYES LOWERED to the tabletop, right forearm flat on the table with the palm down and fingers together, left arm out of view at her side.
Head high and gaze low is the pose. Her head is never tipped down, never bowed, never sunk toward the table at any point in the 10 seconds. The lowered look comes entirely from the eyes.
When she responds, the eyes rise first inside the already-raised head; the head only turns a few degrees afterward to follow. There is no head lift, because the head is already up.
Her RIGHT forearm is flat on the table with the palm down, fingers straight and together, from the first frame to the last. It never leaves the table.
Her LEFT arm starts down at her side, out of view below the table, and comes up onto the tabletop once only, during her lean, settling naturally beside the right. It does not come up earlier, does not come up twice, and does not go back down.
She leans forward from the hips once, during 0:05.6 to 0:08.6, and stays leaning to the end. She does not sit back again.
<<<image_3>>> supplies her posture, head carriage, eye direction and right arm pose only, plus the hand that sets the scale for the device. Its framing, camera height, lens and shot size must not be reproduced. This shot stays wide.
Blocking follows <<<image_2>>>: <<<char_captain>>> standing at the window on the LEFT of frame, <<<char_wife>>> seated at the table on the RIGHT of frame. Do not flip these positions. Do not swap them at any point.
<<<prop_device>>> sits on the table in the position given by <<<image_1>>>. It is the only object on the table and is never touched by either character.
The device's screen is dark and inert for the entire 10 seconds. It never wakes, never glows, never displays an image, never shows readable text, never blinks, never notifies.
The coloured markers in the blocking reference are annotations only. No red or yellow shape, dot, line, arrow, circle or overlay appears anywhere in the render. Neither character wears red or yellow — costume comes from the character references: he in grey linen over dark, she in a white wrap vest over black. The orange of the device is the only orange in the frame.
Exactly one line of dialogue, "Look at me.", spoken once by <<<char_captain>>> after he has completed the turn. No other speech from anyone.
Wide shot of the room, tripod, chest height, squared to the window wall — the full geometry of the room and the distance between the two figures legible in one frame for the entire shot.
Zero camera movement for the full 10 seconds — framing pixel-identical from first frame to last, including through the turn.
The window wall runs perfectly parallel to the sensor — transom horizontal, mullions vertical, no perspective skew, no diagonal convergence, no dutch.
He begins with his back to camera, standing at the window, body parallel to the glass. He turns once, head and body together, and remains facing her until the end. He never turns back to the window. He never walks toward her. He never touches her, never touches the device, never touches the glass, never opens the window, never draws the curtain, never sits.
She stays seated at the table for all 10 seconds. She does not stand, does not turn her chair, does not answer, does not reach for the device, does not touch him. She holds nothing.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass or in the device's screen.
Nothing exists in the room that is not listed in <<<loc_apt_cap>>> plus <<<prop_device>>>: no second screen, no phone, no monitor, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock, no television. Nothing else on the table. Nothing on the sill. No props invented anywhere in frame.
No visible brand marks, logos or legible lettering anywhere, including on the device.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
The cigarette is in his right hand for the entire shot. No drag in this shot. He does not stub it out, does not put it down, does not tap ash, does not flick it away.
Apart from the single turn and her lean, arm and eye movement, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin, fabric or the device.

NEGATIVE — SCALE LOCK
The device is never as large as her hand, never larger than her hand, and never the size of a phone or a book. If it looks like she could not cover it with one palm, it is too big.
No enlarging the device to make it more visible. Its visibility comes from colour contrast against pale wood, not from size.
No close-up, no insert, no rack focus and no framing change to feature the device. It stays a small background detail in a wide shot.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_153335_9c4a5958-4646-4067-9be6-68dd1a175f1e.mp4)
- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_154828_0685945a-28fd-442b-8150-f2f6c759a971.mp4)

</details>

<details><summary>v8 · 2026-08-29 14:10:43 · 1 generation(s) · 054_20260829_141043_f528f3dc.md</summary>

````text
SCENE CONTEXT
A man stands at the window of a small apartment, smoking, his back to the room. The woman is seated at the table on the other side of the room, head held high but her eyes cast down, an orange handheld device lying on the table in front of her. He turns — head and body — to face her. Nothing is said. She leans forward, brings her second arm onto the table and raises her eyes to him. One continuous 10-second take, entirely without dialogue and entirely without music.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. Standing at the window on the LEFT of frame, back to camera, shoulders low, weight settled on one leg, a lit cigarette in his right hand. He is a silent character in this shot — he never speaks. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair pulled back into a low loose knot with fine strands escaping at the temple and the nape. White wrap vest with a wide shawl collar over a black t-shirt, dark trousers. A plain thin silver ring on one finger of the right hand. Seated at the round table on the RIGHT of frame, angled roughly three-quarters away from camera. She is a silent character in this shot — she never speaks. 100% matches the reference.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, large window with a dark metal frame and a deep pale sill, cold grey residential tower block filling the glass, heavy dark red curtain hanging at one edge of the window, dark leafy plant against the wall, white radiator low under the window, round pale table with two chairs. Geography, materials and atmosphere only. Nothing in the room beyond what is listed here and the device below.
<<<prop_device>>> — THE ONE OBJECT ON THE TABLE. A small flat handheld device, roughly the size of a phone but thicker and more solid. Matte burnt-orange plastic body with softly rounded corners and a visible seam running around the middle of the casing. The top face is a flush black glass panel, dark and inert, carrying one small pale line-drawn icon near its centre — a simple stylised animal head, a few thin white strokes, no more. A circular camera lens sits in the middle of the front edge, recessed behind a brushed metal ring, dark glass, catching one small cold specular from the window. A small orange loop lug protrudes at one corner of the top edge. No buttons, no ports, no lettering, no branding, no logo, no readable text anywhere on it. 100% matches the reference.
<<<image_1>>> — DEVICE POSITION REFERENCE ONLY. Shows <<<prop_device>>> lying flat on the scratched pale tabletop, screen face up, its lens edge facing outward across the table, roughly at the centre of the table surface and slightly toward the near edge. Use for the device's design, orientation and position on the table only. Do NOT inherit its framing, focal length, shallow depth of field or camera height — this is a wide room shot from the far side of the apartment, not a tabletop close-up.
<<<image_2>>> — WOMAN'S STARTING POSITION REFERENCE. This is her exact posture in the first frame. Read from it and reproduce it:
— She sits upright and settled, back against the chair, shoulders level and relaxed, no slump.
— HEAD HIGH. The head is NOT tipped down toward the table. The neck is long, the chin level or fractionally raised, the head carried upright and composed on top of the spine. The jawline is clear of the chest. Her face is held in clean profile, turned away from camera toward the window side of the room.
— EYES DOWN. Inside that raised head, the gaze is lowered — the eyelids heavy and half-lowered, the pupils cast down toward the tabletop in front of her. She is not looking at anything. The eyes are down, the head is up. That contradiction is the whole point of the pose and must be visible: a woman holding her head up while refusing to look.
— Her RIGHT arm is extended forward from the shoulder and laid along the tabletop, the forearm resting flat on the surface with the elbow off the near edge and the upper arm relaxed. The right hand is flat, palm down, fingers straight and together, lying fully in contact with the table. The thin silver ring is visible on that hand. The arm is relaxed, not braced, not gripping, not clenched.
— Her LEFT arm is down at her side, below the table line, out of view.
Use this image for her posture, head carriage, eye direction and right arm and hand pose only. Do NOT inherit its framing, its camera height, its lens or its shot size — this is a wide room shot from the far side of the apartment, not a profile medium.
<<<image_2>>> — BLOCKING REFERENCE ONLY. A photograph of the location with the two character positions marked on it: the RED marker is <<<char_captain>>>, standing at the window on the LEFT of frame; the YELLOW marker is <<<char_wife>>>, seated at the table on the RIGHT of frame. Use this image for camera position, room geography and the two standing/seated positions only. The coloured markers are annotations, not objects and not costume — no coloured shape, overlay, line, dot or drawing appears anywhere in the render, and neither character wears red or yellow. Costume comes from the character references.

LOCATION MAP
Wide shot of the whole room, seen from the far side of the apartment looking toward the window wall, matching the camera position of <<<image_2>>>.
Background: the window wall, running parallel to the sensor — flat on, squared, transom horizontal, mullions vertical, no perspective skew, no diagonal convergence. The grey tower block fills the glass, soft, pale, heavily diffused. The pale sill runs straight across. The white radiator sits low beneath it. The heavy dark red curtain hangs as a vertical band at one edge of the window.
Midground-LEFT: <<<char_captain>>> standing at the window, close to the glass, seen from behind — his back to camera, his body squared to the window plane, parallel to it.
Midground-RIGHT: the round pale table with two chairs. <<<char_wife>>> seated at it, angled roughly three-quarters away from camera, in the posture given by <<<image_2>>> — upright, back against the chair, head high, eyes down, right forearm flat on the table, left arm out of view at her side. On the table, and the only thing on the table, <<<prop_device>>> lies flat — screen up, lens edge facing outward, near the centre of the surface and slightly toward the near edge, clear of her hand and never touched. It reads as one small hard orange rectangle against the pale scratched tabletop — the only saturated colour in the frame.
Side wall: plaster, the dark leafy plant against it.
Foreground: bare floor and open room. Empty.
Camera: tripod, chest height, standing back from both figures, squared to the window wall. Mechanically still for the full duration.

FIRST FRAME AND SPATIAL BLOCKING
First frame: the whole room readable in one wide frame. The window wall fills the background across the width of the picture. <<<char_captain>>> stands at the window on the LEFT side of frame, seen from behind, his silhouette dark against the pale glass, body parallel to the window plane, head level, looking out. The lit cigarette is in his right hand at his side, ember live, a thin ribbon of smoke rising past his shoulder into the window light.
<<<char_wife>>> sits at the table in the RIGHT half of frame, midground, exactly as in <<<image_2>>>: back against the chair, shoulders level, HEAD HIGH and neck long with the chin clear of the chest, EYES LOWERED to the tabletop under heavy half-closed lids, right forearm flat on the table with the palm down and fingers together, left arm out of view at her side. Her head is up and her gaze is down. She does not look defeated; she looks composed and withheld.
<<<prop_device>>> lies flat on the table in front of her, small in frame at this wide scale but immediately legible as a hard orange shape against the pale wood. The two are separated by several metres of empty floor. Curtain band at the window edge; plant against the wall; radiator low under the sill. Nothing else on the table, nothing on the sill.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:10.

FORMAT MODE
Single continuous wide take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. Tripod — mechanically still, zero movement. Two figures held in one frame, far apart, for the whole shot. No dialogue and no music anywhere in the shot.

OPTICS
Wide room shot, roughly 55° diagonal field of view — the full geometry of the room legible: floor, walls, the window wall, both figures in their relative positions, her arms on the table, the device. Deep enough focus that both figures, her hands and the device all read clearly; the tower block beyond the glass is soft. Fixed focal length. No focus pull, no rack focus between them, no rack onto the device or onto her hands, no lens breathing, no zoom.

CAMERA
Tripod, head fully clamped, chest height, squared to the window wall.
Zero camera movement for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when he turns and does not react when she leans in.
The window transom, mullions, sill, curtain edge, table position and the device's position on the table remain in identical screen positions from first frame to last, which is the test of whether the lock held.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window on the left, back to the room, body parallel to the glass. Smoke rises past his shoulder in an unbroken ribbon. One slow shallow breath — the shoulder line barely moves. She sits at the table on the right in the <<<image_2>>> posture: head high, eyes down, right hand flat on the table, motionless apart from her breath. Her head does not drop and her eyes do not come up. Several metres of empty floor between them. Nothing else in the room moves.

0:02–0:03.8 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward her across the frame to screen-right. Roughly 160 to 180 degrees of rotation, unhurried, no snap, no aggression. The cigarette stays in his right hand and swings passively with his arm. When the turn completes he is facing her across the room, his front now toward camera and lit only by the window behind him — his face reading as a darker shape against the bright glass, features soft but legible, not a black cut-out. His eyeline runs across the empty floor toward her, passing over the table and the device.

0:03.8–0:05.6 — THE SILENCE. He is facing her and he says nothing. His mouth stays closed and completely still. He does not step toward her, does not gesture, does not raise a hand. His arms stay down.
    She has not moved. Her head is still up and her eyes are still down — she knows he has turned and does not acknowledge it.
    This is the longest still beat in the shot and it is entirely empty: two people in one room, one facing the other, neither speaking, nothing on the soundtrack but breath. Hold it in full. It is not filled with a line, a sound, a music cue, a gesture or a camera move.

0:05.6–0:08.6 — HER RESPONSE. One continuous movement, unhurried, in this order. She begins it on her own — nothing has been said to her and no gesture has been made.
First her weight comes off the chair back: the pelvis stays where it is and the torso hinges forward from the hips, a small lean of ten or fifteen centimetres toward the table. The white vest shifts against her shoulders as she comes forward. Her right forearm stays exactly where it is, flat on the table, and simply takes some of the new weight — the hand does not slide, lift or curl. Her head stays high through the lean; it does not dip.
As she leans, her left arm comes up from her side and settles onto the tabletop: shoulder, elbow, then forearm arriving flat on the surface, the hand finding its own resting place near the right — not mirrored, not symmetrical, not placed with intent. A body opening up and bracing itself because it is about to face someone.
Last, THE EYES COME UP. Because the head is already high, this is not a head lift — it is the gaze rising inside a head that is already raised. The lids open, the pupils travel up off the tabletop and across the empty floor to him, and only then does the head turn a few degrees toward him to follow the eyeline. The eyes lead, the head follows a fraction behind. It is unhurried and unsurprised. She does not startle, does not snap her head up, and does not double-take.
Neither hand ever touches the device.

0:08.6–0:10 — Both hold. He stands facing her across the empty floor, she sits leaning forward with both forearms on the table, looking back at him. Neither of them speaks, then or at any earlier point. A long slow exhale from him; smoke drifts forward into the room and rises through the window light. His shoulder line lowers two or three centimetres. The shot ends with the two of them looking at each other across the distance, in silence, the device untouched between them, the room still. No music enters at the end.

DIALOGUE
THERE IS NO DIALOGUE IN THIS SHOT. Not one word is spoken by anyone at any point in the 10 seconds.
<<<char_captain>>> does not speak. His lips stay completely closed and completely still for the entire duration, including through the turn, through the silence after it, and through her response. He does not mouth anything, does not part his lips as if about to speak, does not murmur, does not sigh audibly, does not clear his throat.
<<<char_wife>>> does not speak. Her lips stay completely closed and completely still for the entire duration.
No voice-over. No offscreen voices. No whisper. No vocalisation of any kind from either character. No subtitles, no captions, no on-screen text.

AUDIO — FOLEY ONLY, ZERO MUSIC, ZERO VOICE, ZERO AMBIENCE

NO MUSIC. THIS IS THE FIRST AND MOST IMPORTANT AUDIO INSTRUCTION.
There is no music anywhere in this shot, at any point, at any volume, under any name. Not at the head, not at the tail, not under the turn, not under the silence, not under her lean, not under the final hold. Not faint, not distant, not "barely audible", not buried in the mix.
Specifically forbidden, in every form: score, soundtrack, underscore, cue, theme, motif, melody, harmony, chord, sustained tone, drone, pad, hum, swell, riser, sting, hit, impact, boom, braam, whoosh, sub-bass pulse, heartbeat pulse, ticking, tension bed, suspense bed, emotional bed, ambient music, atmospheric music, cinematic music, trailer sound design, orchestral element, string tone, piano note, synth tone, bass note, choir, vocal pad, reverb tail used as a musical texture, and any pitched sustained sound of any kind.
Do not add music to make the silence feel intentional. Do not add music to support the emotion of the scene. Do not add music because the shot is long and quiet. The absence of music IS the intended effect. The scene must play completely dry.
If a rendering process would normally add a musical bed to a dialogue-free shot, it must not do so here.

THE SOUNDTRACK CONTAINS EXACTLY ONE ELEMENT: close-mic foley generated by the two bodies. There is no voice track, no music track, and no ambience track. When no foley event is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.

The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry
2. Cloth — the shift of linen shirt fabric as his shoulder line settles; one soft rustle through the turn; the light drag of her white vest as she leans forward and her left arm comes up
3. Cigarette — a faint dry crackle of burning tobacco; fingers adjusting on the paper
4. Feet — the muted shift of shoe on floor through the turn, very quiet: no hard heel strike, no scuff, no tail
5. Her arm — one soft, low contact sound as her left forearm settles onto the tabletop, dull and dry, no knock, no thud, no scrape
6. Body — a single dry swallow, close-mic level only

No spoken word, no vocal sound, no breath shaped like a word, no hum, no sigh with voice in it.
The device makes no sound at all. No chime, no beep, no notification, no vibration, no buzz, no hum, no synthetic voice, no processing tone, no click, no electronic sound of any kind at any point.
No chair sound. Her chair does not creak, scrape, shift or move when she leans forward.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No foley for objects not present.
Despite the wide framing, the mix stays close and dry: no room reverb, no distance perspective, no reflections off the walls, no spatialization.

PHYSICS
The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
Standing posture: weight on one leg, pelvis tilted, opposite shoulder marginally lower. No rocking, no swaying, no pacing.
His face after the turn: still and closed. The jaw does not move, the lips do not part, the mouth does not shape anything. Whatever is happening is happening behind the face. Blinking is irregular and natural.
Her head carriage: the head stays high for the entire 10 seconds. The cervical spine is long and the chin stays clear of the chest at all times. She never drops her head, never tucks her chin, never lets the head sink toward the table. The only head movement in the shot is a small turn of a few degrees toward him at the very end, following the eyes.
Her gaze: for the first 5.6 seconds the eyes are lowered inside that raised head — lids heavy and half-closed, pupils down toward the tabletop, unfocused. This is a downward gaze, not a downward head. When the eyes come up they travel first, the lids opening as the pupils rise, and the head turns a beat later to follow. Real ocular and cervical sequencing.
Her lean: the movement is a hip hinge, not a slide forward on the seat. The lumbar spine stays long, the shoulders come forward with the ribcage, the head stays up on top of the spine, and the weight transfers from the chair back onto the forearms on the table. It happens at real human speed, with a small settle at the end as the weight finds the table. She does not slump, does not lurch, does not push the chair back, does not stand.
Her right arm and hand: flat on the table, palm down, fingers straight and together, in contact with the surface from the first frame to the last. It does not lift, slide, curl, spread or tense at any point — it only takes weight as she leans in.
Her left arm: comes up from below the table with real weight and real joint limits — shoulder, elbow, wrist in sequence. The forearm makes contact with the tabletop and settles, the hand finding its own resting position rather than being placed. Slight asymmetry with the right arm. No slap, no slam, no deliberate placement, no gesture. Once settled it stays still.
Sequencing: torso, then arm, then eyes, then a small head turn — overlapping rather than separate beats, so it reads as one continuous natural movement and not four actions in a row.
Cigarette burn: visibly shorter by the end. Ash accumulates and curls but does not fall within the 10 seconds. The ember does not brighten — there is no drag in this shot.
Smoke: real physical smoke, and the only large moving element in a locked frame. Laminar ribbon from the resting cigarette, breaking into slow turbulence above the tip. The turn disturbs the standing smoke column slightly — it bends and re-forms with real inertia. Slow, heavy. Genuine physical volume, never CG particles, never faster than still indoor air allows. Smoke never reaches the table or drifts across the device.
The device: a solid inert object with real weight, resting flat on the tabletop and in contact with it. Absolutely motionless for all 10 seconds — it does not slide, tip, rotate, vibrate, wake, glow, flicker or change state. Its screen stays dark and dead throughout, showing only the small pale icon as a printed-looking mark, never as a lit display. Nobody touches it, picks it up, points at it or looks at it. It casts a small soft contact shadow onto the table and its metal lens ring holds one steady cold specular from the window; both stay constant.

LIGHTING
Cold grey-green ambient from the window wall — the primary and only light source, backlighting the whole room. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change when he turns, no change when her eyes come up.
The window is the brightest zone of the frame, a soft luminous field across the background. The tower block behind the glass is pale, flat, heavily diffused, its window grid barely legible.
Standing at the glass on the left, he reads as a dark shape against that field from behind. After the turn his front faces camera and is lit only by the room's weak bounce off the plaster walls — his face is a darker, softer shape, legible but low-contrast. Do not add a fill or a key for the turn: his face must not brighten when he turns around. Do not crush it to pure black either — the face must stay readable, because it is carrying the shot now that there is no line.
Her side of the room, screen-right, falls into the same cold falloff — she is lit by window light raking in from screen-left across the table, sitting a stop or so darker than him. Because her head is up rather than tipped down, that raking light catches the length of her throat, her jawline, her cheekbone and the bridge of her nose in clean profile from the first frame, while her lowered eyes sit in shadow under the brow. As she leans forward she moves marginally further into the light and the profile sharpens a fraction. Do not add a key or a fill for this — the change comes from her moving through the existing falloff, not from the lighting changing.
That same light picks out the loose strands at her temple, the scratches in the tabletop, the flat of her right hand with its thin silver ring, and, once it arrives, her left forearm.
<<<prop_device>>> is lit only by that window light. Its orange body is the single point of saturated colour in an otherwise cold grey-green frame, but it stays low-key and desaturated by the ambient cast — muted burnt orange, not vivid. Its black glass panel reads as a dark rectangle with a soft sheen. The device emits no light of its own: it is not a practical, it casts no glow onto the table, onto her hands, or into the room, and it never lights her face.
The dark red curtain at the window edge is deeply desaturated — closer to brown-grey than red, low saturation.
Plant, plaster walls, radiator and floor: dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass across the pale field.
The cigarette ember is a small warm point only. It does not illuminate his face or hand. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
THE SHOT HAS NO MUSIC AND NO VOICE. The only sound in the entire 10 seconds is body foley — breath, cloth, cigarette, one footstep shift, one forearm settling, one swallow. Everything between those events is silence.
NOBODY SPEAKS. The shot is silent of voice for its entire 10 seconds. Both characters keep their lips closed and still throughout.
Her starting posture follows <<<image_2>>> exactly: upright, back to the chair, HEAD HIGH with the chin clear of the chest, EYES LOWERED to the tabletop, right forearm flat on the table with the palm down and fingers together, left arm out of view at her side.
Head high and gaze low is the pose. Her head is never tipped down, never bowed, never sunk toward the table at any point in the 10 seconds. The lowered look comes entirely from the eyes.
She begins her response on her own, unprompted — no line and no gesture triggers it. The turn is the only thing that has happened.
When she responds, the eyes rise first inside the already-raised head; the head only turns a few degrees afterward to follow. There is no head lift, because the head is already up.
Her RIGHT forearm is flat on the table with the palm down, fingers straight and together, from the first frame to the last. It never leaves the table.
Her LEFT arm starts down at her side, out of view below the table, and comes up onto the tabletop once only, during her lean, settling naturally beside the right. It does not come up earlier, does not come up twice, and does not go back down.
She leans forward from the hips once, during 0:05.6 to 0:08.6, and stays leaning to the end. She does not sit back again.
<<<image_2>>> supplies her posture, head carriage, eye direction and right arm pose only. Its framing, camera height, lens and shot size must not be reproduced. This shot stays wide.
Blocking follows <<<image_2>>>: <<<char_captain>>> standing at the window on the LEFT of frame, <<<char_wife>>> seated at the table on the RIGHT of frame. Do not flip these positions. Do not swap them at any point.
<<<prop_device>>> sits on the table in the position given by <<<image_1>>>. It is the only object on the table and is never touched by either character.
The device's screen is dark and inert for the entire 10 seconds. It never wakes, never glows, never displays an image, never shows readable text, never blinks, never notifies.
The coloured markers in the blocking reference are annotations only. No red or yellow shape, dot, line, arrow, circle or overlay appears anywhere in the render. Neither character wears red or yellow — costume comes from the character references: he in grey linen over dark, she in a white wrap vest over black. The orange of the device is the only orange in the frame.
Wide shot of the room, tripod, chest height, squared to the window wall — the full geometry of the room and the distance between the two figures legible in one frame for the entire shot.
Zero camera movement for the full 10 seconds — framing pixel-identical from first frame to last, including through the turn.
The window wall runs perfectly parallel to the sensor — transom horizontal, mullions vertical, no perspective skew, no diagonal convergence, no dutch.
He begins with his back to camera, standing at the window, body parallel to the glass. He turns once, head and body together, and remains facing her until the end. He never turns back to the window. He never walks toward her. He never touches her, never touches the device, never touches the glass, never opens the window, never draws the curtain, never sits.
She stays seated at the table for all 10 seconds. She does not stand, does not turn her chair, does not reach for the device, does not touch him. She holds nothing.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass or in the device's screen.
Nothing exists in the room that is not listed in <<<loc_apt_cap>>> plus <<<prop_device>>>: no second screen, no phone, no monitor, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock, no television. Nothing else on the table. Nothing on the sill. No props invented anywhere in frame.
No visible brand marks, logos or legible lettering anywhere, including on the device.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
The cigarette is in his right hand for the entire shot. No drag in this shot. He does not stub it out, does not put it down, does not tap ash, does not flick it away.
Apart from the single turn and her lean, arm and eye movement, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin, fabric or the device.

NEGATIVE — LOCAL LOCKS
NO MUSIC OF ANY KIND, ANYWHERE, AT ANY VOLUME. No score, no underscore, no cue, no theme, no drone, no pad, no sustained tone, no swell, no riser, no sting, no impact, no pulse, no tension bed, no ambient or atmospheric music, no orchestral or synth element, no piano, no strings, no choir. No music at the head or tail of the shot. No music faded in under the silence. No musical reverb tail as texture.
No ambience, no room tone, no atmosphere bed of any kind.
NO DIALOGUE OF ANY KIND. No line, no word, no whisper, no murmur, no name spoken, no vocalisation, no voice-over, no offscreen voice, no subtitle.
NO MOUTH MOVEMENT. Neither character opens their mouth, parts their lips, mouths silently, or shapes a word at any point. No lip-sync of any kind is generated.
No sound shaped like speech: no voiced sigh, no groan, no throat clearing, no intake that reads as the start of a line.
No gesture substituting for the missing line: he does not beckon, does not point, does not raise a hand, does not tilt his head at her, does not shrug.
No chair creak, no device sound, no exterior sound, no building sound.
No camera movement. No push in on either face. No rack focus between them.
No second person beyond the two characters. No reflection of a third figure in the glass.
No red or yellow marker, overlay, dot or annotation anywhere in the render.
No screen light, no glow, no wake, no notification on the device.
No head bow, no chin tuck, no slump, no head lift, no startle, no double-take.
No warm light, no coloured practicals, no lens flare, no rim light.
No CG gloss on skin, fabric, smoke or device. No CG particle smoke.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260829_141043_f528f3dc-616c-4fe3-bca3-1aa3866762ae.mp4)

</details>

<details><summary>v9 · 2026-08-29 14:25:17 · 1 generation(s) · 055_20260829_142517_76eef1dc.md</summary>

````text
SCENE CONTEXT
A man stands at the window of a small apartment, smoking, his back to the room. The woman is seated at the table on the other side of the room, head held high but her eyes cast down, an orange handheld device lying on the table in front of her. He turns — head and body — to face her. Nothing is said. She leans forward, brings her second arm onto the table and raises her eyes to him. One continuous 10-second take, entirely without dialogue and entirely without music.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. Standing at the window on the LEFT of frame, back to camera, shoulders low, weight settled on one leg, a lit cigarette in his right hand. He is a silent character in this shot — he never speaks. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair pulled back into a low loose knot with fine strands escaping at the temple and the nape. White wrap vest with a wide shawl collar over a black t-shirt, dark trousers. A plain thin silver ring on one finger of the right hand. Seated at the round table on the RIGHT of frame, angled roughly three-quarters away from camera. She is a silent character in this shot — she never speaks. She is a living body throughout, never a still figure. 100% matches the reference.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, large window with a dark metal frame and a deep pale sill, cold grey residential tower block filling the glass, heavy dark red curtain hanging at one edge of the window, dark leafy plant against the wall, white radiator low under the window, round pale table with two chairs. Geography, materials and atmosphere only. Nothing in the room beyond what is listed here and the device below.
<<<prop_device>>> — THE ONE OBJECT ON THE TABLE. A small flat handheld device, roughly the size of a phone but thicker and more solid. Matte burnt-orange plastic body with softly rounded corners and a visible seam running around the middle of the casing. The top face is a flush black glass panel, dark and inert, carrying one small pale line-drawn icon near its centre — a simple stylised animal head, a few thin white strokes, no more. A circular camera lens sits in the middle of the front edge, recessed behind a brushed metal ring, dark glass, catching one small cold specular from the window. A small orange loop lug protrudes at one corner of the top edge. No buttons, no ports, no lettering, no branding, no logo, no readable text anywhere on it. 100% matches the reference.
<<<image_1>>> — DEVICE POSITION REFERENCE ONLY. Shows <<<prop_device>>> lying flat on the scratched pale tabletop, screen face up, its lens edge facing outward across the table, roughly at the centre of the table surface and slightly toward the near edge. Use for the device's design, orientation and position on the table only. Do NOT inherit its framing, focal length, shallow depth of field or camera height — this is a wide room shot from the far side of the apartment, not a tabletop close-up.
<<<image_2>>> — WOMAN'S STARTING POSITION REFERENCE. This is her exact posture in the first frame. Read from it and reproduce it:
— She sits upright and settled, back against the chair, shoulders level and relaxed, no slump.
— HEAD HIGH. The head is NOT tipped down toward the table. The neck is long, the chin level or fractionally raised, the head carried upright and composed on top of the spine. The jawline is clear of the chest. Her face is held in clean profile, turned away from camera toward the window side of the room.
— EYES DOWN. Inside that raised head, the gaze is lowered — the eyelids heavy and half-lowered, the pupils cast down toward the tabletop in front of her. She is not looking at anything. The eyes are down, the head is up. That contradiction is the whole point of the pose and must be visible: a woman holding her head up while refusing to look.
— Her RIGHT arm is extended forward from the shoulder and laid along the tabletop, the forearm resting flat on the surface with the elbow off the near edge and the upper arm relaxed. The right hand is flat, palm down, fingers straight and together, lying fully in contact with the table. The thin silver ring is visible on that hand. The arm is relaxed, not braced, not gripping, not clenched.
— Her LEFT arm is down at her side, below the table line, out of view.
This is a POSE, not a freeze. It is the position she holds and returns to while breathing and making the constant small adjustments of a living seated body. Use this image for her posture, head carriage, eye direction and right arm and hand pose only. Do NOT inherit its framing, its camera height, its lens or its shot size — this is a wide room shot from the far side of the apartment, not a profile medium. Do NOT treat it as a still image to be held motionless.
<<<image_3>>> — BLOCKING REFERENCE ONLY. A photograph of the location with the two character positions marked on it: the RED marker is <<<char_captain>>>, standing at the window on the LEFT of frame; the YELLOW marker is <<<char_wife>>>, seated at the table on the RIGHT of frame. Use this image for camera position, room geography and the two standing/seated positions only. The coloured markers are annotations, not objects and not costume — no coloured shape, overlay, line, dot or drawing appears anywhere in the render, and neither character wears red or yellow. Costume comes from the character references.

LOCATION MAP
Wide shot of the whole room, seen from the far side of the apartment looking toward the window wall, matching the camera position of <<<image_3>>>.
Background: the window wall, running parallel to the sensor — flat on, squared, transom horizontal, mullions vertical, no perspective skew, no diagonal convergence. The grey tower block fills the glass, soft, pale, heavily diffused. The pale sill runs straight across. The white radiator sits low beneath it. The heavy dark red curtain hangs as a vertical band at one edge of the window.
Midground-LEFT: <<<char_captain>>> standing at the window, close to the glass, seen from behind — his back to camera, his body squared to the window plane, parallel to it.
Midground-RIGHT: the round pale table with two chairs. <<<char_wife>>> seated at it, angled roughly three-quarters away from camera, in the posture given by <<<image_2>>> — upright, back against the chair, head high, eyes down, right forearm flat on the table, left arm out of view at her side. On the table, and the only thing on the table, <<<prop_device>>> lies flat — screen up, lens edge facing outward, near the centre of the surface and slightly toward the near edge, clear of her hand and never touched. It reads as one small hard orange rectangle against the pale scratched tabletop — the only saturated colour in the frame.
Side wall: plaster, the dark leafy plant against it.
Foreground: bare floor and open room. Empty.
Camera: tripod, chest height, standing back from both figures, squared to the window wall. Mechanically still for the full duration.

FIRST FRAME AND SPATIAL BLOCKING
First frame: the whole room readable in one wide frame. The window wall fills the background across the width of the picture. <<<char_captain>>> stands at the window on the LEFT side of frame, seen from behind, his silhouette dark against the pale glass, body parallel to the window plane, head level, looking out. The lit cigarette is in his right hand at his side, ember live, a thin ribbon of smoke rising past his shoulder into the window light.
<<<char_wife>>> sits at the table in the RIGHT half of frame, midground, in the posture given by <<<image_2>>>: back against the chair, shoulders level, HEAD HIGH and neck long with the chin clear of the chest, EYES LOWERED to the tabletop under heavy half-closed lids, right forearm flat on the table with the palm down and fingers together, left arm out of view at her side. Her head is up and her gaze is down. She does not look defeated; she looks composed and withheld. She is already breathing in the first frame — the chest and shoulder line are mid-cycle, not held.
<<<prop_device>>> lies flat on the table in front of her, small in frame at this wide scale but immediately legible as a hard orange shape against the pale wood. The two are separated by several metres of empty floor. Curtain band at the window edge; plant against the wall; radiator low under the sill. Nothing else on the table, nothing on the sill.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:10.

FORMAT MODE
Single continuous wide take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. Tripod — mechanically still, zero movement. Two figures held in one frame, far apart, for the whole shot. No dialogue and no music anywhere in the shot.

OPTICS
Wide room shot, roughly 55° diagonal field of view — the full geometry of the room legible: floor, walls, the window wall, both figures in their relative positions, her arms on the table, the device. Deep enough focus that both figures, her hands and the device all read clearly; the tower block beyond the glass is soft. Fixed focal length. No focus pull, no rack focus between them, no rack onto the device or onto her hands, no lens breathing, no zoom.

CAMERA
Tripod, head fully clamped, chest height, squared to the window wall.
Zero camera movement for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when he turns and does not react when she leans in.
The window transom, mullions, sill, curtain edge, table position and the device's position on the table remain in identical screen positions from first frame to last, which is the test of whether the lock held.

HER MICRO-LIFE — 0:00 TO 0:05.6
For the first five and a half seconds she does not move her position, but she is never still. The pose holds; the body inside it is alive and working. All of this must be visible at wide scale — it is played in the torso, the shoulders and the throat, where it reads across a room, not in the face, which is too small in frame to carry it.

BREATHING — the primary and most visible sign of life. Her breath is CONTROLLED BUT NOT SUPPRESSED: shallow, a little high in the chest, and audibly irregular in rhythm even though each breath is small. The chest and the upper ribcage lift and settle visibly under the white vest with each cycle, and the near shoulder rises and falls a centimetre or two with it. The collar of the vest shifts against her collarbone as the chest expands.
The rhythm is uneven and never metronomic: two ordinary shallow breaths, then a slightly longer and deeper one that lifts the shoulders a fraction more and releases slowly, then a shorter one. One breath around 0:02.5 catches very slightly at the top — a half-second hesitation before it releases — and the shoulders hold marginally high through it. This is a person managing themselves, not a person at rest.

THE THROAT AND JAW — she swallows once, around 0:03.5, the movement travelling visibly up the throat in profile. The muscles under the jaw tighten and release once, independently of the swallow. The jaw carries a faint standing tension at the hinge that comes and goes.

POSTURAL DRIFT — the constant micro-corrections of a seated body holding an upright position. Her weight redistributes fractionally on the seat twice across the five seconds, the torso settling a few millimetres and finding balance again. The spine lengthens marginally and eases. The near shoulder drops a centimetre once and comes back. None of these move her out of the pose; they are the pose staying alive.

THE HEAD — never locked to the neck. It drifts by millimetres with the breathing, and makes the involuntary corrections of a real neck holding a head upright for a long time. It settles one or two millimetres lower across the five seconds, the small collapse of someone who has been holding a position. Every one of these is small enough that the head stays high and the chin stays clear of the chest.

THE EYES — lowered, but not dead. Under the heavy half-closed lids the pupils make small involuntary drifts across the tabletop, settling and resettling on nothing. She blinks three or four times across the five seconds, irregularly spaced — one slow heavy blink, a long gap, a fast one. The lids never open fully and the gaze never rises before its moment.

THE RIGHT HAND — flat on the table and in contact with it throughout, but the hand is not a prop. The fingers register her breathing very slightly, and once across the five seconds the whole hand settles a millimetre as her weight shifts. It does not lift, slide, curl, spread, tap or tense.

HAIR AND CLOTH — the loose strands at her temple and nape hang as weighted mass and shift very slightly with her head movement and with the air of her own breath. The white vest creases and releases at the shoulder and across the ribs with each breath cycle.

AMPLITUDE — every movement above is small. Millimetres and single centimetres. Nothing reads as a gesture, a fidget, a shift of position or a reaction. A viewer should register her as motionless and alive at the same time: the stillness is what she is doing, and the small movement is what her body is doing underneath it.
SHE IS NEVER FROZEN. There is no frame in the first five and a half seconds in which nothing about her is moving.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window on the left, back to the room, body parallel to the glass. Smoke rises past his shoulder in an unbroken ribbon. One slow shallow breath — the shoulder line barely moves.
She sits at the table on the right in the <<<image_2>>> posture: head high, eyes down, right hand flat on the table, running the micro-life described above — two shallow breaths lifting the chest and the near shoulder, one small postural settle, one slow blink. Her head does not drop and her eyes do not come up.
Several metres of empty floor between them. Nothing else in the room moves.

0:02–0:03.8 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward her across the frame to screen-right. Roughly 160 to 180 degrees of rotation, unhurried, no snap, no aggression. The cigarette stays in his right hand and swings passively with his arm. When the turn completes he is facing her across the room, his front now toward camera and lit only by the window behind him — his face reading as a darker shape against the bright glass, features soft but legible, not a black cut-out. His eyeline runs across the empty floor toward her, passing over the table and the device.
She does not react to the turn and does not look. But her body registers it without her permission: the breath around 0:02.5 catches slightly at the top and the shoulders hold marginally high through it, and she swallows once at 0:03.5. Nothing else changes. She knows he has turned.

0:03.8–0:05.6 — THE SILENCE. He is facing her and he says nothing. His mouth stays closed and completely still. He does not step toward her, does not gesture, does not raise a hand. His arms stay down.
Her head is still up and her eyes are still down. She does not acknowledge him. The micro-life continues underneath — the breathing settling back toward its earlier rhythm but not quite reaching it, one more blink, one small weight shift on the seat, the jaw tightening and releasing once.
This is the longest still beat in the shot and it is entirely empty of event: two people in one room, one facing the other, neither speaking, nothing on the soundtrack but breath. Hold it in full. It is not filled with a line, a sound, a music cue, a gesture or a camera move.

0:05.6–0:08.6 — HER RESPONSE. One continuous movement, unhurried, in this order. She begins it on her own — nothing has been said to her and no gesture has been made. It grows out of the micro-life rather than interrupting it: the first thing that moves is the breath deepening slightly, and the lean starts on that breath.
First her weight comes off the chair back: the pelvis stays where it is and the torso hinges forward from the hips, a small lean of ten or fifteen centimetres toward the table. The white vest shifts against her shoulders as she comes forward. Her right forearm stays exactly where it is, flat on the table, and simply takes some of the new weight — the hand does not slide, lift or curl. Her head stays high through the lean; it does not dip.
As she leans, her left arm comes up from her side and settles onto the tabletop: shoulder, elbow, then forearm arriving flat on the surface, the hand finding its own resting place near the right — not mirrored, not symmetrical, not placed with intent. A body opening up and bracing itself because it is about to face someone.
Last, THE EYES COME UP. Because the head is already high, this is not a head lift — it is the gaze rising inside a head that is already raised. The lids open, the pupils travel up off the tabletop and across the empty floor to him, and only then does the head turn a few degrees toward him to follow the eyeline. The eyes lead, the head follows a fraction behind. It is unhurried and unsurprised. She does not startle, does not snap her head up, and does not double-take.
Neither hand ever touches the device.

0:08.6–0:10 — Both hold. He stands facing her across the empty floor, she sits leaning forward with both forearms on the table, looking back at him. Neither of them speaks, then or at any earlier point. A long slow exhale from him; smoke drifts forward into the room and rises through the window light. His shoulder line lowers two or three centimetres.
She keeps breathing, and now that she is leaning on the table the breath reads differently — the movement travels down through the forearms into the tabletop rather than up through the shoulders. Two shallow cycles across this beat, and one blink. She does not settle into stillness at the end.
The shot ends with the two of them looking at each other across the distance, in silence, the device untouched between them, the room still. No music enters at the end.

DIALOGUE
THERE IS NO DIALOGUE IN THIS SHOT. Not one word is spoken by anyone at any point in the 10 seconds.
<<<char_captain>>> does not speak. His lips stay completely closed and completely still for the entire duration, including through the turn, through the silence after it, and through her response. He does not mouth anything, does not part his lips as if about to speak, does not murmur, does not sigh audibly, does not clear his throat.
<<<char_wife>>> does not speak. Her lips stay completely closed and completely still for the entire duration. Her breathing is nasal throughout and never opens the mouth.
No voice-over. No offscreen voices. No whisper. No vocalisation of any kind from either character. No subtitles, no captions, no on-screen text.

AUDIO — FOLEY ONLY, ZERO MUSIC, ZERO VOICE, ZERO AMBIENCE

NO MUSIC. THIS IS THE FIRST AND MOST IMPORTANT AUDIO INSTRUCTION.
There is no music anywhere in this shot, at any point, at any volume, under any name. Not at the head, not at the tail, not under the turn, not under the silence, not under her lean, not under the final hold. Not faint, not distant, not "barely audible", not buried in the mix.
Specifically forbidden, in every form: score, soundtrack, underscore, cue, theme, motif, melody, harmony, chord, sustained tone, drone, pad, hum, swell, riser, sting, hit, impact, boom, braam, whoosh, sub-bass pulse, heartbeat pulse, ticking, tension bed, suspense bed, emotional bed, ambient music, atmospheric music, cinematic music, trailer sound design, orchestral element, string tone, piano note, synth tone, bass note, choir, vocal pad, reverb tail used as a musical texture, and any pitched sustained sound of any kind.
Do not add music to make the silence feel intentional. Do not add music to support the emotion of the scene. Do not add music because the shot is long and quiet. The absence of music IS the intended effect. The scene must play completely dry.
If a rendering process would normally add a musical bed to a dialogue-free shot, it must not do so here.

THE SOUNDTRACK CONTAINS EXACTLY ONE ELEMENT: close-mic foley generated by the two bodies. There is no voice track, no music track, and no ambience track. When no foley event is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.

The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry
2. Her breath — shallow, controlled, nasal, irregular in rhythm, present throughout the shot; the slight catch at the top of one inhale around 0:02.5; the deeper intake as she begins to lean at 0:05.6
3. Cloth — the shift of linen shirt fabric as his shoulder line settles; one soft rustle through the turn; the light creasing of her white vest with her breathing, and its drag across her shoulders as she leans forward and her left arm comes up
4. Cigarette — a faint dry crackle of burning tobacco; fingers adjusting on the paper
5. Feet — the muted shift of shoe on floor through the turn, very quiet: no hard heel strike, no scuff, no tail
6. Her arm — one soft, low contact sound as her left forearm settles onto the tabletop, dull and dry, no knock, no thud, no scrape
7. Body — one dry swallow from her at 0:03.5, and one from him, close-mic level only

No spoken word, no vocal sound, no breath shaped like a word, no hum, no sigh with voice in it.
The device makes no sound at all. No chime, no beep, no notification, no vibration, no buzz, no hum, no synthetic voice, no processing tone, no click, no electronic sound of any kind at any point.
No chair sound. Her chair does not creak, scrape, shift or move when she breathes or when she leans forward.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No foley for objects not present.
Despite the wide framing, the mix stays close and dry: no room reverb, no distance perspective, no reflections off the walls, no spatialization.

PHYSICS
NEITHER FIGURE IS EVER FROZEN. Both bodies obey real anatomy, real joint limits, real muscle sequencing and real speed, and both are breathing and micro-adjusting continuously from the first frame to the last. Stillness in this shot means restrained, never motionless. No mannequin pose, no held still-image moment, no waxwork figure, no locked torso on either character.

The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
Standing posture: weight on one leg, pelvis tilted, opposite shoulder marginally lower. Continuous micro-postural sway and the small balance corrections of a man standing in one place. No rocking, no swaying, no pacing.
His face after the turn: still and closed. The jaw does not move, the lips do not part, the mouth does not shape anything. Whatever is happening is happening behind the face. Blinking is irregular and natural.

HER BREATHING: shallow and controlled but genuinely visible at wide scale. The chest and upper ribcage lift and settle under the vest, the near shoulder rising and falling a centimetre or two with each cycle, the vest creasing and releasing at the shoulder and across the ribs. The rhythm is irregular — the intervals between breaths are never equal, the depth varies cycle to cycle, and one inhale catches slightly at the top. Nasal throughout; the mouth never opens. The breathing continues through the turn, through the silence, through the lean and through the final hold — it never stops and never becomes regular.
HER POSTURAL LIFE: continuous small corrections of a seated body — the weight redistributing on the seat, the spine lengthening and easing, the near shoulder dropping and returning, the head drifting by millimetres on the neck and settling fractionally lower across the shot. All in millimetres and single centimetres, none of it reading as a gesture or a shift of position.
Her head carriage: the head stays high for the entire 10 seconds. The cervical spine is long and the chin stays clear of the chest at all times. She never drops her head, never tucks her chin, never lets the head sink toward the table. The only deliberate head movement in the shot is a small turn of a few degrees toward him at the very end, following the eyes.
Her gaze: for the first 5.6 seconds the eyes are lowered inside that raised head — lids heavy and half-closed, pupils down toward the tabletop, drifting slightly and unfocused, blinking irregularly. This is a downward gaze, not a downward head. When the eyes come up they travel first, the lids opening as the pupils rise, and the head turns a beat later to follow. Real ocular and cervical sequencing.
Her lean: the movement is a hip hinge, not a slide forward on the seat. It begins on a deeper inhale, growing out of the breathing rather than starting from stillness. The lumbar spine stays long, the shoulders come forward with the ribcage, the head stays up on top of the spine, and the weight transfers from the chair back onto the forearms on the table. It happens at real human speed, with a small settle at the end as the weight finds the table. She does not slump, does not lurch, does not push the chair back, does not stand.
Her right arm and hand: flat on the table, palm down, fingers straight and together, in contact with the surface from the first frame to the last. It registers her breathing very slightly and settles once with a weight shift, but it does not lift, slide, curl, spread, tap or tense at any point — it only takes weight as she leans in.
Her left arm: comes up from below the table with real weight and real joint limits — shoulder, elbow, wrist in sequence. The forearm makes contact with the tabletop and settles, the hand finding its own resting position rather than being placed. Slight asymmetry with the right arm. No slap, no slam, no deliberate placement, no gesture. Once settled it stays still, apart from the faint transmission of her breathing through the forearm.
Sequencing: breath, then torso, then arm, then eyes, then a small head turn — overlapping rather than separate beats, so it reads as one continuous natural movement and not five actions in a row.
Her hair: the loose strands at temple and nape hang as weighted mass, shifting slightly with her head movement and with her own breath, and settling after the lean.
Cigarette burn: visibly shorter by the end. Ash accumulates and curls but does not fall within the 10 seconds. The ember does not brighten — there is no drag in this shot.
Smoke: real physical smoke, and the only large moving element in a locked frame. Laminar ribbon from the resting cigarette, breaking into slow turbulence above the tip. The turn disturbs the standing smoke column slightly — it bends and re-forms with real inertia. Slow, heavy. Genuine physical volume, never CG particles, never faster than still indoor air allows. Smoke never reaches the table or drifts across the device.
The device: a solid inert object with real weight, resting flat on the tabletop and in contact with it. Absolutely motionless for all 10 seconds — it does not slide, tip, rotate, vibrate, wake, glow, flicker or change state. Its screen stays dark and dead throughout, showing only the small pale icon as a printed-looking mark, never as a lit display. Nobody touches it, picks it up, points at it or looks at it. It casts a small soft contact shadow onto the table and its metal lens ring holds one steady cold specular from the window; both stay constant. It is the only genuinely motionless thing in the frame.

LIGHTING
Cold grey-green ambient from the window wall — the primary and only light source, backlighting the whole room. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change when he turns, no change when her eyes come up.
The window is the brightest zone of the frame, a soft luminous field across the background. The tower block behind the glass is pale, flat, heavily diffused, its window grid barely legible.
Standing at the glass on the left, he reads as a dark shape against that field from behind. After the turn his front faces camera and is lit only by the room's weak bounce off the plaster walls — his face is a darker, softer shape, legible but low-contrast. Do not add a fill or a key for the turn: his face must not brighten when he turns around. Do not crush it to pure black either — the face must stay readable, because it is carrying the shot now that there is no line.
Her side of the room, screen-right, falls into the same cold falloff — she is lit by window light raking in from screen-left across the table, sitting a stop or so darker than him. Because her head is up rather than tipped down, that raking light catches the length of her throat, her jawline, her cheekbone and the bridge of her nose in clean profile from the first frame, while her lowered eyes sit in shadow under the brow. The same raking light catches the rise and fall of her chest and shoulder as she breathes, and the shifting creases in the white vest — this is what makes her breathing legible at wide scale. As she leans forward she moves marginally further into the light and the profile sharpens a fraction. Do not add a key or a fill for this — the change comes from her moving through the existing falloff, not from the lighting changing.
That same light picks out the loose strands at her temple, the scratches in the tabletop, the flat of her right hand with its thin silver ring, and, once it arrives, her left forearm.
<<<prop_device>>> is lit only by that window light. Its orange body is the single point of saturated colour in an otherwise cold grey-green frame, but it stays low-key and desaturated by the ambient cast — muted burnt orange, not vivid. Its black glass panel reads as a dark rectangle with a soft sheen. The device emits no light of its own: it is not a practical, it casts no glow onto the table, onto her hands, or into the room, and it never lights her face.
The dark red curtain at the window edge is deeply desaturated — closer to brown-grey than red, low saturation.
Plant, plaster walls, radiator and floor: dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass across the pale field.
The cigarette ember is a small warm point only. It does not illuminate his face or hand. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
BOTH CHARACTERS ARE ALIVE IN EVERY FRAME. She is breathing visibly and micro-adjusting continuously from 0:00, not only from 0:05.6 when she moves. There is no frame in which she is a still image.
Her breathing is legible at wide scale: the chest and near shoulder rise and fall, the vest creases and releases, the rhythm is irregular.
THE SHOT HAS NO MUSIC AND NO VOICE. The only sound in the entire 10 seconds is body foley — breath from both of them, cloth, cigarette, one footstep shift, one forearm settling, two swallows. Everything between those events is silence.
NOBODY SPEAKS. The shot is silent of voice for its entire 10 seconds. Both characters keep their lips closed and still throughout.
Her starting posture follows <<<image_2>>> exactly: upright, back to the chair, HEAD HIGH with the chin clear of the chest, EYES LOWERED to the tabletop, right forearm flat on the table with the palm down and fingers together, left arm out of view at her side. It is a pose she holds while breathing, not a freeze.
Head high and gaze low is the pose. Her head is never tipped down, never bowed, never sunk toward the table at any point in the 10 seconds. The lowered look comes entirely from the eyes.
She begins her response on her own, unprompted — no line and no gesture triggers it. The turn is the only thing that has happened. The lean grows out of a deeper breath rather than starting from stillness.
When she responds, the eyes rise first inside the already-raised head; the head only turns a few degrees afterward to follow. There is no head lift, because the head is already up.
Her RIGHT forearm is flat on the table with the palm down, fingers straight and together, from the first frame to the last. It never leaves the table.
Her LEFT arm starts down at her side, out of view below the table, and comes up onto the tabletop once only, during her lean, settling naturally beside the right. It does not come up earlier, does not come up twice, and does not go back down.
She leans forward from the hips once, during 0:05.6 to 0:08.6, and stays leaning to the end. She does not sit back again.
<<<image_2>>> supplies her posture, head carriage, eye direction and right arm pose only. Its framing, camera height, lens and shot size must not be reproduced. This shot stays wide.
Blocking follows <<<image_3>>>: <<<char_captain>>> standing at the window on the LEFT of frame, <<<char_wife>>> seated at the table on the RIGHT of frame. Do not flip these positions. Do not swap them at any point.
<<<prop_device>>> sits on the table in the position given by <<<image_1>>>. It is the only object on the table and is never touched by either character.
The device's screen is dark and inert for the entire 10 seconds. It never wakes, never glows, never displays an image, never shows readable text, never blinks, never notifies.
The coloured markers in the blocking reference are annotations only. No red or yellow shape, dot, line, arrow, circle or overlay appears anywhere in the render. Neither character wears red or yellow — costume comes from the character references: he in grey linen over dark, she in a white wrap vest over black. The orange of the device is the only orange in the frame.
Wide shot of the room, tripod, chest height, squared to the window wall — the full geometry of the room and the distance between the two figures legible in one frame for the entire shot.
Zero camera movement for the full 10 seconds — framing pixel-identical from first frame to last, including through the turn.
The window wall runs perfectly parallel to the sensor — transom horizontal, mullions vertical, no perspective skew, no diagonal convergence, no dutch.
He begins with his back to camera, standing at the window, body parallel to the glass. He turns once, head and body together, and remains facing her until the end. He never turns back to the window. He never walks toward her. He never touches her, never touches the device, never touches the glass, never opens the window, never draws the curtain, never sits.
She stays seated at the table for all 10 seconds. She does not stand, does not turn her chair, does not reach for the device, does not touch him. She holds nothing.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass or in the device's screen.
Nothing exists in the room that is not listed in <<<loc_apt_cap>>> plus <<<prop_device>>>: no second screen, no phone, no monitor, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock, no television. Nothing else on the table. Nothing on the sill. No props invented anywhere in frame.
No visible brand marks, logos or legible lettering anywhere, including on the device.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
The cigarette is in his right hand for the entire shot. No drag in this shot. He does not stub it out, does not put it down, does not tap ash, does not flick it away.
Apart from the single turn and her lean, arm and eye movement, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin, fabric or the device.

NEGATIVE — LOCAL LOCKS
NO FROZEN FIGURE. She is not a still image, a photograph, a mannequin or a statue at any point, including the first five seconds. No held frame, no motionless body, no suspended breathing, no waxwork stillness, no paused figure waiting for her cue.
No suppressed or invisible breathing. Her breath must be legible in the chest and shoulder at wide scale, not implied.
No metronomic breathing. No even, mechanical, looping respiratory cycle. No animation loop of any kind on her body.
No fidgeting either: no tapping fingers, no jiggling leg, no touching her hair or face, no adjusting her clothes, no shifting in the chair as a visible action, no looking around the room.
NO MUSIC OF ANY KIND, ANYWHERE, AT ANY VOLUME. No score, no underscore, no cue, no theme, no drone, no pad, no sustained tone, no swell, no riser, no sting, no impact, no pulse, no tension bed, no ambient or atmospheric music, no orchestral or synth element, no piano, no strings, no choir. No music at the head or tail of the shot. No music faded in under the silence. No musical reverb tail as texture.
No ambience, no room tone, no atmosphere bed of any kind.
NO DIALOGUE OF ANY KIND. No line, no word, no whisper, no murmur, no name spoken, no vocalisation, no voice-over, no offscreen voice, no subtitle.
NO MOUTH MOVEMENT. Neither character opens their mouth, parts their lips, mouths silently, or shapes a word at any point. Her breathing is nasal and never opens the mouth. No lip-sync of any kind is generated.
No sound shaped like speech: no voiced sigh, no groan, no throat clearing, no intake that reads as the start of a line.
No gesture substituting for the missing line: he does not beckon, does not point, does not raise a hand, does not tilt his head at her, does not shrug.
No chair creak, no device sound, no exterior sound, no building sound.
No camera movement. No push in on either face. No rack focus between them.
No second person beyond the two characters. No reflection of a third figure in the glass.
No red or yellow marker, overlay, dot or annotation anywhere in the render.
No screen light, no glow, no wake, no notification on the device.
No head bow, no chin tuck, no slump, no head lift, no startle, no double-take.
No warm light, no coloured practicals, no lens flare, no rim light.
No CG gloss on skin, fabric, smoke or device. No CG particle smoke.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260829_142517_76eef1dc-23ed-4a5a-a744-fdc8681006e9.mp4)

</details>

<details><summary>v10 · 2026-09-06 09:51:16 · 1 generation(s) · 061_20260906_095116_10ad2853.md</summary>

````text
SCENE CONTEXT
A man stands at the window of a small apartment, smoking, his back to the room. The woman is seated at the table on the other side of the room, head held high but her eyes cast down, a small orange handheld device lying on the table in front of her. He turns — head and body — to face her. Nothing is said. She leans forward, brings her second arm onto the table and raises her eyes to him. One continuous 10-second take, entirely without dialogue and entirely without music.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. Standing at the window on the LEFT of frame, back to camera, shoulders low, weight settled on one leg, a lit cigarette in his right hand. He is a silent character in this shot — he never speaks. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair pulled back into a low loose knot with fine strands escaping at the temple and the nape. White wrap vest with a wide shawl collar over a black t-shirt, dark trousers. A plain thin silver ring on one finger of the right hand. Seated at the round table on the RIGHT of frame, angled roughly three-quarters away from camera. She is a silent character in this shot — she never speaks. She is a living body throughout, never a still figure. 100% matches the reference.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, large window with a dark metal frame and a deep pale sill, cold grey residential tower block filling the glass, heavy dark red curtain hanging at one edge of the window, dark leafy plant against the wall, white radiator low under the window, round pale table with two chairs. Geography, materials and atmosphere only. Nothing in the room beyond what is listed here and the device below.
<<<image_1>>> — THE ONE OBJECT ON THE TABLE. A SMALL flat handheld device, roughly the size of a phone but thicker and more solid — a palm-sized object, not a large one. Matte burnt-orange plastic body with softly rounded corners and a visible seam running around the middle of the casing. The top face is a flush black glass panel, dark and inert, carrying one small pale line-drawn icon near its centre — a simple stylised animal head, a few thin white strokes, no more. A circular camera lens sits in the middle of the front edge, recessed behind a brushed metal ring, dark glass, catching one small cold specular from the window. A small orange loop lug protrudes at one corner of the top edge. No buttons, no ports, no lettering, no branding, no logo, no readable text anywhere on it. 100% matches the reference.

DEVICE SCALE — CRITICAL
<<<image_1>>> is SMALL. Its scale relative to the table must match <<<image_1>>> exactly: in <<<image_1>>> the device occupies roughly one fifth of the visible width of the round tabletop. It is a compact palm-sized object sitting on a large table — the table dwarfs it. Do NOT enlarge it. Do NOT let it read as a tablet, a book, a large box, or an object that dominates the tabletop. Do NOT scale it up to make it more visible in the wide frame.
At this wide shot size the device is genuinely small in frame — a modest orange rectangle on the pale tabletop, legible as a saturated colour accent but not as a prominent object. That smallness is correct and intended. It must not be compensated for by making it bigger.
Its footprint on the table is a small rectangle. Its thickness is low — it sits close to the tabletop, not standing tall on it.

<<<image_1>>> — DEVICE DESIGN, SCALE AND POSITION REFERENCE ONLY. Shows <<<image_1>>> lying flat on the scratched pale tabletop, screen face up, its lens edge facing outward across the table, roughly at the centre of the table surface and slightly toward the near edge. Use for the device's design, ITS SIZE RELATIVE TO THE TABLE, its orientation and its position on the table. The device's proportion to the tabletop in <<<image_1>>> is the governing reference and must be reproduced exactly. Do NOT inherit its framing, focal length, shallow depth of field or camera height — this is a wide room shot from the far side of the apartment, not a tabletop close-up.

<<<image_2>>> — WOMAN'S STARTING POSITION REFERENCE. This is her exact posture in the first frame. Read from it and reproduce it:
— She sits upright and settled, back against the chair, shoulders level and relaxed, no slump.
— HEAD HIGH. The head is NOT tipped down toward the table. The neck is long, the chin level or fractionally raised, the head carried upright and composed on top of the spine. The jawline is clear of the chest. Her face is held in clean profile, turned away from camera toward the window side of the room.
— EYES DOWN. Inside that raised head, the gaze is lowered — the eyelids heavy and half-lowered, the pupils cast down toward the tabletop in front of her. She is not looking at anything. The eyes are down, the head is up. That contradiction is the whole point of the pose and must be visible: a woman holding her head up while refusing to look.
— Her RIGHT arm is extended forward from the shoulder and laid along the tabletop, the forearm resting flat on the surface with the elbow off the near edge and the upper arm relaxed. The right hand is flat, palm down, fingers straight and together, lying fully in contact with the table. The thin silver ring is visible on that hand. The arm is relaxed, not braced, not gripping, not clenched.
— Her LEFT arm is down at her side, below the table line, out of view.
This is a POSE, not a freeze. It is the position she holds and returns to while breathing and making the constant small adjustments of a living seated body. Use this image for her posture, head carriage, eye direction and right arm and hand pose only. Do NOT inherit its framing, its camera height, its lens or its shot size — this is a wide room shot from the far side of the apartment, not a profile medium. Do NOT treat it as a still image to be held motionless.

<<<image_3>>> — BLOCKING REFERENCE ONLY. A photograph of the location with the two character positions marked on it: the RED marker is <<<char_captain>>>, standing at the window on the LEFT of frame; the YELLOW marker is <<<char_wife>>>, seated at the table on the RIGHT of frame. Use this image for camera position, room geography and the two standing/seated positions only. The coloured markers are annotations, not objects and not costume — no coloured shape, overlay, line, dot or drawing appears anywhere in the render, and neither character wears red or yellow. Costume comes from the character references.

LOCATION MAP
Wide shot of the whole room, seen from the far side of the apartment looking toward the window wall, matching the camera position of <<<image_3>>>.
Background: the window wall, running parallel to the sensor — flat on, squared, transom horizontal, mullions vertical, no perspective skew, no diagonal convergence. The grey tower block fills the glass, soft, pale, heavily diffused. The pale sill runs straight across. The white radiator sits low beneath it. The heavy dark red curtain hangs as a vertical band at one edge of the window.
Midground-LEFT: <<<char_captain>>> standing at the window, close to the glass, seen from behind — his back to camera, his body squared to the window plane, parallel to it.
Midground-RIGHT: the round pale table with two chairs. <<<char_wife>>> seated at it, angled roughly three-quarters away from camera, in the posture given by <<<image_2>>> — upright, back against the chair, head high, eyes down, right forearm flat on the table, left arm out of view at her side. On the table, and the only thing on the table, <<<image_1>>> lies flat — screen up, lens edge facing outward, near the centre of the surface and slightly toward the near edge, clear of her hand and never touched. At its correct small scale it reads as one modest hard orange rectangle against the pale scratched tabletop — the only saturated colour in the frame, and a small one.
Side wall: plaster, the dark leafy plant against it.
Foreground: bare floor and open room. Empty.
Camera: tripod, chest height, standing back from both figures, squared to the window wall. Mechanically still for the full duration.

FIRST FRAME AND SPATIAL BLOCKING
First frame: the whole room readable in one wide frame. The window wall fills the background across the width of the picture. <<<char_captain>>> stands at the window on the LEFT side of frame, seen from behind, his silhouette dark against the pale glass, body parallel to the window plane, head level, looking out. The lit cigarette is in his right hand at his side, ember live, a thin ribbon of smoke rising past his shoulder into the window light.
<<<char_wife>>> sits at the table in the RIGHT half of frame, midground, in the posture given by <<<image_2>>>: back against the chair, shoulders level, HEAD HIGH and neck long with the chin clear of the chest, EYES LOWERED to the tabletop under heavy half-closed lids, right forearm flat on the table with the palm down and fingers together, left arm out of view at her side. Her head is up and her gaze is down. She does not look defeated; she looks composed and withheld. She is already breathing in the first frame — the chest and shoulder line are mid-cycle, not held.
<<<image_1>>> lies flat on the table in front of her — SMALL at this wide scale, matching its proportion to the tabletop in <<<image_1>>>, legible as a compact orange shape against the pale wood but not prominent. The two figures are separated by several metres of empty floor. Curtain band at the window edge; plant against the wall; radiator low under the sill. Nothing else on the table, nothing on the sill.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:10.

FORMAT MODE
Single continuous wide take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. Tripod — mechanically still, zero movement. Two figures held in one frame, far apart, for the whole shot. No dialogue and no music anywhere in the shot.

OPTICS
Wide room shot, roughly 55° diagonal field of view — the full geometry of the room legible: floor, walls, the window wall, both figures in their relative positions, her arms on the table, the device. Deep enough focus that both figures, her hands and the device all read clearly; the tower block beyond the glass is soft. Fixed focal length. No focus pull, no rack focus between them, no rack onto the device or onto her hands, no lens breathing, no zoom.

CAMERA
Tripod, head fully clamped, chest height, squared to the window wall.
Zero camera movement for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when he turns and does not react when she leans in.
The window transom, mullions, sill, curtain edge, table position and the device's position on the table remain in identical screen positions from first frame to last, which is the test of whether the lock held.

HER MICRO-LIFE — 0:00 TO 0:05.6
For the first five and a half seconds she does not move her position, but she is never still. The pose holds; the body inside it is alive and working. All of this must be visible at wide scale — it is played in the torso, the shoulders and the throat, where it reads across a room, not in the face, which is too small in frame to carry it.

BREATHING — the primary and most visible sign of life. Her breath is CONTROLLED BUT NOT SUPPRESSED: shallow, a little high in the chest, and audibly irregular in rhythm even though each breath is small. The chest and the upper ribcage lift and settle visibly under the white vest with each cycle, and the near shoulder rises and falls a centimetre or two with it. The collar of the vest shifts against her collarbone as the chest expands.
The rhythm is uneven and never metronomic: two ordinary shallow breaths, then a slightly longer and deeper one that lifts the shoulders a fraction more and releases slowly, then a shorter one. One breath around 0:02.5 catches very slightly at the top — a half-second hesitation before it releases — and the shoulders hold marginally high through it. This is a person managing themselves, not a person at rest.

THE THROAT AND JAW — she swallows once, around 0:03.5, the movement travelling visibly up the throat in profile. The muscles under the jaw tighten and release once, independently of the swallow. The jaw carries a faint standing tension at the hinge that comes and goes.

POSTURAL DRIFT — the constant micro-corrections of a seated body holding an upright position. Her weight redistributes fractionally on the seat twice across the five seconds, the torso settling a few millimetres and finding balance again. The spine lengthens marginally and eases. The near shoulder drops a centimetre once and comes back. None of these move her out of the pose; they are the pose staying alive.

THE HEAD — never locked to the neck. It drifts by millimetres with the breathing, and makes the involuntary corrections of a real neck holding a head upright for a long time. It settles one or two millimetres lower across the five seconds, the small collapse of someone who has been holding a position. Every one of these is small enough that the head stays high and the chin stays clear of the chest.

THE EYES — lowered, but not dead. Under the heavy half-closed lids the pupils make small involuntary drifts across the tabletop, settling and resettling on nothing. She blinks three or four times across the five seconds, irregularly spaced — one slow heavy blink, a long gap, a fast one. The lids never open fully and the gaze never rises before its moment.

THE RIGHT HAND — flat on the table and in contact with it throughout, but the hand is not a prop. The fingers register her breathing very slightly, and once across the five seconds the whole hand settles a millimetre as her weight shifts. It does not lift, slide, curl, spread, tap or tense.

HAIR AND CLOTH — the loose strands at her temple and nape hang as weighted mass and shift very slightly with her head movement and with the air of her own breath. The white vest creases and releases at the shoulder and across the ribs with each breath cycle.

AMPLITUDE — every movement above is small. Millimetres and single centimetres. Nothing reads as a gesture, a fidget, a shift of position or a reaction. A viewer should register her as motionless and alive at the same time: the stillness is what she is doing, and the small movement is what her body is doing underneath it.
SHE IS NEVER FROZEN. There is no frame in the first five and a half seconds in which nothing about her is moving.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window on the left, back to the room, body parallel to the glass. Smoke rises past his shoulder in an unbroken ribbon. One slow shallow breath — the shoulder line barely moves.
She sits at the table on the right in the <<<image_2>>> posture: head high, eyes down, right hand flat on the table, running the micro-life described above — two shallow breaths lifting the chest and the near shoulder, one small postural settle, one slow blink. Her head does not drop and her eyes do not come up.
Several metres of empty floor between them. Nothing else in the room moves.

0:02–0:03.8 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward her across the frame to screen-right. Roughly 160 to 180 degrees of rotation, unhurried, no snap, no aggression. The cigarette stays in his right hand and swings passively with his arm. When the turn completes he is facing her across the room, his front now toward camera and lit only by the window behind him — his face reading as a darker shape against the bright glass, features soft but legible, not a black cut-out. His eyeline runs across the empty floor toward her, passing over the table and the device.
She does not react to the turn and does not look. But her body registers it without her permission: the breath around 0:02.5 catches slightly at the top and the shoulders hold marginally high through it, and she swallows once at 0:03.5. Nothing else changes. She knows he has turned.

0:03.8–0:05.6 — THE SILENCE. He is facing her and he says nothing. His mouth stays closed and completely still. He does not step toward her, does not gesture, does not raise a hand. His arms stay down.
Her head is still up and her eyes are still down. She does not acknowledge him. The micro-life continues underneath — the breathing settling back toward its earlier rhythm but not quite reaching it, one more blink, one small weight shift on the seat, the jaw tightening and releasing once.
This is the longest still beat in the shot and it is entirely empty of event: two people in one room, one facing the other, neither speaking, nothing on the soundtrack but breath. Hold it in full. It is not filled with a line, a sound, a music cue, a gesture or a camera move.

0:05.6–0:08.6 — HER RESPONSE. One continuous movement, unhurried, in this order. She begins it on her own — nothing has been said to her and no gesture has been made. It grows out of the micro-life rather than interrupting it: the first thing that moves is the breath deepening slightly, and the lean starts on that breath.
First her weight comes off the chair back: the pelvis stays where it is and the torso hinges forward from the hips, a small lean of ten or fifteen centimetres toward the table. The white vest shifts against her shoulders as she comes forward. Her right forearm stays exactly where it is, flat on the table, and simply takes some of the new weight — the hand does not slide, lift or curl. Her head stays high through the lean; it does not dip.
As she leans, her left arm comes up from her side and settles onto the tabletop: shoulder, elbow, then forearm arriving flat on the surface, the hand finding its own resting place near the right — not mirrored, not symmetrical, not placed with intent. A body opening up and bracing itself because it is about to face someone.
Last, THE EYES COME UP. Because the head is already high, this is not a head lift — it is the gaze rising inside a head that is already raised. The lids open, the pupils travel up off the tabletop and across the empty floor to him, and only then does the head turn a few degrees toward him to follow the eyeline. The eyes lead, the head follows a fraction behind. It is unhurried and unsurprised. She does not startle, does not snap her head up, and does not double-take.
Neither hand ever touches the device.

0:08.6–0:10 — Both hold. He stands facing her across the empty floor, she sits leaning forward with both forearms on the table, looking back at him. Neither of them speaks, then or at any earlier point. A long slow exhale from him; smoke drifts forward into the room and rises through the window light. His shoulder line lowers two or three centimetres.
She keeps breathing, and now that she is leaning on the table the breath reads differently — the movement travels down through the forearms into the tabletop rather than up through the shoulders. Two shallow cycles across this beat, and one blink. She does not settle into stillness at the end.
The shot ends with the two of them looking at each other across the distance, in silence, the device untouched between them, the room still. No music enters at the end.

DIALOGUE
THERE IS NO DIALOGUE IN THIS SHOT. Not one word is spoken by anyone at any point in the 10 seconds.
<<<char_captain>>> does not speak. His lips stay completely closed and completely still for the entire duration, including through the turn, through the silence after it, and through her response. He does not mouth anything, does not part his lips as if about to speak, does not murmur, does not sigh audibly, does not clear his throat.
<<<char_wife>>> does not speak. Her lips stay completely closed and completely still for the entire duration. Her breathing is nasal throughout and never opens the mouth.
No voice-over. No offscreen voices. No whisper. No vocalisation of any kind from either character. No subtitles, no captions, no on-screen text.

AUDIO — FOLEY ONLY, ZERO MUSIC, ZERO VOICE, ZERO AMBIENCE

NO MUSIC. THIS IS THE FIRST AND MOST IMPORTANT AUDIO INSTRUCTION.
There is no music anywhere in this shot, at any point, at any volume, under any name. Not at the head, not at the tail, not under the turn, not under the silence, not under her lean, not under the final hold. Not faint, not distant, not "barely audible", not buried in the mix.
Specifically forbidden, in every form: score, soundtrack, underscore, cue, theme, motif, melody, harmony, chord, sustained tone, drone, pad, hum, swell, riser, sting, hit, impact, boom, braam, whoosh, sub-bass pulse, heartbeat pulse, ticking, tension bed, suspense bed, emotional bed, ambient music, atmospheric music, cinematic music, trailer sound design, orchestral element, string tone, piano note, synth tone, bass note, choir, vocal pad, reverb tail used as a musical texture, and any pitched sustained sound of any kind.
Do not add music to make the silence feel intentional. Do not add music to support the emotion of the scene. Do not add music because the shot is long and quiet. The absence of music IS the intended effect. The scene must play completely dry.
If a rendering process would normally add a musical bed to a dialogue-free shot, it must not do so here.

THE SOUNDTRACK CONTAINS EXACTLY ONE ELEMENT: close-mic foley generated by the two bodies. There is no voice track, no music track, and no ambience track. When no foley event is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.

The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry
2. Her breath — shallow, controlled, nasal, irregular in rhythm, present throughout the shot; the slight catch at the top of one inhale around 0:02.5; the deeper intake as she begins to lean at 0:05.6
3. Cloth — the shift of linen shirt fabric as his shoulder line settles; one soft rustle through the turn; the light creasing of her white vest with her breathing, and its drag across her shoulders as she leans forward and her left arm comes up
4. Cigarette — a faint dry crackle of burning tobacco; fingers adjusting on the paper
5. Feet — the muted shift of shoe on floor through the turn, very quiet: no hard heel strike, no scuff, no tail
6. Her arm — one soft, low contact sound as her left forearm settles onto the tabletop, dull and dry, no knock, no thud, no scrape
7. Body — one dry swallow from her at 0:03.5, and one from him, close-mic level only

No spoken word, no vocal sound, no breath shaped like a word, no hum, no sigh with voice in it.
The device makes no sound at all. No chime, no beep, no notification, no vibration, no buzz, no hum, no synthetic voice, no processing tone, no click, no electronic sound of any kind at any point.
No chair sound. Her chair does not creak, scrape, shift or move when she breathes or when she leans forward.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No foley for objects not present.
Despite the wide framing, the mix stays close and dry: no room reverb, no distance perspective, no reflections off the walls, no spatialization.

PHYSICS
NEITHER FIGURE IS EVER FROZEN. Both bodies obey real anatomy, real joint limits, real muscle sequencing and real speed, and both are breathing and micro-adjusting continuously from the first frame to the last. Stillness in this shot means restrained, never motionless. No mannequin pose, no held still-image moment, no waxwork figure, no locked torso on either character.

The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
Standing posture: weight on one leg, pelvis tilted, opposite shoulder marginally lower. Continuous micro-postural sway and the small balance corrections of a man standing in one place. No rocking, no swaying, no pacing.
His face after the turn: still and closed. The jaw does not move, the lips do not part, the mouth does not shape anything. Whatever is happening is happening behind the face. Blinking is irregular and natural.

HER BREATHING: shallow and controlled but genuinely visible at wide scale. The chest and upper ribcage lift and settle under the vest, the near shoulder rising and falling a centimetre or two with each cycle, the vest creasing and releasing at the shoulder and across the ribs. The rhythm is irregular — the intervals between breaths are never equal, the depth varies cycle to cycle, and one inhale catches slightly at the top. Nasal throughout; the mouth never opens. The breathing continues through the turn, through the silence, through the lean and through the final hold — it never stops and never becomes regular.
HER POSTURAL LIFE: continuous small corrections of a seated body — the weight redistributing on the seat, the spine lengthening and easing, the near shoulder dropping and returning, the head drifting by millimetres on the neck and settling fractionally lower across the shot. All in millimetres and single centimetres, none of it reading as a gesture or a shift of position.
Her head carriage: the head stays high for the entire 10 seconds. The cervical spine is long and the chin stays clear of the chest at all times. She never drops her head, never tucks her chin, never lets the head sink toward the table. The only deliberate head movement in the shot is a small turn of a few degrees toward him at the very end, following the eyes.
Her gaze: for the first 5.6 seconds the eyes are lowered inside that raised head — lids heavy and half-closed, pupils down toward the tabletop, drifting slightly and unfocused, blinking irregularly. This is a downward gaze, not a downward head. When the eyes come up they travel first, the lids opening as the pupils rise, and the head turns a beat later to follow. Real ocular and cervical sequencing.
Her lean: the movement is a hip hinge, not a slide forward on the seat. It begins on a deeper inhale, growing out of the breathing rather than starting from stillness. The lumbar spine stays long, the shoulders come forward with the ribcage, the head stays up on top of the spine, and the weight transfers from the chair back onto the forearms on the table. It happens at real human speed, with a small settle at the end as the weight finds the table. She does not slump, does not lurch, does not push the chair back, does not stand.
Her right arm and hand: flat on the table, palm down, fingers straight and together, in contact with the surface from the first frame to the last. It registers her breathing very slightly and settles once with a weight shift, but it does not lift, slide, curl, spread, tap or tense at any point — it only takes weight as she leans in.
Her left arm: comes up from below the table with real weight and real joint limits — shoulder, elbow, wrist in sequence. The forearm makes contact with the tabletop and settles, the hand finding its own resting position rather than being placed. Slight asymmetry with the right arm. No slap, no slam, no deliberate placement, no gesture. Once settled it stays still, apart from the faint transmission of her breathing through the forearm.
Sequencing: breath, then torso, then arm, then eyes, then a small head turn — overlapping rather than separate beats, so it reads as one continuous natural movement and not five actions in a row.
Her hair: the loose strands at temple and nape hang as weighted mass, shifting slightly with her head movement and with her own breath, and settling after the lean.
Cigarette burn: visibly shorter by the end. Ash accumulates and curls but does not fall within the 10 seconds. The ember does not brighten — there is no drag in this shot.
Smoke: real physical smoke, and the only large moving element in a locked frame. Laminar ribbon from the resting cigarette, breaking into slow turbulence above the tip. The turn disturbs the standing smoke column slightly — it bends and re-forms with real inertia. Slow, heavy. Genuine physical volume, never CG particles, never faster than still indoor air allows. Smoke never reaches the table or drifts across the device.
The device: a SMALL solid inert object with real weight, resting flat on the tabletop and in contact with it, at the scale given by <<<image_1>>>. Absolutely motionless for all 10 seconds — it does not slide, tip, rotate, vibrate, wake, glow, flicker or change state. Its screen stays dark and dead throughout, showing only the small pale icon as a printed-looking mark, never as a lit display. Nobody touches it, picks it up, points at it or looks at it. It casts a small soft contact shadow onto the table and its metal lens ring holds one steady cold specular from the window; both stay constant. It is the only genuinely motionless thing in the frame.

LIGHTING
Cold grey-green ambient from the window wall — the primary and only light source, backlighting the whole room. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change when he turns, no change when her eyes come up.
The window is the brightest zone of the frame, a soft luminous field across the background. The tower block behind the glass is pale, flat, heavily diffused, its window grid barely legible.
Standing at the glass on the left, he reads as a dark shape against that field from behind. After the turn his front faces camera and is lit only by the room's weak bounce off the plaster walls — his face is a darker, softer shape, legible but low-contrast. Do not add a fill or a key for the turn: his face must not brighten when he turns around. Do not crush it to pure black either — the face must stay readable, because it is carrying the shot now that there is no line.
Her side of the room, screen-right, falls into the same cold falloff — she is lit by window light raking in from screen-left across the table, sitting a stop or so darker than him. Because her head is up rather than tipped down, that raking light catches the length of her throat, her jawline, her cheekbone and the bridge of her nose in clean profile from the first frame, while her lowered eyes sit in shadow under the brow. The same raking light catches the rise and fall of her chest and shoulder as she breathes, and the shifting creases in the white vest — this is what makes her breathing legible at wide scale. As she leans forward she moves marginally further into the light and the profile sharpens a fraction. Do not add a key or a fill for this — the change comes from her moving through the existing falloff, not from the lighting changing.
That same light picks out the loose strands at her temple, the scratches in the tabletop, the flat of her right hand with its thin silver ring, and, once it arrives, her left forearm.
<<<image_1>>> is lit only by that window light. Its orange body is the single point of saturated colour in an otherwise cold grey-green frame, but it is small and stays low-key and desaturated by the ambient cast — muted burnt orange, not vivid. Its black glass panel reads as a small dark rectangle with a soft sheen. The device emits no light of its own: it is not a practical, it casts no glow onto the table, onto her hands, or into the room, and it never lights her face.
The dark red curtain at the window edge is deeply desaturated — closer to brown-grey than red, low saturation.
Plant, plaster walls, radiator and floor: dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass across the pale field.
The cigarette ember is a small warm point only. It does not illuminate his face or hand. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
<<<image_1>>> IS SMALL — its size relative to the tabletop matches <<<image_1>>> exactly. It occupies roughly one fifth of the visible width of the round table. It is not enlarged, not scaled up for visibility, and never reads as a tablet, a book or a large box. Its smallness in the wide frame is correct and intended.
BOTH CHARACTERS ARE ALIVE IN EVERY FRAME. She is breathing visibly and micro-adjusting continuously from 0:00, not only from 0:05.6 when she moves. There is no frame in which she is a still image.
Her breathing is legible at wide scale: the chest and near shoulder rise and fall, the vest creases and releases, the rhythm is irregular.
THE SHOT HAS NO MUSIC AND NO VOICE. The only sound in the entire 10 seconds is body foley — breath from both of them, cloth, cigarette, one footstep shift, one forearm settling, two swallows. Everything between those events is silence.
NOBODY SPEAKS. The shot is silent of voice for its entire 10 seconds. Both characters keep their lips closed and still throughout.
Her starting posture follows <<<image_2>>> exactly: upright, back to the chair, HEAD HIGH with the chin clear of the chest, EYES LOWERED to the tabletop, right forearm flat on the table with the palm down and fingers together, left arm out of view at her side. It is a pose she holds while breathing, not a freeze.
Head high and gaze low is the pose. Her head is never tipped down, never bowed, never sunk toward the table at any point in the 10 seconds. The lowered look comes entirely from the eyes.
She begins her response on her own, unprompted — no line and no gesture triggers it. The turn is the only thing that has happened. The lean grows out of a deeper breath rather than starting from stillness.
When she responds, the eyes rise first inside the already-raised head; the head only turns a few degrees afterward to follow. There is no head lift, because the head is already up.
Her RIGHT forearm is flat on the table with the palm down, fingers straight and together, from the first frame to the last. It never leaves the table.
Her LEFT arm starts down at her side, out of view below the table, and comes up onto the tabletop once only, during her lean, settling naturally beside the right. It does not come up earlier, does not come up twice, and does not go back down.
She leans forward from the hips once, during 0:05.6 to 0:08.6, and stays leaning to the end. She does not sit back again.
<<<image_2>>> supplies her posture, head carriage, eye direction and right arm pose only. Its framing, camera height, lens and shot size must not be reproduced. This shot stays wide.
Blocking follows <<<image_3>>>: <<<char_captain>>> standing at the window on the LEFT of frame, <<<char_wife>>> seated at the table on the RIGHT of frame. Do not flip these positions. Do not swap them at any point.
<<<image_1>>> sits on the table in the position AND at the scale given by <<<image_1>>>. It is the only object on the table and is never touched by either character.
The device's screen is dark and inert for the entire 10 seconds. It never wakes, never glows, never displays an image, never shows readable text, never blinks, never notifies.
The coloured markers in the blocking reference are annotations only. No red or yellow shape, dot, line, arrow, circle or overlay appears anywhere in the render. Neither character wears red or yellow — costume comes from the character references: he in grey linen over dark, she in a white wrap vest over black. The orange of the device is the only orange in the frame.
Wide shot of the room, tripod, chest height, squared to the window wall — the full geometry of the room and the distance between the two figures legible in one frame for the entire shot.
Zero camera movement for the full 10 seconds — framing pixel-identical from first frame to last, including through the turn.
The window wall runs perfectly parallel to the sensor — transom horizontal, mullions vertical, no perspective skew, no diagonal convergence, no dutch.
He begins with his back to camera, standing at the window, body parallel to the glass. He turns once, head and body together, and remains facing her until the end. He never turns back to the window. He never walks toward her. He never touches her, never touches the device, never touches the glass, never opens the window, never draws the curtain, never sits.
She stays seated at the table for all 10 seconds. She does not stand, does not turn her chair, does not reach for the device, does not touch him. She holds nothing.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass or in the device's screen.
Nothing exists in the room that is not listed in <<<loc_apt_cap>>> plus <<<image_1>>>: no second screen, no phone, no monitor, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock, no television. Nothing else on the table. Nothing on the sill. No props invented anywhere in frame.
No visible brand marks, logos or legible lettering anywhere, including on the device.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
The cigarette is in his right hand for the entire shot. No drag in this shot. He does not stub it out, does not put it down, does not tap ash, does not flick it away.
Apart from the single turn and her lean, arm and eye movement, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin, fabric or the device.

NEGATIVE — LOCAL LOCKS
NO OVERSIZED DEVICE. <<<image_1>>> is never scaled up, never enlarged for legibility, never rendered as a large object on the table. It stays palm-sized, matching <<<image_1>>>'s proportion to the tabletop.
NO FROZEN FIGURE. She is not a still image, a photograph, a mannequin or a statue at any point, including the first five seconds. No held frame, no motionless body, no suspended breathing, no waxwork stillness, no paused figure waiting for her cue.
No suppressed or invisible breathing. Her breath must be legible in the chest and shoulder at wide scale, not implied.
No metronomic breathing. No even, mechanical, looping respiratory cycle. No animation loop of any kind on her body.
No fidgeting either: no tapping fingers, no jiggling leg, no touching her hair or face, no adjusting her clothes, no shifting in the chair as a visible action, no looking around the room.
NO MUSIC OF ANY KIND, ANYWHERE, AT ANY VOLUME. No score, no underscore, no cue, no theme, no drone, no pad, no sustained tone, no swell, no riser, no sting, no impact, no pulse, no tension bed, no ambient or atmospheric music, no orchestral or synth element, no piano, no strings, no choir. No music at the head or tail of the shot. No music faded in under the silence. No musical reverb tail as texture.
No ambience, no room tone, no atmosphere bed of any kind.
NO DIALOGUE OF ANY KIND. No line, no word, no whisper, no murmur, no name spoken, no vocalisation, no voice-over, no offscreen voice, no subtitle.
NO MOUTH MOVEMENT. Neither character opens their mouth, parts their lips, mouths silently, or shapes a word at any point. Her breathing is nasal and never opens the mouth. No lip-sync of any kind is generated.
No sound shaped like speech: no voiced sigh, no groan, no throat clearing, no intake that reads as the start of a line.
No gesture substituting for the missing line: he does not beckon, does not point, does not raise a hand, does not tilt his head at her, does not shrug.
No chair creak, no device sound, no exterior sound, no building sound.
No camera movement. No push in on either face. No rack focus between them.
No second person beyond the two characters. No reflection of a third figure in the glass.
No red or yellow marker, overlay, dot or annotation anywhere in the render.
No screen light, no glow, no wake, no notification on the device.
No head bow, no chin tuck, no slump, no head lift, no startle, no double-take.
No warm light, no coloured practicals, no lens flare, no rim light.
No CG gloss on skin, fabric, smoke or device. No CG particle smoke.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_38JDnD2aJxtjnkHGSvDeUpDsT5p/hf_20260906_095116_10ad2853-8ed2-4fc3-837d-2aff84ca711b.mp4)

</details>

<details><summary>v11 · 2026-09-06 10:01:59 · 1 generation(s) · 062_20260906_100159_62bb7415.md</summary>

````text
SCENE CONTEXT
A man stands at the window of a small apartment, smoking, his back to the room. The woman is seated at the table on the other side of the room, head held high but her eyes cast down, a small orange handheld device lying on the table in front of her. He turns — head and body — to face her. Nothing is said. She leans forward, brings her second arm onto the table and raises her eyes to him. One continuous 10-second take, entirely without dialogue and entirely without music.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. Standing at the window on the LEFT of frame, back to camera, shoulders low, weight settled on one leg, a lit cigarette in his right hand held low at his side. He is a silent character in this shot — he never speaks. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair pulled back into a low loose knot with fine strands escaping at the temple and the nape. White wrap vest with a wide shawl collar over a black t-shirt, dark trousers. A plain thin silver ring on one finger of the right hand. Seated at the round table on the RIGHT of frame, angled roughly three-quarters away from camera. She is a silent character in this shot — she never speaks. She is a living body throughout, never a still figure. 100% matches the reference.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, large window with a dark metal frame and a deep pale sill running the full width of the left and centre of frame, cold grey residential tower block filling the glass, heavy dark red curtain hanging as a vertical band at the right edge of the window, dark leafy plant against the wall behind her, round pale table. Geography, materials and atmosphere only. Nothing in the room beyond what is listed here and the device below.
<<<image_1>>> — THE ONE OBJECT ON THE TABLE. A SMALL flat handheld device, roughly the size of a phone but thicker and more solid — a palm-sized object. Matte burnt-orange plastic body with softly rounded corners and a visible seam running around the middle of the casing. The top face is a flush black glass panel, dark and inert, carrying one small pale line-drawn icon near its centre — a simple stylised animal head, a few thin white strokes, no more. A circular camera lens sits in the middle of the front edge, recessed behind a brushed metal ring, dark glass, catching one small cold specular from the window. A small orange loop lug protrudes at one corner of the top edge. No buttons, no ports, no lettering, no branding, no logo, no readable text anywhere on it. 100% matches the reference.

<<<image_2>>> — MASTER FRAMING AND BLOCKING REFERENCE. This image gives the exact camera position, focal length, shot size, horizon, headroom, and the exact screen positions of both characters, the table, the window, the curtain and the plant. Reproduce it precisely as the first frame of this shot:
— <<<char_captain>>> stands in the LEFT third of frame, seen from behind, body squared to the window plane, head level, looking out. His cigarette is in his right hand, held low and away from his body at hip height, ember live, a thin ribbon of smoke rising past his arm.
— The window wall fills the left and centre of frame, running parallel to the sensor. The dark red curtain hangs as a vertical band at the right edge of the window.
— <<<char_wife>>> sits in the RIGHT third of frame, in clean left profile, back against her chair, head high, eyes lowered. Her right arm extends forward onto the tabletop, forearm flat, palm down, fingers straight and together, silver ring visible.
— The round pale table enters from the bottom of frame and occupies the lower right quadrant, its far edge curving across.
— The plant sits against the wall directly behind her.
— Empty floor and empty table surface separate the two figures across the width of the frame.
Reproduce this framing, these positions, this camera height and this shot size exactly.
DO NOT reproduce the size of the device shown in <<<image_2>>>. In that image the device is rendered too large. Its correct scale is given separately below and by <<<image_1>>>. Everything else in <<<image_2>>> is correct and is to be matched.

<<<image_1>>> — DEVICE DESIGN, SCALE AND POSITION REFERENCE ONLY. Shows <<<image_1>>> lying flat on the scratched pale tabletop, screen face up, its lens edge facing outward across the table. Use for the device's design, ITS SIZE RELATIVE TO THE TABLE, and its orientation. The device's proportion to the tabletop in <<<image_1>>> is the governing reference and must be reproduced exactly. Do NOT inherit its framing, focal length, shallow depth of field or camera height.

DEVICE SCALE — CRITICAL
<<<image_1>>> is SMALL. Its scale relative to the table must match <<<image_1>>>, NOT <<<image_2>>>. In <<<image_1>>> the device occupies roughly one fifth of the visible width of the tabletop — a compact palm-sized object on a large table. The table dwarfs it.
In the wide frame of this shot the device is genuinely small — a modest orange rectangle on the pale tabletop, legible as a saturated colour accent but never prominent. That smallness is correct and intended and must not be compensated for by scaling it up. Do NOT let it read as a tablet, a book, a large box or an object that dominates the tabletop. Its footprint is a small rectangle and its thickness is low — it sits close to the surface, not standing tall on it.
Its position: lying flat on the table between the two figures, screen up, lens edge facing outward, roughly at the centre of the visible tabletop and clear of her hand. It is never touched.

LOCATION MAP
Wide shot of the room, camera position and framing exactly as <<<image_2>>>.
Background: the window wall running parallel to the sensor — flat on, squared, transom horizontal, mullions vertical, no perspective skew, no diagonal convergence. The grey tower block fills the glass, soft, pale, heavily diffused. The pale sill runs straight across beneath it.
LEFT third: <<<char_captain>>> standing at the window, close to the glass, seen from behind, body parallel to the window plane.
CENTRE: the window, the sill, the dark red curtain band at its right edge, empty wall.
RIGHT third: <<<char_wife>>> seated at the round table in clean left profile, the plant on the wall behind her.
LOWER RIGHT: the round pale table entering from the bottom of frame, its far edge curving across. <<<image_1>>> lying flat on it at its correct small scale — the only object on the table.
Camera: tripod, chest height, squared to the window wall, at the exact position given by <<<image_2>>>. Mechanically still for the full duration.

FIRST FRAME AND SPATIAL BLOCKING
First frame: exactly <<<image_2>>>, with <<<image_1>>> reduced to its correct small scale.
<<<char_captain>>> in the left third, seen from behind, dark against the pale window field, cigarette low in his right hand, smoke rising in a thin ribbon.
<<<char_wife>>> in the right third in clean left profile: back against the chair, shoulders level, HEAD HIGH with the neck long and the chin clear of the chest, EYES LOWERED to the tabletop under heavy half-closed lids. Her head is up and her gaze is down — that contradiction is the pose and must be visible. Right forearm flat on the table, palm down, fingers straight and together, silver ring catching the light. Left arm down at her side, below the table line, out of view.
She does not look defeated; she looks composed and withheld. She is already breathing in the first frame — the chest and shoulder line are mid-cycle, not held.
<<<image_1>>> small on the table between them. Nothing else on the table. Nothing on the sill.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:10.

FORMAT MODE
Single continuous wide take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. Tripod — mechanically still, zero movement. Two figures held in one frame, far apart, for the whole shot. No dialogue and no music anywhere in the shot.

OPTICS
Focal length and field of view exactly as <<<image_2>>> — the full geometry of the room legible: the window wall, both figures in their relative positions, her arm on the table, the device. Deep enough focus that both figures, her hands and the device all read clearly; the tower block beyond the glass is soft. Fixed focal length. No focus pull, no rack focus between them, no rack onto the device or onto her hands, no lens breathing, no zoom.

CAMERA
Tripod, head fully clamped, chest height, squared to the window wall.
Zero camera movement for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when he turns and does not react when she leans in.
The window transom, mullions, sill, curtain edge, table position and the device's position on the table remain in identical screen positions from first frame to last, which is the test of whether the lock held.

HER MICRO-LIFE — 0:00 TO 0:05.6
For the first five and a half seconds she does not move her position, but she is never still. The pose holds; the body inside it is alive and working. All of this must be visible at this shot size — it is played in the torso, the shoulders and the throat, where it reads across a room, not in the face.

BREATHING — the primary and most visible sign of life. Her breath is CONTROLLED BUT NOT SUPPRESSED: shallow, a little high in the chest, and irregular in rhythm even though each breath is small. The chest and upper ribcage lift and settle visibly under the white vest with each cycle, and the near shoulder rises and falls a centimetre or two with it. The collar of the vest shifts against her collarbone as the chest expands.
The rhythm is uneven and never metronomic: two ordinary shallow breaths, then a slightly longer and deeper one that lifts the shoulders a fraction more and releases slowly, then a shorter one. One breath around 0:02.5 catches very slightly at the top — a half-second hesitation before it releases — and the shoulders hold marginally high through it. This is a person managing themselves, not a person at rest.

THE THROAT AND JAW — she swallows once, around 0:03.5, the movement travelling visibly up the throat in profile. The muscles under the jaw tighten and release once, independently of the swallow. The jaw carries a faint standing tension at the hinge that comes and goes.

POSTURAL DRIFT — the constant micro-corrections of a seated body holding an upright position. Her weight redistributes fractionally on the seat twice across the five seconds, the torso settling a few millimetres and finding balance again. The spine lengthens marginally and eases. The near shoulder drops a centimetre once and comes back. None of these move her out of the pose; they are the pose staying alive.

THE HEAD — never locked to the neck. It drifts by millimetres with the breathing and makes the involuntary corrections of a real neck holding a head upright. It settles one or two millimetres lower across the five seconds. Every one of these is small enough that the head stays high and the chin stays clear of the chest.

THE EYES — lowered, but not dead. Under the heavy half-closed lids the pupils make small involuntary drifts across the tabletop, settling and resettling on nothing. She blinks three or four times across the five seconds, irregularly spaced — one slow heavy blink, a long gap, a fast one. The lids never open fully and the gaze never rises before its moment.

THE RIGHT HAND — flat on the table and in contact with it throughout, but the hand is not a prop. The fingers register her breathing very slightly, and once across the five seconds the whole hand settles a millimetre as her weight shifts. It does not lift, slide, curl, spread, tap or tense.

HAIR AND CLOTH — the loose strands at her temple and nape hang as weighted mass and shift very slightly with her head movement and with the air of her own breath. The white vest creases and releases at the shoulder and across the ribs with each breath cycle.

AMPLITUDE — every movement above is small. Millimetres and single centimetres. Nothing reads as a gesture, a fidget, a shift of position or a reaction. A viewer should register her as motionless and alive at the same time.
SHE IS NEVER FROZEN. There is no frame in the first five and a half seconds in which nothing about her is moving.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window in the left third, back to the room, body parallel to the glass. Smoke rises past his arm in an unbroken ribbon. One slow shallow breath — the shoulder line barely moves.
She sits at the table in the right third in the <<<image_2>>> posture: head high, eyes down, right hand flat on the table, running the micro-life described above — two shallow breaths lifting the chest and near shoulder, one small postural settle, one slow blink. Her head does not drop and her eyes do not come up.
The width of the frame separates them. Nothing else in the room moves.

0:02–0:03.8 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward her across the frame to screen-right. Roughly 160 to 180 degrees of rotation, unhurried, no snap, no aggression. The cigarette stays in his right hand and swings passively with his arm. When the turn completes he is facing her across the room, his front now toward camera and lit only by the window behind him — his face reading as a darker shape against the bright glass, features soft but legible, not a black cut-out. His eyeline runs across the empty floor toward her, passing over the table and the device.
She does not react to the turn and does not look. But her body registers it without her permission: the breath around 0:02.5 catches slightly at the top and the shoulders hold marginally high through it, and she swallows once at 0:03.5. Nothing else changes. She knows he has turned.

0:03.8–0:05.6 — THE SILENCE. He is facing her and he says nothing. His mouth stays closed and completely still. He does not step toward her, does not gesture, does not raise a hand. His arms stay down.
Her head is still up and her eyes are still down. She does not acknowledge him. The micro-life continues underneath — the breathing settling back toward its earlier rhythm but not quite reaching it, one more blink, one small weight shift on the seat, the jaw tightening and releasing once.
This is the longest still beat in the shot and it is entirely empty of event. Hold it in full. It is not filled with a line, a sound, a music cue, a gesture or a camera move.

0:05.6–0:08.6 — HER RESPONSE. One continuous movement, unhurried, in this order. She begins it on her own — nothing has been said to her and no gesture has been made. It grows out of the micro-life rather than interrupting it: the first thing that moves is the breath deepening slightly, and the lean starts on that breath.
First her weight comes off the chair back: the pelvis stays where it is and the torso hinges forward from the hips, a small lean of ten or fifteen centimetres toward the table. The white vest shifts against her shoulders as she comes forward. Her right forearm stays exactly where it is, flat on the table, and simply takes some of the new weight — the hand does not slide, lift or curl. Her head stays high through the lean; it does not dip.
As she leans, her left arm comes up from her side and settles onto the tabletop: shoulder, elbow, then forearm arriving flat on the surface, the hand finding its own resting place near the right — not mirrored, not symmetrical, not placed with intent. A body opening up and bracing itself because it is about to face someone.
Last, THE EYES COME UP. Because the head is already high, this is not a head lift — it is the gaze rising inside a head that is already raised. The lids open, the pupils travel up off the tabletop and across the empty floor to him, and only then does the head turn a few degrees toward him to follow the eyeline. The eyes lead, the head follows a fraction behind. It is unhurried and unsurprised. She does not startle, does not snap her head up, and does not double-take.
Neither hand ever touches the device.

0:08.6–0:10 — Both hold. He stands facing her across the empty floor, she sits leaning forward with both forearms on the table, looking back at him. Neither of them speaks, then or at any earlier point. A long slow exhale from him; smoke drifts forward into the room and rises through the window light. His shoulder line lowers two or three centimetres.
She keeps breathing, and now that she is leaning on the table the breath reads differently — the movement travels down through the forearms into the tabletop rather than up through the shoulders. Two shallow cycles across this beat, and one blink. She does not settle into stillness at the end.
The shot ends with the two of them looking at each other across the distance, in silence, the device untouched between them, the room still. No music enters at the end.

DIALOGUE
THERE IS NO DIALOGUE IN THIS SHOT. Not one word is spoken by anyone at any point in the 10 seconds.
<<<char_captain>>> does not speak. His lips stay completely closed and completely still for the entire duration, including through the turn, through the silence after it, and through her response. He does not mouth anything, does not part his lips as if about to speak, does not murmur, does not sigh audibly, does not clear his throat.
<<<char_wife>>> does not speak. Her lips stay completely closed and completely still for the entire duration. Her breathing is nasal throughout and never opens the mouth.
No voice-over. No offscreen voices. No whisper. No vocalisation of any kind from either character. No subtitles, no captions, no on-screen text.

AUDIO — FOLEY ONLY, ZERO MUSIC, ZERO VOICE, ZERO AMBIENCE

NO MUSIC. THIS IS THE FIRST AND MOST IMPORTANT AUDIO INSTRUCTION.
There is no music anywhere in this shot, at any point, at any volume, under any name. Not at the head, not at the tail, not under the turn, not under the silence, not under her lean, not under the final hold. Not faint, not distant, not "barely audible", not buried in the mix.
Specifically forbidden, in every form: score, soundtrack, underscore, cue, theme, motif, melody, harmony, chord, sustained tone, drone, pad, hum, swell, riser, sting, hit, impact, boom, braam, whoosh, sub-bass pulse, heartbeat pulse, ticking, tension bed, suspense bed, emotional bed, ambient music, atmospheric music, cinematic music, trailer sound design, orchestral element, string tone, piano note, synth tone, bass note, choir, vocal pad, reverb tail used as a musical texture, and any pitched sustained sound of any kind.
Do not add music to make the silence feel intentional. Do not add music to support the emotion of the scene. Do not add music because the shot is long and quiet. The absence of music IS the intended effect. The scene must play completely dry.

THE SOUNDTRACK CONTAINS EXACTLY ONE ELEMENT: close-mic foley generated by the two bodies. There is no voice track, no music track, and no ambience track. When no foley event is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.

The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry
2. Her breath — shallow, controlled, nasal, irregular in rhythm, present throughout; the slight catch at the top of one inhale around 0:02.5; the deeper intake as she begins to lean at 0:05.6
3. Cloth — the shift of linen shirt fabric as his shoulder line settles; one soft rustle through the turn; the light creasing of her white vest with her breathing, and its drag across her shoulders as she leans forward and her left arm comes up
4. Cigarette — a faint dry crackle of burning tobacco; fingers adjusting on the paper
5. Feet — the muted shift of shoe on floor through the turn, very quiet: no hard heel strike, no scuff, no tail
6. Her arm — one soft, low contact sound as her left forearm settles onto the tabletop, dull and dry, no knock, no thud, no scrape
7. Body — one dry swallow from her at 0:03.5, and one from him, close-mic level only

No spoken word, no vocal sound, no breath shaped like a word, no hum, no sigh with voice in it.
The device makes no sound at all. No chime, no beep, no notification, no vibration, no buzz, no hum, no synthetic voice, no processing tone, no click, no electronic sound of any kind at any point.
No chair sound. Her chair does not creak, scrape, shift or move when she breathes or when she leans forward.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No foley for objects not present.
Despite the wide framing, the mix stays close and dry: no room reverb, no distance perspective, no reflections off the walls, no spatialization.

PHYSICS
NEITHER FIGURE IS EVER FROZEN. Both bodies obey real anatomy, real joint limits, real muscle sequencing and real speed, and both are breathing and micro-adjusting continuously from the first frame to the last. Stillness in this shot means restrained, never motionless. No mannequin pose, no held still-image moment, no waxwork figure, no locked torso on either character.

The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
Standing posture: weight on one leg, pelvis tilted, opposite shoulder marginally lower. Continuous micro-postural sway and the small balance corrections of a man standing in one place. No rocking, no swaying, no pacing.
His face after the turn: still and closed. The jaw does not move, the lips do not part, the mouth does not shape anything. Whatever is happening is happening behind the face. Blinking is irregular and natural.

HER BREATHING: shallow and controlled but genuinely visible at this shot size. The chest and upper ribcage lift and settle under the vest, the near shoulder rising and falling a centimetre or two with each cycle, the vest creasing and releasing at the shoulder and across the ribs. The rhythm is irregular — the intervals between breaths are never equal, the depth varies cycle to cycle, and one inhale catches slightly at the top. Nasal throughout; the mouth never opens. The breathing continues through the turn, through the silence, through the lean and through the final hold — it never stops and never becomes regular.
HER POSTURAL LIFE: continuous small corrections of a seated body — the weight redistributing on the seat, the spine lengthening and easing, the near shoulder dropping and returning, the head drifting by millimetres on the neck. All in millimetres and single centimetres, none of it reading as a gesture.
Her head carriage: the head stays high for the entire 10 seconds. The cervical spine is long and the chin stays clear of the chest at all times. She never drops her head, never tucks her chin, never lets the head sink toward the table. The only deliberate head movement in the shot is a small turn of a few degrees toward him at the very end, following the eyes.
Her gaze: for the first 5.6 seconds the eyes are lowered inside that raised head — lids heavy and half-closed, pupils down toward the tabletop, drifting slightly and unfocused, blinking irregularly. This is a downward gaze, not a downward head. When the eyes come up they travel first, the lids opening as the pupils rise, and the head turns a beat later to follow.
Her lean: a hip hinge, not a slide forward on the seat. It begins on a deeper inhale, growing out of the breathing rather than starting from stillness. The lumbar spine stays long, the shoulders come forward with the ribcage, the head stays up on top of the spine, and the weight transfers from the chair back onto the forearms on the table. Real human speed, with a small settle at the end as the weight finds the table. She does not slump, does not lurch, does not push the chair back, does not stand.
Her right arm and hand: flat on the table, palm down, fingers straight and together, in contact with the surface from the first frame to the last. It registers her breathing very slightly and settles once with a weight shift, but it does not lift, slide, curl, spread, tap or tense at any point — it only takes weight as she leans in.
Her left arm: comes up from below the table with real weight and real joint limits — shoulder, elbow, wrist in sequence. The forearm makes contact with the tabletop and settles, the hand finding its own resting position rather than being placed. Slight asymmetry with the right arm. No slap, no slam, no deliberate placement, no gesture.
Sequencing: breath, then torso, then arm, then eyes, then a small head turn — overlapping rather than separate beats, so it reads as one continuous natural movement and not five actions in a row.
Her hair: the loose strands at temple and nape hang as weighted mass, shifting slightly with her head movement and with her own breath, and settling after the lean.
Cigarette burn: visibly shorter by the end. Ash accumulates and curls but does not fall within the 10 seconds. The ember does not brighten — there is no drag in this shot.
Smoke: real physical smoke, and the only large moving element in a locked frame. Laminar ribbon from the resting cigarette, breaking into slow turbulence above the tip. The turn disturbs the standing smoke column slightly — it bends and re-forms with real inertia. Slow, heavy. Genuine physical volume, never CG particles, never faster than still indoor air allows. Smoke never reaches the table or drifts across the device.
The device: a SMALL solid inert object with real weight, resting flat on the tabletop and in contact with it, at the scale given by <<<image_1>>>. Absolutely motionless for all 10 seconds — it does not slide, tip, rotate, vibrate, wake, glow, flicker or change state. Its screen stays dark and dead throughout, showing only the small pale icon as a printed-looking mark, never as a lit display. Nobody touches it, picks it up, points at it or looks at it. It casts a small soft contact shadow onto the table and its metal lens ring holds one steady cold specular from the window; both stay constant.

LIGHTING
Cold grey-green ambient from the window wall — the primary and only light source, backlighting the whole room. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change when he turns, no change when her eyes come up.
The window is the brightest zone of the frame, a soft luminous field across the left and centre. The tower block behind the glass is pale, flat, heavily diffused, its window grid barely legible.
Standing at the glass on the left, he reads as a dark shape against that field from behind. After the turn his front faces camera and is lit only by the room's weak bounce off the plaster walls — his face is a darker, softer shape, legible but low-contrast. Do not add a fill or a key for the turn: his face must not brighten when he turns around. Do not crush it to pure black either — the face must stay readable, because it is carrying the shot now that there is no line.
Her side of the room, screen-right, falls into the same cold falloff — she is lit by window light raking in from screen-left across the table, sitting a stop or so darker than him. Because her head is up rather than tipped down, that raking light catches the length of her throat, her jawline, her cheekbone and the bridge of her nose in clean profile from the first frame, while her lowered eyes sit in shadow under the brow. The same raking light catches the rise and fall of her chest and shoulder as she breathes, and the shifting creases in the white vest — this is what makes her breathing legible at this shot size. As she leans forward she moves marginally further into the light and the profile sharpens a fraction. Do not add a key or a fill for this — the change comes from her moving through the existing falloff, not from the lighting changing.
That same light picks out the loose strands at her temple, the scratches in the tabletop, the flat of her right hand with its thin silver ring, and, once it arrives, her left forearm.
<<<image_1>>> is lit only by that window light. Its orange body is the single point of saturated colour in an otherwise cold grey-green frame, but it is small and stays low-key and desaturated by the ambient cast — muted burnt orange, not vivid. Its black glass panel reads as a small dark rectangle with a soft sheen. The device emits no light of its own: it is not a practical, it casts no glow onto the table, onto her hands, or into the room, and it never lights her face.
The dark red curtain at the window edge is deeply desaturated — closer to brown-grey than red, low saturation.
Plant, plaster walls and floor: dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass against the pale field.
The cigarette ember is a small warm point only. It does not illuminate his face or hand. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
FRAMING AND BLOCKING MATCH <<<image_2>>> EXACTLY — camera position, focal length, shot size, headroom, and the screen positions of both characters, the table, the window, the curtain and the plant. <<<char_captain>>> in the LEFT third, seen from behind at the window. <<<char_wife>>> in the RIGHT third, seated in clean left profile. The table entering from the bottom right. Do not flip these positions. Do not swap them at any point.
<<<image_1>>> IS SMALL — its size relative to the tabletop matches <<<image_1>>>, NOT <<<image_2>>>. The device in <<<image_2>>> is too large and its scale there is explicitly not to be reproduced. It occupies roughly one fifth of the visible width of the tabletop. It is never enlarged for visibility and never reads as a tablet, a book or a large box.
BOTH CHARACTERS ARE ALIVE IN EVERY FRAME. She is breathing visibly and micro-adjusting continuously from 0:00, not only from 0:05.6 when she moves. There is no frame in which she is a still image.
Her breathing is legible at this shot size: the chest and near shoulder rise and fall, the vest creases and releases, the rhythm is irregular.
THE SHOT HAS NO MUSIC AND NO VOICE. The only sound in the entire 10 seconds is body foley — breath from both of them, cloth, cigarette, one footstep shift, one forearm settling, two swallows. Everything between those events is silence.
NOBODY SPEAKS. Both characters keep their lips closed and still throughout.
Head high and gaze low is the pose. Her head is never tipped down, never bowed, never sunk toward the table at any point. The lowered look comes entirely from the eyes.
She begins her response on her own, unprompted — no line and no gesture triggers it. The turn is the only thing that has happened. The lean grows out of a deeper breath rather than starting from stillness.
When she responds, the eyes rise first inside the already-raised head; the head only turns a few degrees afterward to follow. There is no head lift, because the head is already up.
Her RIGHT forearm is flat on the table with the palm down, fingers straight and together, from the first frame to the last. It never leaves the table.
Her LEFT arm starts down at her side, out of view below the table, and comes up onto the tabletop once only, during her lean. It does not come up earlier, does not come up twice, and does not go back down.
She leans forward from the hips once, during 0:05.6 to 0:08.6, and stays leaning to the end. She does not sit back again.
The device's screen is dark and inert for the entire 10 seconds. It never wakes, never glows, never displays an image, never shows readable text, never blinks, never notifies.
Zero camera movement for the full 10 seconds — framing pixel-identical from first frame to last, including through the turn.
The window wall runs perfectly parallel to the sensor — transom horizontal, mullions vertical, no perspective skew, no diagonal convergence, no dutch.
He begins with his back to camera, standing at the window. He turns once, head and body together, and remains facing her until the end. He never turns back to the window. He never walks toward her. He never touches her, never touches the device, never touches the glass, never opens the window, never draws the curtain, never sits.
She stays seated at the table for all 10 seconds. She does not stand, does not turn her chair, does not reach for the device, does not touch him. She holds nothing.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass or in the device's screen.
Nothing exists in the room that is not listed in <<<loc_apt_cap>>> plus <<<image_1>>>: no second screen, no phone, no monitor, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock, no television. Nothing else on the table. Nothing on the sill. No props invented anywhere in frame.
No visible brand marks, logos or legible lettering anywhere, including on the device.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
The cigarette is in his right hand for the entire shot. No drag in this shot. He does not stub it out, does not put it down, does not tap ash, does not flick it away.
Apart from the single turn and her lean, arm and eye movement, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin, fabric or the device.

NEGATIVE — LOCAL LOCKS
NO OVERSIZED DEVICE. <<<image_1>>> is never scaled up, never enlarged for legibility, never rendered at the size shown in <<<image_2>>>. It stays palm-sized, matching <<<image_1>>>'s proportion to the tabletop.
NO FROZEN FIGURE. She is not a still image, a photograph, a mannequin or a statue at any point, including the first five seconds. No held frame, no motionless body, no suspended breathing, no waxwork stillness, no paused figure waiting for her cue.
No suppressed or invisible breathing. Her breath must be legible in the chest and shoulder, not implied.
No metronomic breathing. No even, mechanical, looping respiratory cycle. No animation loop of any kind on her body.
No fidgeting either: no tapping fingers, no jiggling leg, no touching her hair or face, no adjusting her clothes, no shifting in the chair as a visible action, no looking around the room.
NO MUSIC OF ANY KIND, ANYWHERE, AT ANY VOLUME. No score, no underscore, no cue, no theme, no drone, no pad, no sustained tone, no swell, no riser, no sting, no impact, no pulse, no tension bed, no ambient or atmospheric music, no orchestral or synth element, no piano, no strings, no choir. No music at the head or tail of the shot. No music faded in under the silence. No musical reverb tail as texture.
No ambience, no room tone, no atmosphere bed of any kind.
NO DIALOGUE OF ANY KIND. No line, no word, no whisper, no murmur, no name spoken, no vocalisation, no voice-over, no offscreen voice, no subtitle.
NO MOUTH MOVEMENT. Neither character opens their mouth, parts their lips, mouths silently, or shapes a word at any point. Her breathing is nasal and never opens the mouth. No lip-sync of any kind is generated.
No sound shaped like speech: no voiced sigh, no groan, no throat clearing, no intake that reads as the start of a line.
No gesture substituting for the missing line: he does not beckon, does not point, does not raise a hand, does not tilt his head at her, does not shrug.
No chair creak, no device sound, no exterior sound, no building sound.
No camera movement. No push in on either face. No rack focus between them.
No second person beyond the two characters. No reflection of a third figure in the glass.
No screen light, no glow, no wake, no notification on the device.
No head bow, no chin tuck, no slump, no head lift, no startle, no double-take.
No warm light, no coloured practicals, no lens flare, no rim light.
No CG gloss on skin, fabric, smoke or device. No CG particle smoke.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_38JDnD2aJxtjnkHGSvDeUpDsT5p/hf_20260906_100159_62bb7415-6d57-4173-ae6d-cac408529fd4.mp4)

</details>
