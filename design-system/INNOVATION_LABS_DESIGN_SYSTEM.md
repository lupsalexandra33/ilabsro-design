# Innovation Labs Design System — portable source of truth

This bundled specification is the **portable source of truth** for the `ilabsro-design` plugin. It mirrors the native **Innovation Labs** Design System created in Claude Design and synchronized with the refreshed v0.4 Hub/deck/showcase on 2026-10-12 so the plugin still works for collaborators who do not have that native Design System installed in their account.

When the native Innovation Labs Design System is available, use it as the visual editor/runtime representation of these same rules. If it is unavailable, follow this file, `TOKENS.css` and `BRAND_ELEMENTS.md` directly.

Innovation Labs is editorial, modern and human: energetic but controlled, experimental without looking like a tech demo, playful in small moments and never childish. One identity runs across websites, presentations, one-pagers and social assets: teal and deep teal, bold Poppins headlines, mono labels, medium-rounded cards, flat reading surfaces and controlled branded grounds. Color and hierarchy do the work; gradients, template meshes and official illustration elements are accents rather than wallpaper.

The refreshed Strategy Hub and route-first presentation are reference implementations, not templates. Take their decisions, not their layouts. Their narrative stop lists may differ; require one identical cross-format route only when a shared route model is supplied/approved or a coordinated artifact family is explicitly requested.

## Principles

1. **Flat reading surfaces, branded fields at the edges.** Body reading areas stay on `surface-page`, `surface`, `surface-alt` or `surface-tint`. Approved gradients/template grounds may appear on navs, heroes, covers, transitions, closing bands and social canvases. No dotted grids or decorative micro-lines behind reading content; Strategy Route maps remain mesh-free.
2. **If a number is the message, the number is the visual.** Set it in `stat-number`, in `teal`, with one line of meaning and a source in `meta`.
3. **One statement per screen.** A slide, a hero and a social card each carry one headline. Everything else is supporting detail, cards, or tap-to-open.
4. **Editorial density.** Airy heroes, balanced modular deep-dives, denser only where people work with data. Break long text into intro, takeaways, cards, stats, quotes and expandable detail.
5. **Playful, in small doses.** One handwritten `hand` note, one arrow, one official brand element or one interactive flourish is usually enough. Do not pile motifs.
6. **Theme and accent change mood, never structure.** Light/Night and purple/yellow accent share the same layout, hierarchy and information.
7. **Style information, never manufacture it.** Never invent figures, quotes, research findings or names. Mark estimates and plans as such ("about", dashed marks, `caution`).
8. **Never look AI-generated.** The patterns in `AI_TELLS.md` (generic icon tiles, emoji, glassmorphism, em dashes, default AI fonts, three-card rows, bento grids, fake terminals, "it's not X, it's Y", placeholder demos, purple-on-black, glow orbs, dot grids, sparkles, arrow-nudge CTAs, big hover motion, rainbow color) are out in every format. This file's own specified versions (mesh grounds, 1–3px lift, semantic purple, route stops) are the only exceptions.

## Voice and content

- Plain, confident sentences. Short. No hype words, no exclamation marks, no emoji.
- Headlines state the point, often in two beats: "The program works. *Teams told us why.*" The second beat goes in `teal` (`teal-ink` under 24px) or, for AI/challenger/current-step statements, the semantic accent (`ax-ink`).
- Kickers and labels are mono, uppercase, three words or fewer: `THE EVIDENCE`, `WHAT WORKED`, `INNOVATION LABS 2027`.
- Sentence case everywhere else. "Open the strategy hub", not "Open The Strategy Hub".
- Say what evidence is. Caveats go in `note` under the claim, not in a footnote page.
- Use "we" for Innovation Labs and "founders" or "teams" for participants.
- Calls to action name the destination: "Go deeper · The calendar", "Open the strategy hub".

## Logo

- Use the 2027 lockup only, from the bundled Logos assets.
- `il-logo-2027-primary` uses ink `#2B6363` on `surface`, `surface-page` and `surface-tint`.
- `il-logo-2027-white` is used on `teal`, `teal-deep`, `surface-ink` and every Night ground.
- Never redraw, outline or stretch the logo. On photography, place it only where contrast is controlled by a calm overlay/field; otherwise use a separate solid/gradient area.
- Height: 24px in a web nav (22px under 520px), 28–40px on slides and one-pagers, at least 6% of the short side on social.
- Clear space: the height of the lightbulb icon on every side.

