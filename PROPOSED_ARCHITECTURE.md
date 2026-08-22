# PROPOSED_ARCHITECTURE.md

**Ajdevhub — Step 3: proposed architecture.**

Written 2026-08-16, against the audit in `CURRENT_ARCHITECTURE.md` and the pattern analysis in
`REFERENCE_ARCHITECTURE.md`. **Nothing in the production site has been changed.**

---

## 1. The decision: Option A vs B vs C

### 1.1 What the choice actually turns on

The audit produced one number that reframes this question: **3.18 M characters (44.2 %) of the
learning corpus is embedded presentational HTML — 52,820 `<div>`/`<span>`/`style=` occurrences
across 361 files.**

That cost is paid under **every** option. Rewriting hand-written HTML onto reusable components
is content remediation, not a framework migration. Choosing Astro does not reduce it; staying
on Jekyll does not avoid it. Any evaluation that treats "migration cost" as the deciding factor
is measuring the wrong thing, because the dominant cost is common to all three.

So the real question is narrower: **which stack makes the work that remains cheaper over the
next several years?**

### 1.2 The three options

**Option A — Improve Jekyll in place.** Stay on Jekyll, add a Node-based content validation
layer in CI, convert per-page CSS onto the existing token system, replace duplicated Liquid
with layouts and parameterised includes, add Pagefind, switch CI from
`actions/jekyll-build-pages` to a custom `bundle exec jekyll build` step so non-whitelisted
plugins (KaTeX, redirects) become available.

**Option B — Migrate to Astro** with TypeScript, Content Collections, Zod, MDX, Pagefind,
KaTeX and Shiki.

**Option C — Something else.** Eleventy, Hugo, VitePress/Docusaurus, or a Jekyll + Node hybrid.

### 1.3 Evaluation

Scored against the brief's own criteria. "Both" means the option does not differentiate.

| Criterion | A · Jekyll improved | B · Astro | C · Others |
|---|---|---|---|
| **Type safety** | None. Liquid has no type system. Validation possible only as an external script | Native. Zod schemas + TS strict; `astro check` in CI | 11ty: external script only. Hugo: none. VitePress: partial |
| **Schema validation** | Achievable — a `validate-content.mjs` in CI gives ~90 % of the benefit | Native, and the *build itself* fails on violation | Achievable everywhere as an external step |
| **Components inside content** | **The weak point.** `{% include callout.html body="…" %}` cannot cleanly wrap multi-paragraph markdown. Nesting prose inside an include means escaping or splitting content | MDX: `<Callout>` wraps arbitrary markdown; components injected from the route so content files need no imports | 11ty WebC/shortcodes: same wrapping problem as Jekyll. Hugo shortcodes: better than Liquid, worse than MDX |
| **Migration complexity** | **Lowest.** Content stays put; URLs untouched; incremental | High. New build, new templates, 407-URL mapping, Decap reconfiguration | Medium–high; no better than B while offering less |
| **Build performance** | 9.9 s today; fine at 3× | Comparable; better incremental dev | Hugo faster, irrelevant at this scale |
| **Math rendering** | Needs `kramdown-math-katex` + custom CI build step | Native `remark-math`/`rehype-katex` | Both |
| **Search** | Pagefind works on any static output | Same | Same |
| **GitHub Pages** | Native, but `jekyll-build-pages` caps plugins unless CI is rewritten anyway | Works via Actions artifact upload | Works |
| **Dynamic generation / derived UI** | Liquid can do it; expressing a track→module→concept tree with prev/next and resolved prerequisites in Liquid is painful and untestable | TypeScript functions in `src/lib/`, unit-testable | 11ty: JS, good. Hugo: painful |
| **Content relationships / graph** | Possible; every traversal is hand-rolled Liquid | Straightforward TS; backlinks derivable | 11ty comparable to B |
| **Long-term extensibility** | Caps out. Every new capability is a bespoke Liquid or external script | Strong | 11ty close; ecosystem thinner |
| **Author familiarity** | Known — 5 years of it | New: Node, TS, Astro | New, with less payoff |
| **Decap CMS survives** | Yes, unchanged | Yes, with reconfigured collections — Decap is git-based, not Jekyll-specific | Yes |

