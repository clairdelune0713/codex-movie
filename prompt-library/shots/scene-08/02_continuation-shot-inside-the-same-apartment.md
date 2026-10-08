# scene-08-02 · Continuation shot inside the same apartment.

[← Index](../../INDEX.md) · Scene: **SCENE 08**

| | |
|---|---|
| Shot size | Wide |
| Camera | Handheld |
| Format | Single take · 25s · 21:9 · 1080p |
| Sound | Dialogue · No music |
| Model | seedance_2_5 |
| Characters | captain-agentv4, char_dad, char_mum, char_son |
| Location | loc_family_apt |
| Props | — |
| Iterations | 2 prompt version(s), 2 generation(s) total |

**Sections:** SCENE CONTEXT → OUTPUT SETTINGS → ACTIVE REFERENCES → CONTINUITY — STARTING STATE → LOCATION MAP → FIRST FRAME AND SPATIAL BLOCKING → CAMERA ORBIT LOCK → FORMAT MODE → SINGLE CONTINUOUS TAKE. → OPTICS → CAMERA → FACE AND SPEECH LOCK → JAW SIGNAL → LIVING BODY LOCK → ACTION TIMING → DIALOGUE RULES → PHYSICS → LIGHTING → AUDIO → POSITIVE CONSTRAINTS → NEGATIVE CONSTRAINTS — LIGHT EMISSION

## Final prompt (latest version)

_Element IDs replaced with names. Original with IDs: [008_20260901_093335_dc2e7a67.md](../../../prompts/04_FOOTAGE/SCENE%2008/008_20260901_093335_dc2e7a67.md)_

````text
SCENE CONTEXT
Continuation shot inside the same apartment. The camera holds on the kneeling father, finds the helmeted officer standing over the row, then orbits him in one unbroken circle while he delivers a procedural order, coming back to rest behind him with all three kneeling civilians visible beyond his shoulders.

OUTPUT SETTINGS
Single continuous handheld take, 25 seconds, real-time motion, no internal cuts. One continuous spoken passage, delivered through a helmet pickup. No subtitles, no captions, no music.

ACTIVE REFERENCES
<<<image_1>>>: the exact first frame of this shot. The take begins on this image and moves out of it. It controls opening framing, composition, subject position and scale, room layout, light direction, exposure, and color.
<<<loc_family_apt>>>: the apartment interior. Controls architecture, materials, and geography only.
<<<audio_1>>>: voice reference for the spoken passage. Controls timbre and identity of the speaking voice only. No character from this reference appears on screen at any point.
<<<captain-agentv4>>>: adult male officer, tall, fully armored, no visible face. Pale grey-white composite dome helmet with a four-lens optical cluster hanging down over the entire face, olive-green tactical fabric with a high padded neck gaiter covering the jaw, mouth and throat, olive plate carrier with magazine pouches, white ID placard clipped at chest, thin grey cable running from the side of the helmet down to the vest, olive gloves, suppressed black carbine hanging on its sling. 100% matches the reference.
<<<char_dad>>>: 60yo East Asian man, thin build, grey-black hair swept back, grey stubble beard, worn olive-green open jacket over a brown waffle-knit shirt, dark brown trousers, barefoot. Kneeling, both hands laced behind his head. Alive and breathing. 100% matches the reference.
<<<char_son>>>: 20yo East Asian man, lean, black shoulder-length shaggy hair falling over his forehead, thin moustache and sparse chin stubble, oversized taupe-brown raw-seam sweatshirt, distressed wide brown trousers. Kneeling, both hands laced behind his head. Alive and breathing. 100% matches the reference.
<<<char_mum>>>: 50yo East Asian woman, slight build, grey hair pinned back in a low bun with loose strands, beige linen tunic under a dark charcoal vest, brown trousers, barefoot. Kneeling, both hands laced behind her head. Alive and breathing. 100% matches the reference.

CONTINUITY — STARTING STATE
The take starts on <<<image_1>>>, unchanged, and the first movement grows out of that image.
The subject in <<<image_1>>> is <<<char_dad>>>. His position, scale, posture, wardrobe and the room behind him are already correct and must not be re-staged, re-scaled, re-framed or re-lit at the start.
Nothing resets. No wardrobe change, no repositioning, no zoom-in or reframe onto him, no cut back to an earlier moment. The first thing that changes in the shot is his breathing, then the camera.
The light direction, exposure and color of <<<image_1>>> carry through the entire take. The window in <<<image_1>>> is the only light source and stays fixed in the room while the camera moves.

