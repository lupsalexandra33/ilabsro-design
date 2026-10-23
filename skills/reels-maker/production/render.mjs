#!/usr/bin/env node
// Render an IL Reel (reel.html built on il-reel-kit) to a review-ready 1080x1920 H.264 MP4.
//
// Usage:
//   node render.mjs path/to/reel.html [--out reel.mp4] [--fps 30] [--from 0 --to 5] [--cover 0.4] [--no-sheet]
//
// Produces next to the output:
//   <name>.mp4                 H.264 / yuv420p / +faststart, silent
//   <name>.cover-9x16.jpg      cover frame (default t=0.4s, i.e. the hook)
//   <name>.cover-4x5.jpg       centre 1080x1350 crop — what the profile grid shows
//   <name>.sheet.jpg           contact sheet, one frame per second, for visual review
//   <name>.report.json         ffprobe facts + lint warnings (reading time, safe zone, type size, hook)
//   <name>.onscreen.txt        every registered on-screen line, in order — feed it to human-pass
//
// Requirements: Node 18+, Playwright (Chromium), ffmpeg/ffprobe on PATH. Fonts (OFL: Poppins, IBM Plex Mono,
// Caveat) are fetched once from npm (@fontsource) into ~/.cache/il-reels and embedded at render time.
// Fonts are never bundled in the plugin.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawn, execSync, execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
const input = args.find((a, i) => !a.startsWith('--') && !(i > 0 && args[i - 1].startsWith('--') && !['--no-sheet'].includes(args[i - 1])));
if (!input) { console.error('usage: node render.mjs reel.html [--out reel.mp4] [--from s --to s] [--cover s]'); process.exit(1); }
const opt = (k, d) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : d; };
const flag = (k) => args.includes('--' + k);
const htmlPath = path.resolve(input);
const outPath = path.resolve(opt('out', htmlPath.replace(/\.html?$/i, '') + '.mp4'));
const base = outPath.replace(/\.mp4$/i, '');
fs.mkdirSync(path.dirname(outPath), { recursive: true });

// ---------- playwright ----------
async function loadPlaywright() {
  try { return await import('playwright'); } catch {}
  try {
    const root = execSync('npm root -g', { encoding: 'utf8' }).trim();
    const req = createRequire(path.join(root, 'noop.js'));
    return req('playwright');
  } catch {}
  console.error('Playwright not found. Install with: npm i -g playwright (and a Chromium build).');
  process.exit(2);
}

// ---------- fonts (OFL, fetched not bundled) ----------
function fontCSS() {
  const cache = process.env.IL_REELS_CACHE || path.join(os.homedir(), '.cache', 'il-reels');
  const fsDir = path.join(cache, 'node_modules', '@fontsource');
  const need = ['poppins', 'ibm-plex-mono', 'caveat'];
  if (!need.every((n) => fs.existsSync(path.join(fsDir, n)))) {
    fs.mkdirSync(cache, { recursive: true });
    if (!fs.existsSync(path.join(cache, 'package.json'))) fs.writeFileSync(path.join(cache, 'package.json'), '{"name":"il-reels-cache","private":true}');
    console.log('fetching fonts (one time) into', cache);
    execSync('npm i --silent @fontsource/poppins @fontsource/ibm-plex-mono @fontsource/caveat', { cwd: cache, stdio: 'inherit' });
  }
  const faces = [
    ['Poppins', 'poppins', [400, 500, 600, 700, 800]],
    ['IBM Plex Mono', 'ibm-plex-mono', [400, 500]],
    ['Caveat', 'caveat', [400, 500, 600, 700]],
  ];
  let css = '';
  for (const [family, dir, weights] of faces) {
    for (const w of weights) {
      for (const sub of ['latin', 'latin-ext']) {
        const f = path.join(fsDir, dir, 'files', `${dir}-${sub}-${w}-normal.woff2`);
        if (!fs.existsSync(f)) continue;
        const range = sub === 'latin'
          ? 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'
          : 'U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF';
        css += `@font-face{font-family:"${family}";font-style:normal;font-weight:${w};font-display:block;src:url(data:font/woff2;base64,${fs.readFileSync(f).toString('base64')}) format("woff2");unicode-range:${range};}\n`;
      }
    }
  }
  return css;
}

function probe(file) {
  const j = JSON.parse(execFileSync('ffprobe', ['-v', 'error', '-print_format', 'json', '-show_streams', '-show_format', file], { encoding: 'utf8' }));
  const v = j.streams.find((s) => s.codec_type === 'video');
  const [n, d] = v.r_frame_rate.split('/').map(Number);
  return { width: v.width, height: v.height, codec: v.codec_name, profile: v.profile, pix_fmt: v.pix_fmt, fps: +(n / d).toFixed(3),
    duration: +(+j.format.duration).toFixed(3), frames: +v.nb_frames || null, audio: j.streams.some((s) => s.codec_type === 'audio'),
    size_mb: +(+j.format.size / 1048576).toFixed(2) };
}

