# Prompt template

[← README](README.md)

This skeleton is distilled from the 387 CONTROL prompts. Almost all of them (377) open with `SCENE CONTEXT` and close with `POSITIVE CONSTRAINTS`, and in between they follow the same order. Fill in what you need. Each section links to every variant the author wrote for it in [sections/](sections/README.md).

The prompts come in two styles:

- **Compact style** (earlier shots): 12 sections, about 4–8K characters. Good model: [scene-02-08, red shower ECU](shots/scene-02/08_a-man-stands-alone-in-a-deep-red-shower-head-bowed.md).
- **Locked style** (later shots, scenes 08–12): the compact style plus `OUTPUT SETTINGS`, a `NO MUSIC — ABSOLUTE` block, `FRAMING`, a "what this shot is doing" section and several `… LOCK` blocks. About 10–20K characters. Each lock exists to stop a specific failure the model kept producing. Good model: [the Captain turning his head as the son is carried out](shots/scene-08/22_medium-shot-on-the-armored-captain-two-agents-carr.md).

Start compact, and add a lock only when a generation gets that part wrong. This is how the author worked: compare any shot's *Earlier versions* with its final prompt.

---

## Skeleton

````text
SCENE CONTEXT
<2–5 plain sentences: who, where, what happens, and the emotional point. End on what the shot is ABOUT, e.g. "He is not moving. He is thinking.">

OUTPUT SETTINGS
Single continuous <handheld|locked-off|dolly> take, <N> seconds, real-time motion, no internal cuts. <Wordless. No dialogue, no subtitles, no captions.>
REAL-TIME ONLY. No slow motion, no speed ramp, no time stretch, no frame blending.

NO MUSIC — ABSOLUTE            (optional; copy from REUSABLE_BLOCKS.md)

ACTIVE REFERENCES
<<<char_x>>>: <age, build, hair, face, wardrobe, position in this shot, what is/isn't visible>. 100% matches the reference.
<<<loc_y>>>: <space, materials, palette, light direction>. Geography, materials, palette and light direction only.
<<<prop_z>>>: <object, state, where it sits>.

LOCATION MAP
<<<char_x>>>: <position on screen: screen-left / center / right, facing direction>
<Furniture / landmarks>: <position on screen>
Camera: <position, height, distance, axis>.
<Light source>: <where, on or off screen>.

FIRST FRAME AND SPATIAL BLOCKING
First frame: <exact composition at 0:00: what fills the frame, edges, crops>.
No establishing shot, no push-in, no empty frame first.

FORMAT MODE
Single continuous uncut take. <N> seconds. No cuts. <Camera support in one line>.

FRAMING                        (locked style)
<Shot size, what the frame holds from/to, angle, off-centre placement, what is soft in the background>.

OPTICS
<Focal length, e.g. 85mm equivalent>. <Depth of field>. <Where focus sits and that it never racks>. Straight lines stay straight, no distortion.

ACTION TIMING
0:00 to 0:02 — <beat>
0:02 to 0:04 — <beat>
0:04 to 0:06 — <beat; end on a held state, not an action>
<List what the subject does NOT do: does not speak, does not look at the lens, ...>

WHAT THIS SHOT IS DOING        (locked style, optional)
<The subtext in prose, and how it must NOT read: not remorse, not hesitation...>

<SUBJECT> LOCK — <RULE>       (locked style, add as needed: FACE, STILLNESS, LIGHT EMISSION, CONTINUITY...)
<Exhaustive list of the one thing that must never happen>.

CAMERA
<Support and operator: e.g. naturalistic documentary handheld, shoulder-mounted, near-static>.
<What it does NOT do: no push, no pan, no reframe, no reacting to the action>.
<Organic behaviour: breathing drift, late micro-corrections, horizon slightly off level>.

PHYSICS
<Weight and mass of bodies, gear, cloth, liquids. Real ground contact. No floating, no rubbery CG motion, no snapping between poses>.

LIGHTING
<Single motivated source, direction, quality, colour>. <What catches light, what stays dark>. <The light never changes>. No fill, no rim, no beauty light.

AUDIO
Diegetic only, and this is the complete list of what is heard:
1. <room tone>
2. <action sounds>
3. <offscreen sounds>
That is everything. <No dialogue / no music>.

