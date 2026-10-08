# scene-08-05 · Continuation shot inside the same apartment.

[← Index](../../INDEX.md) · Scene: **SCENE 08**

| | |
|---|---|
| Shot size | Wide |
| Camera | Handheld |
| Format | Single take · 25s · 21:9 · 1080p |
| Sound | Dialogue · No music |
| Model | seedance_2_5 |
| Characters | captain-agentv4, char_dad, char_mum, char_son, team2 |
| Location | loc_family_apt |
| Props | — |
| Iterations | 3 prompt version(s), 3 generation(s) total |

**Sections:** SCENE CONTEXT → OUTPUT SETTINGS → SCRIPT LOCK — DIALOGUE IS FIXED → SET LOCK — NOTHING IS INVENTED → BLOCKING LOCK — POSITIONS ARE FIXED → CAMERA INDEPENDENCE LOCK — NOT BODY-MOUNTED → ACTIVE REFERENCES → CONTINUITY — STARTING STATE → OCCUPANCY LOCK → LOCATION MAP → FIRST FRAME AND SPATIAL BLOCKING → CAMERA ORBIT LOCK → FORMAT MODE → SINGLE CONTINUOUS TAKE. → OPTICS → CAMERA → FACE AND SPEECH LOCK → JAW SIGNAL → LIVING BODY LOCK → ACTION TIMING → DIALOGUE RULES → PHYSICS → LIGHTING → AUDIO → POSITIVE CONSTRAINTS → NEGATIVE CONSTRAINTS — LIGHT EMISSION

## Final prompt (latest version)

_Element IDs replaced with names. Original with IDs: [017_20260901_103742_620fd8fd.md](../../../prompts/04_FOOTAGE/SCENE%2008/017_20260901_103742_620fd8fd.md)_

````text
SCENE CONTEXT
Continuation shot inside the same apartment. The camera holds on the kneeling father, finds the helmeted officer standing over the row, then walks all the way around him in one unbroken move while he delivers a procedural order, revealing the broken-open door and the agents holding behind him, and settles behind him with all three kneeling civilians visible beyond his shoulders.

OUTPUT SETTINGS
Single continuous handheld take, 25 seconds, real-time motion, no internal cuts. One continuous spoken passage, delivered through a helmet pickup. No subtitles, no captions, no music.

SCRIPT LOCK — DIALOGUE IS FIXED
The spoken content of this shot is closed. Exactly three sentences are spoken in the entire take, in this order, word for word:
1. "Demographic control."
2. "Present your birth code for verification under the current quota regulations."
3. "Left wrist, palm up. The procedure is mandatory. Refusal, obstruction, or tampering with the code constitutes non-compliance."
Do not invent, add, extend, shorten, reorder, paraphrase or improvise any line. Do not generate a fourth sentence. Do not add greetings, warnings, callouts, confirmations, numbers, codes, names, acknowledgements or reactions. Do not have any character answer, repeat, echo or respond.
Every one of these lines is spoken by <<<captain-agentv4>>> alone, using the voice of <<<audio_1>>> and no other voice. No other character in the room or the corridor speaks a single word.
If the shot has silence to fill, it stays silent. Silence is correct. Invented speech is not.

SET LOCK — NOTHING IS INVENTED
The world of this shot is closed. It consists of exactly one room and one corridor visible through one doorway. Nothing else exists and nothing else may be generated.
There is exactly ONE door in this shot: the pale green forced-open apartment door on its wall. No second door, no other doorway, no archway, no opening, no passage, no hatch, no window onto another space, no stairwell, no adjoining room, no hallway other than the single corridor beyond that one door.
The room contains only what is listed in the LOCATION MAP: white distempered walls, cracked ceiling, one switched-off hanging bulb, dark wooden floorboards, one curtained window, one low wooden bed with a dark blanket, one metal-legged table with one wooden chair, and the forced green door.
Do not add furniture, appliances, cabinets, shelves, wardrobes, mirrors, pictures, posters, signage, rugs, plants, lamps, screens, curtains beyond the one window, radiators beyond the one under the window, or clutter of any kind.
Do not enlarge the room, do not add depth, do not open the space out, do not reveal a further area behind any wall.
Do not add exterior environment beyond the window: the window shows only a flat grey overcast brightness, no city, no landscape, no buildings, no sky detail.
The corridor beyond the one door is a bare passage with a white upper wall and a green lower wall and one fluorescent tube. It contains nothing else: no furniture, no other doors, no stairs, no windows.
If the camera's path reaches an angle where the model has no reference for what is there, it shows plain wall. A blank wall is correct. An invented room is not.

BLOCKING LOCK — POSITIONS ARE FIXED
Every character's position on the floor is already defined below and is final. Nobody may be placed anywhere else, at any moment, from any camera angle.
Nobody walks, steps, shuffles, kneels down, stands up, edges sideways, changes their distance from anyone else, or ends up on a different part of the floor than where they start. Nobody swaps places with anyone.
The kneeling row keeps its exact spacing and its exact order for the whole take. <<<captain-agentv4>>> stays on his single spot facing them. The single interior agent stays on his single spot behind the officer. The two corridor agents stay out in the corridor.
When the camera moves, the characters do not move to accommodate the new angle. Their apparent arrangement in frame changes only because the camera has changed position around them.
Do not restage the scene for a better composition. Do not relocate a character to keep them in frame. If a character falls out of frame, they are simply out of frame, still standing or kneeling exactly where they were.

CAMERA INDEPENDENCE LOCK — NOT BODY-MOUNTED
The camera is an independent observer standing on the floor of the room. It is not attached to <<<captain-agentv4>>> in any way.
It is not parented to his body, not rigged to his shoulder, not mounted on his chest, not fixed to his helmet, not orbiting as if bolted to an armature around him.
Parallax is mandatory and is the test of this. As the operator walks around him, the room behind him must visibly slide, rotate and change: the window wall passes, the table and chair pass, the doorway passes, the kneeling row passes. Near objects shift faster than far objects. The background is never pinned behind him.
His position within the frame must change independently of the background. He is not locked to the center. He drifts across frame as the operator walks and is loosely re-found.
His scale in frame changes as the operator's distance changes. The camera does not maintain a fixed distance to him.
Absolutely no shot where the officer appears static while only the background spins behind him. No turntable effect, no rotating backdrop, no character-locked tracking, no subject stabilisation, no "camera glued to the actor" motion.
<<<captain-agentv4>>> does not rotate, does not pivot, does not turn to stay facing the camera, and does not track the lens with his helmet. He faces the kneeling row for the entire take while the camera moves around him.

ACTIVE REFERENCES
<<<image_1>>>: the exact first frame of this shot. The take begins on this image and moves out of it. It controls opening framing, composition, subject position and scale, room layout, light direction, exposure, and color.
<<<loc_family_apt>>>: the apartment interior. Controls architecture, materials, and geography only.
<<<audio_1>>>: the voice used for every spoken line in this shot. Controls timbre and identity of the speaking voice only. No character from this reference appears on screen at any point.
<<<captain-agentv4>>>: adult male officer, tall, fully armored, no visible face. Pale grey-white composite dome helmet with a four-lens optical cluster hanging down over the entire face, olive-green tactical fabric with a high padded neck gaiter covering the jaw, mouth and throat, olive plate carrier with magazine pouches, white ID placard clipped at chest, thin grey cable running from the side of the helmet down to the vest, olive gloves, suppressed black carbine hanging on its sling. 100% matches the reference.
<<<team2>>>: identical armored agents, same helmets, same four-lens optical cluster, same olive gear, same white ID placards, no visible faces, suppressed black carbines. No recorder unit on their chests. 100% matches the reference.
<<<char_dad>>>: 60yo East Asian man, thin build, grey-black hair swept back, grey stubble beard, worn olive-green open jacket over a brown waffle-knit shirt, dark brown trousers, barefoot. Kneeling, both hands laced behind his head. Alive and breathing. 100% matches the reference.
<<<char_son>>>: 20yo East Asian man, lean, black shoulder-length shaggy hair falling over his forehead, thin moustache and sparse chin stubble, oversized taupe-brown raw-seam sweatshirt, distressed wide brown trousers. Kneeling, both hands laced behind his head. Alive and breathing. 100% matches the reference.
<<<char_mum>>>: 50yo East Asian woman, slight build, grey hair pinned back in a low bun with loose strands, beige linen tunic under a dark charcoal vest, brown trousers, barefoot. Kneeling, both hands laced behind her head. Alive and breathing. 100% matches the reference.

CONTINUITY — STARTING STATE
The take starts on <<<image_1>>>, unchanged, and the first movement grows out of that image.
The subject in <<<image_1>>> is <<<char_dad>>>. His position, scale, posture, wardrobe and the room behind him are already correct and must not be re-staged, re-scaled, re-framed or re-lit at the start.
Nothing resets. No wardrobe change, no repositioning, no zoom-in or reframe onto him, no cut back to an earlier moment. The first thing that changes in the shot is his breathing, then the camera.
The light direction, exposure and color of <<<image_1>>> carry through the entire take. The window in <<<image_1>>> is the only light source in the room and stays fixed while the camera moves.
The apartment door was forced open before this shot and stays open for the whole take. Nobody closes it, nobody moves it, nobody enters or exits through it.

