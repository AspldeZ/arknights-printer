#!/usr/bin/env python3
"""Render an artboard and check it mechanically.

    python3 render_check.py page.bundled.html                 # screen medium
    python3 render_check.py page.bundled.html --medium feed -o page.png
    python3 render_check.py page.bundled.html --medium print --print-mm 297
    python3 render_check.py page.bundled.html --scale 2       # 4K from a 1920×1080 board

Run it on the bundled file (bundle.py first): that is the file you deliver, and
its fonts load without network access.

Checks:
  font      text rendered in a system fallback font (a web font failed to load or
            lacks the glyph)
  outside   text ink outside the artboard
  overlap   ink of two text boxes overlapping
  size      text smaller than the medium's minimum (references/parameters.md);
            CJK text needs 2px more (references/cjk-typography.md)
  hue       saturated hues by role: the brand hue is free; a declared --counter
            hue stays under 3% of the area, --alert and --timed together under 1%;
            any other saturated hue above --hue-area is reported

Elements inside data-role="ghost" or data-role="texture" are skipped by the
outside, overlap, size and hue checks. The script catches mechanical faults, not
taste: look at the screenshot as well.

Needs Playwright (pip install playwright; playwright install chromium). Uses
--chromium PATH, $CHROMIUM, /opt/pw-browsers/chromium, Playwright's own Chromium
or the installed Chrome, in that order. Exit status is 1 when anything is found.
"""

import argparse
import base64
import json
import math
import os
import sys
from pathlib import Path

MIN_PX = {"screen": 9, "feed": 14, "slides": 16}   # at a 1080px short side
COUNTER_MAX, STATUS_MAX = 0.03, 0.01                 # share of area (parameters.md, Palettes)
HUE_MATCH = 25                                       # degrees between a cluster and a role's hue
PRINT_MIN_PT = 6
CJK_EXTRA_PX = 2                                   # cjk-typography.md: Chinese needs 2px more
EXEMPT = '[data-role="ghost"], [data-role="texture"]'

TEXT_JS = r"""
({ exempt }) => {
  const board = document.querySelector(".artboard") || document.body;
  const B = board.getBoundingClientRect();
  const ctx = document.createElement("canvas").getContext("2d");
  const items = [];
  let n = 0;

  const shown = (el) => {
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
      const s = getComputedStyle(e);
      if (s.display === "none" || s.visibility === "hidden" || +s.opacity === 0) return false;
    }
    return true;
  };
  const describe = (el) => {
    const cls = el.getAttribute("class");
    return el.tagName.toLowerCase() + (cls ? "." + cls.trim().split(/\s+/).join(".") : "");
  };
  const scaleOf = (el) => {
    if (el instanceof SVGElement && el.getScreenCTM) {
      const m = el.getScreenCTM();
      return m ? Math.sqrt(Math.abs(m.a * m.d - m.b * m.c)) : 1;
    }
    // product of the scale parts of every transform up to the board; translations do not count
    let s = 1;
    for (let t = el; t && t !== board; t = t.parentElement) {
      const tr = getComputedStyle(t).transform;
      if (tr && tr !== "none") { const m = new DOMMatrix(tr); s *= Math.sqrt(Math.abs(m.a * m.d - m.b * m.c)); }
    }
    return s;
  };
  const transform = (t, mode) =>
    mode === "uppercase" ? t.toUpperCase() : mode === "lowercase" ? t.toLowerCase() : t;

  const walker = document.createTreeWalker(board, NodeFilter.SHOW_TEXT);
  for (let node; (node = walker.nextNode()); ) {
    const raw = node.nodeValue;
    if (!raw.trim()) continue;
    const el = node.parentElement;
    if (!el || el.closest("script, style, defs, title, desc") || !shown(el)) continue;
    const range = document.createRange();
    range.selectNodeContents(node);
    const rects = [...range.getClientRects()].filter((r) => r.width > 0.5 && r.height > 0.5);
    if (!rects.length) continue;

    const s = getComputedStyle(el);
    const fontPx = parseFloat(s.fontSize);
    const scale = scaleOf(el);
    const text = transform(raw.trim(), s.textTransform);

    // Ink box: horizontal extent from the line box, vertical extent from the glyphs.
    ctx.font = `${s.fontStyle} ${s.fontWeight} ${fontPx * scale}px ${s.fontFamily}`;
    ctx.letterSpacing = s.letterSpacing === "normal" ? "0px" : s.letterSpacing;
    const m = ctx.measureText(text);
    const vertical = s.writingMode.startsWith("vertical");
    const ink = rects.map((r) => {
      if (vertical || !m.fontBoundingBoxAscent) return { x0: r.left, y0: r.top, x1: r.right, y1: r.bottom };
      // the content-area rect is centred on the font box; find the baseline inside it
      const pad = (r.height - (m.fontBoundingBoxAscent + m.fontBoundingBoxDescent)) / 2;
      const base = r.top + pad + m.fontBoundingBoxAscent;
      return { x0: r.left, x1: r.right,
               y0: base - m.actualBoundingBoxAscent, y1: base + m.actualBoundingBoxDescent };
    });

    if (!el.dataset.rc) el.dataset.rc = String(n++);
    items.push({
      rc: el.dataset.rc, el: describe(el), text: text.slice(0, 40),
      exempt: !!el.closest(exempt), px: +(fontPx * scale).toFixed(2), ink,
      cjk: /[\u3040-\u30ff\u3400-\u9fff\uf900-\ufaff\uac00-\ud7af]/.test(raw),
    });
  }
  return { board: { x: B.left, y: B.top, w: B.width, h: B.height }, items };
}
"""

