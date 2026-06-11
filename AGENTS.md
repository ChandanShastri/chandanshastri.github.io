# Repository Guidelines

## Scope
- This repository is a static GitHub Pages site.
- The main entry points are standalone HTML files at the repo root and under `apps/` and `games/`.
- Preserve the existing no-build, no-framework structure unless the user explicitly asks for a larger refactor.

## Editing Rules
- Prefer editing the relevant HTML file in place instead of introducing a build step.
- Keep relative paths intact for links, images, icons, and embedded assets.
- Make changes minimal and focused on the requested page or feature.
- Do not add dependencies, bundlers, or generated output unless the task clearly requires it.

## UI And Content
- Match the existing visual style of the page you are editing.
- Keep game pages self-contained when possible.
- Favor responsive behavior and mobile-safe interactions for interactive pages.

## Validation
- For HTML/CSS/JS changes, check the affected page paths and confirm links or assets still resolve.
- If a change affects a game or interactive page, validate the targeted page specifically rather than the entire site.

## Repository Layout
- `index.html` is the main landing page.
- `games/` contains standalone game pages.
- `apps/` contains standalone app pages.
- `imgs/` stores shared image assets.