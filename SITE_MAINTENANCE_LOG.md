# Site Maintenance Log & Fix Guide

Last Updated: 2025-12-28

**Changelog**

- 2025-12-28:
  - Emoji/mojibake repair across learning/* via `ftfy` script
  - External links converted to open in new tabs (`{:target="_blank" rel="noopener noreferrer"}`)
  - Icon paths updated from `/ajdevhub/assets/icons/...` to `/assets/icons/...` and wrapped with `relative_url`
  - Internal links normalized to `{{ '/path' | relative_url }}` for baseurl safety
  - Homepage and footer enhancements (modern overview, multi-column footer)
  - Documentation updates: [README.md](README.md) and [.github/copilot-instructions.md](.github/copilot-instructions.md)
  - Targeted page fixes in sorting guide and DSA hub

Template for future entries:
- YYYY-MM-DD:
  - Brief summary of change 1
  - Brief summary of change 2

**Setup**

Before running any commands, set the `$WORKSPACE_ROOT` variable in PowerShell:

```powershell
# Set to your repo root directory
$WORKSPACE_ROOT = "C:\path\to\your\repo"  # or use $(Get-Location) if already in repo root
```

All commands below use `$WORKSPACE_ROOT` instead of full paths for privacy and portability.

---

**Purpose**

- **Central record:** Tracks problems found, the fixes applied, and the exact steps used to resolve them.
- **Repeatable workflows:** Provides copy-paste commands and checklists to re-run or extend fixes.
- **Living document:** Add future issues and resolutions in the same format below.

---

**Recent Fixes**

- **Emoji/Mojibake Repair:** Corrupted sequences (e.g., `ðŸ`, `ï¸`) across learning pages fixed.
- **External Links (new-tab):** Ensured HTTP/HTTPS links open in new tabs via Jekyll Markdown attributes.
- **Icon Path Cleanup:** Replaced stale `/ajdevhub/assets/icons/...` with `/assets/icons/...`.
- **Baseurl-Safe Internal Links:** Converted absolute internal links to `{{ '/path' | relative_url }}`.
- **Homepage & Footer Enhancements:** Modernized [index.md](index.md) and [_layouts/default.html](_layouts/default.html).
- **Docs & Guidance:** Created [.github/copilot-instructions.md](.github/copilot-instructions.md) and rewrote [README.md](README.md).

---

**1) Emoji/Mojibake Repair**

- **Problem:** Garbled emoji characters displayed as `ðŸ...` or `ï¸...` in multiple files under [learning/](learning/).
- **Scope:** Strings, Arrays, Searching-Sorting, OOP, Networking, OS, System Design sections.
- **Solution:** Use `ftfy` to automatically repair text and write back safely.

- **Files Updated:** Script [fix_emojis.py](fix_emojis.py) replaced with a robust `ftfy`-based repair.

- **Steps to Re-run:**

```powershell
# Ensure venv is active for the repo (already configured)
& "$WORKSPACE_ROOT/.venv/Scripts/python.exe" -m pip install ftfy

# Run the repair script from repo root
& "$WORKSPACE_ROOT/.venv/Scripts/python.exe" -u fix_emojis.py
```

- **Validation:** Search for mojibake remnants after repair.

```powershell
# Quick grep-like scan (pattern often seen in mojibake)
Select-String -Path learning/**/*.md -Pattern "ðŸ|ï¸" -AllMatches
```

- **Notes:** The updated script reads file content with `errors='replace'` and fixes text using `ftfy`, then writes atomically where possible.

---

**2) External Links Open in New Tabs**

- **Problem:** External links were opening in the same tab.
- **Scope:** ~87 markdown files under [learning/](learning/) had ~94 HTTP/HTTPS links.
- **Solution:** Append Jekyll Markdown attributes to links: `{:target="_blank" rel="noopener noreferrer"}`.

- **Example:**
  - Before: `[LeetCode 88](https://leetcode.com/...)`
  - After: `[LeetCode 88](https://leetcode.com/...){:target="_blank" rel="noopener noreferrer"}`

- **One-liner (PowerShell) to re-apply if needed):**

