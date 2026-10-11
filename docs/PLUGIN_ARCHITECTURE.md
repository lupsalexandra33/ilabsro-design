# Plugin architecture

```text
ilabsro-design
├── .claude-plugin/plugin.json
├── design-system/
│   ├── INNOVATION_LABS_DESIGN_SYSTEM.md
│   ├── TOKENS.css
│   ├── COMPONENT_CATALOG.md
│   └── CLAUDE_DESIGN_SETUP.md
├── skills/
│   ├── website-maker/
│   ├── presentation-maker/
│   ├── one-pager-maker/
│   ├── insta-post-maker/
│   ├── formal-lens/
│   ├── friendly-lens/
│   └── jokey-lens/
├── examples/
├── docs/
└── scripts/
```

The plugin intentionally does not bundle connectors, agents or hooks in v0.2. The first goal is to validate skill composition and the native Design System.
