# ajdevhub

Portfolio site for Ajay Kumar Gupt (software engineer focused on networking, data plane, and backend systems). The site is a Jekyll-powered static site deployed via GitHub Pages, with custom layouts, navigation, and content sections for blogs, projects, and learning notes.

## Quick start
- Clone the repo and install Ruby with Jekyll: `gem install jekyll bundler` (no Gemfile is committed; use system gems).
- From the repo root, run a local preview:

```
jekyll serve --livereload
```

## Site structure
- Home: [index.md](index.md#L1-L127) sets the landing page with tabs, search, and recent posts/projects fed by `site.posts` and `site.projects`.
- Blogs index: [blogs/index.md](blogs/index.md#L1-L70) lists categories and every post generated from [_posts](_posts).
- Projects index: [projects.md](projects.md#L1-L20) lists all entries from [_projects](_projects).
- Learning hub: [learning/index.md](learning/index.md) links to topic subfolders (DSA, system design, networking, AI/ML, etc.).
- About: [about.md](about.md#L1-L33) has the personal summary.
- Layouts: [ _layouts/default.html](_layouts/default.html#L1-L38) defines the shared shell; posts and projects use [ _layouts/post.html](_layouts/post.html#L1-L18) and [ _layouts/project.html](_layouts/project.html#L1-L17).
- Styling: [assets/css/main.css](assets/css/main.css) contains all theme, card, and responsive rules.
- Scripts: [assets/js/nav.js](assets/js/nav.js) handles the mobile nav toggle; [assets/js/home.js](assets/js/home.js) powers home-page tabs, search filtering, and entry animations.

## Content authoring
- Blog posts: add Markdown files to [_posts](_posts) named `YYYY-MM-DD-slug.md` with front matter `layout: post`, `title`, `date`, `categories`, and optional `excerpt`; see [2025-01-05-two-pointer-technique.md](_posts/2025-01-05-two-pointer-technique.md#L1-L46).
- Projects: add Markdown files to [_projects](_projects) with `layout: project`, `title`, and optional `description`; see [face-recognition.md](_projects/face-recognition.md#L1-L53).
- Learning pages: plain Markdown under [learning/](learning/index.md) and its subfolders. Use `layout: default` and relative links.

## Navigation and URLs
- Active nav is computed in the default layout using `page.url` substring checks. Posts render under `/blog/...`; project pages under `/projects/...` based on [_config.yml](_config.yml#L1-L24).
- Use `{{ '/path' | relative_url }}` in templates to stay compatible if `baseurl` changes. Content Markdown can link with relative paths.

## Deploy
GitHub Pages builds the site automatically on push. No CI scripts are required; ensure content compiles locally with `jekyll serve` if you change layouts or config.

## Preview
- Live site: https://ajay3007.github.io
- Local: `jekyll serve --livereload` then open http://127.0.0.1:4000. The livereload script will refresh as you edit Markdown, layouts, CSS, or JS.

## Contribute
- Keep pages under the existing layouts and collections (`_posts`, `_projects`, `learning/`).
- Use relative links or the `relative_url` filter for new nav items and cross-page links.
- Run a local serve before committing layout or CSS changes to catch Liquid or build errors early.

### Create a blog post
1) In `_posts`, add a file named `YYYY-MM-DD-slug.md` (e.g., `2025-02-15-my-topic.md`).
2) Add front matter like:

```markdown
---
layout: post
title: "Post Title"
date: 2025-02-15
categories: [dsa, algorithms]
excerpt: "One-line summary for listings."
---
```

3) Write content in Markdown below the front matter. Code blocks auto-style via the post layout.
4) Preview locally (`jekyll serve --livereload`) and verify it appears under Blogs and in the home recent posts.

### Create a project page
1) In `_projects`, add `my-project.md`.
2) Add front matter like:

```markdown
---
layout: project
title: "Project Name"
description: "Short description shown on listings."
---
```

3) Add project details (overview, tech stack, usage). Listings pull `title` and `description` automatically.
4) Preview locally and confirm it appears on Projects and the home recent projects block.

### Add a learning page
1) Pick or create a topic folder under `learning/` (e.g., `learning/dsa/` or `learning/networking/`).
2) Add a Markdown file such as `index.md` or `topic-name.md` with front matter:

```markdown
---
layout: default
title: "Topic Title"
---
```

3) Write your content in Markdown. Use relative links to other learning pages (e.g., `../` for sibling topics) and to site pages via `{{ '/path' | relative_url }}` if needed.
4) Link the new page from its parent index (for example, add a bullet in `learning/index.md` or the relevant sub-index) so it’s discoverable from the Learning hub.
5) Preview locally to ensure navigation and links work.

### Navigation checklist (for new sections)
- If you add a brand-new top-level area, update the nav links in [ _layouts/default.html](_layouts/default.html#L9-L25) and use `relative_url`.
- Ensure Learning hub indexes link down to your new page (parent `learning/index.md` and any relevant sub-index).
- Verify the nav active state still works after your change by visiting the new page locally.

### Common mistakes
- Forgetting front matter: pages without `layout` and `title` won’t render with the site shell or show correct headings.
- Missing `relative_url` on template links: hardcoded paths can break if `baseurl` changes; follow existing patterns.
- Post filenames not using `YYYY-MM-DD-slug.md`: Jekyll will skip or misdate them.
- Not updating indexes: new learning pages must be linked from their parent `index.md` to be discoverable.
- Editing CSS/JS without local preview: always run `jekyll serve --livereload` to catch layout or script issues early.

## File map
| Path | Purpose |
| --- | --- |
| [index.md](index.md) | Home page with tabs, search, and recent posts/projects.
| [blogs/index.md](blogs/index.md) | Blog landing page and category tiles.
| [projects.md](projects.md) | Projects listing fed by `_projects` collection.
| [about.md](about.md) | About page content.
| [_config.yml](_config.yml) | Jekyll site config, collections, plugins, permalinks.
| [_layouts/default.html](_layouts/default.html) | Shared shell, header/nav/footer, scripts.
| [_layouts/post.html](_layouts/post.html) | Post layout wrapper.
| [_layouts/project.html](_layouts/project.html) | Project layout wrapper.
| [assets/css/main.css](assets/css/main.css) | Global styling, layout, responsive rules.
| [assets/js/nav.js](assets/js/nav.js) | Mobile nav toggle and scroll behavior.
| [assets/js/home.js](assets/js/home.js) | Home page tabs, search filter, animations.
| [_posts/]( _posts) | Blog posts (`YYYY-MM-DD-slug.md`).
| [_projects/]( _projects) | Project pages with `layout: project`.
| [learning/index.md](learning/index.md) | Learning hub index linking to topic subfolders.
