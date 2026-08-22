# CURRENT_ARCHITECTURE.md

**Ajdevhub — Step 1 audit of `Ajay3007.github.io` (read-only).**

Audit date: 2026-08-15 · HEAD: `0c6a7f0` ("Phase 6: Cmd/Ctrl+K command palette search") · Branch: `master`

No repository files were modified during this audit. A build was run to a scratch directory
(`jekyll build -d <scratch>`) purely to derive the authoritative URL inventory and measure
output; nothing was written into `_site/` or into tracked files. This file and
`AUDIT_URL_INVENTORY.txt` are the only additions.

> **Flag:** this file has no YAML front matter, so Jekyll will copy it verbatim to
> `https://ajay3007.github.io/CURRENT_ARCHITECTURE.md`. Same for `AUDIT_URL_INVENTORY.txt`.
> Both should be added to `exclude:` in `_config.yml` before the next deploy. I have not
> made that change (Step 1 is read-only).

---

## 1. Executive summary

The site is a **Jekyll 3.9 / GitHub Pages** static site that has grown from a 2021
`jekyll-theme-cayman` portfolio into a 407-page technical knowledge base of ~4.0 M characters
of prose. It works, it deploys reliably, and the most recent five weeks of commits
(Phases 1–6, 2026-07-29 → 2026-07-31) moved real architecture in the right direction:
data-driven navigation, a data-driven roadmap hub, derived breadcrumbs, a shared design-token
layer, a docs layout with TOC, and a ⌘K command palette.

The problem is not the tooling. **The problem is that the content model stops at the page
boundary.** A learning page carries exactly four pieces of metadata — `layout`, `title`,
`permalink`, and occasionally `custom_css`/`custom_js`. Everything else the platform would need
in order to derive UI — domain, track, module, order, difficulty, status, prerequisites,
related concepts, tags — does not exist as data. It exists as hand-written HTML *inside* the
markdown body. That is why **44.2 % of the learning corpus source is markup rather than prose**,
why there are **31 per-page stylesheets totalling 10,029 lines** against a 1,966-line shared
design system, and why adding a concept today means editing between three and six files.

Three structural facts dominate everything downstream:

| Fact | Number | Consequence |
|---|---|---|
| Learning pages with any semantic metadata beyond title/permalink | **7 of 361** (`description`) | Nothing can be derived; every index is hand-written |
| Learning source that is HTML/CSS, not prose | **44.2 %** (3.18 M of 7.19 M chars) | Content is not portable to any other renderer without a de-HTML pass |
| Per-page CSS vs shared design system | **10,029 lines / 31 files** vs **1,966 lines / 4 files** | 23 of 31 page stylesheets define their *own* private colour variables — 31 parallel mini design systems |

There are also **three live content-loss bugs** (duplicate permalinks silently overwriting
pages), **17 broken internal links**, a **missing site-wide OG image**, and **two Python
maintenance scripts that no longer run** because they point at a `learning/` directory that
was renamed to `_learning/`. These are listed with exact locations in §7.

None of this argues for throwing the content away. It argues that the *metadata layer* has to
be built, and that the HTML-in-markdown is the single largest migration cost regardless of
which target architecture is chosen in Step 3.

---

## 2. Repository shape

```
Ajay3007.github.io/
├── _config.yml                  # 63 lines — 4 collections, 3 plugins, exclude list
├── _data/                       # 3 files
│   ├── nav.yml                  #  1.8 K — top nav + learning sidebar groups
│   ├── problems.yml             # 47 K  — 164 DSA problems (the one real database)
│   └── roadmaps.yml             #  3.6 K — 7 roadmap cards for /roadmap/
├── _includes/                   # 2 files only
│   ├── breadcrumbs.html         # derived from page.url — genuinely good
│   └── problem-card.html        # the site's only reusable component
├── _layouts/                    # 5 layouts
│   ├── default.html             # 182 lines — head, SEO, header, nav, ⌘K, footer
│   ├── learning.html            #  76 lines — 3-col docs shell (sidebar / body / TOC)
│   ├── editorial.html           # 230 lines
│   ├── post.html                #  29 lines
│   └── project.html             #  32 lines
├── _learning/                   # 361 md + 116 source artefacts   ← 95 % of the site
├── _posts/                      # 6 posts
├── _projects/                   # 5 projects
├── _editorials/                 # 22 DSA solutions
├── assets/
│   ├── css/                     # 35 files, 11,995 lines
│   ├── js/                      # 35 files,  2,312 lines
│   ├── diagrams/                # 83 CI-generated SVGs
│   ├── icons/  images/
├── blogs/                       # 8 hand-written category index pages
├── projects/index.md            # hand-written project grid (duplicates _projects data)
├── scripts/                     # 3 Python scripts (2 broken)
├── admin/                       # Decap CMS + Netlify Identity
├── .github/workflows/           # 2 workflows
└── 12 root-level .md docs       # README, CLAUDE, AUDIT_REPORT, 3× RELEASE_*, guides, prompts
```

