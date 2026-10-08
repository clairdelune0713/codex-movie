# scene-01-19 · SCENE CONTEXTA man and a woman sit facing each other at a table in a small apartment.

[← Index](../../INDEX.md) · Scene: **SCENE 01**

| | |
|---|---|
| Shot size | Close-up |
| Camera | Locked-off |
| Format | Single take · 10s · 21:9 · 1080p |
| Sound | Dialogue · No music |
| Model | seedance_2_5 |
| Characters | char_captain, char_wife |
| Location | loc_apt_cap |
| Props | — |
| Iterations | 1 prompt version(s), 1 generation(s) total |

**Sections:** (PREAMBLE) → ACTIVE REFERENCES → DIALOGUE → CAMERA AND FRAMING — REVERSE OF THE PREVIOUS SETUP → OPTICS → FIRST FRAME AND SPATIAL BLOCKING → FORMAT MODE → PERFORMANCE — HER FACE. THIS IS THE PRIORITY OF THE SHOT. → CONTINUOUS, AT ALL TIMES → KEYED TO THE LINES, ALWAYS UNDERPLAYED → ACTION TIMING — 10 SECONDS → AUDIO — HER VOICE AND HER FOLEY ONLY. HE IS SILENT. ZERO AMBIENCE. → PHYSICS → LIGHTING → POSITIVE CONSTRAINTS → NEGATIVE — LOCAL LOCKS

## Final prompt (latest version)

_Element IDs replaced with names. Original with IDs: [039_20260828_223920_c12d5820.md](../../../prompts/04_FOOTAGE/SCENE%2001/039_20260828_223920_c12d5820.md)_

````text
SCENE CONTEXTA man and a woman sit facing each other at a table in a small apartment. Reverse angle: tight single on her, frontal, framed past his out-of-focus shoulder. She speaks three short lines; he says nothing and takes them. Both of them are alive in every frame. The table is never seen. One continuous 10-second take.

ACTIVE REFERENCES
<<<char_wife>>>: 38yo woman, blonde hair pulled back into a low loose knot with fine strands escaping at the temple and the nape, fair skin, fine lines at the corners of the eyes, pale eyebrows, a faint natural asymmetry between the two sides of the face. White wrap vest with a wide shawl collar over a black t-shirt. A plain thin silver ring on her right hand. 100% matches the reference. She is the sharp subject of this shot and the entire performance sits on her face.
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey. Grey collarless linen shirt over a dark under-layer. He is not smoking and has nothing in his hands. In this shot he is a FOREGROUND element only: the back and side of his shoulder, the line of his neck and the edge of his dark hair, heavily out of focus, occupying the left edge of frame. His face is never seen and he never comes into focus — but he is a living body under pressure and everything he feels must read in that soft dark silhouette. He is entirely SILENT: his performance is visual only. 100% matches the reference for hair, costume and build.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, a large three-pane window with a dark metal frame and a deep pale sill, a cold grey residential tower block filling the glass, heavy dark red curtains hanging as vertical bands at both edges of the window, tall dark leafy plants against the walls, stacks of old books and newspapers piled along the floor beneath the window, a sagging sofa and low coffee table at one end, a conical pendant lamp hanging over the table, a round pale table with metal-framed chairs, and at the far end a kitchen area with pale cabinet fronts and a doorway. Geography, materials, colour and light only. Nothing in the room beyond what is listed here.
@Ref_Composition — BLOCKING REFERENCE ONLY. A photograph of the room with the two seated positions marked on it. The RED marker is <<<char_captain>>>: SEATED at the round table on the LEFT chair, his back toward the window, facing across the table to screen-right. The YELLOW marker is <<<char_wife>>>: SEATED at the round table on the RIGHT chair, opposite him, facing across the table to screen-left, with a tall dark plant and the pale kitchen units behind her.
Use this image ONLY for where the two of them are in the room, which way each faces, and what lies behind each of them. Do NOT reproduce its wide framing. The coloured markers are annotations, not objects and not costume: no red or yellow shape, outline, dot, line, overlay or drawn figure appears anywhere in the render, and neither character wears red or yellow.
@WIFE_Lines — DIALOGUE AUDIO REFERENCE (the supplied recording). This file is the sole source of <<<char_wife>>>'s spoken voice. It supplies the entire spoken performance — all three lines and the silences between them — and its timing governs the shot. Use it as-is. Do not synthesize a new voice, do not replace it, do not re-perform, re-time, stretch, compress, pitch-shift, add reverb or alter the delivery. Do not add breaths, sighs or vocalisations that are not in the file. Her lip movement is locked to this recording frame-accurately, and her lips are still whenever the file is silent.

