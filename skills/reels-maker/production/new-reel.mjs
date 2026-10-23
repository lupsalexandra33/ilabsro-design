#!/usr/bin/env node
// Scaffold a self-contained Reel folder: kit + official IL assets + an empty reel.html skeleton.
// Usage: node new-reel.mjs <folder> [--title "Reel title"] [--duration 20]
// The folder is portable: open reel.html in a browser to review, publish it, or render it with render.mjs.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const pluginRoot = path.resolve(here, '../../..');
const args = process.argv.slice(2);
const dest = args.find((a) => !a.startsWith('--'));
if (!dest) { console.error('usage: node new-reel.mjs <folder> [--title ...] [--duration 20]'); process.exit(1); }
const opt = (k, d) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : d; };
const title = opt('title', 'Innovation Labs Reel');
const duration = Number(opt('duration', '20'));

const out = path.resolve(dest);
fs.mkdirSync(path.join(out, 'kit'), { recursive: true });
fs.mkdirSync(path.join(out, 'assets', 'brand-elements'), { recursive: true });
fs.mkdirSync(path.join(out, 'assets', 'mascots'), { recursive: true });
fs.mkdirSync(path.join(out, 'media'), { recursive: true });

for (const f of ['il-reel-kit.js', 'il-reel-kit.css']) fs.copyFileSync(path.join(here, 'kit', f), path.join(out, 'kit', f));
for (const f of ['logo_primary_2027.svg', 'logo_white_2027.svg', 'logo_currentcolor.svg'])
  fs.copyFileSync(path.join(pluginRoot, 'assets', f), path.join(out, 'assets', f));
for (const f of fs.readdirSync(path.join(pluginRoot, 'assets', 'brand-elements')))
  fs.copyFileSync(path.join(pluginRoot, 'assets', 'brand-elements', f), path.join(out, 'assets', 'brand-elements', f));
for (const f of ['flying-pig.png', 'flying-purple-pig.png'])
  fs.copyFileSync(path.join(pluginRoot, 'skills', 'insta-post-maker', 'assets', 'brand-elements', f), path.join(out, 'assets', 'mascots', f));

const html = path.join(out, 'reel.html');
if (!fs.existsSync(html)) {
  fs.writeFileSync(html, `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title.replace(/</g, '&lt;')}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&family=Caveat:wght@400;600;700&display=block">
<link rel="stylesheet" href="kit/il-reel-kit.css">
<style>
  /* Reel-specific layout goes here. Write it fresh for this concept. */
</style>
</head>
<body>
<div class="il-stage">
  <!-- One .il-scene per beat. The first scene must show the hook at t = 0. -->
  <section class="il-scene" id="s1"></section>
  <section class="il-scene" id="outro"></section>
</div>
<script src="kit/il-reel-kit.js"></script>
<script>
ILReel.run({ duration: ${duration}, fps: 30, title: ${JSON.stringify(title)}, family: '', ending: 'pig' }, async (r) => {
  // r.scene('#s1', 0, 4, { exit: 'fade' }); r.read('#hook', 0, 4, 'hook');
  // r.outro('#outro', { t: ${duration} - 2.2, variant: 'pig' });
});
</script>
</body>
</html>
`);
}
console.log('reel folder ready:', out);
console.log('  edit      ', path.join(out, 'reel.html'));
console.log('  preview    open reel.html in a browser (space = play/pause, "safe zone" toggles guides)');
console.log('  render     node', path.join(here, 'render.mjs'), html);
