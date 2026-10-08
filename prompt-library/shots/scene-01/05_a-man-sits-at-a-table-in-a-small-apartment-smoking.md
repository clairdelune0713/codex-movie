# scene-01-05 · A man sits at a table in a small apartment, smoking, waiting for a decision he cannot influence.

[← Index](../../INDEX.md) · Scene: **SCENE 01**

| | |
|---|---|
| Shot size | Medium |
| Camera | Locked-off |
| Format | Single take · 20s · 21:9 · 1080p |
| Sound | Dialogue · No music |
| Model | seedance_2_5 |
| Characters | char_captain, char_wife |
| Location | loc_apt_cap |
| Props | prop_device |
| Iterations | 1 prompt version(s), 1 generation(s) total |

**Sections:** SCENE CONTEXT → ACTIVE REFERENCES → LOCATION MAP → FIRST FRAME AND SPATIAL BLOCKING → FORMAT MODE → OPTICS → CAMERA → ACTION TIMING → AUDIO → PHYSICS → LIGHTING → POSITIVE CONSTRAINTS

## Final prompt (latest version)

_Element IDs replaced with names. Original with IDs: [009_20260826_144523_93d62f62.md](../../../prompts/04_FOOTAGE/SCENE%2001/009_20260826_144523_93d62f62.md)_

````text
SCENE CONTEXT
A man sits at a table in a small apartment, smoking, waiting for a decision he cannot influence. Across the table, slightly out of focus, his wife's shoulder and the back of her head occupy the foreground — her head is tipped down, her gaze on the small orange device lit in her hands. He watches her. He smokes, offers her a piece of procedure, asks her to look at him, and gets nothing. She never lifts her head from the device.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt, dark wide-leg trousers. Seated at the far end of the table, facing the camera. A lit cigarette held between the index and middle finger of his right hand. Expression is not performed — the face of a man waiting for a result he already suspects and cannot change. 100% matches the reference.
<<<char_wife>>>: 38yo woman, blonde hair loosely pulled back. White wrap vest over black t-shirt. Seated at the near end of the table — her left shoulder and the back of her head occupy the lower-center foreground, out of focus, her head tipped down and forward over the device held in both hands on the table in front of her. She does not turn. She does not lift her head. She does not speak. Her presence is felt, not seen. 100% matches the reference.
<<<prop_device>>>: small square handheld unit, matte orange bezel with rounded corners, black glass front panel, small camera module set into the upper-right corner of the bezel, chrome-ringed circular side button on the right edge. Screen is ON — black display with a single small white pictogram glowing at its center. Held flat in both of <<<char_wife>>>'s hands, screen facing up toward her lowered face. 100% matches the reference. Correct scale: it fits within two palms.
<<<loc_apt_cap>>>: small residential apartment — grey-green walls, large window behind <<<char_captain>>> with dark red curtains partially open, cold grey residential tower block visible through the window, pendant lamp above the table. Geography and atmosphere only.
AUDIO REFERENCE — ElevenLabs_2026-08-26T14_11_50__s0_v3: the supplied voiceover recording of <<<char_captain>>>'s dialogue. This file is the sole source of the spoken voice. Do not synthesize, replace, re-time, pitch-shift, or regenerate the voice.

LOCATION MAP
Table: running toward and away from the camera. <<<char_wife>>> at the near end — her shoulder, the back of her lowered head, and her hands holding <<<prop_device>>> in the foreground, out of focus. <<<char_captain>>> at the far end — sharp, screen-center.
Window: directly behind <<<char_captain>>>, squared to the lens — the window plane is parallel to the sensor, its frame reading as a straight horizontal-and-vertical rectangle with no perspective skew, no diagonal convergence, no tilt. Its vertical center line runs behind his head. The window fills the background across the width of the frame. Cold grey-green light from the tower block beyond. Dark red curtains at the left and right edges, hanging vertically and evenly. The window is a light source only, never a sound source.
Camera: locked off on a tripod, positioned behind and slightly above <<<char_wife>>>'s left shoulder, aimed at <<<char_captain>>> screen-center, and squared to the window plane behind him.
Gaze lines: his eyes travel down and slightly screen-left, aimed at her lowered head and at the lit device in her hands below the frame edge. Her gaze is aimed straight down at the device screen. The two gaze lines never meet at any point in the shot.