DIALOGUE
Three lines, all spoken by <<<char_wife>>>, in this order, all delivered into his eyes:
1. "You said there was room."
2. "Somebody else."
3. "You decide who lives."
Source: @WIFE_Lines. That file supplies all three lines and both pauses; its timing governs the shot.
Delivery, as recorded: quiet, low, level, conversational volume across a small table. Not raised, not tearful, not shouted. The first line is a plain statement handed back to him. The second is shorter and flatter — two words, almost to herself. The third is the quietest of the three and lands hardest for being quiet.
<<<char_captain>>> says nothing at all and makes no sound at all. His lips are never seen. There is no reply, no offscreen voice, no voice-over, no muttering, no subtitles, no captions.
Her lips are completely still whenever the file is silent, and move only in exact sync with it when it plays.

CAMERA AND FRAMING — REVERSE OF THE PREVIOUS SETUP
Tight over-the-shoulder single on <<<char_wife>>>.
The camera sits just past <<<char_captain>>> on the LEFT side of the room, close behind his shoulder, on the same axis that ran across the table in the previous shot — the reverse of it, with the line of action respected. Because the camera is almost on that axis, <<<char_wife>>> reads close to FRONTAL — facing very nearly into the lens, with only a few degrees of offset. Her eyeline goes just past the camera to his eyes, to screen-LEFT.
FOREGROUND, LEFT edge of frame, running from the bottom edge upward: the out-of-focus mass of his shoulder, the side of his neck and the edge of his dark hair. Dark, soft, no readable detail, no face, no eye. He occupies roughly the left quarter to left third of the frame.
MIDGROUND, sharp, filling the RIGHT two thirds of frame: <<<char_wife>>>, seated, framed from the CHEST UP. Her shoulders read close to full width. She sits roughly centred in that open right-hand portion of frame.
SCREEN DIRECTION IS LOCKED AND MIRRORS THE PREVIOUS SHOT: she is on the right and looks left; he is the shoulder on the left. Do not flip this.
THE TABLE IS NEVER IN FRAME. The bottom edge of frame sits above the tabletop line: no table surface, no table edge, no chair seat, no hands, no forearms and no objects on the table are ever visible.
BACKGROUND, behind her and soft: the tall dark leafy plant, the pale kitchen cabinet fronts and the dark doorway beyond, and a stretch of plaster wall. This background is DARK and low-contrast — she is not backlit by the window in this angle. The window is behind camera, out of shot. The pendant lamp hangs above and outside the top of frame and is not visible.
Camera height: seated eye height, level. Not looking up at her, not looking down at her.
TRIPOD, HEAD FULLY CLAMPED, ZERO MOVEMENT for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no boom, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not react when she speaks and does not punch in on the third line.
Framing is pixel-identical from the first frame to the last.

