# Techniques

Each technique is a transferable operation. None of them corresponds to a specific image in any reference.

## 1. Borrow a real cartographic genre

When the image introduces a place, a piece of equipment or an organization, first choose an existing cartographic or technical genre and let its rules order the canvas: architectural plans and blueprints, isometric wireframes, shaded relief maps, transit diagrams, cross-sections, equipment nameplates, inspection reports. The constraints a genre brings with it (45° routing, station dots, contour lines, dimension lines, scale bars) are more convincing than invented ornament.

The genre must suit the subject: a city takes a transit diagram, terrain takes shaded relief, equipment takes a blueprint.

## 2. Two representational states at once

Show one object in two states at the same time, switching along an axis or across a region: plan and wireframe, wireframe and solid, silhouette and section, clean vector and pixel breakup. The viewer reads that the object is being scanned, modeled or transmitted, and the image gains a sense of time.

Use pixel breakup only when the subject concerns data, transmission or archiving. In that case it may double as the intruder.

## 3. Frames taken from the subject

Masks, viewing apertures and outer frames must have a shape whose origin can be stated from the subject's physical form: a ring building gets a ring aperture, a tunnel an arch, a cabin the proportions of a porthole, a land parcel its own boundary. Arbitrary circles and rectangles do not count.

The image inside an aperture may be out of focus or color-shifted; the frame itself stays sharp.

## 4. Where labels live

Labels can be placed in two ways. One image uses mainly one of them.

- **Screen plane.** A thin leader line leaves a hollow dot on the object, bends once, and lands on a short underlined text. The label faces the viewer like an annotation laid over a monitoring feed.
- **Object plane.** The text is set in perspective on the floor, a wall or a device surface, sharing the object's space.

Important information sits on a reversed bar: a solid bar in the reverse of the ground (black with white text on a light ground, light with dark text on a dark one; `.bar` in `kit.css`), flush left. Captions use the same bar, so captions too become document elements inside the world.

## 5. The brand color marks state

The brand color lands on what the sheet is about: the selected path, the measured peak, the solar arrays, the reflected wave. It may sit away from the center of the composition; the eye goes to the color first.

The strongest use of the brand color is to mark the current state. In a row of category tags, every tag is grey except the selected one, which takes the brand color. In a group of nodes, only the one being monitored is colored. Add a timestamp ("updated 2 min ago") and data status fields, and the document turns from an archive into a live reading.

## 6. Type scale

