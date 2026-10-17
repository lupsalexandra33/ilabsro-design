# ilabsro-design

Innovation Labs design and content plugin for creating consistent websites, presentations, one-pagers, social content, standalone visuals and source-grounded content plans.

**Plugin version:** `v0.5.1`

The project packages Innovation Labs visual language, reusable brand elements, artifact-making skills, content planning and voice guidance into one working system.

The goal is not to generate one fixed template.

The goal is to make different Innovation Labs artifacts feel recognizably related while still allowing each format and story to choose the structure that fits it.

---

## What the distributed plugin includes

The Claude-distributed plugin is designed to be usable without access to the full development repository.

The runtime package includes:

- the 10 plugin skills under `skills/`;
- the portable Innovation Labs design system under `design-system/`;
- shared reusable brand assets under `assets/`;
- validated capability references under `generated-examples/`;
- first-time usage guidance in `docs/USAGE.md`;
- the curated example index in `docs/EXAMPLES.md`.

The bundled generated examples are **references, not canonical templates**.

They exist so Claude can inspect the relationship between a request, its constraints and a successful output when a concrete example would materially help.

Claude should use only a small number of relevant examples for a task and must not mechanically inherit their facts, wording, URLs, layout or composition.

Current source material, the current request and the current skill rules always take priority.

---

## What it can make

`ilabsro-design` currently supports:

- websites and microsites;
- presentation decks;
- one-pagers;
- Instagram / social carousels;
- standalone explanatory visuals;
- source-grounded content plans and briefs;
- reusable Innovation Labs brand elements;
- tone adaptation through voice lenses.

Generated and validated examples live in:

`generated-examples/`

---

## Skills

The plugin currently contains **10 skills**.

### Artifact makers

#### `website-maker`

Creates responsive Innovation Labs websites and microsites.

It focuses on:

- information architecture;
- story structure;
- responsive layouts;
- interaction;
- Innovation Labs visual consistency;
- choosing a layout appropriate to the specific content rather than repeating one site pattern.

---

#### `presentation-maker`

Creates Innovation Labs presentation decks.

It supports different storytelling structures rather than relying on one fixed route-based deck format.

It focuses on:

- one clear idea per slide;
- visual pacing;
- varied composition;
- diagrams and custom visuals;
- presentation-specific hierarchy;
- readable partner-facing storytelling.

---

#### `one-pager-maker`

Creates compact Innovation Labs one-pagers and explainers.

It focuses on:

- editorial hierarchy;
- one-page information architecture;
- visual comparison;
- diagrams;
- print and screen readability;
- concise supporting copy.

---

#### `insta-post-maker`

Creates Innovation Labs social posts and carousels.

It prefers:

- one primary thought per frame;
- more frames with less information per frame;
- strong visual explanation;
- custom drawings and diagrams;
- concise copy;
- avoiding repetitive eyebrow + headline + paragraph layouts.

---

## Planning and visual generation

### `content-planner`

Transforms source material into source-grounded content directions and briefs.

The core workflow is:

```text
source material
→ candidate ideas
→ evaluation
→ human selection
→ content brief
→ artifact generation
→ human review
```

The skill prioritizes source fidelity over creativity.

It is designed so the human remains responsible for selecting the idea and format before generation continues.

---

### `brand-image-maker`

Creates standalone Innovation Labs visuals and supporting illustrations.

It can autonomously select an appropriate visual direction based on the idea being communicated.

Current visual modes include:

- `handdrawn-diagram`
- `narrative-illustration`
- `event-glow`

The goal is to avoid generic AI visual language and create visuals that feel specific to Innovation Labs.

Examples include:

- explanatory hand-drawn diagrams;
- comparison visuals;
- narrative startup illustrations;
- event-oriented branded imagery.

---

### `brand-elements`

Provides reusable Innovation Labs visual elements for other skills.

The plugin currently includes **16 shared SVG brand elements** used across websites, decks, one-pagers and other outputs.

---

## Voice lenses

### `formal-lens`

Adapts content toward a more formal Innovation Labs voice.

Useful for:

- partner material;
- institutional communication;
- structured briefs;
- formal presentations.

---

### `friendly-lens`

Adapts content toward a more approachable and conversational tone while preserving clarity.

---

### `jokey-lens`

Adds a more playful tone where appropriate without turning the content into generic internet copy.

---

## Design system

The plugin includes portable Innovation Labs design tokens and visual rules under:

`design-system/`

The current design-system token version may remain different from the plugin version.

For example:

```text
Plugin: v0.5.1
Design system / portable tokens: v0.4
```

These versions describe different layers of the project and do not need to move together.

The system includes guidance for:

- typography;
- Innovation Labs teal;
- semantic accent colours;
- Light / Night modes;
- branded mesh backgrounds;
- spacing;
- borders;
- radius;
- shadows;
- layout;
- visual hierarchy;
- reusable brand elements.

---

## Generated examples

Validated outputs created with the plugin live under:

`generated-examples/`

The examples are intentionally varied.

They are not intended to demonstrate one canonical layout.

Instead, they test whether the system can generate different artifact archetypes while remaining recognizably Innovation Labs.

The generated examples are also bundled with the distributed plugin as capability references.

Where available, an example may include:

- `README.md` — what the artifact tests and why it was kept;
- `prompt.md` — the archived generation prompt;
- `brief.md` — a documented downstream brief when one exists;
- the generated output itself.

Not every historical example has every provenance file. Missing prompts must not be reconstructed or presented as original prompts.

See `docs/EXAMPLES.md` for the curated map between examples, skills and intended use.

