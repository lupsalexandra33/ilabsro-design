# Bundled examples

`ilabsro-design` includes a small set of validated generated artifacts.

These examples exist to help Claude understand the relationship between a request, the relevant skill guidance and the resulting artifact.

They are **references, not templates**.

When a concrete reference would materially help the current task, Claude may inspect one or two relevant examples.

Learn from:

- the relationship between request, constraints and result;
- the quality bar;
- format behaviour;
- visual and editorial grammar;
- how multiple skills can work together.

Do not inherit:

- facts;
- names;
- URLs;
- claims;
- exact wording;
- exact layout;
- exact composition.

Current source material and the current skill rules always take priority over an example.

Do not inspect every example by default. Choose only the example or examples that are relevant to the current task.


## Websites

### Strategy Hub

**Path**

`generated-examples/website/strategy-hub/`

**Skills**

`website-maker`

**What it demonstrates**

A source-rich Innovation Labs strategy website using a route-first structure when the source supports a meaningful sequence.

It demonstrates:

- editorial website structure rather than dashboard composition;
- a calm strategy route;
- shared route ordering across representations;
- responsive transformation from horizontal route to vertical mobile journey;
- source-grounded strategic content.

**Archived prompt**

`generated-examples/website/strategy-hub/prompt.md`

**Output**

`generated-examples/website/strategy-hub/index.html`

**When to inspect it**

Inspect this example when building a strategy hub, programme website or source-rich website whose material naturally supports a route or sequence.

Do not assume every Innovation Labs website should use a route-first structure.


### Build for real problems

**Path**

`generated-examples/website/build-for-real-problems/`

**Skills**

`website-maker` + `brand-elements`

**What it demonstrates**

A fictional Innovation Labs campaign / challenge microsite using a different website archetype from the Strategy Hub.

It demonstrates:

- campaign-oriented information architecture;
- a strong campaign hero;
- responsive static web output;
- use of the shared Innovation Labs design system without copying the Strategy Hub layout;
- the ability of `website-maker` to generalize across different site structures.

**Archived prompt**

`generated-examples/website/build-for-real-problems/prompt.md`

**Output**

`generated-examples/website/build-for-real-problems/index.html`

**When to inspect it**

Inspect this example when the task is a campaign, challenge, landing page or microsite and a route-first structure would not fit the content.


## Presentations

### Route Deck

**Path**

`generated-examples/presentation/route-deck/`

**Skills**

`presentation-maker`

**What it demonstrates**

A route-first Innovation Labs presentation based on the 2027 strategy.

It demonstrates:

- route-first storytelling when the source has a meaningful sequence;
- presentation-specific hierarchy;
- route context carried through the deck;
- presentation-only visual behaviour;
- responsive presentation treatment.

**Archived prompt**

Original prompt not archived.

Do not reconstruct or invent an “original prompt” for this example.

**Output**

`generated-examples/presentation/route-deck/index.html`

**When to inspect it**

Inspect this example when a strategy or programme presentation genuinely benefits from a route, journey or sequence.

Do not treat route-first storytelling as the default for every deck.


### Useful startup learning environment

**Path**

`generated-examples/presentation/learning-environment/`

**Skills**

`presentation-maker` + `brand-image-maker` + `brand-elements`

**What it demonstrates**

A fictional seven-slide conversation deck that deliberately avoids the Route Deck structure.

It demonstrates:

- one primary idea per slide;
- non-route-first narrative structure;
- varied slide composition;
- diagrams and custom illustrations;
- concise partner-facing storytelling;
- Innovation Labs consistency across a different presentation archetype.

**Archived prompt**

`generated-examples/presentation/learning-environment/prompt.md`

**Output**

`generated-examples/presentation/learning-environment/index.html`

**When to inspect it**

Inspect this example when the presentation should feel conversational, educational or idea-led rather than route-led.


## One-pagers

### 2027 Vision one-pager

**Path**

`generated-examples/one-pager/2027-vision/`

**Skills**

`one-pager-maker` + `formal-lens`

**What it demonstrates**

A formal one-page partner brief based on Innovation Labs 2027 strategy material.

It demonstrates:

- strict one-page constraint;
- compression of source material;
- formal partner-facing voice;
- strong editorial hierarchy;
- restrained Innovation Labs visual treatment;
- source fidelity.

**Archived prompt**

`generated-examples/one-pager/2027-vision/prompt.md`

**Output**

`generated-examples/one-pager/2027-vision/IL2027_Revamp_OnePager.pdf`

**When to inspect it**

Inspect this example when producing a concise partner, institutional or programme one-pager where information must remain formal and fit on one page.


### Better AI output starts with better context

**Path**

`generated-examples/one-pager/better-ai-context/`

**Skills**

`one-pager-maker` + `brand-image-maker` + `brand-elements`

**What it demonstrates**

A standalone educational Innovation Labs one-pager explaining a practical AI working principle.

It demonstrates:

