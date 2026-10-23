# Changelog

## 0.7.0 (2026-10-23)

Applied on top of the full repo working tree (HEAD `1c4a247` plus your uncommitted `reels-maker` work). Files not listed here are byte-identical to what you sent.

### New
- **IL Reel Kit** (`skills/reels-maker/production/`): deterministic HTML timeline with IL motion primitives (handwriting reveal, hand-drawn marks, chat thread, camera, signature outro). Includes:
  - `new-reel.mjs` (scaffold), `render.mjs` (1080×1920 H.264 MP4 + 9:16/4:5 covers + contact sheet + `onscreen.txt` + `report.json`), `export-artifact.mjs` (live, shareable Artifact version);
  - built-in lint: reading time, safe zone, minimum type size, hook at t = 0, hook inside the 4:5 grid crop.
- **`human-pass` skill**: copy check for every maker. `humanize.py` / `detect.py` / `slop.json` are adapted from Jake Schincariol's MIT `instagram-agent-skill` (license included) and extended with an IL voice block (and IL's `·` separator is kept, not converted). `design_tells.py` is new: it scans HTML/CSS/SVG for visual AI tells.
- **`design-system/AI_TELLS.md`**: the 17 patterns IL never ships, plus #18 (coloured left-border accent, already an IL rule). Referenced by every maker and by design-system principle 8.
- **`generated-examples/reels/context-engineering/`**: the first validated Reel.

### Changed
- `reels-maker` 0.6.1 → 0.7.0: production path (the kit), review steps (contact sheet + full-resolution frames), `human-pass` and `design_tells` in the gate, caption/cover/audio handoff, Reels log (`~/.claude/ilabs/reels-log.md`), Artifact delivery, Claude Motion rules (used only when the session lists a Motion type), no emoji in avatars or reactions.
- `insta-post-maker`: final copy check through `human-pass`; reads `AI_TELLS.md`.
- `website-maker`, `presentation-maker`, `one-pager-maker`, `brand-image-maker`, `brand-elements`: read `AI_TELLS.md` and run `design_tells.py` before delivery.
- `plugin.json` 0.5.1 → 0.7.0; description and keywords mention Reels / video.
- README, `docs/USAGE.md`, `docs/EXAMPLES.md`: new skills, the kit and the companion plugin `ilabsro-instagram`.

### Fixed in existing examples (found by `design_tells.py`)
- `skills/one-pager-maker/examples/IL2027_vision_onepager.html`: removed the dot-grid page background (the design system already banned it).
- `skills/website-maker/examples/index.html`: removed `backdrop-filter: blur` on the mini map (glassmorphism); removed coloured left-border stripes on quote/highlight/summary boxes and research blocks; the external link arrow `→` became `↗`, and the internal "Open in Hub: …" link no longer carries an arrow.

### Bugs found while testing the kit (fixed)
- A scene's marks painted over the next scene during its fade-in. Every scene now gets `isolation: isolate`.
- `<br>` merged words in the text export. Quiet labels (`data-quiet`) inflated the reading-time count.
- Chat scroll cut bubbles with a hard edge. The chat now fades its top edge once the thread scrolls.
- The hook was cut by the 4:5 grid crop. A new `cover-crop` lint check catches it.

### Repo scripts (minimal, required by the changes above)
- `scripts/validate_plugin.py`: expected version 0.5.1 → 0.7.0 (check and OK message); `human-pass` added to the required skills.
- `scripts/build_plugin_zip.py`: `EXPECTED_PLUGIN_VERSION` 0.5.1 → 0.7.0.
- Your uncommitted edits already in these two files (the `reels-maker` checks) are untouched.

## How to validate

```bash
python3 scripts/validate_plugin.py                       # expect OK v0.7.0, 12 skills
python3 scripts/build_plugin_zip.py --output /tmp/ilabsro-design-v0.7.0.zip
git status && git diff                                    # every change, against your last commit
# AI tells across the shipped examples (expect: clean)
python3 skills/human-pass/scripts/design_tells.py generated-examples skills/*/examples
# render the example Reel (needs Node 18+, Playwright/Chromium, ffmpeg); expect FORMAT ok, LINT clean
node skills/reels-maker/production/render.mjs generated-examples/reels/context-engineering/reel.html --out /tmp/ce.mp4
# copy check on its on-screen text (expect 0 artefacts removed; the only flag is "uniform sentence length",
# which is expected for short Reel lines, see skills/human-pass/SKILL.md)
python3 skills/human-pass/scripts/humanize.py generated-examples/reels/context-engineering/onscreen.txt --report -o /dev/null
```

Then, in Claude: ask for a Reel from an approved IL source and check that it follows `reels-maker` end to end (scaffold → render → frames reviewed → `human-pass` → `design_tells` → MP4 + cover + caption + Artifact).
