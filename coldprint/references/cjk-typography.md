# CJK typography

The Latin rules in `parameters.md` (all caps, tracking 0.12–0.18em, 9px labels) were written for alphabetic text and do not carry over to Chinese. This file replaces them for Chinese text; for Japanese, substitute the JP version of each face.

## Faces

- **Everything by default**: Noto Sans SC (思源黑体). Labels 500–700; titles and anchor words 900. At label sizes, 400 is too thin on a dark ground and 900 clogs.
- **One ceremonial element** (optional, mirrors the Latin serif rule): Noto Serif SC 900.
- **Handwriting as an intruder**: use real handwriting, scanned or drawn, rather than a calligraphy font. A calligraphy font used as decoration breaks principle 8.

All are on Google Fonts under the SIL Open Font License. CJK fonts are large; always subset them with `scripts/embed_fonts.py`, which keeps only the characters used.

## Labels

- **No case, so rhythm comes from weight and spacing.** Keep one weight and one size for all Chinese labels of the same rank.
- **Tracking 0.04–0.1em.** Wider tracking turns a word into a row of separate characters. The one exception is a fixed tag of two to four characters (档案编号, 状态), which may be spaced out to match the width of the Latin label it sits beside.
- **Size**: at least 2px larger than the Latin label size, so at least 11px on a 1920×1080 screen canvas. Chinese strokes are dense and fail before Latin letters do. The per-medium minimums in `parameters.md` apply to Chinese text plus 2px.
- **Numbers and Latin inside Chinese labels** use the monospace face. Put the monospace face first in the font stack, `font-family: "Geist Mono", "Noto Sans SC", sans-serif;`, so digits and Latin take the mono and Chinese falls through to Noto Sans SC.
- **Punctuation**: labels carry no full-width punctuation. Separate fields with a space, `/`, `·` or `—`.

## Bilingual pairs

A bilingual label is two lines: one leads, one follows. Decide once per document which language leads and keep it everywhere.

- Chinese leads: Chinese line in ink at label size; English line below in caps, one size smaller, `--grey-1`.
- English leads: the reverse.

Never set both lines at the same size and color; the pair then reads as two competing labels.

## Large type

- **Anchor words** (paper dialect): two to four characters, weight 900, tracking −0.02em at sizes above 1/8 of the canvas height. The 2.5× step rule from `techniques.md` §6 applies unchanged.
- **Progressive sentences**: break at word boundaries, never inside a word, and never leave a single character alone on a line. Set each line as its own element; do not rely on automatic wrapping.
- **Ghost type**: one or two characters work better than a full name. A single character at half the canvas height reads as texture almost at once.
- **Sentence punctuation**: in a progressive sentence either use full-width punctuation correctly or drop the final full stop. Do not mix.

## Vertical setting

A vertical column of Chinese along a side rail reads like the spine label on a piece of equipment or a file folder, and fits the labeling logic.

- `writing-mode: vertical-rl;`
- Latin words inside a vertical line lie on their side (`text-orientation: mixed;`).
- One- or two-digit numbers stand upright with `text-combine-upright: digits 2;` (or `all` on the wrapping span).
- One vertical column per image, used as a rail, not as body text.

## Alignment

Chinese glyphs fill a square box while Latin capitals sit on a baseline. In a reversed bar or next to a Latin label, Noto Sans SC tends to sit slightly high: check the render and nudge by 0.05–0.08em if needed.