ROLES_JS = r"""
() => {
  const board = document.querySelector(".artboard");
  const probe = document.createElement("i");
  board.append(probe);
  const out = {};
  for (const k of ["brand", "counter", "alert", "timed"]) {
    const v = getComputedStyle(board).getPropertyValue("--" + k).trim();
    if (!v) { out[k] = null; continue; }
    probe.style.color = "rgb(0 0 0 / 0)";
    probe.style.color = v;
    const m = getComputedStyle(probe).color.match(/[\d.]+/g).map(Number);
    out[k] = m.length >= 3 && (m[3] === undefined || m[3] > 0) ? m.slice(0, 3) : null;
  }
  probe.remove();
  return out;
}
"""

HUE_JS = r"""
async ({ png, minC }) => {
  const img = new Image();
  img.src = "data:image/png;base64," + png;
  await img.decode();
  const c = document.createElement("canvas");
  c.width = img.width; c.height = img.height;
  const g = c.getContext("2d");
  g.drawImage(img, 0, 0);
  const d = g.getImageData(0, 0, c.width, c.height).data;
  const lin = (v) => (v /= 255) <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
  const BINS = 36, bins = Array.from({ length: BINS }, () => ({ n: 0, r: 0, g: 0, b: 0 }));
  let total = 0;
  for (let i = 0; i < d.length; i += 8) {            // every other pixel
    total++;
    const r = lin(d[i]), gg = lin(d[i + 1]), b = lin(d[i + 2]);
    const l = Math.cbrt(0.4122214708 * r + 0.5363325363 * gg + 0.0514459929 * b);
    const m = Math.cbrt(0.2119034982 * r + 0.6806995451 * gg + 0.1073969566 * b);
    const s = Math.cbrt(0.0883024619 * r + 0.2817188376 * gg + 0.6299787005 * b);
    const A = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s;
    const Bb = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s;
    if (Math.hypot(A, Bb) < minC) continue;
    const h = (Math.atan2(Bb, A) * 180 / Math.PI + 360) % 360;
    const bin = bins[Math.floor(h / (360 / BINS)) % BINS];
    bin.n++; bin.r += d[i]; bin.g += d[i + 1]; bin.b += d[i + 2];
  }
  // Merge runs of occupied bins (circular) into hue clusters, ignoring noise.
  const floor = total * 0.0001;
  const on = bins.map((b) => b.n > floor);
  if (on.every(Boolean)) return { total, clusters: [{ share: bins.reduce((a, b) => a + b.n, 0) / total, hue: "all", color: "#888888" }] };
  let start = on.findIndex((v, i) => v && !on[(i - 1 + BINS) % BINS]);
  const clusters = [];
  if (start >= 0) {
    for (let k = 0; k < BINS; k++) {
      const i = (start + k) % BINS;
      if (!on[i]) continue;
      if (!on[(i - 1 + BINS) % BINS] || !clusters.length) clusters.push({ n: 0, r: 0, g: 0, b: 0, h0: i, h1: i });
      const cl = clusters[clusters.length - 1], b = bins[i];
      cl.n += b.n; cl.r += b.r; cl.g += b.g; cl.b += b.b; cl.h1 = i;
    }
  }
  const hex = (v) => Math.round(v).toString(16).padStart(2, "0");
  return {
    total,
    clusters: clusters.map((cl) => ({
      share: cl.n / total,
      hue: `${cl.h0 * 10}-${cl.h1 * 10 + 10}`,
      color: "#" + hex(cl.r / cl.n) + hex(cl.g / cl.n) + hex(cl.b / cl.n),
    })).sort((a, b) => b.share - a.share),
  };
}
"""


