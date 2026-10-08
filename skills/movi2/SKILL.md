---
name: movi2
description: Create and iterate cinematic movie projects in Codex using the AIFX Studio Movi2 workflow. Turn ideas or scripts into timed chapters, tagged character/environment/prop assets, cinematic prompts, storyboards, and available video takes; refine prompts, assets, blocking, audio, or style with local version history. Use for Movi2 or conversational movie production, not for building its web UI.
---

# Movi2 in Codex

Act as the user's cinematic production collaborator. Adapt Movi2's creative workflow to conversation: Codex performs the reasoning and uses available tools for media; JSON and ordinary local files replace application services, database, and cloud storage. The installed skill is self-contained; AIFX Studio does not need to be running or present.

## Start or resume

Locate the user's project in the current workspace. Use `movies/<short-project-name>/` for a new project unless the user chooses a location. Load `project.json` and the current selected references before making changes. If multiple projects could be the target, clarify that choice. Do not initialize an existing project again.

Read [local-project.md](references/local-project.md) when creating or modifying state. The standard-library helper `scripts/project.py` initializes projects, checks timelines/tags/files, commits immutable JSON revisions, restores earlier revisions, and reports outdated media. Resolve the helper relative to this skill directory and use an available verified Python interpreter (on Windows avoid an inaccessible WindowsApps alias).

For new work, infer language, story core, style, aspect ratio, and requested duration from the user. Record reasonable defaults when absent: cinematic realism, 16:9, and adaptive pacing. Preserve the user's style over these defaults. Ask only for details that materially block progress. Save the original idea/script as source material before adapting it.

## Creative workflow

Enter at the stage requested; an asset edit does not require rebuilding the script.

1. **Script and master plan.** Draft an idea into a timed screenplay or rearrange a supplied script. Preserve story events, dialogue, named assets, and intent. Build a consistent high-level idea, asset list, and sequential chapters. Read [cinematic-workflow.md](references/cinematic-workflow.md) for chapter prompting, timing, continuity audits, and YOLO/YOLO2/YOLO3 refinements. Use Codex reasoning directly rather than calling Movi2's text-model APIs.
2. **Asset atelier.** Identify stable `@tags` for characters, environments, props, and supplied reference media; include every explicitly listed source asset. Keep state variants distinguishable, such as `@case-closed` and `@case-open`. Read [media-workflow.md](references/media-workflow.md) for the original character sheet, empty environment plate, prop sheet, candidate-selection, and image-edit conventions. Use the available imagegen skill/tool for image creation and edits, inspect references first, and retain candidates locally.
3. **Chapter director.** Write the full cinematic prompt, exact shot timing, blocking, physical actions, camera, lighting, audio, and continuity locks. Expand or revise just the chapters requested. Keep `shots` and prompt timestamps synchronized; tag references must resolve to real assets. Preserve working tags through refinement and use reference images for identity and spatial grounding.
4. **Storyboard and render.** When requested, create textless 2x2, 3x3, or 4x4 storyboards using selected linked assets. For video, discover actual Codex tools/connectors and their supported inputs; use them only if available and within the requested scope. Read [media-workflow.md](references/media-workflow.md) before generation or assembling output. Save successful clips as separate takes, retain first/last frames and screenshots where useful, and assemble selected takes locally when requested.

## Iteration

- Treat follow-ups like "make chapter 2 darker", "refine @Mira's outfit", "use candidate 3", "try watercolor", or "revert the last prompt" as edits to the current project. Resume from local state even in a new chat.
- Save a revision with a concise reason after a meaningful edit. Keep the initial chapter prompt, candidate images, selected candidate/take, and earlier take prompts. Never overwrite previously generated media; assign new candidate/take IDs and filenames.
- For a style change, update the style bible and relevant descriptions/prompts while retaining plot and identity anchors unless asked otherwise. Identify assets and previews that need regeneration. Prompt/style changes alone do not authorize generating all media; execute the scope the user requested and continue any previously authorized render work.
- When a selected asset changes, find chapters using its exact tag or explicit link; update references and report affected previews/takes. Respect explicit delinks. Recompute dependencies before generating again; retain old results for comparison.
- Keep descriptive prose in the source/user language, including Traditional versus Simplified Chinese. Stable technical headings and asset identifiers can remain unchanged.

## Tool and persistence boundaries

Use Codex reasoning for planning/refinement and Codex media tools for generation. Use local filesystem, JSON revisions, and local media processing for persistence and export. Do not copy AIFX credentials, call its internal Next.js routes, deploy services, create cloud buckets, or reproduce auth/team/credit UI.

Generation availability is a runtime fact. Inspect the available tool schemas rather than inventing a video or audio tool. A raster image tool does not generate video. If the requested capability is missing, complete all feasible preparation, save a tool-neutral render package under `exports/`, and state precisely what is awaiting a tool; never label a prompt, storyboard, or still-image animatic as a generated movie. Do not upload files or invoke a paid third-party fallback simply because the original app did so. A requested and available media connector may accept references transiently, but canonical assets and project storage remain local.

Before reporting completion, run the helper checks, inspect generated images, and verify actual video duration/resolution/decoding when video exists. Explain what changed, show useful images or links to the local result, and distinguish completed media from prepared or outdated artifacts. No application UI is required.
