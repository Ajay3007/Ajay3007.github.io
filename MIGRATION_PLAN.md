# MIGRATION_PLAN.md

**Ajdevhub — Step 4: staged migration plan.**

Written 2026-08-16. Companion to `CURRENT_ARCHITECTURE.md`, `REFERENCE_ARCHITECTURE.md`,
`PROPOSED_ARCHITECTURE.md` and the machine-readable `MIGRATION_INVENTORY.csv` (436 rows).

**Nothing in the production site has been changed. This plan is for review.**

---

## 1. Governing principles

1. **The live site never breaks.** Jekyll keeps serving `ajay3007.github.io` until the Astro
   build reaches parity and you approve the cutover. There is no window where the site is half
   migrated in public.
2. **No content is deleted.** Everything obsolete is marked for review in the inventory and
   decided by you, not by me.
3. **No URL is lost.** Enforced by CI, not by care — see §4.
4. **Migrate first, beautify second.** Legacy pages move as `.md` with their existing HTML
   intact and working. Conversion to components is a separate, incremental backlog.
5. **Small commits.** One phase produces several logical commits, never one large one.

---

## 2. Content mapping

Full detail: `MIGRATION_INVENTORY.csv` — every content item with old path, type, title, current
URL, destination, new URL, status and notes. Summary:

| Status | Count | Meaning |
|---|---:|---|
| `MIGRATE` | 302 | Moves as-is into a typed collection. URL unchanged |
| `REVIEW` | 73 | Needs your decision before it moves |
| `RETIRE` | 27 | Source file goes away; **the URL stays** and is now generated |
| `KEEP` | 18 | Repo docs, not published, unaffected |
| `CONVERT` | 9 | Roadmaps → track records + derived views |
| `REWRITE` | 6 | Hand-coded site pages rebuilt as derived pages |
| `FIX` | 1 | The unreachable editorial |

### 2.1 The 27 `RETIRE` items are deletions of *duplication*, not content

- **18 DSA topic pages** (`*-problems.md`, 1,597 lines) → one `/problems/[topic]/` route. The
  pages are near-identical; a normalised diff between any two is 6 lines. All 18 URLs keep
  working.
- **8 blog category pages** → derived from post tags. These also still carry pre-redesign
  light-theme inline styles, so retiring them fixes a visual bug at the same time.
- **`_data/roadmaps.yml`** → derived from tracks + modules + concepts, which removes the
  hardcoded `"100+ curated problems"` that already disagrees with the real 164.

### 2.2 The 73 `REVIEW` items — your decisions

| Group | Count | Decision needed |
|---|---:|---|
| Section `index.md` pages | 64 | Most content is derivable (child lists, counts). Keep the bespoke prose, drop the hand-maintained link lists. Per-page, quick |
| Legacy `-old` duplicates | 2 | **Verified: the current file wins both collisions today**, so deleting the `-old` files loses nothing that is live |
| `published: false` sorting pages | 5 (4 rows) | Duplicate `Searching-Sorting/`. Merge or drop |
| `COPILOT_RULES.md` | 1 | Internal doc currently public at `/learning/COPILOT_RULES/`. Recommend de-publishing |
| PDFs (15, 30.6 MB) | 1 row | Keep / compress / drop. Largest single content weight |
| `.exe` binaries (17, 2.7 MB) | 1 row | Recommend removing — Windows binaries in a public repo |

### 2.3 The conversion backlog

**81 pages are flagged HTML-heavy** (>200 presentational tags). They migrate as working `.md`
in Phase 5 and convert to MDX components afterwards, at whatever pace suits you. **35 stubs**
are flagged so they can be given an honest `status:` rather than looking finished.

---

## 3. Phases

Sizing is relative, not calendar-based: **S** ≈ one sitting, **M** ≈ a few, **L** ≈ sustained
work over weeks. Phases 1–4 are independent of the Astro decision.

