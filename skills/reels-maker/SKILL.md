---
name: reels-maker
description: Create educational and promotional Innovation Labs Instagram Reels as review-ready 9:16 MP4s, using hook-first storytelling, text-on-screen, human-first motion and teal-led branding.
version: 0.7.0
---

# Innovation Labs Reels Maker

Use when the user wants an Innovation Labs Instagram Reel, vertical short-form video, educational explainer, announcement, teaser, invitation, program reminder, founder lesson or source-grounded video recap.

**Default deliverable: a finished, review-ready 9:16 MP4**, not just a script, storyboard or animated mockup. The Reel must communicate with **text on screen**, without voiceover. A successful export is not sufficient: the finished video must also meet the creative and visual quality criteria below.

This skill belongs to the same family as `insta-post-maker`, `content-planner`, `brand-image-maker`, `brand-elements` and the existing voice lenses. It owns **time-based storytelling, animation and video production**, while `insta-post-maker` owns static posts, carousels and static Stories. For motion-heavy Stories, this skill may be used with Story-specific delivery constraints.

Do not turn this into a two-template Reel generator. **Chat and handwritten are preferred creative directions, not the only possible outputs.** Choose whichever concept makes a specific idea clearer, more interesting and more recognizably Innovation Labs.

## Read first

1. Read `../../design-system/INNOVATION_LABS_DESIGN_SYSTEM.md` for brand identity, principles, copy, typography and logo rules.
2. Read `../../design-system/TOKENS.css` for exact Light-mode color tokens and contrast constraints.
3. Read `../../design-system/BRAND_ELEMENTS.md` for official shared assets and their appropriate use.
   Read `../../design-system/AI_TELLS.md`: the patterns Innovation Labs never ships (generic icon tiles, emoji, glassmorphism, em dashes, Inter/Geist/Space Grotesk, three feature cards, bento grids, fake terminals, "it's not X, it's Y", placeholder demos, purple-on-black, glow orbs, dot grids, sparkles, arrow-nudge CTAs, big hover motion, rainbow color). Before delivering, run `python3 ../human-pass/scripts/design_tells.py <output>` and fix every finding that isn't a documented IL exception.
4. Read the relevant voice modifier when needed: `../friendly-lens/SKILL.md`, `../formal-lens/SKILL.md` or `../jokey-lens/SKILL.md`.
5. If the brief comes from `content-planner`, preserve approved angle, audience, evidence limits, claims and CTA. If the user asks directly for a Reel and provides a usable topic, proceed without forcing a separate planning step.
6. If the user provides a visual reference, analyze its composition, timing, scene construction and animation behavior. Adapt those mechanics into the IL design system; **do not copy its off-brand palette, typography, UI or unsupported claims**.

## Core goal

Make short videos that:
- teach a useful founder/innovation concept **or** communicate a real Innovation Labs update;
- earn attention with a specific hook visible immediately;
- feel editorial, human, intentionally animated and native to social video;
- look like Innovation Labs, especially through the Light teal palette and real branded assets;
- work without audio and remain easy to read on a phone;
- progress visually, rather than displaying a series of static social cards with entrance effects;
- close with a consistent, polished Innovation Labs signature;
- are actually rendered, inspected and ready for **human review**, never silently published.

**Creative quality outranks an easy export.** Never select a crude compositor, auto-slideshow or generic animated template merely because it can output MP4. Select a production path capable of the requested visual treatment. If the active environment cannot reach a review-worthy result, report the specific limitation rather than presenting an ugly technical proof as final work.

## Content and creative decisions

Choose in this order:

1. **Purpose:** teach, explain, challenge an assumption, invite, announce, remind, recap, showcase or promote an Innovation Labs activity.
2. **Single takeaway:** what should the viewer understand, remember or do when the Reel ends?
3. **Hook:** a concrete curiosity gap, counterintuitive observation, practical problem, recognizable founder tension, useful promise or verified timely update.
4. **Narrative mechanism:** conversation, handwritten explanation, drawing/diagram reveal, wrong-way/right-way, before/after, myth/reality, mistake/fix, progressive checklist, real-photo/video-led story, simple visual metaphor or another suitable mechanism.
5. **Voice lens, timing and visual treatment.** User-selected mode, tone or reference takes precedence over an automatic choice.