Current example families include:

```text
generated-examples/
├── website/
├── presentation/
├── one-pager/
├── social/
└── visuals/
```

Examples currently include work such as:

### Websites

- Strategy Hub
- Build for real problems

These explore different website structures:

- route / strategy exploration;
- campaign / challenge microsite.

### Presentations

- Route Deck
- Learning Environment

These explore:

- route-first storytelling;
- non-route-first narrative presentation structure.

### One-pagers

- 2027 Vision
- Better AI output starts with better context

### Social

- Context Engineering
- Source Before Prompt

Each multi-frame carousel is treated as one artifact.

### Standalone visuals

- Idea Meets Real Users
- You Go First / AI as You Sharpen
- Test My Thinking

The visual examples intentionally test different explanatory structures, including:

- narrative illustration;
- sequential process;
- direct comparison.

---

## Artifact Index

The repository includes an Innovation Labs Artifact Index under:

`artifact-index/`

The Artifact Index answers:

> What have we built, explored, documented or systematized for Innovation Labs?

It acts as a working library / studio archive across:

- generated examples;
- workflows;
- tools;
- systems;
- documentation.

It includes:

- Selected work;
- complete Library;
- Registry;
- category filtering;
- format filtering;
- search;
- Light / Night modes;
- accent switching;
- direct viewing for visual artifacts.

For visual work, the Artifact Index is intended to be the primary viewing experience.

GitHub remains the source of provenance rather than the gallery itself.

Canonical generated media remains in:

`generated-examples/`

The Artifact Index may keep lightweight UI previews, but it should not become a second copy of the generated artifact library.

---

## Plugin Showcase

The repository also contains a separate Plugin Showcase under:

`showcase/`

The Artifact Index and Plugin Showcase have different purposes.

### Artifact Index

> What exists across the Innovation Labs work?

### Plugin Showcase

> What can `ilabsro-design` do and how does the system work?

The Plugin Showcase focuses on:

- design system;
- plugin capabilities;
- skills;
- visual language;
- representative generated outputs;
- usage patterns.

It should not replace the Artifact Index, and the Artifact Index should not become plugin documentation.

---

## Content workflow

Public workflow documentation lives under:

`docs/content-workflow/`

The current source-grounded content flow is:

```text
source
↓
content-planner
↓
candidate ideas
↓
evaluation
↓
human selects idea + format
↓
brief
↓
artifact maker
↓
human review
```

The human selection step is intentional.

The system is designed to assist with discovery, structure and generation without silently deciding what should be published.

The current workflow is an MVP and does not imply production publishing, scheduling or external integrations.

---

## Repository structure

```text
ilabsro-design/
│
├── .claude-plugin/
│   └── plugin.json
│
├── assets/
│   ├── backgrounds/
│   ├── elements/
│   └── logos/
│
├── design-system/
│   └── ...
│
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
│
├── generated-examples/
│   ├── website/
│   ├── presentation/
│   ├── one-pager/
│   ├── social/
│   └── visuals/
│
├── artifact-index/
│   ├── index.html
│   ├── assets/
│   └── previews/
│
├── showcase/
│   └── ...
│
├── docs/
│   ├── content-workflow/
│   ├── EXAMPLES.md
│   ├── PLUGIN_ARCHITECTURE.md
│   ├── TEST_MATRIX.md
│   └── USAGE.md
│
├── scripts/
│   └── validate_plugin.py
│
└── README.md
```

---

## Source of truth

The repository follows a simple ownership rule:

```text
skills/
= behaviour and generation guidance

design-system/
= visual system and tokens

assets/
= shared reusable brand assets

generated-examples/
= canonical generated outputs

artifact-index/
= library / navigation / viewing layer

showcase/
= plugin capability showcase

docs/
= usage guidance, example index, workflows and technical documentation
```

Original generated outputs should not be unnecessarily duplicated inside the Artifact Index or Showcase.

---

## Working principles

### Source fidelity over invention

When an artifact is based on source material, generation should remain grounded in that material.

The system should not turn weak evidence into strong claims.

---

### Human choice remains explicit

For content planning, candidate ideas may be generated automatically, but a human chooses the idea and output format before downstream production.

---

### Different artifacts need different structures

A website, carousel, deck and one-pager should not all look like the same template resized into different dimensions.

Shared brand language should coexist with format-specific composition.

---

### Visuals should explain, not decorate

Custom drawings, diagrams and illustrations should carry part of the meaning.

They should not exist only as decorative filler.

---

### Simpler frames over overloaded frames

Especially in social content and presentations, the system prefers splitting complex ideas across multiple frames or slides instead of compressing everything into one.

---

### AI should support thinking, not erase it

Several generated examples explore a human-first use of AI:

```text
human brings the first thinking
→ AI challenges assumptions
→ human reviews and sharpens the result
```

These examples are conceptual communication artifacts, not claims about a specific AI model.

---

## Validation

The repository includes validation tooling under:

`scripts/`

Generated examples are kept when they meaningfully test a capability, format or visual direction.

Examples may be labelled as:

- validated;
- example;
- prototype;
- exploratory.

Validation is about whether the artifact is useful as a reference for the system, not whether it represents an official Innovation Labs publication.

---

## Status

Current plugin version:

`v0.5.1`

Current plugin scope:

```text
10 skills
16 shared SVG brand elements
multiple artifact formats
source-grounded content planning
custom visual generation
validated generated examples
Artifact Index
Plugin Showcase
```

The project is actively evolving toward a more complete production workflow while keeping the repository usable as a clear design-system and artifact-generation reference.