FIRST FRAME AND SPATIAL BLOCKING
First frame: <<<char_captain>>> screen-center in sharp focus — face from mid-chest to crown filling the center of the frame. His head is angled 5–8° down and 3–5° toward screen-left; his eyes aimed off-camera screen-left and below the camera axis, at her. His right hand is visible at the lower-right of frame, elbow planted on the table, forearm angled up, the lit cigarette held between index and middle finger at roughly chest height, about 25cm from his face. The ember is live. A thin ribbon of smoke rises through the cold backlight. His left hand rests on the table below the frame edge, not visible.
<<<char_wife>>>'s left shoulder and the back of her loosely-pinned blonde hair occupy the lower-center foreground — soft, out of focus, head tipped down, a few loose strands falling forward past her cheek. At the lower-left of frame, partially cropped by the bottom edge and heavily out of focus, her hands hold <<<prop_device>>> flat on the table, screen up. The orange bezel reads as a soft warm blur; the black screen and its small white glowing pictogram read as a contained pool of light under her face. The device is unmistakably present but never sharp and never dominant.
The window behind him fills the background — squared, straight, symmetrical, cold grey-green, the tower block compressed into a flat rectangle behind his head. Dark red curtains at the left and right edges. The pendant lamp hangs above, out of frame and unlit.
This exact framing is fixed for the entire shot. The frame edges do not move by a single pixel from 0:00 to 0:20.

FORMAT MODE
Single continuous take. 20 seconds. No cuts. Real-time motion, no slow motion. Locked-off tripod shot — the camera is a fixed observer and never moves. Dialogue is driven by the supplied audio file, not generated. Sound is close-mic foley and voice only, with no ambience bed. All drama carried through unforced micro-behavior and the two spoken lines separated by a long silence. Every movement is small, biological, and involuntary except the two cigarette lifts and the speech.

OPTICS
29° diagonal field of view — 85mm equivalent portrait compression. Foreground — <<<char_wife>>>'s shoulder, hair, hands and <<<prop_device>>> — out of focus throughout: soft masses, the device screen a diffuse glowing rectangle rather than a readable display. <<<char_captain>>>: sharp throughout — face, eyes, beard texture, pores, the mouth, the cigarette and the fingers holding it. Micro-expressions and lip movement must be readable at this focal length. The window behind him compresses into a flat cold grey-green rectangle, its straight frame lines reading clean and parallel to the edges of the picture. Shallow depth of field, constant — no focus pull, no rack focus to the device, no lens breathing. Focal length fixed: no zoom.

CAMERA
Single continuous take, 20 seconds. Locked-off camera on a tripod with the head fully clamped. 29° FOV, fixed. Camera behind and above <<<char_wife>>>'s left shoulder, aimed at <<<char_captain>>> screen-center, squared to the window plane.
Absolutely no camera movement for the full duration: no push in, no pull back, no dolly, no truck, no crane, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift toward the subject, no stabilization wobble. The tripod does not move because it cannot move.
Static tripod plate, not a stabilized handheld emulation. No breathing tremble, no operator micro-motion, no simulated organic camera life. The frame is dead still — all movement inside the frame comes from the actors and the smoke.
The window frame lines and the tower block behind him remain in identical screen positions from first frame to last, which is the test of whether the lock held.

ACTION TIMING
0:00–0:03.5 He is looking at her — eyes down-left, head tipped 5–8° down. The cigarette rests at chest height, still, smoke rising in an unbroken ribbon. Two slow shallow breaths in this block. At 0:00.8 his eyes make a small scanning saccade — 2–3° from the back of her head down toward the glow of the device in her hands, then back up. At 0:02.0 a single blink, normal speed. At 0:03.0 a second blink. Her head stays down over the device. Her shoulder rises and falls with her own breath. The device screen holds a constant, unchanging glow.