Tracked files: **881**. Working tree: **333 MB** (`.git` 106 MB, `_site/` 113 MB untracked,
`node_modules/` 52 MB untracked, `_learning/` 49 MB).

---

## 3. Content inventory

### 3.1 Collections

| Collection | Files | Output URLs | Permalink pattern | Layout(s) |
|---|---|---|---|---|
| `_learning` | 361 md (+116 artefacts) | 358 | `/learning/:path/` — **overridden per file 353×** | `learning` (304), `default` (57) |
| `_editorials` | 22 | 21 ⚠️ | `/editorials/:title/` — overridden per file | `editorial` |
| `_posts` | 6 | 6 | `/blog/:year/:month/:day/:slug/` | `post` |
| `_projects` | 5 | 5 | `/projects/:path/` | `project` |
| Static pages | 13 | 17 | per-file `permalink` | `default` |

### 3.2 Learning corpus by domain

| Domain | md files | Notes |
|---|---:|---|
| `dsa` | 94 | 13 chapters, 18 topic-problem pages, 2 dead `-old` duplicates, 5 `published: false` |
| `system-design` | 67 | Track A (LLD, A1–A6), Track B (HLD, B1–B14), Track C (C1,C2,C4,C5 — **C3 missing**), each with a paired `-notes` page |
| `data-plane` | 53 | VPP (10 modules), DPDK (6), NGFW (8), 21 project modules |
| `programming-language` | 48 | C (11 + practice), C++, Java (12 sections + journal), Go/JS/Python/Rust stubs |
| `ai-ml` | 34 | Parts 1–9, 27 modules + roadmap |
| `networking` | 28 | Networking Mastery M01–M26 + roadmap |
| `backend` | 13 | M01–M17 with **5 gaps** (m08, m10, m12, m14, m16) |
| `finance` | 8 | tax_hurdle docs — arguably project documentation, not learning |
| `operating-systems` | 5 | mostly stubs |
| `oop` | 4 | plus 34 `.cpp` and 17 `.exe` |
| `competitive-programming` | 4 | mostly stubs |
| `4g-5g` | 1 | index + 14 `.puml` diagrams |

Volume: **7,187,144 raw chars → 4,009,047 chars of prose** after stripping tags,
`<style>` and `<script>` blocks. **72 of 361 files are under 40 lines** (stubs).

### 3.3 Non-markdown content in `_learning`

43 `.puml` (rendered to SVG by CI) · 34 `.cpp` · **17 `.exe`** (2.7 MB of committed Windows
binaries) · **15 `.pdf`** (30.6 MB — the single largest content weight) · 3 `.sh` · 3 `.c` ·
1 `.html` · 1 `.docx`. Plus `_learning/manim-scripts/` (153 files, 8.7 MB video tooling,
excluded from the build).

### 3.4 The DSA problem database — the one thing that already works

`_data/problems.yml`: **164 problems**, a perfectly consistent 9-key schema
(`id`, `title`, `platform`, `difficulty`, `topics[]`, `solved`, `problem_url`,
`approach_url`, `solution_url`), **19 topic slugs**, 56 solved. It feeds
`_includes/problem-card.html` and 18 topic pages, and is editable through Decap CMS.

**This is the design principle worth preserving verbatim into any new architecture.** Its
weaknesses are the surrounding plumbing, not the data:

- The 18 topic pages each re-implement the *same* ~89 lines of Liquid. A diff between
  `tree-problems.md` and `graphs-problems.md`, normalised for the topic slug, is **6 lines**.
  That is **1,597 lines of copy-paste** where a layout plus one front-matter key would do.
- The problem ↔ editorial relationship is maintained **manually in both directions** and is
  already inconsistent: 20 of 164 problems link to an internal editorial, while **2 of 22
  editorials (`#199`, `#572`) reference problem IDs that do not exist in `problems.yml`**.
- `_data/roadmaps.yml` hardcodes `curated_problems: "100+"` while `problems.yml` knows the
  real answer is 164. Two sources, one fact.

---

## 4. Template and rendering architecture

### 4.1 Layout hierarchy

```
default.html ──┬── post.html
               ├── project.html
               ├── editorial.html
               └── learning.html      (3-column docs shell)
```

