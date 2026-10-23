#!/usr/bin/env node
// Turn a rendered Reel folder into a publishable Claude Artifact: a live, playable, shareable preview of the Reel.
//
// Usage: node export-artifact.mjs <reel folder>
// Writes <reel folder>/artifact/ with:
//   index.html       the page (no <html>/<head>/<body>: the Artifact publish adds the skeleton)
//   kit/…            the kit script + css
//   assets/…         only the assets the Reel can reference (logos, mascots, brand elements used, media/)
//   files.json       the `files` map to pass to the Artifact publish call
// Then publish with the Artifact tool: file_path = artifact/index.html, files = files.json contents.
// The MP4 stays the posting deliverable; the Artifact is the review / share surface.
import fs from 'node:fs';
import path from 'node:path';

const dir = path.resolve(process.argv[2] || '.');
const src = path.join(dir, 'reel.html');
if (!fs.existsSync(src)) { console.error('no reel.html in', dir); process.exit(1); }
const out = path.join(dir, 'artifact');
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

let html = fs.readFileSync(src, 'utf8');
const title = (html.match(/<title>([\s\S]*?)<\/title>/i) || [, 'Innovation Labs Reel'])[1].trim();
const headInner = (html.match(/<head>([\s\S]*?)<\/head>/i) || [, ''])[1];
const bodyInner = (html.match(/<body[^>]*>([\s\S]*?)<\/body>/i) || [, html])[1];
// keep the head's stylesheet links and <style>, drop charset/viewport/title (the skeleton and our own title cover them)
const keepHead = headInner
  .replace(/<meta[^>]*>/gi, '')
  .replace(/<title>[\s\S]*?<\/title>/i, '')
  .trim();
const page = `<title>${title}</title>
<style>
  /* Artifact page chrome: the player commits to one dark look so the Light IL stage reads as the subject.
     Stage colors come from the IL tokens in kit/il-reel-kit.css. */
  :root { --page-bg: #0D1515; --page-fg: #CFEEEE; color-scheme: dark; }
  body { background: var(--page-bg); color: var(--page-fg); }
</style>
${keepHead}
${bodyInner.trim()}
`;
fs.writeFileSync(path.join(out, 'index.html'), page);

const files = {};
const copy = (rel) => {
  const from = path.join(dir, rel);
  if (!fs.existsSync(from) || fs.statSync(from).isDirectory()) return;
  const to = path.join(out, rel);
  fs.mkdirSync(path.dirname(to), { recursive: true });
  fs.copyFileSync(from, to);
  files[rel.split(path.sep).join('/')] = path.relative(process.cwd(), to);
};
copy('kit/il-reel-kit.js');
copy('kit/il-reel-kit.css');
// assets the kit loads by name (outro variants) + anything reel.html references directly
for (const a of ['assets/logo_primary_2027.svg', 'assets/logo_white_2027.svg', 'assets/mascots/flying-pig.png', 'assets/brand-elements/bulb-glass.svg']) copy(a);
for (const m of html.matchAll(/(?:src|href)=["']((?:assets|media)\/[^"']+)["']/g)) copy(m[1]);
for (const m of html.matchAll(/url\(["']?((?:assets|media)\/[^"')]+)["']?\)/g)) copy(m[1]);

const size = Object.keys(files).reduce((n, k) => n + fs.statSync(path.join(out, k)).size, 0) + Buffer.byteLength(page);
fs.writeFileSync(path.join(out, 'files.json'), JSON.stringify(files, null, 2));
console.log(`artifact ready: ${path.join(out, 'index.html')}  (${Object.keys(files).length} files, ${(size / 1024).toFixed(0)} KB)`);
console.log('publish: Artifact file_path=' + path.relative(process.cwd(), path.join(out, 'index.html')) + '  files=' + path.relative(process.cwd(), path.join(out, 'files.json')));
