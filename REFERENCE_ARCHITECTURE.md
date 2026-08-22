# REFERENCE_ARCHITECTURE.md

**Ajdevhub — Step 2: architectural analysis of `github.com/aspiremis/aspiremis.github.io`.**

Analysed 2026-08-16 at reference HEAD `2026-08-11` (shallow clone into a scratch directory;
nothing from it was copied into this repository).

Scope, per the brief: architecture, organisation, content-driven design, reusable components,
learning-system patterns, automation and UX ideas. **No content, personal information,
branding, copy, colour choices or domain-specific schemas from the reference are reproduced
here or proposed for adoption.** Where a pattern is worth taking, it is described in the
abstract and re-specified for Ajdevhub's own domains.

---

## 1. What the reference is

A greenfield Astro 7 engineering notebook for a postgraduate power-systems engineer, started
July 2026. 247 tracked files, 129 content files, ~1.08 M characters of prose.

| Layer | Choice |
|---|---|
| Framework | Astro 7, static output, `build.format: 'directory'` |
| Language | TypeScript, `astro/tsconfigs/strict`, path aliases |
| Content | Markdown + MDX via Content Collections, 15 collections |
| Validation | Zod schemas — every collection, every field |
| Styling | Tailwind CSS 4 (CSS-first `@theme`), one 406-line stylesheet |
| Math | `remark-math` + `rehype-katex`, rendered at **build time** |
| Code | Shiki, dual light/dark theme baked into one render |
| Search | Pagefind (full-text) + a small JSON index for the ⌘K palette |
| Feeds | `@astrojs/rss`, `@astrojs/sitemap` |
| Deploy | GitHub Actions → GitHub Pages, plus a nightly cron rebuild |

Explicitly rejected by the reference, and worth noting because the reasoning transfers:
**no React, no animation library.** Their stated argument is that pulling a framework runtime
into a static site for a few animations is the largest single threat to the performance
budget. Animation is CSS transitions plus one `IntersectionObserver`, honouring
`prefers-reduced-motion`.

---

## 2. The comparison the brief asked for

### 2.1 My current architecture

Jekyll 3.9. Content is 361 markdown files whose metadata is `layout` + `title` + `permalink`.
Structure lives in filename prefixes and folder names. Presentation lives as hand-written HTML
inside the markdown body, backed by 31 per-page stylesheets. UI that should be derived —
indexes, roadmaps, related links, progress — is hand-maintained. Nothing is validated.

### 2.2 Reference architecture

Content is 129 files whose metadata is a **typed, validated record**. Structure lives in
frontmatter fields (`track`, `module`, `order`, `prerequisites`). Presentation lives in 55
reusable components; content files invoke them semantically. Every index, breadcrumb,
prev/next link, progress bar and search entry is **derived at build time** from the metadata.
A typo in frontmatter fails the build.

### 2.3 The measurement that matters

Both sites are "markdown with some HTML in it". They are not remotely the same thing:

| | Ajdevhub `_learning/` | Reference `src/content/` |
|---|---:|---:|
| Presentational tags in content (`<div`, `<span`, `<section`, `style=`) | **52,820** | **0** |
| Semantic component invocations in content (`<Capitalised>`) | ~120 (mostly false positives) | **1,725** across 23 component types |
| Distinct components available to content authors | 1 (`problem-card.html`) | 55 |
| Total CSS | **11,995 lines** across 35 files | **406 lines** in 1 file |
| Per-page stylesheets | 31 | 0 |
| Content files | 361 | 129 |

The reference's most-used content components are `Callout` (605 uses), `Solution` (195),
`Exercise` (195), `CodeFile` (134), `Step` (117), `Compare` (103), `KeyIdea` (100),
`Quiz` (74), `Analogy` (48). Every one of those is a thing Ajdevhub's content *also* does —
it just does it by hand-writing a `<div class="mb4-hs">` and a matching CSS file each time.

This is the whole story in one line: **the reference solved presentation once and reuses it
1,725 times; Ajdevhub solves it again on every page.**

---

## 3. Patterns worth adopting

Ranked by value to Ajdevhub specifically.

### 3.1 Typed, validated content schemas — highest value

Every collection has a Zod schema. Fields have enums, defaults, ranges, regexes and
`.optional()` where genuinely optional. The build fails on a violation.

