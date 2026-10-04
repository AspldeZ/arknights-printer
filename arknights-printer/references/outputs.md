# Output types

## Poster or key visual (HTML)

- Start from `assets/templates/poster.html`: a fixed artboard (1920×1080 by default) scaled to the viewport with `transform: scale`.
- Data graphics are computed from real formulas or real data, not drawn by eye.
- Run `scripts/bundle.py` so stylesheet, scripts and subsetted fonts are inlined and the file renders the same on any machine.
- Run `scripts/render_check.py` on the bundled file. Look at the screenshot yourself as well: the script catches fallback fonts, overflow, overlap, small text and extra saturated colors, not taste.
- Deliver the PNG and the bundled HTML.

## Image-generation prompt

See `image-prompts.md`.

## Logo

- Build it from simple geometry on a modular grid: straight segments, circles, 45° chamfers, stencil breaks.
- Present it as a construction drawing: grid, dimension lines, minimum size.
- Add two or three applications, such as a label, an ID badge, a sticker.

## Information sheet and series

The main output: one sheet about one real subject, issued as a document.

- **Frame.** Institution and department top-left; file number and sheet number ("sheet 02 of 03") top-right; sources in one fine-print line bottom-left; bottom-right the color control strip and, when a real institution's name is used, a disclaimer such as "concept study, not an official publication of …". Corner squares mark the margin.
- **Language.** The sheet speaks the institution's language (a Swiss lab writes German, an orbital archive English). Chinese follows `cjk-typography.md`.
- **Hero.** One data graphic computed from real data: a spectrum, a longitudinal profile, a packet header, a ray-path section, a ground track, a plan with dimension lines.
- **Instrument props.** A few elements borrowed from the instrument that produced the data make the sheet a reading, not an illustration: mode tags with the current mode in the brand color, a live dot with the time of the last acquisition, a fields table of parameters, a bill of parts. They are printed on the sheet; nothing is meant to be clicked.
- **Series.** Sheets of one series share header, footer, palette, type and motif; each has its own hero graphic and composition, numbered 01/03, 02/03 ….

## Archive card (person, equipment, place)

- Four layers: subject echo (the subject enlarged, one step off the ground); local name (title size, ink black, heaviest); reversed information bar (category, index, status); small labels and disclaimer fine print.
- The subject itself stays the sharpest thing on the card.
- The institution's emblem goes in one corner; a color control strip runs along the bottom edge.
- Arrange the four layers to suit the subject. Do not reuse the arrangement of any reference card.

## Slides or documents

- Apply the system throughout: corner index numbers, grid dots, page numbers written as archive numbers.
- One hero graphic per slide; text small and sparse, but no smaller than the `slides` minimum.
- Mark section changes with a dialect switch or a step-and-repeat transition.

## Photo treatment

- The photograph is material, not the finished piece: crop decisively, desaturate and cool it, overlay the dot screen or a halftone.
- Place it in one cell of the grid, or inside an aperture taken from the subject (`techniques.md` §3). Never let it fill the whole canvas.