LOCATION MAP
<<<loc_family_apt>>> and <<<image_1>>> control architecture, materials, and geography.
One long room: white distempered walls, cracked ceiling, bare hanging bulb switched off, dark worn wooden floorboards.
Curtained window with grey overcast daylight: the wall at screen-left in <<<image_1>>>. Only light source. A low wooden bed with a dark blanket sits below and right of it.
A metal-legged table with a wooden chair stands against the wall at screen-right in <<<image_1>>>.
The three civilians kneel in a row on the open floorboards, all three facing the same direction, bodies turned away from the window wall.
Row order on the floor, fixed and never changing for the whole take:
<<<char_dad>>> kneels at one end of the row, nearest the bed and the window.
<<<char_son>>> kneels in the middle.
<<<char_mum>>> kneels at the far end, nearest the table.
Roughly 80 centimeters between each of them.
<<<captain-agentv4>>> stands 2 meters in front of the row, facing the three of them, squarely centered on the middle of the row. He is planted and does not move his feet at any point.
The camera begins at the position implied by <<<image_1>>>, walks a complete circle around <<<captain-agentv4>>>, and returns to that side of the room.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame is <<<image_1>>> itself. No other opening framing, no establishing shot, no empty frame, no delayed reveal, no push-in before the action starts.
All three civilians are physically present and kneeling from frame one, whether or not they are inside the frame. None appears late, none is added mid-shot.
<<<captain-agentv4>>> is already standing in his final position from frame one, out of frame, planted and facing the row. He never walks, never enters, never arrives.
By the end of the take the frame holds <<<captain-agentv4>>> seen from behind, with all three kneeling civilians visible beyond him.

CAMERA ORBIT LOCK
Between 0:08 and 0:22 the camera performs one complete, unbroken 360-degree orbit around <<<captain-agentv4>>>. The camera never stops, never pauses, never reverses direction, never holds a static frame during this stretch.
The orbit direction is constant throughout: the camera walks continuously in one rotational direction around him.
Orbit radius starts at 1.2 meters and widens gradually to 2.5 meters over the final quarter of the circle, so the framing opens naturally from a tight armor detail to a group composition without any lens change.
Because the orbit passes between <<<captain-agentv4>>> and the kneeling row, the camera briefly comes within 0.8 meters of the row without touching it. It never walks into the row, never steps behind the row, and never blocks a kneeling body with its own path.
As the camera travels, the background behind <<<captain-agentv4>>> rotates through the room in a physically consistent order: white wall, then the table and chair, then the kneeling row, then the window and bed, then back to the white wall. Backgrounds never jump, never repeat out of order, never teleport.
This orbit deliberately crosses the axis of the row. The row's left-to-right order in frame therefore reverses partway through the orbit, and this reversal is continuous and visible, never a cut. The physical positions of the three on the floor never change.
The orbit ends with the camera settled behind <<<captain-agentv4>>>, his back and both shoulders filling the foreground, the three kneeling civilians visible beyond him.

FORMAT MODE
SINGLE CONTINUOUS TAKE.

OPTICS
85mm-equivalent angle of view, approximately 29° diagonal field of view, short telephoto portrait lens character, matching the lens character already present in <<<image_1>>>. Background compresses close behind subjects and falls into soft bokeh. Subjects pop against a dissolved background.
Straight lines stay straight. Absolutely no barrel distortion, no fisheye curve, no wide-angle expansion, no stretched edges.
Anti-drift lock: no part of this shot becomes wide-angle or normal-lens coverage. The widening of the frame during the last quarter of the orbit is achieved purely by the operator's increasing physical distance, never by the lens opening up. The background stays compressed and soft in every frame, including the final group framing.

CAMERA
Naturalistic documentary handheld, shoulder-mounted, operator standing and walking. Not a stabilised rig. Objective third-person camera at all times, never a character's eyes.
Camera height starts at the height implied by <<<image_1>>>, rises to 1.5 meters during the move onto the officer, and stays there.
Movement path:
0:00 to 0:05 — held on <<<image_1>>>, no travel, breath and micro-correction only.
0:05 to 0:08 — the operator pans across the row and tilts up, passing <<<char_son>>> and <<<char_mum>>> in soft motion blur, arriving tight on <<<captain-agentv4>>> seen from behind, shoulders and helmet.
0:08 to 0:22 — the continuous 360-degree orbit described in the orbit lock, tight on armor for the first three quarters, widening through the last quarter.
0:22 to 0:25 — the operator settles into the final position behind him and holds, with only breath and micro-correction.
Handheld quality is physical and unglamorous: every walking step drops the frame vertically, the horizon tilts a degree and self-corrects, the arc is never geometrically perfect, corrections arrive late, operator breath moves the frame in shallow cycles. The orbit is a human walking a circle on old floorboards, not a mechanical rotation.
Focus behavior is documentary: focus sits on <<<char_dad>>>, hunts during the pan, resolves on the helmet at 0:08, holds the officer through the orbit with small continuous corrections as the distance changes, then racks past his shoulder onto the kneeling row at 0:22 while his back stays soft in the foreground.
No digital jitter, no random shake, no gimbal smoothness, no drone feel, no mechanical dolly or turntable feel, no zoom, no slow motion, no point-of-view framing, no helmet-cam look.

