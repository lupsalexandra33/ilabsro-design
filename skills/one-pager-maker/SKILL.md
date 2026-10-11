---
name: one-pager-maker
description: Create concise Innovation Labs one-pagers from source material for partners, founders or internal use, following the shared IL design system.
version: 0.2.0
---

# Innovation Labs One-Pager Maker

Use when the user wants a single-page strategy summary, program overview, partner brief or printable reference.

## Before building

1. Read `../../design-system/INNOVATION_LABS_DESIGN_SYSTEM.md` and `../../design-system/TOKENS.css`. If the native **Innovation Labs** Design System is available, use it as a matching runtime representation, not as a separate source of rules.
2. Read `references/one-pager-pattern.md`.
3. Identify the audience and the one message the page must leave behind.
4. Ground every claim in supplied sources.

## Native format contract

- Default to Light and A4/PDF-safe styling.
- Use a 12-column grid with 15mm margins.
- One 36–44pt headline, one lead, then 3–6 modular blocks.
- Body 9.5–10.5pt Poppins; labels 7.5–8pt IBM Plex Mono; stats 28–40pt in teal.
- Prefer `surface-tint` card fills to borders for print reliability.
- No glows or transparency over photos.
- If the user explicitly asks for a one-page or single-page document, the final output MUST fit on exactly one page. Otherwise, two pages maximum; if content exceeds that, move detail to the Hub and link.

## Default contract

- When page count is unspecified, one page is preferred and a second page is allowed only when necessary. When the user explicitly asks for one page, do not spill onto page two: prioritize, compress or remove lower-priority detail and move deeper content to the Hub. Never solve overflow by shrinking into unreadable density.
- One primary thesis.
- 3–5 supporting modules maximum.
- Prefer numbers, short takeaways and diagrams over long prose.
- Use a strong visual hierarchy and clear ending / takeaway.
- Default print treatment is light mode; a dark digital variant is optional when explicitly requested.
- No dotted-grid background.

## Link handling

- If the user provides a current/final Strategy Hub URL for the deliverable, use that exact URL.
- Do not automatically reuse a historical Claude artifact URL found in reference/source material as the final CTA target.
- If no current Hub URL is provided, do not invent one; keep the CTA text without a fabricated destination or use an explicit placeholder when a link target is required.

## Audience adaptation

The visual identity stays IL; tone can be modified using one lens skill.

Examples:
- partner / sponsor → `formal-lens`;
- founder / community → `friendly-lens`.

## References

- `references/one-pager-pattern.md`
- `examples/IL2027_vision_onepager.html` for a concrete content-density reference. Do not copy its dotted-grid background.
