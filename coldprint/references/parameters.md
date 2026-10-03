# Parameters

Sizes below are given for a 1920×1080 canvas unless stated otherwise. For other canvases, scale by the short side (a value of 10px at 1080 becomes 20px at 2160).

## Palettes

The token names match `assets/poster-template.html`.

**Terminal dialect, dark ground**

| Token | Value | Use |
|---|---|---|
| `--ground` | `#0a1016` to `#0e1720` | Ground |
| `--ink` | `#e3e8ec` | Labels, hairlines |
| `--grey-1` | `#7a8a98` | Secondary labels, inactive tags |
| `--grey-2` | `#4a5866` | Grid dots, rulers, construction lines |

**Terminal dialect, light ground** (ice white or neutral grey)

| Token | Ice white | Neutral grey | Use |
|---|---|---|---|
| `--ground` | `#eef3f5` to `#dde6ea` | `#e4e7ea` to `#d6dade` | Ground |
| `--ink` | `#111417` | `#1d2329` | Labels, hairlines |
| `--grey-1` | `#bfe0e8` (ice blue) | `#8a939b` | Secondary, terrain, inactive |
| `--grey-2` | `#9fb3bb` | `#b3bac0` | Grid dots, rulers |

Ice white suits terrain, snow, medical and laboratory subjects; neutral grey suits equipment, labels and physical prints.

**Paper dialect**

| Token | Value | Use |
|---|---|---|
| `--ground` | `#f1f0e2` to `#e8e5d0` | Paper |
| `--ink` | `#141414` | Type, hairlines |
| `--grey-1` | `#8f8a4a` (deep olive) | Secondary labels |
| `--grey-2` | `#d9d4a0` (pale olive) | Grid, ghost type on paper |
| — | `#c9c27c` (olive) | Mid-tone fields |

**Brand color** (one per project)

Cyan `#2fc6d2`, signal orange `#e37222`, warning yellow `#f2c230`, acid green `#b8d400`, olive yellow `#cfc76e`. If the subject's institution has its own corporate color, use that instead.

A second saturated color appears at most as one tiny dot, or inside a color control strip (`techniques.md` §8).

## Latin type

All faces below are on Google Fonts under the SIL Open Font License, which permits embedding.

- **Labels and titles**, one wide face per project: Michroma; Archivo at `wdth` 110–125; Syncopate; Unbounded.
- **Numbers and small text**: Geist Mono, JetBrains Mono, IBM Plex Mono.
- **Heavy grotesque** (paper dialect): Archivo at `wdth` 100, weight 800–900; Inter Tight 800; Schibsted Grotesk 800.
- **Optional**: one classical serif (Cormorant, Instrument Serif) for a single ceremonial element only.

Settings:

- Labels 9–12px, tracking 0.12–0.18em, all caps. Index numbers up to 18–24px.
- Logo lockup no taller than 1/10 of the canvas height.
- No body paragraphs.
- Paper dialect: anchor words 1/8 to 1/5 of the canvas height.
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

`assets/poster-template.html` already contains the brushed light, blurred light, dot screen, grid dots, rulers, crop and registration marks, leader label, reversed bar, state tags and color control strip.
