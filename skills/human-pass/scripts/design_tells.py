#!/usr/bin/env python3
"""
design_tells.py - scan HTML / CSS / SVG / JS for the visual "AI tells" listed in
design-system/AI_TELLS.md, and for the copy tells that leak into markup.

  python3 design_tells.py index.html
  python3 design_tells.py ./site ./deck/index.html --json

Each finding names the tell number from AI_TELLS.md, the file, the line and the
snippet. IL design-system exceptions are recognised and not reported:
  - the official mesh grounds (var(--mesh-*), assets/backgrounds/*),
  - card hover lift of 1-3px,
  - the semantic purple accent tokens (--ax*),
  - the kit's own marks and chat CSS.

Heuristics, not proof: a finding means "look at this", and some tells (three
feature cards, bento) can only be judged by looking at the rendered page.
Python 3 standard library only.
"""
import argparse
import json
import os
import re
import sys

EXTS = {".html", ".htm", ".css", ".svg", ".js", ".mjs", ".jsx", ".tsx"}  # docs (.md) are not shipped output
SKIP_DIRS = {"node_modules", ".git", "kit", "__pycache__"}

EMOJI = re.compile("[\U0001F300-\U0001FAFF\U0001F1E6-\U0001F1FF☀-⛿✀-➿⭐]")  # arrows such as IL's ↗ are not emoji
RULES = [
    # (tell number, name, regex, flags, advice)
    (1, "generic icon set", r"lucide|data-lucide|heroicons|feather-icons|phosphor-icons|tabler-icons", re.I,
     "decorative icon tiles read as AI-builder default; use type, photos, IL elements or a drawn mark"),
    (3, "liquid glass", r"backdrop-filter\s*:\s*[^;]*blur|-webkit-backdrop-filter", re.I,
     "no frosted / glass panels; flat IL surfaces with line borders"),
    (4, "em dash", r"—|&mdash;|&#8212;", 0,
     "use commas, full stops or two sentences"),
    (5, "AI-default font", r"font-family[^;{}]*\b(Inter|Geist|Space Grotesk)\b|family=(Inter|Geist|Space\+Grotesk)", re.I,
     "IL type is Poppins / IBM Plex Mono / Caveat only"),
    (8, "fake terminal", r"#ff5f57|#febc2e|#28c840|#ffbd2e|#27c93f|\bnpx \w+ init\b|zsh\s*[—-]", re.I,
     "traffic-light window chrome; show the real thing or nothing"),
    (9, "it's not X, it's Y", r"(?i)\bit'?s not (?:just |only |a |an |about )?[^.<>\n]{2,40}[.,]\s*(?:<[^>]+>\s*)*it'?s\b", 0,
     "state what it is"),
    (10, "placeholder demo", r"coming soon|screenshot here|lorem ipsum|placeholder image|product screenshot", re.I,
     "real screenshots / photos / footage, or remove the section"),
    (11, "purple-on-black palette", r"#(?:8b5cf6|7c3aed|6d28d9|a855f7|9333ea|c084fc|6366f1)\b", re.I,
     "violet hex outside IL tokens; IL purple is --ax (#954BBC family) as an accent only"),
    (12, "glow orb / blob", r"\b(?:orb|blob|glow|aurora)s?\b[^{]*\{|filter\s*:\s*blur\(\s*(?:[4-9]\d|\d{3,})px", re.I,
     "no floating blurred orbs; only official IL mesh grounds where allowed"),
    (13, "dot grid", r"radial-gradient\([^)]*\b1(?:\.5)?px[^)]*\)[^;]*;[^}]*background-size\s*:\s*\d{1,2}px|dot-?grid|bg-dots", re.I,
     "dotted pattern behind content is banned by the IL design system"),
    (14, "sparkle icon", "✨|✦|✧|\\bsparkles?\\b", re.I,
     "never mark AI with sparkles; name the feature in words"),
    (15, "CTA arrow nudge", r"group-hover:translate-x|:hover[^{]*\{[^}]*translateX\(|(?:→|&rarr;)\s*</(?:a|button)", re.I,
     "CTAs name the destination; no arrow nudge (IL allows ↗ only on 'go deeper' links)"),
    (16, "oversized hover motion", r":hover[^{]*\{[^}]*(?:translateY\(\s*-(?:[4-9]|\d{2,})px|scale\(\s*1\.(?:0[3-9]|[1-9]))", re.I,
     "IL hover is a 1-3px lift with shadow-hover, nothing scales"),
    (18, "coloured left-border accent", r"border-left\s*:\s*[2-9]px\s+solid\s+(?!var\(--(?:line|line-soft|route)\))", re.I,
     "IL design system: never a coloured left border (the 5px top edge on Hub nav cards is the only accent stripe)"),
    (17, "rainbow / gradient text", r"background-clip\s*:\s*text|-webkit-background-clip\s*:\s*text|text-transparent\s+bg-gradient", re.I,
     "no gradient text; one palette per artifact"),
]
COMPILED = [(n, name, re.compile(rx, fl), adv) for n, name, rx, fl, adv in RULES]
HYPE_STATS = re.compile(r"(?<![\w#])(?:10x|99\.9%|120\+|10,000\+|\d{1,3}(?:,\d{3})+\+)(?!\w)")
HYPE_WORDS = re.compile(r"(?i)\b(blazing[- ]fast|ai magic|fort-?knox|loved by teams|second brain|supercharge|game-?chang\w*|next-?level)\b")
TAG = re.compile(r"<[^>]+>")


