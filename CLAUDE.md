# Arknights Industrial · 舟工业: project notes

An Agent Skill (`arknights-industrial/`) for industrial sci-fi graphic design: game-style interfaces, key visuals, emblems, infographics. Unofficial fan project, not affiliated with Hypergryph.

## Decisions already made with the owner

- **Name**: Arknights Industrial · 舟工业. The GitHub repo is still called `coldprint`; the owner renames it in GitHub settings.
- **Language**: SKILL.md and references in English; description carries Chinese trigger words. README in English plus `README.zh-CN.md`. Talk to the owner in Chinese.
- **No proprietary names in the skill body.** Reference works, studios and publishers are never named in SKILL.md, the references or prompts. README may say it is an unofficial fan project.
- **Reference screenshots are for analysis only and are never committed** to this repo (it will go public). Keep them outside the repo or in a separate private repo. `.gitignore` covers `refs/`, `bili-refs/`.
- **One unified style**, industrial sci-fi only, with small dialect differences. Not a multi-genre system (rejected: borrowing retro-futurism etc. per story).
- **Scope**: interfaces and key visuals first. No character illustration, no animation for now.
- **License**: MIT (Copyright (c) 2026 Alex), same as `bespoke-reader`.
- **Default dialect**: field (near-white ground, ink, signal yellow), from Endfield-era design. Other dialects: terminal (dark navy/cyan), paper (olive), wartime (grey, black, crimson; from an event screen set with distressed title, triangle motif, grey imagery with red only).

## Layout

```
arknights-industrial/
  SKILL.md                 principles, dialects, workflow, self-check
  references/              techniques, parameters, cjk-typography, outputs, image-prompts
  assets/kit.css, kit.js   dialect tokens + shared components/helpers
  assets/templates/        poster.html (done); event-hub, mission-list, shop, stage-map (to do)
  scripts/                 bundle.py, render_check.py (to do)
```

## Status (update as work lands; delete this section before release)

Done on branch `draft`: English SKILL.md restructured around nine principles and four dialects; references split; kit.css/kit.js; poster template.

To do, in order:
1. `scripts/bundle.py`: inline local CSS/JS and Google Fonts subsetted with the css2 `text=` parameter (returns woff2 with `unicode-range`), output one self-contained HTML. Always include printable ASCII in the subset (CSS `text-transform: uppercase`).
2. `scripts/render_check.py`: Playwright screenshot plus checks: text outside the artboard, overlapping text boxes, text below the per-medium minimum (`references/parameters.md`), more than one saturated hue by area. Skip elements with `data-role="ghost"`/`"texture"`.
3. Workflow order in SKILL.md §5 should become build → bundle → check (check the delivered file).
4. Fix in kit: reversed bar is invisible on terminal-dark (needs `--bar-bg`/`--bar-fg` tokens, light bar on dark ground); check vertical CJK rail once real fonts load.
5. Interface templates: event hub, mission list, shop, stage map. Rule: system chrome (back/home, global nav) stays neutral; the brand color belongs to the event.
6. Analyse the owner's reference screenshots (Endfield PVs, event screens) and refine the dialect table, the motif system and "Not this". Do not copy compositions.
7. README.md / README.zh-CN.md with original example renders (no reference images).
8. Before going public: remove this status section, make sure no reference images are in history.

## Rendering note

In the cloud container, headless Chromium rejects the proxy's TLS certificate, so pages cannot load Google Fonts directly. Bundle first (Python fetches fonts fine), then render the bundled file. Launch Chromium with `executable_path='/opt/pw-browsers/chromium'`.
