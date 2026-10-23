---
name: brand-image-maker
description: "Create Innovation Labs custom visuals from an approved content brief using controllable hand-drawn, narrative illustration or event-glow directions."
version: "0.1.2"
---

# Innovation Labs Brand Image Maker

Use when an Innovation Labs artifact needs a custom explanatory or atmospheric image rather than only layout, typography, photography or an existing brand element.

This skill is a visual-generation layer. It can support social posts, presentations, one-pagers and other artifacts.

It does **not** decide the content strategy and it does **not** assemble the final social post.

## Read first

1. Read `../../design-system/INNOVATION_LABS_DESIGN_SYSTEM.md`.
2. Read `../../design-system/TOKENS.css`.
3. Read `../../design-system/BRAND_ELEMENTS.md`.
   Read `../../design-system/AI_TELLS.md`: the patterns Innovation Labs never ships (generic icon tiles, emoji, glassmorphism, em dashes, Inter/Geist/Space Grotesk, three feature cards, bento grids, fake terminals, "it's not X, it's Y", placeholder demos, purple-on-black, glow orbs, dot grids, sparkles, arrow-nudge CTAs, big hover motion, rainbow color). Before delivering, run `python3 ../human-pass/scripts/design_tells.py <output>` and fix every finding that isn't a documented IL exception.
4. Treat the approved content brief as authoritative for message, facts and boundaries.
5. If a user supplies visual references, study their visual behavior but do not copy a specific illustration or layout literally.

## Core goal

Turn one approved idea into one useful Innovation Labs visual.

A good generated image should:
- make the idea easier or faster to understand;
- feel recognizably IL;
- be simple enough to work inside another artifact;
- avoid generic corporate infographic aesthetics;
- avoid glossy, over-rendered "AI art" unless that treatment is explicitly requested.

## Human control

The human may optionally select:

### Visual mode
- `handdrawn-diagram`
- `narrative-illustration`
- `event-glow`

### Complexity
- `very-simple`
- `medium`
- `detailed`

### Tone
- `playful`
- `smart`
- `warm`
- `energetic`

Human-selected values are authoritative.

If the human does not specify one or more of these values, choose the best fit from the content brief without forcing an unnecessary clarification question.

If the user explicitly asks to see options before generation, recommend up to 3 directions and wait for selection.

## Input contract

Use the information available from the upstream brief or request:

- purpose of the image;
- core message;
- must-show idea or relationship;
- must-not-introduce claims;
- intended artifact and aspect ratio when known;
- human-selected visual mode, complexity or tone when provided.

When information is missing, infer only visual execution details. Do not invent factual content.

## Visual mode A — handdrawn-diagram

Use when the image should explain a process, distinction, relationship, sequence, framework or mental model.

Possible subtypes:
- sticky board;
- process sketch;
- concept map;
- story sequence;
- annotated doodle;
- whiteboard schema;
- sketched comparison;
- facilitator-style explainer.

Sticky-note boards are only **one** subtype. Do not treat sticky notes as the automatic default for every hand-drawn output.

### Style behavior

Prefer:
- visibly hand-drawn lines;
- slightly imperfect arrows and connectors;
- circles, underlines and quick emphasis marks;
- sticky-note shapes **when useful**, not by default;
- simple symbolic doodles;
- whiteboard-style containers, labels or callouts;
- question marks, magnifiers, balances, pathways, tiny props or mini scene metaphors when they explain better than another sticky note;
- generous whitespace;
- one visual thought per image;
- a workshop / facilitator / sketchnote feeling;
- Innovation Labs teal as the anchor color, with current semantic accent used selectively.

Across a multi-slide set, vary the visual grammar. Some slides may use a sticky note, others may use a sketch, a simple comparison, a callout, a circled term, a mini process or a single doodled object.

Keep embedded text extremely short.

A hand-drawn diagram should normally be understandable from:
- a few labels;
- arrows;
- symbols;
- simple grouping.

Prefer the drawing to carry the explanation. A hand-drawn diagram should not quietly fall back into a polished editorial layout with a kicker, a giant headline and a paragraph unless that structure is absolutely necessary.

If the brief includes a named idea or term (for example, a concept label), integrate it into the sketch language: circled, underlined, annotated, connected to a doodle or positioned as part of the diagram. Do not switch back to a glossy poster treatment unless the user asks for that contrast.

Do not turn it into a text-heavy infographic.

### Avoid

Avoid:
- polished corporate flowchart styling;
- perfect vector geometry everywhere;
- dense dashboards;
- dozens of labels;
- photorealistic people;
- fake handwriting that is difficult to read;
- generic office clip-art;
- repeating the same sticky-note composition on slide after slide;
- decorative doodles that do not explain anything.

## Visual mode B — narrative-illustration

Use when a simple scene or metaphor can communicate an idea faster than explanatory copy.

This mode takes inspiration from Innovation Labs' historical team-brochure behavior: simple scenes, playful metaphors and compact visual storytelling.

