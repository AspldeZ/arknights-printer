#!/usr/bin/env python3
"""Bundle an HTML document into one self-contained file.

Inlines local stylesheets, scripts and images, and replaces Google Fonts links
with @font-face rules whose woff2 files are subsetted to the characters the
document uses (css2 `text=` parameter) and embedded as base64.

    python3 bundle.py page.html                  # writes page.bundled.html
    python3 bundle.py page.html -o out/page.html
    python3 bundle.py page.html --text "额外字符"   # characters added at runtime
    python3 bundle.py page.html --font-file "Archivo=fonts/Archivo.ttf"  # offline

The character set is every non-ASCII character in the document and its local
CSS/JS (comments excluded), their case variants, and all printable ASCII
(labels use CSS text-transform: uppercase, so the source case says nothing).
Text that only exists at runtime (fetched data) must be passed with --text.

Standard library only. --font-file subsets with fontTools when it is installed
and embeds the whole file otherwise.
"""

import argparse
import base64
import html
import mimetypes
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")  # modern UA → woff2
GOOGLE_CSS = re.compile(r"https?://fonts\.googleapis\.com/css2?\?[^\"')\s]+")
ASCII = "".join(chr(c) for c in range(0x20, 0x7F))
TEXT_CHUNK = 600  # characters per text= request, keeps URLs well under 8 KB

TAG = re.compile(r"<(link|script|img|image)\b([^>]*?)/?>(?:\s*</script>)?", re.I | re.S)
ATTR = re.compile(r"""([\w:-]+)\s*=\s*("([^"]*)"|'([^']*)'|([^\s>]+))""", re.S)
CSS_URL = re.compile(r"""url\(\s*(['"]?)([^'")]+)\1\s*\)""")
CSS_IMPORT = re.compile(r"""@import\s+(?:url\()?\s*['"]?([^'")\s;]+)['"]?\s*\)?\s*;""")


def fetch(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    return data if binary else data.decode("utf-8")


def attrs_of(s):
    return {m.group(1).lower(): html.unescape(m.group(3) or m.group(4) or m.group(5) or "")
            for m in ATTR.finditer(s)}


def is_remote(ref):
    return re.match(r"^(?:[a-z]+:)?//|^data:|^#", ref, re.I) is not None


def data_uri(path):
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


# ---------- character set ----------

def charset(sources, extra=""):
    text = "".join(sources) + extra
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = html.unescape(text)
    chars = {c for c in text if ord(c) > 0x7E}   # includes U+3000 and other non-ASCII spaces
    for c in list(chars):
        for v in (c.upper(), c.lower()):
            if len(v) == 1:
                chars.add(v)
    return ASCII + "".join(sorted(chars))


# ---------- Google Fonts ----------

def parse_faces(css):
    faces = []
    for block in re.findall(r"@font-face\s*{([^}]*)}", css):
        props = {}
        for decl in block.split(";"):
            if ":" in decl:
                k, v = decl.split(":", 1)
                props[k.strip().lower()] = v.strip()
        faces.append(props)
    return faces


def weight_range(ws):
    nums = [int(n) for w in ws for n in w.split()]
    lo, hi = min(nums), max(nums)
    return str(lo) if lo == hi else f"{lo} {hi}"


def google_faces(url, chars, log):
    """Fetch a css2 URL subsetted to `chars`; return @font-face CSS with embedded woff2."""
    parts = urllib.parse.urlsplit(url)
    query = [(k, v) for k, v in urllib.parse.parse_qsl(parts.query, keep_blank_values=True) if k != "text"]
    faces = []
    for i in range(0, len(chars), TEXT_CHUNK):
        q = urllib.parse.urlencode(query + [("text", chars[i:i + TEXT_CHUNK])])
        faces += parse_faces(fetch(urllib.parse.urlunsplit(parts._replace(query=q))))

    # Weights of a variable family come back as separate rules pointing at one file:
    # merge them into one rule with a weight range so each file is embedded once.
    groups = {}
    for f in faces:
        key = (f.get("font-family"), f.get("font-style", "normal"), f.get("font-stretch"),
               f.get("src"), f.get("unicode-range"))
        groups.setdefault(key, {**f, "_weights": []})["_weights"].append(f.get("font-weight", "400"))

    cache, out = {}, []
    for g in groups.values():
        def embed(m):
            src = m.group(2)
            if src not in cache:
                cache[src] = base64.b64encode(fetch(src, binary=True)).decode()
                log(f"  font  {g['font-family']} {weight_range(g['_weights'])}  "
                    f"{len(cache[src]) * 3 // 4 / 1024:.0f} KB")
            return f"url(data:font/woff2;base64,{cache[src]})"
        src = CSS_URL.sub(embed, g["src"])
        decls = [f"font-family: {g['font-family']}", f"font-style: {g.get('font-style', 'normal')}",
                 f"font-weight: {weight_range(g['_weights'])}"]
        if g.get("font-stretch"):
            decls.append(f"font-stretch: {g['font-stretch']}")
        if g.get("font-display"):
            decls.append(f"font-display: {g['font-display']}")
        decls.append(f"src: {src}")
        if g.get("unicode-range"):
            decls.append(f"unicode-range: {g['unicode-range']}")
        out.append("@font-face { " + "; ".join(decls) + "; }")
    return "\n".join(out)


def google_families(url):
    q = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)
    return [f.split(":")[0].replace("+", " ") for f in q.get("family", [])]