All type is small. The title (or the document's index number) is the largest text, about three times the label size; weight and tracking, not size, separate the levels.

- **Sentence split by the image.** The hero image can break the one-line sentence in two, first half on the left and second half on the right, so the reading path must pass through the image and the image becomes a pause in the sentence.
- **Subject echo.** The hero image, not a word, can be enlarged several times and dropped to very low contrast behind itself, as texture.

## 7. Form operations

- **Slicing.** Cut a circle, sphere or solid into evenly spaced horizontal bands, like scan layers or tomographic sections.
- **Step-and-repeat.** Copy one shape a dozen or more times at a fixed step in one direction, offsetting each copy, so the edge becomes a sawtooth or staircase. Use it for sequences, batches or transitions.
- **Construction lines overrun.** Thin lines extended from the object's geometry cross its outline into empty space and stop at the canvas edge or at another element, so the object seems still to be in the middle of being drawn.
- **Arc scales.** Ticks and numbers can run along an arc whose center sits on the subject, marking the reference point of a measurement.

## 8. Color control strip

Status colors and a declared counter color have their own limits (`parameters.md`, Palettes). Beyond those, a further saturated color may appear only as a print color control strip: a thin segmented bar at the page edge or under a label, one color per segment. In the printing industry it is a calibration tool, so it has a function. Its area must stay small enough that the image still reads as having one brand color.

## 9. The motif system

Principle 2 in practice:

1. **Find the primitive.** Ask what single shape the subject is built from: a pyramid or tower gives a triangle, a pipeline gives a ring or elbow, a container yard gives a chamfered rectangle, a signal gives a bracket. If nothing in the subject yields a shape, use a 45° chamfer, the most neutral industrial primitive.
2. **Build the emblem from it.** Two or three instances of the primitive on a modular grid, with one stencil break or cut.
3. **Break the emblem into parts and give each part a job.**

| Part of the motif | Job |
|---|---|
| The whole shape, very large and one step off the ground | Background ghost shape behind the hero (omit it behind a dense data graphic, where it reads as a glitch) |
| The shape outlined, medium | Frame or aperture for the hero or a portrait slot |
| A corner or tip of the shape | Label plate end, tag end, panel corner |
| The shape filled, small | Bullet, state marker, list index |
| The shape repeated in a row | Progress, rank, divider, loading |

4. **Keep the count.** One primitive per institution. A second primitive only appears when a second institution enters.

## 10. Industrial markings

Each marking has a real-world meaning. Use it only where that meaning applies.

- **Hazard stripes.** 45° stripes, brand color and ink (or ink and ground) in equal widths. Meaning: caution, restricted, under construction, locked, in progress. Put them on a locked item, a warning bar, a loading bar, the edge of a restricted zone, never as a background fill.
- **Chamfered corners.** Cut corners at 45°. Choose one chamfer size per document (for example 8px on panels and 4px on tags) and cut the same corner on every panel, usually the top-right or bottom-right. A chamfer on all four corners reads as a sticker, not equipment.
- **Accent bar.** A thick bar, 4–6px, on the left edge of a panel or list row. Ink marks a section; the brand color marks the current item.
- **Corner brackets.** Four L-shaped marks around an area instead of a full frame. Meaning: a target, a scan region, a selection.
- **Barcodes and data matrices.** Generate them from a real string (the document's index number), not as random stripes.
- **Registration crosses.** At grid intersections and frame corners, small and in grey.

## 11. Distress and breakage (wartime dialect)

Damage is information here: it says the document survived something.

- Distress a stamp or the hero's edge, never the labels; they must stay readable.
- Crack lines or shattered glass radiate from one point that can be named (an impact, a blast), and act as the intruder.
- Ink splatter, if used, is one deliberate mark in the brand color or ink, not a scattered texture.
- Imagery is fully grey. The brand color appears only as flat cuts and state marks.

## 12. The sheet as an instrument readout

Ask what instrument or software produced the data, and borrow the look of its output.

- **Pick the medium.** A spectrum becomes a spectrometer's contour plot with projections on the axes; a seismic event a seismogram trace with marked phases; a protocol a bit-field diagram; a survey a total-station printout. The brand color and motif keep it inside the institution.
- **A workbench, not a stage.** Objects and people under inspection stand on a measuring surface: a dark or light viewport floor with a grid, axes and a few geometric planes, like a modeling program's empty scene. It says the object is being configured, not admired.
- **Recording state.** A screen about the past shows that it is being recorded or analysed: grain, the image cut into vertical strips like frames, a frame counter, a REC mark, a waveform, level meters, channel-split color fringes on a grey image.
- **Process left visible.** Icons and emblems keep their construction lines: the square and circles they were drawn on, dashed guides, module boxes. The viewer sees the system at work and takes part in it.
- **Capabilities as structure.** Show the parts of a system as modules installed in a frame, linked by their relations, rather than a ladder of levels.

## 13. Type over images and busy grounds

- **Build the plate upward.** Under a label set on an image, lay a base in the panel or brand color, then one thin transition layer above it with a fine texture, so the plate has depth without a drop shadow.
- **Darken locally, never drop-shadow.** Where text crosses an image, darken the image a little behind the text. The text itself stays plain so it reads; the richness goes into the ground around it.
- **Outline flat icons on busy grounds.** A solid-color icon or plate over imagery or effects gets a 1–2px outline in the reverse value.
- **Ornament in the margins.** Add detail in the empty areas around the subject, never across it: the center keeps its brightness and sharpness.
- **Opaque enough.** Panels behind text are dense enough that the image behind does not show through the letters.

## 14. Traditional forms in an industrial world

For regional variants (SKILL.md §3) and any subject with a historical style:

- Keep the silhouette of the traditional form (roof line, gate, water wheel), so it is recognized at once.
- Strip the curves and layered ornament; industrial form is straight lines and few curves.
- Replace details with industrial parts: roof tiles become flat panels, carved timber becomes tread plate, a wooden wheel gains a steel frame.
- Render the structure's own construction lines as a graphic: the wireframe of the form, printed as a drawing.
- Curves that remain belong to the intruder: water, plants, terrain.

