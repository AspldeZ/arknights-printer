# Arknights Printer · 舟工业: project notes

An Agent Skill (`arknights-printer/`) for industrial sci-fi graphic design. The product is a poster / information sheet about a real-world subject (a lab measurement, a glacier, a protocol, a planet, a space station), styled as a document issued by an institution. The game is only the source of the style: extract the style, never the game's patterns. We are not making a game, so no game screens (event hub, shop, mission list, stage map). Unofficial fan project, not affiliated with Hypergryph.

## Decisions already made with the owner

- **Name**: Arknights Printer (2026-10-04). Directory `arknights-printer/`. The GitHub repo is still called `coldprint`; the owner renames it.
- **Language**: SKILL.md and references in English; description carries Chinese trigger words. README in English plus `README.zh-CN.md`. Talk to the owner in Chinese.
- **No proprietary names in the skill body.** Reference works, studios and publishers are never named in SKILL.md, the references or prompts. README may say it is an unofficial fan project.
- **Reference screenshots are for analysis only and are never committed** to this repo (it will go public). Keep them outside the repo or in a separate private repo. `.gitignore` covers `refs/`, `bili-refs/`.
- **One unified style**, industrial sci-fi only, with small dialect differences. Not a multi-genre system (rejected: borrowing retro-futurism etc. per story).
- **Scope** (corrected 2026-10-04): posters and information sheets about real subjects, single or as a numbered series; key visuals, emblems, archive cards, slides. No game interfaces, no character illustration, no animation.
- **Style benchmark**: the owner's earlier outputs in `/Users/aspldez/Desktop/design/工业VI/` (2D-NMR, Rhone glacier, SCION, Mars core, ISS ground track and configuration). New work is judged against these.
- **License**: MIT (Copyright (c) 2026 Alex), same as `bespoke-reader`.
- **Brand color is decided by the theme**, never fixed in the skill (2026-10-04). Dialect colors are examples only; color is not a focus of further work.
- **Color rule** (2026-10-03): one dominant brand color; status colors `--alert`/`--timed` as small tags only (≤1% of area); one optional counter color per event (`--counter`) for numerals, emphasis words and hairlines only (≤3%). `render_check.py` enforces these by role.
- **Density is a user parameter** (2026-10-04): airy / standard (default, the level of the benchmark sheets) / dense, budgets in SKILL.md §4a. Whitespace matters; the A/B test sheets were judged too dense. Do not force multi-view heroes.
- **No large type** (2026-10-04): no display titles, anchor words, progressive sentences or ghost type. The title or index number is the largest text, about 3× the label size. Large type rarely looks expensive.
- **Event guide long-image** (竖版长图攻略): not in scope for now.
- **Default dialect**: field (near-white ground, ink, signal yellow), from Endfield-era design. Other dialects: terminal (dark navy/cyan), paper (olive), wartime (grey, black, crimson; from an event screen set with distressed title, triangle motif, grey imagery with red only).

## Layout

```
arknights-printer/
  SKILL.md                 principles, dialects, workflow, self-check
  references/              techniques, parameters, cjk-typography, outputs, image-prompts
  assets/kit.css, kit.js   dialect tokens + shared components/helpers
  assets/templates/        poster.html
  scripts/                 bundle.py, render_check.py
```

## Status (update as work lands; delete this section before release)

Done on branch `draft`: English SKILL.md restructured around nine principles and four dialects; references split; kit.css/kit.js; poster template; `scripts/bundle.py` (local CSS/JS/images inlined, Google Fonts subset via css2 `text=`, variable-weight rules merged so each file is embedded once, `--font-file` offline fallback with optional fontTools subsetting); `scripts/render_check.py` (checks: fallback font via CDP, text ink outside artboard, ink overlap, size per medium with CJK +2px, saturated hues by area in OKLCH); SKILL.md §5 is now build → bundle → check → deliver; kit `--bar-bg`/`--bar-fg` (light bar on terminal-dark), `.rail` with `text-orientation: mixed` and `.up` for upright digits.

To do: owner commits this folder into the `coldprint` repo; before going public, remove this status section and confirm no reference images are in history. Optional: render_check could detect an empty hero.

Research notes on the source game's design: `references-private/design-research-2026-10.md` (gitignored). Only the style findings apply; the game-UI usability findings were removed from the skill on 2026-10-04.

## Rendering note

In the cloud container, headless Chromium rejects the proxy's TLS certificate, so pages cannot load Google Fonts directly. Bundle first (Python fetches fonts fine), then render the bundled file. Launch Chromium with `executable_path='/opt/pw-browsers/chromium'`.