### 1.4 Recommendation: **Option B — Astro**

Three reasons, in order of weight.

**1. The components-inside-content problem is structural, and only MDX solves it well.** The
brief's core requirement is that adding one content file integrates it everywhere. But the
*content itself* is the problem here: 52,820 presentational tags exist because there was no
good way to write a callout, a comparison table, or a step list without hand-rolling a `<div>`.
Jekyll's answer — a parameterised include — cannot wrap multi-paragraph markdown without
escaping it into a string argument. That is precisely why the current site's authors reached
for raw HTML instead. Migrating to Jekyll-with-better-includes would leave the incentive that
created the debt fully intact.

**2. Validation should fail the build, not a side-script.** Option A's validator is a separate
process that can be skipped, forgotten, or drift from reality — exactly what happened to
`validate_site.py`, which has been silently exiting 0 against a directory that no longer exists.
In Astro, an invalid `domain:` is a build error with a file and field name. That difference
matters more than it sounds given the three live permalink collisions.

**3. The brief asks for a decade-long platform.** Over that horizon, TypeScript query functions
that can be unit-tested beat untestable Liquid traversals, and the gap widens as the knowledge
graph, progress system and roadmap derivation grow.

**Against the recommendation, honestly:** Option A is materially cheaper, lower-risk, and the
site works today. If the constraint were "ship improvements this month with minimal risk", A
would be the right answer — and §9 below carves out exactly that work so it can happen
regardless. Option C is dismissed not because Eleventy is bad but because it lands between A
and B on every axis: nearly B's migration cost for meaningfully less of B's benefit.

**One decision that de-risks B substantially:** Astro renders plain `.md` with raw HTML passed
through unchanged, exactly as Jekyll does. MDX's stricter JSX parsing applies only to `.mdx`.
So **legacy pages migrate as `.md` and keep their hand-written HTML working on day one**, and
conversion to `.mdx` + components happens page-by-page afterwards. The 3.18 M characters of
HTML do not block the migration — they become a backlog that can be worked down over months
with the site live throughout. This is the single most important implementation detail in this
document.

---

## 2. Directory structure

```
src/
├── consts.ts                  Identity, nav, DOMAINS taxonomy — the first file to edit
├── content.config.ts          Every collection schema (Zod)
├── content/
│   ├── concepts/              Learning content — the core collection
│   │   └── <domain>/<slug>.md(x)
│   ├── tracks/                One file per track (AI/ML, Networking Mastery, Graph Compilers…)
│   ├── modules.json           Module records — grouping only, never in URLs
│   ├── editorials/            DSA solutions
│   ├── posts/                 Blog
│   ├── projects/              Project pages
│   ├── problems.json          Migrated from _data/problems.yml
│   └── resources.json         Books, papers, courses, tools
├── components/
│   ├── content/               MDX components authors use: Callout, Compare, Steps, …
│   ├── concept/               MentalModel, Intuition, MathView, CompilerView, …
│   └── ui/                    Card, Badge, Tag, Breadcrumb, ProgressRing, …
├── layouts/                   BaseLayout, ConceptLayout, ArticleLayout, ProjectLayout, EditorialLayout
├── lib/
│   ├── content.ts             Shared queries, publish filters
│   ├── graph.ts               Prerequisites, related, backlinks, dependency graph
│   ├── tracks.ts              Track → module → concept tree, prev/next
│   ├── problems.ts            DSA queries, problem ↔ editorial resolution
│   └── urls.ts                Canonical URL resolution + redirect emission
├── pages/                     File-based routes
└── styles/global.css          Token layer
scripts/
├── validate-content.mjs       Uniqueness, referential integrity, confidentiality gate
├── check-links.mjs            Internal link check against dist/
└── generate-assets.mjs        Favicon + OG card from SVG
public/
├── diagrams/                  PlantUML output (pipeline preserved)
└── fonts/                     Self-hosted variable fonts
```

