---
layout: post
title: "Supercharge Your Static Site: Adding a Free, Real-Time CMS to GitHub Pages"
date: 2026-02-25 00:00:00 +0530
categories: [general, system-design]
---

There is an undeniable beauty to static site generators like Jekyll, Hugo, and Next.js. They are incredibly fast, ridiculously secure, and can be hosted for completely free on GitHub Pages. 

However, they all share one incredibly frustrating bottleneck: **The Publishing Experience.**

If you want to write a new blog post or add a new project to your portfolio, you typically have to open your IDE, create a new Markdown file, manually type out the YAML Front Matter exactly right, write your post in raw text, commit the file, and `git push` it to your repository. It is a tedious workflow, especially when you just want to fix a typo from your phone.

But what if you could have the speed and security of a Static GitHub Pages site, combined with the beautiful, rich-text dashboard of WordPress? 

Enter **Decap CMS** (formerly Netlify CMS).

In this post, I am going to walk you through exactly how I added a completely free, database-less, real-time Content Management System to this very portfolio.

## Architecture: How it Works

Because a GitHub Pages site is purely static HTML/CSS, you cannot run a traditional backend database. So, where does the CMS live?

Decap CMS is a "Headless CMS". It is literally just a single HTML file and a Javascript bundle (`admin/index.html`) that lives in your repository. When you navigate to `/admin`, the React application boots up in your browser. 

When you write a post and hit "Publish", the CMS uses the GitHub API to literally write the Markdown file and commit it sequentially to your repository on your behalf. GitHub Pages detects the new commit, rebuilds your site automatically, and your blog is live in seconds.

## Step 1: Bridge the Authentication (The Secret Sauce)

To allow the CMS to safely commit files to your GitHub repository without forcing you to memorize OAuth tokens, you need an Identity broker. The absolute easiest way to do this is to link your GitHub repository to **Netlify**.

> [!NOTE] 
> Your code still permanently lives on GitHub. Netlify is simply acting as the fast CDN host and the authentication broker.

1. Go to [Netlify](https://app.netlify.com/) and create a free account.
2. Click **Add new site -> Import an existing project -> Deploy with GitHub**.
3. Select your Jekyll/Hugo repository and hit **Deploy**.

## Step 2: Enable Git Gateway

Once your site is live on Netlify, we need to explicitly give it permission to edit your GitHub repository.

1. In your Netlify dashboard, go to **Site settings > Identity** (on the left menu).
2. Click the massive **Enable Identity** button.
3. Scroll further down that same page to **Services > Git Gateway**.
4. Click **Enable Git Gateway**.

This securely binds your Netlify Auth infrastructure directly to your GitHub repository structure.

## Step 3: Scaffold the CMS Application

Now we inject the actual CMS into your repository. You only need to create two files. Create an `admin` folder at the root of your project.

### 1. `admin/index.html`
This is the React application payload. It loads the CMS and the Netlify Identity login widget.

```html
<!doctype html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Content Manager</title>
</head>
<body>
    <!-- Decap CMS Script -->
    <script src="https://unpkg.com/decap-cms@^3.0.0/dist/decap-cms.js"></script>
    
    <!-- Netlify Identity Widget for Authentication -->
    <script src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>
    <script>
      if (window.netlifyIdentity) {
        window.netlifyIdentity.on("init", user => {
          if (!user) {
            window.netlifyIdentity.on("login", () => {
              document.location.href = "/admin/";
            });
          }
        });
      }
    </script>
</body>
</html>
```

### 2. `admin/config.yml`
This file is the brain of the CMS. It tells Decap exactly what folders to look at (e.g., `_posts`) and what fields to generate in the dashboard UI. Notice that we set the backend to `git-gateway`.

```yaml
backend:
  name: git-gateway
  branch: master # Update this to 'main' if that is your default branch

media_folder: "assets/images/posts"
public_folder: "/assets/images/posts"

collections:
  - name: "blog"
    label: "Blog Posts"
    folder: "_posts"
    create: true
    slug: "{{year}}-{{month}}-{{day}}-{{slug}}"
    fields:
      - {label: "Layout", name: "layout", widget: "hidden", default: "post"}
      - {label: "Title", name: "title", widget: "string"}
      - {label: "Publish Date", name: "date", widget: "datetime"}
      - {label: "Categories", name: "categories", widget: "list", default: ["general"]}
      - {label: "Body", name: "body", widget: "markdown"}
```

## Step 4: The Crucial Routing Fix

There is one major "Gotcha" that frustrated me during implementation.

To gain access to your shiny new CMS dashboard, you have to invite yourself via the Netlify Identity panel. Netlify will send you an email with a link that looks like this:
`yourwebsite.com/#invite=token123`

**The Problem:** The email link usually drops you onto your *homepage*, not the `/admin` page. If your homepage doesn't have the Netlify Identity script loaded, the website won't know how to intercept that `#invite=` URL token! You'll just see your normal site.

**The Fix:** You *must* inject the Identity script into your global layout template (usually `_layouts/default.html`) before the closing `</head>` tag:

```html
<!-- Inside _layouts/default.html -->
<script src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>
```

Now, no matter where the invite email links you, the Identity widget will catch the token and open the setup modal!

## Step 5: Invite Yourself and Publish

1. Go back to your Netlify Dashboard and click the **Identity** tab at the top.
2. Click **Invite Users** and send an invite to your email.
3. Click the link in your email, set your password in the modal, and you are in!

Navigating to `yourwebsite.com/admin/` will now greet you with a beautiful, rich-text WYSIWYG editor. You can drag and drop images, assign categories natively, and write your technical documentation naturally. 

When you click "Publish", the CMS handles the Git pipeline invisibly in the background. It is truly the ultimate blend of static-site performance and modern content management.

<br>

> [!TIP]
> You can easily expand your `admin/config.yml` to define multiple collections. For example, I have a second collection mapping directly to my `_projects` repository to easily update my portfolio showcases!
