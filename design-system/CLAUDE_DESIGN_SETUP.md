# Create or update the native Innovation Labs Design System in Claude

The native Claude Design System is an optional richer representation of the bundled portable spec. The plugin must still work without it.

## Source material to attach

Recommended:
1. `INNOVATION_LABS_DESIGN_SYSTEM.md`
2. `TOKENS.css`
3. `BRAND_ELEMENTS.md`
4. the approved Strategy Hub HTML/screenshots
5. the approved route-first Presentation HTML/screenshots
6. official logos and, when supported, the shared `assets/brand-elements/`
7. optionally the deployed showcase

## Prompt

Create/update a reusable design system called **Innovation Labs** from the attached references.

Treat the written design-system specification as the rules and the Hub + Presentation as reference implementations, not templates to copy blindly.

Capture:
- teal/deep-teal identity and Light/Night behavior;
- purple default accent and optional yellow accent through the same semantic role;
- Poppins display/body, IBM Plex Mono labels, Caveat one-off human emphasis;
- flat reading surfaces plus approved gradients/template grounds for bands/covers/social;
- official SVG brand elements as optional decoration, normally one per view;
- medium-rounded cards/pills and editorial data visualization;
- route-first map/deck patterns and responsive vertical journey behavior;
- fluid layout rules: one scaling unit, one container, continuous sizing, no stacked patch CSS;
- distinction between calm map grounds, static brand mesh grounds and the optional presentation-only playable network;
- photo-led social composition including text overlays and photo-to-teal blending.

Do not include dotted-grid page backgrounds. Do not generalize decorative mesh into Strategy Route maps.

## Validation prompts

After updating the Design System, test:
- “Create a strategy landing page for Innovation Labs.”
- “Create a route-first strategy presentation with yellow accent.”
- “Create a one-page partner brief from this document.”
- “Create a 5-card event recap carousel from these photos.”

If outputs feel like unrelated brands, refine the Design System before changing output skills.
