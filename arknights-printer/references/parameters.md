# Parameters

Sizes below are given for a 1920×1080 canvas unless stated otherwise. For other canvases, scale by the short side (a value of 10px at 1080 becomes 20px at 2160).

## Palettes

Token names match `assets/kit.css`, where each dialect is a `data-dialect` value. `--panel` is the dark surface used for panels and bars on light grounds.

| Token | Field | Terminal (dark) | Terminal (ice) | Paper | Wartime | Use |
|---|---|---|---|---|---|---|
| `--ground` | `#f2f2ef` | `#0b121a` | `#e8eff2` | `#efeee0` | `#dcdcda` | Ground |
| `--surface` | `#fafaf8` | `#121c26` | `#f4f8f9` | `#f6f5ea` | `#ececea` | Raised panels, cards |
| `--panel` | `#1c1c1c` | `#06090d` | `#111417` | `#141414` | `#232323` | Dark panels, reversed bars |
| `--ink` | `#191919` | `#e3e8ec` | `#111417` | `#141414` | `#161616` | Type, hairlines |
| `--grey-1` | `#6e6e6a` | `#7a8a98` | `#6f8790` | `#77723c` | `#6b6b6b` | Secondary labels, inactive states |
| `--grey-2` | `#c4c4be` | `#4a5866` | `#9fb3bb` | `#c9c48e` | `#b5b5b3` | Grid dots, rulers, borders |
| `--ghost` | `#e6e6e2` | `#131e29` | `#dae4e8` | `#e3e1c9` | `#cfcfcd` | Ghost shapes (the motif, very large, one step off the ground) |
| `--brand` | `#fff200` | `#2fc6d2` | `#2fc6d2` | `#cfc76e` | `#c8102e` | The one saturated color |
| `--on-brand` | `#191919` | `#0b121a` | `#111417` | `#141414` | `#ffffff` | Text on the brand color |
| `--bar-bg` / `--bar-fg` | panel / on-panel | ink / ground | panel / on-panel | panel / on-panel | panel / on-panel | Reversed bar: always the reverse of the ground |
| `--alert` | `#e5383b` | `#ff5a5f` | `#e0383e` | `#c0392b` | brand | Status: danger, locked, failed |
| `--timed` | `#f28c28` | `#ffa630` | `#ef8a1f` | `#d9822b` | `#d9822b` | Status: time-limited, expiring |
| `--counter` | — | — | — | — | — | Optional counter color, declared per sheet or series |

Notes:

- **Signal yellow on a light ground** is a fill, never a text color: yellow type on near-white is unreadable. Put ink type on yellow, or yellow on `--panel`.
- **Neutral grey** (`#e4e7ea` to `#d6dade`, ink `#1d2329`) is an alternative light ground for the terminal dialect when the subject is equipment, labels or physical prints.
- **Other brand colors**: signal orange `#e37222`, warning yellow `#f2c230`, acid green `#b8d400`. If the subject's institution has its own corporate color, use that instead.
- **Status colors** (`--alert`, `--timed`) appear only as small tags, badges and icons on the item whose state they report, never as decoration. Together they stay under 1% of the canvas area.
- **Counter color** (`--counter`, set on `.artboard` to declare it): one per sheet or series, far from the brand hue on the wheel (deep blue `#1f3bd6` against signal yellow, for example). It colors index numerals, emphasis words and hairlines; the `.counter` class applies it. Never a panel fill or a large field: under 3% of the canvas area.
- Any other saturated color appears at most as one tiny dot, or inside a color control strip (`techniques.md` §8).
- `render_check.py` reads `--brand`, `--counter`, `--alert` and `--timed` from the artboard and checks each hue against these limits.
- **Grey with temperature.** Large neutral areas keep a trace of warm or cool (a few points of chroma), never dead grey or a plain two-stop gradient. White is an off-white with a trace of grey.
- **Steps within one hue.** When one hue needs several values, lighter steps lean slightly cooler and darker steps slightly warmer, all inside a narrow hue range.

## Latin type

All faces below are on Google Fonts under the SIL Open Font License, which permits embedding.

- **Labels and the title**, one wide face per project: Michroma; Archivo at `wdth` 110–125; Syncopate; Unbounded.
- **Numbers and small text**: Geist Mono, JetBrains Mono, IBM Plex Mono.
- **Condensed** (field and wartime dialects): Archivo at `wdth` 62–75; Saira Condensed; Barlow Condensed.
- **Heavy grotesque** (paper dialect): Archivo at `wdth` 100, weight 800–900; Inter Tight 800; Schibsted Grotesk 800.
- **Optional**: one classical serif (Cormorant, Instrument Serif) for a single ceremonial element only.

Settings:

