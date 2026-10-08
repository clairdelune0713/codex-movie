# scene-01-16 · A man stands at the window of a small apartment with his back to the room, smoking.

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
| Iterations | 2 prompt version(s), 6 generation(s) total |

**Sections:** SCENE CONTEXT → ACTIVE REFERENCES → CAMERA AND FRAMING → OPTICS → FIRST FRAME AND SPATIAL BLOCKING → FORMAT MODE → ACTION TIMING — 10 SECONDS → DIALOGUE → AUDIO — FOLEY ONLY, ZERO AMBIENCE → PHYSICS → LIGHTING → POSITIVE CONSTRAINTS → NEGATIVE — LOCAL LOCKS

## Final prompt (latest version)

_Element IDs replaced with names. Original with IDs: [033_20260828_212125_575db72b.md](../../../prompts/04_FOOTAGE/SCENE%2001/033_20260828_212125_575db72b.md)_

````text
SCENE CONTEXT
A man stands at the window of a small apartment with his back to the room, smoking. He turns, crosses to the table, sits down opposite the woman and looks her straight in the eyes. Tight single on him, frontal, framed past her out-of-focus shoulder. The table is never seen. One continuous 10-second take.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. A lit cigarette in his right hand, held low at his side and OUT OF FRAME below the bottom edge for the whole shot. 100% matches the reference. He is the sharp subject of this shot.
<<<char_wife>>>: 38yo woman, blonde hair pulled back into a low loose knot with fine strands escaping at the temple and the nape. White wrap vest with a wide shawl collar over a black t-shirt. In this shot she is a FOREGROUND element only: the back and side of her shoulder and the low knot of her hair, heavily out of focus, occupying the right edge of frame. Her face is never seen, she never turns, she never comes into focus. 100% matches the reference for hair, costume and build.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, a large three-pane window with a dark metal frame and a deep pale sill, a cold grey residential tower block filling the glass, heavy dark red curtains hanging as vertical bands at both edges of the window, tall dark leafy plants against the walls, stacks of old books and newspapers piled along the floor beneath the window, a sagging sofa and low coffee table at one end, a conical pendant lamp hanging over the table, a round pale table with metal-framed chairs. Geography, materials, colour and light only. Nothing in the room beyond what is listed here.
<<<image_1>>> — BLOCKING REFERENCE ONLY. A photograph of the room with the two seated positions marked on it. The RED marker is <<<char_captain>>>: the LEFT chair at the round table, his back toward the window, facing across the table to screen-right. The YELLOW marker is <<<char_wife>>>: the RIGHT chair, opposite him, facing across the table to screen-left. The window is directly behind the red position, a few paces back, with the book stacks and the sill beneath it.
Use this image ONLY for where the two of them are in the room, which way each faces, what lies behind each of them, and the short path he walks from the window to the left chair. Do NOT reproduce its wide framing — this shot is far tighter and holds only him. The coloured markers are annotations, not objects and not costume: no red or yellow shape, outline, dot, line, overlay or drawn figure appears anywhere in the render, and neither character wears red or yellow.

CAMERA AND FRAMING
Tight over-the-shoulder single on <<<char_captain>>>.
The camera sits just past <<<char_wife>>> on the right side of the room, close behind her shoulder, on the axis that runs across the table between them. Because the camera is almost on that axis, <<<char_captain>>> reads close to FRONTAL once he is seated — facing very nearly into the lens, with only a few degrees of offset. His eyeline goes just past the camera to her eyes.
FOREGROUND, right edge of frame, running from the bottom edge upward: the out-of-focus mass of her shoulder, the side of her neck and the low knot of her hair. Dark, soft, no readable detail, no face, no eye. She occupies roughly the right quarter to right third of the frame and nothing more.
MIDGROUND, the left two thirds of frame: <<<char_captain>>>. THE FRAME IS SIZED FOR HIM SEATED — once he is in the chair it holds him from the CHEST UP, shoulders close to full width. Because the camera never moves, while he is still standing at the start his head is ABOVE the top edge and we see only his torso from roughly the waist to the shoulders. He descends into the frame as he sits. This is the point of the shot: the framing waits and he arrives in it.
THE TABLE IS NEVER IN FRAME. The bottom edge sits above the tabletop line, so no table surface, no table edge, no chair seat, no hands and no objects on the table are ever visible. His hands and the cigarette stay below the bottom edge throughout.
BACKGROUND, behind him and soft: the pale luminous window glass with the tower block dissolved into a wash beyond it, the deep pale sill running horizontally, the vertical band of the dark red curtain at the left edge, the dark shape of a plant, and the low dark mass of the book stacks. The pendant lamp hangs above and outside the top of frame and is not visible.
Camera height: SEATED eye height, level. Not looking up at him, not down at him. While he is standing this means the camera is well below his eyeline and his head is out of frame — do not correct for this.
TRIPOD, HEAD FULLY CLAMPED, ZERO MOVEMENT for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no boom, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not follow him across the room, does not tilt up to keep his head, and does not tilt down as he sits.
Framing is pixel-identical from the first frame to the last. The window sill line, the curtain edge and her foreground shoulder hold the exact same screen positions at 0:10 as at 0:00 — that is the test of whether the lock held.

