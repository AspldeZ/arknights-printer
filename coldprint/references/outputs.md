# Output types

## Poster or key visual (HTML)

- Start from `assets/poster-template.html`: a fixed artboard (1920×1080 by default) scaled to the viewport with `transform: scale`.
- Data graphics are computed from real formulas or real data, not drawn by eye.
- Render and run `scripts/render_check.py`. Look at the screenshot yourself as well: the script catches overflow, overlap, small text and extra saturated colors, not taste.
- Before delivery, run `scripts/embed_fonts.py` so fonts are inlined as base64 and the file renders the same on any machine.
- Deliver the PNG and the self-contained HTML.

## Image-generation prompt

See `image-prompts.md`.

## Logo

- Build it from simple geometry on a modular grid: straight segments, circles, 45° chamfers, stencil breaks.
- Present it as a construction drawing: grid, dimension lines, minimum size.
- Add two or three applications, such as a label, an ID badge, a sticker.

## Interface

- Make it a terminal inside the world (diegetic): frosted cards, chamfered corners, hairline frames, scales.
- Hierarchy comes from depth and blur. The brand color marks only what is selected, actionable or a warning.
- Status fields and timestamps are always present, so the interface reads as live.
- Interface text that must be read (not just scanned as rhythm) uses the `feed` minimum size from `parameters.md` or larger, and text contrast of at least 4.5:1 against its background.

## Archive card (person, equipment, place)

- Four layers: ghost name (huge, one step off the ground); local name (medium, ink black, heaviest); reversed information bar (category, index, status); small labels and disclaimer fine print.
- The subject echo sits behind the ghost name; the subject itself stays the sharpest thing on the card.
- The institution's emblem goes in one corner; a color control strip runs along the bottom edge.
- Arrange the four layers to suit the subject. Do not reuse the arrangement of any reference card.

## Slides or documents

- Apply the system throughout: corner index numbers, grid dots, page numbers written as archive numbers.
- One hero graphic per slide; text small and sparse, but no smaller than the `slides` minimum.
- Mark section changes with a dialect switch or a step-and-repeat transition.

## Photo treatment

- The photograph is material, not the finished piece: crop decisively, desaturate and cool it, overlay the dot screen or a halftone.
- Place it in one cell of the grid, or inside an aperture taken from the subject (`techniques.md` §3). Never let it fill the whole canvas.