- Labels 9–12px, tracking 0.12–0.18em, all caps. Index numbers up to 18–24px.
- Logo lockup no taller than 1/10 of the canvas height.
- No body paragraphs.
- Formulas and symbols (T = 2π √(L/g), φ, δ, units like km/s) inside uppercase labels go in `.formula`, which keeps their case; load Noto Sans Math when they use √, π or Greek letters, or `render_check.py` reports a fallback font.
- No large type. The title or index number is the largest text, about three times the label size: 24–32px for `screen`, about 40px for `feed`.
- Ghost shapes (not type): lightness differs from the ground by 6–12 points (OKLCH L).

## Canvas sizes

Set `--w` / `--h` on `.artboard`; the sheet frame in `kit.css` and the helpers in `kit.js` follow the board.

| Format | Board | Render | Medium |
|---|---|---|---|
| Landscape screen | 1920×1080 | `--scale 1` | `screen` |
| 4K | 1920×1080 | `--scale 2` (3840×2160) | `screen` |
| Portrait feed | 1080×1350 | `--scale 1` | `feed` |
| Square | 1080×1080 | `--scale 1` | `feed` |

A portrait or square sheet is a new composition, not a shrunken landscape one: the hero goes on top and takes the width, the column of tags and fields goes below, and the feed minimum makes every label larger, so there is room for fewer of them.

## Minimum text size by medium

The 9px label is a full-screen size. Text that will be seen smaller needs more. Values are for the short side of the canvas at 1080px; `render_check.py --medium` uses the same table.

| Medium | Minimum | Typical viewing |
|---|---|---|
| `screen` | 9px | Full-screen display, wallpaper, poster file opened at full size |
| `feed` | 14px | Social media, phone screen, thumbnails |
| `slides` | 16px | Projected or shared-screen slides |
| `print` | 6pt at final print size | Printed matter; check at 100% print size |

Color control strips and decorative numerals on scales are exempt; mark them with `data-role="ghost"` or `data-role="texture"` so the checker skips them.

## Layout

- Outer margin at least 5% of the canvas width.
- Grid dot spacing about 1/10 of the canvas width.
- Hairlines 1–1.5px. Brand-color areas are solid flat fills or hatching.
- Reversed bar: height about 1.8× its font size; horizontal padding about 0.6× the font size.
- Leader-line end dot: hollow circle, diameter 6–8× the line width.
- Sources: a single fine-print line, prefixed `SRC` (or `来源`), in the document's footer zone, as an archive would cite them.

## Texture recipes (HTML/SVG)

- **Brushed light**: SVG `feTurbulence` with `baseFrequency="0.01 0.0007"` (vertical streaks) or the reverse (horizontal), tinted cold with `feColorMatrix`, lightly blurred along the streak direction.
- **Blurred light**: large ellipses or polygons with `feGaussianBlur`, `stdDeviation` 30–80.
- **Dot-matrix screen**: a `radial-gradient` dot, `background-size: 4px 4px`; 7% white on dark grounds, 7% ink on light grounds.
- **Depth interleaving**: split one group of graphics into two SVG layers, one behind the subject and one in front, so 2D graphics seem to pass through a 3D object.
- **Labels on the floor**: CSS `transform: perspective(1200px) rotateX(55deg) rotateZ(-20deg)`, or an SVG `matrix` transform, so the text shares the floor plane.
- **Self-lit wireframe** (terminal dialect only): duplicate the stroke, blur the copy with `stdDeviation` 1.5–3, and composite it under the original line. Never apply glow to a filled surface.
- **Step-and-repeat**: generate SVG `<use>` copies in a loop, each translated by a fixed step and one lightness step darker.
- **Mirror crop**: `scaleY(-1)` with a linear-gradient `mask-image` that keeps only the top half.
- **Film grain** (dark, rendered subjects): `feTurbulence` with `baseFrequency` 0.8–1.2 and `numOctaves="1"`, blended with `overlay` at 8–15% opacity.
- **Pixel breakup**: at the object's edge, replace the continuous shape with grid squares whose side is a whole fraction of the dot spacing, thinning out with distance from the subject.
- **Hazard stripes**: `repeating-linear-gradient(-45deg, var(--brand) 0 8px, var(--panel) 8px 16px)`.
- **Chamfer**: `clip-path: polygon(0 0, calc(100% - 8px) 0, 100% 8px, 100% 100%, 0 100%)` cuts the top-right corner by 8px.
- **Frosted panel**: `background: color-mix(in srgb, var(--surface) 72%, transparent); backdrop-filter: blur(14px);`.
- **Contour-line fill**: a few SVG paths offset from one closed curve, 1px, `--grey-2`, inside a plate or panel only.
- **Distressed print** (wartime): an SVG mask made of `feTurbulence` (`baseFrequency` 0.5–0.9) pushed through `feComponentTransfer` with a hard threshold, applied to the title only.
- **Desaturated imagery**: CSS `filter: grayscale(1) contrast(1.05)`, or `grayscale(.85)` to keep a trace of temperature.

`assets/kit.css` and the templates already contain the brushed light, blurred light, dot screen, grid dots, rulers, crop and registration marks, leader label, reversed bar, state tags, chamfered panels, hazard stripes, accent bars, corner brackets and color control strip.
