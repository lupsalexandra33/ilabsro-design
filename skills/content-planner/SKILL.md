---
name: content-planner
description: "Extract and evaluate source-grounded Innovation Labs content opportunities, then turn a human-selected idea and format into a structured downstream brief."
version: "0.1.2-draft"
---

# Innovation Labs Content Planner

A source-first editorial planning skill for Innovation Labs.

Its job is to answer:

**What is worth communicating from the material we already have, and how can we frame it without losing the substance of the source?**

It sits upstream of execution skills such as `insta-post-maker`.

The planner may discover, structure, evaluate and recommend.
The human decides what moves forward and in what format.

## 1. What this skill is for

Use this skill when the user provides one or more approved sources such as:

- strategy documents;
- research notes;
- event scripts;
- program notes;
- reports;
- internal planning material;
- other source documents explicitly supplied for content planning.

The skill has two modes:

1. **PLAN** — extract and evaluate content opportunities.
2. **BRIEF** — turn a human-selected opportunity and format into a source-grounded content brief.

Do not jump directly from raw source material to final social copy or visual execution.

## 2. Rules that outrank everything else

1. **Source fidelity over creativity.** Preserve the meaning, nuance, status and limitations of the source.
2. **No paraphrase inflation.** Do not create several themes that are the same strategic point rewritten in different words.
3. **Traceability is mandatory.** Every retained opportunity must include a source reference and a supporting excerpt in the original wording.
4. **Separate source language from generated framing.** A generated angle must never be presented as if it were original source language. Generated framing may be opinionated or punchy, but it must not strengthen unsupported factual claims.
5. **Human selection stays human.** The AI may recommend ideas and formats; the human chooses what moves forward.
6. **No unsupported completion.** If the source does not support an idea, claim, number, outcome or implication, omit it or flag the gap.
7. **Preserve uncertainty and status.** Proposed, planned, estimated, tentative, correlational, incomplete or disputed material must remain labeled that way.
8. **Fewer strong ideas beat many weak ones.** Return a maximum of 5 final content opportunities per run.
9. **No design decisions.** This skill does not choose colors, typography, layout, image treatment, brand elements or visual composition.
10. **No final publishing copy by default.** The output is planning material and a structured brief for downstream execution.

## 3. PLAN mode

### Step 1 — Read and map the source

Identify the parts of the source that could carry public-facing value.

Look for material such as:

- a strong strategic thesis;
- useful research or evidence;
- an unexpected or counter-intuitive finding;
- a practical framework;
- a lesson from the program;
- a problem worth explaining;
- a decision and the reasoning behind it;
- a useful distinction;
- a strong observation that can stand on its own.

Do not treat every section as content-worthy.

Operational detail, internal logistics or context that only makes sense inside the team should not automatically become a content theme.

### Step 2 — Generate candidate themes

Create candidate themes and possible content angles.

A **theme** is the source-grounded idea worth communicating.

A **content angle** is a possible way to make that theme useful, understandable or interesting to an external audience.

Do not generate duplicate themes from the same strategic point.

Multiple angles from the same strategic point are allowed only when they create genuinely different standalone value.

Every candidate must carry:

- theme;
- content angle;
- source document;
- source section or heading;
- supporting excerpt in the original wording.

If a candidate cannot be traced to a source, drop it.

### Step 3 — Evaluate candidates

Evaluate every candidate before returning it.

Two criteria are mandatory gates.

#### Gate 1 — Source fidelity: PASS / FAIL

PASS only when the proposed theme and angle stay within what the source actually supports.

FAIL when the candidate:

- changes the strategic meaning;
- turns a hypothesis into a fact;
- turns a proposal into a confirmed decision;
- removes an important caveat;
- overstates research;
- introduces an unsupported claim or implication;
- combines separate source ideas into a new claim that the source does not make.

A high quality score can never override a Source fidelity FAIL.

#### Gate 2 — Distinctness: PASS / FAIL

PASS only when the candidate adds a meaningfully different content opportunity.

FAIL when it is substantially the same underlying idea as another candidate with different wording.

When two candidates overlap:

- keep the stronger version;
- merge source references when appropriate;
- or keep multiple angles only when each creates genuinely different standalone audience value.

A high quality score can never override a Distinctness FAIL.

### Step 4 — Score the candidates that pass both gates

Use 1–5 scores.

#### Clarity

How easily can someone outside Innovation Labs understand the idea?

- **1** — depends heavily on internal context or jargon;
- **3** — understandable with a short explanation;
- **5** — immediately understandable without reading the source.

#### Substance / usefulness

Does the idea teach, explain or clarify something meaningful?

- **1** — generic, promotional or empty;
- **3** — useful but familiar or limited;
- **5** — contains a strong insight, framework, evidence point or useful perspective.

#### Save / share potential

Is there a concrete reason someone might save, repost or share it?