FACE AND SPEECH LOCK
<<<captain-agentv4>>>'s face is fully occluded. The four-lens optical cluster hangs over the upper and mid face. A thick padded neck gaiter covers the jaw, mouth and throat. There is no visible mouth at any point.
No lip movement is rendered. No lip shapes, no mouth opening, no teeth, no tongue, no visible articulation, no lipsync, no mouth animation of any kind.
The gaiter is thick structured fabric, not skin. It does not deform into lip shapes, does not stretch over a mouth, does not ripple in speech patterns, does not behave like a rubber membrane over a face.

JAW SIGNAL
The only physical sign of speech is at the jaw hinge and the throat, and it is subtle.
On stressed syllables, the padded gaiter shifts by one or two millimeters where it crosses the jaw hinge below the ear, and the fabric fold at the front of the throat moves slightly with the larynx.
The helmet itself does not nod, bob, or rock with the words. The head stays level.
No exaggerated jaw drop, no chewing motion, no bobbing head, no fabric pulsing in time with syllables.

LIVING BODY LOCK
<<<char_dad>>>, <<<char_son>>> and <<<char_mum>>> are living people holding a forced position under threat. Holding still is active physical effort, never a frozen image.
Continuous for all three: shallow irregular breathing visible in chest and shoulders, ribcage moving under fabric, micro-tremor in the raised arms, elbows sagging a few millimeters and lifting back, shoulders creeping up and settling, small weight shifts on the knees, blinking at irregular intervals with eyes downcast and wet, swallowing, jaw tension, loose hair and loose fabric moving with breath.
Differentiated:
- <<<char_dad>>>: deepest and slowest breathing, jaw set, steadiest arms, one slow swallow.
- <<<char_son>>>: fastest and least stable, visible tremor in forearms and shoulders, chest heaving, one elbow dropping and pulled back up.
- <<<char_mum>>>: shallowest breathing held high in the chest, two visible catches, fingers tightening and loosening behind her head.
When the officer begins speaking, none of them looks up. Their breathing shortens. <<<char_son>>>'s tremor increases.
<<<captain-agentv4>>> is also alive under the armor: his chest plate rises and falls slightly with breathing, the hanging carbine sways minutely on its sling, the helmet cable and ID placard move with his body.
No mannequin stillness, no frozen pose, no waxwork, no statue, no dead-eyed stare, no held breath across the whole shot.

ACTION TIMING
0:00 to 0:05 — Held on <<<image_1>>>. <<<char_dad>>> kneeling, head bowed, hands laced behind his head. Two full slow breath cycles visible in his shoulders and chest. He blinks once. His elbows sag and lift back. He does not look up. Silence except room tone and three sets of breathing.
0:05 to 0:08 — The camera pans across the row and tilts up, crossing <<<char_son>>> and <<<char_mum>>> in motion blur, and arrives tight on <<<captain-agentv4>>> from behind, shoulders and helmet filling the frame. He stands planted, weight even, gloved hands loose at his sides, carbine hanging on its sling.
0:08 to 0:09 — The orbit begins. The camera starts walking. It does not stop again until 0:22.
0:09 to 0:10.5 — Still orbiting. He speaks: "Demographic control." His body does not move. Only the jaw signal at the gaiter.
0:10.5 to 0:12 — Silence. The orbit continues without pause. Room tone and breathing.
0:12 to 0:17.5 — Still orbiting, now passing his front. He speaks: "Present your birth code for verification under the current quota regulations." His helmet stays level. He does not turn to follow the camera.
0:17.5 to 0:19.5 — Silence. The orbit continues, widening. The kneeling row rotates into the background behind him.
0:19.5 to 0:25 — The orbit completes and settles into the final framing behind him during the first seconds of the line. He speaks: "Left wrist, palm up. The procedure is mandatory. Refusal, obstruction, or tampering with the code constitutes non-compliance."
Nobody obeys. Nobody lowers their hands. Nobody looks up. The three keep breathing. The take ends on the held framing of his back and the row beyond, on the last word, without resolution.