- compact educational information architecture;
- visual comparison;
- custom explanatory diagrams;
- concise practical guidance;
- screen-readable and print-safe execution;
- use of the Innovation Labs system for an abstract topic rather than programme strategy.

**Archived prompt**

`generated-examples/one-pager/better-ai-context/prompt.md`

**Output**

`generated-examples/one-pager/better-ai-context/better-ai-context.pdf`

**When to inspect it**

Inspect this example when a one-pager needs to explain an idea, working principle or educational concept rather than summarize a programme.


## Social

### Context engineering

**Path**

`generated-examples/social/context-engineering/`

**Skills**

`insta-post-maker` + `brand-image-maker` + `brand-elements`

**What it demonstrates**

A validated Innovation Labs carousel about improving AI work through better source material, domain context, correction and iteration.

It demonstrates:

- one primary thought per frame;
- simpler carousel pacing;
- hand-drawn explanatory diagrams;
- coordination between editorial structure and custom visuals;
- source-aware claims;
- quiet handling of non-critical evidence notes.

**Archived prompt**

`generated-examples/social/context-engineering/prompt.md`

**Archived brief**

`generated-examples/social/context-engineering/brief.md`

The brief is a documented downstream content brief for this artifact.

Do not claim that it was generated by `content-planner` unless separate provenance explicitly establishes that.

**Output**

`generated-examples/social/context-engineering/01.png`
through
`generated-examples/social/context-engineering/11.png`

**When to inspect it**

Inspect this example when building a more developed educational carousel that needs both editorial structure and simple explanatory drawings.


### Source before prompt

**Path**

`generated-examples/social/source-before-prompt/`

**Skills**

`insta-post-maker` + `brand-image-maker` + `brand-elements`

**What it demonstrates**

A shorter Innovation Labs carousel using a very simple hand-drawn visual system.

It demonstrates:

- one thought per frame;
- concise editorial copy;
- hand-drawn visual explanation;
- variation between frames without losing coherence;
- the combined social + custom visual pipeline.

**Archived prompt**

`generated-examples/social/source-before-prompt/prompt.md`

**Output**

`generated-examples/social/source-before-prompt/01.png`
through
`generated-examples/social/source-before-prompt/07.png`

**When to inspect it**

Inspect this example when a short carousel needs to explain one clear idea with very little text and simple visual metaphors.


## Standalone visuals

### Idea meets real users

**Path**

`generated-examples/visuals/idea-meets-real-users/`

**Skills**

`brand-image-maker` + `brand-elements`

**Visual direction**

`narrative-illustration`

**What it demonstrates**

A simple narrative illustration showing a founder changing an idea after encountering real user feedback.

It demonstrates:

- visual storytelling through a scene;
- simplified characters and symbolic objects;
- visible transformation;
- very little embedded text;
- a playful Innovation Labs visual language without generic glossy AI imagery.

**Archived prompt**

`generated-examples/visuals/idea-meets-real-users/prompt.md`

**Output**

`generated-examples/visuals/idea-meets-real-users/output.png`

**When to inspect it**

Inspect this example when the idea is best communicated as a small story, human moment or transformation rather than a diagram.


### You go first

**Path**

`generated-examples/visuals/ai-as-you-sharpen/`

**Skill**

`brand-image-maker`

**What it demonstrates**

A conceptual Innovation Labs visual showing a human-first AI workflow: the person brings the initial thinking, AI challenges it and the person sharpens the result.

It demonstrates:

- autonomous visual-direction selection;
- translation of an abstract principle into a simple sequence;
- clear human ownership of the thinking;
- concise embedded copy;
- avoidance of generic human-and-robot imagery.

**Archived prompt**

`generated-examples/visuals/ai-as-you-sharpen/prompt.md`

**Output**

`generated-examples/visuals/ai-as-you-sharpen/output.png`

**When to inspect it**

Inspect this example when `brand-image-maker` needs to translate an abstract working principle into a simple explanatory visual.


### Test my thinking

**Path**

`generated-examples/visuals/test-my-thinking/`

**Skill**

`brand-image-maker`

**What it demonstrates**

A comparison visual contrasting AI replacing human thinking with AI pressure-testing thinking the person already did.

It demonstrates:

- autonomous visual-direction selection;
- direct comparison as an explanatory structure;
- one clear conceptual distinction;
- concise embedded copy;
- avoidance of generic AI collaboration clichés.

**Archived prompt**

`generated-examples/visuals/test-my-thinking/prompt.md`

**Output**

`generated-examples/visuals/test-my-thinking/output.png`

**When to inspect it**

Inspect this example when a concept is easier to understand through a direct comparison rather than a sequence or narrative scene.


## How Claude should use this library

Before consulting an example, first understand the current request and source material.

Then:

1. identify the current artifact type;
2. choose at most one or two examples that are genuinely relevant;
3. inspect their README and archived prompt when available;
4. use them to understand quality, constraints and format behaviour;
5. return to the current source and current skill rules;
6. create a new solution appropriate to the present task.

A new artifact should be recognizably Innovation Labs without becoming a copy of a previous artifact.
