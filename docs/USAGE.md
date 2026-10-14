# Using the ilabsro-design plugin

## Mental model

**Bundled Design System = portable rules for how Innovation Labs looks and behaves.**

**Native Claude Design System = optional visual/runtime mirror of those rules.**

**Output skill = what you are making.**

**Tone lens = how the copy sounds.**

**brand-elements = optional visual modifier for accent, approved grounds and official decorative assets.**

**Source material = what the output says.**

## Recommended combinations

### Strategy website
Use `website-maker`. Add `brand-elements` only when the user explicitly wants an alternate accent or branded hero/band treatment. Map/route backgrounds stay calm even when brand-elements is active.

### Strategy presentation
Use `presentation-maker` + optional `friendly-lens` or `formal-lens`. For strategy/program narratives, route-first is preferred when the source has a meaningful sequence. Add `brand-elements` for purple/yellow accent choice or a branded cover/transition ground.

### Partner one-pager
Use `one-pager-maker` + `formal-lens`. `brand-elements` may add a controlled gradient header/closing band or one approved decorative element.

### Founder/community one-pager
Use `one-pager-maker` + `friendly-lens`.

### Social with event photos
Use `insta-post-maker` + optional lens. Prefer full-photo text overlays, photo-to-teal blends or teal-led editorial crops. A small social-only mascot may be used when meaningful.

### Campaign/social without photos
Use `insta-post-maker` + `brand-elements`. Pick one approved template ground, one accent and usually one official SVG element.

## Content planning

Use `content-planner` when approved strategy, research, event scripts or program notes need to become a small set of source-grounded content opportunities.

The normal flow is:

`source → content-planner PLAN → human selects idea + format → content-planner BRIEF → output skill → human review`

`content-planner` does not make final visual decisions and does not replace the downstream output skill.

## Custom brand images

Use `brand-image-maker` when a diagram, sketch, narrative illustration or atmospheric generated visual communicates an idea faster than another text block.

It can be used by `insta-post-maker` or other output skills. Human-selected visual mode, complexity and tone are authoritative when supplied.

## Accent

Purple is the default accent. Yellow is an optional alternate accent when requested or when `brand-elements` selects it for a suitable campaign. The accent is a semantic role: new, AI/challenger, current step, plans, focus and selective human emphasis.

Never use white text on a yellow accent fill; use the dark `--ax-on` token.

## Humanizer

The public Humanizer skill is an optional final copy pass. Do not run it automatically on factual tables, labels, citations, source quotes or numbers. Prefer it for narrative copy after structure is approved.

## Rule of one

For a normal task, use:
- one output skill;
- zero or one tone lens;
- one design system;
- zero or one `brand-elements` modifier;
- one accent per artifact.

Do not stack multiple output-maker skills unless the user explicitly asks for a multi-format campaign.