## Color

The palette is teal-led. Weight it roughly 60% grounds (`surface-page`, `surface`, `surface-tint`), 30% teal family (`teal`, `teal-deep`, `teal-ink`), 10% everything else.

- **Brand.** `teal` is the brand fill: hero fields, stat numerals, active markers, routes, the focus series of a chart. `teal-deep` is the solid dark brand fill and the gradient end. Teal text below 24px is always `teal-ink`, because `teal` on white is 3.56:1.
- **Accent is a role, not a second brand.** Purple is the default accent; yellow is an approved alternate. Use `ax`, `ax-ink`, `ax-tint`, `ax-soft`, `ax-on`, `ax-deep` and `ax-grad` for AI/challenger, current step, plans, focus and selective human emphasis. Change the accent without changing structure. Accent selection is normally a **design-time choice**, not a user-facing control: do not add a visible purple/yellow switch unless the user explicitly asks for it or the artifact is demonstrating the design system. Never hard-code white text on yellow fills; `ax-on` is dark there.
- **Surfaces.** On white, cards go `surface-tint`; on `surface-tint`, cards go `surface`. `surface-alt` provides subtle page alternation. `surface-ink` is for footers, dark panels and tooltips.
- **Text.** `ink` for headings, `ink-muted` for body, `ink-subtle` for notes and sources. On brand fills, `on-brand`.
- **Actions.** Primary buttons fill with `action` and label in `on-action`. Plain `teal` fills take text only at 24px+ or bold 19px+ because white on the Light teal is 3.56:1.
- **Status.** Use only when meaning needs it: `positive`, `caution`, `issue`, each on its `-soft` ground and always with a word or icon. No traffic-light brights.
- **Lines.** `line` for card borders, `line-soft` for hairlines, `line-control` for controls that must be seen.

Approved gradients are tokens: `grad-brand`, `grad-band`, `grad-accent` and `grad-surface`, plus the branded mesh/template grounds documented in `BRAND_ELEMENTS.md`. Use them on bands/covers/campaign grounds, not behind dense reading. Keep lead copy large and short on brand gradients.

### Confirmed v0.4 color roles

Canonical values live in `TOKENS.css`. Key roles:

| Role | Light/default | Night |
|---|---|---|
| `teal` | `#0095AC` | `#2BC4DB` |
| `teal-deep` | `#016462` | `#016462` |
| `teal-ink` | `#016462` | `#72ECE7` |
| `surface-page` | `#FFFFFF` | `#061B1B` |
| `surface-alt` | `#F4FBFB` | `#0A2928` |
| `surface` | `#FFFFFF` | `#0D3A39` |
| `surface-tint` | `#EAF7F7` | `#0F4443` |
| `ink` | `#10201F` | `#FFFFFF` |
| `ink-muted` | `#3C5052` | `#B9CECE` |
| `action` | `#007A8C` | `#1AB7BE` |
| `ax` purple | `#954BBC` | `#C48BEA` |
| `ax-ink` purple | `#6B2E8C` | `#D2A8EE` |
| `ax` yellow | `#FBBF45` | `#FBBF45` |
| `ax-ink` yellow | `#7A4B00` | `#F6D27A` |
| `ax-on` yellow | `#10201F` | `#2A1B00` |

Backward-compatible `purple*` aliases remain, but new work should prefer `ax*`.

## Typography

- **Display and body: Poppins.** Headlines 700 (`display-hero`, `display-page`, `slide-title`, `headline`, `title`), numerals 800 (`stat-number`), reading text 400 (`lead`, `body`, `body-s`, `note`), UI 600 (`ui`).
- **Labels: IBM Plex Mono** (`label`, `kicker`, `meta`): uppercase, tracked, never longer than a line. Never set paragraphs in mono.
- **Hand: Caveat** (`hand`) for one human aside. Never a headline, never body text.
- Headlines use `text-wrap: balance`, tight tracking (-0.01 to -0.03em) and max 900px measure. Body measure 60–78ch.
- Fonts load from Google Fonts: Poppins 400–800, IBM Plex Mono 500–700, Caveat 700.