OPTICS
Roughly 30° diagonal field of view, short-telephoto character, camera positioned back from him rather than pushed into his face.
Shallow-to-moderate depth of field. THE FOCAL PLANE IS SET ON THE SEATED POSITION and does not move. Her foreground shoulder and hair fall well in front of the plane and are strongly defocused into a soft dark mass. The window, the sill, the book stacks and the plant behind him fall behind the plane and are soft, the tower block dissolving into a pale luminous wash with its window grid barely legible.
Because the focus is locked to the chair, he is SOFT while standing at the window at the start, sharpens as he walks in, and is fully sharp only once he has sat down. He walks into focus; the focus never travels to meet him. No focus pull, no rack focus onto her, no focus hunting, no lens breathing, no zoom.
The background sits flat and close behind him rather than receding. Once seated, skin texture, the grey in his beard, the wet catchlight-free surface of his eyes, the weave of the linen shirt and the smoke are all readable at this scale. The eyes must resolve clearly — they carry the last third of the shot.

FIRST FRAME AND SPATIAL BLOCKING
First frame: <<<char_captain>>> is STANDING at the window, a few paces back from the chair, his BACK to the room and to camera, looking out at the tower block. He occupies the left two thirds of frame from roughly the waist to the shoulders — his head is cropped off by the TOP edge of frame and is not visible. He is slightly soft, sitting behind the focal plane.
His shoulders are low, his weight settled on one leg. The cigarette is in his right hand at his side, below the bottom edge, and a thin ribbon of smoke rises past his hip and shoulder and up out of the top of frame through the window light.
Her defocused shoulder and hair occupy the right edge of frame as a dark soft mass. Behind him the pale window field, the sill, the red curtain band at the left edge, the dark plant, the book stacks, all soft.
No empty first frame. No establishing wide at any point. He is large and immediate in frame one, even without his head.

FORMAT MODE
Single continuous take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. One figure moving through a locked frame and one defocused foreground shape, for the whole shot.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window, back to camera, head above the top edge of frame. One slow shallow breath — the shoulder line barely moves. Smoke rises past him in an unbroken ribbon. She does not move.
0:02–0:03.6 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward the table and toward camera. Roughly 160 to 180 degrees, unhurried, no snap, no aggression. His head is still out of frame, so the turn is read entirely from the torso: the back gives way to the shoulder, then the chest arrives. The cigarette arm swings passively with the torso, below frame.
0:03.6–0:05.4 — HE CROSSES. Two unhurried steps toward the chair, closing the short distance from the window to the table. He grows in frame and sharpens as he comes into the focal plane. The trailing smoke column tears apart in the air he moves through and re-forms behind him. His head is still above the top edge.
0:05.4–0:07.6 — HE SITS, AND FINDS HER EYES ON THE WAY DOWN. He reaches the chair, takes its back with his LEFT hand below frame — his right hand is occupied by the cigarette and stays down — and draws it out with a low dry drag. He steps into the gap, turns his body square to her, and lowers himself. The descent is heavy and controlled: hips travel back before they travel down, the torso hinges slightly forward to counterbalance, the shoulders drop, and HIS HEAD DESCENDS INTO FRAME from above the top edge, arriving in the upper third. He comes fully sharp at this moment.
As his head enters the frame his eyes are ALREADY ON HER. He does not arrive looking down, does not land and then search for her. The eyeline is set before the head appears and travels down with it, locked on her the whole way, so the first thing we see of his face is a man already looking at her. He settles onto the seat with a small final drop and the chair frame compresses.
0:07.6–0:08.8 — He pulls the chair in a few centimetres, a short scrape and a settle. His shoulders release two or three centimetres as the weight comes off his legs. He shifts once to find the seat. Through all of it the eyeline does not break — the head and body move under the gaze while the gaze stays fixed on her. He is now framed chest up, close to frontal, filling the left two thirds of frame.
0:08.8–0:10 — HE HOLDS HER LOOK. Level, direct, unblinking except for one slow heavy blink. The eyes are locked just past the lens to screen-right at her eye height — not at her shoulder, not at her mouth, not at the space beside her. He is looking straight into her eyes and she is looking back. A slow exhale through the nose; smoke drifts forward across the space between them, spreads, then rises. The shot ends on that held look.
He does not speak. He does not lean forward, does not reach out, does not touch her, does not gesture, does not look into the lens, does not look away at any point once seated.
She does not move at any point beyond the millimetre rise and fall of her breath in the defocused foreground. She does not turn, does not shift, does not react to the chair or to him sitting down.

