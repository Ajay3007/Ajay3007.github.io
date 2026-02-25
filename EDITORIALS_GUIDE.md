---
layout: default
title: Editorials & Code Solutions Guide
permalink: /editorials-guide/
---

# 📖 Editorials & Code Solutions Guide

This guide explains how to add approaches, solutions, and code files to your Practice Problems database securely. The **Interactive Problems Hub** automatically detects your links and generates beautiful, color-coded buttons based on the file type you provide!

---

## 🏗️ 1. Adding Markdown Editorials (`.md`)
*Best for written approaches, time/space complexities, and embedded code combined.*

### From Decap CMS (Netlify Admin) **[RECOMMENDED]**
1. Navigate to **`ajdevhub.netlify.app/admin`** and log in.
2. Click on **DSA Editorials** on the left menu.
3. Click **New DSA Editorial**, write out your Markdown solution, and hit Publish.
4. Next, go to **Data Files > DSA Problems Database** and select the problem.
5. In the `approach_url` field, paste exactly: `/editorials/your-slug/`
6. Publish! The UI will instantly generate a 📖 **Editorial** button.

### From Local Repository
1. Create a markdown file inside the `_editorials/` directory: `_editorials/my-solution.md`
2. At the top of the file, include the required YAML frontmatter:
   ```yaml
   ---
   layout: editorial
   title: "Problem Title Solution"
   problem_id: "123"
   date: 2024-03-24T12:00:00.000Z
   ---
   ```
3. Open `_data/problems.yml`, exactly find your problem, and set:
   `approach_url: "/editorials/my-solution/"`

---

## 📝 2. Adding Handwritten PDF Notes (`.pdf`)
*Best for scanning your notebook or attaching visual diagrams.*

### From Local Repository
1. Move your `.pdf` into the relevant topic path: `_learning/dsa/Arrays/notes.pdf`
2. Open `_data/problems.yml` and find the problem block.
3. EXACTLY copy the case-sensitive path to your file:
   `approach_url: "/learning/dsa/Arrays/notes.pdf"`
4. Commit and push. The UI will extract the `.pdf` extension and generate a 📝 **PDF Notes** button.

*Note: GitHub Pages routing is strictly **case-sensitive** (e.g. `/Arrays/` is not `/arrays/`).*

---

## 💻 3. Adding Raw Code Files (`.cpp`, `.py`, `.java`, etc.)
*Best if you only want to save raw code snippets without any markdown explanation.*

### From Local Repository
1. Save your `.cpp` or `.py` file into the relevant directory: `_learning/dsa/Arrays/solution.cpp`
2. Open `_data/problems.yml` and find the problem block.
3. Link the code string directly into the database:
   `solution_url: "/learning/dsa/Arrays/solution.cpp"`
4. Commit and push. The UI will extract the code extension and generate a 💻 **Raw Code** button.

---

## 🔗 4. Adding External Links (LeetCode)
*Best if you want to reference a heavily upvoted community solution on Leetcode.*

### From Decap CMS (Netlify Admin) or Local
1. Copy the full static link: `https://leetcode.com/problems/two-sum/solutions/123/my-solution/`
2. Depending on whether it's more theory or just code, dump it into the Database under `approach_url` or `solution_url`.
3. The custom UI will detect the external domain name and generate a 🔗 **External Docs/Code** button.

---

## ⚠️ Important Rules for `problems.yml`
- **Do not duplicate URLs:** If you have just ONE link that contains both explanation and code (like a Markdown editorial), ONLY put it in `approach_url`. Leave `solution_url` completely empty so the UI doesn't render two identical buttons.
- **Paths are strict strings:** Always start internal paths with a forward slash (`/`).
- **Never point directly to GitHub repo blobs:** Use Jekyll relative routing: `/editorials/...` instead of `https://github.com/...`