Do not reproduce historical characters, exact scenes or layouts.

### Style behavior

Prefer:
- simplified geometric characters or objects;
- one scene with one clear idea;
- flat or lightly textured shapes;
- expressive poses rather than facial detail;
- simple props that explain the concept;
- optional short speech bubble when it materially improves the story;
- smart humor when the brief supports it;
- a limited IL-compatible palette.

The scene should explain, not merely decorate.

### Avoid

Avoid:
- generic 3D mascot renders;
- cinematic realism;
- over-detailed environments;
- multiple unrelated jokes;
- large blocks of text inside the image;
- copying existing brochure artwork literally.

## Visual mode C — event-glow

Use when a campaign or event visual needs an atmospheric generated image rather than a diagram.

Use this mode especially for:
- event teasers;
- transitions;
- recap atmosphere;
- concept art that should sit behind or beside social copy.

### Style behavior

Prefer:
- teal-led brand atmosphere;
- optional purple or yellow/gold accent selected from the current semantic palette;
- luminous or translucent forms;
- soft glow, haze or gradient depth;
- one focal object or gesture;
- enough calm negative space for downstream text placement.

If real people are present in supplied photography, do not fabricate identities or event facts.

### Avoid

Avoid:
- unrelated sci-fi imagery;
- excessive neon;
- multiple focal objects;
- text baked into the image unless explicitly requested;
- images that compete with the downstream copy.

## Brand color behavior

Use the design-system tokens as the source of truth.

Anchor colors include:
- teal `#0095AC`;
- deep teal `#016462`;
- ink `#10201F`;
- bright teal `#72ECE7`;
- default semantic purple `#954BBC`;
- optional semantic yellow `#FBBF45`.

Do not use every color in one image.

The current accent choice is semantic, not a separate brand.

## Text inside generated images

Default to little or no text.

When text is necessary:
- keep it to short labels, 1–4 words where possible;
- use exact wording supplied by the brief when factual precision matters;
- do not generate paragraphs inside the image;
- leave final long-form copy to the downstream artifact.

If the image generator is unreliable at typography, generate the visual without critical text and let the downstream layout layer add it.

## Factual and source boundaries

Custom visuals may simplify a concept but must not change its meaning.

Do not:
- invent statistics;
- imply research certainty that the brief does not support;
- invent event outcomes;
- invent people, roles or identities as factual depictions;
- turn an illustrative example into a real case;
- add partner logos or claims that were not supplied.

Illustrative scenes must remain visibly illustrative when there is a risk they could be interpreted as factual documentation.

## Complexity levels

### very-simple
- one visual idea;
- few shapes;
- minimal labels;
- generous whitespace;
- suitable for social slides.

### medium
- one main idea plus a few supporting relationships;
- moderate annotation;
- still readable at mobile size.

### detailed
- only when the content genuinely requires it;
- preserve one dominant visual hierarchy;
- do not use detail as decoration.

Default to `very-simple` for social unless the brief clearly needs more.

## Output behavior

If the runtime has an image-generation tool, generate the image directly.

If direct image generation is unavailable, produce a concise generation brief containing:
- selected visual mode;
- complexity;
- tone;
- composition;
- required objects/relationships;
- palette direction;
- text to include, if any;
- explicit negative constraints.

Do not output a long creative essay.

## Bundled examples

When a concrete visual reference would materially help, consult `../../docs/EXAMPLES.md` and at most 1–2 relevant examples under `../../generated-examples/visuals/`.

Use bundled examples to understand:

- how an abstract idea can become a visual structure;
- how visual mode, complexity and tone affect the result;
- how much text is appropriate inside the image;
- the expected quality bar for Innovation Labs custom visuals;
- how different explanatory patterns can still remain recognizably Innovation Labs.

Examples are references, not templates.

Do not mechanically copy their characters, metaphors, labels, wording, facts, layout or composition into a new visual.

Do not assume that a previous visual mode is the right one for the current task. Choose the mode that best fits the current idea unless the human has already selected one.

Current source material, the current request, human-selected controls and the current skill rules always take priority.

## Handoff

The normal social flow is:

`content-planner` → human selection → `insta-post-maker` → `brand-image-maker` → `insta-post-maker`

`brand-image-maker` owns the custom image.

`insta-post-maker` still owns:
- slide sequencing;
- final copy;
- typography;
- layout;
- logo placement;
- integration of the generated image into the final social artifact.

## Done checklist

- [ ] The image communicates one clear idea
- [ ] Human-selected mode / complexity / tone were respected
- [ ] The visual follows IL color behavior
- [ ] Text inside the image is minimal
- [ ] No unsupported facts were introduced
- [ ] The image supports the downstream artifact instead of competing with it
- [ ] Hand-drawn output is actually sketch-like when that mode is selected
- [ ] Narrative output uses a meaningful scene/metaphor rather than decoration
- [ ] Event-glow output preserves usable negative space