### Confirmed type tokens

| Token | Font | Size |
|---|---|---:|
| `display-hero` | Poppins | 81px max; clamp 40.5–81px on web |
| `display-page` | Poppins | 67px max; clamp 33.4–67px on web |
| `slide-title` | Poppins | 60px |
| `headline` | Poppins | 45.8px max; clamp 28.2–45.8px on web |
| `stat-number` | Poppins | 56.3px max; clamp 38.7–56.3px on web |
| `title` | Poppins | 19.4px |
| `lead` | Poppins | 19.4px max; clamp 15.8–19.4px on web |
| `body` | Poppins | 15px |
| `body-s` | Poppins | 14.1px |
| `ui` | Poppins | 13.2px |
| `note` | Poppins | 12.3px |
| `label` | IBM Plex Mono | 11.4px |
| `kicker` | IBM Plex Mono | 12px |
| `meta` | IBM Plex Mono | 11px |
| `hand` | Caveat | 38.7px |

## Spacing and layout

- Content width `content-max` (1180px). Use one shared container/gutter for header, section rail and body so left/right edges align.
- Sections breathe: `space-88` top and bottom (60px under 620px). Sub-sections start `space-64` below the previous block.
- Card grids gap `space-18` on websites, `space-12` in presentations. Card padding `space-26` on websites, `space-16` in presentations and dense UI.
- Grids: 4 → 2 → 1 columns at 900px and 620px. Split layouts are 1 : 1.2 with a `space-48` gap and stack under 900px.
- Adapt, don't shrink: tabs become scrollable chip rows, side panels become bottom sheets, maps become a vertical journey, comparisons stack.

### Confirmed spacing tokens

`space-4: 4px`, `space-8: 8px`, `space-12: 12px`, `space-16: 16px`, `space-18: 18px`, `space-22: 22px`, `space-26: 26px`, `space-40: 40px`, `space-48: 48px`, `space-64: 64px`, `space-88: 88px`.

### Confirmed layout tokens

- `content-max: 1180px`
- `text-max: 780px`
- `slide-max: 760px`
- `nav-height: 58px`

## Fluid layout

New web/deck outputs should start from one coherent responsive layer rather than accumulating breakpoint patches.

- Derive type, gaps, padding and radii from one fluid scale/unit where practical.
- Landscape layouts scale from the smaller viewport dimension; portrait layouts follow width and may scroll vertically.
- Keep one shared page container/gutter across header, rails and content.
- Let long labels wrap; do not squeeze content columns to preserve a rigid desktop composition.
- Controls must never cover text. Move deck controls to a bottom thumb row on portrait phones.
- Avoid `!important` patch stacks and duplicate override layers. Rewrite the governing rule instead.
- Check at minimum 1440×900, 844×390 and 390×844. Nothing should scroll sideways.

## Corner radius, borders and shadows

### Radius

- `radius-xs: 4px`
- `radius-sm: 8px`
- `radius-md: 12px`
- `radius-row: 14px`
- `radius-lg: 18px`
- `radius-panel: 22px`
- `radius-xl: 24px`
- `radius-pill: 999px`

### Borders

- `border-card: 1px`
- `border-accent: 5px`
- `border-focus: 3px`

### Shadow geometry confirmed in the native system

- `shadow-hover`: `0 10px 28px`, restrained teal/ink in Light / 40% black in Night
- `shadow-nav`: `0 2px 14px`, 25% Light / 45% Night
- `shadow-raised`: `0 14px 40px`, restrained teal/ink in Light / 45% black in Night
- `shadow-sheet`: `0 -14px 40px`, 28% Light / 50% Night

Use restrained ink/teal-derived shadow color; do not introduce decorative glow. The screenshots confirmed geometry and opacity but did not expose a separate named shadow-color token.

## Surfaces and cards