DIALOGUE RULES
Only the scripted passage is spoken, exactly as written, in this order and no other words:
"Demographic control."
"Present your birth code for verification under the current quota regulations."
"Left wrist, palm up. The procedure is mandatory. Refusal, obstruction, or tampering with the code constitutes non-compliance."
No ad-libs, no repetition, no paraphrase, no additional commands, no radio chatter, no responses from anyone.
The three kneeling civilians never speak. Their lips stay closed for the entire take.
The voice is a pickup output, not visible speech. Nothing in frame is seen forming words.

PHYSICS
<<<captain-agentv4>>> carries real weight: armor plates settle against each other, the carbine hangs with visible mass on its sling and sways minutely, the helmet cable and clipped ID placard hang under gravity and move slightly with his breathing. His feet stay planted; he does not sway, drift, or rotate.
The kneeling bodies carry real weight through knees and shins. Ankles and toes bear load. Breathing drives continuous small motion through torso, shoulders and clothing. Loose fabric on <<<char_son>>>'s oversized sweatshirt hangs and shifts with every breath. Loose strands of <<<char_mum>>>'s hair move on exhale.
Old floorboards creak and give under the operator's walking steps throughout the orbit.
No floating motion, no weightless weapons, no frictionless feet, no rubbery CG movement, no game-engine look, no frozen human bodies.

LIGHTING
One source only, established by <<<image_1>>>: thin grey overcast daylight through the curtained window. No sun, no warmth, no visible beam. The hanging bulb stays off. No lamp is switched on in the room.
The light stays fixed in the room while the camera moves around it. As the camera orbits, the key wraps continuously across <<<captain-agentv4>>>: he passes from rim-lit at the back of the helmet, through a hard side key on one shoulder, to near-silhouette against the bright window, and back. This transition is smooth and physically consistent with a single fixed window.
The kneeling civilians stay lit from the window side, faces angled down and held in soft shadow, with a faint wet catchlight in the downcast eyes. Rim light along their shoulders rises and falls visibly with their breathing.
The helmet stays a dull matte grey-white, never bright, never glossy. Armor reads dark and desaturated.
Exposure and color grade match <<<image_1>>> throughout and do not shift during the orbit.
No flat front light, no beauty fill, no studio key, no light from camera position, no colored light of any kind.

AUDIO
Diegetic only. Exactly the scripted passage, spoken in the voice of <<<audio_1>>>. No other words from anyone.
Low building hum. Three distinct sets of human breathing, close and audible from 0:00 to 0:25, never stopping: one deep and slow, one fast and unsteady, one shallow and high with catches. The breathing is the human floor of the entire soundtrack and remains faintly audible under the dialogue.
Continuous floorboard creaks and soft footfalls from the moving camera between 0:08 and 0:22.
Faint armor and fabric noise from <<<captain-agentv4>>> standing.
0:09, 0:12 and 0:19.5: the three scripted lines, voice matched to <<<audio_1>>>.
Delivery: procedural, flat, unraised. Not a shout, not a threat. A phrase said a thousand times. No urgency, no emphasis, no rising inflection, flat terminal fall on every sentence. The pauses between lines are dead air, not dramatic holds.
Voice processing: heavily compressed and band-limited, as through a helmet pickup. Narrow midrange, rolled-off lows and highs, close and dry with no room reverb, slightly clipped consonants. The voice sits closer to the listener than the room does, and its level does not change as the camera orbits.
Ambient sound ducks under each line and returns after it.
No music, no score, no subtitles, no radio chatter, no other offscreen voices, no crying, no whimpering, no vocalisations.

POSITIVE CONSTRAINTS
The take begins on <<<image_1>>> exactly, with no alteration to that image.
Exactly three civilians in the room: <<<char_dad>>>, <<<char_son>>>, <<<char_mum>>>. All three kneel on the floorboards for the entire take, present from frame one whether or not they are in frame, breathing whenever visible. No duplicates, no additional civilians, no children, nobody in the background.
Exactly one armored figure: <<<captain-agentv4>>>. No other agents are visible at any point, from any angle of the orbit.
<<<audio_1>>> contributes voice only. No additional character, body, or figure is generated from it.
The three kneeling civilians stay in the same physical spots on the floor for the whole take. Their apparent left-to-right order in frame changes only because the camera moves around them.
The kneeling three never stand, never turn, never look up, never lower their hands, never speak.
<<<captain-agentv4>>> never kneels, never crouches, never raises his weapon, never touches anyone, never removes his helmet, never turns to face the camera, never tracks the camera with his head.
The orbit is continuous and completes a full circle. The camera never stops between 0:08 and 0:22.
Kodak Vision3 500T, naturalistic low-key cold daylight, real grain, grounded physical cinema texture, no blur, no ghosting, no flickering.

