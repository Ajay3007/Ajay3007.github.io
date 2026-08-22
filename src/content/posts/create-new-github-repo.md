---
title: "How to Create a New GitHub Repo and Push a Local Project"
description: "When you start a new project locally (Java, DSA notes, website, etc.), the next step is usually to push it into GitHub. This guide explains the complete workflow."
date: 2026-01-18
tags: [general]
url: /blog/2026/01/18/create-new-github-repo/
---

# How to Create a New GitHub Repo and Push a Local Project 🚀

When you start a new project locally (Java, DSA notes, website, etc.), the next step is usually to push it into GitHub. This guide explains the complete workflow to:

✅ Create a new GitHub repository  
✅ Initialize Git in your local project  
✅ Commit your code  
✅ Push it to GitHub  

This is a reusable step-by-step process you can follow for any future project.

---

## Prerequisites

Before starting, make sure you have:

- A GitHub account
- Git installed on your system

Check Git installation:

```bash
git --version
```

---

## Step 1: Create a New Repository on GitHub

1. Open GitHub and click **"+" → New repository**
2. Enter a repository name  
   Example: `JavaFoundry`
3. Choose repo visibility:
   - ✅ Public (recommended for portfolio)
   - 🔒 Private (if needed)
4. **Important:** Do **NOT** check:
   - “Add a README”
   - “Add .gitignore”
   - “Add license”

(We will create them locally.)

5. Click **Create repository**

GitHub will show the repo URL like:

- HTTPS: `https://github.com/<username>/<repo>.git`
- SSH: `git@github.com:<username>/<repo>.git`

---

## Step 2: Open Terminal in Your Local Project Folder

Navigate into your project folder:

```bash
cd path/to/your/project
```

Verify files:

```bash
ls
```

---

## Step 3: Initialize Git in Your Local Folder

Run:

```bash
git init
```

Now your folder becomes a Git repository.

---

## Step 4: Add a `.gitignore` File (Recommended)

A `.gitignore` tells Git what **NOT** to push to GitHub.

Create `.gitignore`:

```bash
touch .gitignore
```

For Java + IntelliJ projects, add:

```gitignore
# IntelliJ IDEA
.idea/
*.iml

# Java build output
out/
target/
*.class

# OS files
.DS_Store
Thumbs.db
```

---

## Step 5: Stage Your Code

Stage everything:

```bash
git add .
```

Check status:

```bash
git status
```

---

## Step 6: Commit Your Changes

Commit with a meaningful message:

```bash
git commit -m "Initial commit"
```

---

## Step 7: Link Local Repo with GitHub Repo (Add Remote)

Add the GitHub remote:

### ✅ Using HTTPS
```bash
git remote add origin https://github.com/<username>/<repo>.git
```

Verify remote:

```bash
git remote -v
```

---

## Step 8: Push Your Code to GitHub

Rename branch to `main` (GitHub standard):

```bash
git branch -M main
```

Push code:

```bash
git push -u origin main
```

✅ Done — your local project is now available on GitHub.

---

## Step 9: Verify on GitHub

Go to your repo page and refresh. You should see:

- all your files
- latest commit message
- branch `main`

---

# Common Errors and Fixes

## 1) ❌ `remote origin already exists`

Fix:

```bash
git remote remove origin
git remote add origin https://github.com/<username>/<repo>.git
```

---

## 2) ❌ Authentication Failed (HTTPS)

GitHub no longer allows password authentication for git pushes.

✅ Fix options:
- Use **Personal Access Token (PAT)** as password
- OR use **SSH**
- OR use **GitHub Desktop** (easy UI)

---

# Recommended Workflow for Future Updates

Whenever you make changes:

```bash
git add .
git commit -m "Updated notes: Constructors + GC"
git push
```

---

# Bonus: Best Repo Structure for Learning Projects

If you're building a learning repo like JavaFoundry:

```
JavaFoundry/
├── src/
├── notes/
│   ├── constructors.md
│   ├── methods.md
│   └── memory-management-gc.md
├── diagrams/
│   └── *.puml
├── README.md
└── .gitignore
```

This makes your repo clean and scalable.

---

## Summary

✅ Create repo on GitHub  
✅ `git init` locally  
✅ `git add .`  
✅ `git commit -m "..."`  
✅ `git remote add origin <url>`  
✅ `git push -u origin main`  

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="/blogs" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← All Blogs</a>
  <a href="/" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Home 🏠</a>
</div>