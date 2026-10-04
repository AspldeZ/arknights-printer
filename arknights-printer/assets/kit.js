// Arknights Printer kit: drawing helpers shared by the templates.
// scripts/bundle.py inlines this file for delivery.

const KIT_NS = "http://www.w3.org/2000/svg";

function kitEl(tag, attrs, parent) {
  const n = document.createElementNS(KIT_NS, tag);
  for (const k in attrs) n.setAttribute(k, attrs[k]);
  if (parent) parent.append(n);
  return n;
}

// Board geometry: size, 5% margin and grid gap derived from the artboard, so the
// helpers work on any canvas (landscape, portrait, square).
function kitBoard(node = document.querySelector(".artboard")) {
  const board = node.closest ? node.closest(".artboard") || node : node;
  const W = board.offsetWidth, H = board.offsetHeight;
  const M = Math.round(W * 0.05);
  return { W, H, M, x0: M, x1: W - M, y0: M, y1: H - M, gap: Math.round(Math.max(W, H) / 10) };
}

// Rulers along the top and left margins, ticks every `step`, majors every `major`.
function kitRulers(svg, o = {}) {
  const b = kitBoard(svg);
  const { x0 = b.x0, x1 = b.x1, y0 = b.y0, y1 = b.y1, at = Math.round(b.M * 2 / 3), step = 24, major = 192 } = o;
  const g = kitEl("g", { "data-kit": "rulers" }, svg);
  kitEl("path", { d: `M${x0} ${at}H${x1}M${at} ${y0}V${y1}` }, g);
  for (let x = x0; x <= x1; x += step)
    kitEl("path", { d: `M${x} ${at}V${at - ((x - x0) % major ? 6 : 12)}` }, g);
  for (let y = y0; y <= y1; y += step)
    kitEl("path", { d: `M${at} ${y}H${at - ((y - y0) % major ? 6 : 12)}` }, g);
  return g;
}

// Grid dots at every `gap` px inside the margins.
function kitGrid(svg, o = {}) {
  const b = kitBoard(svg);
  const { x0 = b.x0, x1 = b.x1, y0 = b.y0, y1 = b.y1, gap = b.gap, r = 1.6 } = o;
  const g = kitEl("g", { "data-kit": "grid", stroke: "none", fill: "var(--grey-2)" }, svg);
  for (let x = x0; x <= x1; x += gap)
    for (let y = y0; y <= y1; y += gap) kitEl("circle", { cx: x, cy: y, r }, g);
  return g;
}

// Crop marks and corner squares at the four margin corners.
function kitCropMarks(svg, o = {}) {
  const b = kitBoard(svg);
  const { x0 = b.x0, x1 = b.x1, y0 = b.y0, y1 = b.y1, len = Math.round(b.M / 3), gap = Math.round(b.M / 4) } = o;
  const d = [
    `M${x0} ${y0 - gap}V${y0 - gap - len}M${x0 - gap} ${y0}H${x0 - gap - len}`,
    `M${x1} ${y0 - gap}V${y0 - gap - len}M${x1 + gap} ${y0}H${x1 + gap + len}`,
    `M${x0} ${y1 + gap}V${y1 + gap + len}M${x0 - gap} ${y1}H${x0 - gap - len}`,
    `M${x1} ${y1 + gap}V${y1 + gap + len}M${x1 + gap} ${y1}H${x1 + gap + len}`,
  ].join("");
  const g = kitEl("g", { "data-kit": "crop" }, svg);
  kitEl("path", { d, stroke: "var(--grey-1)" }, g);
  for (const [x, y] of [[x0, y0], [x1, y0], [x0, y1], [x1, y1]])
    kitEl("rect", { x: x - 3, y: y - 3, width: 6, height: 6, fill: "var(--ink)", stroke: "none" }, g);
  return g;
}

// Make a full-board SVG's coordinates match the board's pixels.
function kitLayer(svg) {
  const b = kitBoard(svg);
  svg.setAttribute("viewBox", `0 0 ${b.W} ${b.H}`);
  return b;
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

// Hero slot: size an SVG to its slot so 1 unit = 1 board pixel; returns { w, h }.
function kitHero(svg) {
  const r = svg.parentElement.getBoundingClientRect();
  const k = svg.closest(".artboard").getBoundingClientRect().width / svg.closest(".artboard").offsetWidth;
  const w = Math.round(r.width / k), h = Math.round(r.height / k);
  svg.setAttribute("viewBox", `0 0 ${w} ${h}`);
  return { w, h };
}

// Mark the board's orientation so the sheet frame can restack (portrait, square, landscape).
function kitOrient(board = document.querySelector(".artboard")) {
  const { W, H } = kitBoard(board);
  board.dataset.orient = W < H * 0.95 ? "portrait" : W > H * 1.05 ? "landscape" : "square";
}

// Scale the artboard to fit the viewport.
function kitFit(board = document.querySelector(".artboard")) {
  const w = board.offsetWidth, h = board.offsetHeight;
  const fit = () => { board.style.transform = `scale(${Math.min(innerWidth / w, innerHeight / h)})`; };
  addEventListener("resize", fit);
  fit();
}
