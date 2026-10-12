---
name: insta-post-maker
description: Create Innovation Labs Instagram carousels, stories and social posts using photo-led event art direction or approved campaign grounds and brand elements.
version: 0.4.0
---

# Innovation Labs Insta Post Maker

Use when the user wants Innovation Labs social output for Instagram: carousels, feed posts, stories, recaps, teasers, announcements or a lightweight animated concept.

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
Usually 3–8 frames.
- frame 1: strongest hook / cover;
- middle: narrative progression, not unrelated cards;
- final: closing message / CTA.

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

## Two visual families

Choose between these based on the source. Do not force both into every asset.

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

- one idea per frame;
- frame 1 strongest hook;
- final frame closes the story;
- composition can vary across frames;
- keep one palette/accent/type rhythm;
- do not force all slides onto the exact same ground;
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
5. Does a brand element add meaning?
6. Is the default purple accent right, or has yellow/another approved ground been requested?

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
- logo at a corner;
- usually one official SVG element;
- body reading content stays off the decorative edge areas.