This directly fixes the audit's worst finding. Ajdevhub currently has **three duplicate
permalinks silently overwriting live pages** and **two editorials pointing at problem IDs that
don't exist** — both classes of bug are structurally impossible under a validated schema plus
a uniqueness/referential check. The audit found them by scripting; a schema would have found
them at author time.

The reference's schema file is also worth copying as a *practice*: it is heavily commented
with the reasoning behind each field, so the model documents itself.

### 3.2 Structure in frontmatter, never in filenames or URLs

Two rules, stated explicitly in the reference's schema comments:

> "Modules group lessons visually but deliberately do NOT appear in URLs
> (`/learning/matlab/variables`, not `/learning/matlab/foundations/variables`). That keeps
> paths short and means modules can be reorganised later without breaking a single link."

> "Lesson filenames carry no numeric prefix — ordering lives in `order`, so a lesson can be
> moved within its module without renaming the file and invalidating its URL."

Ajdevhub does the opposite on both counts. Ordering is encoded in filenames using **three
incompatible conventions** (`p4-m13-`, `module-b9-`, `m17-`, `ch5-`), and the folder path is
baked into the URL — which is exactly why 52 permalinks had to be hand-overridden to escape
their own directory structure, and why moving `_learning/networking/networking-mastery/` under
`/learning/networking-mastery/` broke the sidebar's active-category test on 27 pages.

Adopting this rule is what makes the taxonomy reorganisable later — which the brief demands
in §2 ("add new domains later without changing the application architecture").

### 3.3 The two-shapes content rule

> "Anything with a *body* to read is markdown under `src/content/<name>/`. Anything that is a
> pure *record* is one JSON list — appending an entry is one object, not a new file."

The reference uses `file()` loaders for `modules.json`, `resources.json`,
`publications.json`, `lab-courses.json`, and `glob()` loaders for everything with prose.
Crucially, **both go through the same Zod validation**.

Ajdevhub already has this instinct — `problems.yml` is exactly a validated record list, minus
the validation. The rule tells you where the other borderline cases belong: roadmap stages and
module definitions are records; concepts, editorials and posts are documents.

### 3.4 Build-time derivation isolated in a `lib/` layer

`src/lib/learning.ts` holds `getTrackTree()`, `getLessonNeighbours()`,
`resolvePrerequisites()`, `formatDuration()`. Pages and layouts call these; they contain no
traversal logic themselves. Two details worth stealing:

- **Prev/next crosses module boundaries** — the reader experiences one continuous sequence,
  not disconnected units.
- **Empty modules are kept deliberately**: "a scaffolded module still renders as a roadmap
  entry with its objectives visible, which is the honest way to show 'planned but not
  written' rather than hiding it."

That second point is a direct answer to Ajdevhub's 72 stub pages, which currently look
identical to finished work everywhere they appear.

### 3.5 Two kinds of progress, kept separate

This is the cleanest idea in the reference and the answer to brief §9.

- **Authored status** is frontmatter: `status: exploring | in-progress | consolidating |
  paused`, plus a self-assessed `progress: 0–100` annotated *"Honest, not aspirational."*
  This is the author's claim about the content, and it is build-time data.
- **Visitor completion** is `localStorage`, via one `ProgressStore` component: a single
  versioned key (`learn-progress:v1`), a `window.learnProgress` API, and a `learn:progress`
  event. Components opt in declaratively with `data-lesson-tick="<id>"` and
  `data-progress-group="a,b,c"` — so a new component gets progress for free without being
  wired individually. It degrades to "nothing done" in private mode rather than throwing, and
  ships an export/import escape hatch.

Ajdevhub currently has **8 scripts implementing progress independently with ad-hoc keys** and
no aggregate view. One store with declarative opt-in replaces all of them.

### 3.6 Components injected into MDX from the route

```
const components = { Callout, Analogy, KeyIdea, Exercise, Solution, Quiz, CodeFile, Compare };
...
<Content components={components} />
```

with the comment: *"Lessons stay clean prose with no import boilerplate at the top, and adding
a new component to the whole Hub is a one-line change here."*

This is the mechanism that makes 3.3's "0 presentational tags" achievable in practice. Without
it, every content file needs an import block and authors stop bothering.

### 3.7 Split search: navigation vs full-text

Two systems, deliberately:

- **Pagefind** (`pagefind --site dist` as a post-build step) indexes rendered HTML for
  full-text search, scoped by a `data-pagefind-body` attribute so nav and footer chrome don't
  pollute results.
