---
layout: default
title: How to Add Problems & Solutions
permalink: /editorials-guide/
---

# 📖 How to Add Problems & Solutions

This guide covers the complete workflow for adding new problems, marking them solved, and attaching approaches, PDFs, code files, and external solution links.

---

## How the System Works

All problems live in **one file**: `_data/problems.yml`. Every change you make there automatically propagates to:

- **`/problems/`** — the interactive Problems Hub (searchable, filterable table)
- **`/learning/dsa/<topic>/<topic>-problems/`** — every topic page whose slug matches an entry in the problem's `topics` array

You never need to edit topic pages manually to add or update problems.

---

## Quick Checklist — Adding a New Problem

```
1. Open _data/problems.yml
2. Add a new entry block (see schema below)
3. Set topics: to the correct slug(s)
4. Save — it auto-appears everywhere
5. (Optional) Attach a solution/approach link
```

---

## `problems.yml` Schema

Each entry in `_data/problems.yml` looks like this:

```yaml
- id: '1'                          # LeetCode number, or a custom slug like 'gfg-two-sum'
  title: Two Sum                   # Exact problem title
  platform: leetcode               # leetcode | gfg | interviewbit | codeforces
  difficulty: easy                 # easy | medium | hard  (all lowercase)
  topics:                          # list of topic slugs — drives which pages show this problem
    - arrays
    - searching-sorting
  solved: false                    # true once you've solved it
  problem_url: https://leetcode.com/problems/two-sum/
  approach_url: ''                 # written notes, PDF, or external link — see below
  solution_url: ''                 # code file or external solution link — see below
```

### Field reference

| Field | Required | Notes |
|-------|----------|-------|
| `id` | Yes | LeetCode number as string (`'1'`) or custom (`'gfg-two-sum'`) |
| `title` | Yes | Displayed as the problem name everywhere |
| `platform` | Yes | Source platform |
| `difficulty` | Yes | Exactly `easy`, `medium`, or `hard` |
| `topics` | Yes | One or more slugs from the recognised list below |
| `solved` | Yes | `true` or `false` — drives the ✓ Solved badge |
| `problem_url` | Recommended | Direct link to the problem statement |
| `approach_url` | Optional | Written notes, PDF, or external editorial link |
| `solution_url` | Optional | Raw code file or external solution link |

### Recognised topic slugs

| Slug | Dedicated topic page |
|------|---------------------|
| `arrays` | `/learning/dsa/arrays/arrays-problems/` |
| `strings` | `/learning/dsa/strings/strings-problems/` |
| `linked-list` | `/learning/dsa/linked-list/linked-list-problems/` |
| `tree` | `/learning/dsa/tree/tree-problems/` |
| `stacks` | `/learning/dsa/stacks/stacks-problems/` |
| `searching-sorting` | `/learning/dsa/searching-sorting/searching-sorting-problems/` |
| `sliding-window` | No page — filters the hub table only |
| `two-pointers` | No page — filters the hub table only |

A problem can have **multiple topics**. It will appear on every matching topic page.

---

## Attaching Solutions & Approaches

The Problems Hub generates buttons automatically based on what you put in `approach_url` and `solution_url`. The button label and colour are detected from the link type.

### Option 1 — Written Editorial (Markdown)

Best for: written explanations, complexity analysis, diagrams, embedded code.

**Step 1.** Create a file in `_editorials/`:

```
_editorials/two-sum-approach.md
```

**Step 2.** Add front matter:

```yaml
---
layout: editorial
title: "Two Sum — Approach"
problem_id: "1"
date: 2025-02-28T12:00:00.000Z
---
```

**Step 3.** Write your explanation in Markdown below the front matter.

**Step 4.** In `_data/problems.yml`, set:

```yaml
approach_url: '/editorials/two-sum-approach/'
```

The hub renders a **📖 Editorial** button.

---

### Option 2 — Handwritten PDF Notes

Best for: scanned notebook pages, visual diagrams, hand-drawn trees/graphs.

**Step 1.** Place the PDF in the relevant topic directory:

```
_learning/dsa/Arrays/two-sum-notes.pdf
```

**Step 2.** In `_data/problems.yml`, set (path is case-sensitive):

```yaml
approach_url: '/learning/dsa/Arrays/two-sum-notes.pdf'
```

The hub renders a **📝 PDF Notes** button.

> **Note:** GitHub Pages paths are case-sensitive. `/Arrays/` and `/arrays/` are different URLs.

---

### Option 3 — Raw Code File (`.cpp`, `.py`, `.java`, etc.)

Best for: saving your solution code alongside the problem notes.

