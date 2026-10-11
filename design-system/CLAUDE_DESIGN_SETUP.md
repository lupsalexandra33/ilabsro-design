# Create the native Innovation Labs Design System in Claude

The native Claude Design System is an optional richer representation of the bundled portable spec. The plugin must still work without it. Create or share the native system when convenient, then use it alongside the same plugin rules.

## Source material to attach

Recommended:
1. `INNOVATION_LABS_DESIGN_SYSTEM.md`
2. the approved Strategy Hub HTML or screenshots
3. the approved Pitch/Presentation HTML or screenshots
4. Innovation Labs logos
5. optionally the deployed Vercel site / codebase

## Prompt

Create a reusable design system called **Innovation Labs** from the attached references.

Treat the written design-system specification as the rules and the Hub + Presentation as reference implementations, not as templates to copy blindly.

Capture:
- the teal/deep-teal palette and light/night behavior;
- bold modern sans headings, clean sans body, mono metadata;
- white and baby-teal surface logic;
- medium-rounded cards and pills;
- editorial data visualization;
- restrained playful accents;
- navigation and responsive patterns;
- the distinction between calm web/map backgrounds and the optional playable mesh treatment used in presentations.

Do not include dotted-grid page backgrounds. Do not generalize the animated map mesh into a default component.

The system must support websites, one-pagers and presentations while keeping the same Innovation Labs identity.

## Validation prompts

After creating the Design System, test it with:
- “Create a strategy landing page for Innovation Labs.”
- “Create a one-page strategy summary from this document.”
- “Create a six-slide founder-facing strategy presentation.”

If the output feels like three unrelated brands, refine the Design System before changing the output skills.