NEGATIVE CONSTRAINTS — LIGHT EMISSION
No glowing helmet lenses. The four optical cluster lenses stay dark, dead, unlit glass for the entire take, from every angle of the orbit.
No blue glow, no cyan glow, no white glow, no glow of any color from any lens.
No internal illumination behind the lenses, no emissive rings, no lit apertures, no scanner beams, no projected light, no laser lines.
No LEDs anywhere: not on the helmet, not on the plate carrier, not on the ID placard, not on the weapon, not on optics or sights, not on gloves, not on any pouch or piece of gear.
No status lights, no indicator lights, no recorder light, no charging lights, no blinking dots, no small glowing points on any part of the equipment.
No glowing weapon optics. No illuminated reticles, no lit red dot sights, no lit rangefinders.
No light spilling from the helmet onto the gaiter, the shoulders, the wall, or the floorboards. No colored bounce from equipment onto any surface.
No screens, panels, or displays are switched on anywhere in the room.
The lenses may only carry faint passive reflections of existing room light. A reflection is never a source: it does not brighten surrounding surfaces and never appears when the surroundings are dark.
````

### Generated videos

- 2026-09-01 09:33:35 · [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260901_093335_dc2e7a67-5fc9-4776-92dd-9fc7a9e9bcdb.mp4)

## Earlier versions

Oldest first. Compare against the final to see what the author changed between attempts.

<details><summary>v1 · 2026-09-01 09:05:59 · 1 generation(s) · 007_20260901_090559_91f71296.md</summary>

````text
SCENE CONTEXT
Continuation shot inside the same apartment. The camera holds on the kneeling father, then finds the helmeted officer standing over the row, then opens out to hold the officer and all three kneeling civilians together as he delivers a procedural order.

OUTPUT SETTINGS
Single continuous handheld take, 25 seconds, real-time motion, no internal cuts. One continuous spoken passage, delivered offscreen-voiced through a helmet pickup. No subtitles, no captions, no music.

CONTINUITY — STARTING STATE
This shot begins exactly where the previous one ended, same room, same light, same bodies, same wardrobe, same second.
Opening frame reproduces the previous final frame: <<<char_dad>>> kneeling, centered in frame, framed from mid-chest up, both hands laced behind his head, elbows raised and wide, head bowed forward, eyes downcast and nearly closed, mouth closed. Worn dark olive-green open jacket over a brown waffle-knit shirt.
Behind him: white distempered wall across the center and right of frame, a curtained window with grey daylight at the far screen-left, a low wooden bed with a dark folded blanket in the mid-ground screen-left, a metal-legged table with a chair at screen-right.
Light comes from screen-left, cold and soft. His right side is lit, his screen-right side falls into shadow.
Nothing resets. No wardrobe change, no repositioning, no cut back to an earlier moment.

ACTIVE REFERENCES
<<<loc_family_apt>>>: the apartment interior. Controls architecture, materials, and geography only.
<<<audio_1>>>: voice reference for the spoken passage. Controls timbre and identity of the speaking voice only. No character from this reference appears on screen at any point.
<<<captain-agentv4>>>: adult male officer, tall, fully armored, no visible face. Pale grey-white composite dome helmet with a four-lens optical cluster covering the entire face, olive-green tactical fabric with high padded neck gaiter, olive plate carrier with magazine pouches, white ID placard clipped at chest, thin grey cable running from the side of the helmet down to the vest, olive gloves, suppressed black carbine hanging on its sling. 100% matches the reference.
<<<char_dad>>>: 60yo East Asian man, thin build, grey-black hair swept back, grey stubble beard, worn olive-green open jacket over a brown waffle-knit shirt, dark brown trousers, barefoot. Kneeling, both hands laced behind his head. Alive and breathing. 100% matches the reference.
<<<char_son>>>: 20yo East Asian man, lean, black shoulder-length shaggy hair falling over his forehead, thin moustache and sparse chin stubble, oversized taupe-brown raw-seam sweatshirt, distressed wide brown trousers. Kneeling, both hands laced behind his head. Alive and breathing. 100% matches the reference.
<<<char_mum>>>: 50yo East Asian woman, slight build, grey hair pinned back in a low bun with loose strands, beige linen tunic under a dark charcoal vest, brown trousers, barefoot. Kneeling, both hands laced behind her head. Alive and breathing. 100% matches the reference.

