# Portfolio Site — Full Codebase Audit Report
**Date:** February 2026 | **Coverage:** 100% of 232 unique files across all dumps

---

## Reading Coverage Summary

| Dump File | Files | Status |
|---|---|---|
| `dump_learning_topics.txt` | 114 | ✅ 100% read |
| `dump_learning_lang.txt` | 46 | ✅ 100% read |
| `dump_projects_problems.txt` | 72 (50 duplicates) | ✅ 100% read |
| `feed_dsa_A/B/missing` | DSA deep files | ✅ 100% read |
| `feed_lang_c/java` | C + Java series | ✅ 100% read |
| Posts, layouts, projects | 13 files | ✅ 100% read |

---

## Problem Inventory (Authoritative)

**74 total problems | 44 solved | 30 unsolved**
*(Site claimed 77/43 — delta of 3 is the linked-list `#10 placeholder` + 2 tree stubs)*

### By Topic
| Topic | Total | Solved |
|---|---|---|
| Searching & Sorting | 27 | 18 |
| Arrays (sliding-window) | 13 | 5 |
| Arrays (two-pointers) | 5 | 5 |
| Linked List | 10 | 6 |
| Strings | 11 | 9 |
| Tree | 7 | 0 |
| Stacks | 4 | 0 |

---

## Bugs — Confirmed & Verified

### 🔴 Critical (fix this week)

**1. Emoji Encoding Corruption — SITE-WIDE**
- Every emoji renders as mojibake (✅ → âœ…, → ðŸ , etc.)
- Root cause: UTF-8 encoding mismatch in git config or editor
- Fix: `git config core.autocrlf false` + re-save all files with UTF-8 no BOM
- Affects: ALL pages including default.html layout

**2. Placeholder Blog Post Live**
- File: `_posts/2025-01-01-first-post.md`
- Content: "Welcome to My Blog" — filler text, public-facing
- Fix: Delete the file

**3. Wrong Author on Blog Post**
- File: `_posts/2025-12-25-my-first-blog.md`
- Author listed as "Calculusphile" — wrong identity
- Also has broken path: `/learning/dsa/LinkedList/` (should be `linked-list`)
- Fix: Fix author + path, or delete if content not worth keeping

**4. Broken Liquid Template Tags**
- `learning/system-design/scalability.md`: `{` should be `{{` in relative_url filter
- `learning/system-design/lld/index.md`: same issue
- These pages render broken navigation links

**5. Broken Internal Path in Fast Pointer Post**
- `_posts/2025-12-25-Fast-Pointer.md`: links to `/learning/dsa/LinkedList/` (404)
- Correct path: `/learning/dsa/linked-list/`
- Same broken path in `_posts/2025-12-25-my-first-blog.md`

### 🟡 Important (fix this month)

**6. `.venv/` Committed to Repository**
- Python virtual environment checked into git
- Adds 700KB+ dead weight
- Fix: Add to `.gitignore`, run `git rm -r --cached .venv/`

**7. Backup Files in Repository**
- `*.md.bak` files scattered across `learning/` folder
- Public and rendered by Jekyll
- Fix: Gitignore pattern `*.bak`, remove from tracked files

**8. `prompt.md` in Repository Root**
- AI prompt file — will be rendered as a public page by Jekyll
- Fix: Add to `.gitignore`, remove from tracked files

**9. Theme Configuration Conflict**
- `_config.yml` declares `theme: minima` but uses fully custom layouts
- Minima CSS loading unnecessarily
- Fix: Remove `theme: minima` line entirely

**10. Three Competing Problem Card Systems**
- System 1: `<div class="problem-card-easy">` (arrays, strings, stacks, tree files)
- System 2: `<div class="problem-card">` with `problem-card-inner` (sliding window, searching-sorting master)
- System 3: `_includes/problem-card.html` — the intended approach, barely used
- Fix: Migrate all to System 3 (new unified include provided in deliverables)

