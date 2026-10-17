# Test matrix — v0.5.1

Run each test in a fresh chat. First test with only the plugin installed; then repeat core tests with the native Innovation Labs Design System selected. Both should remain recognizably the same brand.

| Test | Prompt intent | Expected skill(s) | Pass if |
|---|---|---|---|
| Website / Hub | “Turn this strategy into an Innovation Labs Strategy Hub.” | website-maker | Source-grounded; shared internal stop model drives full map + mini-map; calm serpentine route; no generic Open Threads; responsive vertical journey on phone |
| Route deck | “Make a route-first presentation from this strategy and link to the Hub.” | presentation-maker | Route overview comes first when the source supports it; later slides retain route context; pitchy; phone portrait/landscape adapt; final Hub path |
| Yellow deck | “Same deck, yellow accent.” | presentation-maker + brand-elements | Structure unchanged; semantic accent swaps coherently; dark text on yellow fills; no random recoloring |
| Presentation mesh | “Use the interactive network on the community transition.” | presentation-maker | Playable network is selective, readable and presentation-only; reduced-motion respected |
| One-pager | “Make a one-page partner brief.” | one-pager-maker + formal-lens | Exactly one page; strong hierarchy; no invented facts; optional controlled brand header/band |
| Content planning | “Turn this approved strategy into content opportunities.” | content-planner | Max 5 distinct opportunities; exact source traceability; fidelity + distinctness gates; human selection remains explicit |
| Hand-drawn social | “Turn this approved brief into a simple hand-drawn carousel.” | insta-post-maker + brand-image-maker | One primary thought/frame; varied sketch grammar; drawings carry explanation; no generic AI-carousel look; factual boundaries preserved |
| Narrative illustration | “Explain this founder idea as one playful IL scene.” | brand-image-maker | One clear metaphor/scene; recognizably IL; little embedded text; not generic glossy AI art |
| Event social | “Turn these Demo Day photos into a 5-card recap carousel.” | insta-post-maker | Photo-first; photo-to-teal blend / overlay used intentionally; people remain focal; no repeated photo-card template; source-faithful |
| Campaign social | “Turn this update into a 5-card carousel on the green gradient.” | insta-post-maker + brand-elements | Approved background family, one message/frame, one major element/frame max, coherent logo placement and accent |
| Story sequence | “Create 4 connected event stories from these photos.” | insta-post-maker | Safe zones; concise overlays; varied but coherent photo integration; people not obscured |
| Brand element modifier | “Use a yellow accent and an appropriate official element.” | brand-elements + one output skill | Selects a meaningful asset/ground; does not change facts or information architecture; no decorative pile-up |
| Lens isolation | “Rewrite only the tone; do not redesign.” | one lens | Content facts and visual brief remain unchanged |
| First-time-user onboarding | “I have never used this plugin before. Explain how I should use it to make an Innovation Labs social post.” | usage guidance + relevant social skill | Uses bundled usage guidance; explains skills in plain language; gives a sensible first workflow; does not require technical plugin knowledge |
| Bundled-example reference | “Before making this new carousel, inspect one relevant bundled social example and explain what you are learning from it. Do not copy its layout or content.” | insta-post-maker + relevant bundled example | Can access `generated-examples/`; selects a relevant example; distinguishes reference from template; does not inherit facts, claims, URLs or exact composition |

## v0.5.1 distribution checks

### First-time-user onboarding

Run with only the distributed plugin installed.

Prompt:

> I have never used Innovation Labs Design before. Explain how I should use it to make an Innovation Labs social post. Do not create anything yet.

Pass only if Claude:

- can use the bundled usage guidance;
- explains what a skill is in plain language;
- explains that the user may describe the desired outcome without already knowing skill names;
- identifies an appropriate social workflow;
- explains when source material should be supplied;
- does not require access to the development repository.


### Bundled-example access

Run with only the distributed plugin installed.

Prompt:

> Before making this new carousel, inspect one relevant bundled social example and its archived prompt. Explain what you are learning from it without treating it as a template. Do not create the carousel yet. Tell me the exact bundled file paths you successfully read.

Pass only if Claude:

- can access `docs/EXAMPLES.md`;
- can access a relevant path under `generated-examples/social/`;
- can read the example README and archived prompt when available;
- describes the example as a reference rather than a template;
- does not inherit the example's facts, claims, URLs, wording or exact composition;
- can report the actual bundled paths it inspected.


### Distribution boundary

The distributed plugin should be sufficient for the two tests above without bundling the development surfaces.

The runtime package should include:

- `.claude-plugin/`;
- `skills/`;
- `design-system/`;
- `assets/`;
- `generated-examples/`;
- `docs/USAGE.md`;
- `docs/EXAMPLES.md`;
- `README.md`.

It should not require:

- `artifact-index/`;
- `showcase/`;
- `scripts/`;
- Git history;
- access to the full development repository.

## Responsive checks

For generated web/deck artifacts check at least:
- 1440×900 laptop;
- 844×390 phone landscape;
- 390×844 phone portrait.

Pass only if nothing scrolls sideways, controls do not cover content, labels wrap instead of squeezing and the layout scales continuously rather than jumping.

## Failure diagnosis

- Wrong visual identity → fix bundled/native Design System.
- Right brand, wrong format → fix output skill.
- Map becomes decorative/mesh-heavy → fix map rules; brand-elements must not override them.
- Deck is a document pasted into slides → fix `presentation-maker` narrative/route rules.
- Yellow accent has poor contrast → fix accent token usage; never hard-code white text on yellow.
- Event social becomes photo rectangle + teal block repeatedly → fix `insta-post-maker` photo integration rules.
- Campaign social ignores official assets → fix `brand-elements` asset selection/path rules.
- Generic `Open Threads` appears → strengthen website architecture guardrails.
- Invented facts/quotes → strengthen source discipline.

## Portability test

Disable/unselect the native Design System and repeat Website, Route deck, One-pager, Event social and Campaign social. Pass only if bundled Markdown + tokens + assets produce the same core identity and format behavior.