| # | Phase | Size | Gate to pass |
|---|---|---|---|
| 0 | Audit | ✅ done | The four documents |
| 1 | **Fix the live site** | S | Bugs closed on the current Jekyll site |
| 2 | Astro foundation | M | Empty site builds and deploys to a preview URL |
| 3 | Schemas + validation | M | `npm run validate` green on real content |
| 4 | Component library | M | ~20 components, rendered on a demo page |
| 5 | Bulk content migration | L | All 407 URLs resolve in the preview build |
| 6 | Learning system | M | Tracks, modules, prev/next, prerequisites, backlinks |
| 7 | DSA system | S | 164 problems, dynamic topic route, editorial integrity check |
| 8 | Roadmaps | S | `roadmaps.yml` retired, counts derived |
| 9 | Remaining content | S | Posts, projects, about, resources |
| 10 | Search, SEO, performance | M | Pagefind, OG cards, 404, sitemap, Lighthouse pass |
| 11 | **Cutover** | S | Parity checklist signed off |
| 12 | Visual redesign + MDX conversion | L | Ongoing, post-cutover |

### Phase 1 — Fix the live site *(do this whether or not you approve the migration)*

Six defects, all live now, none dependent on the migration:

1. Fix the `binary-tree-level-order-traversal` permalink collision — an editorial is
   unreachable today.
2. Remove or unpublish `index-old.md` and `master-problem-list-old.md`.
3. Add `assets/images/og-default.png` or drop `og_image` — every social preview is broken.
4. Re-add `node_modules` to `_config.yml` `exclude:`; add `CURRENT_ARCHITECTURE.md`,
   `REFERENCE_ARCHITECTURE.md`, `PROPOSED_ARCHITECTURE.md`, `MIGRATION_PLAN.md` and
   `AUDIT_URL_INVENTORY.txt` / `MIGRATION_INVENTORY.csv` too — they are currently publishable.
5. Fix the 17 broken internal links.
6. Repoint or delete `validate_site.py` / `generate_summary.py`; correct `CLAUDE.md`'s
   `main`-vs-`master` claim.

Commits: `fix: recover unreachable level-order editorial` · `fix: remove colliding legacy dsa
pages` · `fix: add missing default OG image` · `chore: repair jekyll exclude list` ·
`fix: repair 17 broken internal links` · `chore: repoint maintenance scripts at _learning`

### Phase 2 — Astro foundation

Astro 7 + TS strict + Tailwind 4 in the **same repository**, on a `migration/astro` branch,
building to `dist/`. A second workflow deploys that branch to a **preview environment** so you
can see it without touching production. Self-hosted variable fonts. `consts.ts` with `DOMAINS`.

Commits: `chore: add astro foundation` · `chore: preview deployment workflow` ·
`feat: design token layer` · `feat: base layout and site shell`

### Phase 3 — Schemas and validation

`content.config.ts` per `PROPOSED_ARCHITECTURE.md` §3, plus `scripts/validate-content.mjs`:
URL uniqueness, URL-preservation check against `AUDIT_URL_INVENTORY.txt`, prerequisite/related
resolution, prerequisite cycle detection, editorial↔problem integrity, `visibility: review`
gate. Wire into CI before any bulk content moves, so the migration is checked as it happens.

### Phase 4 — Component library

The ~20 components in §4 of the proposal, injected from routes. Includes ports of
`problem-card.html` and the URL-derived breadcrumbs — both already good.

### Phase 5 — Bulk content migration *(the big one)*

Scripted, not manual. A migration script reads each file, maps front matter to the new schema,
sets `url:` to the **current** permalink, infers `domain` from the path, and infers
`track`/`module`/`order` from the three filename-prefix conventions (`p4-m13-`, `module-b9-`,
`m17-`, `ch5-`) where they exist. Files move as `.md`; embedded HTML keeps working untouched.

What the script **cannot** infer, and you supply: `status`, `prerequisites`, `related`,
`description` for the 354 pages that lack one. Suggest doing this domain by domain rather than
all at once — it is the genuine intellectual work of the migration and it is what unlocks
§6–§11 of the brief.

Gate: **all 407 URLs resolve in the preview build.** CI-enforced.

### Phases 6–10

As tabled. Phase 7 deletes 1,597 lines of duplicated Liquid. Phase 8 deletes `roadmaps.yml`.
Phase 10 adds Pagefind, generated OG cards, a 404 page, and the filtered search UI.

### Phase 11 — Cutover

Parity checklist: all 407 URLs resolve · sitemap clean · feed valid · search covers all types ·
mobile checked at 375/768/1280 · Lighthouse ≥ 90 on four representative pages · Decap CMS
working against the new collections. Then switch the production workflow to build Astro from
`master`. Tag the last Jekyll commit `jekyll-final` first.