OPTICS
Roughly 30° diagonal field of view, short-telephoto character, camera positioned back from her rather than pushed into her face. Matches the lens of the previous setup exactly, so the two angles cut together.
Shallow-to-moderate depth of field. The focal plane sits on her eyes. His foreground shoulder falls well in front of the plane and is strongly defocused into a soft dark mass. The plant, the kitchen units and the doorway behind her fall behind the plane and are soft.
Focus is set on her near eye and DOES NOT MOVE for the whole take. No focus pull, no rack focus onto him, no focus hunting, no lens breathing, no zoom.
Skin resolves in real detail at this scale: pores, the fine lines at the corners of her eyes, the faint down on her cheek, the texture and dryness of her lips, the movement of the tendons in her throat, the loose strands at her temple. The eyes and the mouth must be fully readable — they are the shot.

FIRST FRAME AND SPATIAL BLOCKING
First frame: <<<char_wife>>> already seated and already facing him, chest up, filling the right two thirds of frame, sharp. Her back is against the chair, shoulders level, neck long, head carried high. Her eyes are already on him, going just past the lens to screen-left. Her hands are below the bottom edge.
His defocused shoulder and the edge of his dark hair occupy the left edge of frame as a soft dark mass, breathing.
Behind her the dark plant, the pale cabinet fronts, the doorway, all soft. The air is completely clear.
Neither of them is still in the first frame. Both are already breathing, already carrying small postural life.
No empty first frame. No establishing wide. No walking in, no sitting down. She is seated, large and immediate, in frame one.

FORMAT MODE
Single continuous take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. Dialogue driven by the supplied audio file, not generated.

PERFORMANCE — HER FACE. THIS IS THE PRIORITY OF THE SHOT.
She is not composed and she is not hysterical. She is a woman saying something she has already been carrying for a long time, and the cost of saying it is continuously visible in micro-activity across her face. None of what follows is an "expression change" — it is the constant low-level noise of a real face under strain, running underneath everything.
CONTINUOUS, AT ALL TIMES:
The eyes are never dead. Micro-saccades flicker as they hold on him — tiny involuntary shifts between his left eye and his right, and occasionally down to his mouth and back, the way real eyes do when locked on someone's face. The pupils sit slightly dilated in the low light and adjust minutely.
Blinking is irregular and never metronomic: a quick one, then a long gap held too long, then a slow heavy one. The lids do not close symmetrically.
The lower lids sit fractionally tense throughout — the small squint of someone holding something in.
The eyes are wet with tear film catching the light, glassy, but she does NOT cry: no tear breaks the lid, nothing runs down her face.
Breath is uneven and visible: the chest and shoulders rise and fall irregularly under the white vest, never in a steady rhythm. One breath is caught halfway and held before she speaks.
The head is never locked on the neck. It drifts by fractions of a centimetre with her breathing and makes the constant minute corrections of a person sitting upright.
The nostrils flare slightly on each intake. A swallow travels the throat at least twice, the tendons in the neck moving with it.
Micro-postural sway throughout: the small continuous adjustments of a torso balancing on a chair. One real weight shift as she settles her hips. One small lift and drop of a shoulder.
KEYED TO THE LINES, ALWAYS UNDERPLAYED:
Before the first line — the lips press together dry and part again. A swallow. The jaw sets.
ON "You said there was room." — Level, almost gentle. She hands his own words back to him. The eyes stay steady; the only tell is a slight tightening at the outer corners and the smallest lift at one side of the mouth that is not a smile and is gone immediately.
IN THE FIRST PAUSE — The jaw sets again, harder. Another swallow. The eyes hold on him and flick once between his eyes. She is deciding whether to keep going. Her chest rises on a shallow breath that does not fully release.
ON "Somebody else." — Shorter, flatter, dropping in volume, half to herself. Her chin comes down a degree on it, the eyes staying up on him from under the brow. The mouth stays parted a beat after the words end.
IN THE SECOND PAUSE — The longest and the worst. Her breathing goes shallow and quick. THE CHIN TREMOR arrives here: one fine involuntary quiver of the chin and lower lip, clamped down within a fraction of a second by a hard set of the jaw. The brow draws in a millimetre and releases. One hard blink. Her throat works.
ON "You decide who lives." — The quietest of the three. Her chin lifts a degree as she says it, the neck lengthening, the head coming up rather than forward. She is not attacking; she is stating something she has finally allowed herself to say out loud. The delivery is steady but the mouth is not quite under control on the last word.
AFTER THE LAST WORD — One hard blink. The eyes stay on him and go glassier. A long uneven exhale. Her shoulder line lowers two or three centimetres and her chin comes back down a degree. She holds his look to the last frame.
SPEECH ARTICULATION: driven by the audio file only. The mouth and jaw do the work of the words, but the whole lower face participates — cheek, chin, the muscles at the corners of the mouth, the small movements of the throat — as it does in real speech. No head-nodding on stressed words, no eyebrow punctuation, no theatrical emphasis. The performance is under the words, not on them.
HER GAZE stays on him for the whole shot. If it leaves at any point it is only for a fraction of a second, dropping a few degrees and coming straight back — never a look away, never a look at the lens.