def launch(p, path):
    path = path or os.environ.get("CHROMIUM")
    if not path and Path("/opt/pw-browsers/chromium").exists():
        path = "/opt/pw-browsers/chromium"
    if path:
        return p.chromium.launch(executable_path=path)
    try:
        return p.chromium.launch()
    except Exception:
        return p.chromium.launch(channel="chrome")


def overlaps(a, b, tol=1.0):
    return min(a["x1"], b["x1"]) - max(a["x0"], b["x0"]) > tol and \
        min(a["y1"], b["y1"]) - max(a["y0"], b["y0"]) > tol


def fallback_fonts(page, cdp):
    """Text elements whose glyphs Chromium drew with a non-web (system) font."""
    cdp.send("DOM.enable")
    cdp.send("CSS.enable")
    root = cdp.send("DOM.getDocument", {"depth": -1, "pierce": True})["root"]["nodeId"]
    found = []
    for node_id in cdp.send("DOM.querySelectorAll", {"nodeId": root, "selector": "[data-rc]"})["nodeIds"]:
        attrs = cdp.send("DOM.getAttributes", {"nodeId": node_id})["attributes"]
        rc = dict(zip(attrs[::2], attrs[1::2])).get("data-rc")
        fonts = cdp.send("CSS.getPlatformFontsForNode", {"nodeId": node_id})["fonts"]
        system = [f"{f['familyName']} ({f['glyphCount']} glyphs)" for f in fonts if not f.get("isCustomFont")]
        if system:
            found.append((rc, system))
    return found


def check(args):
    from playwright.sync_api import sync_playwright

    issues, notes = [], []
    with sync_playwright() as p:
        browser = launch(p, args.chromium)
        page = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=args.scale)
        page.goto(args.html.resolve().as_uri(), wait_until="load")
        size = page.evaluate("""() => { const b = document.querySelector('.artboard');
            return b ? { width: b.offsetWidth, height: b.offsetHeight } : null; }""")
        if not size:
            sys.exit("error: no .artboard element")
        page.set_viewport_size(size)
        page.evaluate("""async () => { document.querySelector('.artboard').style.transform = 'none';
            await document.fonts.ready; await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); }""")
        if args.wait:
            page.wait_for_timeout(args.wait)

        short = min(size["width"], size["height"])
        if args.medium == "print":
            min_px = PRINT_MIN_PT * short / (args.print_mm / 25.4 * 72)
        else:
            min_px = MIN_PX[args.medium] * short / 1080

        data = page.evaluate(TEXT_JS, {"exempt": EXEMPT})
        by_rc = {it["rc"]: it for it in data["items"]}
        board = data["board"]

        cdp = page.context.new_cdp_session(page)
        for rc, system in fallback_fonts(page, cdp):
            it = by_rc.get(rc)
            if it:
                issues.append(("font", f"{it['el']} “{it['text']}” drawn in {', '.join(system)}"))

        live = [it for it in data["items"] if not it["exempt"]]
        bx1, by1 = board["x"] + board["w"], board["y"] + board["h"]
        for it in live:
            for r in it["ink"]:
                if r["x0"] < board["x"] - .5 or r["y0"] < board["y"] - .5 or r["x1"] > bx1 + .5 or r["y1"] > by1 + .5:
                    issues.append(("outside", f"{it['el']} “{it['text']}” ink at "
                                   f"{r['x0']:.0f},{r['y0']:.0f} → {r['x1']:.0f},{r['y1']:.0f}"))
                    break
            need = min_px + (CJK_EXTRA_PX * short / 1080 if it["cjk"] else 0)
            if it["px"] < need - 0.01:
                issues.append(("size", f"{it['el']} “{it['text']}” is {it['px']:g}px, minimum for "
                               f"{args.medium} is {need:.1f}px{' (CJK +2px)' if it['cjk'] else ''}"))
        for i, a in enumerate(live):
            for b in live[i + 1:]:
                if a["rc"] == b["rc"]:
                    continue
                if any(overlaps(ra, rb) for ra in a["ink"] for rb in b["ink"]):
                    issues.append(("overlap", f"{a['el']} “{a['text']}” × {b['el']} “{b['text']}”"))

        art = page.locator(".artboard")
        out = args.out or args.html.with_suffix(".png")
        art.screenshot(path=str(out))

        roles = page.evaluate(ROLES_JS)
        page.add_style_tag(content=f"{EXEMPT} {{ visibility: hidden !important; }}")
        png = base64.b64encode(art.screenshot()).decode()
        hues = page.evaluate(HUE_JS, {"png": png, "minC": args.min_chroma})
        browser.close()

    issues += hue_issues(hues["clusters"], roles, args, notes)
    return out, min_px, issues, notes