`default.html` owns: hand-rolled SEO/OG/Twitter meta, canonical, feed autodiscovery, the four
core stylesheets, the data-driven top nav, the ⌘K palette markup, the footer, and the
Netlify Identity widget.

`learning.html` renders the docs shell: grouped sidebar from `nav.yml` + auto-listed
sub-pages, `breadcrumbs.html`, computed reading time, content, and an "On this page" TOC
hydrated by `docs.js`.

### 4.2 Where automation already exists (keep these)

| Mechanism | File | Quality |
|---|---|---|
| Breadcrumbs derived from `page.url`, link only if a real page exists | `_includes/breadcrumbs.html` | **Excellent** — genuinely content-driven |
| Top nav + sidebar groups from YAML | `_data/nav.yml` → `default.html`, `learning.html` | Good |
| Sidebar sub-pages auto-listed from `site.learning` when a category is active | `learning.html:21-26` | Good, but depth-1 only and defeated by permalink drift (§7.2) |
| Roadmap hub cards + live/soon counts from YAML | `_data/roadmaps.yml` → `roadmap.md` | Good, except the hardcoded `"100+"` |
| Problem cards from YAML | `problems.yml` → `problem-card.html` | **Excellent** |
| Reading time | `learning.html:37`, `post.html:15` | Fine |
| Blog archive grouped by category | `blogs/index.md` | Fine |
| PlantUML → SVG on push | `.github/workflows/plantuml-render.yml` | **Excellent** — temp-dir render, keeps good SVGs on failure, auto-commits |
| Sitemap, feed, robots.txt | `jekyll-sitemap`, `jekyll-feed` | Working |

### 4.3 Where it stops being automated

Everything else. Concretely, adding one new learning concept today requires:

1. Create the `.md` with `layout` / `title` / `permalink` front matter.
2. Hand-write the page chrome as HTML inside the markdown (hero, stat strip, tabs, cards).
3. Usually add a `<style>` block or a new `assets/css/<page>.css` + `custom_css` key.
4. Often add `assets/js/<page>.js` + `custom_js` key.
5. Hand-add a link on the parent index page.
6. Hand-add a link on the roadmap page, and update the roadmap's hardcoded counts.
7. If it is a new domain: hand-edit `_data/nav.yml`, `_learning/index.md` (hardcoded 10-card
   grid), and `index.md` (a *second* hardcoded 10-topic grid built from three parallel
   comma-split strings at `index.md:108-110`).

Nothing in steps 2–7 is derivable today, because the data to derive it from does not exist.

### 4.4 Two competing page styles

| Style | Count | Layout | Chrome | Per-page CSS |
|---|---:|---|---|---|
| "Docs" pages | 304 | `learning` | sidebar + breadcrumbs + TOC + reading time | shared (or `dsa-chapter`) |
| "Bespoke" pages | 57 | `default` | none — full-bleed custom design | own CSS + JS |

The 57 bespoke pages (all DSA chapters `ch0`–`ch12`, all system-design modules, the four
roadmaps) are the site's most visually impressive work and its least maintainable. They also
load per-page CSS through **two different mechanisms**: `custom_css` front matter (A1–A3,
B1–B3, phase0, roadmaps) versus a raw `<link rel="stylesheet">` inside the markdown body
(B4–B14, C1–C5). Same job, two conventions.

---

## 5. Assets

### 5.1 CSS — 11,995 lines across 35 files

| Layer | Files | Lines | Loaded |
|---|---:|---:|---|
| Core design system (`base`, `modules`, `syntax-print`, `signal`) | 4 | 1,966 | every page (56.6 KB unminified) |
| Per-page stylesheets (`sd-module-*` ×24, roadmaps ×5, `dsa-chapter`, `roadmap-hub`) | 31 | 10,029 | one page each |

`base.css` `:root` is a real design-token set (backgrounds, ink, rules, `--accent: #22d3ee`,
spacing scale, type scale, radii, durations, semantic colours) with legacy aliases mapped on
top for older classes. It is the right foundation.

It is also largely bypassed: **23 of the 31 per-page stylesheets declare their own private
variables** (`--muted` ×284, `--bord2` ×216, `--text` ×156, `--grn`, `--red`, `--cyan`,
`--sand`, `--gold`, `--aiml-1`…) alongside **658 hardcoded hex literals**. Each bespoke module
is effectively its own micro design system. There is no path by which changing `--accent`
restyles the site.

The site is **dark-only**; there is no theme toggle. `backend-roadmap.css:314-320` still
carries dead `[data-theme="dark"]` rules from the removed light/dark era.

### 5.2 JavaScript — 2,312 lines across 35 files