PERFORMANCE — HIS REACTIONS. HE IS ALIVE, HE TAKES IT, AND HE IS COMPLETELY SILENT.
He is out of focus and faceless, so every reaction must be legible as a change in a soft dark silhouette: the height and angle of his shoulder, the line of his neck, the tilt of the back of his head, the loose edge of his hair, the visible rate of his breathing. Play them large enough in the body to read at this softness, but never large enough to become melodrama. He is the second performance in this shot, not a piece of set dressing.
CRITICAL: HIS PERFORMANCE IS PURELY VISUAL. He breathes visibly but INAUDIBLY. Everything he does must read with the eye alone, because nothing he does makes a sound. Do not compensate for the silence by making his movements bigger.
HIS BASELINE, CONTINUOUS: breathing steadily and visibly, shoulder rising and falling, small continuous postural life — the micro-sway of a torso on a chair, the constant minute corrections of a real neck. He is never a static shape in the foreground, not for a single frame.
BEFORE SHE SPEAKS — One slow breath. His shoulder settles a centimetre. He is waiting for it.
ON "You said there was room." — He goes still. The breathing stops mid-cycle and the shoulder holds at the top of an inhale a beat too long. The stillness itself is the reaction, and it is only legible because he was moving before it.
IN THE FIRST PAUSE — The held breath releases, slowly and unevenly, visible in the shoulder dropping. The back of his head lowers a centimetre.
ON "Somebody else." — The head turns a few degrees away from her, toward screen-left, then comes back — a man who wanted to look away and did not. The loose edge of his hair shifts and settles with the movement.
IN THE SECOND PAUSE — His shoulder rises: not breath this time but tension, the trapezius pulling up as he braces for the next one. One slow deliberate breath in and out, read entirely from the shoulder line. One small weight shift on the chair, the whole silhouette resettling a centimetre lower than it was.
ON "You decide who lives." — THE FLINCH. The shoulder contracts a centimetre and releases, instantly suppressed. It is small, it is involuntary, and it is the only large thing his body does in the whole shot. His head drops a fraction with it.
AFTER IT, to 0:10 — He holds, the shoulder rising and falling shallow and uneven. One more small settle. He does not answer, does not stand, does not lean in, does not reach out, does not turn away. The silhouette stays exactly where it is, alive and taking it.
At no point does he come into focus, show his face, or turn toward the lens.

ACTION TIMING — 10 SECONDS
The three lines land where the supplied recording puts them; the beats above are keyed to the audio, not to a stopwatch. Let the file drive them.
Opening, before she speaks — Both settling and breathing. Her eyes are on him already. Neither is still.
FIRST LINE — She speaks, level; he stills mid-breath.
FIRST PAUSE — Her jaw sets and she swallows; his held breath releases and his shoulder drops.
SECOND LINE — Her chin comes down; his head turns a few degrees and comes back.
SECOND PAUSE — Her breathing goes shallow, the chin tremor arrives and is clamped; his shoulder rises with tension and he resettles.
THIRD LINE — Her chin lifts; he flinches once.
AFTER THE LAST WORD, to 0:10 — She exhales unevenly, her shoulders lower, her chin comes back down, her eyes stay on him. He does not answer. The shot ends on two people who have not moved apart.
She does not stand, does not lean across the table, does not reach out, does not touch him, does not gesture, does not raise a hand into frame, does not look into the lens.