- **1** — little reusable or shareable value;
- **3** — relevant to a narrower audience or useful in context;
- **5** — strongly useful, surprising, explanatory, reusable or discussion-worthy.

Do not score something highly merely because it sounds provocative.

#### Standalone value

Can it work as a piece of social content without requiring the audience to know the whole strategy?

- **1** — only understandable inside the original document;
- **3** — works with some framing;
- **5** — can stand on its own while remaining accurate.

### Step 5 — Select the final opportunities

Return at most 5 opportunities.

Only candidates that PASS both mandatory gates may be returned as final opportunities.

Prefer:

- higher substance;
- higher clarity;
- higher save/share potential;
- genuinely distinct ideas;
- themes with strong direct support from the source.

Do not force 5 opportunities if the source only supports fewer strong ones.

## 4. PLAN output contract

For each final opportunity, return:

### Theme
The source-grounded strategic or informational idea.

### Content angle
A possible public-facing framing.

### Why someone would care
One concise sentence explaining the audience value.

Do not use generic wording such as “this is important because AI is changing the world.”

### Exact source excerpt
The shortest sufficient verbatim excerpt that supports the opportunity.

Do not rewrite the excerpt.

### Source section
Document name plus section, heading or another useful source locator.

### Recommended formats
Recommend up to 3 suitable formats, ranked.

Examples:

- carousel;
- single post;
- story sequence;
- short educational post;
- quote-led post;
- short video concept.

For each recommendation, explain in one sentence why the format fits the idea.

The recommendation is advisory only.

### Evaluation
Always show:

- Source fidelity: PASS
- Distinctness: PASS
- Clarity: X/5
- Substance / usefulness: X/5
- Save / share potential: X/5
- Standalone value: X/5

Add a short evaluation rationale when useful.

## 5. Human selection

After PLAN mode, stop before creating the execution brief unless the user has already made a clear selection.

The human selects:

1. which content opportunity moves forward;
2. which format should be used.

The AI may recommend a best-fit format, but it does not silently make the final format decision.

If the human explicitly delegates the format choice to the AI, that counts as human authorization to choose.

If the idea is selected but the format is not, ask for the format selection or present the recommended options for selection.

Do not make visual design decisions at this stage.

## 6. BRIEF mode

Use BRIEF mode only after an opportunity has been selected.

The brief must remain attached to the original source context.

### Brief output

Return:

#### Goal
What the content should help the audience understand, learn, reconsider or remember.

#### Audience
Who the content is primarily for, using supplied context when available.

If the audience is inferred rather than explicitly supplied, label it `Recommended audience` or `Inferred audience`.

Do not invent a narrow audience if the source or user has not defined one.

#### Selected theme
The approved source-grounded theme.

#### Selected angle
The approved content angle.

#### Selected format
The format chosen by the human, or explicitly delegated to the AI.

#### Key message
One concise statement of what the final content must communicate.

It must stay within the source.

#### Why it matters
The audience value, expressed plainly.

#### Source context
Include:

- source document;
- source section;
- exact supporting excerpt;
- any important caveat, status or limitation that must survive execution.

Classify caveats by visibility:

- **Content-critical caveat** — must remain in the public-facing content when removing it would make the claim materially misleading.
- **Source / evidence note** — must remain available to downstream generation, but may live in a caption, closing slide or quiet source note rather than dominate the visual.
- **Internal planning note** — constrains generation but should not automatically become public-facing copy.

Do not convert every source limitation into a prominent disclaimer. Preserve accuracy, then match the public prominence of the caveat to how much it changes the meaning of the claim.

#### Content requirements
List the information that must be retained in the final content.

#### Content boundaries
List claims, interpretations or implications the downstream skill must not introduce.

#### Suggested structure
Provide a lightweight information structure appropriate to the selected format.

Examples:

For a carousel:
- opening idea;
- explanation;
- evidence/example;
- implication;
- closing takeaway.

For a single post:
- hook;
- core point;
- support;
- takeaway.

This is information architecture, not visual design.

#### Handoff note
State that downstream generation must preserve the approved message, source context and factual boundaries. Also carry forward the caveat visibility class so downstream execution knows what must be prominent, what may be quiet, and what is internal-only.

## 7. Handoff to downstream skills

`content-planner` should produce a stable brief that another skill can consume.

For social execution, the normal handoff is:

`content-planner` -> human approval -> `insta-post-maker` (static)
                                    -> `reels-maker` (video MP4)

For Reel handoff, provide the approved angle, key point, intended audience, verified source details, caveats, CTA constraints and any approved photos or footage. Let reels-maker select the time-based narrative, copy lens, scene construction, motion, official branding and final MP4 export. An explicit direct user request for a Reel with a sufficient brief does not need an additional planning approval step.

The downstream skill owns:

- final social copy;
- visual hierarchy;
- layout;
- typography;
- colors;
- photography treatment;
- brand elements;
- composition;
- export-ready social assets.

The downstream skill must not silently reinterpret the approved strategic message.

The planner does not need to call or depend on `insta-post-maker` directly. Orchestration may happen through the user prompt, an agent, a workflow or a future application.

## 8. Source handling rules

### Strategy

Preserve strategic wording when the wording carries meaning.

Do not turn internal strategy into polished external claims unless the source supports that transformation.

### Research

Do not convert a research finding into an Innovation Labs position unless the source explicitly makes that connection.

Preserve limitations such as:

- early evidence;
- correlational findings;
- conflicting studies;
- uncertain transfer;
- small samples;
- estimates;
- unvalidated hypotheses.

Preserving a limitation does not mean it must become a large visual disclaimer. Classify it by whether it is content-critical, an evidence note, or an internal planning note.

### Event scripts and program notes

Use them as factual and narrative sources only to the extent they support the proposed content.

Do not infer:

- attendee identities or roles;
- outcomes;
- winners;
- relationships;
- unsupported event facts.

### Conflicting sources

If supplied sources conflict, do not silently reconcile them.

Flag the conflict and keep the affected opportunity out of the final list unless a source priority has been provided.

## 9. Failure and revision behavior

Drop or flag a candidate when:

- source support is missing;
- the source is too ambiguous;
- it duplicates another candidate;
- the angle requires overstating the source;
- the idea only becomes interesting after inventing a stronger claim;
- it is understandable only with large amounts of internal context.

When a candidate is weak but recoverable, revise the **angle**, not the underlying source meaning.

If revision cannot improve it without changing the source, discard it.

## 10. What this skill must not do

- Do not make visual design decisions.
- Do not create final social assets.
- Do not generate many paraphrases to simulate variety.
- Do not prioritize virality over accuracy.
- Do not turn uncertainty into certainty.
- Do not fabricate facts, quotes, statistics or examples.
- Do not silently merge unrelated strategic ideas.
- Do not select the final idea for the human.
- Do not select the final format for the human unless explicitly delegated.
- Do not publish or schedule content.
- Do not require Notion, n8n, Make or any production integration to work.

## Bundled examples

When a concrete downstream brief reference would materially help, consult `../../docs/EXAMPLES.md`.

The bundled examples are primarily execution references. They must not be treated as proof that `content-planner` created a specific historical brief unless provenance explicitly establishes that.

A relevant documented brief currently exists at:

`../../generated-examples/social/context-engineering/brief.md`

It may be inspected as an example of a downstream content brief structure.

Do not claim that this brief was generated by `content-planner`.

Use it only to understand qualities such as:

- a clear goal;
- an explicit audience;
- a selected theme and angle;
- a concise key message;
- source-aware boundaries;
- useful downstream structure.

Do not copy its topic, wording, claims, audience assumptions or content framing into a new brief.

For PLAN mode, current source material remains the primary evidence. Do not use generated examples as source material for new content opportunities unless the user explicitly provides them as sources.

For BRIEF mode, the current human-selected opportunity, selected format and source traceability always take priority over any bundled example.

## 11. Minimal MVP workflow

The smallest useful workflow is:

1. User supplies approved source material.
2. PLAN mode extracts candidate themes and angles.
3. Candidates are evaluated.
4. At most 5 gate-passing opportunities are returned.
5. Human selects an opportunity.
6. Human selects a format, or explicitly delegates the choice.
7. BRIEF mode creates the source-grounded content brief.
8. The brief is handed to a downstream execution skill.
9. Human reviews the resulting draft.

The MVP stops before publishing automation.

## 12. Done checklist

### PLAN
- [ ] Final output contains no more than 5 opportunities
- [ ] Every opportunity has an exact source excerpt
- [ ] Every opportunity has a useful source locator
- [ ] Every opportunity PASSES Source fidelity
- [ ] Every opportunity PASSES Distinctness
- [ ] Clarity is scored 1–5
- [ ] Substance / usefulness is scored 1–5
- [ ] Save / share potential is scored 1–5
- [ ] Standalone value is scored 1–5
- [ ] Recommended formats include a reason
- [ ] Source language and generated framing are distinguishable
- [ ] Important uncertainty / proposal status is preserved
- [ ] Caveats are classified by public-visibility importance
- [ ] No visual design decisions are made

### BRIEF
- [ ] Human-selected idea is explicit
- [ ] Human-selected or explicitly delegated format is explicit
- [ ] Exact source excerpt is carried forward unchanged
- [ ] Inferred audience is labeled as inferred/recommended
- [ ] Key message stays within the source
- [ ] Content requirements and boundaries are explicit
- [ ] Suggested structure is informational, not visual
- [ ] Brief is usable by a downstream execution skill
- [ ] No final publishing action is taken
