# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

The site is **Astro** (production since the Phase 11 cutover). Node ≥ 20.

```bash
npm ci
npm run dev          # astro dev → http://localhost:4321
npm run verify       # what CI runs: validate content, astro check, mount AxioByte, build, link check
npm run build        # astro build && pagefind
npm run axiobyte     # mount the pinned AxioByte experiences at public/axiobyte/ (see below)
```

`.github/workflows/deploy.yml` builds and deploys on **push to `master`** — pushing to this branch
publishes to production. `astro-ci.yml` runs the same checks on pull requests.

## AxioByte — interactive experiences under /axiobyte/

`/axiobyte/<domain>/<concept>/` (e.g. `/axiobyte/networking/nic/`) is **not built here**. Its source
is `github.com/Ajay3007/axiobyte-studio` (`experiences/`). This repo only:

- pins a released build in `axiobyte.json` (`tag`, `asset`, `sha256`);
- mounts it at build time with `scripts/fetch-axiobyte.mjs` into `public/axiobyte/` (gitignored —
  never commit it);
- renders the hub pages `src/pages/axiobyte/` from its `manifest.json` (`src/lib/axiobyte.ts`).

To upgrade, bump the three pin values from the Studio release notes. To work against a local
Studio build: `AXIOBYTE_LOCAL=../axiobyte-studio/experiences/dist npm run axiobyte`.
AxioByte is deliberately **not** a `projects` collection entry.

## Legacy Jekyll sources

The sections below describe the **Jekyll** site that preceded the Astro cutover. Its sources
(`_layouts/`, `_posts/`, `_projects/`, `_config.yml`, `Gemfile`) are still in the repository but are
no longer built or deployed. The Astro source is `src/` (content collections in
`src/content.config.ts`, pages in `src/pages/`).

**Template hierarchy:**
- `_layouts/default.html` — base shell with header, nav (active state via Liquid `page.url` matching), footer, and shared scripts
- `_layouts/post.html` — inherits default; wraps `<article class="post">`
- `_layouts/project.html` — inherits default; wraps `<article class="project">`

**Content types and locations:**
- `_posts/YYYY-MM-DD-slug.md` — blog posts; accessed via `site.posts`; permalink `/blog/:year/:month/:day/:slug/`
- `_projects/slug.md` — project pages; accessed via `site.projects`; permalink `/projects/:path/`
- `learning/` — unstructured Markdown files manually cross-linked; not a Jekyll collection

**Required front matter for posts:**
```yaml
layout: post
title: "Title"
date: YYYY-MM-DD
categories: [category]
excerpt: "Short description"
```

**Required front matter for projects:**
```yaml
layout: project
title: "Title"
description: "Short description"
```

## Link Conventions

All internal template links must use the `relative_url` filter:
```liquid
{{ '/path/to/page' | relative_url }}
```

External links in Markdown must include security attributes:
```markdown
[Link text](https://example.com){:target="_blank" rel="noopener noreferrer"}
```

Nav active state uses exact or substring matching:
```liquid
{% assign cur = page.url | default: '/' %}
class="{% if cur == '/' %}active{% endif %}"
class="{% if cur contains '/blog' %}active{% endif %}"
```

## CSS

Core styles live in four ordered layer files under `assets/css/`, loaded in this order by `_layouts/default.html` (load order = cascade order):
1. `base.css` — reset, `:root` design tokens, base elements, site shell (header/nav/footer), buttons, global search
2. `modules.css` — feature/page modules (problem cards, topic pages, learning sidebar, breadcrumbs, post article, scroll-to-top)
3. `syntax-print.css` — Rouge code highlighting + print stylesheet
4. `signal.css` — the "Signal / Packet" component system (`c-*` classes: hero, sections, cards, about, timeline, project visualizers)

The site is **dark-only**. Design tokens (in `base.css` `:root`) are the single source of truth:
- Colour: `--bg: #06080d`, `--panel`, `--panel-2`, `--ink`, `--body`, `--dim`, `--rule`; single accent `--accent: #22d3ee`; `--warm` (used sparingly). Legacy aliases (`--primary-color`, `--secondary-color`, `--accent-color`, `--bg-color`, `--card-bg`, `--shadow`, `--shadow-sm`) map onto these for older classes.
- Scale: `--space-*`, `--fs-*`, `--leading-*`, `--radius-*`, `--container`, `--z-*`, `--dur-*`, and semantic `--info` / `--tip` / `--warn` / `--danger`.

Per-page CSS is still loaded additionally via the `custom_css` front-matter key (e.g. roadmap pages), after the core layers.

## AI Assistant Constraints

Per `learning/COPILOT_RULES.md`: when editing learning content, do not introduce new technical ideas or decide system design choices. Only expand or clarify content that the author has already written. Ask rather than assume when intent is unclear.
