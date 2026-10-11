# Map Proposal pattern

Use this pattern for the Innovation Labs strategy route. This is a **strategy journey**, not a geographic map and not a generic timeline.

## Desktop composition

- Use one wide horizontal, gently serpentine route flowing left-to-right across a deep-teal / pale-teal field.
- The route is the dominant visual: a continuous 4px turquoise line with 8–10 sequential numbered circular stops.
- Stops sit directly on the route. Use compact rounded label cards that alternate above and below the line so the path stays readable.
- The first/current stop can have a larger ring/halo to establish the entry point. Current step uses purple only when there is a meaningful selected/current state.
- Keep generous negative space around the route. Do not turn the map into a card grid, dashboard, subway diagram or geographic map.
- In Night, a restrained route glow is allowed. The glow belongs to the route/stops only, never to ambient background decoration.
- Background may contain at most a few large, very faint contour/wave curves. No dots, mesh, particle field, tiny reactive lines or decorative micro-network.

## Interaction

- Hover/focus may slightly enlarge a stop and emphasize its label.
- Selecting a stop reveals detail in a panel/sheet while preserving the route geometry.
- Do not animate the entire background. A short route reveal or selected-segment transition is enough.
- Respect reduced motion.

## Connected Map + Hub behavior

- The Map Proposal is a visual gateway into the Strategy Hub and should include a clear `Open Strategy Hub` action.
- The Strategy Hub keeps `Map` in its main navigation.
- The Hub landing hero may show a **compact version of the same route** on the right side. It must use the same stop names, order and route logic as the full map.
- The compact map is simplified, not reinterpreted: same route silhouette / sequence, fewer details, and a clear `Open full map` action.
- If a previous approved artifact/reference provides a stop order or route composition, preserve that model rather than inventing a new one.

## Mobile

- Under 820px, transform the same ordered stops into a vertical journey.
- Keep the numbering and semantic order identical to desktop.
- Stop details open in a bottom sheet.

## Anti-patterns

Never use:
- a dense animated mesh or spring network;
- dotted paper/grid texture;
- radial ambient glows;
- a generic horizontal progress bar with labels detached from the route;
- a map made mainly of independent cards;
- a literal geographic map unless the source explicitly requires geography.
