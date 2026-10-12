# Design-system sync notes — 2026-10-12

v0.4 synchronizes the portable plugin with Flavia's refreshed showcase and the newly generated 2027 Strategy Hub + route-first presentation.

## Confirmed v0.4 changes

- Purple remains the default semantic accent; yellow is now a supported alternate accent.
- Accent is represented by `--ax*` tokens so structure does not change when color swaps.
- Approved brand gradients and template mesh grounds are available for bands, covers, campaign social and selected callouts.
- Reading surfaces remain flat; Strategy Route map backgrounds remain calm and decorative-mesh-free.
- 16 official transparent SVG brand elements are bundled in `assets/brand-elements/`.
- Approved template JPG backgrounds are bundled in `assets/backgrounds/`.
- `brand-elements` is a visual modifier skill for choosing accent, branded ground and a meaningful official element.
- Presentations can be route-first when the strategy/program has a meaningful journey. Portrait uses a vertical journey; landscape uses the full route.
- `Lead the room` is an optional Artifact-runtime enhancement and must degrade gracefully when room capability is unavailable.
- Fluid layout guidance now favors one scaling unit, one shared container, no stacked patch layers, continuous scaling and explicit laptop/phone checks.
- Social has two supported visual families: photo-led event content and template-ground campaign content.
- Social event photography may use text directly on the image or a photo-to-teal transition; it should not default to a hard photo rectangle plus color block.

## Preserved rules

- Source material remains authoritative; never invent figures, quotes, findings, names or personal insights.
- No generic `Open Threads` / `Open Questions` section by default.
- Maps are calm journey maps, not decorative network backgrounds.
- Presentation playable network remains selective and presentation-only.
- Explicit one-page requests must produce exactly one page.

## Reference note

The refreshed Hub and route deck are reference implementations, not universal templates. They currently use different narrative stop lists. Therefore the plugin only requires an identical shared route across formats when the user supplies/approves a shared route model or asks for a coordinated Hub + deck family.
