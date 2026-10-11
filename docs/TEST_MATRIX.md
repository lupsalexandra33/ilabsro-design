# Test matrix

Run each test in a fresh chat. First test with only the plugin installed; then repeat with the native Innovation Labs Design System selected. Both should remain recognizably the same brand.

| Test | Prompt intent | Expected skill(s) | Pass if |
|---|---|---|---|
| Website | “Turn this strategy into an Innovation Labs Strategy Hub.” | website-maker | Hub is source-grounded; desktop map is a connected serpentine route with numbered stops and alternating labels; no generic Open Threads section; themes coherent |
| Presentation | “Make this strategy into a catchy 7-slide presentation and link to the Hub.” | presentation-maker | Pitchy sequence, optional mesh only in slides, CTA to Hub |
| One-pager | “Make a partner one-pager from this strategy.” | one-pager-maker + formal-lens | One clear page, strong hierarchy, no invented facts |
| Friendly one-pager | “Make a founder-facing one-pager; friendly, not corporate.” | one-pager-maker + friendly-lens | Same design system, warmer copy |
| Social | “Turn this update into a 5-card Instagram carousel.” | insta-post-maker | Source-faithful, 4:5 cards, readable hierarchy |
| Lens isolation | “Rewrite only the tone; do not redesign.” | one lens | Content and visual brief remain unchanged |

### Failure diagnosis

- Wrong visual identity → fix native Design System / fallback design spec.
- Right brand, wrong format → fix output skill.
- Map is calm but composition drifts from the approved route → fix `map-proposal-pattern.md`, not the global design system.
- Generic `Open Threads` section appears → strengthen website content-architecture guardrails.
- Right format, wrong voice → fix lens.
- Invented facts/quotes → strengthen source rules in relevant output skill.


### Portability test

Disable/unselect the native Design System and repeat Website, Presentation and One-pager tests. Pass only if the bundled Markdown + tokens produce the same core identity and format rules.
