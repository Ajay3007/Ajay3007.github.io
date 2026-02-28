# ajdevhub

Portfolio and learning journal for **Ajay Kumar Gupt** — software engineer focused on networking, data plane, and backend systems. Built with Jekyll and deployed via GitHub Pages.

**Live site:** https://ajay3007.github.io

---

## Quick Start

```bash
# First-time setup
gem install jekyll bundler
bundle install

# Local dev server with live reload
bundle exec jekyll serve --livereload
# Opens at http://127.0.0.1:4000
```

---

## Site Architecture

### Layout hierarchy

| Layout | File | Used by |
|--------|------|---------|
| Base shell | `_layouts/default.html` | All pages — header, nav, footer, dark mode, scripts |
| Blog post | `_layouts/post.html` | Inherits default; wraps `<article class="post">` |
| Project | `_layouts/project.html` | Inherits default; wraps `<article class="project">` |
| Learning | `_layouts/learning.html` | Long-form learning pages with sidebar TOC |

### Key pages

| URL | Source | Description |
|-----|--------|-------------|
| `/` | `index.md` | Home — tabs, hero, recent posts/projects |
| `/about/` | `about.md` | Personal summary |
| `/blog/` | `blogs/index.md` | Blog listing by category |
| `/projects/` | `projects.md` | Projects listing |
| `/learning/` | `learning/index.md` | Learning hub |
| `/learning/dsa/` | `_learning/dsa/index.md` | DSA hub with live solved/total counts |
| `/problems/` | `problems.md` | **Interactive Problems Hub** — searchable/filterable table |

### Collections (defined in `_config.yml`)

- `_posts/` → `/blog/:year/:month/:day/:slug/`
- `_projects/` → `/projects/:path/`
- `_editorials/` → `/editorials/:title/` (written approach notes)

---

## Problems System

The Problems Hub is driven by a **single YAML file as source of truth**. No duplication across pages.

### Data flow

```
_data/problems.yml
       │
       ├─► /problems/          (Interactive Hub — JS renders the table)
       │
       └─► /learning/dsa/<topic>/<topic>-problems/   (Liquid-powered topic pages)
```

### Adding a new problem

1. Open `_data/problems.yml` and append a new entry:

```yaml
- id: '1'
  title: Two Sum
  platform: leetcode
  difficulty: easy         # easy | medium | hard
  topics:
    - arrays
    - searching-sorting    # use existing slugs; see topic list below
  solved: false            # true once you've solved it
  problem_url: https://leetcode.com/problems/two-sum/
  approach_url: ''         # leave empty or fill per EDITORIALS_GUIDE
  solution_url: ''         # leave empty or fill per EDITORIALS_GUIDE
```

2. Save — the problem **automatically appears** in both the Problems Hub and every topic page whose slug matches an entry in `topics`.

### Recognised topic slugs

| Slug | Dedicated page |
|------|---------------|
| `arrays` | `/learning/dsa/arrays/arrays-problems/` |
| `strings` | `/learning/dsa/strings/strings-problems/` |
| `linked-list` | `/learning/dsa/linked-list/linked-list-problems/` |
| `tree` | `/learning/dsa/tree/tree-problems/` |
| `stacks` | `/learning/dsa/stacks/stacks-problems/` |
| `searching-sorting` | `/learning/dsa/searching-sorting/searching-sorting-problems/` |
| `sliding-window` | — (filters hub only) |
| `two-pointers` | — (filters hub only) |

---

## Content Authoring

### Blog post

1. Create `_posts/YYYY-MM-DD-slug.md`
2. Add front matter:

```yaml
---
layout: post
title: "Post Title"
date: 2025-02-15
categories: [dsa, algorithms]
excerpt: "One-line summary for listings."
---
```

3. Write content below. Preview at `/blog/`.

### Project page

1. Create `_projects/my-project.md`
2. Add front matter:

```yaml
---
layout: project
title: "Project Name"
description: "Short description shown in listings."
---
```

3. Add details. Preview at `/projects/`.

### Learning page

1. Create `_learning/<topic>/my-page.md` with `layout: default` or `layout: learning`.
2. Set a permalink: `permalink: /learning/<topic>/my-page/`
3. Link the new page from its parent `index.md`.

### DSA topic page (problem list)

Topic pages use a standard Liquid template — no manual HTML required. To add a new one:

1. Create `_learning/dsa/<topic>/<topic>-problems.md`:

```liquid
---
layout: default
title: <Topic> - Practice Problems
permalink: /learning/dsa/<topic>/<topic>-problems/
---

{% assign topic_slug = "<topic>" %}
{% assign topic_back_url = "/learning/dsa/<topic>/" %}

{% assign topic_all    = site.data.problems.problems | where_exp: "p", "p.topics contains topic_slug" %}
{% assign topic_solved = topic_all | where: "solved", true %}
{% assign topic_easy   = topic_all | where: "difficulty", "easy" %}
{% assign topic_medium = topic_all | where: "difficulty", "medium" %}
{% assign topic_hard   = topic_all | where: "difficulty", "hard" %}

# <Emoji> <Topic> — Practice Problems

<div class="topic-crosslinks">
  <a href="{{ '/problems/' | relative_url }}" class="topic-hub-link topic-hub-link--primary">🎯 All Problems Hub</a>
  <a href="{{ topic_back_url | relative_url }}" class="topic-hub-link">← Back to <Topic></a>
  <a href="{{ '/learning/dsa' | relative_url }}" class="topic-hub-link">📊 DSA Hub</a>
</div>

<!-- stats bar, easy/medium/hard grids — copy from any existing topic page -->
```

2. Add the new topic slug to `topicPages` in `assets/js/problems.js` so the hub banner and tag links work.

3. Add a chip link in `problems.md` under the `topic-chips` div.

---

## Navigation & URLs

- All template links must use the `relative_url` filter: `{{ '/path' | relative_url }}`
- External links in Markdown must include security attrs: `[Text](https://url){:target="_blank" rel="noopener noreferrer"}`
- Nav active state uses `page.url` substring matching in `_layouts/default.html`

---

## Styling & Scripts

| File | Purpose |
|------|---------|
| `assets/css/main.css` | Single stylesheet — CSS custom properties, dark mode via `[data-theme=dark]` |
| `assets/js/nav.js` | Mobile nav toggle, scroll-aware header |
| `assets/js/problems.js` | Problems Hub — filtering, search, topic banners, tag links |
| `assets/js/typing.js` | Home page typing animation |

**CSS custom properties (root):**
- `--primary-color`, `--secondary-color`, `--accent-color`
- `--bg-color`, `--card-bg`, `--shadow`, `--shadow-sm`
- `--text-color`, `--light-text`, `--border-color`

**Dark mode:** toggled via `document.documentElement.setAttribute('data-theme', 'dark')` and persisted in `localStorage`.

---

## File Map

```
.
├── _config.yml                   Jekyll config, collections, plugins
├── _data/
│   └── problems.yml              Single source of truth for all DSA problems
├── _editorials/                  Written editorial .md files
├── _includes/
│   └── problem-card.html         Canonical reusable problem card component
├── _layouts/
│   ├── default.html              Base shell — header, nav, footer, dark mode
│   ├── learning.html             Learning pages with sidebar TOC
│   ├── post.html                 Blog post wrapper
│   └── project.html              Project page wrapper
├── _learning/
│   └── dsa/
│       ├── index.md              DSA hub (live problem counts)
│       ├── Arrays/               Arrays guide + sub-pages
│       ├── Strings/
│       ├── linked-list/
│       ├── stacks/
│       ├── tree/
│       ├── Searching-Sorting/    Includes sorting-guide.md, searching-guide.md
│       ├── binary-search/
│       ├── dynamic-programming/
│       ├── graphs/
│       ├── queues/
│       ├── recursion/
│       └── backtracking/
├── _posts/                       Blog posts (YYYY-MM-DD-slug.md)
├── _projects/                    Project pages (layout: project)
├── assets/
│   ├── css/main.css              All styles
│   ├── js/
│   │   ├── nav.js
│   │   ├── problems.js
│   │   └── typing.js
│   └── icons/
├── index.md                      Home page
├── about.md                      About page
├── problems.md                   Problems Hub (Interactive)
├── projects.md                   Projects listing
├── blogs/index.md                Blog listing
├── learning/index.md             Learning hub index
└── EDITORIALS_GUIDE.md           Guide: how to add problems & solutions
```

---

## Deploy

GitHub Actions deploys on push to `main`. Working branch is `master`; merge `master → main` to publish.

```bash
git push origin master        # save work
git push origin master:main   # publish to GitHub Pages
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| No `layout` in front matter | Page renders without site shell |
| Hardcoded `/path` in templates | Use `{{ '/path' \| relative_url }}` |
| `_posts` file not named `YYYY-MM-DD-slug.md` | Jekyll skips or misdates it |
| Problem not appearing in topic page | Check the `topics` array in `problems.yml` uses exact slug |
| Duplicate permalink across two files | One will silently overwrite the other in `_site` — use `published: false` on the stale file |
