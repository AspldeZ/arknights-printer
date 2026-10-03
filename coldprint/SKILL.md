---
name: coldprint
description: "Coldprint 冷印: designs posters, key visuals, logos, interfaces, slides, archive cards, photo treatments and image-generation prompts in a restrained cold-industrial visual-identity style. Every image is treated as a document issued by an institution: Swiss grid made visible, industrial labels that each have a function, one bold brand color, three layers of depth, small type. Derived from principles, never traced from references. Triggers: \"cold industrial\", \"industrial VI\", \"make it look like an institutional document\", \"coldprint\"; 「冷工业」「冷印」「工业 VI」「工业风海报」「做成冷工业风格」."
---

# Coldprint

A visual method that applies to any subject: posters, key visuals, logos, interfaces, slides, archive cards, photo treatments and image-generation prompts. It was distilled from contemporary game graphic design. This skill keeps the principles and none of the works.

## Host and language conventions

This skill runs on any agent that can write files (Claude apps, Claude Code, Codex and similar). HTML output is checked in a headless browser when one is available.

- **Before designing**, settle four things: output type and canvas size; issuing institution and what the document is for (or permission to invent both); dialect (§3); brand color. Ask only about what the request leaves open, as multiple choice, in one batch of at most four questions. Use the host's structured question tool if there is one. If the user says to go ahead without answering, use the defaults: 1920×1080 poster, terminal dialect on a dark ground, cyan brand color, an institution invented for the subject.
- **Language**: talk to the user in their language. On the canvas, short English labels are the default because they work as rhythm. When the audience reads Chinese, or the subject is Chinese, information-bearing lines go in Chinese and follow `references/cjk-typography.md`.
- **Working files** go in `coldprint-work/<slug>/` under the current working directory (or the host's scratch directory). Final files go to the host's output directory if it has one, otherwise `./output/`, and are delivered through whatever mechanism the host provides for sending files.
- **Scripts** live in `<skill-dir>/scripts/` and need Python 3. `render_check.py` also needs Playwright; `embed_fonts.py` needs network access to Google Fonts, or local font files.

## 0. Original, never traced

References exist to explain why something works, never to supply a composition. None of the following may be borrowed:

- a reference work's composition
- its logos, custom letterforms, event names, numbering systems, mascots, faction emblems, invented place or country names
- the name of any reference work or its publisher, anywhere in an image-generation prompt

Test: put the result next to the reference. If someone can point out "this part corresponds to that part", it is a tracing; start again.

The way to avoid tracing is to let the form grow out of the subject. First find the subject's own logic (its physics, process, data, history), then use this system to express it. The system is shared; the hero graphic belongs to this subject alone.

## 1. Every image is a document

Before designing, answer two questions:

1. **Which institution issued this?** A real one, or one invented for the subject.
2. **What is it for, inside that institution?** An archive page, an equipment label, a notice, an inspection report, an ID card, a manual, a monitoring screen, an annual-report insert.

Every index number, scale, coordinate, barcode and corner mark on the canvas must be explainable from that answer. Decoration with no function is deleted. Modernist form can carry any content; the tension comes from the gap between the content and the calm of the form.

If one world holds more than one institution, each speaks its own dialect (§3).

## 2. Eight principles

1. **Corporate identity and industrial labeling logic.** Index numbers, scales, section lines, crop marks, registration marks. Every element has a job.
2. **Swiss order with the grid made visible.** A strict grid, drawn out with dot markers, small corner squares and rulers. Centered or asymmetric, whichever holds the subject.
3. **Two grounds, both calm.** The terminal dialect uses a dark navy-black or a cold light ground; the paper dialect uses a warm off-white paper. Either one takes **exactly one saturated brand color**, laid in large flat areas, never sprinkled timidly. The number of hues is fixed; the amount of the one hue is not. Coldness comes from a low-saturation ground, flat light and restraint, not only from hue.
4. **Three layers of depth.**
   - Bottom: blurred light, motion streaks, out-of-focus objects or photographs.
   - Middle: a fine dot-matrix screen over the whole canvas.
   - Top: razor-sharp hairline vectors.

   The contrast in sharpness between layers is the main source of the finished, expensive look.
5. **One organic or playful intruder.** Something foreign enters the calm system: liquid, a biological form, terrain, handwriting, a small character. It must come from the subject itself.
6. **Small type.** Wide geometric sans, widely tracked, used for labels and rhythm. Visual weight goes to the graphics, not the words. A logo lockup may be somewhat larger and still restrained. Large type has exactly two legitimate roles: ghost type, in the ground's own hue one or two steps off in lightness, reading like a watermark and carrying no information; and the anchor word of a progressive sentence in the paper dialect (`references/techniques.md` §6).
7. **Matte surfaces, even flat light.** No gloss, no dramatic lighting. The single exception: wireframe images on a screen in the terminal dialect. In the world of the image they are light on a display, so they may glow, but the glow belongs to the lines, never to any surface.
8. **Restraint above everything.** Delete every element that is not needed. Leave large empty fields and concentrate detail in a few dense areas so that sparse and dense play against each other.

## 3. Dialects

When a world holds several institutions, they share one grammar (grid, labeling logic, restraint, a single brand color) and each speaks a dialect. Switching institution switches dialect: ground, type weight, color temperature and rendering all change at once, so the viewer knows the sender has changed without reading a word.

| | Terminal | Paper |
|---|---|---|
| Character | Internal screens of a dispatch, monitoring, medical or military body | Research institute, publication, corporate annual report |
| Ground | Dark navy-black; or a cold light ground (ice white, neutral light grey), often with terrain | Off-white paper, fine grid or none |
| Brand color | Cyan | Olive yellow or ochre |
| Type | Monospace and wide sans, all caps, all small | Heavy grotesque, extreme size contrast |
| Graphics | Blueprints, wireframes, HUD leader lines | Diagrams, cropped photographs, geometric color blocks |
| Texture | Pixel noise, scan lines, self-lit wireframes | Soft-focus photography, paper, step-and-repeat |

Rules:

- One image uses one dialect.
- The brand colors above are defaults. If the subject's institution has its own corporate color, that color wins.
- **Type in the terminal dialect stays small throughout.** Ghost type is allowed because it is texture, not information. Progressive sentences and anchor words belong to the paper dialect.
- A new dialect may be invented for a subject, but all six rows must be filled in before drawing starts, and it must keep the shared grammar.

## 4. Not this

These break the system even when every rule above seems satisfied:

- Gloss, bevels, chrome, rim light, lens flares.
- Several saturated hues glowing together (neon cyberpunk).
- Hexagon fields, circuit traces, random HUD rings, fake code: industrial detail with no function.
- A large headline carrying the image.
- Grunge, distressed textures, drop shadows, two-hue or rainbow gradients.
- Detail spread evenly everywhere, with no empty field.

## 5. Workflow

1. **Research the subject.** Collect real information: data, coordinates, years, formulas, processes, terminology. Graphics driven by data are more convincing than invented ornament.
2. **One-line concept.** State the core of the image in one sentence, such as "analog turning into digital" or "a field growing inside a grid".
3. **Dialect and cartographic genre.** Fix the issuing institution's dialect (§3) and pick one cartographic genre (`references/techniques.md` §1).
4. **Hero and intruder.** The canvas has exactly one hero graphic, and it belongs to this subject alone. Then decide what the intruder is.
5. **Apply the system.** Grid, palette, type and labels follow `references/parameters.md`; Chinese text follows `references/cjk-typography.md`; the output type follows `references/outputs.md`; image-generation prompts come from `references/image-prompts.md`.
6. **Build the three layers.** For HTML, start from `assets/poster-template.html`.
7. **Check.** Render, run `scripts/render_check.py`, fix what it reports, then go through §6 and the originality test in §0.
8. **Deliver.** Inline fonts with `scripts/embed_fonts.py` so the file renders the same on any machine. Send the PNG and the self-contained HTML.

For several images on one subject, each hero graphic and composition must be clearly different; only the system is shared (palette, type, label language, logo). If the images belong to different institutions, the dialect switches with the institution and the grammar stays.

## 6. Self-check

- [ ] The issuing institution and the document's purpose can be named.
- [ ] The dialect can be named, and the image does not mix two.
- [ ] The hero graphic belongs to this subject alone and has no part-by-part correspondence with any reference.
- [ ] There is exactly one saturated brand color, used boldly. Other saturated colors appear only as a tiny dot or a color control strip.
- [ ] The brand color marks a state, a selection, or a whole color field, never scattered accents.
- [ ] All three layers of depth are present.
- [ ] There is one intruder, and it comes from the subject.
- [ ] Large type is either low-contrast ghost type or, in the paper dialect, the anchor word of a progressive sentence; all other text is labels and rhythm.
- [ ] Every frame and mask shape can be traced to the subject.
- [ ] Every industrial detail has a nameable function.
- [ ] There is enough empty space, and detail is concentrated in a few areas.
- [ ] Ground calm, surfaces matte, light flat; glow only on screen wireframes in the terminal dialect.
- [ ] Text is no smaller than the minimum for the output medium (`references/parameters.md`).
- [ ] Facts and data are verified, and their sources are cited in the document's fine print.

## Files

| File | Read when |
|---|---|
| `references/techniques.md` | Choosing a cartographic genre, frames, label placement, type scale and form operations (step 3 onward) |
| `references/parameters.md` | Building anything: palettes, Latin type, minimum sizes per medium, layout, texture recipes for HTML/SVG |
| `references/cjk-typography.md` | Any Chinese (or Japanese) text on the canvas |
| `references/outputs.md` | Per output type: poster, logo, interface, archive card, slides, photo treatment |
| `references/image-prompts.md` | Writing a prompt for an image-generation model |
| `assets/poster-template.html` | Starting an HTML poster or key visual |
| `scripts/render_check.py` | After every HTML render |
| `scripts/embed_fonts.py` | Before delivering HTML |
