---
name: presentation-maker
description: Turn Innovation Labs strategy or program material into a pitch-like route-aware presentation using the IL v0.4 design system and links to deeper source material.
version: 0.4.1
---

# Innovation Labs Presentation Maker

Use when the user asks for a strategy presentation, pitch-style story, live deck or guided narrative.

## Before building

1. Read `../../design-system/INNOVATION_LABS_DESIGN_SYSTEM.md`, `../../design-system/TOKENS.css` and `../../design-system/BRAND_ELEMENTS.md`.
2. Read `references/pitch-structure.md`.
3. Ground every factual claim in supplied source material.
4. If a Strategy Hub URL is supplied, plan a clear final/recurring path into it.
5. If `brand-elements` is active, use it only for accent, cover/transition ground and at most one official decorative element per view.

## Goal

The presentation is the **catchy front door**, not a compressed copy of the Hub.

It should make the audience want to go deeper, then link to the Strategy Hub for full evidence and detail.

## Route-first behavior

For strategy/program material with a meaningful journey, timeline or set of stages, **route-first is the preferred v0.4 pattern**.

- Slide 1 establishes the route/journey rather than starting with a dense title page.
- The route is serpentine/full-width on desktop and phone landscape.
- Portrait phone turns the same route into a vertical journey.
- Later slides carry route/stop context so the audience knows where they are.
- Stops can jump into their chapters when the runtime supports it.
- Do not invent route stops only to satisfy the pattern; if the source is not naturally sequential, use a conventional pitch narrative instead.

If a Hub and deck are explicitly being built as one coordinated family and a shared route model is supplied/approved, reuse it. Otherwise a deck may use presentation-specific narrative compression as long as it stays semantically aligned with the source.

## Native format contract

- Default to Night for projected/phone-followed decks; use Light for print/PDF delivery.
- Purple is the default accent; yellow is optional. Accent changes semantic highlight color, not structure.
- One story beat per slide: kicker → strong title → at most one main content pattern.
- Phone-first decks keep progress/route context and Back/Next controls in the thumb zone.
- Detail belongs behind taps rather than being shrunk onto the slide.
- Each slide may end with one `Deeper` link into the Strategy Hub.
- If yellow accent is active, never use white labels on yellow fills; use `ax-on`.

## Default story shape

A route-first strategy sequence often looks like:
1. route / journey overview;
2. why the journey starts here;
3. tension / evidence;
4. the core idea or bet;
5. what changes in practice;
6. people / delivery / program mechanics;
7. calendar or next milestones;
8. ending / invitation;
9. go deeper → Strategy Hub.

Length follows the story; do not force an exact count if route stops or source structure require more/fewer slides.

## “Pitchy” means

- faster narrative progression;
- fewer words;
- stronger visual hierarchy;
- memorable phrasing supported by evidence;
- intentional reveals;
- clear stakes and change;
- a finish that points to the Hub.

It does **not** mean exaggerating or inventing certainty.

## Personal insight blocks

The presentation may become more personal/catchy with insights from Flavia, Daniel, Ana or other team members.

Never invent what a real person thinks. If their insight/quote is not supplied, create a labeled placeholder such as `TEAM INSIGHT NEEDED` rather than fabricating it.

## Playable network treatment

A playful interactive network is allowed as a **presentation-only** expressive treatment when it supports the story and remains behind the content.

Good uses:
- cover/transition moments;
- community, relationships, connected systems;
- moments where interaction adds delight.

Rules:
- selective, not every slide;
- teal nodes/lines with semantic-accent tap/focus states;
- vignette/calm zones around text;
- pause/disable under `prefers-reduced-motion`;
- never treat it as the strategy route;
- never generalize it to Hub maps, one-pagers or social.

Static brand/template mesh grounds from `BRAND_ELEMENTS.md` are a separate thing and may be used as cover/transition art when appropriate.

## Lead the room

`Lead the room` is an optional collaborative presenter feature: when supported by the Artifact room runtime, one presenter can broadcast the current slide so other open clients follow automatically.

Do **not** expose a visible `Lead` / `Leading` control by default. Include it only when the user explicitly asks for presenter/follower synchronization or when the artifact is intentionally demonstrating that capability.

If included:
- hide/disable the control when room capability is unavailable;
- the deck must still navigate normally on every device;
- show follower count/status only while the feature is active;
- never claim cross-device sync if the runtime does not provide it.

## Fluid layout contract

- Use one coherent fluid size unit or scale for type, spacing and radii.
- Landscape follows the smaller viewport dimension; portrait follows width and may scroll vertically.
- Keep left and right spacing balanced.
- Controls never cover content; move them to a bottom row on portrait phones.
- Long labels wrap; do not squeeze text into narrow fixed columns.
- Avoid `!important` patch stacks.
- Check 1440×900, 844×390 and 390×844.

## Link to the Hub

If a Hub URL is known:
- final slide includes a prominent `Open Strategy Hub` / `Go deeper` action;
- earlier deep-dive references may link to specific Hub sections where useful.

Do not reuse a historical artifact URL from source/reference material as the final destination unless the user confirms it is the current URL.

## References

- `references/pitch-structure.md`
- `examples/index.html` as the current v0.4 route-first reference implementation, including portrait/landscape adaptation, accent switching and optional `Lead the room` behavior.

## Bundled examples

When a concrete presentation reference would materially help, consult `../../docs/EXAMPLES.md` and at most 1–2 relevant examples under `../../generated-examples/presentation/`.

Use bundled examples to understand:

- the relationship between request, constraints and result;
- the expected quality bar;
- presentation pacing and slide-level hierarchy;
- how different narrative structures can remain recognizably Innovation Labs.

Examples are references, not templates.

Do not mechanically copy their slide sequence, wording, facts, URLs, route structure or composition into a new deck.

In particular, do not assume every Innovation Labs presentation should use route-first storytelling. Use a route only when the source genuinely supports a meaningful journey, sequence or set of stages.

Current source material, the current request and the current skill rules always take priority.
