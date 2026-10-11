# Using the ilabsro-design plugin

## Mental model

**Bundled Design System = portable rules for how Innovation Labs looks.**

**Native Claude Design System = optional visual/runtime mirror of those rules.**

**Output skill = what you are making.**

**Tone lens = how the copy sounds.**

**Source material = what the output says.**

## Recommended combinations

### Strategy website
Use `website-maker` + bundled Innovation Labs Design System; native Claude Design may mirror it when available.

### Strategy presentation
Use `presentation-maker` + optional `friendly-lens` or `formal-lens` + bundled Design System; native Claude Design may mirror it when available.

### Partner one-pager
Use `one-pager-maker` + `formal-lens` + native Design System.

### Founder/community one-pager
Use `one-pager-maker` + `friendly-lens`.

### Social post
Use `insta-post-maker` + `friendly-lens` or `jokey-lens`.

## Humanizer

The public Humanizer skill is an optional final copy pass. Do not run it automatically on factual tables, labels, citations, source quotes or numbers. Prefer it for narrative copy after the output structure is approved.

## Rule of one

For a normal task, use:
- one output skill;
- zero or one tone lens;
- one design system.

Do not stack multiple output-maker skills unless the user explicitly asks for a multi-format campaign.
