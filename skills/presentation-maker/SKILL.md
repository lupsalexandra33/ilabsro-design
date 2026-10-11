---
name: presentation-maker
description: Turn Innovation Labs strategy or program material into a catchy, pitch-like presentation that uses IL design and links audiences to deeper source material.
version: 0.2.0
---

# Innovation Labs Presentation Maker

Use when the user asks for a strategy presentation, pitch-style story, live deck or guided narrative.

## Before building

1. Read `../../design-system/INNOVATION_LABS_DESIGN_SYSTEM.md` and `../../design-system/TOKENS.css`. If the native **Innovation Labs** Design System is available, use it as a matching runtime representation, not as a separate source of rules.
2. Read `references/pitch-structure.md`.
3. Ground every factual claim in supplied source material.
4. If a Strategy Hub URL is supplied, plan a clear final/recurring path into it.

## Goal

The presentation is the **catchy front door**, not a compressed copy of the Hub.

It should make the audience want to go deeper, then link to the Strategy Hub for full evidence and detail.

## Native format contract

- Default to Night for projected/phone-followed decks; use Light for print/PDF delivery.
- One story beat per slide: kicker → two-beat slide title → at most one main content pattern (3 cards, 3 stats, 4–7 steps, timeline, or two columns).
- Phone-first decks use `DeckNav`, `slide-max`, thumb-zone Back/Next and tap-to-open detail.
- Each slide may end with one `Deeper` link into the Strategy Hub.
- Keep detail behind taps instead of shrinking it onto the slide.

## Default story shape

Aim for roughly 6–9 core slides unless the user requests another length.

A good strategy sequence may include:
1. sharp opening / thesis;
2. the tension or problem;
3. the key insight;
4. the proposed direction;
5. what changes in practice;
6. evidence / why believe this;
7. what happens next;
8. go deeper → Strategy Hub.

One main idea per slide. Avoid turning sections into documents pasted onto slides.

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

## Mesh/network treatment

A playful interactive mesh/network is allowed as a presentation-only expressive treatment when it remains behind the content and does not damage readability. Use teal nodes around 55% opacity, lines around 26%, pale-cyan touch glow and purple tap ripples; vignette toward edges and disable/pause under `prefers-reduced-motion`.

Good uses:
- cover/transition slides;
- slides about community, relationships, connected systems;
- moments where interaction adds delight.

Do not use the mesh on every slide. Do not treat it as a map.

## Link to the Hub

If a Hub URL is known:
- final slide includes a prominent `Open Strategy Hub` / `Go deeper` action;
- earlier deep-dive references may link to specific Hub sections where useful.

## References

- `references/pitch-structure.md`
- `examples/IL2027_pitch.html` as a reference implementation, especially for the playable mesh treatment.
