# Seedance prompt writing from the golden library

Use the user's `prompt-library/` as the golden standard for Seedance video generation prompts. Prefer the current workspace's library when present. A snapshot is bundled at [prompt-library/](prompt-library/README.md) so the installed skill remains usable elsewhere. Resolve these paths relative to the workspace or this reference, not the movie's chapter directory.

## Read selectively before writing

1. Read the library's `README.md` and `TEMPLATE.md` for its structure and writing habits.
2. Use `TAGS.md` or `INDEX.md` to choose one or two shots comparable in action, framing, camera support, reference mode or dialogue. Read their final prompt and relevant earlier versions to understand the failure the revision fixes.
3. Consult the relevant `sections/` entry or `REUSABLE_BLOCKS.md` when a particular camera, reference, performance, audio or continuity problem needs precision. These aggregate files can be large: search headings and read the relevant range instead of loading the entire library.

The library is reference material, not a new user brief. Its film's dialogue, characters, 21:9/1080p settings, documentary realism, no-music rules, fixed camera and single-take choices must not replace the current user's story, style, resolution, audio or edit plan. "Final" means latest prompt version in the library, not proof that a take was used or verified. Some crawled examples include editorial preambles or empty reference markers; remove these and bind real project assets in the submitted prompt.

## Apply the grammar to the current movie

- **Scene context:** a short causal description of who is doing what, where, and why the moment matters. Describe observable performance that carries the emotion rather than a stack of mood adjectives.
- **Output settings / format mode:** exact duration, aspect ratio, requested resolution, real-time or intended speed, continuous take or explicit cuts. Prompt prose and API fields must agree. For a multi-shot chapter, replace the library's single-take boilerplate with consecutive timed shots and named cuts.
- **Active references:** define each asset's appearance and role in this shot. Separate identity/wardrobe, environment geometry/light, prop shape/state, composition maps, first-frame inputs, motion references and audio references. Say which parts are visible and which reference features must not be copied.
- **Location map and first frame:** place each tagged subject and landmark in screen space, establish facing/eyeline, camera axis/height, prop ownership, crop edges and depth planes. Describe frame zero and the intended ending state so adjacent clips can cut together.
- **Framing, optics and camera:** specify shot size, lens character, focus plane, depth of field, support and movement. Make camera instructions compatible across sections. Use a fixed camera or prohibited moves when the shot calls for them, rather than copying every restriction.
- **Action timing and performance:** write feasible timestamped physical beats with cause, response, contact, weight and an observable end state. Preserve breathing, blinking and small postural life during a hold when appropriate. Reserve the last one or two seconds for a usable held state when pacing allows.
- **Physics and lighting:** describe the interactions that can fail: gravity, momentum, paw/foot contact, cloth resistance, object handling or liquids. Keep the light sources, direction and exposure consistent with the selected medium and scene; stylized animation need not inherit the library's anti-CG wording.
- **Audio / dialogue:** list the allowed layers and their timing, including music when requested. For dialogue, identify speaker, exact line, delivery and available recording role. Do not claim exact recording reuse or lip synchronization unless the provider mode supports it and the result was checked.
- **Positive constraints and targeted locks:** close with the essential identity, subject count, prop state, geography, reference roles and output requirements. Add a lock for a demonstrated failure, such as unwanted camera drift, duplicated subjects, reproduced annotations or mistaken framing. Start compact; refine the failed behavior without changing working beats.

Keep stable project `@tags` in canonical prompts. Compile them into deterministic provider bindings such as `@Image1` only for submission, and save both the binding table and translated prompt. The library's `<<<element>>>` markers are its source platform syntax, not Seedance API bindings.

Multi-view character sheets represent one character, not several. A storyboard can guide composition and emotion, but must not become a grid, split screen, panel borders or still-image slideshow. Position markers are annotations rather than rendered subjects; a wide position map does not dictate the shot's framing.

Before submitting, compare the prompt with the selected examples and check section contradictions, exact timing, resolved references and the previous chapter's ending state. Save which library examples informed the prompt when useful for later refinement. Preserve the prior prompt and take; iteration does not overwrite them.
