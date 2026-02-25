# 🎉 Release v1.1.0: Editorials CMS & Problems Hub Re-architecture

This release represents a massive structural upgrade to the Learning Portal's Problem Tracking infrastructure. We have completely decoupled rigid inline solutions into a dedicated CMS database, added dynamic URL tracking, and modernized the UI.

---

### 🚀 Major Features & Updates

#### 1. The Decap CMS Editorials Pipeline (`_editorials/`)
- **Automated Solutions Extraction Workflow:** Programmatically stripped hundreds of legacy inline anchors (`#minimum-window-substring`) embedded within massive `*-problems.md` markdown pages.
- **Dedicated CMS Collection:** Ported all extracted standalone solutions and embedded notes into a brand new `_editorials/` Jekyll collection natively hooked up to the Decap CMS Admin dashboard.
- **Frontmatter Injection:** Dynamically injected precise YAML frontmatter (ex: `problem_id`, `date`, `title`) into all recovered `.md` and `.cpp` solutions to allow CMS parsing.

#### 2. Problem Hub UI Deduplication Engine
- **Intelligent URL Sniffing:** Rewrote the DOM Generation script (`problems.js`) to actively read the file extensions of incoming database links (e.g. `.pdf`, `.cpp`, `.com`) to automatically generate perfect semantics. 
- **Dynamic Buttons:** The Hub now accurately assigns graphical buttons such as 📝 **PDF Notes**, 💻 **Raw Code**, 📖 **Editorial**, or 🔗 **External Link** based purely on the string path.
- **Cloned Link Scrubbing:** Ran a global deduplication script across the `_data/problems.yml` schema to aggressively delete any duplicated strings where `solution_url` perfectly matched `approach_url`. The UI now seamlessly combines dual-format materials without rendering double buttons.

#### 3. Cross-Domain Authentication Fixes
- **Git Gateway Config Repairs:** Fixed the critical Netlify Identity configuration mismatch in `admin/config.yml` where Decap CMS was erroneously attempting to auth against the GitHub Pages subpath instead of the Netlify backend.
- **Script Inject Order:** Reordered the HTML `<script>` tags in `admin/index.html` to guarantee the Identity Token payload mounts before Decap CMS attempts to call the login endpoint.

#### 4. System Documentation
- **Editorials Insertion Guide:** Built a canonical `EDITORIALS_GUIDE.md` manual instructing users exactly how to assign `.md`, `.pdf`, `.cpp`, or Leetcode links from both the Local Repository and Netlify CMS dashboard.
- Navigational routing hooked into the top of the Problems Hub for instant reading!

---

*Compiled on: February 25, 2026*