OCCUPANCY LOCK
Exactly five figures are inside the room for the whole take, and no more:
<<<char_dad>>>, <<<char_son>>> and <<<char_mum>>>, kneeling in a row.
<<<captain-agentv4>>>, standing in front of them.
One single <<<team2>>> agent, standing behind the officer.
Every other agent is out in the corridor, beyond the open doorway, and stays there. Two <<<team2>>> agents hold the corridor.
This count never changes. Nobody enters the room, nobody leaves it, no additional agent walks in from the corridor, no extra figure appears from any angle of the camera's walk. The room contains five people from the first frame to the last.

LOCATION MAP
<<<loc_family_apt>>> and <<<image_1>>> control architecture, materials, and geography.
One long room: white distempered walls, cracked ceiling, bare hanging bulb switched off, dark worn wooden floorboards.
Curtained window with grey overcast daylight: the wall at screen-left in <<<image_1>>>. Only light source in the room. A low wooden bed with a dark blanket sits below and right of it.
A metal-legged table with a wooden chair stands against the wall at screen-right in <<<image_1>>>.
The apartment door, the only door in the shot: pale green painted wood, forced open inward, hanging on its hinges with the lock plate torn out and splinters at the jamb. It stands open against the wall and does not move. Beyond it a bare corridor lit by one cold fluorescent tube, white wall above and green below.
The three civilians kneel in a row on the open floorboards, all three facing the door, bodies turned away from the window wall.
Row order on the floor, fixed and never changing for the whole take:
<<<char_dad>>> kneels at one end of the row, nearest the bed and the window.
<<<char_son>>> kneels in the middle.
<<<char_mum>>> kneels at the far end, nearest the table.
Roughly 80 centimeters between each of them.
<<<captain-agentv4>>> stands 2 meters in front of the row, facing the three of them, squarely centered on the middle of the row. His back is toward the open door. He is planted and does not move his feet at any point.
Standing order along the room's axis, fixed: the kneeling row, then <<<captain-agentv4>>>, then the single <<<team2>>> agent, then the open doorway, then the corridor.
The single <<<team2>>> agent inside the room entered first and holds a position 1.5 meters behind <<<captain-agentv4>>> and slightly to one side, between the officer and the open door, carbine lowered on its sling. He does not move his feet at any point.
The two corridor <<<team2>>> agents stand beyond the open doorway, framed by the door opening, carbines raised. They hold the corridor and never cross the threshold.
The camera stays inside the room for the whole take. It never passes through the doorway, never films from the corridor.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame is <<<image_1>>> itself. No other opening framing, no establishing shot, no empty frame, no delayed reveal, no push-in before the action starts.
All three civilians are physically present and kneeling from frame one, whether or not they are inside the frame. None appears late, none is added mid-shot.
<<<captain-agentv4>>> and all three <<<team2>>> agents are already in their final positions from frame one, out of frame. Nobody walks, nobody enters, nobody arrives, nobody leaves during the take.
By the end of the take the frame holds <<<captain-agentv4>>> seen from behind, with all three kneeling civilians visible beyond him.

CAMERA ORBIT LOCK
Between 0:08 and 0:22 the operator walks all the way around <<<captain-agentv4>>> on foot and ends up where he started. He is a person carrying a camera on his shoulder while stepping around a standing man in a cramped room, not a rig on a track and not attached to that man. The circle is the result of his path, never the instruction.
Continuity: he never stops, never pauses, never reverses direction, never holds a static frame during this stretch. Direction of travel is constant.
Gait: the path is walked in real footsteps on old floorboards. Each footfall drops the frame vertically by a small uneven amount. The steps are not evenly spaced and not evenly timed. Two of them land heavier than the others. Weight transfers heel to toe and the shoulder mass settles a beat after each step.
Path shape: the route is a rough polygon, not a smooth arc. He walks three or four short straight segments and corrects direction between them, so the framing drifts off the officer and is pulled back, repeatedly. Every correction arrives late and slightly overshoots before resolving.
Radius: the distance breathes between 1.0 and 1.6 meters through the first three quarters, never constant, then opens to 2.5 meters over the final quarter as he steps outward and back. The subject's size in frame therefore changes continuously and unevenly.
Speed: the walk is not uniform. He slows twice, once where the floor narrows near the kneeling row and once as he clears the corner of the table, then picks the pace back up. Both slowdowns are physical hesitations, not dramatic beats.
Framing: the officer is not centered and does not stay centered. He sits off-center and slides across the frame as the operator walks, held loosely rather than locked. The horizon tilts a degree or two and self-corrects. The camera height rises and falls a few centimeters with the operator's stride.
Breath: the operator's breathing moves the frame in slow shallow cycles underneath all of the above, and becomes slightly heavier in the last third of the walk.
Room containment: on the segment that passes between <<<captain-agentv4>>> and the open door, the operator tightens his path so he stays at least 1 meter inside the room and never reaches the threshold. He stays on the room floorboards for every frame.
On the segment that passes between <<<captain-agentv4>>> and the kneeling row, he comes within 0.8 meters of the row without touching it, turns his shoulders to clear the space, and the frame swings with that turn. He never walks into the row, never steps behind the row, never blocks a kneeling body with his own path.
As he travels, the background behind <<<captain-agentv4>>> rotates through the room in a physically consistent order and returns to where it began: the kneeling row and the far wall, then the table and chair wall, then the open doorway with the single <<<team2>>> agent in front of it and the two corridor agents framed in the opening, then the bed and the window wall, then back to the kneeling row. Backgrounds never jump, never repeat out of order, never teleport, and never stay pinned behind him.
This path crosses the axis of the row. The row's left-to-right order in frame reverses partway through, continuously and visibly, never as a cut. The physical positions of the three on the floor never change.
The walk ends with the operator settling behind <<<captain-agentv4>>>, his back and both shoulders filling the foreground, the three kneeling civilians visible beyond him.
No smooth constant-radius arc. No mechanical rotation, no turntable feel, no dolly or track feel, no gimbal glide, no drone motion. No perfectly level horizon, no perfectly centered subject, no constant subject size, no constant walking speed. No digital jitter and no random shake either: every movement comes from a body walking.

FORMAT MODE
SINGLE CONTINUOUS TAKE.

OPTICS
85mm-equivalent angle of view, approximately 29° diagonal field of view, short telephoto portrait lens character, matching the lens character already present in <<<image_1>>>. Background compresses close behind subjects and falls into soft bokeh. Subjects pop against a dissolved background.
Straight lines stay straight. Absolutely no barrel distortion, no fisheye curve, no wide-angle expansion, no stretched edges.
Anti-drift lock: no part of this shot becomes wide-angle or normal-lens coverage. The widening of the frame during the last quarter of the walk is achieved purely by the operator's increasing physical distance, never by the lens opening up. The background stays compressed and soft in every frame, including the final group framing.

CAMERA
Naturalistic documentary handheld, shoulder-mounted, operator standing and walking. Not a stabilised rig, not attached to any character. Objective third-person camera at all times, never a character's eyes.
Camera height starts at the height implied by <<<image_1>>>, rises to 1.5 meters during the move onto the officer, and stays around there, drifting a few centimeters with the operator's stride.
Movement path:
0:00 to 0:05 — held on <<<image_1>>>, no travel, breath and micro-correction only.
0:05 to 0:08 — the operator pans across the row and tilts up, passing <<<char_son>>> and <<<char_mum>>> in soft motion blur, arriving tight on <<<captain-agentv4>>> seen from behind, shoulders and helmet. The pan overshoots him slightly and pulls back.
0:08 to 0:22 — the operator walks the full circuit around him described in the orbit lock: uneven footsteps, breathing radius, loose off-center framing, visible parallax in the background, tight on armor for the first three quarters and opening out through the last quarter.
0:22 to 0:25 — the operator settles into the final position behind him and holds, with only breath and micro-correction. The frame is still not perfectly level.
Handheld quality is physical and unglamorous throughout: corrections arrive late, the horizon tilts and self-corrects, the operator's breath moves the frame in shallow cycles.
Focus behavior is documentary: focus sits on <<<char_dad>>>, hunts during the pan, resolves on the helmet at 0:08, then breathes continuously through the walk as the distance changes, missing slightly and recovering twice. At 0:22 it racks past his shoulder onto the kneeling row while his back stays soft in the foreground. The standing agent and the doorway behind him stay soft in every frame.
No digital jitter, no random shake, no gimbal smoothness, no drone feel, no mechanical dolly or turntable feel, no zoom, no slow motion, no point-of-view framing, no helmet-cam look, no character-locked tracking.

FACE AND SPEECH LOCK
<<<captain-agentv4>>>'s face is fully occluded. The four-lens optical cluster hangs over the upper and mid face. A thick padded neck gaiter covers the jaw, mouth and throat. There is no visible mouth at any point.
No lip movement is rendered. No lip shapes, no mouth opening, no teeth, no tongue, no visible articulation, no lipsync, no mouth animation of any kind.
The gaiter is thick structured fabric, not skin. It does not deform into lip shapes, does not stretch over a mouth, does not ripple in speech patterns, does not behave like a rubber membrane over a face.
The same applies to every <<<team2>>> agent: no visible faces, no mouths, no lip movement, and none of them speaks.