DIALOGUE
No dialogue in this shot. Neither character speaks. Both sets of lips stay completely still for the entire 10 seconds. No voice-over, no offscreen voices, no muttering, no breath vocalisations shaped as words. No subtitles, no captions.

AUDIO — FOLEY ONLY, ZERO AMBIENCE
The soundtrack contains exactly one element: close-mic foley generated by his body and by the chair. There is no second layer. There is no bed underneath. When no foley event is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.
The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry, going quieter once he is seated
2. Footsteps — two quiet, flat, soft-soled steps across the floor and one small adjusting step through the turn: no hard heel strike, no scuff, no tail
3. The chair — one dry drag as it is pulled out, catching once; one short scrape as it is pulled back in; the low dull creak of the frame taking his weight
4. Cloth — the shift of linen shirt fabric through the turn, through the walk, and as his shoulder line settles after he sits
5. Cigarette — a faint dry crackle of burning tobacco from below frame; fingers adjusting on the paper
6. Body — a single dry swallow, close-mic level only
She makes no sound at all — no breath, no sigh, no sniff, no cloth, no chair movement, no reply.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz — the pendant lamp above the table is unlit and silent. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No music, score, drone, pad, tension bed, sting, swell, riser, whoosh, sub-bass hit or reverb tail used as texture — nothing under the turn, nothing under the walk, nothing under the sit, nothing under the held look, nothing at the head or tail of the shot. No foley for objects not present or not in frame.
The mix stays close and dry: no room reverb, no distance perspective, no reflections off the walls, no spatialization.

PHYSICS
The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
The walk: real weight on a hard floor, unhurried, two steps, no stalking, no hesitation, no pause. He arrives at the chair as a man who has done this ten thousand times.
The chair: a real object with mass and friction, entirely below frame. It resists on the first pull, catches on the floor, then slides. It does not glide, does not float, does not travel further than it needs to. When he pulls it in beneath him it moves a short distance and stops dead.
Sitting: a controlled descent, not a drop and not a collapse. Hips back before down, knees flexing, the seat taking the weight with one small final settle and a compression of the chair frame. His shirt gathers and folds as he bends. Once seated, his shoulders release.
THE EYELINE. This is the anatomical spine of the second half of the shot. As he lowers, the head and neck counter-rotate to keep the eyes on target — the gaze stays fixed on a point in space at her eye height while the skull travels down beneath it, exactly as a real person keeps looking at someone while sitting. The vestibulo-ocular behaviour must read: the body moves, the eyes do not. Once seated, the eyes stay locked with only natural micro-saccades and one slow blink. He does not scan, does not glance at her shoulder or her hands, does not drop to the table, does not drift to the lens, does not look away.
Handedness: the cigarette is in his right hand for the entire shot and never leaves it, so all chair work is done with the left hand. He does not switch hands, does not raise the cigarette, does not take a drag, does not stub it out, does not put it down, does not tap ash. Its only visible presence is the smoke.
Smoke: real physical smoke and the largest moving element in a locked frame. A laminar ribbon rising from below the bottom edge, breaking into slow turbulence as it climbs past his body. The turn bends the standing column; the walk tears it apart and it re-forms behind him with real inertia. Once he is seated the ribbon re-establishes and rises steadily. The exhale at the end falls first, spreads horizontally, then rises. Slow and heavy, never CG particles, never faster than still indoor air allows. The smoke must never cross in front of his eyes and obscure the look.
Her stillness: breathing only, a few millimetres of rise and fall in the defocused foreground shape. No turn, no shift, no gesture, no reaction.