Default: **educational → consider handwritten/notebook teaching first**; **announcements/teasers → consider a natural chat or direct announcement first**. Neither is mandatory. A factual date announcement may need direct clarity rather than dialogue. A process lesson may need a changing diagram rather than handwriting. A real event recap may be better with actual footage than graphics.

Be creatively flexible, but not arbitrary: every visual device must help attention, comprehension or brand recognition.

### Screen-first narrative

- **Opening frame = hook.** No brand-intro animation, generic welcome, empty lead-in, throat-clearing or delayed title. The hook must be readable and interesting from the first visible moment.
- **Build:** develop one clear idea through distinct visual beats. Introduce information only when the viewer needs it.
- **Payoff:** show a meaningful answer, correction, actionable lesson, specific announcement or clear next step. The final teaching frame must have a conclusion, not stop mid-list.
- **Signature:** end with a short branded closing scene using official IL assets; a content-appropriate CTA is optional.

Don't mistake a catchy hook for clickbait. Do not promise an insight that the Reel does not deliver. Avoid the repeated structure “question / three tips / save this” unless it genuinely fits.

### Writing and voice lenses

Reuse the plugin's lenses **as modifiers, not separate content generators**:

- `friendly-lens` — usual default for teaching, founder-to-founder advice, credible everyday chat and approachable invitations.
- `formal-lens` — official announcements, application/partner information, logistics, program facts, deadlines and communications requiring precision.
- `jokey-lens` — occasional restrained observation or playful twist when the subject warrants it; do not make it the default or turn official information into a joke.

Mixing levels of warmth is allowed only when intentional and coherent. A lens changes *wording*, not facts, branding or the approved strategic angle.

Write **for humans reading a small screen**:
- short, natural, direct, specific lines; one idea per beat;
- conversational rhythm without forced slang, filler, fake typos or manufactured awkwardness;
- no generic AI writing, exaggerated hype, startup-guru language, forced rhetorical questions or “perfectly scripted” fake dialogue;
- no emoji anywhere (copy, bubbles, avatars, reactions), no exclamation marks or decorative jargon (see `../../design-system/AI_TELLS.md`);
- no unverified statistics, founder stories, quotes, outcomes, promises, timelines or fake urgency;
- preserve caveats whenever removing them would change the meaning; move noncritical attribution to caption/quiet note only when still truthful;
- preserve the language requested by the user or used in the approved brief. Never silently translate source facts.

Revise every screen as a human editor: does this sound like something a real founder, colleague or program team would write? Is there a useful point beyond sounding clever? If not, rewrite.

## Preferred creative family A — Chat / conversation

Use when a believable exchange creates a reveal, objection, tension, invitation or relatable problem. Especially useful for announcements, teasers, challenges and short misconception corrections.

