---
name: human-pass
description: Final copy and design check for Innovation Labs output. Strips AI fingerprints, flags IL voice rules and scans pages for visual AI tells. Use before showing any draft.
version: 0.1.0
---

# Innovation Labs Human Pass

A copy-cleaning layer, like the voice lenses: it never changes facts, structure or visual direction. Every output maker (`reels-maker`, `insta-post-maker`, `website-maker`, `one-pager-maker`, `presentation-maker`) should run its final English copy through it before showing a draft for review.

The scripts are adapted from Jake Schincariol's MIT-licensed `instagram-agent-skill` (`ig-human`), with an added Innovation Labs block. License: `scripts/LICENSE-instagram-agent-skill.txt`.

```bash
python3 scripts/humanize.py draft.txt --report -o clean.txt   # fix what is mechanical, flag what needs judgment
python3 scripts/detect.py draft.txt clean.txt                 # five-signal score, before vs after
```

```bash
python3 scripts/design_tells.py output.html [folder ...]   # visual AI tells in HTML/CSS/SVG (design-system/AI_TELLS.md)
```

Python 3 standard library only. No network, nothing uploaded. Mark a deliberate, human-approved exception on its line with an `il-allow-tell` comment (for example, a deliberately bad example that the artifact strikes out).

## What it does

**Fixes automatically:** invisible Unicode characters, em dashes and curly quotes, and the stock-phrase lexicon in `scripts/slop.json`. The `il-hype` entries come from the IL voice rules ("we're thrilled to announce", "revolutionary", "next-level", "don't miss out"...).

**Flags for a human rewrite** (never auto-rewritten, because the shape of a sentence needs judgment):
- the generic tells: "It's not just X, it's Y", rule-of-three triads, one-word rhetorical questions, emoji bullets, hashtag walls, follow/tag bait;
- the IL voice rules from `design-system/INNOVATION_LABS_DESIGN_SYSTEM.md`:
  - `il-exclamation`: no exclamation marks;
  - `il-emoji`: no emoji in copy (a reaction inside a designed chat bubble is a visual element, not copy);
  - `il-title-case`: sentence case everywhere except proper nouns;
  - `il-hype-claim`: "proven to", "guaranteed", "the only way", "100%". Check the source and keep the claim at the strength the evidence supports.

Rewrite every flagged line yourself, keeping the meaning, then run it again.

## How to read the score (important)

`detect.py` scores burstiness, specificity, slop density, fingerprint and voice. It was built for captions and longer prose.

- **Captions, posts, page copy (roughly 60+ words):** aim for PASS (70+, no check under 55). Two rounds is normal. **Exception, found in testing:** when the approved source has no numbers, names or concrete details, SPECIFICITY reads 0 and the 40% weakest-check weight keeps the verdict at FLAGGED however good the prose is. In that case, accept it when every *other* check is 55+ and there are zero lexicon hits and zero structural flags, and write `SPECIFICITY 0: source has no concrete detail; none invented` in the review notes.
- **Reel on-screen text and carousel frames:** short, evenly sized lines are correct design for a phone screen, so BURSTINESS and VOICE will read low on purpose. For this copy the gate is **`humanize.py` reporting zero lexicon hits and zero unresolved structural flags**. Treat the `detect.py` number as information only.
- **SPECIFICITY is worth listening to everywhere.** A low score means there are no concrete markers (numbers, names, real examples). If the approved brief has a real detail, use it. If it doesn't, never invent one to raise the score.

These are local heuristics, not GPTZero, Originality or Turnitin, and they don't call them. Never tell anyone their copy is "undetectable". What makes IL content read as human is real source material, real photos, specific details and a person who approved it. This pass only cleans what is left over.

## Don't run it on

Factual tables, labels, citations, source quotes, names or numbers. Run it on narrative copy after the structure is approved.

## Order of operations

1. Get the final copy: for a Reel, `render.mjs` writes `<name>.onscreen.txt`; for other makers, the visible copy plus the caption.
2. `humanize.py --report`, then apply the mechanical fixes.
3. Rewrite the flagged lines by hand, applying the active lens (`friendly-lens`, `formal-lens` or `jokey-lens`).
4. Run it again. For captions, also run `detect.py before after` and show the delta.
5. Show the human the cleaned copy and the remaining flags, never just a score.

## Editing the lexicon

`scripts/slop.json` is meant to be edited. If IL legitimately uses a word the lexicon strips (for example a program name), remove that entry rather than fighting the tool. Keep new IL-specific entries tagged with `"family": "il-..."` so they stay separate from the upstream list.
