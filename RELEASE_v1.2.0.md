# 🎉 Release v1.2.0: Problem System Unification & Site Hardening

This release unifies the problem-tracking infrastructure across all DSA topic pages, redesigns the problem card system, fixes long-standing UI bugs, and delivers a full documentation refresh.

---

### 🚀 Major Features & Updates

#### 1. Unified Problem Card System

- **Canonical `_includes/problem-card.html` component:** Replaced all per-topic hardcoded HTML cards with a single reusable Liquid include. Every topic page now renders identical, consistent cards driven directly from `_data/problems.yml`.
- **New `.pc-card` CSS system:** Introduced `.pc-card`, `.pc-card--easy/medium/hard`, `.pc-status`, `.pc-diff`, `.pc-btn`, `.pc-grid` classes in `main.css`. Cards use CSS custom properties for seamless dark/light mode compatibility — no more visibility issues in dark theme.
- **Single source of truth:** `_data/problems.yml` now drives both the Interactive Problems Hub (`/problems/`) and all six dedicated topic pages simultaneously. Adding one YAML entry propagates everywhere automatically.

#### 2. Liquid-Powered Topic Pages (All 6)

Replaced all old hardcoded HTML problem lists with clean Liquid templates using Jekyll's `where_exp` filter:

- `/learning/dsa/arrays/arrays-problems/`
- `/learning/dsa/strings/strings-problems/`
- `/learning/dsa/linked-list/linked-list-problems/`
- `/learning/dsa/tree/tree-problems/`
- `/learning/dsa/stacks/stacks-problems/`
- `/learning/dsa/searching-sorting/searching-sorting-problems/`

Each page shows live stats (Total / Solved / Easy / Medium / Hard) and groups problems by difficulty using the canonical card component.

#### 3. Cross-Navigation & UX

- **Topic chips row** on the Problems Hub for one-click jumps to dedicated topic pages.
- **Topic page banner** in the hub: when filtering by a topic that has a dedicated page, a banner appears linking directly to it.
- **Clickable topic tags** in the hub table: tags with dedicated pages link to them; tags without pages trigger an inline filter.
- **Back-to-top link** on long problem lists.
- **Cross-links** on every topic page: All Problems Hub ↔ Back to Topic ↔ DSA Hub.

#### 4. Dark Mode Fix

- Added synchronous `<script>` in `<head>` to apply the saved theme before first paint — eliminates flash of unstyled content (FOUC).
- Extracted theme toggle into an isolated IIFE at end of `<body>`, fully decoupled from `SimpleJekyllSearch`'s `DOMContentLoaded` handler which was silently blocking the click listener on error.

#### 5. DSA Hub Card Redesign

- Reduced padding and font sizes; switched to horizontal flex layout.
- Stats row changed from grid to flex for a more compact, readable presentation.

#### 6. Repository Cleanup

- **Removed `arrays_backup/`**: Confirmed identical duplicate of `_learning/dsa/Arrays/` — deleted entirely with zero data loss.
- **Suppressed `sorting/` stubs**: All five stub pages (`index`, `mergesort`, `quicksort`, `heapsort`, `counting-radix-bucket`) marked `published: false`. Their content was already fully covered by `Searching-Sorting/sorting-guide.md`.
- **Fixed dead link** in DSA hub: `master-problem-list/` (non-existent) replaced with the live `/problems/` hub.
- **Resolved permalink conflict**: `arrays_backup/` was serving the same URL as `Arrays/arrays-problems.md`, causing Jekyll to overwrite the new page with the old backup on every build. Fixed by suppressing the backup before deletion.

#### 7. Problems Data Updates

- **Added LeetCode 88** (Merge Sorted Array — easy, `searching-sorting` + `arrays` + `two-pointers`, solved) which was present in `sorting-guide.md` but missing from `problems.yml`.
- **Filled solution URLs** for problems 148 (Sort List), 179 (Largest Number), and 75 (Sort Colors) — all had published LeetCode solutions but empty `solution_url` fields.

#### 8. Documentation Refresh

- **README.md** — complete rewrite aligned to the current codebase: accurate quick-start, Problems system data-flow diagram, topic slug reference, DSA topic page template, updated file map, deploy workflow, and common mistakes table.
- **EDITORIALS_GUIDE.md** — expanded from a short CMS reference into a full developer guide covering: `problems.yml` schema, all 5 solution attachment options (editorial MD, PDF, raw code, LeetCode link, CMS UI), `approach_url` vs `solution_url` rules, step-by-step new topic page creation, and a troubleshooting table.

---

*Compiled on: February 28, 2026*
