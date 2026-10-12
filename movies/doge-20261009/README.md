# doge-20261009

New Movi2 movie adapted from the supplied plot. Tart is the beige guide dog; Tine is the brown therapy dog with a cream heart patch. The planned film runs 390 seconds across 24 chapters with 75 directed shots. It uses warm, expressive 3D animation inspired by *Up*, Cantonese dialogue, original music, and no in-video titles or credits.

The approved images are stored separately in `assets/`; the original supplied dog sheets are preserved in `references/`. The immutable source plot is archived in `source/`. Asset approval and revisions live in `project.json` and `history/`. Only individual approved images and the chapter text prompt enter generation; the review galleries are excluded.

`direct_render.py` journals every provider task before polling. Re-running its `render` command polls accepted tasks and reuses downloaded clips. It refuses duplicate submissions when a previous POST outcome is uncertain, and it does not automatically pay for retries of failed tasks. The adapter reads only the four explicitly authorized settings at runtime; credentials and temporary tokens are never stored in this project.

`finish_movie.py inspect` fully decodes downloaded clips, records their metadata, and extracts three sample frames per chapter. `sync` commits task records; `sync --select` is used after visual inspection. `assemble` joins selected successful takes, preserves generated audio, normalizes the video to 1470×630 at 30 fps, verifies the full decode and 11,700-frame runtime, and fades the ending to black.

Final delivery path: `exports/doge-20261009-720p-21x9.mp4`. Technical evidence is written to `exports/video-verification.json` and `exports/assembly-manifest.json` when assembly completes.


<!-- movie-source-archive -->
## Versioned source archive

`source/` contains the current creative plan, original story, screenplay, final chapter prompts, shot timing, selected asset images and supplied reference media. `source/delivery-summary.json` records compact observed delivery checks.

Production scripts beside this README are retained. Live `project.json`, local revisions, proposals, rendered takes, exports, review images, downloaded tools and task journals are ignored and remain on disk.

On a fresh checkout, run `python restore_local_project.py` with a working Python interpreter to initialize local state and copy the versioned media references into their working locations. The command preserves an existing local project and never submits a render. New generation requires asset review and explicit authorization for provider credentials.