LOCATION MAP
<<<loc_family_apt>>> controls architecture, materials, and geography.
One long room: white distempered walls, cracked ceiling, bare hanging bulb switched off, dark worn wooden floorboards.
Curtained window with grey overcast daylight: far wall, screen-left. Only light source. A low wooden bed with a dark blanket sits below and right of it.
A metal-legged table with a chair stands against the wall at screen-right.
The three civilians kneel in a row on the open floorboards, all three facing the same direction, bodies turned away from the window wall.
Row order on the floor, fixed and never changing for the whole take:
<<<char_dad>>> kneels at the screen-left end of the row, nearest the bed and the window.
<<<char_son>>> kneels in the middle of the row.
<<<char_mum>>> kneels at the screen-right end of the row, nearest the table.
The gap between each of them is roughly 80 centimeters.
<<<captain-agentv4>>> stands facing the row, on the camera side of it, screen-right of the group.
Camera operates from a single area of floor 2 to 3 meters from the row, on the side the three are facing. It pans, tilts, and steps back, but never crosses behind the row and never goes to the window wall.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame is <<<char_dad>>>, already in position, framed mid-chest up, centered, hands laced behind his head, head bowed. No empty frame, no establishing shot, no delayed reveal.
All three civilians are physically present and kneeling on the floorboards from frame one, whether or not they are inside the frame. None appears late, none is added mid-shot.
<<<captain-agentv4>>> is already standing in the room from frame one, out of frame screen-right, in his final position facing the row. He does not walk in, does not arrive, does not enter from a door.
By the end of the take the frame holds <<<captain-agentv4>>> and all three kneeling civilians at once.

LIVING BODY LOCK
<<<char_dad>>>, <<<char_son>>> and <<<char_mum>>> are living people holding a forced position under threat. They hold still, but holding still is active physical effort, never a frozen image.
Continuous throughout the take, for all three:
- Real breathing. Chest and shoulders rise and fall in visible cycles, shallow, slightly irregular, with occasional held breaths and quicker releases. The ribcage moves under the fabric.
- Micro-tremor in the raised arms. Elbows sag a few millimeters and are lifted back up. Shoulders creep up and settle. Forearms show a faint continuous shake.
- Small involuntary weight shifts on the knees, hips easing side to side by a few millimeters.
- Blinking. Eyes angled down at the floor but open and wet, blinking at irregular intervals.
- Swallowing, jaw tension, a faint pulse at the neck, nostrils flaring slightly on inhale.
- Loose hair moves with breath. Loose fabric hangs and shifts with the body.
Differentiated:
- <<<char_dad>>>: deepest and slowest breathing, jaw set, steadiest arms. One slow swallow. The stillness of practice.
- <<<char_son>>>: fastest and least stable. Visible tremor in forearms and shoulders, chest heaving, one elbow dropping and pulled back up.
- <<<char_mum>>>: shallowest breathing, held high in the chest, two visible catches where the breath stops and restarts. Fingers tightening and loosening behind her head.
When the officer begins speaking at 0:09, none of them looks up. Their breathing shortens. <<<char_son>>>'s tremor increases.
No mannequin stillness, no frozen pose, no waxwork, no statue, no dead-eyed stare, no held breath across the whole shot, no perfectly repeating identical breathing cycle.

FORMAT MODE
SINGLE CONTINUOUS TAKE.

OPTICS
85mm-equivalent angle of view, approximately 29° diagonal field of view, short telephoto portrait lens character, camera 2 to 3.5 meters from subjects. Background compresses close behind subjects and falls into soft bokeh. Subjects pop against a dissolved background.
Straight lines stay straight. Absolutely no barrel distortion, no fisheye curve, no wide-angle expansion, no stretched edges.
Anti-drift lock: no part of this shot becomes wide-angle or normal-lens coverage. The final wider framing is achieved by the operator physically stepping backward with the same long-lens reach, never by the lens opening up. The background stays compressed and soft in every frame, including the final framing.
Because of the lens, the final group framing is an over-shoulder composition: <<<captain-agentv4>>>'s back and shoulder occupy the screen-right foreground, large and close, and the three kneeling civilians are held beyond him across the screen-left and center of frame.