LIGHTING
Cold grey-green ambient from the window, the primary and only light source, behind him. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change as he turns, walks or sits. The pendant lamp above the table is switched OFF and contributes nothing.
The window is the brightest zone of the frame, a soft luminous field filling the background.
Standing at the glass with his back to camera he reads as a dark shape against that field, his shoulder line catching a thin cold edge from above and behind.
As he crosses toward the chair he steps out of the direct backlight and into the room's weak bounce off the plaster walls out of frame — so by the time he is seated his front is lit only by that bounce: a darker, softer, low-contrast face. Do NOT add a fill or a key when he sits. His face must not brighten as he comes down into the seat. Do not crush it to pure black either — THE EYES MUST STAY READABLE, because the last third of the shot is nothing but that look. The change in his exposure comes from him moving through the existing falloff, never from the lighting changing.
Her foreground shoulder and hair are the darkest mass in the frame — a soft near-silhouette with the faintest cold sheen on the top of the knot and on the shoulder of the white vest. That white vest is the one pale note in the foreground and stays desaturated and dim, never bright, never a hotspot.
The dark red curtain at the left frame edge is deeply desaturated — closer to brown-grey than red, low saturation. It is the only warm-leaning element in the palette.
The plant, the sill, the book stacks and the plaster behind him are dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass across the pale field — the brightest moving thing in the frame.
The cigarette ember is below frame and never seen. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim. No eye light — the eyes read through shape and shadow, not through an added catchlight.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
Character positions follow <<<image_1>>>: <<<char_captain>>> ends at the LEFT chair with his back toward the window, <<<char_wife>>> is seated at the RIGHT chair opposite him for the whole shot. Do not flip these positions.
The coloured markers in <<<image_1>>> are annotations only. No red or yellow shape, dot, line, outline, arrow or drawn figure appears anywhere in the render. Neither character wears red or yellow — costume comes from the character references: he in grey linen over dark, she in a white wrap vest over black.
The action is exactly this, once, in this order: he stands at the window with his back to camera, turns, walks two steps to the chair, pulls it out with his left hand, sits while already looking at her, settles, and holds her eyes to the end. Nothing else.
HE LOOKS HER IN THE EYES. From the moment his head enters the frame until the last frame, his gaze is locked on her eyes — level, direct, at her eye height, just past the lens to screen-right. He never looks down, never looks at her shoulder or hands, never looks away, never looks into the lens.
He starts STANDING with his head above the top edge of frame, and his head only enters the frame as he lowers into the chair. The camera does not adjust for this. If his head is fully in frame at 0:00, the framing is wrong.
Tight over-the-shoulder single: he is on the LEFT two thirds of frame, close to frontal once seated; her defocused shoulder and hair occupy the RIGHT edge. This composition never changes.
THE TABLE IS NEVER VISIBLE. The bottom edge of frame sits above the tabletop. No table surface, no table edge, no chairs, no hands, no objects on the table appear at any point.
No object of any kind appears in this shot — no device, no screen, no phone, no display, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock. Nothing is invented anywhere in frame.
Her face is never visible. She never turns toward camera, never turns toward him, never comes into focus. She is a shape for the entire 10 seconds.
Tripod, zero camera movement, framing pixel-identical from first frame to last, including through the turn, the walk and the sit.
Focus locked on the seated position and never moved. He walks into focus. No rack onto her, no rack onto the background.
He is already standing and already in frame in the first frame. No empty first frame, no establishing wide at any point.
Neither character speaks. Silence throughout, broken only by the listed foley.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass.
No visible brand marks, logos or legible lettering anywhere.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
Apart from the turn, the walk and the sit, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised, no slamming the chair.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin or fabric.

NEGATIVE — LOCAL LOCKS
No table in frame. If any part of the tabletop or its edge is visible, the framing is too loose.
No camera movement of any kind — no tilt up to keep his head while standing, no tilt down to follow him into the chair, no push, no pan. Hard lock.
No focus pull of any kind. Her foreground shoulder never comes sharp; the window never comes sharp; the focus does not travel to him while he walks.
No broken eyeline. He does not land in the chair looking down and then raise his eyes. He does not blink the look away. He does not check the room. The gaze is on her from the moment his face is visible.
No wide shot, no reverse angle, no cutaway, no second setup. One frame, one take.
No orange device anywhere in the shot, in frame or reflected.
No look to camera, no break of the fourth wall, no drift of the eyeline to the lens.
No aggression in the action: he does not yank the chair, does not scrape it loudly, does not drop into it, does not slam anything. The held look is steady, not a stare-down.
No dramatic performance: no crying, no grimace, no head shake, no nod, no smile, no clenched jaw held for effect, no lean forward.
No dialogue, no music, no ambience.
No hero lighting, no rim light, no eye light, no lens flare, no volumetric god rays beyond the natural backlit smoke.
````

### Generated videos

- 2026-08-28 21:21:25 · [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_212125_575db72b-3b59-46d1-8a61-95538a1aadb4.mp4)

## Earlier versions

Oldest first. Compare against the final to see what the author changed between attempts.

<details><summary>v1 · 2026-08-28 16:53:05 · 5 generation(s) · 032_20260828_165305_508f5ef9.md</summary>

````text
SCENE CONTEXT
A man stands at the window of a small apartment with his back to the room, smoking. He turns, crosses to the table and sits down opposite the woman. Tight single on him, frontal, framed past her out-of-focus shoulder. The table is never seen. One continuous 10-second take.

