# IL Reel Kit

The default production path for `reels-maker`: HTML + a deterministic timeline → Playwright frame capture → ffmpeg H.264.

## Requirements

- Node 18+
- Playwright with Chromium (`npm i -g playwright`, then `npx playwright install chromium` if no browser is present)
- ffmpeg and ffprobe on PATH
- Fonts: Poppins, IBM Plex Mono and Caveat (all SIL OFL). `render.mjs` fetches them once from npm (`@fontsource/*`) into `~/.cache/il-reels` and embeds them at render time. They are **not** bundled in the plugin. For browser preview, `reel.html` loads them from Google Fonts.

## Workflow

```bash
node new-reel.mjs ./reels/my-topic --title "My topic" --duration 24   # scaffold (re-run any time to refresh kit/ and assets/; reel.html is kept)
# write the concept in ./reels/my-topic/reel.html
open ./reels/my-topic/reel.html                                         # live preview: space = play/pause, scrubber, "safe zone" guides
node render.mjs ./reels/my-topic/reel.html --cover 0.5                  # MP4 + covers + sheet + onscreen.txt + report.json
node render.mjs ./reels/my-topic/reel.html --from 8 --to 12 --out /tmp/beat.mp4   # fast check of one beat
python3 ../../human-pass/scripts/humanize.py ./reels/my-topic/reel.onscreen.txt --report -o /dev/null
python3 ../../human-pass/scripts/design_tells.py ./reels/my-topic/reel.html  # AI tells (design-system/AI_TELLS.md)
node export-artifact.mjs ./reels/my-topic                              # live, shareable Artifact version (publish artifact/index.html + files.json)
```

A 30-second Reel renders in about 1.5 minutes.

## Writing a reel.html

```html
<div class="il-stage">
  <section class="il-scene il-ground-alt" id="s1"> … </section>
  <section class="il-scene" id="outro"></section>
</div>
<script src="kit/il-reel-kit.js"></script>
<script>
ILReel.run({ duration: 24, fps: 30, title: '…', family: 'handwritten', ending: 'pig' }, async (r) => {
  r.scene('#s1', 0, 6.45, { enter: 'cut', exit: 'cut' });
  r.read('#hook', 0, 6, 'hook');                       // registers copy for the reading-time / safe-zone / size lint
  r.write('#note', 1.2, 0.8);                           // handwriting ink reveal (use .il-hand / .il-hand-sm)
  r.mark('circle', '#claim', { t: 2.0, pad: 10 });      // underline | circle | strike | highlight | box | check | arrow
  r.appear('#line', 2.6, { y: 20 });
  r.outro('#outro', { t: 21.8, variant: 'pig' });       // 'pig' | 'bulb' | 'logo'; ground 'light' | 'teal'
});
</script>
```

### Primitives

| call | what it does |
|---|---|
| `r.tween(el, {t, dur, from, to, ease})` | animate `opacity x y scale rotate blur reveal revealY draw` |
| `r.set(el, t, props)` | jump to values at `t` |
| `r.fn(t0, t1, cb)` | custom per-frame motion (bobbing, counters); `cb(localTime, globalTime)` |
| `r.appear / r.vanish` | opacity + small travel in / out |
| `r.write(el, t, dur)` | left-to-right ink reveal with a soft edge |
| `r.draw(svgEl, t, dur)` | stroke drawing; groups draw their strokes in sequence |
| `r.mark(kind, el, opts)` | hand-drawn mark measured from the element: `underline circle strike highlight box check arrow` (`to`, `bend`, `seed`, `color`, `width`, `pad`) |
| `r.chat(box, {head, messages})` | thread with typing dots, staggered arrivals, auto-scroll with a soft top fade, `receipt`, `react: {kind: 'heart'\|'check', at}` (drawn, never emoji) |
| `r.scene(el, from, to, {enter, exit})` | scene in/out: `fade up zoom cut` |
| `r.camera(el, t, dur, {x, y, scale})` | move a layer (pan/zoom) |
| `r.outro(el, {t, variant, ground, cta})` | signature ending with the real 2027 logo |
| `r.read(el, from, to, label)` | register copy for the lint; mark quiet labels with `data-quiet` |

Easing: `out` (default), `in`, `inOut`, `outQuart`, `settle` (a hint of overshoot, never a bounce), `pen` (quick start, careful finish), `linear`.

### Rules the lint enforces

- **Reading time**: `0.6 s + words / 3.2` per registered element, a heuristic for short on-screen bursts. Quiet `data-quiet` labels don't count.
- **Safe zone**: registered copy stays inside x 90–990, y 250–1550 (a conservative guide; still check a real phone preview).
- **Type size**: 34 px minimum for anything the viewer must read.
- **Hook**: at least one registered element is visible at t = 0.
- **Cover crop**: anything registered with the label `'hook'` sits inside the 4:5 grid crop (y 285–1635), because the profile grid shows that crop of the cover. A hook placed at the very top of the frame gets cut in the grid (found in testing).

### Layout notes learned from testing

- Centre the content block in the safe zone. A layout that ends at y ≈ 1250 leaves the bottom third empty on a phone and looks unfinished.
- Light cyan highlights need strong opacity (`rgba(114,236,231,.85)`) to read behind dark text.
- The flying-pig PNG is 465 px wide. Keep it at 440 px or less so it never upscales.
- Scenes with opaque grounds: fade the next scene in on top and cut the previous one after the fade (`exit: 'cut'` at `next + inDur`). Crossfading both leaves a washed-out frame.
- Every `.il-scene` is its own stacking context (`isolation: isolate`). Without it, a scene's marks (z-index 5) painted over the next scene while it faded in. That bug was caught on the outro of the second test Reel.
- Chat threads fade their top edge once they scroll, so a half-visible bubble never shows a hard cut.
- Chat reactions are drawn (`react: {kind: 'heart' | 'check'}`), never emoji.

Before delivery also run `python3 ../../human-pass/scripts/design_tells.py <folder>/reel.html` (AI tells, see `design-system/AI_TELLS.md`).

Example: `../../../generated-examples/reels/context-engineering/` (study the decisions, don't copy the layout).
