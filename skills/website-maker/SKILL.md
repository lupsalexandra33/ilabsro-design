---
name: website-maker
description: Build Innovation Labs Strategy Hubs, route/map previews and connected web artifacts from source material using the portable IL v0.4 design system.
version: 0.4.0
---

# Innovation Labs Website Maker

Use for Innovation Labs websites, interactive strategy references, Strategy Hubs and Map/route previews.

## Before building

1. Read `../../design-system/INNOVATION_LABS_DESIGN_SYSTEM.md`, `../../design-system/TOKENS.css` and `../../design-system/BRAND_ELEMENTS.md` as the portable visual contract.
2. If the native **Innovation Labs** Design System is available, use it as the editor/runtime representation of the same rules; it must not override the bundled source with contradictory styling.
3. Ground all copy in supplied source material. Do not invent research, dates, quotes, people or outcomes.
4. Read `references/website-patterns.md`.
5. For any Map Proposal / strategy-route output, also read `references/map-proposal-pattern.md`.
6. If `brand-elements` is active, treat it as an optional visual modifier. It may affect accent, hero/band ground and one official decorative element; it must not change the content architecture or map rules.

## Primary patterns

### Strategy Hub

Use when the audience needs non-linear exploration of a large strategy/program source.

For the **Innovation Labs 2027 Strategy Hub**, the canonical hero title is:

`Analog first. AI second.`

Treat that line as the fixed 2027 strategy slogan. Do not replace it with a paraphrase such as “Human cognition first. AI amplification second.” The supporting lede may adapt to the source, but the hero title stays exact.

A Strategy Hub is **source-rich, not source-complete**. Curate before laying out:
- surface the thesis, route and highest-value decisions first;
- do not mirror every master-note section, statistic or caveat on the landing view;
- keep the hero lede to roughly 1–2 short sentences;
- keep the first overview to roughly 3–4 strategic pillars or a small set of decisive stats, not both at maximum density;
- move evidence and secondary mechanics into the relevant deep-dive section or progressive disclosure;
- if a section becomes a wall of cards, collapse, combine or remove lower-priority material.

Default structure:
- persistent IL shell and obvious top navigation;
- one strong landing hero that frames the thesis;
- optional compact route/mini-map when a route is central to the strategy;
- source-backed deep dives;
- digestible sections rather than walls of text;
- selective stats, diagrams, quotes and real photography;
- global Light/Night theme when appropriate;
- purple accent by default; yellow only when explicitly requested/selected.

### Map Proposal / route preview

Use when the strategy benefits from being understood as a connected journey.

Rules:
- route and stops are the hero;
- on desktop, prefer one wide gently serpentine left-to-right route with sequential numbered stop discs and compact labels alternating above/below;
- preserve an approved/source stop order and route model when one is available;
- if the Hub contains both a full map and mini-map, generate both from the same ordered stop data/model;
- map background stays calm and readable;
- **never** place decorative template mesh, radial brand mesh or a playable network behind the route;
- sparse large contour/wave cues are allowed;
- stop detail opens on demand without rearranging route geometry;
- current/selected stop uses the semantic accent (`ax`), purple by default or yellow when the entire artifact uses yellow accent;
- mobile becomes the same journey vertically, with detail in a bottom sheet.

### Connected strategy experience

When a Map Proposal and Hub belong to the same artifact:
- Map acts as preview/gateway to the Hub;
- the Hub keeps Map/Route in navigation;
- compact and full maps share stop names/order and recognizable route silhouette;
- theme/accent remain coherent.

Across **separate** outputs (for example a Hub and a presentation), use one identical shared route only when the user supplies/approves that shared model or explicitly requests a coordinated artifact family. Do not force unrelated narrative compression to use identical stop labels.

## v0.4 branded fields

Web reading sections remain flat. `brand-elements` may introduce:
- `grad-brand` / `grad-band` in nav or hero;
- one approved pale template ground in an isolated hero/campaign band;
- one official SVG brand element placed away from reading content.

Do not use branded decorative grounds as the default page background. Do not generalize them to the route map.

## Presentation network exception

Do not copy the presentation's playable network into web/map backgrounds. The interactive network belongs to `presentation-maker` when it supports the story. Static official brand elements may appear in a web hero only when selected intentionally.

## Fluid layout contract

Start with one responsive layer rather than breakpoint patches.

- One shared content container/gutter aligns header, rail and sections.
- Use fluid `clamp()` sizing or one coherent size unit; avoid abrupt type/gap jumps.
- Long labels wrap rather than squeezing adjacent content.
- Do not accumulate `!important` patch layers.
- Portrait phones adapt the composition; they do not merely shrink desktop.
- Check 1440×900, 844×390 and 390×844. Nothing should scroll sideways.

## Native format contract

- Default website theme is Light; Night is optional and keeps identical structure.
- Reading grounds use `surface-page` / `surface-alt` / `surface` / `surface-tint`.
- Long pages use `Expand`; add desktop progress/mobile guide only when complexity justifies it.
- Hub navigation cards use the `Card` link pattern with a top `border-accent`, never a colored left rail.
- Route line remains calm, numbered and readable; under ~680–820px switch to a vertical journey depending on the composition.

## Content architecture guardrails

- Do **not** create a standalone section named `Open Threads`, `Open Questions`, `Loose Ends`, `What remains open`, or similar unless the user explicitly asks for it or the supplied source explicitly presents it as a public-facing section.
- Source uncertainties, caveats and unresolved items belong next to the relevant claim as `note`, `caution`, estimate labels or expandable detail.
- Never manufacture unresolved questions merely to make the Hub feel comprehensive.

## Output contract

- Preserve brand identity but adapt internal layout to information.
- Avoid generic SaaS dashboards.
- Make navigation explicit.
- Adapt layout for mobile rather than shrinking desktop.
- If a published Hub URL is provided, use it consistently for cross-links.

## References

- `references/website-patterns.md`
- `references/map-proposal-pattern.md`
- `examples/IL2027_strategy_hub.html` as the current v0.4 reference implementation: one shell, Map + Hub views, a shared full/mini-map stop model and fluid responsive behavior.