### Phase 12 — Ongoing

The 81 HTML-heavy pages convert to MDX components at your pace. The site is live and correct
throughout; each conversion is independently revertible.

---

## 4. URL mapping and the preservation guarantee

Derived from all 407 live URLs (`AUDIT_URL_INVENTORY.txt`) against the inventory:

| | Count |
|---|---:|
| **URLs preserved unchanged** | **401** |
| URLs changed (with redirect) | 1 |
| Source files retired whose URL is now generated | included in the 401 |
| Currently-live URLs lost | **0** |

The one change is a **fix**, and it adds a page rather than removing one:

```
/editorials/balanced-binary-tree/   → keeps serving balanced-binary-tree (correct owner)
/editorials/binary-tree-level-order-traversal/   → NEW, restores the currently-lost editorial
```

Eight rows show no new URL. None is a live page:

- 5 × `_learning/dsa/sorting/*` — already `published: false`, never rendered.
- 2 × `-old` duplicates — **verified** against the built site: `index.md` and
  `master-problem-list.md` win both collisions today, so the URLs stay with their correct
  owners.
- 1 × `COPILOT_RULES.md` — an internal document, intentionally de-published. Add a redirect
  only if it turns out to have inbound links.

**Enforcement, not intention:** `scripts/validate-content.mjs` reads
`AUDIT_URL_INVENTORY.txt` and fails the build if any listed URL stops resolving. A dropped URL
becomes a red CI run, not a silent regression discovered months later in Search Console.

Redirects use statically generated meta-refresh + `<link rel="canonical">` stubs, since GitHub
Pages has no server-side redirect support.

---

## 5. Risks

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 1 | **Metadata backfill stalls.** `status`, `prerequisites`, `related` and 354 descriptions cannot be automated — this is authoring, and it is where the project can quietly die | High | High | All fields optional in the schema. The site works fully with none of them; each one added lights up more derived UI. Do it domain by domain, never as one blocking task |
| 2 | **MDX conversion never finishes.** 81 HTML-heavy pages | High | Low | Structurally de-risked: legacy stays `.md` and renders correctly forever. Conversion is optional polish, not a blocker |
| 3 | **A URL is silently dropped** | Medium | High | CI check against the 407-URL inventory (§4) |
| 4 | **Astro/Node learning curve** | Medium | Medium | Phases 2–4 are small and reversible. If it isn't working by end of Phase 4, abandon with only a branch discarded — production untouched |
| 5 | **Decap CMS breaks** | Medium | Medium | Reconfigure in Phase 9 and verify in the Phase 11 checklist. Decap is git-based, not Jekyll-specific. Fallback: edit files directly |
| 6 | **Filename-prefix inference is wrong** for `track`/`module`/`order` | Medium | Low | Script emits a report for review; wrong `order` is a cosmetic sort issue, trivially fixed |
| 7 | **Jekyll collision resolution is not contractual.** Today the correct file wins both `-old` collisions, but that depends on build ordering | Low | High | Phase 1 removes the collisions entirely, before anything else happens |
| 8 | **Confidential material reaches the public repo** as the compiler track grows | Low | Severe | `visibility: review` hard-fails production builds; any uncertain page is flagged, never published |
| 9 | **Scope creep into redesign during migration** | High | Medium | Phase 12 exists precisely to hold it. Phases 5–10 preserve appearance; they do not improve it |
| 10 | **Repo weight** (30.6 MB PDFs, 106 MB `.git`) slows CI | Low | Low | Phase 1 review decision; not on the critical path |

---

## 6. Dependencies

```
Phase 1  (independent — do now)
   │
Phase 2 ── Phase 3 ── Phase 4
                │        │
                └──── Phase 5 ────┬── Phase 6 ── Phase 8
                                  ├── Phase 7
                                  └── Phase 9
                                        │
                                     Phase 10 ── Phase 11 ── Phase 12
```

Hard ordering: 3 before 5 (validation must exist before bulk moves), 5 before 6/7/9,
everything before 11. Phases 6, 7 and 9 are parallelisable. Phase 8 needs 6.

---

## 7. Rollback

