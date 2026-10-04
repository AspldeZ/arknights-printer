---
name: arknights-printer
description: "Arknights Printer 舟工业 (unofficial): designs posters, key visuals and information sheets about real-world subjects (a measurement, a structure, a process, a place), plus emblems, archive cards, slides and image-generation prompts, in an industrial sci-fi visual language. Every image is a document issued by an institution: one motif from its emblem, Swiss grid made visible, labels that each have a function, one bold brand color, three layers of depth, small type. Derived from principles, never traced from references. Triggers: \"Arknights style\", \"Endfield style\", \"industrial sci-fi UI\", \"industrial VI\"; 「舟工业」「方舟风」「终末地风格」「工业风界面」「工业 VI」「冷工业」."
---

# Arknights Printer

A visual method for industrial sci-fi graphic design. It was distilled from contemporary game graphic design; this skill keeps the style and none of the works or their patterns. Its output is never a game screen: it is a poster or information sheet about a real subject (a lab measurement, a glacier, a network protocol, a planet's core, a space station), set as a document that a real or invented institution could have issued.

## Scope

| Makes | How |
|---|---|
| Posters and information sheets about a real subject, single or as a numbered series | HTML/SVG, finished quality |
| Key visuals: layout and graphics with a small title lockup | HTML/SVG; photographic or 3D backgrounds come from an image model or the user |
| Archive cards for a person, piece of equipment or place | HTML/SVG |
| Emblems, wordmarks, construction sheets | HTML/SVG |
| Infographics: route diagrams, cross-sections, data graphics | HTML/SVG |
| Slides | HTML, one slide per artboard |
| Background plates: environments, materials | A prompt for an image-generation model (`references/image-prompts.md`), then the HTML layers sit on top |

Out of scope: character illustration, animation.

## Host and language conventions

This skill runs on any agent that can write files (Claude apps, Claude Code, Codex and similar). HTML output is checked in a headless browser when one is available.

- **Before designing**, settle four things: output type and canvas size; issuing institution and what the document is for (or permission to invent both); dialect (§3); information density (§4a). The brand color is taken from the subject, not asked. Ask only about what the request leaves open, as multiple choice, in one batch of at most four questions. Use the host's structured question tool if there is one. If the user says to go ahead without answering, use the defaults: 1920×1080, field dialect, standard density, an institution invented for the subject, and a brand color taken from the subject.
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
2. **One motif, taken from the emblem.** Choose one geometric primitive that comes from the subject (a triangle, a chamfered square, a ring, a bracket) and build the emblem from it. Every part of the emblem should come from what the institution works on (its process line, its terrain, its product), and one of those parts may become the motif of the whole system. Then reuse its parts everywhere: label-plate ends, frame corners, dividers, bullets, large ghost shapes in the background. One primitive, many sizes, so every sheet reads as the same institution.
3. **Swiss order with the grid made visible.** A strict grid, drawn out with dot markers, small corner squares, registration crosses and rulers. Centered or asymmetric, whichever holds the subject.
4. **A calm ground and one dominant brand color.** The ground is near-white, cold light grey, dark navy-black or off-white paper, depending on the dialect. Push the whole canvas toward grey and lift pure color only at the points that matter. The brand color is laid in large flat areas, never sprinkled timidly, and marks what can be acted on. Photographs, renders and illustrations are desaturated toward grey. Two declared exceptions, both small: status colors (alert red, time-limited orange) as small tags on the item whose state they report, and one counter color per sheet or series for index numerals, emphasis words and hairlines, never as a fill (`references/parameters.md`).
5. **Three layers of depth.**
   - Bottom: blurred light, motion streaks, out-of-focus objects, desaturated photographs or renders.
   - Middle: a fine dot-matrix screen over the whole canvas.
   - Top: razor-sharp hairline vectors and UI panels.

   The contrast in sharpness between layers is the main source of the finished, expensive look.
6. **One organic or playful intruder.** Something foreign enters the calm system: liquid, a biological form, terrain, handwriting, a small character, breakage. It must come from the subject itself. The system is built of straight lines; the intruder usually enters as the curve.
7. **Small type, no large type.** Wide or condensed sans, widely tracked, used for labels and rhythm. Visual weight goes to the graphics, never the words. The largest text on a sheet is its title or index number, at most about three times the label size (24–32px on a 1080px short side). No display titles, anchor words, progressive sentences or ghost type: large type rarely looks expensive, and the graphics already carry the weight.
8. **Matte surfaces, even flat light.** No gloss, no dramatic lighting. Two exceptions: wireframes on a screen may glow (in the world of the image they are light on a display), and panels may be frosted and translucent. Glow belongs to lines, never to surfaces.
9. **Restraint above everything. Concise and light overall.** Delete every element that is not needed. Leave large empty fields and concentrate detail in a few dense areas so that sparse and dense play against each other. The one heavy element is the brand color, and it should live inside the hero graphic (the selected path, the arrays, the measured band) rather than as a separate block beside it.

## 3. Dialects

All dialects share one grammar (the nine principles). An institution speaks one dialect; switching institution switches dialect, so the viewer knows the sender has changed without reading a word. The differences are deliberately small: ground, brand color, type weight, texture.

| | Field | Terminal | Paper | Wartime |
|---|---|---|---|---|
| Character | A frontier construction or engineering company: its own terminals, signage and requisition forms | Internal screens of a dispatch, monitoring, medical or military body | Research institute, publication, annual report | An institution at war or in ruins: orders, casualty lists, recovered files |
| Ground | Near-white, with dark panels where needed | Dark navy-black, or ice white | Off-white paper | Light grey, with charcoal panels |
| Brand color (example only) | Signal yellow | Cyan | Olive yellow or ochre | Crimson |
| Type | Condensed or wide sans, all caps, with mono | Mono and wide sans, all caps, all small | Heavy grotesque at small sizes, weight contrast instead of size contrast | Condensed labels, heavier weight; small throughout |
| Graphics | Chamfered panels, hazard stripes, thick accent bars, corner brackets, facility layouts, flow diagrams | Blueprints, wireframes, HUD leader lines | Diagrams, cropped photographs, geometric color blocks | Grey imagery split by brand-color cuts, the motif at large scale, routed node maps |
| Texture | Dot matrix, contour-line fills, light grain, frosted panels | Pixel noise, scan lines, self-lit wireframes | Soft-focus photography, paper, step-and-repeat | Distressed print, ink, cracks |

Rules:

- One image uses one dialect. A series may switch dialect between images when the institution switches.
- The brand color is chosen from the theme every time: the institution's own corporate color, the subject's material, or its emotional key. The colors in the table are examples, not fixed values; a dialect is defined by its ground, type, graphics and texture, not by its hue.
- A sheet or series may declare one counter color, chosen far from the brand hue (a deep blue against yellow, for example). It colors numerals, emphasis words and hairlines only. Status colors stay status colors: they never decorate.
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
- Color used for category (element, class, faction) where it should mark state; a status color used as decoration.

## 4a. Information density

Density is a choice the user makes, not a quality to maximise. Whitespace is what makes a sheet look expensive; when in doubt, take the sparser level. Budgets are for a 1920×1080 sheet; on portrait and square feed formats go one level sparser, because labels are larger.

| | Airy | Standard (default) | Dense |
|---|---|---|---|
| Hero | One view of the data | One view, plus at most one linked aid (a projection on an axis, a short table, a row of 3–6 key figures) | Up to three linked views and one detail cluster |
| Annotations on the hero | Up to 6 | Up to 12 | As the data needs |
| Text column | Header, document-type bar, one sentence, up to 4 fields | Adds mode tags and up to 8 fields, or one short list | Adds tables and legends |
| Empty area | At least half the canvas | About a third, in one or two connected fields | At least one empty field of a quarter of the canvas |

Count before you finish: every label, field and annotation beyond the budget is deleted, not shrunk. Ticks and scale numerals count once per axis.

## 5. Workflow

1. **Research the subject.** Collect real information: data, coordinates, years, formulas, processes, terminology. Graphics driven by data are more convincing than invented ornament.
2. **One-line concept.** State the core of the image in one sentence, such as "analog turning into digital" or "a field growing inside a grid". Content comes first: the real data, the real process, the one striking figure. Then choose which document of the institution would carry it: a measurement protocol, a yearbook insert, a path specification, an event sheet, a decommission record.
3. **Institution, dialect, motif.** Name the issuing institution, fix its dialect (§3), and choose the motif (principle 2). Pick one cartographic genre (`references/techniques.md` §1).
4. **Hero and intruder.** The canvas has exactly one hero graphic, and it belongs to this subject alone. How much it shows, and how much text surrounds it, follows the chosen density (§4a); empty space is part of the design, not leftover. Then decide what the intruder is.
5. **Apply the system.** Grid, palette, type and labels follow `references/parameters.md`; Chinese text follows `references/cjk-typography.md`; the output type follows `references/outputs.md`; image-generation prompts come from `references/image-prompts.md`.
6. **Build.** For HTML, start from the matching file in `assets/templates/`; all templates share `assets/kit.css` and `assets/kit.js`.
7. **Bundle.** Run `scripts/bundle.py page.html -o output/page.html`. It inlines the stylesheet, scripts and images and embeds the fonts subsetted to the characters used, so the file renders the same on any machine. Text that only appears at runtime goes in with `--text`.
8. **Check.** Run `scripts/render_check.py output/page.html --medium <medium>` on the bundled file, the one you deliver. It writes the PNG and reports fallback fonts, text outside the artboard, overlapping text, text below the medium's minimum and extra saturated hues. Fix the source, bundle again, check again. Then look at the PNG yourself and go through §6 and the originality test in §0.
9. **Deliver.** Send the PNG and the bundled HTML.

For several images on one subject, each hero graphic and composition must be clearly different; only the system is shared (palette, type, label language, motif, emblem).

## 6. Self-check

- [ ] The issuing institution and the document's purpose can be named.
- [ ] The dialect can be named, and the image does not mix two.
- [ ] The motif comes from the subject and recurs at several scales.
- [ ] The hero graphic belongs to this subject alone and has no part-by-part correspondence with any reference.
- [ ] One saturated brand color dominates, used boldly. Imagery is desaturated. Status colors appear only as small tags; a counter color, if declared, only on numerals, emphasis words and hairlines; anything else only as a tiny dot or a color control strip.
- [ ] The brand color marks a state, a selection, or a whole color field, never scattered accents.
- [ ] All three layers of depth are present.
- [ ] There is one intruder, and it comes from the subject.
- [ ] No large type: the title or index number is the largest text, about three times the label size at most.
- [ ] Every frame and mask shape can be traced to the subject or the motif.
- [ ] Every industrial detail has a nameable function, hazard stripes included.
- [ ] There is enough empty space, and detail is concentrated in a few areas.
- [ ] The brand color lives inside the hero. The sheet stays within its density budget (§4a), and the empty field is really empty.
- [ ] Surfaces matte, light flat; glow only on screen wireframes.
- [ ] Text is no smaller than the minimum for the output medium (`references/parameters.md`).
- [ ] Facts and data are verified, and their sources are cited in the document's fine print.

## Files

| File | Read when |
|---|---|
| `references/techniques.md` | Choosing a cartographic genre, the motif system, frames, labels, type scale, form operations |
| `references/parameters.md` | Building anything: palettes, Latin type, minimum sizes per medium, layout, texture recipes |
| `references/cjk-typography.md` | Any Chinese (or Japanese) text on the canvas |
| `references/outputs.md` | Per output type: information sheet and series, key visual, emblem, archive card, slides, photo treatment |
| `references/image-prompts.md` | Writing a prompt for an image-generation model |
| `assets/kit.css` | Tokens for the four dialects and the shared components |
| `assets/templates/*.html` | Starting any HTML output |
| `scripts/bundle.py` | After building HTML, before checking it |
| `scripts/render_check.py` | On every bundled HTML file before delivery |