def without_families(url, drop):
    parts = urllib.parse.urlsplit(url)
    q = [(k, v) for k, v in urllib.parse.parse_qsl(parts.query, keep_blank_values=True)
         if not (k == "family" and v.split(":")[0].replace("+", " ") in drop)]
    if not any(k == "family" for k, _ in q):
        return None
    return urllib.parse.urlunsplit(parts._replace(query=urllib.parse.urlencode(q)))


# ---------- local font files (offline) ----------

def local_face(family, path, chars, log):
    data = path.read_bytes()
    fmt = "woff2" if path.suffix.lower() == ".woff2" else "woff" if path.suffix.lower() == ".woff" else "truetype"
    try:
        from fontTools import subset
        from fontTools.ttLib import TTFont
        import io
        font = TTFont(io.BytesIO(data))
        opts = subset.Options()
        opts.flavor = "woff2" if _has_brotli() else None
        opts.layout_features = ["*"]
        sub = subset.Subsetter(opts)
        sub.populate(text=chars)
        sub.subset(font)
        buf = io.BytesIO()
        font.save(buf)
        data, fmt = buf.getvalue(), "woff2" if opts.flavor else "truetype"
        axes = {a.axisTag: (a.minValue, a.maxValue) for a in font["fvar"].axes} if "fvar" in font else {}
    except ImportError:
        log(f"  note  fontTools not installed: embedding {path.name} in full")
        axes = {}
    decls = [f"font-family: '{family}'", "font-display: block"]
    if "wght" in axes:
        decls.append(f"font-weight: {axes['wght'][0]:g} {axes['wght'][1]:g}")
    if "wdth" in axes:
        decls.append(f"font-stretch: {axes['wdth'][0]:g}% {axes['wdth'][1]:g}%")
    mime = {"woff2": "font/woff2", "woff": "font/woff", "truetype": "font/ttf"}[fmt]
    decls.append(f"src: url(data:{mime};base64,{base64.b64encode(data).decode()}) format('{fmt}')")
    log(f"  font  {family} (local {path.name})  {len(data) / 1024:.0f} KB")
    return "@font-face { " + "; ".join(decls) + "; }"


def _has_brotli():
    try:
        import brotli  # noqa: F401
        return True
    except ImportError:
        return False


# ---------- bundling ----------

