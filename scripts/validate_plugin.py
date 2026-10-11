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

except Exception as e:
    errors.append(f'plugin.json invalid: {e}')


for p in sorted((root / 'skills').glob('*/SKILL.md')):
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
    'formal-lens',
    'friendly-lens',
    'jokey-lens',
]

found = {
    p.parent.name
    for p in (root / 'skills').glob('*/SKILL.md')
}

for name in required:
    if name not in found:
        errors.append(f'missing skill: {name}')


showcase = root / 'showcase' / 'index.html'

if not showcase.exists():
    errors.append('missing showcase artifact')


if errors:
    print('\n'.join('ERROR: ' + e for e in errors))
    sys.exit(1)

print(
    f'OK: plugin manifest valid; '
    f'{len(found)} skills found; '
    f'showcase present.'
)