0:03.5–0:04.6 His head tilts a further 2–3° toward screen-left — the involuntary micro-adjustment of a person trying to catch a face that is angled away from them. The right hand lifts the cigarette to his lips: 20–25cm of travel, elbow planted, economical, no flourish. His eyes stay on her — they do not follow the cigarette.

0:04.6–0:06.0 First drag. The ember brightens for 1.4 seconds. His cheeks hollow 2–3mm. The skin at the outer corners of his eyes tightens fractionally. His eyes remain on her; they do not close, they do not drift. At 0:05.6 his eyebrows lift 1–2mm at the inner ends only — a brief inner-brow raise, gone within 0.4 seconds.

0:06.0–0:06.5 The hand lowers back to chest height, cigarette between his fingers, tip angled up. He holds the smoke — closed mouth, throat still. His head straightens 1–2mm; his chin lifts almost imperceptibly.

0:06.5–0:08.0 He exhales through the nose — two slow streams descending in front of his chest, spreading, then rising through the cold backlight. His shoulders settle 2–3mm. His nostrils flare 1mm and release. At 0:07.4 his jaw tightens fractionally at the hinge — 1–2mm of masseter definition under the beard — and holds for about a second.

0:08.0–0:09.6 Silence. He looks at her. At 0:08.4 a small dry swallow — the larynx rising and dropping once. At 0:09.0 a single blink, eyes returning to her immediately. At 0:09.3 his eyes drop 8–10° to the device in her hands, 0.4 seconds, then rise back to her lowered head — the return slower than the drop.

0:09.6 First line begins. He speaks the first line of ElevenLabs_2026-08-26T14_11_50__s0_v3 — "Honey, it takes longer when there's room." Lip movement is driven by and locked to the supplied recording, matching its exact phonemes, phrasing, stress and duration. The cigarette stays where it is. Only the mouth moves — small, unemphatic articulation. His eyebrows do not move on the line. His eyes stay on her.

Between the two lines Long silence, exactly as recorded in the supplied file. He waits for an answer that does not come. Her head does not move; her gaze stays on the device. In the foreground blur, one loose strand of her hair shifts a few millimetres with her breath. He blinks once during the pause. Midway through the pause his eyes drop again to the device glow, hold 0.5 seconds, and rise back — slower still. Mouth completely closed and still for the whole gap. No filler movement, no shift in posture.

Second line He speaks the second line of the supplied recording — "Look at me." Lip movement locked to the file. His head lowers 1–2mm as he says it.

After the last word 1.5–2 seconds of nothing. She does not turn. Her head stays down over the device. Her hands do not move on it. His eyes stay on her. His lips press together — 1–2mm for 0.3 seconds — and release. A single blink.

Final block The right hand lifts a second time — slower than the first lift, less economical. Second drag, shorter: the ember brightens for 0.8 seconds. His eyes stay on her throughout. The hand lowers. He exhales through the nose, longer and slower than the first exhale; the smoke falls, spreads, and rises across the frame between them. His shoulders settle again. His jaw relaxes fully. His head lowers 2–3mm and stays lowered.

0:19.0–0:20 Stillness. Ash holds on the cigarette, longer now, curling slightly. The last of the smoke drifts up past his face. The device glow is unchanged in the foreground. Her head is still down, her gaze still on the screen. The shot ends with him looking at her, and with her looking at the device.

AUDIO
Dialogue source: ElevenLabs_2026-08-26T14_11_50__s0_v3. This file supplies the entire spoken performance of <<<char_captain>>> — both lines and the silence between them. Use it as-is. Do not generate a new voice. Do not re-perform, re-time, stretch, compress, pitch-shift, add reverb beyond light room placement, or alter the delivery. Do not add breaths, sighs, or vocalizations that are not in the file.
Lip-sync: mouth movement matches the supplied audio frame-accurately. Lips are completely still whenever the file is silent, including the gap between the two lines and the entire head and tail of the shot.