All 35 are referenced by at least one page (no orphaned files). Breakdown:

- `problems.js` (434) — client-side filter/search/progress for the Problems Hub.
- `command-palette.js` (162) — ⌘K over `search.json`.
- 4 roadmap scripts (632 total), 24 `sd-module-*` scripts (mostly 18–24 lines each).
- `docs.js` (90) — copy-code buttons + TOC scroll-spy.
- `home-hero.js` (85) — canvas packet animation.
- `nav.js` (49), `home.js` (44).

Two are dead:

- **`home.js`** is loaded on every homepage view and targets `.hf-tab`, `.hf-panel`,
  `#home-search`, `.project-card`, `.home-post-item` — **none of which exist** in the current
  `index.md`, which uses `.c-card` / `.c-post-row`. 44 lines, zero effect.
- **`nav.js:22`** queries `.nav-toggle`, which exists nowhere in the repo. The mobile nav
  therefore has no toggle button; `base.css` handles small screens by restyling `.site-nav`
  directly.

**8 scripts implement progress persistence** with independent, ad-hoc `localStorage` keys
(`sd-module-a1`, `a4`, `backend-roadmap`, `problems.js`, …). There is per-page progress but no
progress *system* — no shared key namespace, no aggregate view, no way to ask "what have I
finished in AI/ML?".

### 5.3 Third-party runtime dependencies (every page)

- Google Fonts (Inter + JetBrains Mono) — render-blocking external stylesheet.
- **`identity.netlify.com/v1/netlify-identity-widget.js`** — loaded on *every* page for a CMS
  used only at `/admin/`. This is the single biggest unnecessary payload on the site.

---

## 6. Search, SEO, deployment

### 6.1 Search

`search.json` (Liquid-generated, **229 KB**) indexes posts + projects + learning, at
`content | strip_html | truncate: 500`. `command-palette.js` fetches the whole file on first
⌘K and does substring matching in JS.

Gaps: **editorials and DSA problems are not indexed at all**; there is no ranking, no
stemming, no fielded search, no filtering by type; results carry only title/category/date; and
the 500-char truncation means the body of a 100 KB module page is unsearchable. The 229 KB
payload will grow linearly and unboundedly with content.

### 6.2 SEO

Hand-rolled in `default.html:11-49`: title, description, OG (type/title/description/url/
site_name/image/alt), article metadata for posts, Twitter summary_large_image, canonical, feed
autodiscovery. Structurally sound.

`jekyll-seo-tag` is declared in `_config.yml` and the `Gemfile` but **`{% seo %}` is never
called** — the plugin is dead weight.

Real defects:

- **`site.og_image` → `/assets/images/og-default.png` does not exist.** Every page on the site
  emits an `og:image` and `twitter:image` pointing at a 404. Social previews are broken
  site-wide.
- **7 of 361 learning pages have a `description`.** The other 354 fall back to
  `site.description` ("Projects and Learning Resources"), so 354 pages share one meta
  description. For a knowledge platform that expects search traffic, this is the highest-value
  SEO fix available.
- 2 of 6 posts have no `excerpt`, although `CLAUDE.md` documents it as required.
- No `404.html`.
- Sitemap: 553 URLs locally, of which **131 are `node_modules/` paths** (see §7.1).

### 6.3 Deployment

```
push to master ──► .github/workflows/jekyll-gh-pages.yml
                   actions/jekyll-build-pages@v1  ──►  upload-pages-artifact  ──►  deploy-pages
```

- Trigger branch is **`master`**, not `main`. `CLAUDE.md` states "GitHub Actions deploys on
  push to `main`" — **that documentation is wrong**.
- `actions/jekyll-build-pages@v1` builds in the GitHub Pages sandbox and **ignores the
  `Gemfile`**, allowing only whitelisted plugins. The three plugins in use are whitelisted, so
  this works today, but it silently caps what the site can ever do.
- **There is no validation step.** No link check, no schema check, no build-warning gate.
  Every defect in §7 could have been caught by CI and none was.
- Second workflow `plantuml-render.yml` renders all `.puml` → SVG and commits back to
  `master`. Well built (renders to a temp dir, keeps the previous SVG on failure, warns
  instead of failing the run).
- Local build: **9.9 s** for 407 pages, 115 MB output, on Jekyll 3.9.3 / Ruby 3.2.6.

### 6.4 CMS

Decap CMS at `/admin/` with Netlify Identity + Git Gateway (`site_domain:
ajdevhub.netlify.app`), configured for blog, projects, editorials and — notably — the
`problems.yml` database with typed widgets. It is the reason the problem database stayed clean.
It is also the likely origin of the editorial permalink collision in §7.1: the editorials
collection asks the author to type a `permalink` by hand.

