---
name: arknights-industrial
description: "Arknights Industrial 舟工业 (unofficial): designs game-style interfaces, key visuals, posters, emblems, archive cards, infographics, slides and image-generation prompts in an industrial sci-fi visual language. Every image is a document issued by an institution: one motif from its emblem, Swiss grid made visible, labels that each have a function, one bold brand color, three layers of depth, small type. Derived from principles, never traced from references. Triggers: \"Arknights style\", \"Endfield style\", \"industrial sci-fi UI\", \"industrial VI\"; 「舟工业」「方舟风」「终末地风格」「工业风界面」「工业 VI」「冷工业」."
---

# Arknights Industrial

A visual method for industrial sci-fi graphic design. It was distilled from contemporary game graphic design; this skill keeps the principles and none of the works. It applies to any subject, real or invented.

## Scope

| Makes | How |
|---|---|
| Game-style interfaces: event hub, mission list, shop, stage map, archive card, notice | HTML/SVG, finished quality |
| Key visuals and posters: title lockup, layout, graphics | HTML/SVG; photographic or 3D backgrounds come from an image model or the user |
| Emblems, wordmarks, construction sheets | HTML/SVG |
| Infographics: route diagrams, cross-sections, data graphics | HTML/SVG |
| Slides | HTML, one slide per artboard |
| Background plates: environments, materials | A prompt for an image-generation model (`references/image-prompts.md`), then the HTML layers sit on top |

Out of scope: character illustration, animation.

## Host and language conventions

This skill runs on any agent that can write files (Claude apps, Claude Code, Codex and similar). HTML output is checked in a headless browser when one is available.