---

## 3. Content model

Six collections, not fifteen. Each is justified by content that exists today.

| Collection | Loader | Replaces | Count |
|---|---|---|---:|
| `concepts` | glob `.md`/`.mdx` | `_learning/**` | ~361 |
| `tracks` | glob `.md` | roadmap pages + `_data/roadmaps.yml` | ~10 |
| `modules` | `file()` JSON | filename prefixes (`p4-m13-`, `module-b9-`) | ~60 |
| `problems` | `file()` JSON | `_data/problems.yml` | 164 |
| `editorials` | glob `.md` | `_editorials/**` | 22 |
| `posts` / `projects` | glob `.md` | `_posts`, `_projects` | 6 / 5 |
| `resources` | `file()` JSON | *new* — books, papers, courses, tools (brief §7) | 0 → n |

Applying the reference's two-shapes rule: things with a body to read are markdown; pure records
are one JSON list.

### 3.1 The taxonomy constant

```ts
// src/consts.ts — adding a domain is one line here, and nothing else.
export const DOMAINS = [
  { slug: 'ai-ml',            label: 'AI / ML' },
  { slug: 'compilers',        label: 'Compilers & Graph Compilers' },
  { slug: 'systems',          label: 'Systems & OS' },
  { slug: 'networking',       label: 'Networking' },
  { slug: 'data-plane',       label: 'Data Plane' },
  { slug: 'distributed',      label: 'Distributed Systems' },
  { slug: 'system-design',    label: 'System Design' },
  { slug: 'dsa',              label: 'DSA & Algorithms' },
  { slug: 'languages',        label: 'Programming Languages' },
  { slug: 'engineering',      label: 'Engineering Practice' },
  { slug: 'finance',          label: 'Finance' },
] as const;
```

This is what makes brief §2 work — *"add new domains later without changing the application
architecture."* An unknown `domain:` in frontmatter becomes a build error naming the file.

### 3.2 The `concepts` schema

```ts
const concepts = defineCollection({
  loader: glob({ base: './src/content/concepts', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),          // required — fixes 354 pages sharing one meta description

    domain: domainEnum,               // validated against DOMAINS
    track: z.string().optional(),     // must resolve to a tracks entry
    module: z.string().optional(),    // must resolve to a modules.json slug
    order: z.number().default(99),    // ordering lives here, NEVER in the filename

    /** Brief §9 — the author's own claim, honest not aspirational. */
    status: z.enum(['not-started', 'learning', 'understood', 'solid']).optional(),
    difficulty: z.enum(['foundational', 'intermediate', 'advanced']).optional(),

    /** Brief §11 — concept ids. Unresolvable ids fail the build. */
    prerequisites: z.array(z.string()).default([]),
    related: z.array(z.string()).default([]),

    tags: z.array(z.string()).default([]),
    estimatedMinutes: z.number().int().positive().optional(),
    updated: z.coerce.date().optional(),

    /** Migration: the URL this page has today. Absent = derive from domain + slug. */
    url: z.string().optional(),
    /** Old URLs that must keep working — emitted as redirect stubs. */
    redirectFrom: z.array(z.string()).default([]),

    /** Brief §13 — 'review' content builds locally but fails a production build. */
    visibility: z.enum(['public', 'review']).default('public'),
    draft: z.boolean().default(false),
  }),
});
```

Three fields deserve explanation.

**`order`, not filename prefixes.** Today ordering is encoded three incompatible ways
(`p4-m13-`, `module-b9-`, `ch5-`). Moving a concept means renaming a file and breaking its URL.
With `order` in frontmatter, resequencing is a number change.

**`url` as data, not derivation.** This is the key migration decision and it is deliberately
*not* what the reference does. 52 of the current permalinks diverge from their file path, and
regularising them would break live URLs. Carrying the existing URL as an explicit field makes
the migration lossless, makes new content default to a clean derived URL, and — because a
uniqueness check runs over the resolved set — makes the three current silent collisions
impossible to reintroduce.