JAW SIGNAL
The only physical sign of speech is at the jaw hinge and the throat, and it is subtle.
On stressed syllables, the padded gaiter shifts by one or two millimeters where it crosses the jaw hinge below the ear, and the fabric fold at the front of the throat moves slightly with the larynx.
The helmet itself does not nod, bob, or rock with the words. The head stays level.
No exaggerated jaw drop, no chewing motion, no bobbing head, no fabric pulsing in time with syllables.

LIVING BODY LOCK
<<<char_dad>>>, <<<char_son>>> and <<<char_mum>>> are living people holding a forced position under threat. Holding still is active physical effort, never a frozen image.
Continuous for all three: shallow irregular breathing visible in chest and shoulders, ribcage moving under fabric, micro-tremor in the raised arms, elbows sagging a few millimeters and lifting back, shoulders creeping up and settling, small weight shifts on the knees, blinking at irregular intervals with eyes downcast and wet, swallowing, jaw tension, loose hair and loose fabric moving with breath. None of this displaces them from their spot on the floor.
Differentiated:
- <<<char_dad>>>: deepest and slowest breathing, jaw set, steadiest arms, one slow swallow.
- <<<char_son>>>: fastest and least stable, visible tremor in forearms and shoulders, chest heaving, one elbow dropping and pulled back up.
- <<<char_mum>>>: shallowest breathing held high in the chest, two visible catches, fingers tightening and loosening behind her head.
When the officer begins speaking, none of them looks up. Their breathing shortens. <<<char_son>>>'s tremor increases.
<<<captain-agentv4>>> is also alive under the armor: his chest plate rises and falls slightly with breathing, the hanging carbine sways minutely on its sling, the helmet cable and ID placard move with his body. His feet do not move.
The <<<team2>>> agents are alive too but held in disciplined stillness: minimal chest movement, gear settling slightly, no fidgeting, no weapon adjustment, no head turns, no steps.
No mannequin stillness, no frozen pose, no waxwork, no statue, no dead-eyed stare, no held breath across the whole shot.

ACTION TIMING
0:00 to 0:05 — Held on <<<image_1>>>. <<<char_dad>>> kneeling, head bowed, hands laced behind his head. Two full slow breath cycles visible in his shoulders and chest. He blinks once. His elbows sag and lift back. He does not look up. Silence except room tone and three sets of breathing. Nobody speaks in this stretch.
0:05 to 0:08 — The camera pans across the row and tilts up, crossing <<<char_son>>> and <<<char_mum>>> in motion blur, and arrives tight on <<<captain-agentv4>>> from behind, shoulders and helmet filling the frame. He stands planted, weight even, gloved hands loose at his sides, carbine hanging on its sling. Still silent.
0:08 to 0:09 — The operator starts walking. He does not stop again until 0:22. The background begins to slide behind the officer.
0:09 to 0:10.5 — Still walking. He speaks line 1: "Demographic control." His body does not move. Only the jaw signal at the gaiter.
0:10.5 to 0:12 — Silence. No words from anyone. The walk continues without pause. The table and chair wall passes behind him. The operator slows for a step as he clears the table corner.
0:12 to 0:17.5 — Still walking, now passing his front. Behind him the one open green door comes into the background: the torn jamb, the single <<<team2>>> agent holding position inside the room, and beyond them the corridor with two more <<<team2>>> agents framed in the opening, carbines raised, cold green fluorescent light behind them. All of it soft. He speaks line 2: "Present your birth code for verification under the current quota regulations." His helmet stays level. He does not turn to follow the camera. None of the agents reacts to the camera or to the voice, and none of them moves.
0:17.5 to 0:19.5 — Silence. No words from anyone. The walk continues and opens outward. The doorway leaves the background and the bed and window wall come round behind him. The operator's breathing gets slightly heavier in the frame.
0:19.5 to 0:25 — The walk completes and settles into the final framing behind him during the first seconds of the line. He speaks line 3: "Left wrist, palm up. The procedure is mandatory. Refusal, obstruction, or tampering with the code constitutes non-compliance."
Nobody obeys. Nobody lowers their hands. Nobody looks up. Nobody replies. Nobody has moved from their spot. The three keep breathing. The take ends on the held framing of his back and the row beyond, on the last word, without resolution.

DIALOGUE RULES
The three sentences in the SCRIPT LOCK are the complete spoken content of this shot. Nothing is added to them and nothing is taken away.
Only <<<captain-agentv4>>> speaks, and only in the voice of <<<audio_1>>>. The <<<team2>>> agents never speak. The three kneeling civilians never speak and their lips stay closed for the entire take.
No ad-libs, no improvisation, no invented dialogue, no repetition, no paraphrase, no additional commands, no radio chatter, no responses, no acknowledgements from anyone.
The voice is a pickup output, not visible speech. Nothing in frame is seen forming words.

PHYSICS
<<<captain-agentv4>>> carries real weight: armor plates settle against each other, the carbine hangs with visible mass on its sling and sways minutely, the helmet cable and clipped ID placard hang under gravity and move slightly with his breathing. His feet stay planted; he does not sway, drift, or rotate.
The <<<team2>>> agents carry the same weight in their gear: slung carbines hang and sway minutely, placards and cables hang under gravity.
The forced door hangs on its hinges under its own weight, motionless, splinters and the torn lock plate visible at the jamb.
The kneeling bodies carry real weight through knees and shins. Ankles and toes bear load. Breathing drives continuous small motion through torso, shoulders and clothing. Loose fabric on <<<char_son>>>'s oversized sweatshirt hangs and shifts with every breath. Loose strands of <<<char_mum>>>'s hair move on exhale.
Old floorboards creak and give under the operator's walking steps throughout the circuit.
No floating motion, no weightless weapons, no frictionless feet, no rubbery CG movement, no game-engine look, no frozen human bodies.

LIGHTING
Two sources only, both practical.
Room: thin grey overcast daylight through the curtained window, exactly as established by <<<image_1>>>. No sun, no warmth, no visible beam. The hanging bulb stays off. No lamp is switched on in the room.
Corridor: one cold fluorescent tube beyond the one open door, slightly green, out of frame. It only affects the doorway area and the corridor agents, who read as dark silhouettes against a pale green wash. It does not light the room and does not reach the kneeling civilians.
The window light stays fixed in the room while the camera moves around it. As the operator walks, the key wraps continuously across <<<captain-agentv4>>>: he passes from rim-lit at the back of the helmet, through a hard side key on one shoulder, to near-silhouette against the bright window, and back. This transition is smooth and physically consistent with a single fixed window, and it is further proof that the camera is moving through the room rather than travelling with him.
The kneeling civilians stay lit from the window side, faces angled down and held in soft shadow, with a faint wet catchlight in the downcast eyes. Rim light along their shoulders rises and falls visibly with their breathing.
Helmets stay dull matte grey-white, never bright, never glossy. Armor reads dark and desaturated.
Exposure and color grade match <<<image_1>>> throughout and do not shift during the walk.
No flat front light, no beauty fill, no studio key, no light from camera position, no colored light beyond the corridor fluorescent. No invented light source anywhere in the room.

AUDIO
Diegetic only. Exactly the three scripted sentences, spoken in the voice of <<<audio_1>>>. No other words from anyone, at any point.
Low building hum and the faint buzz of the corridor fluorescent through the open door. Three distinct sets of human breathing, close and audible from 0:00 to 0:25, never stopping: one deep and slow, one fast and unsteady, one shallow and high with catches. The breathing is the human floor of the entire soundtrack and remains faintly audible under the dialogue.
Uneven floorboard creaks and soft footfalls from the moving operator between 0:08 and 0:22, irregular in spacing, two of them heavier than the rest.
Faint armor and fabric noise from the standing armored figures.
0:09, 0:12 and 0:19.5: the three scripted lines, voice matched to <<<audio_1>>>, and nothing else.
Delivery: procedural, flat, unraised. Not a shout, not a threat. A phrase said a thousand times. No urgency, no emphasis, no rising inflection, flat terminal fall on every sentence. The pauses between lines are dead air, not dramatic holds, and they contain no speech.
Voice processing: heavily compressed and band-limited, as through a helmet pickup. Narrow midrange, rolled-off lows and highs, close and dry with no room reverb, slightly clipped consonants. The voice sits closer to the listener than the room does, and its level does not change as the camera moves.
Ambient sound ducks under each line and returns after it.
No music, no score, no subtitles, no radio chatter, no other offscreen voices, no muttering, no crying, no whimpering, no vocalisations, no invented lines.

