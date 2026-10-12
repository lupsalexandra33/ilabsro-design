#!/usr/bin/env python3

from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []

manifest = root / '.claude-plugin' / 'plugin.json'

try:
    data = json.loads(manifest.read_text())
    if data.get('name') != 'ilabsro-design':
        errors.append('plugin name must be ilabsro-design')
    if data.get('version') != '0.4.0':
        errors.append('plugin version must be 0.4.0 for this test package')
except Exception as e:
    errors.append(f'plugin.json invalid: {e}')

skill_files = sorted((root / 'skills').glob('*/SKILL.md'))

for p in skill_files:
    text = p.read_text()
    if not text.startswith('---\n'):
        errors.append(f'{p}: missing YAML frontmatter')

    m = re.search(r'^name:\s*(.+)$', text, re.M)
    d = re.search(r'^description:\s*(.+)$', text, re.M)

    if not m:
        errors.append(f'{p}: missing name')
    if not d:
        errors.append(f'{p}: missing description')
    elif len(d.group(1).strip().strip('"')) > 200:
        errors.append(f'{p}: description > 200 chars')

required = [
    'website-maker',
    'presentation-maker',
    'one-pager-maker',
    'insta-post-maker',
    'brand-elements',
    'formal-lens',
    'friendly-lens',
    'jokey-lens',
]

found = {p.parent.name for p in skill_files}
for name in required:
    if name not in found:
        errors.append(f'missing skill: {name}')

required_files = [
    'design-system/INNOVATION_LABS_DESIGN_SYSTEM.md',
    'design-system/TOKENS.css',
    'design-system/BRAND_ELEMENTS.md',
    'assets/logo_primary_2027.svg',
    'assets/logo_white_2027.svg',
    'assets/brand-elements/bulb-glass.svg',
    'assets/brand-elements/make-it-real.svg',
    'assets/brand-elements/star.svg',
    'assets/backgrounds/blue/cover.jpg',
    'assets/backgrounds/yellow/cover.jpg',
    'skills/insta-post-maker/assets/brand-elements/flying-pig.png',
    'skills/insta-post-maker/references/social-2026/reference-bulb-mesh.jpeg',
    'skills/website-maker/examples/IL2027_strategy_hub.html',
    'skills/presentation-maker/examples/IL2027_pitch.html',
]

for rel in required_files:
    if not (root / rel).exists():
        errors.append(f'missing required file: {rel}')

svg_count = len(list((root / 'assets' / 'brand-elements').glob('*.svg')))
if svg_count != 16:
    errors.append(f'expected 16 shared SVG brand elements, found {svg_count}')

bg_families = {'blue', 'green', 'purple', 'yellow', 'classic'}
found_bg_families = {p.name for p in (root / 'assets' / 'backgrounds').iterdir() if p.is_dir()} if (root / 'assets' / 'backgrounds').exists() else set()
if not bg_families.issubset(found_bg_families):
    errors.append(f'missing background families: {sorted(bg_families - found_bg_families)}')

showcase_dir = root / 'showcase'
if showcase_dir.exists() and not (showcase_dir / 'index.html').exists():
    errors.append('showcase directory exists but showcase/index.html is missing')

if errors:
    print('\n'.join('ERROR: ' + e for e in errors))
    sys.exit(1)

print(
    f'OK: plugin manifest v0.4.0 valid; '
    f'{len(found)} skills found; '
    f'{svg_count} shared SVG brand elements; '
    f'v0.4 references present.'
)
