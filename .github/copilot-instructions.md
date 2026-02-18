# Copilot Instructions for ajdevhub

## Project Architecture

This is a Jekyll-powered static portfolio site deployed via GitHub Pages. Architecture:

- **Content system**: Jekyll collections (`_posts`, `_projects`) + unstructured markdown (`learning/`)
- **Layouts**: Shared shell in [`_layouts/default.html`](_layouts/default.html) (nav, footer), specialized wrappers for posts ([`_layouts/post.html`](_layouts/post.html)) and projects ([`_layouts/project.html`](_layouts/project.html))
- **Navigation**: Active state computed via `page.url` substring checks in default layout header
- **URL structure**: Posts render at `/blog/YYYY/MM/DD/slug/`, projects at `/projects/slug/` per [`_config.yml`](_config.yml)
- **Styling**: Single CSS file [`assets/css/main.css`](assets/css/main.css) with CSS variables, gradient themes, and card-based responsive design
- **Interactivity**: Vanilla JS in [`assets/js/home.js`](assets/js/home.js) (tabs, search filter, animations) and [`assets/js/nav.js`](assets/js/nav.js) (mobile nav toggle)

## Content Authoring Conventions

### Blog Posts (`_posts/`)
- **Naming**: `YYYY-MM-DD-slug.md` (e.g., `2025-01-05-two-pointer-technique.md`)
- **Required front matter**: `layout: post`, `title`, `date`, `categories` (array), `excerpt`
- **Categories**: Use existing tags like `[dsa, algorithms]`, `[networking]`, `[system-design]`
- See [`_posts/2025-01-05-two-pointer-technique.md`](_posts/2025-01-05-two-pointer-technique.md) for template

### Project Pages (`_projects/`)
- **Naming**: `project-slug.md` (e.g., `devtoolbox.md`, `tax_hurdle.md`)
- **Required front matter**: `layout: project`, `title`, `description`, optional `permalink`
- **Structure**: Hero section with GitHub CTA, problem statement, features as cards with gradient styling
- See [`_projects/devtoolbox.md`](_projects/devtoolbox.md) for comprehensive example

### Learning Pages (`learning/`)
- **Organization**: Topic folders (`dsa/`, `networking/`, `system-design/`, `ai-ml/`, `finance/`) with `index.md` hubs
- **Front matter**: `layout: default`, `title` only (simpler than posts/projects)
- **Navigation**: Must link from parent `index.md` to be discoverable; uses relative paths
- **Summaries**: Can include auto-generated TOC/summary blocks (see script workflow below)

### Solution Files (`learning/dsa/[topic]/leetcode-[number]-solution.md`)
- **Naming**: `leetcode-[number]-solution.md` (e.g., `leetcode-206-solution.md`)
- **Location**: Same directory as the problem list file
- **Required front matter**: 
  - `layout: default`
  - `title: [Problem Name] - Solution`
  - `permalink: /learning/dsa/[topic]/leetcode-[number]-solution/`