**Step 1.** Save your code file in the topic directory:

```
_learning/dsa/Arrays/solution-two-sum.cpp
```

**Step 2.** In `_data/problems.yml`, set:

```yaml
solution_url: '/learning/dsa/Arrays/solution-two-sum.cpp'
```

The hub renders a **💻 Raw Code** button.

---

### Option 4 — External LeetCode Solution Link

Best for: linking to a well-upvoted community solution or your own published solution.

Copy the full URL of the solution post and set it in `problems.yml`:

```yaml
solution_url: 'https://leetcode.com/problems/two-sum/solutions/123456/my-solution/'
```

The hub detects the `leetcode.com` domain and renders a **🔗 Solution** button.

Use `approach_url` for editorial/theory links, `solution_url` for code-focused links.

---

### Option 5 — Decap CMS (Netlify Admin UI)

If you prefer a GUI instead of editing YAML directly:

1. Go to `ajdevhub.netlify.app/admin` and log in.
2. Click **DSA Editorials** → **New DSA Editorial**, write your Markdown, and publish.
3. Go to **Data Files → DSA Problems Database**, find the problem, and paste the slug into `approach_url`.

---

## Rules for `approach_url` vs `solution_url`

| Scenario | Use |
|----------|-----|
| One link covering both explanation and code | `approach_url` only — leave `solution_url` empty |
| Separate editorial + separate code | Both fields |
| Only raw code, no explanation | `solution_url` only |
| Only a LeetCode solution post | Heavy theory → `approach_url`, mostly code → `solution_url` |

> **Never point to GitHub blob URLs.** Use Jekyll-relative paths (`/editorials/...`, `/learning/...`) for internal files.

---

## Marking a Problem as Solved

Simply change `solved: false` to `solved: true` in `_data/problems.yml`:

```yaml
solved: true
```

The ✓ Solved badge updates on both the Problems Hub and the topic page automatically.

---

## Complete Example

A fully-filled entry with a PDF note:

```yaml
- id: '875'
  title: Koko Eating Bananas
  platform: leetcode
  difficulty: medium
  topics:
    - searching-sorting
    - arrays
  solved: true
  problem_url: https://leetcode.com/problems/koko-eating-bananas/
  approach_url: '/learning/dsa/Searching-Sorting/koko-banana.pdf'
  solution_url: ''
```

---

## Adding a New Topic Page

If you want a dedicated problems page for a new topic (e.g., `graphs`):

**Step 1.** Create `_learning/dsa/graphs/graphs-problems.md` using this template:

```liquid
---
layout: default
title: Graphs - Practice Problems
permalink: /learning/dsa/graphs/graphs-problems/
---

{% raw %}{% assign topic_slug = "graphs" %}
{% assign topic_back_url = "/learning/dsa/graphs/" %}
{% assign topic_all    = site.data.problems.problems | where_exp: "p", "p.topics contains topic_slug" %}
{% assign topic_solved = topic_all | where: "solved", true %}
{% assign topic_easy   = topic_all | where: "difficulty", "easy" %}
{% assign topic_medium = topic_all | where: "difficulty", "medium" %}
{% assign topic_hard   = topic_all | where: "difficulty", "hard" %}{% endraw %}
```

Copy the full structure from any existing topic page such as
`_learning/dsa/Strings/strings-problems.md` and update only the three
`topic_slug`, `topic_back_url`, and heading values.

**Step 2.** Register the page in `assets/js/problems.js` inside `topicPages`:

```javascript
const topicPages = {
    // existing entries...
    'graphs': '/learning/dsa/graphs/graphs-problems/',
};
```

**Step 3.** Add a chip in `problems.md` inside the `topic-chips` div:

```html
<a href="{{ '/learning/dsa/graphs/graphs-problems/' | relative_url }}" class="topic-chip">🕸️ Graphs</a>
```

**Step 4.** Add problems with `topics: [graphs]` in `_data/problems.yml` and they appear instantly.

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Problem not on topic page | Wrong slug in `topics:` | Slug must exactly match — `linked-list` not `linked_list` |
| Problem not in hub | YAML syntax error | Check 2-space indentation, no tabs |
| PDF/code link 404 | Path case mismatch | `/Arrays/` ≠ `/arrays/` — match exactly |
| Two identical buttons | Same URL in both fields | Put it in one field only |
| Topic page shows 0 problems | `topic_slug` mismatch | Ensure the slug in the page matches the slug used in `problems.yml` |
| Stale page after changes | `_site` cache | Run `rm -rf _site .jekyll-cache && bundle exec jekyll serve --livereload` |