**`visibility`.** Brief §13 asks for uncertainty to be flagged rather than published. A
`review` value keeps a page working in local dev and hard-fails the production build, so
"I'll check that later" cannot ship by accident.

### 3.3 Tracks and modules

```ts
const tracks = defineCollection({                    // one markdown file per track
  loader: glob({ base: './src/content/tracks', pattern: '**/*.md' }),
  schema: z.object({
    title: z.string(), tagline: z.string(), description: z.string(),
    domain: domainEnum,
    order: z.number(),
    status: z.enum(['active', 'planned', 'paused']),
    tags: z.array(z.string()).default([]),
  }),
});

const modules = defineCollection({                   // modules.json — records, not pages
  loader: file('./src/content/modules.json'),
  schema: z.object({
    id: z.string(), track: z.string(), slug: z.string(),
    title: z.string(), description: z.string(),
    order: z.number(),
    stage: z.string().optional(),                    // roadmap stage label, e.g. 'Phase 2'
  }),
});
```

Modules group concepts for display and **never appear in URLs**, so the AI/ML track can be
resequenced from 9 parts to 6 without touching a single link.

### 3.4 Problems and editorials — preserving what works

`problems.yml`'s 9-field schema migrates unchanged, plus two additions:

```ts
const problems = defineCollection({
  loader: file('./src/content/problems.json'),
  schema: z.object({
    id: z.string(), title: z.string(),
    platform: z.enum(['leetcode', 'gfg']),
    difficulty: z.enum(['easy', 'medium', 'hard']),
    topics: z.array(z.string()).min(1),
    solved: z.boolean().default(false),
    problem_url: z.url(),
    approach_url: z.string().default(''),
    solution_url: z.string().default(''),
    /** NEW — concept ids this problem exercises. Powers "related concepts" both ways. */
    concepts: z.array(z.string()).default([]),
  }),
});
```

Editorials keep `problem_id`, and **a build-time check asserts it resolves** — the two orphans
(`#199`, `#572`) become build failures instead of silent dead links. The relationship is
declared once, on the editorial, and the reverse link is derived rather than stored.

### 3.5 Mental-model sections (brief §10)

Not schema fields — MDX components, so an author uses only the ones that fit:

```mdx
<Intuition>Attention is a soft dictionary lookup…</Intuition>
<MentalModel>Q asks, K advertises, V delivers.</MentalModel>
<MathView>$\text{softmax}(QK^\top/\sqrt{d_k})V$</MathView>
<CompilerView>Fusable with the following softmax when…</CompilerView>
<HardwareView>Memory-bound at short sequence lengths…</HardwareView>
<Confusion>Attention weights are not feature importances.</Confusion>
<MyUnderstanding>Still shaky on multi-query vs grouped-query.</MyUnderstanding>
```

Each renders a labelled block *and* registers itself, so a concept page can show which
perspectives it covers and the domain index can surface "concepts with a compiler view". The
brief's rule is respected: nothing is mandatory.

---

## 4. Component architecture

Target: the 52,820 presentational tags collapse onto **roughly 20 components**, injected from
the route so content files carry no imports.