class Bundler:
    def __init__(self, src, extra_text="", font_files=None, log=print):
        self.src = src
        self.log = log
        self.font_files = font_files or {}
        self.extra_text = extra_text
        self.local_css = {}
        self.local_js = {}

    def read_css(self, path, seen=()):
        """Local CSS with @import inlined and url() resolved to data URIs."""
        css = path.read_text(encoding="utf-8")

        def imp(m):
            ref = m.group(1)
            if is_remote(ref) or path in seen:
                return m.group(0)
            return self.read_css((path.parent / ref).resolve(), seen + (path,))
        css = CSS_IMPORT.sub(imp, css)
        return self.resolve_urls(css, path.parent)

    def resolve_urls(self, css, base):
        def sub(m):
            ref = m.group(2)
            if is_remote(ref):
                return m.group(0)
            p = (base / urllib.parse.unquote(ref.split("#")[0].split("?")[0])).resolve()
            return f"url({data_uri(p)})" if p.is_file() else m.group(0)
        return CSS_URL.sub(sub, css)

    def run(self):
        doc = self.src.read_text(encoding="utf-8")
        base = self.src.parent

        # Pass 1: read every local stylesheet and script, so the charset sees their text.
        for m in TAG.finditer(doc):
            tag, a = m.group(1).lower(), attrs_of(m.group(2))
            if tag == "link" and "stylesheet" in a.get("rel", "") and not is_remote(a.get("href", "#")):
                p = (base / a["href"]).resolve()
                self.local_css[a["href"]] = self.read_css(p)
            elif tag == "script" and a.get("src") and not is_remote(a["src"]):
                self.local_js[a["src"]] = (base / a["src"]).resolve().read_text(encoding="utf-8")
        chars = charset([doc, *self.local_css.values(), *self.local_js.values()], self.extra_text)
        self.log(f"  text  {len(chars)} characters ({len(chars) - len(ASCII)} beyond ASCII)")

        local_faces = "\n".join(local_face(fam, p, chars, self.log) for fam, p in self.font_files.items())
        placed_local = False

        def fonts_for(url):
            nonlocal placed_local
            rest = without_families(url, self.font_files)
            css = google_faces(rest, chars, self.log) if rest else ""
            if not placed_local:
                css, placed_local = (local_faces + "\n" + css).strip(), True
            return css

        def tag_sub(m):
            tag, a = m.group(1).lower(), attrs_of(m.group(2))
            if tag == "link":
                rel, href = a.get("rel", ""), a.get("href", "")
                if rel in ("preconnect", "dns-prefetch") and "fonts.g" in href:
                    return ""
                if "stylesheet" in rel and GOOGLE_CSS.match(href):
                    return f"<style>\n{fonts_for(href)}\n</style>"
                if "stylesheet" in rel and href in self.local_css:
                    css = GOOGLE_CSS_IMPORT.sub(lambda i: fonts_for(i.group(1)), self.local_css[href])
                    return f"<style>\n{css}\n</style>"
                return m.group(0)
            if tag == "script":
                src = a.get("src")
                if src in self.local_js:
                    js = self.local_js[src].replace("</script", "<\\/script")
                    return f"<script>\n{js}\n</script>"
                return m.group(0)
            # img / image
            for key in ("src", "href", "xlink:href"):
                ref = a.get(key)
                if ref and not is_remote(ref):
                    p = (base / urllib.parse.unquote(ref)).resolve()
                    if p.is_file():
                        return m.group(0).replace(m.group(2), re.sub(
                            rf"""(\s{re.escape(key)}\s*=\s*)("[^"]*"|'[^']*'|[^\s>]+)""",
                            lambda x: f'{x.group(1)}"{data_uri(p)}"', m.group(2), count=1))
            return m.group(0)

        doc = TAG.sub(tag_sub, doc)
        # Google Fonts @import and local url() inside inline <style> blocks and style attributes
        doc = re.sub(r"(<style\b[^>]*>)(.*?)(</style>)", lambda m: m.group(1) + self.resolve_urls(
            GOOGLE_CSS_IMPORT.sub(lambda i: fonts_for(i.group(1)), m.group(2)), base) + m.group(3),
            doc, flags=re.S | re.I)
        doc = re.sub(r"""(\sstyle\s*=\s*)(["'])(.*?)\2""",
                     lambda m: m.group(1) + m.group(2) + self.resolve_urls(m.group(3), base) + m.group(2),
                     doc, flags=re.S)
        if local_faces and not placed_local:
            doc = re.sub(r"</head>", f"<style>\n{local_faces}\n</style>\n</head>", doc, count=1, flags=re.I)
        return doc


GOOGLE_CSS_IMPORT = re.compile(r"""@import\s+(?:url\()?\s*['"]?(https?://fonts\.googleapis\.com/css2?\?[^'")\s]+)['"]?\s*\)?\s*;""")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html", type=Path)
    ap.add_argument("-o", "--out", type=Path, help="output path (default: <name>.bundled.html)")
    ap.add_argument("--text", default="", help="extra characters to include in the font subset")
    ap.add_argument("--text-file", type=Path, help="file whose characters are added to the subset")
    ap.add_argument("--font-file", action="append", default=[], metavar="FAMILY=PATH",
                    help="use a local font file for FAMILY instead of Google Fonts (repeatable)")
    args = ap.parse_args()

    extra = args.text + (args.text_file.read_text(encoding="utf-8") if args.text_file else "")
    fonts = {}
    for spec in args.font_file:
        fam, _, path = spec.partition("=")
        if not path or not Path(path).is_file():
            ap.error(f"--font-file expects FAMILY=PATH to an existing file: {spec}")
        fonts[fam.strip()] = Path(path)

    out = args.out or args.html.with_name(args.html.stem + ".bundled.html")
    print(f"bundle {args.html} → {out}")
    try:
        doc = Bundler(args.html.resolve(), extra, fonts).run()
    except OSError as e:
        sys.exit(f"error: {e}\nGoogle Fonts unreachable? Pass local files with --font-file FAMILY=PATH.")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    left = sorted(set(re.findall(r"""(?:href|src)\s*=\s*["']((?!data:|#|https?://www\.w3\.org)[^"']+)["']""", doc)))
    if left:
        print("  warn  still external: " + ", ".join(left))
    print(f"  done  {out.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