- **Before designing**, settle four things: output type and canvas size; issuing institution and what the document is for (or permission to invent both); dialect (§3); brand color. Ask only about what the request leaves open, as multiple choice, in one batch of at most four questions. Use the host's structured question tool if there is one. If the user says to go ahead without answering, use the defaults: 1920×1080, field dialect, signal yellow, an institution invented for the subject.
- **Language**: talk to the user in their language. On the canvas, short English labels are the default because they work as rhythm. When the audience reads Chinese, or the subject is Chinese, information-bearing lines go in Chinese and follow `references/cjk-typography.md`.
- **Working files** go in `ark-work/<slug>/` under the current working directory (or the host's scratch directory). Final files go to the host's output directory if it has one, otherwise `./output/`, and are delivered through whatever mechanism the host provides for sending files.
- **Scripts** live in `<skill-dir>/scripts/` and need Python 3. `render_check.py` also needs Playwright; `bundle.py` needs network access to Google Fonts, or local font files.

## 0. Original, never traced

References exist to explain why something works, never to supply a composition. None of the following may be borrowed:

- a reference work's composition or screen layout
- its logos, emblems, custom letterforms, event names, numbering systems, mascots, faction marks, invented place or country names
- the name of any reference work, studio or publisher, anywhere in an image-generation prompt

Test: put the result next to the reference. If someone can point out "this part corresponds to that part", it is a tracing; start again.

The way to avoid tracing is to let the form grow out of the subject. First find the subject's own logic (its physics, process, data, history), then use this system to express it. The system is shared; the hero graphic and the motif belong to this subject alone.

## 1. Every image is a document

Before designing, answer two questions:

1. **Which institution issued this?** A real one, or one invented for the subject.
2. **What is it for, inside that institution?** An operations terminal, an archive page, an equipment label, a notice, an inspection report, an ID card, a manual, a requisition list, an annual-report insert.

Every index number, scale, coordinate, barcode and corner mark must be explainable from that answer. Decoration with no function is deleted. Modernist form can carry any content; the tension comes from the gap between the content and the calm of the form.

If one world holds more than one institution, each speaks its own dialect (§3).

## 2. Nine principles

1. **Corporate identity and industrial labeling logic.** Index numbers, scales, section lines, crop marks, registration marks, barcodes, hazard markings. Every element has a job.
2. **One motif, taken from the emblem.** Choose one geometric primitive that comes from the subject (a triangle, a chamfered square, a ring, a bracket) and build the emblem from it. Then reuse its parts everywhere: button ends, frame corners, dividers, loading marks, large ghost shapes in the background. One primitive, many sizes, so every screen reads as the same institution.
3. **Swiss order with the grid made visible.** A strict grid, drawn out with dot markers, small corner squares, registration crosses and rulers. Centered or asymmetric, whichever holds the subject.
4. **A calm ground and exactly one saturated brand color.** The ground is near-white, cold light grey, dark navy-black or off-white paper, depending on the dialect. The brand color is laid in large flat areas, never sprinkled timidly. The number of hues is fixed; the amount of the one hue is not. Photographs, renders and illustrations are desaturated toward grey so that the brand color is the only saturated thing on the canvas.
5. **Three layers of depth.**
   - Bottom: blurred light, motion streaks, out-of-focus objects, desaturated photographs or renders.
   - Middle: a fine dot-matrix screen over the whole canvas.
   - Top: razor-sharp hairline vectors and UI panels.

   The contrast in sharpness between layers is the main source of the finished, expensive look.
6. **One organic or playful intruder.** Something foreign enters the calm system: liquid, a biological form, terrain, handwriting, a small character, breakage. It must come from the subject itself.
7. **Small type.** Wide or condensed sans, widely tracked, used for labels and rhythm. Visual weight goes to the graphics, not the words. A logo lockup or event title may be larger and still restrained. Large type has exactly two legitimate roles: ghost type, in the ground's own hue one or two steps off in lightness, reading like a watermark and carrying no information; and an anchor word or event title (`references/techniques.md` §6).
8. **Matte surfaces, even flat light.** No gloss, no dramatic lighting. Two exceptions: wireframes on a screen may glow (in the world of the image they are light on a display), and interface panels may be frosted and translucent. Glow belongs to lines, never to surfaces.
9. **Restraint above everything.** Delete every element that is not needed. Leave large empty fields and concentrate detail in a few dense areas so that sparse and dense play against each other.

## 3. Dialects

All dialects share one grammar (the nine principles). An institution speaks one dialect; switching institution switches dialect, so the viewer knows the sender has changed without reading a word. The differences are deliberately small: ground, brand color, type weight, texture.

| | Field | Terminal | Paper | Wartime |
|---|---|---|---|---|
| Character | A frontier construction or engineering company: its own terminals, signage and requisition forms | Internal screens of a dispatch, monitoring, medical or military body | Research institute, publication, annual report | An institution at war or in ruins: orders, casualty lists, recovered files |
| Ground | Near-white, with dark panels where needed | Dark navy-black, or ice white | Off-white paper | Light grey, with charcoal panels |
| Brand color | Signal yellow | Cyan | Olive yellow or ochre | Crimson |
| Type | Condensed or wide sans, all caps, with mono | Mono and wide sans, all caps, all small | Heavy grotesque, extreme size contrast | Heavy condensed display for one title; small labels elsewhere |
| Graphics | Chamfered panels, hazard stripes, thick accent bars, corner brackets, facility layouts, flow diagrams | Blueprints, wireframes, HUD leader lines | Diagrams, cropped photographs, geometric color blocks | Grey imagery split by brand-color cuts, the motif at large scale, routed node maps |
| Texture | Dot matrix, contour-line fills, light grain, frosted panels | Pixel noise, scan lines, self-lit wireframes | Soft-focus photography, paper, step-and-repeat | Distressed print, ink, cracks |

Rules:

- One image uses one dialect. A series may switch dialect between images when the institution switches.
- The brand colors above are defaults. If the subject's institution has its own corporate color, that color wins.
- Type in the terminal dialect stays small throughout; ghost type is allowed because it is texture, not information.
- Distress, ink and breakage belong to the wartime dialect, and only when the story is about damage.
- **Regional variants.** The same institution working in a different region keeps its dialect and brand color; only the bottom layer changes material: rust and dust for a wasteland, mist and ink-wash mountains for a river valley, snow and ice for a polar station. The ground may shift a few points in temperature to follow.
- A new dialect may be invented for a subject, but all six rows must be filled in before drawing starts, it must keep the shared grammar, and it must stay within industrial sci-fi.

## 4. Not this

These break the system even when every rule above seems satisfied:

- Gloss, bevels, chrome, rim light, lens flares.
- Several saturated hues glowing together (neon cyberpunk).
- Hexagon fields, circuit traces, random HUD rings, fake code, hazard stripes where nothing is hazardous: industrial detail with no function.
- A large headline carrying a poster on its own.
- Drop shadows, two-hue or rainbow gradients, grunge used as decoration.
- Detail spread evenly everywhere, with no empty field.

## 5. Workflow

1. **Research the subject.** Collect real information: data, coordinates, years, formulas, processes, terminology. Graphics driven by data are more convincing than invented ornament.
2. **One-line concept.** State the core of the image in one sentence, such as "analog turning into digital" or "a field growing inside a grid".
3. **Institution, dialect, motif.** Name the issuing institution, fix its dialect (§3), and choose the motif (principle 2). Pick one cartographic genre (`references/techniques.md` §1).
4. **Hero and intruder.** The canvas has exactly one hero graphic, and it belongs to this subject alone. Then decide what the intruder is.
5. **Apply the system.** Grid, palette, type and labels follow `references/parameters.md`; Chinese text follows `references/cjk-typography.md`; the output type follows `references/outputs.md`; image-generation prompts come from `references/image-prompts.md`.
6. **Build.** For HTML, start from the matching file in `assets/templates/`; all templates share `assets/kit.css`.
7. **Check.** Render, run `scripts/render_check.py`, fix what it reports, then go through §6 and the originality test in §0.
8. **Deliver.** Run `scripts/bundle.py` to inline the stylesheet and the subsetted fonts, so the file renders the same on any machine. Send the PNG and the self-contained HTML.

For several images on one subject, each hero graphic and composition must be clearly different; only the system is shared (palette, type, label language, motif, emblem).

## 6. Self-check

- [ ] The issuing institution and the document's purpose can be named.
- [ ] The dialect can be named, and the image does not mix two.
- [ ] The motif comes from the subject and recurs at several scales.
- [ ] The hero graphic belongs to this subject alone and has no part-by-part correspondence with any reference.
- [ ] There is exactly one saturated brand color, used boldly. Imagery is desaturated. Other saturated colors appear only as a tiny dot or a color control strip.
- [ ] The brand color marks a state, a selection, or a whole color field, never scattered accents.
- [ ] All three layers of depth are present.
- [ ] There is one intruder, and it comes from the subject.
- [ ] Large type is either low-contrast ghost type, an anchor word, or the one title; all other text is labels and rhythm.
- [ ] Every frame and mask shape can be traced to the subject or the motif.
- [ ] Every industrial detail has a nameable function, hazard stripes included.
- [ ] There is enough empty space, and detail is concentrated in a few areas.
- [ ] Surfaces matte, light flat; glow only on screen wireframes.
- [ ] Text is no smaller than the minimum for the output medium (`references/parameters.md`).
- [ ] Facts and data are verified, and their sources are cited in the document's fine print.

## Files

| File | Read when |
|---|---|
| `references/techniques.md` | Choosing a cartographic genre, the motif system, frames, labels, type scale, form operations |
| `references/parameters.md` | Building anything: palettes, Latin type, minimum sizes per medium, layout, texture recipes |
| `references/cjk-typography.md` | Any Chinese (or Japanese) text on the canvas |
| `references/outputs.md` | Per output type: interfaces, key visual, emblem, archive card, slides, photo treatment |
| `references/image-prompts.md` | Writing a prompt for an image-generation model |
| `assets/kit.css` | Tokens for the four dialects and the shared components |
| `assets/templates/*.html` | Starting any HTML output |
| `scripts/render_check.py` | After every HTML render |
| `scripts/bundle.py` | Before delivering HTML |