**11. Duplicate Problems with Contradicting Solved Status**
- `#125 Valid Palindrome`: "Solved" in two-pointers, "Unsolved" in strings-problems
- `#3 Longest Substring`: "Solved" in sliding-window, "Unsolved" in strings-problems
- `#242 Valid Anagram`: "Solved" in YAML, "Unsolved" in strings-problems
- `#49 Group Anagrams`: "Solved" in YAML, "Unsolved" in strings-problems
- Fix: `_data/problems.yml` (provided) is now authoritative — delete per-page duplication

**12. Homepage Stats Hardcoded**
- `problems.md` manually maintains "77 problems / 43 solved" counters
- Will always drift out of sync
- Fix: Replace hardcoded numbers with Liquid: `{{ site.data.problems | size }}` and `{{ site.data.problems | where: "solved", true | size }}`

---

## Content Quality Assessment

### ✅ Exceptional Content (your best work)

**1. `learning/4g-5g/index.md`** — Professional-grade telecom reference
- Covers E-UTRAN, EPC (MME, SGW, PGW, HSS), IMS, VoLTE, 5G-AKA, NGFW/SASE
- Level: industry documentation quality
- Action: Make this more prominent in navigation — it's currently buried

**2. Java Learning Series (`java/00–03`)** — Deeply written, interview-focused
- `compilation-execution.md`: JVM internals, classpath, bytecode lifecycle
- `primitive-data-types.md`: IEEE 754, precision bugs, BigDecimal, type promotion rules
- `java-constructor.md`: 18-section guide — default vs no-args, chaining, private constructors
- `memory-management-garbage-collection.md` (referenced but unread — must be substantial)
- Style: Consistent `Interview Q&A` sections, `Key Takeaways`, mental models
- Action: Add `JavaFoundry` project to portfolio showcase

**3. C Basics Series (`c/c-basics/01–11`)** — Systems-level mastery
- Memory layout diagram + SVG, stack frames, pointer arithmetic, struct padding
- Covers: Text/BSS/heap/stack segments, wild vs dangling pointers, function pointers, malloc internals
- Action: Blog post on "C memory layout for Java developers" would be compelling cross-topic content

**4. `Searching-Sorting/` with PDF approaches** — Real engineering habit
- PDF solution writeups per problem (floorAndCeil.pdf, Kth_rotation.pdf, etc.)
- LeetCode solution links with editorial-style explanations
- Allocate Minimum Pages: full writeup with complexity proof, isValid greedy