| Group | Components |
|---|---|
| Content (MDX) | `Callout`, `KeyIdea`, `Compare`, `Steps`/`Step`, `CodeFile`, `Figure`, `Table`, `Exercise`, `Solution`, `Quiz`, `Terminal` |
| Concept sections | `Intuition`, `MentalModel`, `MathView`, `CompilerView`, `HardwareView`, `Confusion`, `MyUnderstanding` |
| UI | `Card`, `Badge`, `Tag`, `Breadcrumb`, `StatusChip`, `ProgressRing`, `PrerequisiteList`, `RelatedConcepts`, `ConceptGraph`, `Sidebar`, `TableOfContents`, `SearchPalette` |
| Domain | `ProblemCard` (port of today's), `ProjectCard`, `ResourceCard`, `TrackTree`, `RoadmapStage` |

The 24 `sd-module-*.js` scripts and their 24 stylesheets are the acid test: they exist because
each module page invented its own tabs, checklists and stat strips. Three shared components
(`Tabs`, `Checklist`, `StatStrip`) retire most of that. What genuinely cannot be generalised
stays as a page-scoped `.astro` component — scoped styles mean no global CSS file per page.

---

## 5. Routing and URL strategy

```
/                                     index.astro
/learning/                            domain index, derived from DOMAINS + concept counts
/learning/[domain]/                   domain page: tracks, modules, concepts, progress
/learning/[...slug]/                  concept — resolved from `url` or derived
/roadmaps/  /roadmaps/[track]/        derived from tracks + modules + concepts
/problems/  /problems/[topic]/        one dynamic route replaces 18 near-identical pages
/editorials/[slug]/                   as today
/blog/[year]/[month]/[day]/[slug]/    unchanged
/projects/  /projects/[slug]/         unchanged
/resources/  /tags/[tag]/  /search/   new
/404
```

**URL preservation is the hard constraint.** The rule:

1. Every one of the 407 current URLs is carried as an explicit `url` on its content entry.
   Nothing changes by default.
2. `scripts/validate-content.mjs` asserts the resolved URL set is unique and that every URL in
   `AUDIT_URL_INVENTORY.txt` still resolves. **A dropped URL fails the build.**
3. Where a URL genuinely should change, the old one goes in `redirectFrom[]` and a static
   redirect stub is emitted. Nothing 404s.
4. New content omits `url` and gets the clean derived form.

Deliberately *not* adopting the reference's "derive URLs from structure" rule wholesale: it is
correct for a greenfield site and would break 52 live URLs here.

---

## 6. Learning, roadmap, DSA and progress systems

### 6.1 Hierarchy (brief §8)

`Domain → Track → Module → Concept → sub-concepts`, entirely from data: `domain` on the track,
`track`/`module`/`order` on the concept, sub-concepts via `prerequisites`/`related`. Adding
`concepts/ai-ml/attention.md` with `track: transformers, module: core-mechanism, order: 3`
places it in the track tree, the roadmap, the sidebar, prev/next, search and the domain index
with no other edit.

### 6.2 Knowledge graph (brief §11)

`src/lib/graph.ts`:

- resolves `prerequisites[]` and `related[]` to real concepts; **unresolvable ids fail the
  build** (stronger than the reference, which silently drops them);
- **derives backlinks** — if A lists B, B shows A, so the relationship is authored once;
- exposes `getNeighbourhood(id, depth)` for a small dependency diagram;
- detects prerequisite cycles and fails the build.

Deliberately not over-engineered per §11: no site-wide graph visualisation initially, just
per-concept prerequisites, related, backlinks and prev/next.

### 6.3 Progress (brief §9) — two layers

- **Authored**: `status: not-started | learning | understood | solid` in frontmatter, shown as
  `StatusChip`, aggregated per module/track/domain at build time. Optional — pages without it
  simply show nothing.
- **Visitor**: one versioned `localStorage` store with declarative `data-*` opt-in, replacing
  the 8 ad-hoc implementations, with export/import and graceful degradation.

The two never mix: authored status is the author's honest self-assessment; visitor completion
is per-browser.

### 6.4 Roadmaps (brief §15)

`_data/roadmaps.yml` is **deleted, not migrated.** A roadmap becomes a *view* over
`tracks + modules + concepts`, grouped by `stage`. This removes the duplication the audit
found — the hardcoded `"100+ curated problems"` becomes `problems.length` (164), and module
counts stop being hand-maintained strings.

### 6.5 DSA (brief §14)

The 18 near-identical topic pages (1,597 lines, 6-line diff between any two) become **one
dynamic route** over the topic list derived from `problems.json`. Problem cards, filters,
difficulty splits and stats all derive. `concepts[]` on a problem links it to learning content,
and the reverse link appears on the concept — one declaration, both directions.

---

## 7. Search (brief §16)

Two systems, per §3.7 of the reference analysis:

- **Pagefind** over rendered output for full text, scoped with `data-pagefind-body`, with
  filters emitted as `data-pagefind-filter` on **type** (concept / problem / editorial /
  project / post / resource), **domain**, and **status** — which is what makes results show
  "Title · Category · Type · description · match" as the brief asks.
- **A light JSON index** for ⌘K navigation, fetched lazily on first open, covering every
  content type — including problems and editorials, which today's index omits entirely.

Replaces the current 229 KB always-truncated-to-500-characters index.

---

## 8. Deployment and CI (brief §24)

```
push → checkout → setup-node (cache npm) → npm ci
     → npm run assets            # favicon + OG card from SVG (fixes the missing og-default.png)
     → npm run validate          # uniqueness, referential integrity, URL preservation,
     │                           # confidentiality gate, prerequisite cycles
     → npm run check             # astro check — TypeScript, strict
     → npm run build             # Zod schema validation happens here; violations fail
     → npx pagefind --site dist
     → npm run check:links       # internal link check over dist/  → fails on 404
     → upload-pages-artifact → deploy-pages
```

This is strictly stronger than the reference's CI, which skips both `astro check` and link
checking. Every one of the audit's 17 broken links and 3 permalink collisions would have been
caught here.

Also carried over unchanged: the **PlantUML → SVG workflow**, which already works well.

---

## 9. Do this first, regardless of the decision

Six defects are live on the site today and none of them should wait for a migration. They are
independent of Option A/B/C and total perhaps a day:

1. Fix the `binary-tree-level-order-traversal` permalink collision — an editorial is currently
   unreachable.
2. Delete or unpublish `index-old.md` and `master-problem-list-old.md`, which claim live URLs.
3. Add `assets/images/og-default.png`, or drop the `og_image` key — every social preview on the
   site is currently broken.
4. Add `node_modules` back to `_config.yml`'s `exclude:`.
5. Fix the 17 broken internal links.
6. Repoint `validate_site.py` and `generate_summary.py` at `_learning/`, or delete them and
   correct `CLAUDE.md`. Also correct `CLAUDE.md`'s claim that CI deploys from `main`.

If the answer to §1.4 turns out to be "not now", this list is still the right next action.

---

## 10. What this architecture delivers against the brief

| Brief | Delivered by |
|---|---|
| §6 Content drives UI | Everything in §6 derives from frontmatter; no hand-maintained index survives |
| §7 Typed schemas | §3, Zod, build fails on violation |
| §8 Domain→Track→Module→Concept | §3.3, §6.1 — data, not filenames |
| §9 Learning status | §6.3 — two layers, both optional |
| §10 Mental models | §3.5 — components, none mandatory |
| §11 Knowledge graph | §6.2 — prerequisites, related, derived backlinks, cycle detection |
| §12 Graph compilers | A `compilers` domain and a track; no schema change needed |
| §13 Confidentiality | `visibility: review` hard-fails production builds |
| §14 DSA | §6.5 — `problems.yml` preserved, 1,597 duplicated lines deleted |
| §15 Roadmaps | §6.4 — derived, `roadmaps.yml` retired |
| §16 Search | §7 — Pagefind + ⌘K, all types indexed |
| §17 UI/UX | Token layer, light+dark, KaTeX, Shiki dual-theme |
| §19 Automated UI | §6 throughout |
| §20 Design system | §4 — ~20 components |
| §21 URL compatibility | §5 — URL as data, build fails on a dropped URL |
| §22 SEO | Required `description`, generated OG cards, sitemap, 404 |
| §23 Performance | Static, zero JS by default, self-hosted fonts, no Netlify widget site-wide |
| §24 CI | §8 |

---

**Step 3 complete.** `MIGRATION_PLAN.md` follows: phases, risks, dependencies, content
mapping, URL mapping and rollback.