- **Structure** (sections in order):
  1. **Header**: H1 with emoji + platform info (`**LeetCode #[number]** | **Difficulty:** [Easy/Medium/Hard]`)
  2. **Approach**: High-level strategy and technique description
  3. **Algorithm Explanation**: Step-by-step numbered breakdown
  4. **Complexity Analysis**: Time and Space complexity with explanations
  5. **[Language] Solution**: Code block with implementation (preserve user's exact code)
  6. **Footer**: Navigation buttons back to Problems page and topic Hub
- **Important**: Do NOT modify the user's solution code - use it exactly as provided
- See [`learning/dsa/linked-list/leetcode-206-solution.md`](learning/dsa/linked-list/leetcode-206-solution.md) for reference template

## Link Patterns (Critical)

**Always use these patterns** to ensure baseurl compatibility and proper external link behavior:

### Internal links in Liquid templates
```liquid
{{ '/path/to/page' | relative_url }}
```
Used in: layouts, includes, front matter `permalink`. See [`_layouts/default.html`](_layouts/default.html) nav links.

**Active nav state pattern** (in [`_layouts/default.html`](_layouts/default.html)):
```liquid
{% assign cur = page.url | default: '/' %}
<a href="..." class="{% if cur == '/exact/path' %}active{% endif %}">Link</a>
<a href="..." class="{% if cur contains '/section' %}active{% endif %}">Link</a>
```
Uses substring matching (`contains`) for section detection and exact match for homepage.

### External links in Markdown
```markdown
[Link text](https://example.com){:target="_blank" rel="noopener noreferrer"}
```
**Required** for all HTTP/HTTPS links per [`LINK_CONVERSION_GUIDE.md`](LINK_CONVERSION_GUIDE.md). Opens in new tab with security attributes. Use this pattern consistently; internal Jekyll links (relative or `relative_url`) do NOT need these attributes.

### Internal content links
```markdown
[Relative link](../sibling/page.md)
[Absolute link](/learning/dsa/index.md)
```
Prefer relative for sibling pages; absolute with leading `/` for cross-section links.

### Icon paths
```liquid
{{ '/assets/icons/filename.svg' | relative_url }}
```
**Never** hardcode `/ajdevhub/assets/icons/...` (old baseurl artifact). Use `relative_url` filter.

## Development Workflow

### Local preview (required before commits)
```powershell
jekyll serve --livereload
```
Opens at `http://127.0.0.1:4000` with auto-refresh on file changes. **No Gemfile** exists; uses system gems (`gem install jekyll bundler`).

### Python environment
Virtual environment at `.venv/` for maintenance scripts. Activate with:
```powershell
& ".venv\Scripts\Activate.ps1"
```
Used for `fix_emojis.py`, `generate_summary.py`, and validation scripts.

### Content maintenance scripts (`scripts/`)

**Summary generator** ([`scripts/generate_summary.py`](scripts/generate_summary.py)):
- Auto-generates executive summaries with TOC, reading time, key points
- Usage: `python scripts/generate_summary.py learning/dsa/Arrays/index.md` (single file)
- Batch mode: `python scripts/generate_summary.py --batch learning/dsa/` (entire directory)
- Creates `.bak` backups; see [`scripts/SUMMARY_GENERATION_GUIDE.md`](scripts/SUMMARY_GENERATION_GUIDE.md)

**Emoji repair** ([`fix_emojis.py`](fix_emojis.py)):
- Fixes mojibake (garbled UTF-8 sequences like `ðŸ`, `ï¸`) using `ftfy` library
- Run from repo root: `python -u fix_emojis.py`
- Validates with grep search after repair (see [`SITE_MAINTENANCE_LOG.md`](SITE_MAINTENANCE_LOG.md))

**Link conversion** (documented in [`LINK_CONVERSION_GUIDE.md`](LINK_CONVERSION_GUIDE.md)):
- PowerShell regex script to batch-add `{:target="_blank"}` to external links
- Pattern: `\[([^\]]+)\]\((https?://[^)]+)\)(?!\{:target)` → with attributes

## Style Guidelines

### Card-based UI components
Projects and blog listings use gradient-styled cards:
```html
<div class="project-card" style="background:#f8fafc;border-radius:10px;box-shadow:0 2px 8px #e2e8f0;padding:1.5rem;">
  <h3>Title</h3>
  <p>Description</p>
</div>
```
CSS classes defined in [`assets/css/main.css`](assets/css/main.css) with `--primary-color`, `--secondary-color`, `--accent-color` variables.

### Gradient CTAs
Buttons use dual-color gradients:
```html
<a href="..." style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); ...">
  📦 View on GitHub
</a>
```
Common in project pages (see [`_projects/devtoolbox.md`](_projects/devtoolbox.md)).

### Responsive design
- **Breakpoints**: Mobile-first with `@media (max-width: 768px)` in CSS
- **Grid layout**: `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` for cards
- **Mobile nav**: Hamburger toggle handled by [`assets/js/nav.js`](assets/js/nav.js)

## Maintenance Patterns

### Before major changes
1. Check [`SITE_MAINTENANCE_LOG.md`](SITE_MAINTENANCE_LOG.md) for recent fixes and patterns
2. Run `jekyll serve --livereload` to catch build errors
3. Grep search for old patterns before bulk changes

### After content edits
1. **Validate links**: Use PowerShell script from [`LINK_CONVERSION_GUIDE.md`](LINK_CONVERSION_GUIDE.md) to ensure external links have `{:target="_blank" rel="noopener noreferrer"}`
2. **Check encoding**: Run `fix_emojis.py` if emoji display issues occur
3. **Update summaries**: For learning pages, run `generate_summary.py --batch` on modified directories
4. **Test locally**: Always verify `jekyll serve --livereload` builds without errors before committing

### Batch reorganization patterns
When restructuring file paths (e.g., `taxhrd/` → `tax_hurdle/`):
1. Create new directory structure first
2. Update `_projects/` and `learning/` hub pages with new paths
3. Update internal links in markdown files pointing to moved content
4. Verify no broken references by searching old path names in `.md` files (check logs in [`SITE_MAINTENANCE_LOG.md`](SITE_MAINTENANCE_LOG.md) for examples)

## Critical AI Agent Constraints

**Read [`learning/COPILOT_RULES.md`](../learning/COPILOT_RULES.md) before making changes.**

These rules govern AI involvement in this portfolio:
1. **NEVER** introduce new technical ideas, architectures, or design decisions
2. **ONLY** expand clarity, format content, or implement explicitly requested features
3. **Preserve ownership**: Core logic, understanding, and trade-offs belong to the repo owner
4. **When uncertain**: Ask clarifying questions instead of assuming design intent
5. **Documentation-first role**: Format, structure, and clarify—don't architect

This is a **personal learning portfolio**, not a collaborative system design exercise. Respect the owner's voice and authority over all technical decisions.

## Project-Specific Knowledge

### Why no Gemfile?
Site uses system-installed Jekyll gems (referenced in [`README.md`](README.md)). Keep it this way to match deployment env.

### Why .bak files exist
Summary generator creates backups before modifications. Clean with PowerShell:
```powershell
Get-ChildItem "learning\dsa\" -Filter "*.md.bak" -Recurse | Remove-Item
```
See cleanup commands in [`SITE_MAINTENANCE_LOG.md`](SITE_MAINTENANCE_LOG.md#L64-L72).

### Why search is client-side
Home page search ([`assets/js/home.js`](assets/js/home.js)) filters DOM via `textContent.toLowerCase().indexOf()`. No server component; static site limits. Preserves GitHub Pages compatibility.

### Learning hub organization
- **Structured sections**: `dsa/`, `networking/`, `system-design/`, `ai-ml/`, `programming-language/`, `operating-systems/`, `oop/`, `competitive-programming/`, `data-plane/`, `4g-5g/`, `finance/`
- **Finance hub** is multi-project: Contains `tax_hurdle/` subdirectory (TaxHrd investment tax system) + future finance topics
- **Each section** has `index.md` hub that links to subtopics; pages must be discoverable via parent navigation

### Collections vs. unstructured content
- `_posts` and `_projects` are Jekyll collections with rich metadata, pagination, URL patterns
- `learning/` is plain Markdown for flexibility, manually linked hierarchies
- Both render through layouts but different access patterns (`site.posts` vs. relative links)

## When Making Changes

**Adding nav items**: Update [`_layouts/default.html`](_layouts/default.html) header with `relative_url` and active state logic.

**Changing URL structure**: Modify `_config.yml` permalinks; verify all internal links still resolve.

**New content sections**: Follow existing patterns—create `index.md` hub, use appropriate layout, link from main nav or parent index.

**Batch operations**: Use PowerShell for link conversion, Python scripts for content generation. Always back up first (`.bak` convention).

**Before deployment**: Run local preview, check browser console for errors, verify mobile nav, test search filter on home page.