def visible_text_lines(text, ext):
    """For HTML, strip tags so copy checks look at what a reader sees (line numbers kept)."""
    if ext not in {".html", ".htm", ".svg"}:
        return None
    out, in_style, in_comment = [], False, False
    for line in text.split("\n"):
        low = line.lower()
        if "<style" in low or "<script" in low:
            in_style = True
        work = line
        if in_comment:
            if "-->" in work:
                work, in_comment = work.split("-->", 1)[1], False
            else:
                work = ""
        work = re.sub(r"<!--.*?-->", " ", work)
        if "<!--" in work:
            work, in_comment = work.split("<!--", 1)[0], True
        t = "" if in_style else TAG.sub(" ", work)
        if "</style" in low or "</script" in low:
            in_style = False
        out.append(t)
    return out


def scan_file(path):
    ext = os.path.splitext(path)[1].lower()
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError as e:
        return [{"tell": 0, "name": "unreadable", "file": path, "line": 0, "snippet": str(e), "advice": ""}]
    lines = text.split("\n")
    found = []

    def add(n, name, i, snip, adv):
        found.append({"tell": n, "name": name, "file": path, "line": i + 1, "snippet": snip.strip()[:110], "advice": adv})

    COPY_RULES = {4, 9, 10, 14}               # judged on what a reader sees, not on code comments
    vis = visible_text_lines(text, ext)
    for i, line in enumerate(lines):
        if "il-allow-tell" in line:          # explicit, human-approved exception marker on that line
            continue
        for n, name, rx, adv in COMPILED:
            if n in COPY_RULES:
                if vis is None:
                    continue
                line_v = vis[i]
                m = rx.search(line_v)
                if m:
                    add(n, name, i, line_v[max(0, m.start() - 30): m.end() + 50], adv)
                continue
            m = rx.search(line)
            if not m:
                continue
            if n == 12 and ("--mesh" in line or "assets/backgrounds" in line):
                continue
            # IL exceptions documented in the design system:
            if n == 18:
                blk_start = line.rfind("{", 0, m.start()); blk_end = line.find("}", m.end())
                block = line[blk_start + 1: blk_end if blk_end > 0 else None]
                if re.search(r"border-(?:bottom|top)\s*:\s*[2-9]px", block):
                    continue   # a drawn corner / chevron (two borders), not an accent stripe
            if n == 16 and re.search(r"\.(?:stop|disc|mdot|dot|miniStop)\b", line):
                continue   # Strategy Route stop markers may grow on hover / selection
            if n == 15 and re.search(r"(?i)aria-label=\"(?:next|prev|previous)|>\s*(?:next|prev|previous)\s*(?:→|&rarr;)", line):
                continue   # pager controls (Next / Prev) are controls, not CTA nudges
            add(n, name, i, line[max(0, m.start() - 30): m.end() + 50], adv)

    if vis is not None:
        for i, line in enumerate(vis):
            if "il-allow-tell" in lines[i]:
                continue
            if EMOJI.search(line):
                add(2, "emoji", i, line, "no emoji anywhere in IL output")
            if HYPE_STATS.search(line):
                add(6, "unsourced round stat", i, line, "bento/feature-card stat filler; use a real, sourced number or none")
            if HYPE_WORDS.search(line):
                add(6, "hype feature copy", i, line, "feature-card filler language; say the real thing")
    # bento / three-card heuristics (structure, needs a human look)
    spans = len(re.findall(r"grid-(?:column|row)\s*:\s*span\s*2|col-span-2|row-span-2", text, re.I))
    if spans >= 2:
        add(7, "bento grid (heuristic)", 0, f"{spans} span-2 grid cells", "mixed-size tile mosaic; check the rendered layout")
    three = len(re.findall(r"grid-template-columns\s*:\s*repeat\(\s*3\s*,|grid-cols-3", text, re.I))
    if three and re.search(r"class=\"[^\"]*\bicon|\bicon-|<svg[^>]*class=\"[^\"]*icon|lucide", text, re.I):
        add(6, "three feature cards (heuristic)", 0, f"{three} three-column grid(s) next to icon markup", "check for the icon+title+line x3 pattern")
    return found


def walk(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                for f in files:
                    if os.path.splitext(f)[1].lower() in EXTS:
                        yield os.path.join(root, f)
        else:
            yield p


def main():
    ap = argparse.ArgumentParser(description="Scan output files for the AI tells in AI_TELLS.md.")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    findings = [f for p in walk(a.paths) for f in scan_file(p)]
    if a.json:
        print(json.dumps(findings, indent=1, ensure_ascii=False))
    else:
        if not findings:
            print("DESIGN TELLS  clean")
        else:
            print(f"DESIGN TELLS  {len(findings)} finding(s)  (numbers refer to design-system/AI_TELLS.md)")
            for f in sorted(findings, key=lambda x: (x["file"], x["line"])):
                loc = f"{f['file']}:{f['line']}" if f["line"] else f["file"]
                print(f"  #{f['tell']:<2} {f['name']:<30} {loc}\n      {f['snippet']}\n      -> {f['advice']}")
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
