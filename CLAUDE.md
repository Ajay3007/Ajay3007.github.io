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

Single stylesheet at `assets/css/main.css`. CSS custom properties (defined in `:root`):
- `--primary-color: #1a1f36`, `--secondary-color: #00d4ff`, `--accent-color: #ff6b9d`
- `--bg-color: #f7fafc`, `--card-bg: #ffffff`, `--shadow`, `--shadow-sm`

## AI Assistant Constraints

Per `learning/COPILOT_RULES.md`: when editing learning content, do not introduce new technical ideas or decide system design choices. Only expand or clarify content that the author has already written. Ask rather than assume when intent is unclear.