ACTIVE REFERENCES
<<<char_captain>>>: 40yo male, dark medium-length slightly disheveled hair, short dark beard with grey, deep-set eyes, fine lines at the corners. Grey collarless linen shirt over a dark under-layer, dark wide-leg trousers. A lit cigarette in his right hand, held low at his side and OUT OF FRAME below the bottom edge for the whole shot. 100% matches the reference. He is the sharp subject of this shot.
<<<char_wife>>>: 38yo woman, blonde hair pulled back into a low loose knot with fine strands escaping at the temple and the nape. White wrap vest with a wide shawl collar over a black t-shirt. In this shot she is a FOREGROUND element only: the back and side of her shoulder and the low knot of her hair, heavily out of focus, occupying the right edge of frame. Her face is never seen, she never turns, she never comes into focus. 100% matches the reference for hair, costume and build.
<<<loc_apt_cap>>>: small residential apartment — textured off-white plaster walls, a large three-pane window with a dark metal frame and a deep pale sill, a cold grey residential tower block filling the glass, heavy dark red curtains hanging as vertical bands at both edges of the window, tall dark leafy plants against the walls, stacks of old books and newspapers piled along the floor beneath the window, a sagging sofa and low coffee table at one end, a conical pendant lamp hanging over the table, a round pale table with metal-framed chairs. Geography, materials, colour and light only. Nothing in the room beyond what is listed here.
<<<image_1>>> — BLOCKING REFERENCE ONLY. A photograph of the room with the two seated positions marked on it. The RED marker is <<<char_captain>>>: the LEFT chair at the round table, his back toward the window, facing across the table to screen-right. The YELLOW marker is <<<char_wife>>>: the RIGHT chair, opposite him, facing across the table to screen-left. The window is directly behind the red position, a few paces back, with the book stacks and the sill beneath it.
Use this image ONLY for where the two of them are in the room, which way each faces, what lies behind each of them, and the short path he walks from the window to the left chair. Do NOT reproduce its wide framing — this shot is far tighter and holds only him. The coloured markers are annotations, not objects and not costume: no red or yellow shape, outline, dot, line, overlay or drawn figure appears anywhere in the render, and neither character wears red or yellow.

CAMERA AND FRAMING
Tight over-the-shoulder single on <<<char_captain>>>.
The camera sits just past <<<char_wife>>> on the right side of the room, close behind her shoulder, on the axis that runs across the table between them. Because the camera is almost on that axis, <<<char_captain>>> reads close to FRONTAL once he is seated — facing very nearly into the lens, with only a few degrees of offset. His eyeline goes just past the camera to her.
FOREGROUND, right edge of frame, running from the bottom edge upward: the out-of-focus mass of her shoulder, the side of her neck and the low knot of her hair. Dark, soft, no readable detail, no face, no eye. She occupies roughly the right quarter to right third of the frame and nothing more.
MIDGROUND, the left two thirds of frame: <<<char_captain>>>. THE FRAME IS SIZED FOR HIM SEATED — once he is in the chair it holds him from the CHEST UP, shoulders close to full width. Because the camera never moves, while he is still standing at the start his head is ABOVE the top edge and we see only his torso from roughly the waist to the shoulders. He descends into the frame as he sits. This is the point of the shot: the framing waits and he arrives in it.
THE TABLE IS NEVER IN FRAME. The bottom edge sits above the tabletop line, so no table surface, no table edge, no chair seat, no hands and no objects on the table are ever visible. His hands and the cigarette stay below the bottom edge throughout.
BACKGROUND, behind him and soft: the pale luminous window glass with the tower block dissolved into a wash beyond it, the deep pale sill running horizontally, the vertical band of the dark red curtain at the left edge, the dark shape of a plant, and the low dark mass of the book stacks. The pendant lamp hangs above and outside the top of frame and is not visible.
Camera height: SEATED eye height, level. Not looking up at him, not down at him. While he is standing this means the camera is well below his eyeline and his head is out of frame — do not correct for this.
TRIPOD, HEAD FULLY CLAMPED, ZERO MOVEMENT for the full 10 seconds: no push, no pull, no dolly, no truck, no crane, no boom, no pan, no tilt, no roll, no zoom, no handheld, no gimbal float, no parallax, no reframing, no drift, no stabilization wobble, no simulated breath tremble. The camera does not follow him across the room, does not tilt up to keep his head, and does not tilt down as he sits.
Framing is pixel-identical from the first frame to the last. The window sill line, the curtain edge and her foreground shoulder hold the exact same screen positions at 0:10 as at 0:00 — that is the test of whether the lock held.

OPTICS
Roughly 30° diagonal field of view, short-telephoto character, camera positioned back from him rather than pushed into his face.
Shallow-to-moderate depth of field. THE FOCAL PLANE IS SET ON THE SEATED POSITION and does not move. Her foreground shoulder and hair fall well in front of the plane and are strongly defocused into a soft dark mass. The window, the sill, the book stacks and the plant behind him fall behind the plane and are soft, the tower block dissolving into a pale luminous wash with its window grid barely legible.
Because the focus is locked to the chair, he is SOFT while standing at the window at the start, sharpens as he walks in, and is fully sharp only once he has sat down. He walks into focus; the focus never travels to meet him. No focus pull, no rack focus onto her, no focus hunting, no lens breathing, no zoom.
The background sits flat and close behind him rather than receding. Once seated, skin texture, the grey in his beard, the weave of the linen shirt and the smoke are all readable at this scale.