AUDIO — HER VOICE AND HER FOLEY ONLY. HE IS SILENT. ZERO AMBIENCE.
The soundtrack contains exactly two elements: the supplied voice file, and close-mic foley generated by HER body alone. There is no third layer and no bed underneath. Between foley events and dialogue the track is absolute digital silence — a flat zero. Do not soften it, fill it, or make it natural.
Permitted sounds, nothing else:
1. The supplied voice file @WIFE_Lines
2. HER breath — uneven, close and dry: one caught breath before she starts, shallow quick breathing in the second pause, one long uneven exhale after her last word. All of it ducked out or kept clear of the dialogue so nothing overlaps her words.
3. HER cloth — the white vest shifting as her shoulders move and as she resettles
4. HER body — one or two dry swallows, close-mic level only
<<<char_captain>>> PRODUCES NO SOUND WHATSOEVER for the entire 10 seconds. This is a hard lock and the most important audio note in the shot. Specifically forbidden from him: no inhale, no exhale, no held breath released audibly, no nasal breath, no sharp intake, no shudder, no sigh, no sniff, no gasp, no groan, no throat clearing, no swallow, no hum, no grunt, no vocalisation of any kind, no word, no whisper. Also no cloth sound from his shirt when he turns, braces, flinches or resettles, and no chair sound from his seat. His entire performance is silent and visual only.
The reason for this lock: her three lines and her breaths are the only voice in the shot, and any breath from him would collide with her delivery. If a breath is heard anywhere in this shot, it is hers.
No cigarette sound of any kind: no tobacco crackle, no paper rustle, no lighter, no ashtray. No chair creak from either of them.
Absolutely no ambience, in any form, under any name. Forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, ventilation, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz — the pendant lamp is unlit and silent, and no kitchen appliance is running. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children — the window is behind camera and is a light source only, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No music, score, drone, pad, tension bed, sting, swell, riser, whoosh, sub-bass hit or reverb tail used as texture — nothing under any of the three lines, nothing in the pauses, nothing at the head or tail.
The mix stays close and dry: no room reverb, no distance perspective on the voice, no reflections, no spatialization.

PHYSICS
Photoreal human behaviour throughout. Both bodies obey real anatomy, real joint limits, real muscle sequencing, real speed.
NEITHER OF THEM IS EVER FROZEN. Even in the stillest moments there is postural micro-sway, breathing, and the constant small corrections a body makes to stay upright in a chair. Stillness in this shot means restrained, never motionless. If a single second of this shot could be mistaken for a still photograph, it is wrong.
His silence is acoustic only, never physical: he breathes, moves, turns and flinches with full visible weight, and none of it makes a sound.
Her movements come from the spine and the hips, not from the neck alone. When she settles her weight the pelvis moves and the ribcage follows. When her chin lifts on the third line the movement runs up through the cervical spine, not as a tilt of the skull alone.
His turns and braces come from the shoulder first, the head following a fraction behind. When he flinches, it is a fast small contraction with a real overshoot and settle afterward, not an instant snap and not a frozen hold.
Facial muscle behaviour is human only: real orbicularis and masseter activity, real asymmetry between the two sides of her face, real involuntary suppression of the chin tremor. No rubbery deformation, no uncanny smoothness, no motion-capture stiffness, no exaggerated grimace, no animated over-articulation, no symmetrical puppet expressions.
Cloth: the white vest and the linen respond with real weight and creasing to every shift of the bodies underneath. Fabric does not cling, ripple or flow. No cloth-simulation shimmer, no jelly motion.
Hair: her loose strands at the temple and nape move slightly and settle with each head movement, as a weighted mass. The low knot holds its shape. The loose edge of his hair shifts when his head turns.
Skin: real pores, real texture, real subsurface warmth in the low light, slight flush at the cheek and the base of the throat. Never smoothed, never waxy, never plastic. No CG gloss.
THE AIR IS COMPLETELY STILL AND CLEAR. No smoke, no vapour, no haze, no drifting particulate, no dust. The only motion in the frame is the two of them.