---

## 7. Defects found

### 7.1 Live bugs — content is currently being lost or is unreachable

| # | Severity | Defect |
|---|---|---|
| 1 | **High** | `_editorials/tree/binary-tree-level-order-traversal.md` declares `permalink: /editorials/balanced-binary-tree/` — a copy-paste collision with `_editorials/tree/balanced-binary-tree.md`. Jekyll silently drops one. **The Level Order Traversal editorial does not exist on the live site**; 22 editorials produce 21 pages. |
| 2 | Medium | `_learning/dsa/index-old.md` and `_learning/dsa/index.md` both claim `permalink: /learning/dsa/`. Silent collision. |
| 3 | Medium | `_learning/dsa/master-problem-list-old.md` and `master-problem-list.md` both claim `/learning/dsa/master-problem-list/`. Silent collision. |
| 4 | Medium | `og_image: /assets/images/og-default.png` — file missing. Every page's social preview is broken. |
| 5 | Medium | `_config.yml`'s `exclude:` list **overrides Jekyll's defaults**, and re-adds `Gemfile`/`vendor` but **not `node_modules`**. Locally this copies 52 MB into `_site/` and injects **131 `node_modules` URLs into `sitemap.xml`**. CI is unaffected only because `node_modules` is gitignored — the sitemap is wrong on every local build and one committed dependency away from being wrong in production. |
| 6 | Medium | `scripts/validate_site.py` and `scripts/generate_summary.py --all` target `Path('learning')`, which no longer exists (content moved to `_learning/`). Running the validator prints "❌ Learning directory not found" and exits 0. **Both scripts documented in `CLAUDE.md` are no-ops.** |

### 7.2 Broken internal links (17, verified against the built site)

| Broken link | Cause |
|---|---|
| `/editorials/binary-tree-level-order-traversal/` | bug #1 above |
| `/editorials/reverse-nodes-in-k-group/` | actual slug is `reverse-nodes-k-group` |
| `/editorials/symmetric-tree/` | actual slug is `symmetrical-tree` |
| `/learning/networking-mastery/m15-socket-programming/`, `m16-raw-sockets-bpf/`, `m17-kernel-bypass/`, `m18-high-performance/`, `m26-ngfw-policy/` | roadmap links use old slugs; real slugs are `m15-sockets`, `m16-ebpf-xdp`, `m17-dpdk`, `m18-vpp`, `m26-policy-capstone` |
| `/learning/backend/m02-http/`, `/learning/backend/m08-db-scaling/` | `m02` has no `permalink` (real URL `…/m02-http-servers/`); `m08` was never written |
| `/learning/system-design/hld/module-b2-caching/`, `module-b9-rate-limiter-notes/`, `module-b14-notes/` | wrong slug; `-notes` permalink differs from filename; page never written |
| `/learning/dsa/trees/ch5-trees/` | `trees` vs `tree`, `ch5-trees` vs `ch5-trees-graphs` |
| `/learning/ai-ml/topics`, `/learning/networking/topics` | pages never created |
| `/learning/d/learning/dsa/recursion/sort_array_using_rec.cpp` | malformed href |

### 7.3 Convention drift

- **236 `target="_blank"` links carry no `rel="noopener"`**, against the rule stated in
  `CLAUDE.md` and `learning/COPILOT_RULES.md` (2,190 external links total, 276 without
  `noopener` in any form).
- **52 of 353 permalinks diverge from their file path**, and not by one rule but by four
  different ones: numeric-prefix stripping (`01-memory-layout.md` → `…/memory-layout/`),
  directory flattening (`_learning/networking/networking-mastery/m05-tcp.md` →
  `/learning/networking-mastery/m05-tcp/`), name shortening
  (`module-b8-youtube-notes.md` → `…/module-b8-notes/`), and legacy aliasing (`*-old.md`
  claiming the live URL). The flattening case actively breaks the sidebar: 27 Networking
  Mastery pages live outside `/learning/networking/`, so `learning.html`'s
  `page.url contains '/learning/networking/'` test never fires and the sidebar shows no active
  category on any of them.
- **3 of 407 URLs are `.html` files rather than directory URLs**, where the other 404 are
  directories:
  - `/about.html` — `about.md` has no `permalink`, so it outputs `about.html`, while
    `_data/nav.yml` and the footer both link to `/about`. GitHub Pages resolves the
    extensionless form, so it works, but `default.html` emits
    `<link rel="canonical" href=".../about.html">` — the canonical URL and the linked URL
    disagree on the site's second-most-visited page.
  - `/learning/programming-language/cpp/lambda-functions.html` — the one permalink with **no
    trailing slash** (all 352 others have one) produces a file, not a directory, so the
    trailing-slash form 404s.
  - `/learning/dsa/dsa-mastery-roadmap.html` — the standalone HTML document described below.