| Point of failure | Rollback | Cost |
|---|---|---|
| Any of Phases 2–10 | Delete the `migration/astro` branch. Production is Jekyll on `master` and was never touched | Zero |
| Phase 11, immediately after cutover | Revert the workflow commit; `master` still contains every Jekyll file | One commit, ~5 minutes |
| Phase 11, discovered later | `git checkout jekyll-final -- .` — the tag pins the last known-good Jekyll tree | One commit |
| A single Phase 12 conversion | Revert that commit; conversions are one page each | One commit |

The Jekyll site is **not deleted at cutover.** `_layouts/`, `_includes/`, `_config.yml` and the
`_*` collection folders stay in the repository, unbuilt, until you are satisfied — proposed at
one full release cycle. Removing them is a separate, deliberate commit.

---

## 8. Commit sequence

```
Phase 1   fix: recover unreachable level-order editorial
          fix: remove colliding legacy dsa pages
          fix: add missing default OG image
          chore: repair jekyll exclude list
          fix: repair 17 broken internal links
          chore: repoint maintenance scripts at _learning

Phase 2   chore: add astro foundation
          chore: preview deployment workflow
          feat: design token layer
          feat: base layout and site shell

Phase 3   feat: content schemas with zod validation
          feat: content validation script
          chore: wire validation into CI

Phase 4   feat: core ui components
          feat: mdx content components
          feat: concept section components

Phase 5   chore: content migration script
          feat: migrate dsa content          (one commit per domain — 12 commits)
          feat: migrate system-design content
          …
          test: url preservation check passes for all 407 urls

Phase 6   feat: track/module/concept hierarchy
          feat: prerequisites, related and backlinks
          feat: two-layer progress system

Phase 7   feat: migrate problems database
          feat: dynamic problems topic route
          refactor: remove 18 duplicated topic pages

Phase 8   feat: derive roadmaps from tracks
          refactor: retire _data/roadmaps.yml

Phase 9   feat: migrate posts, projects and pages
          feat: resources collection

Phase 10  feat: pagefind search with filters
          feat: generated og cards and favicons
          feat: 404 page and sitemap hygiene
          perf: font preloading and asset budget

Phase 11  chore: tag jekyll-final
          chore: cut production deploy over to astro

Phase 12  refactor: convert <domain> pages to mdx components   (ongoing)
```

---

## 9. Open questions for you

These change the plan materially and I have not assumed answers:

1. **Approve Option B (Astro)?** If you would rather do Option A, Phases 1, 3, 4 and 10 still
   apply in modified form and I will rewrite the plan around Jekyll.
2. **Domain taxonomy.** `PROPOSED_ARCHITECTURE.md` §3.1 proposes 11 domains, which regroups
   today's 12 folders (e.g. `4g-5g` folding under `networking`, a new `compilers`). Right?
3. **The 30.6 MB of PDFs and 17 `.exe` binaries** — keep, compress, or drop?
4. **`COPILOT_RULES.md`** — de-publish it?
5. **Decap CMS** — still using it? If not, Phase 9 gets simpler.
6. **The `finance/tax_hurdle` content** — learning material, or project documentation that
   belongs under `/projects/tax_hurdle/`?

---

## 10. Where this leaves the brief's quality bar

> *"I should be able to learn a new technical concept and add one well-structured content file,
> and the website should automatically integrate that concept."*

After Phase 6, adding `src/content/concepts/compilers/operator-fusion.md` with

```yaml
title: Operator Fusion
description: Merging adjacent graph operators to cut memory traffic.
domain: compilers
track: graph-compilers
module: graph-optimisation
order: 4
status: learning
prerequisites: [computational-graph, graph-ir]
related: [memory-planning, kernel-scheduling]
```

automatically produces: the domain index entry, the track tree position, breadcrumbs,
prev/next, a resolved prerequisite list, backlinks on both related concepts, the roadmap stage
entry with its status chip, a full-text search entry with type/domain/status filters, a ⌘K
entry, a sitemap entry, and page metadata — **with no other file edited.**

---

**Steps 1–4 complete. Stopping here for your review, as the brief specifies.** Nothing in the
production site has been modified. The four documents plus `AUDIT_URL_INVENTORY.txt` and
`MIGRATION_INVENTORY.csv` are uncommitted in the working tree.
