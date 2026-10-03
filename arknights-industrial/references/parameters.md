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
| `--ghost` | `#e6e6e2` | `#131e29` | `#dae4e8` | `#e3e1c9` | `#cfcfcd` | Ghost type and ghost shapes |
| `--brand` | `#fff200` | `#2fc6d2` | `#2fc6d2` | `#cfc76e` | `#c8102e` | The one saturated color |
| `--on-brand` | `#191919` | `#0b121a` | `#111417` | `#141414` | `#ffffff` | Text on the brand color |

Notes:

- **Signal yellow on a light ground** is a fill, never a text color: yellow type on near-white is unreadable. Put ink type on yellow, or yellow on `--panel`.
- **Neutral grey** (`#e4e7ea` to `#d6dade`, ink `#1d2329`) is an alternative light ground for the terminal dialect when the subject is equipment, labels or physical prints.
- **Other brand colors**: signal orange `#e37222`, warning yellow `#f2c230`, acid green `#b8d400`. If the subject's institution has its own corporate color, use that instead.
- A second saturated color appears at most as one tiny dot, or inside a color control strip (`techniques.md` §8).
- **System chrome** in interfaces (back and home buttons, global navigation) uses `--panel`, `--ink` and greys only, never the brand color, so the event's brand color stays the only saturated hue (`outputs.md`, Interfaces).

## Latin type

All faces below are on Google Fonts under the SIL Open Font License, which permits embedding.

- **Labels and titles**, one wide face per project: Michroma; Archivo at `wdth` 110–125; Syncopate; Unbounded.
- **Numbers and small text**: Geist Mono, JetBrains Mono, IBM Plex Mono.
- **Condensed** (field and wartime dialects): Archivo at `wdth` 62–75; Saira Condensed; Barlow Condensed. For the one heavy title: Archivo at `wdth` 62, weight 900; Anton; Big Shoulders Display 900.
- **Heavy grotesque** (paper dialect): Archivo at `wdth` 100, weight 800–900; Inter Tight 800; Schibsted Grotesk 800.
- **Optional**: one classical serif (Cormorant, Instrument Serif) for a single ceremonial element only.

Settings:

- Labels 9–12px, tracking 0.12–0.18em, all caps. Index numbers up to 18–24px.
- Logo lockup no taller than 1/10 of the canvas height.
- No body paragraphs.
- Paper dialect: anchor words 1/8 to 1/5 of the canvas height.
- Event title (field and wartime): up to a quarter of the canvas width.
- Ghost type: a quarter of the canvas height or more; its lightness (OKLCH L or HSL L) differs from the ground by 6–12 points.

## Minimum text size by medium

The 9px label is a full-screen size. Text that will be seen smaller needs more. Values are for the short side of the canvas at 1080px; `render_check.py --medium` uses the same table.

| Medium | Minimum | Typical viewing |
|---|---|---|
| `screen` | 9px | Full-screen display, wallpaper, poster file opened at full size |
| `feed` | 14px | Social media, phone screen, thumbnails |
| `slides` | 16px | Projected or shared-screen slides |
| `print` | 6pt at final print size | Printed matter; check at 100% print size |

Ghost type, color control strips and decorative numerals on scales are exempt; mark them with `data-role="ghost"` or `data-role="texture"` so the checker skips them.

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
- **Contour-line fill**: a few SVG paths offset from one closed curve, 1px, `--grey-2`, inside a button or panel only.
- **Distressed print** (wartime): an SVG mask made of `feTurbulence` (`baseFrequency` 0.5–0.9) pushed through `feComponentTransfer` with a hard threshold, applied to the title only.
- **Desaturated imagery**: CSS `filter: grayscale(1) contrast(1.05)`, or `grayscale(.85)` to keep a trace of temperature.

`assets/kit.css` and the templates already contain the brushed light, blurred light, dot screen, grid dots, rulers, crop and registration marks, leader label, reversed bar, state tags, chamfered panels, hazard stripes, accent bars, corner brackets and color control strip.