```powershell
$basePath = "$WORKSPACE_ROOT/learning"
$files = Get-ChildItem -Path $basePath -Filter "*.md" -Recurse
foreach ($file in $files) {
  $content = Get-Content -Path $file.FullName -Raw
  $pattern = '\[([^\]]+)\]\((https?://[^)]+)\)(?!\{:target)'
  $updated = [regex]::Replace($content, $pattern, {
    param($m)
    "[{0}]({1}){:target=\"_blank\" rel=\"noopener noreferrer\"}" -f $m.Groups[1].Value, $m.Groups[2].Value
  })
  if ($updated -ne $content) { Set-Content -Path $file.FullName -Value $updated }
}
```

- **Validation:** Manually click external links in a local preview; confirm they open in a new tab.

---

**3) Icon Path Cleanup**

- **Problem:** Some pages referenced icons via an old prefix `/ajdevhub/assets/icons/...`.
- **Scope:** Arrays, Two-Pointers, Sliding Window, Searching-Sorting, Strings.
- **Solution:** Update to `/assets/icons/...`, then convert to baseurl-safe `relative_url`.

- **Examples:**
  - [learning/dsa/Arrays/two-pointers/index.md](learning/dsa/Arrays/two-pointers/index.md)
  - [learning/dsa/Arrays/sliding-window/index.md](learning/dsa/Arrays/sliding-window/index.md)
  - [learning/dsa/Arrays/index.md](learning/dsa/Arrays/index.md)
  - [learning/dsa/Searching-Sorting/index.md](learning/dsa/Searching-Sorting/index.md)
  - [learning/dsa/Searching-Sorting/searching-sorting.md](learning/dsa/Searching-Sorting/searching-sorting.md)
  - [learning/dsa/Strings/index.md](learning/dsa/Strings/index.md)
  - [learning/dsa/Strings/string.md](learning/dsa/Strings/string.md)

- **Pattern Used:**
  - Before: `<img src="/ajdevhub/assets/icons/rocket.svg" ...>`
  - After: `<img src="{{ '/assets/icons/rocket.svg' | relative_url }}" ...>`

- **Validation:** Workspace scan shows no remaining `/ajdevhub/assets/icons` references.

---

**4) Baseurl-Safe Internal Links**

- **Problem:** Absolute internal links (e.g., `](/projects)`) can break if `baseurl` changes.
- **Scope:** Various pages including [about.md](about.md).
- **Solution:** Use Liquid filter for internal links: `{{ '/path' | relative_url }}`.

- **Example Changes:**
  - [about.md](about.md):
    - `[/projects]` → `{{ '/projects' | relative_url }}`
    - `[/blogs]` → `{{ '/blogs' | relative_url }}`

- **Validation:** Repo-wide scan confirms no markdown links starting with `](/...)` remain.

---

**5) Homepage & Footer Enhancements**

- **Homepage:** [index.md](index.md)
  - **Overview section:** Modern hero, stats, exploration cards.
  - **Activity section:** Fixed recent posts rendering to use proper HTML anchors.
  - **CTAs:** Button-style links via `.btn-crosslink`.

- **Footer:** [_layouts/default.html](_layouts/default.html)
  - **Multi-column grid:** About, Learning, Connect sections.
  - **Social links:** GitHub, LinkedIn, tech attribution.
  - **All internal links:** Use `relative_url`.

---

**6) Documentation & Guidance**

- **AI Agent Guidance:** [.github/copilot-instructions.md](.github/copilot-instructions.md)
  - Jekyll stack, permalink patterns, layout dependencies, JS expectations, authoring templates, build workflow.