- Base the visual grammar on **modern mobile messaging / iMessage-inspired interaction**, not a literal Apple UI replica and not a generic “AI conversation” interface.
- Light IL background by default: white or pale teal. Use teal/deep teal as dominant brand colors and dark neutral text; no large purple background or purple conversation bubbles.
- Incoming and outgoing messages must be clearly differentiated through alignment, color and spacing. Use round, comfortable bubbles but avoid inflated pill shapes, dense blocks and anonymous rectangles.
- Use **Poppins or a clean readable sans** inside bubbles. Handwriting is not the default chat font; avoid childish, bot-like or overly futuristic typography.
- Optional chat header, small profile avatar (authorized photo, an initial, or a simple illustrated face; never an emoji), contact cue, typing dots, understated delivered/reaction behavior (the kit's drawn heart or check, never an emoji reaction) or subtle interface motion, only if these add realism.
- Never generate a fabricated real person's face/name or imply a genuine chat happened unless the source actually supports that. A scripted/sketched conversation may be visibly framed as illustrative.
- Messages appear with believable timing, staggered arrival and pauses before important replies. Keep enough of the conversation visible to preserve context; adapt scrolling/panning to the actual text.
- Give each message a job. People should not be exchanging long, polished exposition in bubbles. A few well-paced replies beat a fake 12-message speech.
- The reveal/punchline must be visually and narratively earned. Don't force every chat to end with the same lesson or CTA.

**Failure modes:** purple-first visuals, overly perfect assistant copy, one message occupying most of the screen, fake phone chrome, unnecessarily tiny text, robotic pacing and every bubble having the same entrance animation.

## Preferred creative family B — Handwritten / human teaching

Default direction to consider for educational Reels explaining a concept, process, feedback loop, founder mistake, decision, framework or change of perspective.

- Aim for **a real person explaining an idea as it unfolds**, not an animated list with a handwriting font pasted on top.
- Favor warm white or light IL surfaces, restrained notebook/paper cues when useful, deep ink and teal as the primary highlight. Do not inherit purple accents from an external reference; purple is only a restrained semantic signal when relevant.
- Use handwriting with purpose: write or draw a key phrase, draw the next arrow, circle the key assumption, cross out the wrong step, add a tiny margin note, correct an order, complete a diagram, connect two ideas, check off a conclusion.
- **Human-first motion is essential:** information should be constructed, annotated, revised or revealed **through time**. A line appears because it is being drawn; an underline follows a thought; a wrong answer is struck through before its correction appears. These are teaching actions, not arbitrary decoration.
- Balance authentic handwritten character with readability. The design system's **Caveat** can provide human accents where suitable; use **Poppins** for dense explanatory copy and **IBM Plex Mono** for occasional micro-labels. Don't sacrifice legibility to imitate handwriting.
- Use a consistent stroke, line weight, icon language and restrained composition. One or two meaningful doodles are better than a clutter of cute motifs.
- Vary teaching scenes: a comparison, a sketched causal chain, a thought crossed out, an evolving diagram, a physical note, a zoomed correction, a before/after reconstruction. **Do not repeat the same notebook layout in every scene or every Reel.**
- Keep text and marks visually connected. Let the drawing replace explanatory words whenever it makes the concept faster to understand.
- Pace ink/reveals so the viewer can follow what changes. Holding the final answer matters as much as animating its construction.

**Failure modes:** static lists that simply fade in, a full screen of tiny script, template-like notebook cards, decorative doodle overload, “study aesthetic” unrelated to IL, chaotic pen motion or motion with no cognitive purpose.

## Other valid visual families

Consider these whenever they better serve the approved message:

- **Mistake → fix / wrong sequence → corrected sequence:** physically replace or repair an idea through the motion.
- **Myth → reality:** make the contrast legible, grounded in evidence rather than imaginary universal claims.
- **Before → after:** show meaningful difference without inventing results or metrics.
- **Visual process / checklist:** animate a diagram or process progressing; don't simply stack bullet points.
- **Real-event photo/footage-led:** prioritize authentic moments, crops, captions and context; never infer identities, locations or outcomes from appearance alone.
- **One strong thought / visual metaphor:** one well-timed composition or object transformation can outperform a forced chat.
- **Direct campaign announcement:** crisp, memorable typography and restrained motion when urgency/clarity matter more than dialogue.

The families are *creative options*, not mandatory menu items. User requests and the source may call for an original treatment. Never make all Reels look like the same preset.

## Innovation Labs visual system

The portable design system remains authoritative. For **this Reel skill**, prioritize its **Light teal expression**, regardless of the general semantic accent defaults elsewhere in the plugin.

Core reference tokens:
- `--teal: #0095AC` — main brand fill / emphasis;
- `--teal-deep: #016462` and `--teal-ink: #016462` — dark teal fills and readable smaller teal text;
- `--surface-page: #FFFFFF`, `--surface-alt: #F4FBFB`, `--surface-tint: #EAF7F7` — default grounds;
- `--ink: #10201F` and `--ink-muted: #3C5052` — primary/secondary copy;
- `--on-brand: #FFFFFF` — text on appropriate teal/dark fills;
- purple/`--ax` — **limited semantic accent only**, e.g. a meaningful AI/challenger role, not the dominant Reel palette.

Follow actual token contrast guidance: raw brand teal on white is not suitable for small text; use deep teal (`--teal-ink`) instead. Avoid small white text on bright teal without verified contrast.

Typography: **Poppins** for primary editorial type and chat; **IBM Plex Mono** for rare small labels; **Caveat** or a legible handwriting treatment for intentional teaching marks. Use existing licensed/available fonts; don't invent fonts or distribute font files. Keep type big enough for mobile. Avoid generic tech/neon aesthetics, gradient wallpaper, oversized UI chrome and carousel-looking title cards.

One strong visual focus per beat. Empty space is an asset. Use branded backgrounds or official elements selectively, without turning each scene into a template.

## Signature ending — required

After the actual message/payoff, reserve a brief closing beat recognizably **Innovation Labs**.

- Use the **real 2027 Innovation Labs logo** from `../../assets/logo_primary_2027.svg` on Light surfaces or `../../assets/logo_white_2027.svg` on dark/teal surfaces. Preserve aspect ratio, contrast and required clearspace. Never redraw, retype or invent a substitute logo.
- By default **consider the flying pig social mascot plus the logo**, with the pig positioned above, beside or moving into the composition. Existing mascot: `../insta-post-maker/assets/brand-elements/flying-pig.png` (or another approved variant only if consistent with the scene).
- A short, subtle **pig float/fly/settle** animation, then logo reveal, is one signature variation. Other variations may use a simple approved bulb/motif or a different restrained entrance. Aim for **2–3 coherent ending treatments over time**, rather than one rigid animation or completely unrelated styles.
- In formal, partner-facing or sensitive material, use an approved official brand element or only the logo when a mascot would weaken credibility.
- An optional one-line CTA must fit the approved content and be actionable; never invent a registration destination, date, deadline or claim.
- The outro should normally last roughly **1.5–2.5 seconds**, enough to register the brand without dominating the Reel. Keep it short, polished and aligned with the preceding art direction.
- Brand elements are **not mandatory in intermediate scenes**. Use them sparingly, when they actually contribute. Do not put a flying pig or bulb in every educational screen.

**Never put the signature before the hook.** The first frame sells the idea; the final frame signs it.

## Motion and production direction

Motion must have an editorial reason. Prefer gestures people recognize: message arriving, typing hesitation, a drawn correction, an underline progressing, a note unfolding, one item replacing another, an intentional crop/pan, a simple icon following the logic. Use easing, spacing and timing that feel designed; avoid relentless bounce, glows, elastic overshoot and filler transitions.

**Do not default to the lowest-effort animation route.** A sequence of text-card fades, scrolling screenshots or static carousels exported to MP4 does not satisfy the intention of this skill. Invest motion detail where it explains, delights briefly or creates a reveal, without spending complexity on meaningless spectacle.

### Production path: the IL Reel Kit (default)

`production/` contains the default way to make a Reel. Read `production/README.md` before the first Reel in a session.

- `new-reel.mjs <folder>` scaffolds a self-contained Reel folder: the kit, the official logos, shared brand elements, mascots and an empty `reel.html`.
- `kit/il-reel-kit.js` is a **deterministic timeline plus IL motion primitives**: `appear`, `write` (handwriting ink reveal), `draw` (stroke drawing), `mark` (hand-drawn underline / circle / strike / highlight / box / check / arrow), `chat` (iMessage-inspired thread with typing, receipts and reactions), `camera`, `scene` and `outro` (pig / bulb / logo signature). Every frame is a pure function of time, so a render is reproducible and the same file plays live in a browser for review.
- `render.mjs reel.html` exports a 1080×1920 H.264/yuv420p MP4 at 30 fps, plus a 9:16 and a 4:5 cover, a contact sheet, `onscreen.txt` (all registered copy, in order) and `report.json` (ffprobe facts and lint).
- The built-in lint checks **reading time** for every line registered with `r.read()`, **safe-zone** placement, **minimum type size** and that **a hook is visible at t = 0**. Fix every warning, or leave a comment in `reel.html` explaining why it is intentional (for example, text used as texture).

The kit is a toolkit, **not a template and not a JSON scene engine**. Each Reel's concept, layout, copy and timing are written fresh in `reel.html` for that brief. Never copy the layout of a previous Reel or of `generated-examples/reels/`. The primitives exist so effort goes into the idea and the motion, not into rebuilding a renderer.

Other paths stay valid when they serve the piece better:
- **Real footage / photos**: place them in the Reel folder's `media/` and use them as `<video>`/`<img>` layers. For long footage edits, ffmpeg directly is fine.
- **Claude Motion**: see below.
- Do not search for or invoke the old `render_reel.py` from earlier plugin versions.

### Deliver as an Artifact too (review and sharing)

Every Reel is also a live web page, because `reel.html` plays itself (scrubber, play/pause, safe-zone guides). After the MP4 passes the gate:

1. `node production/export-artifact.mjs <folder>` writes `<folder>/artifact/index.html` (artifact-ready: no own `<html>/<head>`, tokenised page colors, fonts from Google Fonts) plus `files.json`, which contains only the kit and the assets the Reel uses.
2. Publish it with the Artifact tool: `file_path` = `<folder>/artifact/index.html`, `files` = the map in `files.json`, `icon` = `video` on the first publish. To update it, publish the same path again so it keeps the same link.

The Artifact is the review and share surface: the team scrubs to any second and comments, and the link can be shared from the page's Share menu. **The MP4 stays the file that gets posted.** Both come from the same source, so they never drift apart.

### Claude Motion (optional, when the session offers it)

Use Claude Motion only when the session lists a **Motion** Artifact type (`Artifact` → list types). If it isn't listed, don't mention it as an option and use the kit. When it is available, consider it for pieces where its motion editor adds something the kit doesn't: kinetic typography with complex choreography, character-style animation of a brand element, or a piece the team wants to keep editing by hand on a timeline. In that case:
- the same brief, hook, copy and boundaries apply. Motion is a production tool, not a new creative brief;
- the same brand inputs: IL tokens, Poppins / IBM Plex Mono / Caveat, the real logo and mascot files, `design-system/AI_TELLS.md`;
- the same gate: hook at frame 0 and inside the 4:5 crop, reading time, safe zone, the signature ending, `human-pass` on every visible line;
- export to 1080×1920 MP4 if Motion supports it. If not, rebuild the final piece in the kit so the posted file is reproducible. Say which path you used in the review notes.

Default stays the kit. Never pick Motion "to look expensive".
- Preserve source footage/photography where used; do not fabricate evidence of real IL events or people.
- Only use audio/music/SFX when requested and the rights or permission are clear. A silent MP4 is fully valid. **Never add voiceover.**

### Default format and pacing

- Vertical `9:16`, preferred **1080 × 1920** MP4, H.264 video, standard broadly compatible pixel format (e.g. `yuv420p`), normally **30 fps** unless source footage or brief justifies otherwise.
- Default duration is determined by information density: compact teasers roughly 8–12 s, announcements around 10–20 s, a single educational insight often 15–30 s, multi-step explanation roughly 20–40 s. These are guides, not requirements.
- Reading time wins over an arbitrary 15-second target. Shorten copy or split the concept before accelerating everything beyond comprehension.
- Protect critical text from Instagram interface overlays. For 1080 × 1920, a **conservative starting guide** is x about 90–990 and y about 250–1550 for critical content; verify against current platform framing and the actual mobile preview rather than treating these numbers as guaranteed safe zones.
- Strong type hierarchy, few words visible at once, accessible contrast and readable hold times. Check actual playback **with sound off** at phone size.

## Workflow

1. **Ground the source.** Extract actual claims, audience, dates, actions, proof, visual assets and caveats. For repurposing, preserve the source's factual scope; do not turn an idea or proposal into a past result. A supplied post/deck is source material, not a fixed animation storyboard.
2. **Find the angle.** Decide the single outcome the viewer should remember; write a specific hook and a purposeful payoff. Select the relevant `friendly-lens`, `formal-lens` or restrained `jokey-lens` as appropriate.
3. **Art-direct the mechanism.** Choose chat, handwritten, footage-led or another visual structure. Define what changes onscreen over time, not merely which static frames appear. Resolve why each motion beat exists.
4. **Plan screen text and timing.** Write concise on-screen copy, sequencing, entrances, holds, exits and end-card. No narrated script and no voiceover dependency. Use the user-selected creative treatment when specified.
5. **Check variety.** Read the Reels log (below). Pick a family, a hook mechanism and an ending treatment that do not repeat the last few Reels without a reason.
6. **Produce the Reel.** `node production/new-reel.mjs <folder>`, write the concept in `reel.html`, then `node production/render.mjs <folder>/reel.html`. Reuse authentic IL logos and approved assets and keep Light teal the visual anchor. Do not stop at a concept, preview, storyboard or video code if an MP4 can be produced.
7. **Review the result visually.** Open the contact sheet, then extract full-resolution frames at the hook, each reveal, the payoff and the last branded second (`ffmpeg -ss <t> -i reel.mp4 -frames:v 1 f.png`) and look at them. Correct copy, contrast, crop, composition balance (no empty bottom half), timing, text density, motion coherence, mascot placement and logo fidelity. If a scene feels like an auto-generated slide, redesign it rather than adding another fade. Re-render after every fix.
8. **Run `human-pass`** on `<name>.onscreen.txt` and on the caption. Rewrite flagged lines through the active lens. For on-screen copy, the gate is zero lexicon hits and zero unresolved structural flags (see `../human-pass/SKILL.md` on why the detect score reads low for short Reel lines).
9. **Verify and deliver.** Confirm `report.json` shows `FORMAT ok` and a clean or justified lint. Deliver the MP4, the 4:5 cover and the caption draft, with concise review notes, and publish the live Artifact preview (see "Deliver as an Artifact too"). Flag facts or CTAs that need human confirmation. Do not publish without an explicit request. When the human approves, append the entry to the Reels log.

## Caption, cover and audio handoff

A Reel ships with more than the video:
- **Caption draft.** The first ~125 characters carry the hook, because that is what shows before "more". Use plain IL voice: no hashtag walls (0–3 relevant tags at most), no follow/tag bait, and one action at most. The quiet source/evidence note may live here when it is not content-critical. Run it through `human-pass`.
- **Cover.** `render.mjs --cover <t>` chooses the frame. Check `<name>.cover-4x5.jpg`: the profile grid shows that centre crop, so the hook must read inside it.
- **Audio.** The MP4 is silent by design. If the team wants music, add it at publish time from Instagram's in-app audio library, where licensing is handled by the platform. Never bake in unlicensed tracks.

## Reels log

Keep `~/.claude/ilabs/reels-log.md` (create it if missing). It is how variety across Reels is actually enforced. Add one line per approved Reel:

```
- 2026-10-23 | context-engineering | family: handwritten | hook: question ("Still polishing the prompt?") | ending: pig | 33s | lens: friendly
```

Before step 3, read the last 5–10 entries. Avoid repeating the same family + ending pair more than twice in a row, and rotate the 2–3 ending treatments.

### If MP4 production is unavailable

Be precise and transparent: **“MP4 not rendered”** and explain the unavailable capability or blocking issue. Provide the approved on-screen script, storyboard, motion direction, brand asset paths and the minimum practical production handoff **only as an explicitly labeled fallback**. Never present that fallback as a completed Reel and never silently supply a poor-quality video as a substitute for the intended creative work.

## Final quality gate

A Reel is not complete until all applicable checks pass:

- [ ] The first visible moment contains a readable, specific hook; no branded intro delays it.
- [ ] The content provides a real insight or a clear, fact-checked program message.
- [ ] It makes sense with sound off; **text on screen, no voiceover**.
- [ ] The selected narrative mode fits the message and user reference without slavishly copying a template.
- [ ] Motion **builds, teaches, reacts or reveals**; it is not just a static carousel with fades.
- [ ] Text feels human and has been adapted through the right voice lens; no fake AI-written dialogue.
- [ ] Innovation Labs **Light teal** dominates appropriately; purple is controlled and justified.
- [ ] Phone-size legibility, pacing, contrast and interface safe areas have been checked.
- [ ] Official IL logo is accurate, and the ending uses a fitting mascot/approved brand element where appropriate.
- [ ] Brand assets are not mechanically repeated through every content scene.
- [ ] The MP4 was **actually rendered and visually inspected** (contact sheet + full-resolution frames), or the production limitation is clearly declared.
- [ ] `report.json`: format ok; lint clean, or every remaining warning justified in `reel.html`.
- [ ] `human-pass` run on the on-screen copy and the caption; no unresolved flags.
- [ ] `design_tells.py` run on `reel.html`: clean, or every finding is a documented IL exception.
- [ ] Caption draft and 4:5 cover delivered; live Artifact published; Reels log updated after approval.
- [ ] Claims are source-grounded; final video is for human review, not assumed published.