- Cards: `surface`, 1px `line` border, roomy medium rounding (`radius-lg` / `radius-panel` depending on density). No drop shadow at rest.
- Clickable cards lift 3px with `shadow-hover` on hover. Hub navigation cards carry a `border-accent` (5px) top edge in `teal`, `teal-deep` or the semantic accent; that top edge is the only accent stripe allowed. Never a colored left border.
- AI/current/new cards: `ax-tint` with an `ax` border, titles in `ax-ink`.
- Brand panels: `teal-deep` or `surface-ink`, `radius-panel`, `on-brand` text, `lilac` bullets.
- Avoid heavy floating-card dashboards: no stacked shadows, no glass panels over busy backgrounds.

## Buttons and links

- Primary: `action` fill, `on-action` label, pill (`radius-pill`), `ui` text, at least 44px tall. One primary per view.
- Secondary: `surface` with `line-control` border and `teal-ink` label; `action-soft` wash on hover.
- On brand grounds: white fill with `teal-deep` label or the outline ghost.
- Presentations use `radius-sm` (8px) buttons pinned to the thumb zone.
- "Go deeper" links are `action-soft` pills with a ↗ arrow, never a bare underline.
- Inline links: `teal-ink`, underlined with a 3px offset, weight 600.

## Navigation

Navigation is obvious, not clever.

- **Top nav:** a sticky teal gradient band (`nav-height`, `shadow-nav`) with the white logo and pill links; the current page is a white pill with `teal-deep` text. Over ~8 links, collapse to a "Menu" pill opening a white panel of buttons under 1060px.
- **Section nav:** a sticky row of `surface` chips under the page header, scrollable sideways on small screens.
- **Segmented control:** for switching views of the same data (Year / Month, Day / Night).
- **Breadcrumbs:** on inner pages, in `note` size, white on the header band.
- Floating helpers only on long or complex pages. A phone deck gets segmented progress on top and Back / Next at the bottom.

## Data visualization

- Lead with the takeaway: a headline that states it, then the chart. If one number is the story, show the number, not a chart.
- Color the point, grey the rest: focus in `viz-1`, comparison in `viz-2`, context in `viz-context`, plans/AI in `viz-ai` with a dashed outline.
- Label values directly on bars and line ends; skip legends when there are three series or fewer.
- Mark estimates: dashed outlines, "about" in the label, a `note` under the chart.
- Every chart carries a source in `meta` under it.
- Bars get `radius-md` tops and square bases. No 3D, no pie charts over four slices, no gradients inside marks.

## Maps

- Calm, readable and route-focused. Innovation Labs strategy maps are journey maps, not geographic maps unless geography is explicitly required. Ground is plain `surface-tint` (Light) or `surface-page` (Night), with at most a few large, faint contour/wave curves.
- No mesh, no animated aurora, no particle network, dotted grid or decorative micro-lines behind a map.
- **Desktop Strategy Route:** one wide horizontal, gently serpentine 4px `route` line flowing left-to-right; 8–10 sequential numbered stops sit on the path; compact `surface` label cards alternate above and below the route. Keep generous negative space and avoid dashboard/card-grid compositions.
- Stops are numbered `teal-deep` discs with a white ring; the first/current stop may use a larger halo; the meaningful current/selected stop uses the semantic accent (`ax`); upcoming stops are outlined and route ahead may be dashed `line-control`.
- In Night, a restrained glow is allowed only on the route/stops. No ambient background glow.
- Selecting a stop reveals detail without changing the route geometry. Current state uses the semantic accent; purple is default, yellow is allowed when the artifact explicitly uses the yellow accent.
- A Hub mini-map uses the same stop names/order and recognizable route silhouette as the full Map Proposal, simplified for the smaller space.
- Under 820px the same map becomes a vertical journey (`Route`), and stop detail opens in a bottom sheet (`Sheet`).

## Imagery and icons

- Diagrams and flows that explain a relationship come first; then real photography of people, events and community, used selectively.
- Photos are real and unstaged where possible, full color, cropped intentionally around people/emotion. No stock handshakes and no AI-generated people.
- Official decorative SVGs in `assets/brand-elements/` are allowed where `BRAND_ELEMENTS.md` permits them. Use the supplied asset rather than approximating it with generic clip-art.
- Icons remain functional line icons at 1.75–2px stroke in `teal-ink` or `ink`, 20–24px.
- Hand-drawn arrows, circles and underlines are welcome where they point at something, usually one per screen.