- **Project Onboarding:** [README.md](README.md)
  - Quick start, structure overview, authoring guides, navigation rules, common mistakes, file map.

---

**7) Targeted Page Fixes**

- **Sorting Guide:** [learning/dsa/Searching-Sorting/sorting.md](learning/dsa/Searching-Sorting/sorting.md)
  - Fixed hybrid HTML/Markdown conflicts.
  - Corrected icon paths.
  - Ensured external links have new-tab attributes.
  - Cleaned PDF link formatting.

- **DSA Hub:** [learning/dsa/index.md](learning/dsa/index.md)
  - Replaced corrupted emojis with proper Unicode.

---

**Validation Checklist**

- **Links:**
  - Internal links use `{{ '/path' | relative_url }}`.
  - External links include `{:target="_blank" rel="noopener noreferrer"}`.
- **Icons/Images:**
  - No `/ajdevhub/...` paths remain.
  - Image `src` uses `relative_url` for baseurl safety.
- **Mojibake:**
  - No `ðŸ` or `ï¸` sequences detected by scans.
- **Layouts:**
  - CSS/JS includes use `relative_url`.

---

**How To Add Future Entries**

- **Append a new section** with the format: Problem, Scope, Solution, Steps, Validation, Files.
- **Keep it actionable:** Include commands and exact patterns.
- **Reference files** using markdown links (e.g., [path/to/file.md](path/to/file.md)).
- **Update this log** after each change; keep it the single source of truth.

---

**Quick Commands**

- **Local preview:**

```powershell
jekyll serve --livereload
```

- **Run emoji repair:**

```powershell
& "$WORKSPACE_ROOT/.venv/Scripts/python.exe" -u fix_emojis.py
```

---

**Notes**

- **Config:** [_config.yml](_config.yml) sets `url` to the GitHub Pages domain; `baseurl` is empty.
- **Best practice:** Always use `relative_url` for internal assets/links.
- **OneDrive locks:** Atomic writes are used to minimize sync conflicts; rerun scripts if locked.

---

**Helper Script: Append Changelog Entry**

- **Purpose:** Quickly add a dated entry under the **Changelog** section of this file.
- **Script:** [scripts/add_changelog_entry.py](scripts/add_changelog_entry.py)

- **Usage:**

```powershell
# Dry-run (prints proposed changes without writing)
& "$WORKSPACE_ROOT/.venv/Scripts/python.exe" scripts/add_changelog_entry.py --dry-run --item "Your change summary" --item "Another bullet"

# Write to file with today's date
& "$WORKSPACE_ROOT/.venv/Scripts/python.exe" scripts/add_changelog_entry.py --item "Updated footer styles" --item "Normalized image paths"

# Specify custom date
& "$WORKSPACE_ROOT/.venv/Scripts/python.exe" scripts/add_changelog_entry.py --date 2025-12-28 --item "Refactored navigation JS" --item "Added new blog post"
```

- **Behavior:**
  - Inserts entries immediately after the **Changelog** header.
  - Uses atomic write to avoid OneDrive sync locks.
  - Accept multiple `--item` flags to include several bullets.

---

**Pre-Commit Validation**

- **Purpose:** Run automated checks before committing to catch common issues.
- **Script:** [scripts/validate_site.py](scripts/validate_site.py)

- **Checks Performed:**
  - Mojibake/corrupted emoji sequences
  - External links missing `target="_blank"` attributes
  - Stale `/ajdevhub/` asset paths
  - Absolute internal markdown links (not using `relative_url`)
  - Image `src` attributes without `relative_url` filter

- **Quick Run:**

```powershell
& "$WORKSPACE_ROOT/.venv/Scripts/python.exe" scripts/validate_site.py
```

- **Integration Suggestion:**
  - Run before every commit to catch issues early.
  - Fix any reported issues, re-run validation to confirm.
  - Consider adding to CI/CD or pre-commit hooks if using Git LFS or Actions.