POSITIVE CONSTRAINTS
The take begins on <<<image_1>>> exactly, with no alteration to that image.
Exactly three civilians in the room: <<<char_dad>>>, <<<char_son>>>, <<<char_mum>>>. All three kneel on the floorboards for the entire take, on their defined spots, present from frame one whether or not they are in frame, breathing whenever visible. No duplicates, no additional civilians, no children.
Exactly two armored figures inside the room: <<<captain-agentv4>>> and one single <<<team2>>> agent. Exactly two further <<<team2>>> agents in the corridor. Four armored figures total. No fifth agent appears from any angle of the walk. The count never changes.
Exactly one door in the shot, and it stays open and unmoving for the whole take. Nobody passes through it in either direction.
<<<audio_1>>> contributes voice only. No additional character, body, or figure is generated from it.
The three kneeling civilians stay in the same physical spots on the floor for the whole take. Their apparent left-to-right order in frame changes only because the camera moves around them.
The kneeling three never stand, never turn, never look up, never lower their hands, never speak, never change position.
<<<captain-agentv4>>> never kneels, never crouches, never raises his weapon, never touches anyone, never removes his helmet, never turns to face the camera, never tracks the camera with his head, never moves his feet. The <<<team2>>> agents do the same.
The camera stays inside the room for every frame, never crosses the threshold, never films from the corridor, and is never attached to any character's body.
The walk is continuous and completes a full circuit. The camera never stops between 0:08 and 0:22, and the background visibly moves behind the officer throughout.
Kodak Vision3 500T, naturalistic low-key cold daylight, real grain, grounded physical cinema texture, no blur, no ghosting, no flickering.

NEGATIVE CONSTRAINTS — LIGHT EMISSION
No glowing helmet lenses on any agent. The four optical cluster lenses stay dark, dead, unlit glass for the entire take, from every angle of the walk, including the agents in the corridor.
No blue glow, no cyan glow, no white glow, no glow of any color from any lens.
No internal illumination behind the lenses, no emissive rings, no lit apertures, no scanner beams, no projected light, no laser lines.
No LEDs anywhere: not on helmets, not on plate carriers, not on ID placards, not on weapons, not on optics or sights, not on gloves, not on any pouch or piece of gear.
No status lights, no indicator lights, no recorder light, no charging lights, no blinking dots, no small glowing points on any part of the equipment.
No glowing weapon optics. No illuminated reticles, no lit red dot sights, no lit rangefinders. No weapon-mounted lamps switched on.
No light spilling from any helmet onto a gaiter, shoulders, the door, the walls, or the floorboards. No colored bounce from equipment onto any surface.
No screens, panels, or displays are switched on anywhere in the room or the corridor.
The lenses may only carry faint passive reflections of existing room or corridor light. A reflection is never a source: it does not brighten surrounding surfaces and never appears when the surroundings are dark.
````

### Generated videos

- 2026-09-01 10:37:42 · [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260901_103742_620fd8fd-f601-4428-83c8-1d15fa1dd1d6.mp4)

## Earlier versions

Oldest first. Compare against the final to see what the author changed between attempts.

<details><summary>v1 · 2026-09-01 10:01:23 · 1 generation(s) · 011_20260901_100123_2aba1218.md</summary>

````text
SCENE CONTEXT
Continuation shot inside the same apartment. The camera holds on the kneeling father, finds the helmeted officer standing over the row, then walks all the way around him in one unbroken move while he delivers a procedural order, revealing the broken-open door and the agents holding behind him, and settles behind him with all three kneeling civilians visible beyond his shoulders.

OUTPUT SETTINGS
Single continuous handheld take, 25 seconds, real-time motion, no internal cuts. One continuous spoken passage, delivered through a helmet pickup. No subtitles, no captions, no music.

ACTIVE REFERENCES
<<<image_1>>>: the exact first frame of this shot. The take begins on this image and moves out of it. It controls opening framing, composition, subject position and scale, room layout, light direction, exposure, and color.
<<<loc_family_apt>>>: the apartment interior. Controls architecture, materials, and geography only.
<<<audio_1>>>: voice reference for the spoken passage. Controls timbre and identity of the speaking voice only. No character from this reference appears on screen at any point.
<<<captain-agentv4>>>: adult male officer, tall, fully armored, no visible face. Pale grey-white composite dome helmet with a four-lens optical cluster hanging down over the entire face, olive-green tactical fabric with a high padded neck gaiter covering the jaw, mouth and throat, olive plate carrier with magazine pouches, white ID placard clipped at chest, thin grey cable running from the side of the helmet down to the vest, olive gloves, suppressed black carbine hanging on its sling. 100% matches the reference.
<<<team2>>>: identical armored agents, same helmets, same four-lens optical cluster, same olive gear, same white ID placards, no visible faces, suppressed black carbines. No recorder unit on their chests. 100% matches the reference.
<<<char_dad>>>: 60yo East Asian man, thin build, grey-black hair swept back, grey stubble beard, worn olive-green open jacket over a brown waffle-knit shirt, dark brown trousers, barefoot. Kneeling, both hands laced behind his head. Alive and breathing. 100% matches the reference.
<<<char_son>>>: 20yo East Asian man, lean, black shoulder-length shaggy hair falling over his forehead, thin moustache and sparse chin stubble, oversized taupe-brown raw-seam sweatshirt, distressed wide brown trousers. Kneeling, both hands laced behind his head. Alive and breathing. 100% matches the reference.
<<<char_mum>>>: 50yo East Asian woman, slight build, grey hair pinned back in a low bun with loose strands, beige linen tunic under a dark charcoal vest, brown trousers, barefoot. Kneeling, both hands laced behind her head. Alive and breathing. 100% matches the reference.

CONTINUITY — STARTING STATE
The take starts on <<<image_1>>>, unchanged, and the first movement grows out of that image.
The subject in <<<image_1>>> is <<<char_dad>>>. His position, scale, posture, wardrobe and the room behind him are already correct and must not be re-staged, re-scaled, re-framed or re-lit at the start.
Nothing resets. No wardrobe change, no repositioning, no zoom-in or reframe onto him, no cut back to an earlier moment. The first thing that changes in the shot is his breathing, then the camera.
The light direction, exposure and color of <<<image_1>>> carry through the entire take. The window in <<<image_1>>> is the only light source in the room and stays fixed while the camera moves.
The apartment door was forced open before this shot and stays open for the whole take. Nobody closes it, nobody moves it, nobody enters or exits through it.

LOCATION MAP
<<<loc_family_apt>>> and <<<image_1>>> control architecture, materials, and geography.
One long room: white distempered walls, cracked ceiling, bare hanging bulb switched off, dark worn wooden floorboards.
Curtained window with grey overcast daylight: the wall at screen-left in <<<image_1>>>. Only light source in the room. A low wooden bed with a dark blanket sits below and right of it.
A metal-legged table with a wooden chair stands against the wall at screen-right in <<<image_1>>>.
The apartment door: pale green painted wood, forced open inward, hanging on its hinges with the lock plate torn out and splinters at the jamb. It stands open against the wall and does not move. Beyond it a bare corridor lit by one cold fluorescent tube, white wall above and green below.
The three civilians kneel in a row on the open floorboards, all three facing the door, bodies turned away from the window wall.
Row order on the floor, fixed and never changing for the whole take:
<<<char_dad>>> kneels at one end of the row, nearest the bed and the window.
<<<char_son>>> kneels in the middle.
<<<char_mum>>> kneels at the far end, nearest the table.
Roughly 80 centimeters between each of them.
<<<captain-agentv4>>> stands 2 meters in front of the row, facing the three of them, squarely centered on the middle of the row. His back is toward the open door. He is planted and does not move his feet at any point.
Standing order along the room's axis, fixed: the kneeling row, then <<<captain-agentv4>>>, then the open doorway, then the corridor.
One <<<team2>>> agent is inside the room. He entered first and holds a position 1.5 meters behind <<<captain-agentv4>>> and slightly to one side, between the officer and the open door, carbine lowered on its sling. He does not move his feet at any point.
Two further <<<team2>>> agents stand out in the corridor, beyond the open doorway, framed by the door opening, carbines raised. They hold the corridor and never cross the threshold.
The camera stays inside the room for the whole take. It never passes through the doorway, never films from the corridor.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame is <<<image_1>>> itself. No other opening framing, no establishing shot, no empty frame, no delayed reveal, no push-in before the action starts.
All three civilians are physically present and kneeling from frame one, whether or not they are inside the frame. None appears late, none is added mid-shot.
<<<captain-agentv4>>> and all three <<<team2>>> agents are already in their final positions from frame one, out of frame. Nobody walks, nobody enters, nobody arrives, nobody leaves during the take.
By the end of the take the frame holds <<<captain-agentv4>>> seen from behind, with all three kneeling civilians visible beyond him.