FIRST FRAME AND SPATIAL BLOCKING
First frame: <<<char_captain>>> is STANDING at the window, a few paces back from the chair, his BACK to the room and to camera, looking out at the tower block. He occupies the left two thirds of frame from roughly the waist to the shoulders — his head is cropped off by the TOP edge of frame and is not visible. He is slightly soft, sitting behind the focal plane.
His shoulders are low, his weight settled on one leg. The cigarette is in his right hand at his side, below the bottom edge, and a thin ribbon of smoke rises past his hip and shoulder and up out of the top of frame through the window light.
Her defocused shoulder and hair occupy the right edge of frame as a dark soft mass. Behind him the pale window field, the sill, the red curtain band at the left edge, the dark plant, the book stacks, all soft.
No empty first frame. No establishing wide at any point. He is large and immediate in frame one, even without his head.

FORMAT MODE
Single continuous take. 10 seconds. No cuts, no fades, no dissolves, no transitions. Real-time motion, no slow motion. One figure moving through a locked frame and one defocused foreground shape, for the whole shot.

ACTION TIMING — 10 SECONDS
0:00–0:02 — He stands at the window, back to camera, head above the top edge of frame. One slow shallow breath — the shoulder line barely moves. Smoke rises past him in an unbroken ribbon. She does not move.
0:02–0:03.6 — THE TURN. He turns, head and body together, not head alone. The rotation starts at the hips and shoulders, the feet adjusting one small step, and carries through until he is facing into the room, toward the table and toward camera. Roughly 160 to 180 degrees, unhurried, no snap, no aggression. His head is still out of frame, so the turn is read entirely from the torso: the back gives way to the shoulder, then the chest arrives. The cigarette arm swings passively with the torso, below frame.
0:03.6–0:05.4 — HE CROSSES. Two unhurried steps toward the chair, closing the short distance from the window to the table. He grows in frame and sharpens as he comes into the focal plane. The trailing smoke column tears apart in the air he moves through and re-forms behind him. His head is still above the top edge.
0:05.4–0:07.6 — HE SITS. He reaches the chair, takes its back with his LEFT hand below frame — his right hand is occupied by the cigarette and stays down — and draws it out with a low dry drag. He steps into the gap, turns his body square to her, and lowers himself. The descent is heavy and controlled: hips travel back before they travel down, the torso hinges slightly forward to counterbalance, the shoulders drop, and HIS HEAD DESCENDS INTO FRAME from above the top edge, arriving in the upper third. He settles onto the seat with a small final drop and the chair frame compresses. At this moment he comes fully sharp.
0:07.6–0:08.8 — He pulls the chair in a few centimetres, a short scrape and a settle. His shoulders release two or three centimetres as the weight comes off his legs. He shifts once to find the seat. He is now framed chest up, close to frontal, filling the left two thirds of frame.
0:08.8–0:10 — HIS EYES COME UP to her. The head barely moves; the eyes do the work, rising and settling just past the lens to screen-right. He holds. A slow exhale through the nose; smoke drifts forward across the space between them, spreads, then rises. The shot ends with him seated, sharp, looking at someone we never see.
He does not speak. He does not lean forward, does not reach out, does not touch her, does not gesture, does not look into the lens, does not look away once his eyes have landed.
She does not move at any point beyond the millimetre rise and fall of her breath in the defocused foreground. She does not turn, does not shift, does not react to the chair or to him sitting down.

DIALOGUE
No dialogue in this shot. Neither character speaks. Both sets of lips stay completely still for the entire 10 seconds. No voice-over, no offscreen voices, no muttering, no breath vocalisations shaped as words. No subtitles, no captions.