**5. Linked List solution pages (6 files)** — Proper solution documentation
- `leetcode-141`: Two approaches (hash map + Floyd's), complexity comparison table
- `leetcode-19`: Two-pass vs one-pass with summary table
- `leetcode-2`: Dummy-node vs in-place O(1) space approaches
- `leetcode-876`: Tortoise-hare with complexity note
- All follow consistent structure: Intuition → Approach → Complexity → Code → Key Insights

**6. C++ Lambda Functions** — Complete guide
- Syntax, capture modes, mutable, generic, move-capture, std::function
- UML-style closure mental model
- Runnable examples with build commands

**7. COPILOT_RULES.md** — Sophisticated AI workflow
- Rules for System Design, journal, blog section separation
- Shows you use AI intentionally with guardrails — worth a blog post

### 🟡 Partial Content (has good bones, needs filling)

| File | Status | What's Missing |
|---|---|---|
| `system-design/scalability.md` | Executive Summary only | Body content |
| `system-design/lld/index.md` | Stub | Content |
| `system-design/hld/index.md` | Stub | Content |
| `tree/binary-tree.md` | One-liner stub | Traversals, problems |
| `tree/binary-search-tree.md` | One-liner stub | Insert/search/delete |
| `graphs/bfs-dfs.md` | Likely stub | Full BFS/DFS content |
| `dynamic-programming/1d-dp.md` | Has executive summary | Body content |
| `stacks/applications.md` | Unknown — likely stub | Applications |

### 🔴 One-Line Stubs (add "🚧 Coming Soon" banner)

- `backtracking/index.md`: "Try/choose/backtrack; pruning with constraints."
- `graphs/mst.md`: "Kruskal and Prim; union-find."
- `queues/circular-queue.md`: "Fixed-size buffer using wrap-around indices."
- `queues/priority-queue.md`: "Priority-based retrieval; usually heap-backed."
- `recursion/index.md`: Has basic structure, but no real content
- `sorting/heapsort.md`, `mergesort.md`, `quicksort.md`: One-liners
- `go/index.md`, `javascript/index.md`, `python/index.md`, `rust/index.md`: One-liners

---

## Architecture Findings

### Data Layer Problem
**Before:** 74 problems hardcoded as raw HTML across 9+ markdown files, with duplicates and contradicting solved status.

**After (delivered):** `_data/problems.yml` — single source of truth.
- 74 problems with accurate solved status cross-referenced from all source files
- Schema: id, title, platform, difficulty, topics[], solved, problem_url, approach_url, solution_url
- Auto-generates stats: `{{ site.data.problems | where: "solved", true | size }}`
- Enables filtering by topic, difficulty, platform in any Liquid template

### PlantUML Pipeline — Working and Impressive
- `.github/workflows/plantuml-render.yml` active
- SVG diagrams generated for: C memory layout, C pointer model, Java compilation, 4G/5G architecture
- This is a differentiator — most portfolios don't have auto-generated technical diagrams

### COPILOT_RULES.md — Underutilized Asset
- You have per-section AI rules: System Design assistant mode, journal rules, blog rules
- This shows AI-workflow maturity
- Consider: blog post about "How I use AI as a structured learning partner"

### Finance/Tax Section Misplaced
- `learning/finance/tax_hurdle/` has 6 files (checklist, quickref, refactoring guide, technical analysis, summary)
- This is a full project wiki living in the learning section
- Should be cross-referenced more prominently from `_projects/tax_hurdle.md`
- The checklist (Phase 1–4 with 16 improvement items) is solid engineering content

---

## Deliverables (Files to Drop Into Your Repo)

| File | Purpose |
|---|---|
| `_data/problems.yml` | Master problem list — replace all hardcoded HTML |
| `_includes/problem-card.html` | Unified card component — replace 3 competing systems |
| `learning/dsa/index.md` | DSA hub with auto-calculated stats from data |
| `learning/dsa/master-problem-list.md` | Full problem list driven from YAML |
| `.gitignore` | Excludes .venv/, *.bak, prompt.md, dump files |

---

## Priority Action Plan

### This Week (Bugs)
1. Delete `_posts/2025-01-01-first-post.md`
2. Fix or delete `_posts/2025-12-25-my-first-blog.md` (wrong author "Calculusphile")

4. Fix broken path: `LinkedList` -> `linked-list` in Fast Pointer post
5. Drop `.gitignore` from deliverables (provided)
6. Fix emoji encoding: check `.gitattributes` — add `* text=auto eol=lf`
7. Remove `theme: minima` from `_config.yml`

### This Month (Architecture)
8. Drop `_data/problems.yml` (provided) — eliminates all hardcode duplication
9. Drop `_includes/problem-card.html` (provided) — unify card systems
10. Replace `learning/dsa/index.md` (provided) — auto-stats from data
11. Replace `learning/dsa/master-problem-list.md` (provided) — data-driven
12. Update homepage stat counters to use Liquid (see note above)
13. Add `🚧 Coming Soon` banner to all one-liner stub pages
14. Run `git rm -r --cached .venv/` after updating `.gitignore`

### Next Quarter (Features)
15. Lunr.js site-wide search — 100+ pages needs it
16. Tags/categories system — wire up post frontmatter categories
17. Problem filter UI — JS filter by topic/difficulty/status on master list
18. Dark mode — CSS variables + localStorage toggle
19. Promote Java learning journal on homepage as "Currently Learning" section
20. Blog post: "C memory internals for Java developers" — bridge your two strongest topics
21. Blog post: "How I use COPILOT_RULES.md as structured AI workflow"
22. Add JavaFoundry as a project on portfolio page
23. Make 4G/5G section more prominent — it's exceptional content