LIGHTING
Cold grey-green ambient from the window, the primary and only light source. In this reverse angle the window is BEHIND CAMERA and off to one side, so it now works as a soft frontal-side key raking in from screen-LEFT across the table. Diffuse, flat, overcast. Constant for the full 10 seconds — no change in level, colour or direction, and no change on any of the three lines. The pendant lamp is switched OFF and contributes nothing.
This is the reverse of the previous setup's lighting logic: he was backlit and dark; she is keyed and readable. That asymmetry is intended and must hold.
On her: the light catches the near side of her face — the brow, the cheekbone, the bridge of the nose, the near eye socket, the line of the jaw and the length of her throat — while the far side of her face falls away into soft shadow. The eyes sit in the lit side and read clearly. Low contrast overall, no hard edges, no hot highlights. As she breathes, swallows and resettles, the light shifts by fractions across the planes of her face — that small continuous change is part of what makes her read as alive. When her chin lifts on the third line the light runs further down her throat and the jawline sharpens a fraction; this comes from her moving through the existing light, never from the lighting changing. Her white vest picks up the same light on the shoulder and the shawl collar but stays desaturated and dim, never bright, never a hotspot. Do NOT add a fill or a beauty key; do not lift the shadow side.
On him: his foreground shoulder is the darkest mass in the frame, a soft near-silhouette with only a thin cold edge along the top of the shoulder and the outer line of his hair where the window rakes past him. That thin edge shifts and slides as he breathes, turns and flinches — it is the main way his reactions read, and it carries the whole weight of his performance now that he makes no sound. No detail, no face, no eye.
Behind her: the plant, the pale kitchen cabinet fronts, the doorway and the plaster are all dim, soft and low-contrast, sitting well below her exposure. No bright background, no window in frame, no luminous field behind her — that belonged to his angle.
No fill. No beauty key. No practicals. No artificial rim. No eye light — the eyes read through shape, shadow and the wet of the tear film, not through an added catchlight.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade. Matches the previous setup exactly so the two angles cut together.