AUDIO — FOLEY ONLY, ZERO AMBIENCE
The soundtrack contains exactly one element: close-mic foley generated by his body and by the chair. There is no second layer. There is no bed underneath. When no foley event is playing, the track is absolute digital silence — a flat zero, empty and dead. This vacuum is the intended effect and must not be softened, filled, or made to feel natural.
The complete list of permitted sounds. Nothing outside this list may appear anywhere in the 10 seconds:
1. His breath — slow shallow nasal inhales and exhales, close and dry, going quieter once he is seated
2. Footsteps — two quiet, flat, soft-soled steps across the floor and one small adjusting step through the turn: no hard heel strike, no scuff, no tail
3. The chair — one dry drag as it is pulled out, catching once; one short scrape as it is pulled back in; the low dull creak of the frame taking his weight
4. Cloth — the shift of linen shirt fabric through the turn, through the walk, and as his shoulder line settles after he sits
5. Cigarette — a faint dry crackle of burning tobacco from below frame; fingers adjusting on the paper
6. Body — a single dry swallow, close-mic level only
She makes no sound at all — no breath, no sigh, no sniff, no cloth, no chair movement, no reply.
Absolutely no ambience, in any form, under any name. Specifically forbidden: room tone, roomtone, air, atmos, atmosphere, ambience, ambient bed, background bed, environmental wash, field recording, "quiet apartment" tone, presence track, noise floor, low-level rumble, synthesized air, or any continuous layer added to make the silence feel natural. No HVAC, air conditioning, ventilation, compressor, refrigerator, radiator tick, electrical hum, mains hum or lamp buzz — the pendant lamp above the table is unlit and silent. No sound from outside the window: no traffic, no city rumble, no wind, no rain, no birds, no distant voices, no sirens, no aircraft, no construction, no children, no glass resonance, no muffled exterior anything — the window is a light source, never a sound source. No building sounds: no neighbours, no pipes, no footsteps above or below, no doors, no structural creaks, no plumbing, no lift. No music, score, drone, pad, tension bed, sting, swell, riser, whoosh, sub-bass hit or reverb tail used as texture — nothing under the turn, nothing under the walk, nothing under the sit, nothing at the head or tail of the shot. No foley for objects not present or not in frame.
The mix stays close and dry: no room reverb, no distance perspective, no reflections off the walls, no spatialization.

PHYSICS
The turn: rotation initiated from the hips and shoulders, the head arriving with the body rather than leading it. One small corrective step of the feet, weight redistributing. The cigarette arm swings passively with the torso; the hand does not rise. The turn completes in a single continuous movement — no half-turn, no hesitation mid-rotation, no stagger, no pivot on the spot without foot movement.
The walk: real weight on a hard floor, unhurried, two steps, no stalking, no hesitation, no pause. He arrives at the chair as a man who has done this ten thousand times.
The chair: a real object with mass and friction, entirely below frame. It resists on the first pull, catches on the floor, then slides. It does not glide, does not float, does not travel further than it needs to. When he pulls it in beneath him it moves a short distance and stops dead.
Sitting: a controlled descent, not a drop and not a collapse. Hips back before down, knees flexing, the seat taking the weight with one small final settle and a compression of the chair frame. His shirt gathers and folds as he bends. Once seated, his shoulders release.
Handedness: the cigarette is in his right hand for the entire shot and never leaves it, so all chair work is done with the left hand. He does not switch hands, does not raise the cigarette, does not take a drag, does not stub it out, does not put it down, does not tap ash. Its only visible presence is the smoke.
Smoke: real physical smoke and the largest moving element in a locked frame. A laminar ribbon rising from below the bottom edge, breaking into slow turbulence as it climbs past his body. The turn bends the standing column; the walk tears it apart and it re-forms behind him with real inertia. Once he is seated the ribbon re-establishes and rises steadily. The exhale at the end falls first, spreads horizontally, then rises. Slow and heavy, never CG particles, never faster than still indoor air allows.
Eyeline: once his eyes land on her they stay there to the last frame. Real ocular behaviour — the eyes settle on a point and hold, with only natural micro-saccades and perhaps one slow blink. He does not scan, does not glance away, does not drift to the lens.
Her stillness: breathing only, a few millimetres of rise and fall in the defocused foreground shape. No turn, no shift, no gesture, no reaction.

LIGHTING
Cold grey-green ambient from the window, the primary and only light source, behind him. Diffuse, flat, overcast exterior light through residential glass. Constant for the full 10 seconds — no change in level, colour or direction, no change as he turns, walks or sits. The pendant lamp above the table is switched OFF and contributes nothing.
The window is the brightest zone of the frame, a soft luminous field filling the background.
Standing at the glass with his back to camera he reads as a dark shape against that field, his shoulder line catching a thin cold edge from above and behind.
As he crosses toward the chair he steps out of the direct backlight and into the room's weak bounce off the plaster walls out of frame — so by the time he is seated his front is lit only by that bounce: a darker, softer, low-contrast face. Do NOT add a fill or a key when he sits. His face must not brighten as he comes down into the seat. Do not crush it to pure black either — the eyes must stay readable, because at the end of the shot they are the whole shot. The change in his exposure comes from him moving through the existing falloff, never from the lighting changing.
Her foreground shoulder and hair are the darkest mass in the frame — a soft near-silhouette with the faintest cold sheen on the top of the knot and on the shoulder of the white vest. That white vest is the one pale note in the foreground and stays desaturated and dim, never bright, never a hotspot.
The dark red curtain at the left frame edge is deeply desaturated — closer to brown-grey than red, low saturation. It is the only warm-leaning element in the palette.
The plant, the sill, the book stacks and the plaster behind him are dim soft masses, unlit by anything.
The smoke is fully backlit by the window and reads as a bright volumetric mass across the pale field — the brightest moving thing in the frame.
The cigarette ember is below frame and never seen. No warm bounce, no orange fill on skin.
No fill. No beauty key. No practicals. No artificial rim. No eye light.
Kodak Vision3 500T — fine grain, cold grey-green cast, natural contrast, no HDR, no heavy grade.

