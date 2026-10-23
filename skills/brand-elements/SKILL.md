---
name: brand-elements
description: Optional Innovation Labs visual modifier that selects the semantic accent, an approved branded ground and one meaningful official IL decorative element.
version: 0.4.0
---

# Innovation Labs Brand Elements

Use this skill **with one output-maker skill** when the user wants a stronger campaign/brand treatment, asks for purple/yellow accent, names a gradient/background family, or asks to use official IL visual elements.

This is a modifier, not an output format. It must never change facts, message hierarchy, route semantics or page count.

## Read first

Read:
- `../../design-system/INNOVATION_LABS_DESIGN_SYSTEM.md`
- `../../design-system/TOKENS.css`
- `../../design-system/BRAND_ELEMENTS.md`
- `../../design-system/AI_TELLS.md` (patterns IL never ships; applies to every element choice)

Shared assets live in:
- `../../assets/brand-elements/`
- `../../assets/backgrounds/`
- `../../assets/logo_primary_2027.svg`
- `../../assets/logo_white_2027.svg`

## Decision order

Choose only what the artifact needs:

1. **Accent** — purple (default) or yellow.
2. **Ground** — flat brand field, CSS gradient/mesh token, or approved template JPG.
3. **Element** — usually zero or one official SVG with a semantic reason.

Do not force all three.

## Accent

Purple is default.

Yellow is appropriate when:
- explicitly requested;
- a campaign/reference uses the warm gold/yellow family;
- the chosen official asset/background is clearly built around that family.

The accent role marks AI/challenger, current step, what is new/planned, focus and occasional human emphasis. It is not a second brand color spread everywhere.

Never use white small text on yellow fills; use `--ax-on`.

## Ground selection

Approved CSS grounds are documented in `TOKENS.css`. Exact image backgrounds are under `../../assets/backgrounds/`.

Use branded grounds on:
- hero/nav bands;
- presentation cover/transition slides;
- one-pager header/closing band;
- campaign/social canvases;
- isolated branded panels.

Keep reading surfaces flat.

**Never put decorative mesh/template grounds behind Strategy Route maps.**

## Element selection

Official SVGs live in `../../assets/brand-elements/`.

Use one major element per view by default.

Meaning-first guidance:
- `bulb-glass`, `bulb-mesh` → ideas, experimentation, insight;
- `hourglass-bulb*` → time, countdown, transition, progress;
- `make-it-real` → making, execution, turning intent into action;
- `register-*` → signup / registration / join;
- `frame-mesh-*` → room/stage/framing moments;
- `ring-mesh` → network/community/green-topic visual;
- `star*`, `flask` → playful experimentation, often compatible with purple;
- `hex-gold*` → structured warm/yellow campaign treatment.

Pairings are guidance, not hard rules. Do not choose an asset only because its color matches.

## Format boundaries

- **website-maker:** hero/band decoration only; route/map remains calm.
- **presentation-maker:** cover/transition decoration; playable network remains a separate presentation-only behavior.
- **one-pager-maker:** header/closing treatment only, print-safe.
- **insta-post-maker:** campaign mode may use template ground + logo + one SVG; event-photo mode may use one subtle element if it supports the story.

## Accent controls

Purple/yellow is normally an internal visual choice, not an end-user feature. Choose the accent for the artifact and keep it consistent. Do not add a visible accent switch unless the user explicitly requests one or the artifact is a design-system/demo surface.

## Output contract

When used, internally decide and apply:
- `accent`: purple or yellow;
- `ground`: exact token/background family;
- `element`: exact asset filename or none.

Do not add a visible explanation of those choices unless the user asks for a design rationale.