CAMERA
Naturalistic documentary handheld, shoulder-mounted, operator standing. Not a stabilised rig. Objective third-person camera at all times, never a character's eyes.
Camera height starts at 1.2 meters, roughly level with the kneeling heads.
Movement path:
0:00 to 0:05 — held on <<<char_dad>>>, no travel, breath and micro-correction only.
0:05 to 0:09 — the operator pans screen-right along the row and tilts up, passing across <<<char_son>>> and <<<char_mum>>> in soft blur, and settles on <<<captain-agentv4>>> standing over them. The camera rises to 1.5 meters during the pan.
0:09 to 0:17.5 — held on <<<captain-agentv4>>>, tight, from waist to helmet, slight low angle. Breath and micro-correction only.
0:17.5 to 0:19.5 — the operator steps two real paces backward and pans screen-left, opening the frame into the over-shoulder group composition.
0:19.5 to 0:25 — held on the group composition. No further travel.
Handheld quality is physical and unglamorous: pans overshoot the subject and pull back, the backward steps drop the frame vertically twice, corrections arrive late, operator breath moves the frame in shallow cycles.
Focus behavior is documentary: focus sits on <<<char_dad>>>, hunts during the pan, resolves on <<<captain-agentv4>>>'s helmet at 0:09, then racks back to the kneeling row during the reframe at 0:18 while the officer's shoulder stays soft in the foreground.
No digital jitter, no random shake, no gimbal smoothness, no floating drone feel, no mechanical dolly feel, no zoom, no slow motion, no point-of-view framing, no helmet-cam look.

ACTION TIMING
0:00 to 0:05 — <<<char_dad>>> kneeling, framed mid-chest up, head bowed, hands laced behind his head. Two full slow breath cycles are visible in his shoulders and chest. He blinks once. His elbows sag and lift back. He does not look up. Silence except room tone and three sets of breathing.
0:05 to 0:09 — The camera pans screen-right and tilts up, crossing <<<char_son>>> and then <<<char_mum>>> in motion blur, both kneeling in the same posture, and settles on <<<captain-agentv4>>> standing over the row, framed waist to helmet, slightly low angle. He stands still, weight even, carbine hanging on its sling, gloved hands loose at his sides. No face is visible behind the helmet.
0:09 to 0:10.5 — He speaks. The voice comes through the helmet pickup: "Demographic control." His body does not move while speaking. No gesture, no head turn, no shift of weight.
0:10.5 to 0:12 — Silence. He does not move. Below him the three kneeling civilians keep breathing, heads down.
0:12 to 0:17.5 — He speaks: "Present your birth code for verification under the current quota regulations." Still no movement from his body.
0:17.5 to 0:19.5 — Silence. During this pause the camera steps back twice and pans screen-left, opening into the over-shoulder framing: <<<captain-agentv4>>>'s back and shoulder large in the screen-right foreground, <<<char_mum>>>, <<<char_son>>> and <<<char_dad>>> kneeling beyond him across the frame, all three still in position with hands laced behind their heads.
0:19.5 to 0:25 — He speaks the final passage over the group framing: "Left wrist, palm up. The procedure is mandatory. Refusal, obstruction, or tampering with the code constitutes non-compliance." Nobody obeys yet. Nobody lowers their hands. Nobody looks up. The three keep breathing. The take ends on the held group framing, on the last word, without resolution.

DIALOGUE RULES
Only the scripted passage is spoken, exactly as written, in this order and no other words:
"Demographic control."
"Present your birth code for verification under the current quota regulations."
"Left wrist, palm up. The procedure is mandatory. Refusal, obstruction, or tampering with the code constitutes non-compliance."
No ad-libs, no repetition, no paraphrase, no additional commands, no radio chatter, no responses from anyone.
The three kneeling civilians never speak and never open their mouths. Their lips stay closed for the entire take.
<<<captain-agentv4>>>'s face is fully covered by the helmet. No mouth is visible, no lip movement is rendered, no jaw motion. The voice is a pickup output, not visible speech.

PHYSICS
<<<captain-agentv4>>> carries real weight: armor plates settle against each other, the carbine hangs with visible mass on its sling and sways minutely, the thin helmet cable and the clipped ID placard hang under gravity and move slightly with his breathing. He stands with weight distributed on both feet and does not sway or drift.
The kneeling bodies carry real weight through knees and shins. Ankles and toes bear load. Breathing drives continuous small motion through torso, shoulders and clothing. Loose fabric on <<<char_son>>>'s oversized sweatshirt hangs, shifts and settles with every breath. Loose strands of <<<char_mum>>>'s hair move on exhale.
Old floorboards give and creak under the operator's backward steps.
No floating motion, no weightless weapons, no frictionless feet, no rubbery CG movement, no game-engine look, no frozen human bodies.