Sound design is close-mic foley and voice only. No ambience bed of any kind. Between sound events the track is true digital silence — empty, dead, uncomfortable. The absence of any room bed is the intended effect: the two people exist in a vacuum.

Permitted sounds — nothing else:
— Breath: slow shallow nasal inhales and exhales from <<<char_captain>>>, close and dry. Ducked out wherever the dialogue file is playing.
— Clothing foley: the faint shift of linen shirt fabric as his shoulders settle after each exhale; the slight rub of sleeve fabric against the table as his forearm lifts and lowers; the near-inaudible fabric movement of her shoulder as she breathes.
— Contact foley: skin and elbow contact on the table surface; fingers adjusting on the cigarette paper; a faint dry crackle of burning tobacco on each drag; the soft contact of lips on the filter; the barely-there contact of her fingertips against the device casing.
— Body sound: the single dry swallow at 0:08.4, close-mic level only.
— Voice: the supplied dialogue file, and nothing else.

Explicitly excluded:
No room tone. No air conditioning, no HVAC, no compressor hum, no refrigerator, no electrical buzz, no lamp hum.
No exterior sound of any kind through or beyond the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children.
No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing.
No device sound whatsoever: the unit is silent — no chime, no beep, no notification, no alert, no vibration, no haptic buzz, no interface click, no synthetic voice.
No atmosphere, no ambience bed, no environmental wash, no field-recording layer, no "quiet apartment" tone, no low-level rumble to fill silence, no synthesized air.
No score, no music, no drone, no pad, no tension bed, no sound design flourishes, no risers, no whooshes, no reverb tails as texture.
No foley for objects not present: no chairs, no cups, no cutlery, no paper.
<<<char_wife>>> makes no vocal sound — no breath audible above the faintest clothing movement, no sigh, no sniff, no cry. She does not speak.
No offscreen voices. No subtitles, no captions.
Mix: everything close, dry, and small. Foley sits well under the voice. When nothing is happening, the track is silent.

PHYSICS
Device: <<<prop_device>>> rests flat and stable in both her hands on the table surface. It does not move, tilt, flip, or get set down during the shot. The screen stays on at constant brightness with no flicker, no scroll, no animation, no change of content, no refresh. Rigid moulded plastic and glass — no bend, no wobble, no floating.
Cigarette burn: the cigarette is visibly shorter by the end of the shot. The ember brightens as airflow increases during each drag, then dims to a dull glow within 0.5 seconds. Paper and ash edge consumed by 3–4mm on the first drag, 2–3mm on the second. Ash accumulates and curls but does not fall within the 20 seconds.
Smoke: real physical smoke. Laminar ribbon from the resting cigarette, breaking into slow turbulence 20–30cm above the tip. Exhaled smoke moves as two denser nasal streams that fall, spread horizontally in front of the chest, and only then rise. Slow, heavy. Over 20 seconds the air visibly accumulates a faint haze in the backlight. Because the camera is locked, the smoke is the only large moving element in the frame — it must read as genuine physical volume, not CG particles, and must never move faster than still indoor air allows.
Hand: his elbow planted for the whole shot — forearm and wrist movement only. The hand never leaves frame and does not gesture during speech. The second lift is measurably slower than the first.
Eye movement: saccades are fast and small; the returns to her face are slower than the departures, and progressively slower across the shot. Blink rate stays natural across 20 seconds — roughly one every 2–4 seconds, never mechanical or evenly spaced.
Jaw and mouth during speech: articulation driven by the audio file only. No head emphasis, no eyebrow punctuation, no hand movement synchronized to speech.
Jaw tension and inner-brow raise: involuntary output of sustained suppression, generated by the body, not performed by the face.
Swallow: dry, single, larynx rising and dropping — a nervous-system response, not a gesture.
Her micro-motion: breathing only, for the full 20 seconds. Shoulder rise and fall of 2–3mm, loose hair strands shifting a few millimetres, fingers unmoving on the device. No turn, no head lift, no gesture, no reaction to either line.