- **Case-inconsistent directories**: `_learning/dsa/Arrays`, `Graphs`, `Strings`,
  `Searching-Sorting` are capitalised while every sibling is lowercase. Permalinks
  hand-lowercase them, which masks the problem until someone renames a file on a
  case-insensitive filesystem.
- `_learning/COPILOT_RULES.md` — an internal AI-instruction file — is published at
  `/learning/COPILOT_RULES/`.
- `_learning/dsa/dsa-mastery-roadmap.html` is a **complete standalone HTML document**
  (1,116 lines, own `<!DOCTYPE>`, `<head>`, Google Fonts) sitting inside the collection. It
  renders at `/learning/dsa/dsa-mastery-roadmap.html` with no site chrome and no nav.
- The 7 blog category pages (`blogs/dsa/`, `blogs/algorithms/`, …) still carry
  **pre-redesign light-theme inline styles** — `background:white`, `#1e293b`, `#f8fafc`,
  purple `#667eea` gradients — on a dark-only site. They were missed by the Phase 1–6 redesign.
  `problems.md` has the same issue in its header strip.
- `projects/index.md` hand-codes all five project cards in HTML while `_projects/*.md` already
  holds `title`, `description`, `tags`, `year`, `github`, `demo`. The homepage renders the same
  five from the collection. One fact, two representations, one of them manual.

### 7.4 Content-state issues

- 5 files under `_learning/dsa/sorting/` are `published: false`, duplicating live content in
  `_learning/dsa/Searching-Sorting/`. Two parallel trees for one topic.
- **72 of 361 learning pages are stubs** (< 40 lines), including 8 Java section indexes, 6
  system-design fundamentals/patterns pages, and the Go/JS/Python/Rust language indexes. They
  are indistinguishable from finished pages in every index and in search, because there is no
  `status` field.
- Numbering gaps published as if complete: backend `m08`, `m10`, `m12`, `m14`, `m16`;
  system-design `c3`.
- 30.6 MB of PDFs and 2.7 MB of committed `.exe` binaries inside `_learning/`.

---

## 8. URL inventory

**407 live URLs.** The complete list is in `AUDIT_URL_INVENTORY.txt` (generated from a clean
build, sorted, one URL per line). Distribution:

| Route prefix | URLs |
|---|---:|
| `/learning/dsa/**` | 87 |
| `/learning/system-design/**` | 67 |
| `/learning/data-plane/**` | 53 |
| `/learning/programming-language/**` | 48 |
| `/learning/ai-ml/**` | 34 |
| `/learning/networking-mastery/**` | 27 |
| `/learning/backend/**` | 13 |
| `/learning/finance/**` | 8 |
| `/learning/operating-systems/**` | 7 |
| `/learning/oop/**`, `/learning/competitive-programming/**` | 6 each |
| `/learning/` + `/learning/networking/` + `/learning/4g-5g/` + `/learning/COPILOT_RULES/` | 4 |
| `/editorials/**` | 21 |
| `/blog/**` | 6 |
| `/projects/**` | 6 |
| `/blogs/**` | 8 |
| `/`, `/about/`, `/roadmap/`, `/problems/`, `/editorials-guide/`, `/admin/` | 6 |

Plus non-HTML outputs that are linked from pages and must survive any migration: 83 SVGs under
`/assets/diagrams/`, 15 PDFs and 34 `.cpp` files served from under `/learning/`, `/search.json`,
`/sitemap.xml`, `/feed.xml`, `/robots.txt`.

Stability assessment: `/learning/**` (358 URLs, 88 % of the site) is the block that matters.
Any restructuring that regularises the 52 divergent permalinks — which is the *correct*
engineering move — breaks live URLs unless each one gets a redirect. That trade-off is a
Step 3/Step 4 decision; the raw data is now captured.

---

## 9. Dependencies

**Ruby** (`Gemfile`, Ruby 3.2.6): `github-pages` (pins Jekyll 3.9.3), `liquid ~> 4.0.4`,
`webrick`, `jekyll-feed`, `jekyll-seo-tag` (**declared but unused**), `jekyll-sitemap`.

**Node** (`package.json`): `js-yaml ^4.1.1` — a single dependency, not referenced by any build
step; `node_modules/` also contains a Puppeteer/chromium-bidi tree, suggesting a one-off script
that is no longer present.