POSITIVE CONSTRAINTS
<Restate the non-negotiables as facts: identity 100% matches reference, exact count of people, what stays out of frame, first frame matches reference, no subtitles, no music>.
````

---

## Section guide

| # | Section | Used in | What it does | Variants |
|---|---|---|---|---|
| 1 | `SCENE CONTEXT` | 377 | A short logline plus the emotional point. Written like a script, not a list of keywords. | [01](sections/01_scene-context.md) |
| 2 | `OUTPUT SETTINGS` | 135 | Take length, continuity, real-time, wordless. Mostly boilerplate. | [02](sections/02_output-settings.md) |
| 3 | `FORMAT MODE` | 249 | A one-line version of the above that also names the camera support. | [03](sections/03_format-mode.md) |
| 4 | `ACTIVE REFERENCES` | 354 | One paragraph per element: its look **plus its role in this shot**. Ends with "100% matches the reference." | [04](sections/04_active-references.md) · [ELEMENTS.md](ELEMENTS.md) |
| 5 | `LOCATION MAP` / `GEOGRAPHY` | 237 | Places each element in screen space (screen-left/centre/right) and places the camera. | [05](sections/05_location-map.md) |
| 6 | `FIRST FRAME (AND SPATIAL BLOCKING)` | 326 | Describes frame 0 exactly. Stops the model from opening on an establishing shot. | [06](sections/06_first-frame.md) |
| 7 | `FRAMING` | 89 | Shot size and crop edges, for more precise control. | [07](sections/07_framing.md) |
| 8 | `ACTION TIMING` | 245+ | Second-by-second beats. Always ends with a hold, followed by a list of what does *not* happen. | [08](sections/08_action-timing.md) |
| 9 | `DIALOGUE` | 34 | Exact lines, who says them and when, and how they are delivered. | [09](sections/09_dialogue.md) |
| 10 | `BREATHING` | 49 | Keeps characters alive during holds. | [10](sections/10_breathing.md) |
| 11 | `OPTICS` | 326 | Lens, depth of field, focus that never racks, no distortion. | [11](sections/11_optics.md) |
| 12 | `CAMERA` | 303 | How the camera is supported and moves, and an explicit list of moves it must *not* make. | [12](sections/12_camera.md) |
| 13 | `PHYSICS` | 334 | Weight, mass, gravity and contact. The main defence against a "CG look". | [13](sections/13_physics.md) |
| 14 | `LIGHTING` | 373 | One motivated source that never changes, and a list of banned lights. | [14](sections/14_lighting.md) |
| 15 | `AUDIO` | 321 | A closed, numbered list of what is heard, so nothing else gets added. | [15](sections/15_audio.md) |
| 16 | `… LOCK` blocks | ~100 | One failure mode per block: face, stillness, glowing lenses, continuity... | [16](sections/16_locks.md) |
| 17 | `POSITIVE CONSTRAINTS` | 364 | Restates the must-haves as facts. Always the last section. | [17](sections/17_positive-constraints.md) |
| 19 | Performance / intent | — | Free-form sections like `THE FACE`, `THE HANDS`, `WHAT THIS SHOT IS DOING`. | [19](sections/19_performance-and-intent.md) |

## Habits worth copying

- **Refer to elements by tag.** Every mention of a character uses `<<<element>>>`, never "he" alone, so the model never has to guess who is meant.
- **Use the screen-direction vocabulary.** "screen-left", "lower center-left", "strict left-facing profile", "three-quarter".
- **Say what doesn't happen.** Each beat or move is followed by the things that must not happen ("does not turn back, does not lower his head…").
- **End on a hold.** The last 1–2 seconds are stillness, so the clip doesn't end mid-action.
- **Close the lists.** "This is the complete list of what is heard. Nothing else is added."
- **Use one light source that never changes.** List the banned lights (fill, rim, beauty, coloured) instead of hoping they won't appear.
- **Design for the cut.** Describe the first frame exactly and the last state exactly, so shots edit together.
- **Specify real-time motion.** "Real-time only, no slow motion" appears in almost every prompt because the models default to dreamy slow-mo.
- **Fix one thing per iteration.** Shots with many versions (see the `Ver.` column in [INDEX.md](INDEX.md)) show which failures needed which locks.