CAMERA ORBIT LOCK
Between 0:08 and 0:22 the operator walks all the way around <<<captain-agentv4>>> on foot and ends up where he started. He is a person carrying a camera on his shoulder while stepping around a standing man in a cramped room, not a rig on a track. The circle is the result of his path, never the instruction.
Continuity: he never stops, never pauses, never reverses direction, never holds a static frame during this stretch. Direction of travel is constant.
Gait: the path is walked in real footsteps on old floorboards. Each footfall drops the frame vertically by a small uneven amount. The steps are not evenly spaced and not evenly timed. Two of them land heavier than the others. Weight transfers heel to toe and the shoulder mass settles a beat after each step.
Path shape: the route is a rough polygon, not a smooth arc. He walks three or four short straight segments and corrects direction between them, so the framing drifts off the officer and is pulled back, repeatedly. Every correction arrives late and slightly overshoots before resolving.
Radius: the distance breathes between 1.0 and 1.6 meters through the first three quarters, never constant, then opens to 2.5 meters over the final quarter as he steps outward and back. The subject's size in frame therefore changes continuously and unevenly.
Speed: the walk is not uniform. He slows twice, once where the floor narrows near the kneeling row and once as he clears the corner of the table, then picks the pace back up. Both slowdowns are physical hesitations, not dramatic beats.
Framing: the officer is not centered and does not stay centered. He sits off-center and slides across the frame as the operator walks, held loosely rather than locked. The horizon tilts a degree or two and self-corrects. The camera height rises and falls a few centimeters with the operator's stride.
Breath: the operator's breathing moves the frame in slow shallow cycles underneath all of the above, and becomes slightly heavier in the last third of the walk.
Room containment: on the segment that passes between <<<captain-agentv4>>> and the open door, the operator tightens his path so he stays at least 1 meter inside the room and never reaches the threshold. He stays on the room floorboards for every frame.
On the segment that passes between <<<captain-agentv4>>> and the kneeling row, he comes within 0.8 meters of the row without touching it, turns his shoulders to clear the space, and the frame swings with that turn. He never walks into the row, never steps behind the row, never blocks a kneeling body with his own path.
As he travels, the background behind <<<captain-agentv4>>> rotates through the room in a physically consistent order and returns to where it began: the kneeling row and the far wall, then the table and chair wall, then the open doorway with the standing <<<team2>>> agent in front of it and the two corridor agents framed in the opening, then the bed and the window wall, then back to the kneeling row. Backgrounds never jump, never repeat out of order, never teleport.
This path crosses the axis of the row. The row's left-to-right order in frame reverses partway through, continuously and visibly, never as a cut. The physical positions of the three on the floor never change.
The walk ends with the operator settling behind <<<captain-agentv4>>>, his back and both shoulders filling the foreground, the three kneeling civilians visible beyond him.
No smooth constant-radius arc. No mechanical rotation, no turntable feel, no dolly or track feel, no gimbal glide, no drone motion. No perfectly level horizon, no perfectly centered subject, no constant subject size, no constant walking speed. No digital jitter and no random shake either: every movement comes from a body walking.

FORMAT MODE
SINGLE CONTINUOUS TAKE.

OPTICS
85mm-equivalent angle of view, approximately 29° diagonal field of view, short telephoto portrait lens character, matching the lens character already present in <<<image_1>>>. Background compresses close behind subjects and falls into soft bokeh. Subjects pop against a dissolved background.
Straight lines stay straight. Absolutely no barrel distortion, no fisheye curve, no wide-angle expansion, no stretched edges.
Anti-drift lock: no part of this shot becomes wide-angle or normal-lens coverage. The widening of the frame during the last quarter of the walk is achieved purely by the operator's increasing physical distance, never by the lens opening up. The background stays compressed and soft in every frame, including the final group framing.

CAMERA
Naturalistic documentary handheld, shoulder-mounted, operator standing and walking. Not a stabilised rig. Objective third-person camera at all times, never a character's eyes.
Camera height starts at the height implied by <<<image_1>>>, rises to 1.5 meters during the move onto the officer, and stays around there, drifting a few centimeters with the operator's stride.
Movement path:
0:00 to 0:05 — held on <<<image_1>>>, no travel, breath and micro-correction only.
0:05 to 0:08 — the operator pans across the row and tilts up, passing <<<char_son>>> and <<<char_mum>>> in soft motion blur, arriving tight on <<<captain-agentv4>>> seen from behind, shoulders and helmet. The pan overshoots him slightly and pulls back.
0:08 to 0:22 — the operator walks the full circuit around him described in the orbit lock: uneven footsteps, breathing radius, loose off-center framing, tight on armor for the first three quarters and opening out through the last quarter.
0:22 to 0:25 — the operator settles into the final position behind him and holds, with only breath and micro-correction. The frame is still not perfectly level.
Handheld quality is physical and unglamorous throughout: corrections arrive late, the horizon tilts and self-corrects, the operator's breath moves the frame in shallow cycles.
Focus behavior is documentary: focus sits on <<<char_dad>>>, hunts during the pan, resolves on the helmet at 0:08, then breathes continuously through the walk as the distance changes, missing slightly and recovering twice. At 0:22 it racks past his shoulder onto the kneeling row while his back stays soft in the foreground. The standing agent and the doorway behind him stay soft in every frame.
No digital jitter, no random shake, no gimbal smoothness, no drone feel, no mechanical dolly or turntable feel, no zoom, no slow motion, no point-of-view framing, no helmet-cam look.

FACE AND SPEECH LOCK
<<<captain-agentv4>>>'s face is fully occluded. The four-lens optical cluster hangs over the upper and mid face. A thick padded neck gaiter covers the jaw, mouth and throat. There is no visible mouth at any point.
No lip movement is rendered. No lip shapes, no mouth opening, no teeth, no tongue, no visible articulation, no lipsync, no mouth animation of any kind.
The gaiter is thick structured fabric, not skin. It does not deform into lip shapes, does not stretch over a mouth, does not ripple in speech patterns, does not behave like a rubber membrane over a face.
The same applies to every <<<team2>>> agent: no visible faces, no mouths, no lip movement, and none of them speaks.

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
The <<<team2>>> agents are alive too but held in disciplined stillness: minimal chest movement, gear settling slightly, no fidgeting, no weapon adjustment, no head turns.
No mannequin stillness, no frozen pose, no waxwork, no statue, no dead-eyed stare, no held breath across the whole shot.

ACTION TIMING
0:00 to 0:05 — Held on <<<image_1>>>. <<<char_dad>>> kneeling, head bowed, hands laced behind his head. Two full slow breath cycles visible in his shoulders and chest. He blinks once. His elbows sag and lift back. He does not look up. Silence except room tone and three sets of breathing.
0:05 to 0:08 — The camera pans across the row and tilts up, crossing <<<char_son>>> and <<<char_mum>>> in motion blur, and arrives tight on <<<captain-agentv4>>> from behind, shoulders and helmet filling the frame. He stands planted, weight even, gloved hands loose at his sides, carbine hanging on its sling.
0:08 to 0:09 — The operator starts walking. He does not stop again until 0:22.
0:09 to 0:10.5 — Still walking. He speaks: "Demographic control." His body does not move. Only the jaw signal at the gaiter.
0:10.5 to 0:12 — Silence. The walk continues without pause. The table and chair wall passes behind him. The operator slows for a step as he clears the table corner.
0:12 to 0:17.5 — Still walking, now passing his front. Behind him the open green door comes into the background: the torn jamb, the standing <<<team2>>> agent holding position inside the room, and beyond them the corridor with two more <<<team2>>> agents framed in the opening, carbines raised, cold green fluorescent light behind them. All of it soft. He speaks: "Present your birth code for verification under the current quota regulations." His helmet stays level. He does not turn to follow the camera. None of the agents reacts to the camera or to the voice.
0:17.5 to 0:19.5 — Silence. The walk continues and opens outward. The doorway leaves the background and the bed and window wall come round behind him. The operator's breathing gets slightly heavier in the frame.
0:19.5 to 0:25 — The walk completes and settles into the final framing behind him during the first seconds of the line. He speaks: "Left wrist, palm up. The procedure is mandatory. Refusal, obstruction, or tampering with the code constitutes non-compliance."
Nobody obeys. Nobody lowers their hands. Nobody looks up. The three keep breathing. The take ends on the held framing of his back and the row beyond, on the last word, without resolution.

DIALOGUE RULES
Only the scripted passage is spoken, exactly as written, in this order and no other words:
"Demographic control."
"Present your birth code for verification under the current quota regulations."
"Left wrist, palm up. The procedure is mandatory. Refusal, obstruction, or tampering with the code constitutes non-compliance."
No ad-libs, no repetition, no paraphrase, no additional commands, no radio chatter, no responses from anyone.
Only <<<captain-agentv4>>> speaks. The <<<team2>>> agents never speak. The three kneeling civilians never speak and their lips stay closed for the entire take.
The voice is a pickup output, not visible speech. Nothing in frame is seen forming words.

PHYSICS
<<<captain-agentv4>>> carries real weight: armor plates settle against each other, the carbine hangs with visible mass on its sling and sways minutely, the helmet cable and clipped ID placard hang under gravity and move slightly with his breathing. His feet stay planted; he does not sway, drift, or rotate.
The <<<team2>>> agents carry the same weight in their gear: slung carbines hang and sway minutely, placards and cables hang under gravity.
The forced door hangs on its hinges under its own weight, motionless, splinters and the torn lock plate visible at the jamb.
The kneeling bodies carry real weight through knees and shins. Ankles and toes bear load. Breathing drives continuous small motion through torso, shoulders and clothing. Loose fabric on <<<char_son>>>'s oversized sweatshirt hangs and shifts with every breath. Loose strands of <<<char_mum>>>'s hair move on exhale.
Old floorboards creak and give under the operator's walking steps throughout the circuit.
No floating motion, no weightless weapons, no frictionless feet, no rubbery CG movement, no game-engine look, no frozen human bodies.

