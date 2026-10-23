---
name: insta-post-maker
description: Create simple, shareable Innovation Labs social assets using photo-led, graphic or custom-illustration art direction while preserving approved content boundaries.
version: 0.5.1
---

# Innovation Labs Insta Post Maker

Use when the user wants Innovation Labs social output for Instagram: carousels, feed posts, stories, recaps, teasers, announcements or a lightweight animated concept.

Scope: this skill owns static Instagram posts, carousels, static Stories and lightweight motion concepts for static assets. For a finished vertical short-form video or Instagram Reel, use reels-maker instead. Choose by requested output, not by topic: announcements and lessons may be static or video.

The output must feel editorial, human, recognizably IL and social-native. It should not feel like a Strategy Hub card resized for Instagram or a generic Canva conference template.

## Read first

1. Read `../../design-system/INNOVATION_LABS_DESIGN_SYSTEM.md`.
2. Read `../../design-system/TOKENS.css`.
3. Read `../../design-system/BRAND_ELEMENTS.md`.
4. Ground every factual claim in the user's supplied material. Never invent names, quotes, winners, numbers or outcomes.
5. Study `references/social-2026/` for composition behavior, not literal layouts.
6. If `brand-elements` is selected, treat it as a modifier for accent, branded ground and official shared assets.

## Core goal

Generate social assets that are:
- visually on-brand;
- highly readable on mobile;
- photo-aware when real event images exist;
- art-directed rather than template-heavy;
- varied frame-to-frame but coherent as one story.

## Supported outputs

### Carousel
Usually 4–10 frames. Use more frames when that lets each frame stay simpler.
- frame 1: strongest hook / cover;
- middle: narrative progression, not unrelated cards;
- final: closing message / CTA.

A longer carousel with one clear thought per frame is better than compressing several hierarchy levels into fewer text-heavy frames.

### Stories
Usually 3–6 frames.
- each frame works alone;
- the sequence still reads as one story;
- preserve platform safe zones.

### Single post
One strong message and one clear visual idea.

### Lightweight motion concept
Only when explicitly requested.
- simple loop or moving accent;
- preserve readability and reduced-motion behavior;
- do not promise MP4/MOV/WebM export unless the active runtime explicitly supports it.

## Three visual families

Choose the family that best serves the source and message. Do not force multiple families into one asset without a reason.

### A. Event / photo-led social

Use when the user supplies real event/community photography.

Preferred treatments:
1. **Full-photo overlay** — photo fills most/all of the frame; text sits on a naturally calm area or over a local tint/scrim.
2. **Photo-to-teal blend** — photograph fades/feathers into a teal or deep-teal field; text sits in the color zone or transition.
3. **Teal-led editorial crop** — teal is the ground, but the photo is intentionally cropped/masked/blended into the composition rather than pasted in a hard rectangle.
4. **Photo + one motif** — one approved element or social mascot supports the concept without covering faces/emotion.

A hard photo rectangle + separate teal block may be used occasionally when the composition calls for it, but it must **not** become the repeated default across a carousel.

### B. Campaign / graphic social

Use when there are no meaningful photos, when the source is an announcement/update, or when the user explicitly asks for a template gradient/background.

Preferred structure:
- one approved ground from `../../assets/backgrounds/` or a CSS branded-ground token;
- primary/white logo placed in a corner according to contrast;
- one short message;
- usually one official SVG from `../../assets/brand-elements/` at the edge or as a focal object;
- purple default accent or yellow when requested/selected.

Text should sit in the calm portion of the template ground. Do not cover the entire background with additional cards.

### C. Custom illustration / diagram social

Use when a diagram, sketch, metaphor or simple generated scene can explain the idea faster than another block of copy.

When `brand-image-maker` is available or selected, use it as the custom-image generation layer rather than duplicating detailed illustration logic here.

Good uses:
- hand-drawn process or concept sketch;
- sticky-note / workshop schema;
- simple narrative scene;
- symbolic explanatory illustration;
- event-glow concept image.

Prefer illustration when it **replaces explanatory copy**, not when it only decorates an already dense slide.

Human-selected visual mode, complexity or tone are authoritative. If those are not supplied, choose the lightest visual treatment that communicates the idea.

## Content density and slide simplicity

Prefer **one primary message per frame**.

Do not default to the repeated pattern:
- small eyebrow / kicker;
- large headline;
- explanatory paragraph.

That structure may be used when it genuinely helps, but it must not become the automatic layout for every frame. In many cases the better solution is just one sentence, one question, one drawing, one comparison or one short label attached to a custom image.

Eyebrows / kickers are optional, not mandatory. If a frame already works without one, omit it. Do not add a mono kicker simply because the system knows how to.

When a frame contains both a strong statement and a substantial explanation, prefer splitting them across multiple carousel frames.

Good social frames often need only one of these:
- one strong sentence;
- one short question;
- one diagram plus a short label;
- one image plus a short line;
- one simple list or checklist.

