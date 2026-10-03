// Arknights Industrial kit: drawing helpers shared by the templates.
// scripts/bundle.py inlines this file for delivery.

const KIT_NS = "http://www.w3.org/2000/svg";

function kitEl(tag, attrs, parent) {
  const n = document.createElementNS(KIT_NS, tag);
  for (const k in attrs) n.setAttribute(k, attrs[k]);
  if (parent) parent.append(n);
  return n;
}

// Rulers along the top and left margins, ticks every `step`, majors every `major`.
function kitRulers(svg, { x0 = 96, x1 = 1824, y0 = 96, y1 = 984, at = 64, step = 24, major = 192 } = {}) {
  const g = kitEl("g", { "data-kit": "rulers" }, svg);
  kitEl("path", { d: `M${x0} ${at}H${x1}M${at} ${y0}V${y1}` }, g);
  for (let x = x0; x <= x1; x += step)
    kitEl("path", { d: `M${x} ${at}V${at - ((x - x0) % major ? 6 : 12)}` }, g);
  for (let y = y0; y <= y1; y += step)
    kitEl("path", { d: `M${at} ${y}H${at - ((y - y0) % major ? 6 : 12)}` }, g);
  return g;
}

// Grid dots at every `gap` px inside the margins.
function kitGrid(svg, { x0 = 96, x1 = 1824, y0 = 96, y1 = 984, gap = 192, r = 1.6 } = {}) {
  const g = kitEl("g", { "data-kit": "grid", stroke: "none", fill: "var(--grey-2)" }, svg);
  for (let x = x0; x <= x1; x += gap)
    for (let y = y0; y <= y1; y += gap) kitEl("circle", { cx: x, cy: y, r }, g);
  return g;
}

// Crop marks at the four margin corners.
function kitCropMarks(svg, { x0 = 96, x1 = 1824, y0 = 96, y1 = 984, len = 32, gap = 24 } = {}) {
  const d = [
    `M${x0} ${y0 - gap}V${y0 - gap - len}M${x0 - gap} ${y0}H${x0 - gap - len}`,
    `M${x1} ${y0 - gap}V${y0 - gap - len}M${x1 + gap} ${y0}H${x1 + gap + len}`,
    `M${x0} ${y1 + gap}V${y1 + gap + len}M${x0 - gap} ${y1}H${x0 - gap - len}`,
    `M${x1} ${y1 + gap}V${y1 + gap + len}M${x1 + gap} ${y1}H${x1 + gap + len}`,
  ].join("");
  return kitEl("path", { d, "data-kit": "crop", stroke: "var(--grey-1)" }, svg);
}

// A deterministic barcode generated from a real string (the document's index).
function kitBarcode(svg, text, { x = 0, y = 0, h = 28, unit = 1.5 } = {}) {
  const g = kitEl("g", { "data-kit": "barcode", fill: "currentColor", stroke: "none" }, svg);
  let cx = x;
  const bits = [...text].flatMap((ch) => {
    const c = ch.charCodeAt(0);
    return [1, (c >> 0) & 1, (c >> 1) & 1, 0, (c >> 2) & 1, (c >> 3) & 1, 1, (c >> 4) & 1, 0];
  });
  for (const b of [1, 0, 1, ...bits, 1, 0, 1]) {
    if (b) kitEl("rect", { x: cx, y, width: unit, height: h }, g);
    cx += unit * (b ? 1 : 1.5);
  }
  return g;
}

// Scale the artboard to fit the viewport.
function kitFit(board = document.querySelector(".artboard")) {
  const w = board.offsetWidth, h = board.offsetHeight;
  const fit = () => { board.style.transform = `scale(${Math.min(innerWidth / w, innerHeight / h)})`; };
  addEventListener("resize", fit);
  fit();
}