def oklch(rgb):
    """(chroma, hue in degrees) of an sRGB triple 0–255."""
    lin = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in (c / 255 for c in rgb)]
    r, g, b = lin
    l_ = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m_ = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s_ = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    a = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    bb = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
    return math.hypot(a, bb), math.degrees(math.atan2(bb, a)) % 360


def hue_issues(clusters, roles, args, notes):
    """Assign each saturated hue cluster to a declared role and apply that role's limit."""
    declared = {k: oklch(v)[1] for k, v in roles.items() if v and oklch(v)[0] >= args.min_chroma}
    notes.append("roles  " + ", ".join(f"{k} {h:.0f}°" for k, h in declared.items()))
    share = {"brand": 0.0, "counter": 0.0, "status": 0.0}
    issues = []
    for c in clusters:
        hue = oklch(tuple(int(c["color"][i:i + 2], 16) for i in (1, 3, 5)))[1]
        dist = {k: min(abs(hue - h), 360 - abs(hue - h)) for k, h in declared.items()}
        role = next((k for k in ("brand", "counter", "alert", "timed") if dist.get(k, 999) <= HUE_MATCH), None)
        role = "status" if role in ("alert", "timed") else role
        notes.append(f"hue {c['hue']}°  {c['color']}  {c['share'] * 100:.2f}% of area  → {role or 'unassigned'}")
        if role:
            share[role] += c["share"]
        elif c["share"] >= args.hue_area / 100:
            issues.append(("hue", f"{c['color']} covers {c['share'] * 100:.2f}% and matches no declared "
                                  f"role (brand, counter, alert, timed)"))
    if share["counter"] > COUNTER_MAX:
        issues.append(("hue", f"counter color covers {share['counter'] * 100:.1f}% of the area "
                              f"(limit {COUNTER_MAX * 100:.0f}%): numerals, emphasis words, hairlines only"))
    if share["status"] > STATUS_MAX:
        issues.append(("hue", f"status colors cover {share['status'] * 100:.1f}% of the area "
                              f"(limit {STATUS_MAX * 100:.0f}%): small tags only"))
    return issues


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html", type=Path)
    ap.add_argument("-o", "--out", type=Path, help="screenshot path (default: <name>.png)")
    ap.add_argument("--medium", choices=["screen", "feed", "slides", "print"], default="screen")
    ap.add_argument("--print-mm", type=float, help="short side of the final print in mm (medium print)")
    ap.add_argument("--hue-area", type=float, default=0.1,
                    help="%% of area above which a saturated hue counts (default 0.1)")
    ap.add_argument("--min-chroma", type=float, default=0.08, help="OKLCH chroma that counts as saturated")
    ap.add_argument("--wait", type=int, default=0, help="extra ms to wait before measuring")
    ap.add_argument("--scale", type=float, default=1,
                    help="pixel ratio of the PNG (2 renders a 1920×1080 board as 3840×2160)")
    ap.add_argument("--chromium", help="path to a Chromium executable")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    args = ap.parse_args()
    if args.medium == "print" and not args.print_mm:
        ap.error("--medium print needs --print-mm (short side of the final print)")

    out, min_px, issues, notes = check(args)
    if args.json:
        print(json.dumps({"screenshot": str(out), "min_px": min_px,
                          "issues": [{"check": k, "detail": d} for k, d in issues], "notes": notes},
                         ensure_ascii=False, indent=2))
    else:
        print(f"render {args.html} → {out}  (medium {args.medium}, min {min_px:.1f}px)")
        for n in notes:
            print(f"  note     {n}")
        for k, d in issues:
            print(f"  {k:<8} {d}")
        if any(k == "font" for k, _ in issues):
            print("  hint     run bundle.py and check the bundled file")
        print(f"  {'ok' if not issues else str(len(issues)) + ' issue(s)'}")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
