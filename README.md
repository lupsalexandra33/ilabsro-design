# ilabsro-design

Portable Innovation Labs design plugin for Claude. v0.5 adds source-grounded content planning and reusable custom image generation on top of the existing Strategy Hub, route-first presentation, social and brand system.

## Mental model

- **Bundled Design System** = portable source of truth for how Innovation Labs looks and behaves.
- **Native Claude Design System** = optional richer editor/runtime representation of the same rules.
- **Output skill** = what you are making.
- **Tone lens** = how the copy sounds.
- **Brand elements** = optional visual modifier for accent, branded grounds and official decorative assets.
- **Source material** = what the output says.

Every output skill must work when the native Design System is unavailable by falling back to `design-system/INNOVATION_LABS_DESIGN_SYSTEM.md`, `design-system/TOKENS.css` and the bundled assets.

## Skills

- `website-maker` — Strategy Hubs, calm route/map previews and connected IL web artifacts.
- `presentation-maker` — pitch-like decks; route-first for strategy/program narratives; optional presentation-only playable network.
- `one-pager-maker` — exact one-page/A4 summaries and partner briefs.
- `insta-post-maker` — photo-led, graphic and custom-illustration social assets.
- `content-planner` — turns approved strategy, research and program material into source-grounded content opportunities and briefs.
- `brand-image-maker` — generates reusable IL visuals using hand-drawn diagrams, narrative illustrations or event-glow directions.
- `brand-elements` — optional visual modifier that selects accent, branded ground and one official IL element.
- `formal-lens` — formal voice modifier.
- `friendly-lens` — warm, clear voice modifier.
- `jokey-lens` — restrained playful voice modifier.

## Portable design files

- `design-system/INNOVATION_LABS_DESIGN_SYSTEM.md` — full v0.4 rules and format behavior.
- `design-system/TOKENS.css` — Light/Night + purple/yellow accent tokens and branded ground tokens.
- `design-system/BRAND_ELEMENTS.md` — official backgrounds, SVG elements and pairing rules.
- `design-system/COMPONENT_CATALOG.md` — reusable interaction/content patterns.
- `assets/brand-elements/` — 16 official SVG decorative elements.
- `assets/backgrounds/` — IL template backgrounds for campaign/social/PDF uses.
- `assets/logo_*.svg` — official 2027 logo variants.

## Composition

For a normal task use **one output skill** + **zero or one tone lens** + **optional `brand-elements`** + the bundled/native Innovation Labs Design System.

Examples:

- `presentation-maker` + `friendly-lens` → founder-facing route-first strategy deck.
- `presentation-maker` + `brand-elements` → route deck with an explicitly requested yellow accent or branded cover ground.
- `one-pager-maker` + `formal-lens` → partner-facing one-pager.
- `website-maker` → source-rich Strategy Hub / calm Route experience.
- `insta-post-maker` → event-photo carousel with photo-to-teal blending.
- `insta-post-maker` + `brand-elements` → campaign carousel on an approved template ground with one official SVG element.
- `content-planner` → source material → evaluated content opportunities → human selection → structured brief.
- `insta-post-maker` + `brand-image-maker` → social carousel where custom drawings or generated visuals carry part of the explanation.

The public Humanizer skill can be an optional final copy pass when useful; it is not a dependency of this plugin.

See `docs/USAGE.md` and `docs/TEST_MATRIX.md`.

## Live examples

### Design references

| Artifact | Live |
| --- | --- |
| Strategy Hub | [Open reference ↗](https://ilabsro-design-examples.vercel.app/) |
| Presentation | [Open reference ↗](https://ilabsro-design-examples-gojv.vercel.app/#1) |

### Plugin-generated outputs

| Artifact | Live |
| --- | --- |
| Strategy Hub | [Open generated example ↗](https://ilabsro-design-website.vercel.app/) |
| Presentation | [Open generated example ↗](https://ilabsro-design-presentation.vercel.app/) |

### Showcase

[Explore the plugin showcase ↗](https://ilabsro-design-showcase.vercel.app/)