## Motion

Subtle but alive.

- Fades and short slides: 150–350ms, `cubic-bezier(.3,.1,.2,1)` for slide changes, ease for the rest.
- Hover lift 1–3px; tap-to-open rotates the "+" 45° and grows the panel.
- Route and stop reveals only when they tell the story.
- Static decorative grounds do not need motion. The presentation-only playable network is the one deliberate exception when interaction supports the story. Respect `prefers-reduced-motion`: disable/pause autoplay and reduce transitions.

## Light and Night

- **Light** is the default for websites, one-pagers and most social: white/pale-teal reading surfaces, teal actions and restrained shadows. Social may still be teal-led or use approved template grounds.
- **Night** is for presentations, maps and screens in dark rooms: `surface-page` (`#061B1B`) near-black teal, never pure black; white headings, pale `ink-muted` text, turquoise actions and routes.
- Glow is allowed in Night only for focus, a route or an interaction, never as ambience.
- Both themes share token names; build once and switch `data-theme="light"` / `data-theme="night"`. Accent switches independently with `data-accent="purple"` / `data-accent="yellow"`.

## Content architecture

- Do not create generic catch-all sections such as `Open Threads`, `Open Questions` or `Loose Ends` by default. Only use one when explicitly requested or when the source itself defines it as a public-facing section.
- Keep caveats, estimates and unresolved evidence beside the claim they qualify using `note`, `caution` or expandable detail.

## Accessibility

- Text pairs named in each token's usage hold 4.5:1 in both themes; marks, control borders and focus rings hold 3:1.
- Focus: 3px `focus-ring` outline with a 2px offset; on teal grounds use `focus-ring-on-brand`.
- Touch targets at least 44px. Status is never color alone.
- Do not use white small-label text on Light `teal`; use `action` for primary buttons or dark text where appropriate.

# Component catalog

The native Design System contains 17 reusable component patterns. The plugin should reproduce their behavior using ordinary HTML/CSS/JS when native components are unavailable.

1. `BarChart` — editorial bar chart with direct labels, takeaway first, estimates dashed.
2. `Button` — primary, secondary, on-brand, disabled and presentation Back/Next variants.
3. `Card` — standard, filled, AI, and link/navigation variants.
4. `Chip` — categories, status, AI, estimates and identity tags.
5. `DeckNav` — segmented deck progress, chapter kicker, Back/Next.
6. `Deeper` — “Go deeper” pill linking to a Hub destination.
7. `Expand` — compact accordion/tap-to-open detail.
8. `Label` — mono label/kicker/meta plus optional one-off handwritten annotation.
9. `Panel` — dark/brand panel for contrast and limits/challenger content.
10. `Route` — mobile vertical route/journey.
11. `SectionNav` — local sticky chip navigation.
12. `Segmented` — switch between equivalent views such as Year/Month or Day/Night.
13. `Sheet` — mobile bottom sheet for detail.
14. `Stat` — number-first evidence block.
15. `Steps` — ordered process with optional semantic-accent AI/current step.
16. `Timeline` — dated sequence with clear confirmed vs estimated states.
17. `TopNav` — IL logo, major sections, active pill, responsive collapse.

# Format rules

The identity stays the same everywhere: teal-led palette, Poppins headlines, mono labels, medium-rounded cards, one statement per view. What changes per format is density, theme and how much the page moves.

## Websites and hubs

- Theme: Light by default; a Night toggle is optional and keeps the same structure.
- Structure: teal gradient top nav → page header band (`display-page`, `lead`, breadcrumbs) → sticky section chips → sections alternating `surface-page`, `surface` and `surface-tint` → `surface-ink` footer.
- Hub home: a grid of navigation cards (`Card`, link variant) with a `border-accent` top edge.
- Long pages: expandable detail (`Expand`) instead of walls of text; a progress rail on desktop and a guide bar on mobile only past ~6 sections.
- Reading sections stay flat. Approved brand/template grounds may appear on the nav/hero or an isolated campaign band when useful. Never put decorative mesh behind the route map or dense reading content.
- Maps: route first, geography second. Full map and mini-map inside the same Hub must be generated from one shared ordered stop model.