**Runtime, external:** Google Fonts, `identity.netlify.com` widget. No framework, no bundler,
no CSS preprocessor, no test suite, no linter, no type checking.

**CI:** `actions/checkout@v4`, `actions/configure-pages@v5`, `actions/jekyll-build-pages@v1`,
`actions/upload-pages-artifact@v3`, `actions/deploy-pages@v4`, `actions/setup-java@v4`,
PlantUML (latest from Maven Central), Graphviz.

---

## 10. Gap analysis against the target platform

Measured against the requirements in `prompt.md`:

| Requirement | Today | Gap |
|---|---|---|
| §6 Content drives the UI | Nav ✅, breadcrumbs ✅, roadmap cards ✅, problem cards ✅ — everything else manual | **Large.** No metadata to derive from |
| §7 Typed content schemas | None. No validation of any kind | **Total.** YAML front matter is unchecked; the 3 permalink collisions prove it |
| §8 Domain → Track → Module → Concept hierarchy | Implicit in folder names and file prefixes (`p4-m13-`, `module-b9-`, `m17-`) — three different encodings | **Large.** Hierarchy is in filenames, not data |
| §9 Learning status | Nothing. `published: false` is the only state flag | **Total.** 72 stubs are indistinguishable from finished pages |
| §10 Mental-model sections | Some pages do this well in prose; nothing is structured or queryable | **Large.** Convention exists in the author's head |
| §11 Knowledge graph / prerequisites / related | Hand-written links only | **Total.** No `prerequisites`, no `related`, no backlinks |
| §14 DSA single source of truth | ✅ `problems.yml` is genuinely good | **Small.** Kill the 1,597 lines of duplicated Liquid; add editorial↔problem validation |
| §15 Data-driven roadmaps | Hub is data-driven; the 7 roadmap *pages* are 300–1,150-line hand-built HTML | **Large.** Roadmap stages/topics are not data |
| §16 Search | 229 KB JSON + substring match; editorials and problems excluded | **Medium.** Pagefind or equivalent replaces this cleanly |
| §17 UI/UX | Strong dark visual identity; excellent code rendering | **Medium.** No light mode, no math renderer at all, 31 competing page styles |
| §19 Automated UI | Partial (see §4.2) | **Large** |
| §20 Design system | 4 shared layers + 31 private ones | **Large** |
| §21 URL compatibility | 407 URLs catalogued here | Manageable, but only if redirects are planned before any restructure |
| §22 SEO | Structure ✅; broken OG image, 354 pages sharing one description | **Medium** |
| §23 Performance | Static ✅, 9.9 s build ✅; but 56 KB always-on CSS, Netlify widget on every page, 175 KB max page | **Medium** |
| §24 CI with validation | Build + deploy only | **Total.** No validate, no type check, no tests |

---

## 11. Migration risks

Ranked by expected cost, highest first.

1. **HTML-in-markdown (44.2 % of the corpus).** 129 learning files contain more than 50 raw
   HTML tags; 93 embed a `<style>` block and 113 embed a `<script>`. This content is not
   markdown that happens to have some HTML in it — for the bespoke pages it *is* an HTML
   document with front matter. Any target renderer with a stricter content pipeline (MDX,
   Astro content collections, anything with component islands) will require a per-file
   conversion decision: keep as raw HTML, convert to components, or rewrite as prose. Assume
   this dominates the migration budget. **Do not estimate the migration without pricing this
   first.**
2. **The 52 divergent permalinks.** Regularising URLs is right and breaks live links.
   GitHub Pages has no server-side redirects; `jekyll-redirect-from` is whitelisted for Pages
   but does not exist in the current Gemfile, and a non-Jekyll target would need generated
   meta-refresh stubs. Every changed URL needs an explicit decision recorded in the Step 4
   mapping.
3. **Metadata backfill for 361 files.** Domain, track, module, order, status, difficulty, tags,
   prerequisites and related links have to be *authored*, not migrated — the information exists
   only in filenames, folder structure, and the author's memory. This is the work that makes
   §6–§11 of the brief possible, and it cannot be fully automated. Filename prefixes
   (`p4-m13-`, `module-b9-`, `m17-`, `ch5-`) give a decent first pass for `order` and `module`;
   `status` and the relationship graph do not.
4. **31 per-page stylesheets and 24 per-page scripts.** Each bespoke page is a bespoke design.
   Migrating them faithfully preserves 10 K lines of CSS debt; redesigning them onto shared
   components is the right call but is 57 pages of visual work.
5. **The three permalink collisions must be fixed before any inventory is trusted.** Right now
   the file count and the URL count disagree, and a naive "migrate every file" pass would
   resurrect `index-old.md` and `master-problem-list-old.md` as live pages.
