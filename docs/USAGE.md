# Using the ilabsro-design plugin

## Start here

`ilabsro-design` is an Innovation Labs plugin for Claude.

It gives Claude reusable Innovation Labs-specific guidance for creating websites, presentations, one-pagers, social content, content plans and custom brand visuals.

You do not need to know the internal skill names before using it.

Start by telling Claude what you want to make and, when the task depends on real information, attach or paste the source material.

For example:

> Turn this strategy into an Innovation Labs presentation for a potential partner.

or:

> Create a 5-frame Innovation Labs Instagram carousel from this event recap.

Claude can choose the relevant plugin skill for the job. If you already know which skill you want, you can also name it explicitly.

A **skill** is a set of task-specific instructions that tells Claude how to handle a particular kind of Innovation Labs work.

The plugin contains different kinds of skills:

- **output skills** create the artifact itself;
- **content-planner** helps decide what the content should be before production;
- **tone lenses** adjust how the copy sounds;
- **brand-image-maker** guides custom diagrams and illustrations;
- **brand-elements** provides approved reusable Innovation Labs visual assets and treatments.

The bundled examples are references for quality and behaviour. They are not templates that every new artifact should copy.


## Your first 5 minutes

### 1. Start with the outcome

Tell Claude what you need in normal language.

Examples:

> Make an Innovation Labs one-pager for a university partner from this source material.

> Turn these event notes into a short Instagram carousel.

> Create a presentation explaining this programme direction.

You do not need to begin by naming a skill.


### 2. Give Claude real source material when facts matter

Attach or paste the strategy, notes, brief, research, event recap or other source material the artifact should be based on.

The plugin is designed to preserve source fidelity rather than invent unsupported facts, numbers, quotes or commitments.


### 3. Use `content-planner` when you do not yet know what the output should say

If you have source material but are still deciding on the strongest angle, ask Claude to start with `content-planner`.

For example:

> Read this material and use content-planner to propose a few grounded content directions. Do not create the final artifact yet.

The normal flow is:

`source → PLAN → human selects idea + format → BRIEF → output skill → human review`

The human selection step is intentional.


### 4. Let the output skill make the artifact

The main output skills are:

- `website-maker` — websites and microsites;
- `presentation-maker` — presentation decks;
- `one-pager-maker` — one-page explainers and partner briefs;
- `insta-post-maker` — social posts and carousels.
- `reels-maker` — educational and promotional Instagram Reels, rendered to MP4 with the bundled IL Reel Kit (needs Node, Playwright/Chromium and ffmpeg).

You may name the skill explicitly, but you can also describe the desired result and let Claude choose the appropriate one.


### 5. Add support only when it helps

Use:

- `formal-lens`, `friendly-lens` or `jokey-lens` when the voice matters;
- `human-pass` as the final copy check before a draft is shown;
- `brand-image-maker` when the artifact needs a custom diagram, illustration or visual concept;
- `brand-elements` when reusable Innovation Labs visual assets or branded treatments are useful.

Do not stack skills just because they exist. The simplest combination that solves the task is usually better.


### 6. Review and iterate

Treat the first output as a working version.

Check:

- whether the facts match the source;
- whether the main idea is clear;
- whether the tone fits the audience;
- whether the visual structure helps explain the content;
- whether anything feels too dense or generic.

Then give Claude specific feedback and iterate.


## Starter prompts

### Website

> Use the Innovation Labs Design plugin to turn this source material into a responsive Innovation Labs website. Choose the appropriate website structure for the content rather than copying an existing example.

### Presentation

> Create an Innovation Labs presentation from this material. Keep one primary idea per slide and choose the narrative structure that best fits the source.

### One-pager

> Turn this source into a concise Innovation Labs one-pager for a partner audience. Keep it to exactly one page and preserve only the most decision-relevant information.

### Social carousel

> Turn this approved content into a short Innovation Labs social carousel. Keep one primary thought per frame and use custom visual explanation where it communicates faster than more text.

### Content planning first

> Use content-planner on this source. Propose up to five distinct, source-grounded content opportunities, then stop so I can choose the idea and format before you continue.

### Custom visual

> Create one standalone Innovation Labs visual for this idea. Choose the most suitable brand-image-maker direction yourself and keep the visual simple enough to understand at a glance.


## About bundled examples

The plugin includes validated generated examples for websites, presentations, one-pagers, social content and standalone visuals.

Claude may inspect a small number of relevant examples when they help clarify:

- the expected quality bar;
- how a format behaves;
- how a prompt or brief became an output;
- the visual or editorial grammar of a particular artifact type.

Examples should not override the current request.

Do not copy their facts, names, URLs, wording, layout or composition into unrelated work.

See `EXAMPLES.md` for the example index.

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

## Humanizer (external, optional)

`human-pass` is bundled with `ilabsro-design` as the final copy pass (see `skills/human-pass/SKILL.md`).

Do not run it automatically on factual tables, labels, citations, source quotes or numbers. Prefer it for narrative copy after structure is approved.

## Rule of one

For a normal task, use:
- one output skill;
- zero or one tone lens;
- one design system;
- zero or one `brand-elements` modifier;
- one accent per artifact.

Do not stack multiple output-maker skills unless the user explicitly asks for a multi-format campaign.