POSITIVE CONSTRAINTS
This is the REVERSE of the previous shot. Same room, same table, same seats, same lens, same grade, same silence. Only the camera has crossed to the other side.
HE MAKES NO SOUND AT ALL for the entire 10 seconds — no breath, no cloth, no chair, no vocalisation. His performance is visual only. Any audible breath in this shot is hers.
BOTH CHARACTERS ARE ALIVE IN EVERY FRAME. Continuous breathing, micro-postural sway and involuntary facial and body activity throughout, for both of them. Neither is ever a still image, not even for a beat.
HER FACE CARRIES THE SHOT and must be photoreal at every scale: pores, tear film, irregular asymmetric blinks, micro-saccades, the chin tremor and its suppression, swallows, uneven breath, real asymmetry.
HIS REACTIONS ARE REQUIRED and must be readable in the defocused foreground: continuous breathing baseline, stillness on the first line, release, a head turn away and back on the second, tension and a resettle in the pause, one suppressed flinch on the third, shallow uneven breathing at the end — all of it silent.
Exactly three lines of dialogue, all spoken by <<<char_wife>>>, in this order: "You said there was room." / "Somebody else." / "You decide who lives." No other words from anyone. No ad-libs, no muttering in the pauses, no repeat of any line, no reply from him.
Dialogue comes only from @WIFE_Lines. No generated voice. Lip movement locked to that file, and completely still whenever it is silent.
SHE is sharp on the RIGHT two thirds of frame and looks screen-LEFT. HIS defocused shoulder occupies the LEFT edge. This composition never changes and is never flipped.
Character positions follow @Ref_Composition: <<<char_captain>>> in the LEFT chair with his back toward the window, <<<char_wife>>> in the RIGHT chair opposite him. Do not swap them.
The coloured markers in @Ref_Composition are annotations only. No red or yellow shape, dot, line, outline, arrow or drawn figure appears anywhere in the render. Neither character wears red or yellow.
His face is never visible, he never turns toward camera, he never comes into focus. Everything he does is read from the shoulder, the neck, the back of the head, the hair and the breathing.
SHE LOOKS HIM IN THE EYES FOR ALL THREE LINES. Level, direct, at his eye height, just past the lens to screen-left, and it does not break.
NOBODY IS SMOKING. No cigarette anywhere — not in either hand, not below frame, not in a mouth, not resting anywhere. No smoke, no ember, no ash, no ashtray, no lighter, no pack.
Both are ALREADY SEATED in the first frame. No walking in, no sitting down, no standing up, no chair movement.
THE TABLE IS NEVER VISIBLE. The bottom edge sits above the tabletop. No table surface, no table edge, no chairs, no hands, no forearms, no objects on the table appear at any point.
No object of any kind appears in this shot — no device, no screen, no phone, no display, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock. Nothing is invented anywhere in frame.
Tripod, zero camera movement, framing pixel-identical from first frame to last.
Focus locked on her eyes and never moved. No rack onto him, no rack onto the background.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures in the kitchen doorway, no reflections of other people.
No visible brand marks, logos or legible lettering anywhere.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
Photoreal documentary-grade human performance. Fine grain, cold grey-green palette, stable exposure. No CG gloss on skin or fabric.

NEGATIVE — LOCAL LOCKS
NO SOUND FROM HIM. No breath, no inhale, no exhale, no sigh, no sniff, no gasp, no shudder, no swallow, no throat clearing, no groan, no whisper, no word, no cloth rustle, no chair creak. If any sound in this shot comes from the foreground shoulder, it is wrong.
No breath from anyone overlapping her lines. Her own breaths sit only in the gaps.
No frozen actors, no mannequin stillness, no held pose, no waxwork faces, no static foreground shoulder. If either of them looks like a still image at any point, it is wrong.
No theatrical performance either: no crying, no sobbing, no tears running down the face, no grimace, no head shake, no nod, no smile, no clenched jaw held for effect, no lean across the table, no hands into frame, no finger pointed.
No raised voice on "You decide who lives." It is the quietest line in the shot, not the loudest.
No flipped screen direction. If she is on the left of frame or looking screen-right, it is wrong.
No window and no bright luminous field behind her — that background belongs to the opposite angle.
No cigarette, no smoke, no vapour, no haze, no drifting particulate.
No table in frame. If any part of the tabletop or its edge is visible, the framing is too loose.
No camera movement of any kind, not even a slow push on the last line. Hard lock.
No focus pull of any kind. His foreground shoulder never comes sharp; the background never comes sharp.
No head emphasis on the dialogue: no nodding, no tilting into a line, no eyebrow punctuation.
No symmetrical or puppet-like facial animation. No blinking in a regular rhythm. No perfectly matched movement between the two sides of the face.
His face never appears — no profile, no turn to camera, no reflection.
No wide shot, no reverse of the reverse, no cutaway, no second setup. One frame, one take.
No look to camera from either of them.
No music, no ambience, no spoken reply from him.
No hero lighting, no rim light, no eye light, no lens flare, no volumetric god rays.
````

### Generated videos

- 2026-08-28 22:39:20 · [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_223920_c12d5820-0ac5-4d7b-b7f2-461f71e47e6e.mp4)