const { chromium } = await loadPlaywright();
const exe = fs.existsSync('/opt/pw-browsers/chromium') && !fs.statSync('/opt/pw-browsers/chromium').isDirectory() ? '/opt/pw-browsers/chromium' : undefined;
const browser = await chromium.launch({ executablePath: exe, args: ['--force-color-profile=srgb', '--disable-lcd-text', '--font-render-hinting=none'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.route(/fonts\.(googleapis|gstatic)\.com/, (r) => r.abort());
const css = fontCSS();
await page.addInitScript((c) => { window.__IL_FONT_CSS = c; }, css);
const errors = [];
page.on('pageerror', (e) => errors.push(String(e)));
page.on('console', (m) => { if (m.type() === 'error' && !/Failed to load resource/.test(m.text())) errors.push(m.text()); });
page.on('requestfailed', (q) => { if (!/fonts\.(googleapis|gstatic)\.com/.test(q.url())) errors.push('missing asset: ' + q.url()); });
await page.goto(pathToFileURL(htmlPath).href + '?render=1');
try { await page.waitForFunction(() => window.__IL_READY === true, null, { timeout: 30000 }); }
catch { console.error('reel did not become ready.\n' + errors.join('\n')); await browser.close(); process.exit(3); }

const info = await page.evaluate(() => ({ duration: window.__IL.duration, fps: window.__IL.fps, meta: window.__IL.meta }));
const fps = Number(opt('fps', info.fps));
const from = Number(opt('from', 0));
const to = Math.min(Number(opt('to', info.duration)), info.duration);
const lint = await page.evaluate(() => window.__IL.lint());
const onscreen = await page.evaluate(() => window.__IL.script());
// plain text for human-pass (one beat per line) + timed JSON for review
fs.writeFileSync(base + '.onscreen.txt', onscreen.map((l) => l.text).filter((t, i, a) => t && a.indexOf(t) === i).join('\n') + '\n');

const total = Math.round((to - from) * fps);
console.log(`rendering ${path.basename(htmlPath)}  ${from}s → ${to}s  ${total} frames @ ${fps}fps`);
const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-',
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
  '-r', String(fps), '-movflags', '+faststart', outPath], { stdio: ['pipe', 'inherit', 'inherit'] });
const write = (buf) => new Promise((res) => (ff.stdin.write(buf) ? res() : ff.stdin.once('drain', res)));
const t0 = Date.now();
for (let i = 0; i < total; i++) {
  const t = from + i / fps;
  await page.evaluate((tt) => window.__IL.seek(tt), t);
  const buf = await page.screenshot({ type: 'png', clip: { x: 0, y: 0, width: 1080, height: 1920 }, animations: 'disabled', caret: 'hide' });
  await write(buf);
  if (i % fps === 0) process.stdout.write(`\r  ${Math.round((i / total) * 100)}%  ${t.toFixed(1)}s`);
}
ff.stdin.end();
await new Promise((res, rej) => ff.on('close', (c) => (c === 0 ? res() : rej(new Error('ffmpeg exit ' + c)))));
process.stdout.write(`\r  100%  done in ${((Date.now() - t0) / 1000).toFixed(1)}s\n`);

// covers
const coverT = Number(opt('cover', 0.4));
await page.evaluate((tt) => window.__IL.seek(tt), coverT);
await page.screenshot({ path: base + '.cover-9x16.jpg', type: 'jpeg', quality: 92, clip: { x: 0, y: 0, width: 1080, height: 1920 } });
await page.screenshot({ path: base + '.cover-4x5.jpg', type: 'jpeg', quality: 92, clip: { x: 0, y: 285, width: 1080, height: 1350 } });
await browser.close();

// contact sheet
if (!flag('no-sheet')) {
  const n = Math.max(1, Math.ceil(to - from));
  const cols = Math.min(8, n), rows = Math.ceil(n / cols);
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', outPath, '-vf',
    `fps=1,scale=270:-1,drawtext=text='%{pts\\:hms}':x=8:y=8:fontsize=18:fontcolor=white:box=1:boxcolor=black@0.55,tile=${cols}x${rows}:padding=6:color=0x0d1515`,
    '-frames:v', '1', base + '.sheet.jpg']);
}

const facts = probe(outPath);
const checks = [];
if (facts.width !== 1080 || facts.height !== 1920) checks.push(`size ${facts.width}x${facts.height}, expected 1080x1920`);
if (facts.codec !== 'h264') checks.push(`codec ${facts.codec}, expected h264`);
if (facts.pix_fmt !== 'yuv420p') checks.push(`pix_fmt ${facts.pix_fmt}, expected yuv420p`);
if (Math.abs(facts.fps - fps) > 0.01) checks.push(`fps ${facts.fps}, expected ${fps}`);
if (Math.abs(facts.duration - (to - from)) > 0.1) checks.push(`duration ${facts.duration}s, expected ${(to - from).toFixed(2)}s`);
const report = { input: htmlPath, output: outPath, meta: info.meta, video: facts, format_issues: checks, lint, onscreen, page_errors: errors };
fs.writeFileSync(base + '.report.json', JSON.stringify(report, null, 2));

console.log(`\n${path.basename(outPath)}  ${facts.width}x${facts.height}  ${facts.codec}/${facts.pix_fmt}  ${facts.fps}fps  ${facts.duration}s  ${facts.size_mb}MB`);
console.log(checks.length ? 'FORMAT  ' + checks.join('; ') : 'FORMAT  ok');
if (lint.length) { console.log(`LINT    ${lint.length} warning(s)`); for (const l of lint) console.log(`  - [${l.kind}] ${l.text} — ${l.detail}`); }
else console.log('LINT    clean');
if (errors.length) console.log('PAGE ERRORS\n  ' + errors.join('\n  '));
console.log(`review: ${path.basename(base)}.sheet.jpg, ${path.basename(base)}.cover-4x5.jpg`);
console.log(`copy:   ${path.basename(base)}.onscreen.txt  (run human-pass on it)`);