LIGHTING
Two sources only, both practical.
Room: thin grey overcast daylight through the curtained window, exactly as established by <<<image_1>>>. No sun, no warmth, no visible beam. The hanging bulb stays off. No lamp is switched on in the room.
Corridor: one cold fluorescent tube beyond the open door, slightly green, out of frame. It only affects the doorway area and the corridor agents, who read as dark silhouettes against a pale green wash. It does not light the room and does not reach the kneeling civilians.
The window light stays fixed in the room while the camera moves around it. As the operator walks, the key wraps continuously across <<<captain-agentv4>>>: he passes from rim-lit at the back of the helmet, through a hard side key on one shoulder, to near-silhouette against the bright window, and back. This transition is smooth and physically consistent with a single fixed window.
The kneeling civilians stay lit from the window side, faces angled down and held in soft shadow, with a faint wet catchlight in the downcast eyes. Rim light along their shoulders rises and falls visibly with their breathing.
Helmets stay dull matte grey-white, never bright, never glossy. Armor reads dark and desaturated.
Exposure and color grade match <<<image_1>>> throughout and do not shift during the walk.
No flat front light, no beauty fill, no studio key, no light from camera position, no colored light beyond the corridor fluorescent.

AUDIO
Diegetic only. Exactly the scripted passage, spoken in the voice of <<<audio_1>>>. No other words from anyone.
Low building hum and the faint buzz of the corridor fluorescent through the open door. Three distinct sets of human breathing, close and audible from 0:00 to 0:25, never stopping: one deep and slow, one fast and unsteady, one shallow and high with catches. The breathing is the human floor of the entire soundtrack and remains faintly audible under the dialogue.
Uneven floorboard creaks and soft footfalls from the moving operator between 0:08 and 0:22, irregular in spacing, two of them heavier than the rest.
Faint armor and fabric noise from the standing armored figures.
0:09, 0:12 and 0:19.5: the three scripted lines, voice matched to <<<audio_1>>>.
Delivery: procedural, flat, unraised. Not a shout, not a threat. A phrase said a thousand times. No urgency, no emphasis, no rising inflection, flat terminal fall on every sentence. The pauses between lines are dead air, not dramatic holds.
Voice processing: heavily compressed and band-limited, as through a helmet pickup. Narrow midrange, rolled-off lows and highs, close and dry with no room reverb, slightly clipped consonants. The voice sits closer to the listener than the room does, and its level does not change as the camera moves.
Ambient sound ducks under each line and returns after it.
No music, no score, no subtitles, no radio chatter, no other offscreen voices, no crying, no whimpering, no vocalisations.

POSITIVE CONSTRAINTS
The take begins on <<<image_1>>> exactly, with no alteration to that image.
Exactly three civilians in the room: <<<char_dad>>>, <<<char_son>>>, <<<char_mum>>>. All three kneel on the floorboards for the entire take, present from frame one whether or not they are in frame, breathing whenever visible. No duplicates, no additional civilians, no children.
Exactly four armored figures total: <<<captain-agentv4>>>, one <<<team2>>> agent inside the room behind him, and two <<<team2>>> agents in the corridor. No fifth agent appears from any angle of the walk. The count never changes.
The door stays open and unmoving for the whole take. Nobody passes through it in either direction.
<<<audio_1>>> contributes voice only. No additional character, body, or figure is generated from it.
The three kneeling civilians stay in the same physical spots on the floor for the whole take. Their apparent left-to-right order in frame changes only because the camera moves around them.
The kneeling three never stand, never turn, never look up, never lower their hands, never speak.
<<<captain-agentv4>>> never kneels, never crouches, never raises his weapon, never touches anyone, never removes his helmet, never turns to face the camera, never tracks the camera with his head. The <<<team2>>> agents do the same and never move their feet.
The camera stays inside the room for every frame, never crosses the threshold, never films from the corridor.
The walk is continuous and completes a full circuit. The camera never stops between 0:08 and 0:22.
Kodak Vision3 500T, naturalistic low-key cold daylight, real grain, grounded physical cinema texture, no blur, no ghosting, no flickering.

NEGATIVE CONSTRAINTS — LIGHT EMISSION
No glowing helmet lenses on any agent. The four optical cluster lenses stay dark, dead, unlit glass for the entire take, from every angle of the walk, including the agents in the corridor.
No blue glow, no cyan glow, no white glow, no glow of any color from any lens.
No internal illumination behind the lenses, no emissive rings, no lit apertures, no scanner beams, no projected light, no laser lines.
No LEDs anywhere: not on helmets, not on plate carriers, not on ID placards, not on weapons, not on optics or sights, not on gloves, not on any pouch or piece of gear.
No status lights, no indicator lights, no recorder light, no charging lights, no blinking dots, no small glowing points on any part of the equipment.
No glowing weapon optics. No illuminated reticles, no lit red dot sights, no lit rangefinders. No weapon-mounted lamps switched on.
No light spilling from any helmet onto a gaiter, shoulders, the door, the walls, or the floorboards. No colored bounce from equipment onto any surface.
No screens, panels, or displays are switched on anywhere in the room or the corridor.
The lenses may only carry faint passive reflections of existing room or corridor light. A reflection is never a source: it does not brighten surrounding surfaces and never appears when the surroundings are dark.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260901_100123_2aba1218-e9e5-4219-8ba4-f2750518132b.mp4)

</details>

<details><summary>v2 · 2026-09-01 10:17:18 · 1 generation(s) · 014_20260901_101718_d32471d6.md</summary>

````text
SCENE CONTEXT
Continuation shot inside the same apartment. The camera holds on the kneeling father, finds the helmeted officer standing over the row, then walks all the way around him in one unbroken move while he delivers a procedural order, revealing the broken-open door and the agents holding behind him, and settles behind him with all three kneeling civilians visible beyond his shoulders.

OUTPUT SETTINGS
Single continuous handheld take, 25 seconds, real-time motion, no internal cuts. One continuous spoken passage, delivered through a helmet pickup. No subtitles, no captions, no music.

SCRIPT LOCK — DIALOGUE IS FIXED
The spoken content of this shot is closed. Exactly three sentences are spoken in the entire take, in this order, word for word:
1. "Demographic control."
2. "Present your birth code for verification under the current quota regulations."
3. "Left wrist, palm up. The procedure is mandatory. Refusal, obstruction, or tampering with the code constitutes non-compliance."
Do not invent, add, extend, shorten, reorder, paraphrase or improvise any line. Do not generate a fourth sentence. Do not add greetings, warnings, callouts, confirmations, numbers, codes, names, acknowledgements or reactions. Do not have any character answer, repeat, echo or respond.
Every one of these lines is spoken by <<<captain-agentv4>>> alone, using the voice of <<<audio_1>>> and no other voice. No other character in the room or the corridor speaks a single word.
If the shot has silence to fill, it stays silent. Silence is correct. Invented speech is not.

ACTIVE REFERENCES
<<<image_1>>>: the exact first frame of this shot. The take begins on this image and moves out of it. It controls opening framing, composition, subject position and scale, room layout, light direction, exposure, and color.
<<<loc_family_apt>>>: the apartment interior. Controls architecture, materials, and geography only.
<<<audio_1>>>: the voice used for every spoken line in this shot. Controls timbre and identity of the speaking voice only. No character from this reference appears on screen at any point.
<<<captain-agentv4>>>: adult male officer, tall, fully armored, no visible face. Pale grey-white composite dome helmet with a four-lens optical cluster hanging down over the entire face, olive-green tactical fabric with a high padded neck gaiter covering the jaw, mouth and throat, olive plate carrier with magazine pouches, white ID placard clipped at chest, thin grey cable running from the side of the helmet down to the vest, olive gloves, suppressed black carbine hanging on its sling. 100% matches the reference.
<<<team2>>>: identical armored agents, same helmets, same four-lens optical cluster, same olive gear, same white ID placards, no visible faces, suppressed black carbines. No recorder unit on their chests. 100% matches the reference.
<<<char_dad>>>: 60yo East Asian man, thin build, grey-black hair swept back, grey stubble beard, worn olive-green open jacket over a brown waffle-knit shirt, dark brown trousers, barefoot. Kneeling, both hands laced behind his head. Alive and breathing. 100% matches the reference.
<<<char_son>>>: 20yo East Asian man, lean, black shoulder-length shaggy hair falling over his forehead, thin moustache and sparse chin stubble, oversized taupe-brown raw-seam sweatshirt, distressed wide brown trousers. Kneeling, both hands laced behind his head. Alive and breathing. 100% matches the reference.
<<<char_mum>>>: 50yo East Asian woman, slight build, grey hair pinned back in a low bun with loose strands, beige linen tunic under a dark charcoal vest, brown trousers, barefoot. Kneeling, both hands laced behind her head. Alive and breathing. 100% matches the reference.

CONTINUITY — STARTING STATE
The take starts on <<<image_1>>>, unchanged, and the first movement grows out of that image.
The subject in <<<image_1>>> is <<<char_dad>>>. His position, scale, posture, wardrobe and the room behind him are already correct and must not be re-staged, re-scaled, re-framed or re-lit at the start.
Nothing resets. No wardrobe change, no repositioning, no zoom-in or reframe onto him, no cut back to an earlier moment. The first thing that changes in the shot is his breathing, then the camera.
The light direction, exposure and color of <<<image_1>>> carry through the entire take. The window in <<<image_1>>> is the only light source in the room and stays fixed while the camera moves.
The apartment door was forced open before this shot and stays open for the whole take. Nobody closes it, nobody moves it, nobody enters or exits through it.