- **A small hand-built JSON index** for the ⌘K palette, listing pages, projects, posts, notes,
  papers, tracks and lessons with a `section` label — jump-to-page, not full-text. Fetched
  lazily: *"a visitor who never presses ⌘K never downloads it."*

Ajdevhub's single 229 KB `search.json` tries to be both and is good at neither: it truncates
every document to 500 characters (so long module bodies are unsearchable), does naive
substring matching, and excludes editorials and problems entirely. The split solves all three.

### 3.8 Build-time math and dual-theme code

`remark-math` + `rehype-katex` render KaTeX **at build time** — no math library ships to the
browser. Shiki emits both light and dark themes from one render, so syntax highlighting costs
zero client JS and works in both modes.

Ajdevhub has **no math renderer at all**, which is disqualifying for the AI/ML and
graph-compiler domains in brief §2 and §12 — attention, softmax, backprop and shape inference
are not writable without it.

### 3.9 One semantic token layer, two-tier

`:root` / `.dark` declare semantic values; `@theme inline` maps them to utilities. Components
only ever reference semantic names, so *"changing `--accent` re-themes the entire site."*
Theme is class-driven (`@custom-variant dark`) rather than media-driven, so a toggle can
override the OS.

Ajdevhub has the right idea in `base.css` `:root` but 23 of 31 per-page stylesheets bypass it
with private variables and 658 hardcoded hex literals, so the promise doesn't hold.

### 3.10 Smaller things worth taking

- **Self-hosted variable fonts** with `unicode-range` subsetting and stable filenames so they
  can be `<link rel="preload">`ed. Replaces Ajdevhub's render-blocking Google Fonts request.
- **`consts.ts` as identity single-source** — name, links, nav, taxonomy in one file, with a
  README table saying *"to change X, edit Y"*.
- **Generated raster assets** (`scripts/generate-assets.mjs`, `sharp`) — favicon and OG card
  built from inline SVG at prebuild time, *"so the design stays editable in source control."*
  Ajdevhub's `og-default.png` is referenced by every page and **does not exist**; generating
  it removes that whole class of bug.
- **Build-time external API calls that fail soft** — GitHub data fetched during the build,
  never in the browser; if the API is down the component renders a fallback and the build
  still succeeds.
- **Nightly cron rebuild** so build-time-baked external data doesn't freeze between pushes.
- **`sitemap({ filter: page => !page.includes('/404') })`** — trivial, and Ajdevhub's sitemap
  currently carries 131 `node_modules` URLs.

---

## 4. What should NOT be copied

### 4.1 Anything domain-specific

The `journey` (semester/courses/LTP credits), `labCourses`, `experiments`, `instruments`,
`labGuides` and `publications` collections encode a taught postgraduate degree with physical
laboratory work. Ajdevhub has no equivalent. Copying the shapes would create empty ceremony.

The same goes for the `TRACK_ICONS` / `LAB_ICONS` enums, the topic taxonomy, the accent
colour, the font pairing, and every word of content.

### 4.2 The assumption that 15 collections is right

The reference has 15 collections for 129 files — roughly 8 files per collection. That density
is fine at its scale and would be over-modelled at Ajdevhub's. Brief §7 says it outright:
*"Do NOT blindly implement all of them if they are unnecessary."* Ajdevhub's real content
types are closer to six.

### 4.3 Tailwind, uncritically

Tailwind 4 works well there and produced a 406-line stylesheet. But that number is partly
because the site is seven weeks old with a single visual language. Ajdevhub is importing 57
bespoke, individually-designed pages; the honest question is whether those get **rebuilt on
shared components** (in which case Tailwind is a fine choice) or **carried across as-is**
(in which case a utility framework buys nothing and adds a build dependency). That decision
belongs in Step 3, and it should be made per-page, not globally.

### 4.4 Its CI, which is weaker than the brief requires

The reference's workflow is `checkout → setup-node → npm ci → npm run build → upload → deploy`.
Schema validation happens because `astro build` fails on a Zod violation — a real and valuable
gate — but:

- **`astro check` (type checking) exists as an npm script and is never run in CI.**
- There is **no link checking**, so the reference could ship the same broken-internal-link
  class of defect the Ajdevhub audit found 17 of.

Brief §24 asks for `install → validate content → type check → build → test → deploy`. The
reference implements roughly half of that. Adopt the shape, not the omissions.

### 4.5 Two things the reference has not solved

Its own "future enhancements" list is candid, and two entries matter here:

- **Backlinks between notes do not exist.** `[[wikilinks]]` render as plain text; a backlink
  index is listed as a future idea. Brief §11 asks for a navigable knowledge graph with
  prerequisites, related concepts and a dependency view. **The reference cannot be copied for
  this — Ajdevhub has to go further.** The closest transferable primitive is `prerequisites`
  as an id array resolved at build time, with unresolvable ids dropped (their comment:
  *"rendered as links, so typos show"* — a weak check that should be upgraded to a hard build
  failure).
- **Per-page OG images** are also future work.

### 4.6 The scale caveat, stated plainly

The reference is a **greenfield site with 129 content files, seven weeks old, 21 commits on
the cloned branch**. It has never migrated anything. It has no legacy URLs, no redirects, no
`-old` files, no accumulated HTML, no five-year commit history.

Ajdevhub has **361 learning files, 407 live URLs, 282 commits since 2021, and 3.18 M
characters of embedded markup**. Every pattern in §3 is sound in itself, but none of them has
been demonstrated at 3× the content volume with a migration attached. The patterns are
adoptable; the reference's *tidiness* is not evidence that adopting them will be tidy.

---

## 5. Recommended Ajdevhub architecture (pattern level)

The framework decision (Option A improve Jekyll / B migrate to Astro / C something else) is
Step 3's job and is deliberately **not** made here — brief §5 asks for it to be argued from
Ajdevhub's own repository, not inherited from the reference. What follows is
framework-independent: these are the properties the Step 3 proposal must deliver, whichever
option wins.

1. **A validated schema per content type**, with the build failing on violation, plus explicit
   uniqueness and referential checks — URL uniqueness, editorial↔problem integrity,
   prerequisite resolution.
2. **A single taxonomy constant** (domains/topics) that schemas validate against, so adding a
   domain is one edit and an invalid `domain:` is a build error.
3. **Structure in frontmatter, not filenames or paths.** `domain`, `track`, `module`, `order`,
   `status`. URLs stay short and stable; grouping is reorganisable without touching a URL.
4. **A component library that content invokes**, injected so authors write no imports. Target:
   the 52,820 presentational tags in `_learning/` collapse onto roughly 12–20 components.
5. **Derivation in one query layer** — indexes, breadcrumbs, prev/next, related, roadmap
   status, search entries all computed from metadata, never hand-listed.
6. **Two-layer progress** — authored `status` in frontmatter, visitor completion in one
   versioned localStorage store with declarative opt-in.
7. **Split search** — full-text over rendered output, plus a light navigation index for ⌘K,
   covering *all* content types including problems and editorials.
8. **Build-time math and dual-theme code highlighting**, zero client-side rendering libraries.
9. **One semantic token layer** that every component consumes, supporting light and dark.
10. **Preserve what already works**: `problems.yml`'s record model, URL-derived breadcrumbs,
    the PlantUML→SVG pipeline. These need re-hosting, not redesigning.

Two things the Step 3 proposal must additionally solve that the reference does **not** answer:

- **The knowledge graph** (brief §11) — bidirectional related-concept links and a dependency
  view. Needs original design.
- **The 407-URL migration** (brief §21) — the reference offers no guidance because it has
  never had a legacy URL. This is Step 4's core problem.

---

## 6. Honest read going into Step 3

The reference makes a strong case that **Astro + TypeScript + Content Collections is a good
fit for this class of site**, and most of §3 is either native to that stack or much easier in
it. I am not treating that as settled. Two facts cut the other way and will be argued properly
in Step 3:

- Several §3 patterns — validated data, derived indexes, a component library, split search,
  build-time math, a real token layer — are achievable in Jekyll with meaningfully less
  disruption, and Ajdevhub is a *working, deployed, five-year-old site*, not a blank page.
- The dominant migration cost is the 3.18 M characters of embedded presentational HTML, and
  **that cost is paid under either option**. It is a content-remediation problem, not a
  framework problem. Choosing Astro does not reduce it; choosing Jekyll does not avoid it.

The framework question therefore turns on which stack makes the *remaining* work cheaper over
several years, not on which one the reference happens to use.

---

**Step 2 complete.** Next: `PROPOSED_ARCHITECTURE.md` — the A/B/C evaluation, the content
model and schemas, component architecture, routing, search, learning/roadmap/DSA/progress
systems, and deployment. Then `MIGRATION_PLAN.md`. No production files change before both are
reviewed.
