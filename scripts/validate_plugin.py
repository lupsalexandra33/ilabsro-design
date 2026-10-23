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
    if data.get('version') != '0.7.0':
        errors.append('plugin version must be 0.7.0')
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
    'reels-maker',
    'human-pass',
    'content-planner',
    'brand-image-maker',
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

    'skills/website-maker/examples/index.html',
    'skills/presentation-maker/examples/index.html',
    'skills/one-pager-maker/examples/IL2027_vision_onepager.html',

    'docs/USAGE.md',
    'docs/EXAMPLES.md',

    'scripts/build_plugin_zip.py',
]

for rel in required_files:
    if not (root / rel).exists():
        errors.append(f'missing required file: {rel}')


# Generated examples

examples_root = root / 'generated-examples'

required_example_families = {
    'website',
    'presentation',
    'one-pager',
    'social',
    'visuals',
}

found_example_families = set()

if not examples_root.exists():
    errors.append('generated-examples directory is missing')
else:
    found_example_families = {
        p.name for p in examples_root.iterdir()
        if p.is_dir()
    }

    missing_example_families = (
        required_example_families - found_example_families
    )

    if missing_example_families:
        errors.append(
            'missing generated-example families: '
            + str(sorted(missing_example_families))
        )


# Guard against stale local example references

stale_skill_references = {
    'skills/website-maker/SKILL.md': 'IL2027_strategy_hub.html',
    'skills/website-maker/examples/README.md': 'IL2027_strategy_hub.html',
    'skills/presentation-maker/SKILL.md': 'IL2027_pitch.html',
    'skills/presentation-maker/examples/README.md': 'IL2027_pitch.html',
}

for rel, stale_name in stale_skill_references.items():
    path = root / rel

    if path.exists() and stale_name in path.read_text():
        errors.append(
            f'{rel}: stale example reference still present: {stale_name}'
        )


# Shared SVG brand elements

brand_elements_dir = root / 'assets' / 'brand-elements'

if brand_elements_dir.exists():
    svg_count = len(list(brand_elements_dir.glob('*.svg')))
else:
    svg_count = 0

if svg_count != 16:
    errors.append(
        f'expected 16 shared SVG brand elements, found {svg_count}'
    )


# Background families

bg_families = {
    'blue',
    'green',
    'purple',
    'yellow',
    'classic',
}

backgrounds_root = root / 'assets' / 'backgrounds'

if backgrounds_root.exists():
    found_bg_families = {
        p.name for p in backgrounds_root.iterdir()
        if p.is_dir()
    }
else:
    found_bg_families = set()

if not bg_families.issubset(found_bg_families):
    errors.append(
        'missing background families: '
        + str(sorted(bg_families - found_bg_families))
    )


# Showcase sanity check

showcase_dir = root / 'showcase'

if showcase_dir.exists() and not (showcase_dir / 'index.html').exists():
    errors.append(
        'showcase directory exists but showcase/index.html is missing'
    )


# Final result

if errors:
    print('\n'.join('ERROR: ' + e for e in errors))
    sys.exit(1)

print(
    f'OK: plugin manifest v0.7.0 valid; '
    f'{len(found)} skills found; '
    f'{svg_count} shared SVG brand elements; '
    f'{len(found_example_families)} generated-example families; '
    f'v0.7.0 required files present.'
)