OCCUPANCY LOCK
Exactly five figures are inside the room for the whole take, and no more:
<<<char_dad>>>, <<<char_son>>> and <<<char_mum>>>, kneeling in a row.
<<<captain-agentv4>>>, standing in front of them.
One single <<<team2>>> agent, standing behind the officer.
Every other agent is out in the corridor, beyond the open doorway, and stays there. Two <<<team2>>> agents hold the corridor.
This count never changes. Nobody enters the room, nobody leaves it, no additional agent walks in from the corridor, no extra figure appears from any angle of the camera's walk. The room contains five people from the first frame to the last.

LOCATION MAP
<<<loc_family_apt>>> and <<<image_1>>> control architecture, materials, and geography.
One long room: white distempered walls, cracked ceiling, bare hanging bulb switched off, dark worn wooden floorboards.
Curtained window with grey overcast daylight: the wall at screen-left in <<<image_1>>>. Only light source in the room. A low wooden bed with a dark blanket sits below and right of it.
A metal-legged table with a wooden chair stands against the wall at screen-right in <<<image_1>>>.
The apartment door: pale green painted wood, forced open inward, hanging on its hinges with the lock plate torn out and splinters at the jamb. It stands open against the wall and does not move. Beyond it a bare corridor lit by one cold fluorescent tube, white wall above and green below.
The three civilians kneel in a row on the open floorboards, all three facing the door, bodies turned away from the window wall.
Row order on the floor, fixed and never changing for the whole take:
<<<char_dad>>> kneels at one end of the row, nearest the bed and the window.
<<<char_son>>> kneels in the middle.
<<<char_mum>>> kneels at the far end, nearest the table.
Roughly 80 centimeters between each of them.
<<<captain-agentv4>>> stands 2 meters in front of the row, facing the three of them, squarely centered on the middle of the row. His back is toward the open door. He is planted and does not move his feet at any point.
Standing order along the room's axis, fixed: the kneeling row, then <<<captain-agentv4>>>, then the single <<<team2>>> agent, then the open doorway, then the corridor.
The single <<<team2>>> agent inside the room entered first and holds a position 1.5 meters behind <<<captain-agentv4>>> and slightly to one side, between the officer and the open door, carbine lowered on its sling. He does not move his feet at any point.
The two corridor <<<team2>>> agents stand beyond the open doorway, framed by the door opening, carbines raised. They hold the corridor and never cross the threshold.
The camera stays inside the room for the whole take. It never passes through the doorway, never films from the corridor.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame is <<<image_1>>> itself. No other opening framing, no establishing shot, no empty frame, no delayed reveal, no push-in before the action starts.
All three civilians are physically present and kneeling from frame one, whether or not they are inside the frame. None appears late, none is added mid-shot.
<<<captain-agentv4>>> and all three <<<team2>>> agents are already in their final positions from frame one, out of frame. Nobody walks, nobody enters, nobody arrives, nobody leaves during the take.
By the end of the take the frame holds <<<captain-agentv4>>> seen from behind, with all three kneeling civilians visible beyond him.

CAMERA ORBIT LOCK
Between 0:08 and 0:22 the operator walks all the way around <<<captain-agentv4>>> on foot and ends up where he started. He is a person carrying a camera on his shoulder while stepping around a standing man in a cramped room, not a rig on a track. The circle is the result of his path, never the instruction.
Continuity: he never stops, never pauses, never reverses direction, never holds a static frame during this stretch. Direction of travel is constant.
Gait: the path is walked in real footsteps on old floorboards. Each footfall drops the frame vertically by a small uneven amount. The steps are not evenly spaced and not evenly timed. Two of them land heavier than the others. Weight transfers heel to toe and the shoulder mass settles a beat after each step.
Path shape: the route is a rough polygon, not a smooth arc. He walks three or four short straight segments and corrects direction between them, so the framing drifts off the officer and is pulled back, repeatedly. Every correction arrives late and slightly overshoots before resolving.
Radius: the distance breathes between 1.0 and 1.6 meters through the first three quarters, never constant, then opens to 2.5 meters over the final quarter as he steps outward and back. The subject's size in frame therefore changes continuously and unevenly.
Speed: the walk is not uniform. He slows twice, once where the floor narrows near the kneeling row and once as he clears the corner of the table, then picks the pace back up. Both slowdowns are physical hesitations, not dramatic beats.
Framing: the officer is not centered and does not stay centered. He sits off-center and slides across the frame as the operator walks, held loosely rather than locked. The horizon tilts a degree or two and self-corrects. The camera height rises and falls a few centimeters with the operator's stride.
Breath: the operator's breathing moves the frame in slow shallow cycles underneath all of the above, and becomes slightly heavier in the last third of the walk.
Room containment: on the segment that passes between <<<captain-agentv4>>> and the open door, the operator tightens his path so he stays at least 1 meter inside the room and never reaches the threshold. He stays on the room floorboards for every frame.
On the segment that passes between <<<captain-agentv4>>> and the kneeling row, he comes within 0.8 meters of the row without touching it, turns his shoulders to clear the space, and the frame swings with that turn. He never walks into the row, never steps behind the row, never blocks a kneeling body with his own path.
As he travels, the background behind <<<captain-agentv4>>> rotates through the room in a physically consistent order and returns to where it began: the kneeling row and the far wall, then the table and chair wall, then the open doorway with the single <<<team2>>> agent in front of it and the two corridor agents framed in the opening, then the bed and the window wall, then back to the kneeling row. Backgrounds never jump, never repeat out of order, never teleport.
This path crosses the axis of the row. The row's left-to-right order in frame reverses partway through, continuously and visibly, never as a cut. The physical positions of the three on the floor never change.
The walk ends with the operator settling behind <<<captain-agentv4>>>, his back and both shoulders filling the foreground, the three kneeling civilians visible beyond him.
No smooth constant-radius arc. No mechanical rotation, no turntable feel, no dolly or track feel, no gimbal glide, no drone motion. No perfectly level horizon, no perfectly centered subject, no constant subject size, no constant walking speed. No digital jitter and no random shake either: every movement comes from a body walking.

FORMAT MODE
SINGLE CONTINUOUS TAKE.

OPTICS
85mm-equivalent angle of view, approximately 29° diagonal field of view, short telephoto portrait lens character, matching the lens character already present in <<<image_1>>>. Background compresses close behind subjects and falls into soft bokeh. Subjects pop against a dissolved background.
Straight lines stay straight. Absolutely no barrel distortion, no fisheye curve, no wide-angle expansion, no stretched edges.
Anti-drift lock: no part of this shot becomes wide-angle or normal-lens coverage. The widening of the frame during the last quarter of the walk is achieved purely by the operator's increasing physical distance, never by the lens opening up. The background stays compressed and soft in every frame, including the final group framing.

CAMERA
Naturalistic documentary handheld, shoulder-mounted, operator standing and walking. Not a stabilised rig. Objective third-person camera at all times, never a character's eyes.
Camera height starts at the height implied by <<<image_1>>>, rises to 1.5 meters during the move onto the officer, and stays around there, drifting a few centimeters with the operator's stride.
Movement path:
0:00 to 0:05 — held on <<<image_1>>>, no travel, breath and micro-correction only.
0:05 to 0:08 — the operator pans across the row and tilts up, passing <<<char_son>>> and <<<char_mum>>> in soft motion blur, arriving tight on <<<captain-agentv4>>> seen from behind, shoulders and helmet. The pan overshoots him slightly and pulls back.
0:08 to 0:22 — the operator walks the full circuit around him described in the orbit lock: uneven footsteps, breathing radius, loose off-center framing, tight on armor for the first three quarters and opening out through the last quarter.
0:22 to 0:25 — the operator settles into the final position behind him and holds, with only breath and micro-correction. The frame is still not perfectly level.
Handheld quality is physical and unglamorous throughout: corrections arrive late, the horizon tilts and self-corrects, the operator's breath moves the frame in shallow cycles.
Focus behavior is documentary: focus sits on <<<char_dad>>>, hunts during the pan, resolves on the helmet at 0:08, then breathes continuously through the walk as the distance changes, missing slightly and recovering twice. At 0:22 it racks past his shoulder onto the kneeling row while his back stays soft in the foreground. The standing agent and the doorway behind him stay soft in every frame.
No digital jitter, no random shake, no gimbal smoothness, no drone feel, no mechanical dolly or turntable feel, no zoom, no slow motion, no point-of-view framing, no helmet-cam look.

FACE AND SPEECH LOCK
<<<captain-agentv4>>>'s face is fully occluded. The four-lens optical cluster hangs over the upper and mid face. A thick padded neck gaiter covers the jaw, mouth and throat. There is no visible mouth at any point.
No lip movement is rendered. No lip shapes, no mouth opening, no teeth, no tongue, no visible articulation, no lipsync, no mouth animation of any kind.
The gaiter is thick structured fabric, not skin. It does not deform into lip shapes, does not stretch over a mouth, does not ripple in speech patterns, does not behave like a rubber membrane over a face.
The same applies to every <<<team2>>> agent: no visible faces, no mouths, no lip movement, and none of them speaks.

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
The <<<team2>>> agents are alive too but held in disciplined stillness: minimal chest movement, gear settling slightly, no fidgeting, no weapon adjustment, no head turns.
No mannequin stillness, no frozen pose, no waxwork, no statue, no dead-eyed stare, no held breath across the whole shot.

