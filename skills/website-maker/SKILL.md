---
name: website-maker
description: Build Innovation Labs strategy websites, Strategy Hubs, Map previews and connected web artifacts from source material using the IL design system.
version: 0.3.0
---

# Innovation Labs Website Maker

Use for Innovation Labs websites, interactive strategy references, Strategy Hubs and Map/route previews.

## Before building

1. Read `../../design-system/INNOVATION_LABS_DESIGN_SYSTEM.md` and `../../design-system/TOKENS.css` as the portable visual contract.
2. If the native **Innovation Labs** Design System is available, use it as the editor/runtime representation of the same rules; it must not override the bundled source with contradictory styling.
3. Ground all copy in the supplied source. Do not invent research, dates, quotes, people or outcomes.
4. Read `references/website-patterns.md`.
5. For any Map Proposal / strategy-route output, also read `references/map-proposal-pattern.md`.

## Primary patterns

### Strategy Hub
Use when the audience needs non-linear exploration of a large strategy/program source.

Default structure:
- persistent IL shell and top navigation;
- one strong landing hero that frames the thesis;
- source-backed deep dives;
- digestible sections rather than walls of text;
- selective stats, diagrams, quotes and real photography;
- global light/night theme when appropriate.

### Map Proposal / route preview
Use when the strategy benefits from being understood as a connected journey.

Rules:
- route and stops are the hero;
- on desktop, prefer the IL Map Proposal composition: one wide horizontal serpentine route, sequential numbered stop discs, and compact labels alternating above/below the path;
- preserve the approved/source stop order and route model when one is available rather than inventing a different map composition;
- map background stays calm;
- no dense reactive mesh behind the map;
- sparse, large contour/wave cues are allowed;
- stop detail opens on demand without rearranging the route;
- mobile becomes the same journey vertically.

### Connected strategy experience
When both exist:
- Map Proposal acts as a preview/gateway to the Strategy Hub;
- the Hub includes Map in navigation;
- the Hub may embed a compact map preview;
- Map and Hub use one shared stop/order model;
- theme choice should remain coherent across both.

## Presentation mesh exception

Do not copy the presentation's playful mesh into the map background. The map should remain legible and calm. Interactive mesh/network treatments belong to `presentation-maker` when they support the story.

## Native format contract

- Default website theme is Light; Night is optional and keeps identical structure.
- Use flat `surface-page` / `surface` / `surface-tint` grounds. No dotted paper, radial ambience or mesh.
- The only gradient is the teal → deep-teal brand hero/nav gradient.
- Long pages use `Expand`; add desktop progress/mobile guide only beyond roughly six sections.
- Hub navigation cards use the `Card` link pattern with a top `border-accent`, never a colored left rail.
- For maps, use a 4px route line, numbered stop discs, purple only for current stop, dashed route-ahead, and surface cards for labels. Under 820px switch to the vertical `Route` + `Sheet` pattern.

## Content architecture guardrails

- Do **not** create a standalone section named `Open Threads`, `Open Questions`, `Loose Ends`, `What remains open`, or similar unless the user explicitly asks for such a section or the supplied source explicitly presents it as a public-facing section that must be preserved.
- Source uncertainties, caveats and unresolved items belong next to the relevant claim as `note`, `caution`, estimate labels, or expandable detail. Do not collect them into a generic catch-all section by default.
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
- `examples/IL2027_strategy_hub.html` when a concrete reference is useful. Treat its information architecture as reference; do not copy deprecated dotted/mesh background treatments.
