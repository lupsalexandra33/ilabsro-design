# Context engineering (Reel)

**Type:** Instagram Reel, 1080×1920 MP4, 33 s, silent
**Status:** Validated example (kit test render)
**Skills:** `reels-maker` + `friendly-lens` + `human-pass`
**Family:** handwritten / human teaching · **Ending:** pig + logo

## What this is

The first end-to-end Reel rendered with the IL Reel Kit. The source is the same approved brief as the `context-engineering` carousel, so the two can be compared as one idea in a static and a time-based format.

## What it tests

- hook readable at frame 0 ("Still polishing the prompt?"), with the polishing loop shown through strike-and-rewrite motion;
- teaching through marks: box + divider drawing, sticky notes filling the gap, then circle / strike / underline with margin questions;
- quiet evidence note and "illustrative" labels that keep the brief's boundaries without dominating;
- scene grounds that vary (alt, white, tint) inside the Light teal system;
- the reading-time, safe-zone, type-size and hook lint (clean on the final render);
- `human-pass` on the extracted on-screen copy (zero lexicon hits, zero IL voice flags).

## Learned during the test (now in the kit README)

- The first layout sat too high and left the bottom third empty. Content blocks were moved to the centre of the safe zone.
- A light cyan highlight behind dark text needs strong opacity to read.
- `detect.py` scores short Reel lines low on burstiness by design. For on-screen copy the gate is the lexicon and the structural flags.

## Files

- `reel.html` — the source (open in a browser to play; uses `kit/` and `assets/`)
- `reel.mp4` — rendered output
- `cover-4x5.jpg` — the profile-grid crop of the cover frame
- `sheet.jpg` — one frame per second
- `onscreen.txt` — extracted on-screen copy
- `prompt.md` — the generation prompt

Study the decisions, not the layout. Don't reuse the copy, sequence or composition for a new Reel.