ACTION TIMING
0:00 to 0:05 — Held on <<<image_1>>>. <<<char_dad>>> kneeling, head bowed, hands laced behind his head. Two full slow breath cycles visible in his shoulders and chest. He blinks once. His elbows sag and lift back. He does not look up. Silence except room tone and three sets of breathing. Nobody speaks in this stretch.
0:05 to 0:08 — The camera pans across the row and tilts up, crossing <<<char_son>>> and <<<char_mum>>> in motion blur, and arrives tight on <<<captain-agentv4>>> from behind, shoulders and helmet filling the frame. He stands planted, weight even, gloved hands loose at his sides, carbine hanging on its sling. Still silent.
0:08 to 0:09 — The operator starts walking. He does not stop again until 0:22.
0:09 to 0:10.5 — Still walking. He speaks line 1: "Demographic control." His body does not move. Only the jaw signal at the gaiter.
0:10.5 to 0:12 — Silence. No words from anyone. The walk continues without pause. The table and chair wall passes behind him. The operator slows for a step as he clears the table corner.
0:12 to 0:17.5 — Still walking, now passing his front. Behind him the open green door comes into the background: the torn jamb, the single <<<team2>>> agent holding position inside the room, and beyond them the corridor with two more <<<team2>>> agents framed in the opening, carbines raised, cold green fluorescent light behind them. All of it soft. He speaks line 2: "Present your birth code for verification under the current quota regulations." His helmet stays level. He does not turn to follow the camera. None of the agents reacts to the camera or to the voice.
0:17.5 to 0:19.5 — Silence. No words from anyone. The walk continues and opens outward. The doorway leaves the background and the bed and window wall come round behind him. The operator's breathing gets slightly heavier in the frame.
0:19.5 to 0:25 — The walk completes and settles into the final framing behind him during the first seconds of the line. He speaks line 3: "Left wrist, palm up. The procedure is mandatory. Refusal, obstruction, or tampering with the code constitutes non-compliance."
Nobody obeys. Nobody lowers their hands. Nobody looks up. Nobody replies. The three keep breathing. The take ends on the held framing of his back and the row beyond, on the last word, without resolution.

DIALOGUE RULES
The three sentences in the SCRIPT LOCK are the complete spoken content of this shot. Nothing is added to them and nothing is taken away.
Only <<<captain-agentv4>>> speaks, and only in the voice of <<<audio_1>>>. The <<<team2>>> agents never speak. The three kneeling civilians never speak and their lips stay closed for the entire take.
No ad-libs, no improvisation, no invented dialogue, no repetition, no paraphrase, no additional commands, no radio chatter, no responses, no acknowledgements from anyone.
The voice is a pickup output, not visible speech. Nothing in frame is seen forming words.

PHYSICS
<<<captain-agentv4>>> carries real weight: armor plates settle against each other, the carbine hangs with visible mass on its sling and sways minutely, the helmet cable and clipped ID placard hang under gravity and move slightly with his breathing. His feet stay planted; he does not sway, drift, or rotate.
The <<<team2>>> agents carry the same weight in their gear: slung carbines hang and sway minutely, placards and cables hang under gravity.
The forced door hangs on its hinges under its own weight, motionless, splinters and the torn lock plate visible at the jamb.
The kneeling bodies carry real weight through knees and shins. Ankles and toes bear load. Breathing drives continuous small motion through torso, shoulders and clothing. Loose fabric on <<<char_son>>>'s oversized sweatshirt hangs and shifts with every breath. Loose strands of <<<char_mum>>>'s hair move on exhale.
Old floorboards creak and give under the operator's walking steps throughout the circuit.
No floating motion, no weightless weapons, no frictionless feet, no rubbery CG movement, no game-engine look, no frozen human bodies.

LIGHTING
Two sources only, both practical.
Room: thin grey overcast daylight through the curtained window, exactly as established by <<<image_1>>>. No sun, no warmth, no visible beam. The hanging bulb stays off. No lamp is switched on in the room.
Corridor: one cold fluorescent tube beyond the open door, slightly green, out of frame. It only affects the doorway area and the corridor agents, who read as dark silhouettes against a pale green wash. It does not light the room and does not reach the kneeling civilians.
The window light stays fixed in the room while the camera moves around it. As the operator walks, the key wraps continuously across <<<captain-agentv4>>>: he passes from rim-lit at the back of the helmet, through a hard side key on one shoulder, to near-silhouette against the bright window, and back. This transition is smooth and physically consistent with a single fixed window.
The kneeling civilians stay lit from the window side, faces angled down and held in soft shadow, with a faint wet catchlight in the downcast eyes. Rim light along their shoulders rises and falls visibly with their breathing.
Helmets stay dull matte grey-white, never bright, never glossy. Armor reads dark and desaturated.
Exposure and color grade match <<<image_1>>> throughout and do not shift during the walk.
No flat front light, no beauty fill, no studio key, no light from camera position, no colored light beyond the corridor fluorescent.

AUDIO
Diegetic only. Exactly the three scripted sentences, spoken in the voice of <<<audio_1>>>. No other words from anyone, at any point.
Low building hum and the faint buzz of the corridor fluorescent through the open door. Three distinct sets of human breathing, close and audible from 0:00 to 0:25, never stopping: one deep and slow, one fast and unsteady, one shallow and high with catches. The breathing is the human floor of the entire soundtrack and remains faintly audible under the dialogue.
Uneven floorboard creaks and soft footfalls from the moving operator between 0:08 and 0:22, irregular in spacing, two of them heavier than the rest.
Faint armor and fabric noise from the standing armored figures.
0:09, 0:12 and 0:19.5: the three scripted lines, voice matched to <<<audio_1>>>, and nothing else.
Delivery: procedural, flat, unraised. Not a shout, not a threat. A phrase said a thousand times. No urgency, no emphasis, no rising inflection, flat terminal fall on every sentence. The pauses between lines are dead air, not dramatic holds, and they contain no speech.
Voice processing: heavily compressed and band-limited, as through a helmet pickup. Narrow midrange, rolled-off lows and highs, close and dry with no room reverb, slightly clipped consonants. The voice sits closer to the listener than the room does, and its level does not change as the camera moves.
Ambient sound ducks under each line and returns after it.
No music, no score, no subtitles, no radio chatter, no other offscreen voices, no muttering, no crying, no whimpering, no vocalisations, no invented lines.

POSITIVE CONSTRAINTS
The take begins on <<<image_1>>> exactly, with no alteration to that image.
Exactly three civilians in the room: <<<char_dad>>>, <<<char_son>>>, <<<char_mum>>>. All three kneel on the floorboards for the entire take, present from frame one whether or not they are in frame, breathing whenever visible. No duplicates, no additional civilians, no children.
Exactly two armored figures inside the room: <<<captain-agentv4>>> and one single <<<team2>>> agent. Exactly two further <<<team2>>> agents in the corridor. Four armored figures total. No fifth agent appears from any angle of the walk. The count never changes.
The door stays open and unmoving for the whole take. Nobody passes through it in either direction.
<<<audio_1>>> contributes voice only. No additional character, body, or figure is generated from it.
The three kneeling civilians stay in the same physical spots on the floor for the whole take. Their apparent left-to-right order in frame changes only because the camera moves around them.
The kneeling three never stand, never turn, never look up, never lower their hands, never speak.
<<<captain-agentv4>>> never kneels, never crouches, never raises his weapon, never touches anyone, never removes his helmet, never turns to face the camera, never tracks the camera with his head. The <<<team2>>> agents do the same and never move their feet.
The camera stays inside the room for every frame, never crosses the threshold, never films from the corridor.
The walk is continuous and completes a full circuit. The camera never stops between 0:08 and 0:22.
Kodak Vision3 500T, naturalistic low-key cold daylight, real grain, grounded physical cinema texture, no blur, no ghosting, no flickering.

NEGATIVE CONSTRAINTS — LIGHT EMISSION
No glowing helmet lenses on any agent. The four optical cluster lenses stay dark, dead, unlit glass for the entire take, from every angle of the walk, including the agents in the corridor.
No blue glow, no cyan glow, no white glow, no glow of any color from any lens.
No internal illumination behind the lenses, no emissive rings, no lit apertures, no scanner beams, no projected light, no laser lines.
No LEDs anywhere: not on helmets, not on plate carriers, not on ID placards, not on weapons, not on optics or sights, not on gloves, not on any pouch or piece of gear.
No status lights, no indicator lights, no recorder light, no charging lights, no blinking dots, no small glowing points on any part of the equipment.
No glowing weapon optics. No illuminated reticles, no lit red dot sights, no lit rangefinders. No weapon-mounted lamps switched on.
No light spilling from any helmet onto a gaiter, shoulders, the door, the walls, or the floorboards. No colored bounce from equipment onto any surface.
No screens, panels, or displays are switched on anywhere in the room or the corridor.
The lenses may only carry faint passive reflections of existing room or corridor light. A reflection is never a source: it does not brighten surrounding surfaces and never appears when the surroundings are dark.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260901_101718_d32471d6-9175-4727-9e0e-97ba5b8e65dc.mp4)

</details>
