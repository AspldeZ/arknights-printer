# Image-generation prompts

Treat whatever the user provides (a photograph, a sketch, a one-line idea) as the subject. Attach one of the two master prompts below unchanged, then add optional lines.

Never put the name of a reference work, studio or publisher in the prompt.

## Master prompt: terminal dialect

```
Reinterpret this as part of a corporate visual identity for a fictional industrial institution.
Swiss modernist order with the grid made visible: dot markers, corner squares, rulers. Centered or asymmetric, whichever holds the subject.
Industrial labeling logic: index numbers, scales, section lines, each with a clear function.
Palette: cold grey and cold blue, with one saturated brand color used boldly in large flat areas.
Layered depth: blurred light and motion streaks beneath, a fine dot-matrix screen over everything, razor-sharp hairline vectors on top.
One organic or playful intrusion into the industrial system.
Text stays small: wide geometric sans and monospace, widely tracked, all caps, used as rhythm and labels. The image carries the weight, not the words.
Matte surfaces, even light, restraint above all. Only hairline wireframes on screens may glow.
```

## Master prompt: paper dialect

```
Reinterpret this as part of a corporate visual identity for a fictional research institution's printed publication.
Swiss modernist order with the grid made visible: dot markers, corner squares, rulers. Centered or asymmetric, whichever holds the subject.
Industrial labeling logic: index numbers, scales, section lines, each with a clear function.
Palette: off-white paper and ink black, with one saturated brand color (olive yellow or ochre) used boldly in large flat areas.
Layered depth: soft-focus photography beneath, a fine dot-matrix screen over everything, razor-sharp hairline vectors on top.
One organic or playful intrusion into the industrial system.
Type: heavy grotesque, all small; labels widely tracked; no large lettering.
Matte paper, even light, no glow, restraint above all.
```

## Optional lines

- `Format: poster / identity sheet / archive file / label / monitoring screen`
- `Ground: dark / light` (terminal dialect)
- `Brand color: cyan / signal orange / warning yellow / acid green / olive yellow`
- `Cartography: blueprint / isometric wireframe / shaded relief map / transit diagram / cross-section`
- `Show the subject in two representational states at once, switching along one axis.`
- `In a list of grey category tags, mark exactly one in the brand color; add a live timestamp.`
- `Frame the subject through an aperture shaped like <a shape taken from the subject>.`

## Text in generated images

- Keep titles short and in English; image models still misspell long or non-Latin text.
- If the text comes out wrong, follow up with: `Keep everything identical, only fix the text: "<exact text>"`.
- For Chinese titles, generate the image without text and set the Chinese in HTML on top of it, following `cjk-typography.md`.