Avoid turning every idea into a mini article.

If a custom visual can carry the explanation, let the image do the work and reduce the copy.

For hand-drawn carousel directions, favor slide types such as:
- one sketched comparison;
- one sticky note plus one arrow;
- one circled question;
- one simple process doodle;
- one named concept with a hand-drawn annotation;
- one illustrative before/after or thin-input / rich-input contrast.

A good hand-drawn sequence should feel varied, not like the same template with different words.

## Evidence, opinions and caveat prominence

Preserve factual boundaries from an approved content brief, but do **not** automatically turn every source limitation into a prominent visual disclaimer.

When the brief classifies caveats:
- **Content-critical caveat** → keep it visibly attached to the claim when removing it would make the post misleading.
- **Source / evidence note** → preserve it, but it may live in the caption, final frame or a quiet source note.
- **Internal planning note** → use it as a generation guardrail; do not automatically surface it as public copy.

If the brief does not classify a limitation, use the same principle: the more the limitation changes the meaning of the claim, the more visible it should be.

The post may take a clear editorial position or have a point of view. Do not weaken every statement with defensive language when the approved brief supports a stronger, plain-language framing.

Still do not:
- turn correlation into causation;
- present a proposal as already implemented;
- present practitioner evidence as peer-reviewed science;
- invent certainty, facts or outcomes.

Avoid large labels such as “HONESTY NOTE” by default. Evidence attribution can be visually quiet when it is not the main point.

## Photo-grounded factuality

Photography may guide composition and visible-detail descriptions, but it must not be used to infer unsupported event facts.

Do not infer or state:
- the exact venue or location from architecture, filenames or visual resemblance;
- attendee roles or identities unless supplied in the brief/materials;
- winners, outcomes or what participants are seeking unless explicitly supported;
- names, affiliations or relationships from appearance alone.

Visible details may be described when unambiguous. If a fact is not explicitly supplied and is not plainly readable in the material, use neutral wording.

## Photo integration rules

Photos must feel part of the composition, not dropped in.

Allowed transitions:
- side fade into teal;
- top/bottom fade into teal;
- teal-to-transparent overlay;
- feathered/organic mask;
- subtle vignette into the brand field;
- local blur + tint behind text;
- controlled crop that follows the subject.

Protect:
- faces;
- hands/objects carrying the emotional moment;
- stage/demo focal point;
- readable branding already visible in the photo where relevant.

Do not force every photograph into the same crop or layout.

## Text directly on photography

Allowed when contrast is strong enough.

Use:
- white or teal/ink text on calm areas;
- a subtle local dark/teal overlay when necessary;
- Poppins for the main line;
- IBM Plex Mono for small kickers;
- one Caveat phrase for human emphasis when it genuinely helps.

Avoid:
- long paragraphs;
- placing text over faces;
- multiple handwritten phrases;
- adding a separate card just because text exists.

## Social color behavior

Default event social is **teal-led Light mode**, not white-first.

Prefer:
- teal / deep teal as dominant fields;
- pale teal/cyan for breathing room;
- white for contrast and type;
- semantic accent (`ax`) sparingly;
- lilac/purple atmosphere only when it supports the reference language.

Campaign social may use blue, green, purple, yellow or classic approved background families through `brand-elements`.

## Shared official assets

Shared v0.4 SVG elements live in:

`../../assets/brand-elements/`

Examples include:
- bulb/glass/bulb-mesh;
- hourglass-bulb variants;
- `make-it-real`;
- registration motifs;
- frame/ring meshes;
- stars/flask;
- gold hex elements.

Use the actual bundled SVG when appropriate rather than recreating it.

Default: **0–1 major shared element per frame**.

## Custom image handoff

When a slide needs a custom explanatory visual, hand the visual brief to `brand-image-maker`.

Pass only what the image layer needs:
- core idea;
- what must be shown;
- factual boundaries;
- intended aspect ratio;
- optional human-selected visual mode / complexity / tone.

`brand-image-maker` owns the generated image. `insta-post-maker` owns how that image is cropped, placed, paired with copy and sequenced inside the carousel.

For social, default custom-image complexity to `very-simple` unless the content requires more.

When the chosen mode is `handdrawn-diagram`, sequence the carousel so the sketch language evolves slide to slide. Do not keep reusing the same sticky-note board, the same title block or the same diagram primitive across the whole set if a simpler or clearer variation would work better.

If one frame introduces a named concept (for example a term such as `context engineering`), keep that frame in the same hand-drawn family as the surrounding slides unless the human explicitly asks for a deliberate visual break.

## Social-only mascot assets

Social-specific assets live in:

`assets/brand-elements/`

Preferred social-only mascots:
- `flying-pig.png`
- `flying-purple-pig.png`

Use them for playful possibility, community, daring/absurdity or a deliberately light moment. Do not use a pig randomly because it is available.

