# Plugin architecture

```text
ilabsro-design/
├── .claude-plugin/
│   └── plugin.json
├── assets/
│   ├── backgrounds/
│   ├── brand-elements/
│   ├── logo_currentcolor.svg
│   ├── logo_primary_2027.svg
│   └── logo_white_2027.svg
├── design-system/
│   ├── INNOVATION_LABS_DESIGN_SYSTEM.md
│   ├── TOKENS.css
│   ├── BRAND_ELEMENTS.md
│   ├── COMPONENT_CATALOG.md
│   ├── CLAUDE_DESIGN_SETUP.md
│   └── SYNC_NOTES.md
├── skills/
│   ├── website-maker/
│   ├── presentation-maker/
│   ├── one-pager-maker/
│   ├── insta-post-maker/
│   ├── content-planner/
│   ├── brand-image-maker/
│   ├── brand-elements/
│   ├── formal-lens/
│   ├── friendly-lens/
│   └── jokey-lens/
├── generated-examples/
├── showcase/
├── docs/
└── scripts/
```

## Why some assets exist twice

`showcase/assets/` is self-contained so the Vercel showcase can deploy from `showcase/` alone. `assets/` is the portable plugin asset library used by skills. Do not deduplicate across those two roots unless the deployment model changes.

Social-only mascot PNGs remain inside `skills/insta-post-maker/assets/brand-elements/`; shared official SVG elements live in root `assets/brand-elements/`.

## Composition model

- Content planning layer: optional `content-planner` before generation when source material needs to become content opportunities or a structured brief.
- Output maker: exactly one of `website-maker`, `presentation-maker`, `one-pager-maker`, `insta-post-maker`.
- Custom image layer: optional `brand-image-maker` when an artifact needs a generated diagram, illustration or atmospheric visual.
- Tone lens: zero or one of `formal-lens`, `friendly-lens`, `jokey-lens`.
- Visual modifier: optional `brand-elements`.
- Design System: bundled v0.4 rules; native Claude Design System may mirror them when available.

The plugin intentionally does not bundle connectors, agents or hooks. Its job is reusable design behavior and portable assets.