LIGHTING
Cold grey-green ambient from the large squared window directly behind <<<char_captain>>> — the primary light source. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 20 seconds — no change in level, color, or direction.
The window light wraps around him from behind and reaches his face as soft frontal ambient — even, no hard shadows. His left cheekbone and the bridge of his nose catch slightly more of the cold light. His beard catches the cold light along the top surface of the hair. The light must be even enough that micro-expression and lip movement remain readable — no crushed shadow across the eyes or mouth.
Secondary practical: <<<prop_device>>>'s screen throws a small, weak, cool-neutral glow upward onto her lowered face and the undersides of her fingers in the out-of-focus foreground — a contained pool of light in the lower-left of frame. It does not spill across the table, does not reach him, does not light the room, does not flicker, and never becomes the key. The orange bezel is the only saturated color in the picture and it stays soft and out of focus.
The smoke is backlit by the window and reads as a bright volumetric mass against the cold grey-green — clearly visible against the window, building slightly over the duration. Smoke must never obscure the mouth during the spoken lines.
The cigarette ember is a small warm point only. It does not illuminate his face or hand.
Tower block through the window: a flat grey rectangle behind his head, individual windows barely readable as texture. Its position in frame is identical in the first and last frame.
Dark red curtains: deeply desaturated in the cold ambient — more brown-grey than red at this exposure, hanging straight and even at both edges of the window.
No artificial fill. No beauty key. The pendant lamp above is unlit.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
Locked-off tripod shot. The camera does not move at all for the full 20 seconds — no push, no pull, no dolly, no pan, no tilt, no roll, no zoom, no handheld, no gimbal drift, no reframing, no stabilization wobble, no simulated breath tremble. Framing is pixel-identical from first frame to last.
The window sits squared and straight behind him — parallel to the sensor, frame lines horizontal and vertical, no perspective skew, no angled wall, no diagonal convergence, no dutch.
<<<prop_device>>> is visible in her hands in the foreground for the entire shot, screen on, out of focus. Exactly one device in frame. It matches the reference exactly — matte orange bezel, black glass front, corner camera module, chrome-ringed side button, single small white pictogram glowing at screen center. No other text, no UI, no readable interface, no changing content, no logos added or removed. It is never in sharp focus, never held up, never handed over, never set down.
Single continuous take, exactly 20 seconds, no cuts, real-time motion.
Dialogue comes only from ElevenLabs_2026-08-26T14_11_50__s0_v3. No generated voice, no added words, no ad-libs, no muttering in the silences.
Lip movement is locked to the supplied audio and completely still whenever that audio is silent.
Audio contains only voice and close foley — breath, cloth, skin contact, cigarette. No room tone, no ambience, no exterior or window sound, no device sound, no music. Silence between events is true silence.
29° FOV, fixed. <<<char_captain>>> sharp throughout, screen-center. Foreground out of focus throughout. No focus pull, no lens breathing.
His eyes remain aimed down-left at her for the entire shot except the three brief scripted micro-drops to the device. He never looks at the camera. He never looks at the window.
Her head stays down over the device for all 20 seconds. She does not turn, does not lift her head, does not answer, does not react. The two gaze lines never meet.
The silences are held exactly — no filler sound, no invented business, no restlessness beyond the scripted micro-behavior. Empty time is intentional.
The cigarette is in his right hand for the entire shot and stays in frame. Exactly two drags, at the scripted moments, never during the dialogue. He does not stub it out, does not put it down, does not tap ash.
All facial movement at micro scale — 1–3mm. No large expressions, no crying, no grimace, no head shake, no nod, no smile.
No other objects on the table. No ashtray visible.
Two people only. No extra characters, no duplicates. Nobody enters or leaves the frame.
Real physical smoke, backlit and clearly visible against the window; no CG particle smoke, no floating motion.
Fine grain, cold grey-green palette, stable exposure across the full duration. No CG gloss on skin, fabric, or device casing.
````

### Generated videos

- 2026-08-26 14:45:23 · [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260826_144523_93d62f62-e8c6-42ea-ab22-f0715333eaea.mp4)
