# Test matrix — v0.4

Run each test in a fresh chat. First test with only the plugin installed; then repeat core tests with the native Innovation Labs Design System selected. Both should remain recognizably the same brand.

| Test | Prompt intent | Expected skill(s) | Pass if |
|---|---|---|---|
| Website / Hub | “Turn this strategy into an Innovation Labs Strategy Hub.” | website-maker | Source-grounded; shared internal stop model drives full map + mini-map; calm serpentine route; no generic Open Threads; responsive vertical journey on phone |
| Route deck | “Make a route-first presentation from this strategy and link to the Hub.” | presentation-maker | Route overview comes first when the source supports it; later slides retain route context; pitchy; phone portrait/landscape adapt; final Hub path |
| Yellow deck | “Same deck, yellow accent.” | presentation-maker + brand-elements | Structure unchanged; semantic accent swaps coherently; dark text on yellow fills; no random recoloring |
| Presentation mesh | “Use the interactive network on the community transition.” | presentation-maker | Playable network is selective, readable and presentation-only; reduced-motion respected |
| One-pager | “Make a one-page partner brief.” | one-pager-maker + formal-lens | Exactly one page; strong hierarchy; no invented facts; optional controlled brand header/band |
| Event social | “Turn these Demo Day photos into a 5-card recap carousel.” | insta-post-maker | Photo-first; photo-to-teal blend / overlay used intentionally; people remain focal; no repeated photo-card template; source-faithful |
| Campaign social | “Turn this update into a 5-card carousel on the green gradient.” | insta-post-maker + brand-elements | Approved background family, one message/frame, one major element/frame max, coherent logo placement and accent |
| Story sequence | “Create 4 connected event stories from these photos.” | insta-post-maker | Safe zones; concise overlays; varied but coherent photo integration; people not obscured |
| Brand element modifier | “Use a yellow accent and an appropriate official element.” | brand-elements + one output skill | Selects a meaningful asset/ground; does not change facts or information architecture; no decorative pile-up |
| Lens isolation | “Rewrite only the tone; do not redesign.” | one lens | Content facts and visual brief remain unchanged |

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