The other PNGs currently present in this local folder are legacy raster compatibility assets. Prefer the shared v0.4 SVG equivalents in `../../assets/brand-elements/` when an equivalent exists.

## Static mesh vs playable network

- Social may use approved **static** template mesh/terrain/backgrounds.
- Social may use static official mesh SVGs as decorative elements.
- The interactive/playable network belongs to `presentation-maker` only.
- Website/Strategy Route maps remain decorative-mesh-free.

## Typography

Use:
- Poppins for display/body;
- IBM Plex Mono for metadata/kickers;
- Caveat for one selective human aside.

Social may be more expressive than other IL formats:
- oversized type;
- filled + outline word combinations;
- controlled crop/overlap;
- asymmetrical placement;
- strong negative space.

Do not apply a different typographic gimmick to every word.

## Logo

Use the bundled 2027 logo.
- primary logo on light/pastel grounds;
- white logo on dark/teal grounds;
- place at a corner with adequate clear space;
- on photography, use only where contrast is controlled by a calm overlay/field.

Do not repeat multiple logos in one frame unless the source explicitly requires partner logos.

## Event recap narrative

When several event photos are supplied, build a visual story such as:
1. atmosphere / cover;
2. people / community;
3. action / stage / demo;
4. memorable detail;
5. closing / CTA.

Choose the strongest emotional image for the cover when possible. Do not use photos merely in upload order.

## Carousel rules

- one primary idea per frame;
- frame 1 strongest hook;
- final frame closes the story;
- split dense material instead of stacking several text hierarchies on one frame;
- use more frames when simplification improves comprehension;
- composition can vary across frames;
- keep one palette/accent/type rhythm;
- do not force all slides onto the exact same ground;
- illustration may carry the explanation on selected frames;
- maintain recognizably shared art direction.

## Story rules

- big type, short copy;
- preserve top/bottom safe zones;
- photo-led is encouraged for event content;
- a story may be more immediate and less card-like than a feed carousel.

## Decision logic

Decide in this order:

1. What is the job? recap / teaser / announcement / quote / community / campaign.
2. Are strong real photos supplied?
   - yes → default to event/photo-led family;
   - no → campaign/graphic family is often better.
3. What format best serves it? single / carousel / stories.
4. Which photo or message leads?
5. Can the idea be understood faster through a custom diagram or illustration than through more copy?
6. Does a brand element add meaning?
7. Is the default purple accent right, or has yellow/another approved ground been requested?

## What to avoid

Avoid:
- repeated photo rectangle + color block on every frame;
- a plain white generic default when teal/photo integration would be stronger;
- floating tiny photos;
- too many logos;
- multiple major motifs in one frame;
- mesh everywhere;
- unreadable copy over busy photography;
- corporate brochure tone;
- generic startup social templates;
- repeating eyebrow + headline + paragraph on every frame;
- oversized evidence disclaimers when a quiet note would preserve accuracy;
- turning every source note into a framed “honesty” box;
- custom illustration used as decoration without explanatory value;
- invented facts/quotes/results;
- using every available asset because it exists.

## References

Study:

`references/social-2026/`

The references demonstrate multiple valid behaviors:
- graphic/mesh + translucent object composition;
- full-photo text overlay;
- handwritten emphasis;
- minimal branding on event photography.

Extract the visual behavior. Do not copy their exact copy or layout.

## Bundled examples

When a concrete social reference would materially help, consult `../../docs/EXAMPLES.md` and at most 1–2 relevant examples under `../../generated-examples/social/`.

Use bundled examples to understand:

- the relationship between prompt, brief and final carousel;
- the expected quality bar;
- one-primary-thought-per-frame pacing;
- how custom visuals can carry part of the explanation;
- how multiple frames can vary without losing coherence.

Examples are references, not templates.

Do not mechanically copy their wording, facts, claims, URLs, frame sequence, visual metaphors or composition into a new post.

Do not assume every Innovation Labs social post should use hand-drawn diagrams. Choose the visual treatment that best fits the current content, source material and available photography.

When an archived `brief.md` exists, it may be inspected to understand the downstream content structure. Do not assume or claim that the brief was generated by `content-planner` unless provenance explicitly establishes that.

Current source material, the current request and the current skill rules always take priority.

## Default recipes

### If event photos are supplied
- output: carousel unless another format is requested;
- palette: teal-led Light;
- visual family: photo overlay / photo-to-teal blend / editorial crop;
- type: strong Poppins + small mono kicker + optional one Caveat phrase;
- motif: zero or one meaningful element;
- CTA on final frame.

### If no photos are supplied
- output: carousel/single according to content;
- visual family: approved template ground;
- one semantic accent;
- one message per frame;
- consider `brand-image-maker` when a hand-drawn or narrative visual can replace explanatory copy;
- logo at a corner;
- usually one official SVG element;
- body reading content stays off the decorative edge areas.
