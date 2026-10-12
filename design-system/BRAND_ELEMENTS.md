# Innovation Labs brand elements — v0.4

This file documents the portable branded grounds and official decorative SVG elements bundled with `ilabsro-design`.

They are **visual modifiers**, not content. They must never change facts, hierarchy or information architecture.

## Paths

Shared plugin assets:

- `../assets/brand-elements/` — 16 transparent SVG elements.
- `../assets/backgrounds/` — approved IL template backgrounds grouped by color family.
- `../assets/logo_primary_2027.svg` — primary logo for light/pastel grounds.
- `../assets/logo_white_2027.svg` — white logo for dark/brand grounds.
- `../assets/logo_currentcolor.svg` — currentColor variant for controlled UI use.

The showcase intentionally keeps its own copies under `showcase/assets/` so it can deploy independently.

## Accent role

Purple is the default accent. Yellow is the optional alternate accent.

Accent marks:
- AI/challenger content;
- current route step;
- what is new or planned;
- focus state;
- one human/handwritten emphasis.

Use `--ax`, `--ax-ink`, `--ax-tint`, `--ax-soft`, `--ax-on`, `--ax-deep` and `--ax-grad` rather than hard-coded purple/yellow values.

Never use white small text on yellow fills. `--ax-on` becomes dark ink for yellow.

## Branded grounds

CSS tokens provide lightweight, theme-aware grounds:
- `--grad-brand`
- `--grad-band`
- `--grad-accent`
- `--grad-surface`
- `--mesh-blue`
- `--mesh-green`
- `--mesh-yellow`
- `--mesh-purple`
- `--mesh-classic`

Exact JPG template backgrounds live in:
- `assets/backgrounds/blue/`
- `assets/backgrounds/green/`
- `assets/backgrounds/purple/`
- `assets/backgrounds/yellow/`
- `assets/backgrounds/classic/`

Available aspect/use variants include `cover`, `post`, `square`, `story`, `view`, `wide`, with some families also carrying `cover-alt`.

### Ground rule

Reading areas stay flat. Approved gradients/template grounds belong on:
- nav/hero bands;
- presentation covers and transitions;
- one-pager headers/closing bands;
- social/campaign canvases;
- occasional branded callout panels.

Do not put a decorative mesh behind a Strategy Route map or dense reading content.

## SVG element library

Bundled files:
- `bulb-glass.svg`
- `bulb-mesh.svg`
- `flask.svg`
- `frame-mesh-1.svg`
- `frame-mesh-2.svg`
- `frame-mesh-3.svg`
- `hex-gold.svg`
- `hex-gold-wide.svg`
- `hourglass-bulb.svg`
- `hourglass-bulb-soft.svg`
- `make-it-real.svg`
- `register-badge.svg`
- `register-simple.svg`
- `ring-mesh.svg`
- `star.svg`
- `star-soft.svg`

These are official decorative brand elements, not clip-art and not logos.

## Pairing guidance

Use **one major decorative element per view by default**.

Useful pairings from the refreshed showcase:
- yellow accent → `hex-gold`, `bulb-glass`, `hourglass-bulb`;
- purple accent → `star`, `flask`;
- green topics → `ring-mesh`;
- rooms/stages/framing → `frame-mesh-*`;
- execution / making → `make-it-real`;
- sign-up / registration → `register-*`.

The content meaning wins. Do not choose an element only because its color matches.

Decorative images in HTML use `alt=""` unless the image itself communicates information.

## Format boundaries

### Website / Hub
May use one branded hero/band treatment or official element when it supports the page. **Map/route grounds stay calm and mesh-free.**

### Presentation
May use branded grounds/elements on cover and transitions. The interactive/playable network is a separate presentation-only treatment; do not confuse it with static template meshes.

### One-pager
May use a brand gradient or pastel template ground in the header and an accent closing band. Body reading areas remain flat and print-safe.

### Social
Two valid families:
1. event photography: photo overlay / photo-to-teal blend / editorial crop, optionally with one small brand element;
2. campaign graphic: approved template ground + logo + one official SVG element.

### Social-only mascots
The flying pig PNGs live inside `skills/insta-post-maker/assets/brand-elements/` because they are not part of the shared 16-SVG library.
