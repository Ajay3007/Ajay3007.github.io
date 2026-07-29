# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Local development:**
```bash
bundle exec jekyll serve --livereload
# Opens at http://127.0.0.1:4000
```

**First-time setup:**
```bash
gem install jekyll bundler
bundle install
```

**Python maintenance scripts** (no external dependencies required):
```bash
python scripts/generate_summary.py learning/dsa/Arrays/index.md   # Single file
python scripts/generate_summary.py --batch learning/dsa/           # Directory
python scripts/generate_summary.py --all                           # All learning sections
python scripts/add_changelog_entry.py "Message"                    # Log entry
python scripts/validate_site.py                                    # Validate structure/links
```

## Architecture

This is a Jekyll static site deployed to GitHub Pages at https://ajay3007.github.io. The working branch is `master`; GitHub Actions deploys on push to `main`.

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