## Presentations

- Theme: Night by default for projected or phone-followed decks; Light for decks that will be printed or sent as PDF. Purple accent is default; yellow is optional.
- For strategy/program material with a meaningful sequence, prefer **route-first**: slide one establishes the route/journey; later slides retain stop/chapter context. On portrait phones the route becomes a vertical journey; landscape shows the full route.
- One story beat per slide: `kicker` → `slide-title` (two-beat headline, second beat in `teal` or `ax-ink` when semantically appropriate) → at most one main content pattern.
- Phone-first decks: segmented progress bar and chapter name on top (`kicker` style), Back / Next in the thumb zone, `slide-max` content column, tap-to-open "+" detail on cards.
- Detail lives behind taps, not on the slide. Each slide may end with one "Go deeper" pill to the Hub page. `Lead the room` may be offered only as an Artifact-room enhancement; without room capability the deck must still work normally.
- **Presentation-only treatment: the playable network.** A springy network of nodes and lines behind the slides may be used when it supports the story (connection, community, the cohort). Nodes use `teal` at 55% and lines at ~26% opacity; touch glow is pale cyan, tap ripples use the semantic accent (`ax`); vignette toward the edges so text stays on calm ground; keep it behind content and never under body text at full strength; pause it under `prefers-reduced-motion`. It never appears on websites, one-pagers, maps or social.
- Stats in presentations may use the `hand` face for the numeral when the slide is about people, not data.

## One-pagers (A4, PDF)

- Theme: Light. Print-safe: no glows, no transparency over photos.
- Grid: 12 columns, 15mm margins, one `display-page`-scale headline (36–44pt), one `lead` paragraph, then 3–6 modular blocks.
- Header: a solid/brand-gradient band with the white logo, or an approved pale template ground with the primary logo. Body remains flat/readable. A closing band may use `grad-accent`; yellow uses dark `ax-on` text. Footer: source notes in `note` / `meta` and a URL.
- Body text 9.5–10.5pt Poppins, labels 7.5–8pt IBM Plex Mono. Stat numerals 28–40pt in `teal`.
- Cards use `surface-tint` fills instead of borders, so they survive printing.
- Two pages maximum. If it doesn't fit, move it to the Hub and link.

## Social assets

- Sizes: 1080×1080 (square), 1080×1350 (portrait), 1080×1920 (story), 1200×627 (link card).
- One message per asset. Keep canvas copy concise; use large Poppins, mono micro-kickers and at most one Caveat emphasis.
- Two valid visual families:
  1. **Event/photo-led:** full or near-full real event photography with text overlay; photo-to-teal fade/blend; or teal-led editorial crop. Do not default to a hard photo rectangle plus a separate color block. Protect faces and emotional focal points.
  2. **Campaign/graphic:** an approved template ground from `assets/backgrounds/` or CSS brand ground, logo at a corner, and usually one official SVG element from `assets/brand-elements/`.
- A carousel may vary composition from frame to frame, but should keep one coherent palette, accent, type rhythm and story.
- Static brand mesh/template terrain is allowed in social. It is not the presentation playable network and must not be generalized to website/map backgrounds.
- Social-only flying-pig mascots may be used from `skills/insta-post-maker/assets/brand-elements/` when the tone/message earns them.
- Motion, when explicitly requested, should be short/simple and respect reduced-motion; do not promise a video export format the runtime does not support.

## Quick matrix

| Format | Default theme | Density | Motion | Mesh |
|---|---|---|---|---|
| Website / hub | Light | Balanced | Hover, reveals | Branded bands only; never behind map |
| Map | Light or Night | Calm | Route reveal | Never |
| Presentation | Night | One beat per slide | Slide transitions | Static grounds + selective playable network |
| One-pager | Light | Modular | None | Header/closing brand ground only |
| Social | Light or Night | One message | Short loops only | Static brand/template mesh allowed |

## Source discipline

- Source material is authoritative.
- Never invent figures, quotes, research findings, names or personal insights.
- Distinguish source fact from interpretation.
- If personal insights from Flavia, Daniel, Ana or anyone else are desired, require actual notes/quotes supplied by the user.
- Use the Design System to style information, not to manufacture information.
