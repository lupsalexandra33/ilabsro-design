# ilabsro-design

Innovation Labs design plugin prototype, synced with the native **Innovation Labs** Claude Design System. v0.3 tightens Strategy Map fidelity and removes generic catch-all `Open Threads` sections by default.

## Mental model

- **Bundled Design System** = portable source of truth for how Innovation Labs looks.
- **Native Claude Design System** = optional richer editor/runtime representation of the same rules.
- **Output skill** = what you are making.
- **Tone lens** = how the copy sounds.
- **Source material** = what the output says.

The plugin is intentionally usable by collaborators who **do not** have Alexandra's native Design System installed. Every output skill must be able to fall back to `design-system/INNOVATION_LABS_DESIGN_SYSTEM.md` and `design-system/TOKENS.css`.

## Skills

- `website-maker` — strategy hubs, calm map/route previews and connected IL web artifacts.
- `presentation-maker` — catchy, pitch-like strategy decks linked back to a deeper Hub; presentation-only playable mesh is allowed.
- `one-pager-maker` — A4/PDF strategy and partner summaries.
- `insta-post-maker` — experimental social post/carousel output.
- `formal-lens` — formal voice modifier.
- `friendly-lens` — warm, clear voice modifier.
- `jokey-lens` — restrained playful voice modifier.

## Portable design files

- `design-system/INNOVATION_LABS_DESIGN_SYSTEM.md` — full rules, format behavior, component catalog and confirmed token values.
- `design-system/TOKENS.css` — reusable Light/Night token subset extracted from the native system.
- `design-system/COMPONENT_CATALOG.md` — 17 component patterns.
- `assets/` — 2027 logo variants.

## Composition

Use **one output skill** + **zero or one tone lens** + the bundled/native Innovation Labs Design System.

Examples:

- `presentation-maker` + `friendly-lens` → founder-facing strategy deck.
- `one-pager-maker` + `formal-lens` → partner-facing one-pager.
- `website-maker` → source-rich Strategy Hub / calm Map experience.
- Add the public Humanizer skill as an optional final copy pass when useful; do not duplicate it inside this plugin.

See `docs/USAGE.md` and `docs/TEST_MATRIX.md`.