POSITIVE CONSTRAINTS
Character positions follow <<<image_1>>>: <<<char_captain>>> ends at the LEFT chair with his back toward the window, <<<char_wife>>> is seated at the RIGHT chair opposite him for the whole shot. Do not flip these positions.
The coloured markers in <<<image_1>>> are annotations only. No red or yellow shape, dot, line, outline, arrow or drawn figure appears anywhere in the render. Neither character wears red or yellow — costume comes from the character references: he in grey linen over dark, she in a white wrap vest over black.
The action is exactly this, once, in this order: he stands at the window with his back to camera, turns, walks two steps to the chair, pulls it out with his left hand, sits, settles, and lifts his eyes to her. Nothing else.
He starts STANDING with his head above the top edge of frame, and his head only enters the frame as he lowers into the chair. The camera does not adjust for this. If his head is fully in frame at 0:00, the framing is wrong.
Tight over-the-shoulder single: he is on the LEFT two thirds of frame, close to frontal once seated; her defocused shoulder and hair occupy the RIGHT edge. This composition never changes.
THE TABLE IS NEVER VISIBLE. The bottom edge of frame sits above the tabletop. No table surface, no table edge, no chairs, no hands, no objects on the table appear at any point.
No object of any kind appears in this shot — no device, no screen, no phone, no display, no readout, no on-screen text, no ashtray, no cups, no bottles, no papers, no photographs, no clock. Nothing is invented anywhere in frame.
Her face is never visible. She never turns toward camera, never turns toward him, never comes into focus. She is a shape for the entire 10 seconds.
Tripod, zero camera movement, framing pixel-identical from first frame to last, including through the turn, the walk and the sit.
Focus locked on the seated position and never moved. He walks into focus. No rack onto her, no rack onto the background.
He is already standing and already in frame in the first frame. No empty first frame, no establishing wide at any point.
Neither character speaks. Silence throughout, broken only by the listed foley.
His eyeline lands on her just past the lens at the end and stays there. He never looks into the lens.
Exactly two people in the room. No extra characters, no duplicates, nobody enters or leaves, no figures or movement visible through the window, no reflections of other people in the glass.
No visible brand marks, logos or legible lettering anywhere.
Single continuous take, exactly 10 seconds, no cuts, real-time motion.
Apart from the turn, the walk and the sit, all movement is at micro scale. No large gestures, no crying, no grimace, no head shake, no nod, no smile, no pointing, no arms raised, no slamming the chair.
Fine grain, cold grey-green palette, stable exposure across the full duration. No blown highlight halation. No CG gloss on skin or fabric.

NEGATIVE — LOCAL LOCKS
No table in frame. If any part of the tabletop or its edge is visible, the framing is too loose.
No camera movement of any kind — no tilt up to keep his head while standing, no tilt down to follow him into the chair, no push, no pan. Hard lock.
No focus pull of any kind. Her foreground shoulder never comes sharp; the window never comes sharp; the focus does not travel to him while he walks.
No wide shot, no reverse angle, no cutaway, no second setup. One frame, one take.
No orange device anywhere in the shot, in frame or reflected.
No look to camera, no break of the fourth wall, no drift of the eyeline to the lens.
No aggression in the action: he does not yank the chair, does not scrape it loudly, does not drop into it, does not slam anything.
No dramatic performance: no crying, no grimace, no head shake, no nod, no smile, no clenched jaw held for effect, no lean forward.
No dialogue, no music, no ambience.
No hero lighting, no rim light, no eye light, no lens flare, no volumetric god rays beyond the natural backlit smoke.
````

- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_165305_508f5ef9-719e-4b35-acea-924bbd21e385.mp4)
- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_165723_38d32097-ebcd-44ee-8f0b-ff8d9e133ef4.mp4)
- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_210153_76313ece-87ac-4efa-8db0-2e1d95a2f567.mp4)
- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_210919_c361994a-ef17-460c-add5-96263f2e2ede.mp4)
- [video](https://d8j0ntlcm91z4.cloudfront.net/user_32KhQdtLdeVmwm7igkUuGWxEdNQ/hf_20260828_211400_003b8e60-4ff8-4620-b941-dd9797b6fb78.mp4)

</details>