LIGHTING
One source only: thin grey overcast daylight through the curtained window on the far wall, screen-left. No sun, no warmth, no visible beam. The hanging bulb stays off. No lamp is switched on in the room.
Light falls from screen-left across the room. The kneeling civilians are lit on their screen-left side and fall into shadow on their screen-right side. Faces are angled down and stay in soft shadow, with a faint wet catchlight in the downcast eyes. Rim light along their shoulders rises and falls visibly with their breathing.
<<<captain-agentv4>>> stands screen-right, further from the window: his armor reads dark and desaturated, with a cold soft edge along his screen-left side and the top of the helmet dome. The helmet stays a dull matte grey-white, never bright, never glossy.
Exposure is set for the grey window light and the white wall, not for skin.
No flat front light, no beauty fill, no studio key, no light from camera position, no colored light of any kind.

AUDIO
Diegetic only. Exactly the scripted passage, spoken in the voice of <<<audio_1>>>. No other words from anyone.
Low building hum. Three distinct sets of human breathing, close and audible from 0:00 to 0:25, never stopping: one deep and slow, one fast and unsteady, one shallow and high with catches. The breathing is the human floor of the entire soundtrack and remains faintly audible underneath the dialogue.
Faint armor and fabric noise from <<<captain-agentv4>>> standing.
Floorboard creaks under the camera's backward steps at 0:18.
0:09, 0:12 and 0:19.5: the three scripted lines, voice matched to <<<audio_1>>>.
Delivery: procedural, flat, unraised. Not a shout, not a threat. A phrase said a thousand times. No urgency, no emphasis, no rising inflection, flat terminal fall on every sentence. The pauses between the three lines are dead air, not dramatic holds.
Voice processing: heavily compressed and band-limited, as through a helmet pickup. Narrow midrange, rolled-off lows and highs, close and dry with no room reverb, slightly clipped consonants. The voice sits closer to the listener than the room does.
Ambient sound ducks under each line and returns after it.
No music, no score, no subtitles, no radio chatter, no other offscreen voices, no crying, no whimpering, no vocalisations.

POSITIVE CONSTRAINTS
Exactly three civilians in the room: <<<char_dad>>>, <<<char_son>>>, <<<char_mum>>>. All three kneel on the floorboards for the entire take, present from frame one whether or not they are in frame, breathing whenever visible. No duplicates, no additional civilians, no children, nobody in the background.
Exactly one armored figure: <<<captain-agentv4>>>. No other agents are visible at any point.
<<<audio_1>>> contributes voice only. No additional character, body, or figure is generated from it.
The row order is <<<char_dad>>> screen-left, <<<char_son>>> center, <<<char_mum>>> screen-right, and never changes.
The kneeling three never stand, never turn, never look up, never lower their hands, never speak.
<<<captain-agentv4>>> never kneels, never crouches, never raises his weapon, never touches anyone, never removes his helmet.
The camera never crosses behind the row, never turns around, and never sees a face behind the helmet.
The final framing holds <<<captain-agentv4>>> and all three civilians simultaneously.
Kodak Vision3 500T, naturalistic low-key cold daylight, real grain, grounded physical cinema texture, no blur, no ghosting, no flickering.

NEGATIVE CONSTRAINTS — LIGHT EMISSION
No glowing helmet lenses. The four optical cluster lenses stay dark, dead, unlit glass for the entire take.
No blue glow, no cyan glow, no white glow, no glow of any color from any lens.
No internal illumination behind the lenses, no emissive rings, no lit apertures, no scanner beams, no projected light, no laser lines.
No LEDs anywhere: not on the helmet, not on the plate carrier, not on the ID placard, not on the weapon, not on optics or sights, not on gloves, not on any pouch or piece of gear.
No status lights, no indicator lights, no recorder light, no charging lights, no blinking dots, no small glowing points on any part of the equipment.
No glowing weapon optics. No illuminated reticles, no lit red dot sights, no lit rangefinders.
No light spilling from the helmet onto the face gaiter, the shoulders, the wall, or the floorboards. No colored bounce from equipment onto any surface.
No screens, panels, or displays are switched on anywhere in the room.
The lenses may only carry faint passive reflections of existing room light. A reflection is never a source: it does not brighten surrounding surfaces and never appears when the surroundings are dark.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260901_090559_91f71296-f067-4dce-a17e-89e93b991dfa.mp4)

</details>