6. **Binary weight.** 30.6 MB of PDFs, 2.7 MB of `.exe`, a 7.5 MB GIF, a 3 MB PNG, and 8.7 MB
   of manim assets, inside a 106 MB `.git`. Worth an explicit keep/LFS/drop decision — the
   `.exe` files in particular have no reason to be in a public knowledge platform.
7. **Decap CMS.** Tied to Netlify Identity and a Jekyll-shaped repo. Any change to collection
   folders or front-matter shape breaks `/admin/`. Decide early whether the CMS survives.
8. **Loss of the good parts.** `breadcrumbs.html`, `problem-card.html`, `problems.yml`, the
   PlantUML CI pipeline, and the `base.css` token set are the five things this repo already
   does right. They should be carried forward deliberately rather than rediscovered.

---

## 12. What is already right

Stated plainly, because the migration plan should protect these:

- `_data/problems.yml` + `problem-card.html` — a clean, typed, CMS-editable single source of
  truth with 164 well-formed records and zero schema drift.
- `_includes/breadcrumbs.html` — derived from the URL, verified against real pages, no
  hardcoding. Exactly the pattern the whole site needs.
- The PlantUML CI pipeline — source-of-truth `.puml` in the repo, SVG generated and committed
  automatically, failures degrade safely.
- `base.css` `:root` — a coherent, complete token set with a documented migration path from
  legacy aliases.
- `.gitattributes` — deliberate, well-commented, fixes a real historical mojibake/CRLF problem.
- The prose itself. 4 million characters of first-person technical writing across 12 domains,
  with a stated authorship philosophy (`COPILOT_RULES.md`) that keeps the thinking the
  author's own. **This is the asset. Everything in this document is in service of not losing
  it.**

---

## 13. Confidentiality check (brief §13)

Scanned for material that should not be public. Findings:

- No internal component names, APIs, chip specifications, benchmark numbers, or proprietary
  algorithms were found in the published content. The NGFW/VPP/DPDK material reads as generic
  public technical knowledge (VPP feature arcs, DPDK PMD polling, Snort integration patterns)
  of the kind covered by upstream project documentation.
- Two items to review before the migration, both process rather than leak:
  - `_learning/COPILOT_RULES.md` is published at `/learning/COPILOT_RULES/`. It is an internal
    working document; it should be excluded from the build.
  - `_learning/data-plane/ngfw/` describes a SASE/NGFW architecture at a level of detail
    (component split, packet path, IPS integration, build/deploy pipeline) that is close to the
    author's day job. Nothing there names an employer system, but **the author is the only
    person who can confirm the boundary**. Flagging rather than judging, per §13.
- The graph-compiler domain (§12 of the brief) does not exist in the repo yet, so there is
  nothing to review there. The confidentiality rule should be encoded as a content-schema
  concern (e.g. a `review: internal` status that blocks the build) rather than left as a habit.

---

## 14. Reading coverage

Fully read: `_config.yml`, all 5 layouts, both includes, all 3 `_data` files, `index.md`,
`roadmap.md`, `problems.md` (header), `about.md` (front matter), `blogs/index.md`,
`blogs/dsa/index.md`, `projects/index.md`, `_learning/index.md`, `COPILOT_RULES.md`,
`search.json`, `nav.js`, `home.js`, `docs.js`, `command-palette.js` (head), both workflows,
`Gemfile`, `package.json`, `.gitignore`, `.gitattributes`, `admin/config.yml`, all 3 Python
scripts (headers + path constants), all front matter in `_posts`, `_projects`, `_editorials`.

Analysed programmatically across the whole corpus: front-matter key frequency, layout and
`custom_css`/`custom_js` distribution, permalink divergence and collisions, HTML/prose ratio,
inline `<style>`/`<script>` counts, stub detection, CSS variable and hex-literal usage,
asset reference graph (orphan detection), external-link attributes, problem↔editorial
referential integrity, and a full internal link check against a clean build.

Not read line-by-line: the bodies of the 361 learning markdown files, the 24 `sd-module-*`
CSS/JS pairs, the 4 roadmap scripts, `editorial.html`, `problems.js`, and
`_learning/manim-scripts/` (excluded from the build). Statistical claims above about those
files are derived from scripted analysis, not from reading each one.

---

**Step 1 complete.** Next: `REFERENCE_ARCHITECTURE.md` (analysis of
`aspiremis/aspiremis.github.io`), then `PROPOSED_ARCHITECTURE.md`, then `MIGRATION_PLAN.md`.
No production files will be changed before those are reviewed.
