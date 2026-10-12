# Map Proposal pattern — v0.4

Use this pattern for the Innovation Labs strategy route. This is a **strategy journey**, not a geographic map and not a generic timeline.

## Desktop composition

- Use one wide horizontal, gently serpentine route flowing left-to-right across a calm pale-teal or deep-teal field.
- The route is the dominant visual: a continuous turquoise line with sequential numbered circular stops.
- Stops sit directly on the route. Use compact rounded label cards alternating above/below so the path stays readable.
- Current/selected stop uses the semantic accent (`ax`): purple by default, yellow when the entire artifact uses yellow accent.
- Keep generous negative space. Do not turn the map into a card grid, dashboard, subway diagram or geographic map.
- In Night, restrained route/stop glow is allowed. The glow never becomes ambient background decoration.
- Background may contain a few large faint contour/wave curves only.
- **No template mesh, static brand mesh, particle field, playable network, tiny reactive lines or decorative micro-network behind the route.**

## Interaction

- Hover/focus may enlarge a stop slightly and emphasize its label.
- Selecting a stop reveals detail in a panel/sheet while preserving route geometry.
- A short route reveal or selected-segment transition is enough.
- Respect reduced motion.

## Connected Map + Hub behavior

- A full map and mini-map inside the same Hub use one shared ordered stop data/model.
- The compact map is simplified, not reinterpreted: same names/order and recognizable silhouette.
- If a previous approved artifact/reference provides a stop order or route composition, preserve that model rather than inventing a new one.

Across separate outputs such as Hub + deck, require one identical shared route only when the user supplies/approves it or explicitly asks for a coordinated artifact family.

## Mobile

- On portrait phones, transform the same ordered stops into a vertical journey.
- Keep numbering and semantic order identical to the desktop route within that artifact.
- Stop details open in a bottom sheet.

## Anti-patterns

Never use:
- dense animated mesh or spring network;
- static template mesh behind the strategy route;
- dotted paper/grid texture;
- radial ambient glow competing with the route;
- generic progress bar with labels detached from the route;
- a route made mainly of independent cards;
- literal geography unless the source requires it.
