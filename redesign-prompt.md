# Redesign brief — ajdevhub (Direction C: Signal / Packet)

You are working on the Jekyll site at this repo (a personal portfolio + learning hub). Apply the redesign described below directly to the existing files. Do **not** create a parallel set of mock files — edit the real ones.

The user has already chosen the visual direction; your job is faithful execution, not redesign. If you find a conflict between this brief and existing code, follow the brief.

---

## 1. Design tokens (the source of truth)

Replace the entire `:root` block in `assets/css/main.css` with these tokens. Delete the `[data-theme="dark"]` block — the site is **dark-only**. Also remove the inline `<script>` in `_layouts/default.html` that sets `data-theme` from localStorage, and remove the `#theme-toggle` button + its handler script. The site has one mode now.

```css
:root {
  /* Background layers */
  --bg:        #06080d;   /* page */
  --panel:     #0d121b;   /* cards, asides */
  --panel-2:   #11182a;   /* nested / chips */

  /* Ink */
  --ink:       #e6ebf2;   /* primary text + headings */
  --body:      #aab4c2;   /* body copy */
  --dim:       #6a7388;   /* metadata, captions */
  --faint:     #2a3142;   /* grid lines, dividers when subtle */

  /* Rules */
  --rule:      #1a2030;   /* card borders, section dividers */

  /* Signal */
  --accent:    #22d3ee;   /* the ONE accent — cyan */
  --accent-dim:#0e7490;   /* hover-darkened accent / underline glow */
  --warm:      #f59e0b;   /* secondary, used SPARINGLY (highlight only) */

  /* Semantic — kept for legacy classes */
  --primary-color:   var(--ink);
  --secondary-color: var(--accent);
  --accent-color:    var(--accent);
  --text-color:      var(--body);
  --light-text:      var(--dim);
  --bg-color:        var(--bg);
  --bg-gradient-end: var(--bg);          /* kill the gradient body bg */
  --card-bg:         var(--panel);
  --border-color:    var(--rule);
  --shadow:          0 8px 24px rgba(0,0,0,0.5);
  --shadow-sm:       0 2px 8px rgba(0,0,0,0.35);

  /* Code blocks */
  --code-bg:    var(--panel);
  --code-text:  var(--accent);
  --pre-bg:     var(--panel);

  /* Post layout */
  --post-bg:           var(--bg);
  --post-text:         var(--body);
  --post-heading:      var(--ink);
  --post-subheading:   var(--ink);
  --post-meta-text:    var(--dim);
  --post-meta-bg:      var(--panel);
  --post-border:       var(--rule);
  --post-footer-btn-bg: var(--panel);
  --post-footer-btn-text: var(--ink);
  --blockquote-bg:     var(--panel);
  --blockquote-border: var(--accent);
  --blockquote-text:   var(--body);

  /* Problem cards */
  --problem-card-bg:    var(--panel);
  --problem-title-color: var(--ink);
  --problem-sub-text:   var(--dim);

  /* Sidebar */
  --sidebar-bg: var(--panel);

  /* Footer */
  --footer-link:    var(--body);
  --footer-subtext: var(--dim);

  /* Type */
  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, 'Menlo', monospace;
}

html, body {
  font-family: var(--font-sans);
  background: var(--bg);  /* solid, no gradient */
  color: var(--body);
}
```

Add to `<head>` in `_layouts/default.html` (after viewport meta):

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

---

## 2. Global header (`_layouts/default.html`)

Replace the `<header class="site-header">` block with this structure (keep the Liquid loops intact — only the markup and class names change):

```html
<header class="site-header">
  <div class="site-header-inner">
    <a href="{{ '/' | relative_url }}" class="brand" aria-label="ajdevhub home">
      <svg class="brand-mark" width="22" height="22" viewBox="0 0 22 22" aria-hidden="true">
        <rect x="1" y="1" width="20" height="20" stroke="var(--accent)" stroke-opacity="0.4" fill="none"/>
        <rect x="5" y="5" width="12" height="12" stroke="var(--accent)" fill="none"/>
        <circle cx="11" cy="11" r="2" fill="var(--accent)"/>
      </svg>
      <span class="brand-name">ajdevhub</span>
    </a>

    <nav class="site-nav">
      {% assign cur = page.url | default: '/' %}
      <a href="{{ '/' | relative_url }}" class="{% if cur == '/' or cur == '' %}active{% endif %}">Home</a>
      <a href="{{ '/learning' | relative_url }}" class="{% if cur contains '/learning' %}active{% endif %}">Learning</a>
      <a href="{{ '/problems' | relative_url }}" class="{% if cur contains '/problems' %}active{% endif %}">Problems</a>
      <a href="{{ '/roadmap' | relative_url }}" class="{% if cur contains '/roadmap' %}active{% endif %}">Roadmap</a>
      <a href="{{ '/projects' | relative_url }}" class="{% if cur contains '/projects' %}active{% endif %}">Projects</a>
      <a href="{{ '/blogs' | relative_url }}" class="{% if cur contains '/blogs' %}active{% endif %}">Blogs</a>
      <a href="{{ '/about' | relative_url }}" class="{% if cur contains '/about' %}active{% endif %}">About</a>
    </nav>

    <div class="header-meta">
      <div id="global-search-wrapper">
        <input type="text" id="global-search-input" class="search-chip" placeholder="Search  ⌘K" autocomplete="off">
        <ul id="global-results-container"></ul>
      </div>
    </div>
  </div>
</header>
```

CSS to add (replace the existing header CSS — the gradient header, gradient wordmark, hover underline, etc. all go away):

```css
.site-header {
  background: var(--bg);
  border-bottom: 1px solid var(--rule);
  padding: 0;
  box-shadow: none;
}
.site-header-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 18px 32px;
  display: flex; align-items: center; gap: 32px;
}
.brand {
  display: flex; align-items: center; gap: 10px;
  text-decoration: none;
}
.brand-mark { flex-shrink: 0; }
.brand-name {
  color: var(--ink); font-size: 15px; font-weight: 600;
  letter-spacing: -0.2px;
}
.site-nav {
  display: flex; gap: 26px;
  font-family: var(--font-sans);
  font-size: 13px;
}
.site-nav a {
  color: var(--body); text-decoration: none; font-weight: 500;
  transition: color 0.15s;
}
.site-nav a::after { display: none; }   /* kill the underline animation */
.site-nav a:hover { color: var(--ink); }
.site-nav a.active { color: var(--accent); font-weight: 600; }
.header-meta { margin-left: auto; }
.search-chip {
  background: transparent;
  border: 1px solid var(--rule);
  color: var(--body);
  padding: 6px 14px;
  font-family: var(--font-mono);
  font-size: 11.5px;
  border-radius: 0;
  width: 200px;
}
.search-chip::placeholder { color: var(--dim); }
.search-chip:focus { outline: none; border-color: var(--accent); }
```

Also: **remove the `🐙` and `💼` emoji** from the footer social buttons in `_layouts/default.html`. Replace with simple text links:

```html
<div class="footer-socials">
  <a href="https://github.com/Ajay3007" target="_blank" rel="noopener noreferrer" class="footer-social-link">GitHub</a>
  <a href="https://linkedin.com/in/ajay-gupt" target="_blank" rel="noopener noreferrer" class="footer-social-link">LinkedIn</a>
</div>
```

CSS:
```css
.footer-social-link {
  color: var(--body); text-decoration: none;
  font-family: var(--font-mono); font-size: 12px;
  border: 1px solid var(--rule); padding: 6px 14px;
  margin-right: 8px; transition: border-color 0.15s, color 0.15s;
}
.footer-social-link:hover { color: var(--accent); border-color: var(--accent); }
```

---

## 3. Home page (`index.md`)

Replace the entire body of `index.md` (keep the front-matter) with the structure below. The hero canvas animation is the signature visual — ship it as plain `<canvas>` + a small JS file.

```markdown
---
layout: default
title: Home
custom_js: home-hero
---

<section class="c-hero">
  <div class="c-hero-grid">
    <div class="c-hero-text">
      <div class="c-eyebrow">
        <span class="c-dot"></span>
        ENGINEER · DATA PLANE · BENGALURU
      </div>
      <h1 class="c-hero-title">
        I make packets<br>
        move <span class="c-hl">fast</span>, and<br>
        write about <em>why.</em>
      </h1>
      <p class="c-hero-lede">
        Ajay Kumar Gupt — Manager &amp; SDE at Jio Platforms.
        Four years on DPDK, VPP and Hyperscan, building deep packet
        inspection for SASE. This site is my notebook in public.
      </p>
      <div class="c-hero-cta">
        <a href="{{ '/projects' | relative_url }}" class="c-btn-primary">Featured projects →</a>
        <a href="{{ '/about' | relative_url }}" class="c-btn-ghost">About me</a>
      </div>
    </div>

    <div class="c-hero-viz">
      <div class="c-viz-head">
        <span>pipeline · sase.dpi</span>
        <span><span class="c-dot"></span> synthetic · illustrative</span>
      </div>
      <canvas id="packet-pipeline" width="520" height="80" aria-hidden="true"></canvas>
      <div class="c-viz-stages">
        <div><div class="c-stage-num">01</div><div class="c-stage-lbl">RX</div></div>
        <div><div class="c-stage-num">02</div><div class="c-stage-lbl">PARSE</div></div>
        <div><div class="c-stage-num">03</div><div class="c-stage-lbl">FIB</div></div>
        <div><div class="c-stage-num">04</div><div class="c-stage-lbl">DPI</div></div>
        <div><div class="c-stage-num">05</div><div class="c-stage-lbl">TX</div></div>
      </div>
      <div class="c-viz-metrics">
        <div><div class="c-metric-k">THROUGHPUT</div><div class="c-metric-v">8.2 Mpps</div></div>
        <div><div class="c-metric-k">P99 LATENCY</div><div class="c-metric-v">1.31 μs</div></div>
        <div><div class="c-metric-k">DPI MATCHES</div><div class="c-metric-v">412 / s</div></div>
      </div>
    </div>
  </div>
</section>

<section class="c-section">
  <div class="c-section-head">
    <div>
      <div class="c-kicker">// SHIPPED</div>
      <h2 class="c-section-title">Selected projects.</h2>
    </div>
    <a href="{{ '/projects' | relative_url }}" class="c-section-action">View all →</a>
  </div>
  <div class="c-card-grid c-cols-3">
    {% for project in site.projects limit: 3 %}
    <a href="{{ project.url | relative_url }}" class="c-card">
      <div class="c-card-meta">
        <span>№ {{ forloop.index | prepend: "0" | slice: -2, 2 }}</span>
        <span>{{ project.year | default: "" }}</span>
      </div>
      <h3 class="c-card-title"><span class="c-card-slash">~/</span>{{ project.title }}</h3>
      {% if project.description %}<p class="c-card-desc">{{ project.description }}</p>{% endif %}
      {% if project.tags %}
      <div class="c-tag-row">
        {% for tag in project.tags %}<span class="c-tag">{{ tag }}</span>{% endfor %}
      </div>
      {% endif %}
    </a>
    {% endfor %}
  </div>
</section>

<section class="c-section">
  <div class="c-section-head">
    <div>
      <div class="c-kicker">// LATEST</div>
      <h2 class="c-section-title">From the journal.</h2>
    </div>
    <a href="{{ '/blogs' | relative_url }}" class="c-section-action">Archive →</a>
  </div>
  <div class="c-post-list">
    {% for post in site.posts limit: 5 %}
    <a href="{{ post.url | relative_url }}" class="c-post-row">
      <span class="c-post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      <span class="c-post-title">{{ post.title }}</span>
      <span class="c-post-cat">{{ post.categories | first | default: "general" }}</span>
      <span class="c-post-arrow">→</span>
    </a>
    {% endfor %}
  </div>
</section>

<section class="c-section">
  <div class="c-section-head">
    <div>
      <div class="c-kicker">// NOTEBOOK</div>
      <h2 class="c-section-title">Topics I'm learning.</h2>
    </div>
    <a href="{{ '/learning' | relative_url }}" class="c-section-action">Browse all →</a>
  </div>
  <div class="c-card-grid c-cols-5">
    {% assign topics = "data-plane,system-design,networking,dsa,4g-5g,operating-systems,oop,programming-language,ai-ml,competitive-programming" | split: "," %}
    {% assign labels  = "Data Plane,System Design,Networking,DSA & Algorithms,4G / 5G,Operating Systems,OOP & Patterns,Languages,AI / ML,Competitive Prog." | split: "," %}
    {% assign notes   = "DPDK, VPP, line-rate processing|Architecture, scale, tradeoffs|TCP/IP, routing, protocols|Patterns, structures, proofs|RAN, AS/NAS, user plane|Memory, scheduling, IPC|SOLID, design patterns|C, C++, Java, Python|Foundations, models|Patterns & contests" | split: "|" %}
    {% for slug in topics %}
    <a href="{{ '/learning/' | append: slug | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta">
        <span>{{ forloop.index | prepend: "0" | slice: -2, 2 }}</span>
      </div>
      <div class="c-topic-name">{{ labels[forloop.index0] }}</div>
      <div class="c-topic-note">{{ notes[forloop.index0] }}</div>
    </a>
    {% endfor %}
  </div>
</section>
```

### CSS for the home page (append to `assets/css/main.css`)

```css
/* ─────────────────────────────────────────────────────────────
   Direction C — shared component CSS
   ───────────────────────────────────────────────────────────── */

.site-main { max-width: 1200px; padding: 0; }   /* override the 900px / 3rem padding */

.c-hero {
  padding: 64px 32px 56px;
  border-bottom: 1px solid var(--rule);
  background-image:
    radial-gradient(circle at 18% 30%, var(--panel-2) 0%, transparent 50%),
    linear-gradient(var(--faint) 1px, transparent 1px),
    linear-gradient(90deg, var(--faint) 1px, transparent 1px);
  background-size: auto, 48px 48px, 48px 48px;
}
.c-hero-grid {
  display: grid; grid-template-columns: 1.1fr 1fr; gap: 48px;
  align-items: center; max-width: 1200px; margin: 0 auto;
}
.c-eyebrow {
  font-family: var(--font-mono); font-size: 11px; color: var(--accent);
  letter-spacing: 2px; margin-bottom: 22px;
  display: flex; align-items: center; gap: 10px;
}
.c-dot {
  width: 6px; height: 6px; background: var(--accent); border-radius: 50%;
  box-shadow: 0 0 12px var(--accent);
}
.c-hero-title {
  font-size: 52px; line-height: 1.06; font-weight: 700;
  color: var(--ink); margin: 0; letter-spacing: -1.2px;
}
.c-hl {
  background: linear-gradient(180deg, transparent 65%, var(--accent-dim) 65%);
  padding: 0 6px;
}
.c-hero-title em { color: var(--accent); font-style: normal; }
.c-hero-lede {
  color: var(--body); font-size: 16px; line-height: 1.7;
  max-width: 500px; margin: 26px 0 0;
}
.c-hero-cta { display: flex; gap: 14px; margin-top: 30px; }
.c-btn-primary, .c-btn-ghost {
  font-size: 13px; font-weight: 600; padding: 11px 20px;
  text-decoration: none; transition: opacity 0.15s, border-color 0.15s, color 0.15s;
}
.c-btn-primary { background: var(--accent); color: #06080d; }
.c-btn-primary:hover { opacity: 0.85; }
.c-btn-ghost { border: 1px solid var(--rule); color: var(--ink); }
.c-btn-ghost:hover { border-color: var(--accent); color: var(--accent); }

/* Hero packet visualization */
.c-hero-viz {
  background: var(--panel); border: 1px solid var(--rule);
  padding: 22px;
}
.c-viz-head {
  display: flex; justify-content: space-between;
  font-family: var(--font-mono); font-size: 10.5px; color: var(--dim);
  margin-bottom: 16px;
}
#packet-pipeline { width: 100%; height: 80px; display: block; }
.c-viz-stages {
  display: flex; justify-content: space-between; padding: 0 4%; margin-top: 8px;
}
.c-viz-stages > div { text-align: center; }
.c-stage-num {
  width: 32px; height: 32px; margin: 0 auto;
  border: 1.5px solid var(--accent); color: var(--accent);
  font-family: var(--font-mono); font-size: 9.5px; font-weight: 600;
  display: flex; align-items: center; justify-content: center;
  background: var(--bg);
}
.c-stage-lbl {
  font-family: var(--font-mono); font-size: 9.5px; color: var(--body);
  margin-top: 6px; letter-spacing: 1px;
}
.c-viz-metrics {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;
  margin-top: 20px; padding-top: 18px; border-top: 1px solid var(--rule);
}
.c-metric-k { font-family: var(--font-mono); font-size: 9.5px; color: var(--dim); letter-spacing: 1px; }
.c-metric-v { color: var(--ink); font-size: 18px; font-weight: 600; margin-top: 4px; }

/* Sections */
.c-section {
  padding: 48px 32px; max-width: 1200px; margin: 0 auto;
  border-bottom: 1px solid var(--rule);
}
.c-section-head {
  display: flex; align-items: flex-end; margin-bottom: 28px;
}
.c-kicker {
  font-family: var(--font-mono); font-size: 11px; color: var(--accent);
  letter-spacing: 2px; margin-bottom: 8px;
}
.c-section-title {
  font-size: 28px; font-weight: 700; color: var(--ink);
  margin: 0; letter-spacing: -0.6px;
}
.c-section-action {
  margin-left: auto; font-size: 13px; color: var(--accent);
  text-decoration: none; font-weight: 500;
}
.c-section-action:hover { text-decoration: underline; }

/* Cards (single canonical .c-card pattern) */
.c-card-grid { display: grid; gap: 14px; }
.c-cols-3 { grid-template-columns: repeat(3, 1fr); }
.c-cols-5 { grid-template-columns: repeat(5, 1fr); }
.c-card {
  background: var(--panel); border: 1px solid var(--rule);
  padding: 22px 20px; text-decoration: none; color: inherit;
  transition: border-color 0.15s, transform 0.15s;
  display: block;
}
.c-card:hover { border-color: var(--accent); }
.c-card-meta {
  font-family: var(--font-mono); font-size: 10.5px; color: var(--dim);
  letter-spacing: 1.5px; display: flex; justify-content: space-between;
}
.c-card-title {
  color: var(--ink); font-size: 20px; font-weight: 600;
  margin: 18px 0 10px; letter-spacing: -0.3px;
}
.c-card-slash { color: var(--accent); }
.c-card-desc { color: var(--body); font-size: 13.5px; line-height: 1.6; margin: 0; }
.c-tag-row { margin-top: 18px; display: flex; gap: 6px; flex-wrap: wrap; }
.c-tag {
  font-family: var(--font-mono); font-size: 10.5px; color: var(--body);
  background: var(--panel-2); padding: 3px 8px;
}

/* Topic / learning cards */
.c-topic-card {
  background: var(--panel); border: 1px solid var(--rule);
  padding: 16px 14px; text-decoration: none; min-height: 120px;
  display: block; transition: border-color 0.15s;
}
.c-topic-card:hover { border-color: var(--accent); }
.c-topic-meta {
  font-family: var(--font-mono); font-size: 10px; color: var(--dim);
  letter-spacing: 1.5px; margin-bottom: 8px;
}
.c-topic-name { color: var(--ink); font-size: 13px; font-weight: 600; line-height: 1.25; }
.c-topic-note { color: var(--dim); font-size: 11.5px; margin-top: 6px; line-height: 1.5; }

/* Posts list */
.c-post-list { display: flex; flex-direction: column; }
.c-post-row {
  display: grid; grid-template-columns: 110px 1fr 110px 30px;
  gap: 24px; padding: 16px 0; align-items: center;
  border-top: 1px solid var(--rule); text-decoration: none; color: inherit;
}
.c-post-row:last-child { border-bottom: 1px solid var(--rule); }
.c-post-row:hover .c-post-title { color: var(--accent); }
.c-post-date { font-family: var(--font-mono); font-size: 11.5px; color: var(--dim); }
.c-post-title { color: var(--ink); font-size: 15px; font-weight: 500; transition: color 0.15s; }
.c-post-cat {
  font-family: var(--font-mono); font-size: 10.5px; color: var(--accent);
  letter-spacing: 1px; text-transform: uppercase;
}
.c-post-arrow { color: var(--dim); text-align: right; }

/* Responsive */
@media (max-width: 960px) {
  .c-hero-grid { grid-template-columns: 1fr; }
  .c-hero-title { font-size: 40px; }
  .c-cols-3 { grid-template-columns: 1fr; }
  .c-cols-5 { grid-template-columns: repeat(2, 1fr); }
}
```

### Hero canvas animation — `assets/js/home-hero.js` (NEW FILE)

```js
// Animated packet flowing across the data-plane pipeline.
// Resolution-independent; respects prefers-reduced-motion.
(function () {
  const canvas = document.getElementById('packet-pipeline');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  let dpr = window.devicePixelRatio || 1;
  let cssW = 0, cssH = 0;

  function resize() {
    const rect = canvas.getBoundingClientRect();
    cssW = rect.width; cssH = rect.height;
    canvas.width  = Math.floor(cssW * dpr);
    canvas.height = Math.floor(cssH * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  const ACCENT = '#22d3ee';
  const FAINT  = '#2a3142';

  let t0 = performance.now();
  const PERIOD = 3600; // ms per traverse
  const TRAIL  = 6;

  function frame(now) {
    const w = cssW, h = cssH;
    if (!w || !h) { requestAnimationFrame(frame); return; }
    const cy = h / 2;
    const x0 = w * 0.06, x1 = w * 0.94;

    ctx.clearRect(0, 0, w, h);

    // Track (dashed)
    ctx.strokeStyle = FAINT;
    ctx.lineWidth = 1;
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(x0, cy);
    ctx.lineTo(x1, cy);
    ctx.stroke();
    ctx.setLineDash([]);

    // Packet position (eased ping-pong)
    const phase = ((now - t0) % PERIOD) / PERIOD;
    const tri = phase < 0.5 ? phase * 2 : (1 - phase) * 2; // 0..1..0
    const eased = tri * tri * (3 - 2 * tri); // smoothstep
    const px = x0 + (x1 - x0) * eased;

    // Trail
    for (let i = TRAIL; i >= 1; i--) {
      const back = px - (i * 8);
      if (back < x0) continue;
      ctx.fillStyle = ACCENT;
      ctx.globalAlpha = (TRAIL - i + 1) / (TRAIL * 3);
      ctx.beginPath();
      ctx.arc(back, cy, 3, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1;

    // Glow
    ctx.fillStyle = ACCENT;
    ctx.shadowColor = ACCENT;
    ctx.shadowBlur = 10;
    ctx.beginPath();
    ctx.arc(px, cy, 4.5, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    if (!reduce) requestAnimationFrame(frame);
  }

  resize();
  window.addEventListener('resize', resize);
  if (reduce) {
    // Draw a single static frame mid-pipeline.
    t0 = performance.now() - PERIOD / 4;
    frame(performance.now());
  } else {
    requestAnimationFrame(frame);
  }
})();
```

The `custom_js: home-hero` front-matter on `index.md` triggers the existing loader in `_layouts/default.html` which appends `<script src="/assets/js/home-hero.js" defer>`. No layout change needed for this part.

### Remove from `index.md`

Delete the existing `<section class="hero-section">` (typed-text effect), the `<section class="modern-section">` for "By The Numbers", "Featured Projects" old version, "DSA Hub Showcase", "Learning Paths", "Recent Thoughts", and "About This Site". The new structure above replaces all of them. Also delete `assets/js/typing.js` from the load order in `default.html` and the file itself — the typed hero is gone.

---

## 4. About page (`about.md`)

Replace the entire body (keep front-matter) with:

```markdown
---
layout: default
title: About
---

<section class="c-about-hero">
  <div class="c-about-grid">
    <div>
      <div class="c-kicker">// ABOUT</div>
      <h1 class="c-about-title">
        Ajay Kumar Gupt.<br>
        Engineer who reads<br>
        <span class="c-accent">man pages</span> for fun.
      </h1>
      <p class="c-about-lede">
        Four-plus years building packet-processing pipelines for SASE —
        deep packet inspection, real-time threat detection, and the
        unglamorous plumbing that keeps traffic moving at line rate.
        Day job is C/C++ and DPDK. Off-hours, I write here so I learn
        faster and forget less.
      </p>
    </div>

    <aside class="c-whoami">
      <div class="c-whoami-head">~/whoami</div>
      <table class="c-whoami-table">
        <tbody>
          <tr><td>role</td><td>Manager, SDE</td></tr>
          <tr><td>org</td><td>Jio Platforms</td></tr>
          <tr><td>loc</td><td>Bengaluru, IN</td></tr>
          <tr><td>focus</td><td>data plane</td></tr>
          <tr><td>tenure</td><td>4+ yrs</td></tr>
          <tr><td>status</td><td>open to talk</td></tr>
        </tbody>
      </table>
    </aside>
  </div>
</section>

<section class="c-section">
  <div class="c-section-head">
    <div>
      <div class="c-kicker">// TIMELINE</div>
      <h2 class="c-section-title">Where the work has happened.</h2>
    </div>
  </div>
  <div class="c-timeline">
    <div class="c-timeline-row">
      <span class="c-timeline-when">2022 — now</span>
      <span class="c-timeline-role">Manager, SDE @ Jio Platforms</span>
      <span class="c-timeline-note">SASE / DPI / DPDK pipelines, ultra-low-latency security.</span>
    </div>
    <div class="c-timeline-row">
      <span class="c-timeline-when">2020 — 2022</span>
      <span class="c-timeline-role">Software Engineer</span>
      <span class="c-timeline-note">5G core backend, Aerospike clusters, Redis caching.</span>
    </div>
    <div class="c-timeline-row">
      <span class="c-timeline-when">2019 — 2020</span>
      <span class="c-timeline-role">Engineer (Intern)</span>
      <span class="c-timeline-note">Networking R&amp;D, packet capture &amp; analysis tooling.</span>
    </div>
  </div>
</section>

<section class="c-section">
  <div class="c-section-head">
    <div>
      <div class="c-kicker">// STACK</div>
      <h2 class="c-section-title">What I work in.</h2>
    </div>
  </div>
  <div class="c-card-grid c-cols-4">
    <div class="c-stack-card">
      <div class="c-stack-key">core/</div>
      <div>· DPDK</div><div>· VPP</div><div>· Hyperscan</div><div>· Linux perf</div>
    </div>
    <div class="c-stack-card">
      <div class="c-stack-key">lang/</div>
      <div>· C / C++</div><div>· Java</div><div>· Python</div><div>· Go</div>
    </div>
    <div class="c-stack-card">
      <div class="c-stack-key">infra/</div>
      <div>· Aerospike</div><div>· Redis</div><div>· 5G core</div><div>· DPI / SASE</div>
    </div>
    <div class="c-stack-card">
      <div class="c-stack-key">tools/</div>
      <div>· perf, ftrace</div><div>· eBPF</div><div>· git, cmake</div><div>· make</div>
    </div>
  </div>
</section>
```

CSS to append:

```css
.c-about-hero {
  padding: 56px 32px; max-width: 1200px; margin: 0 auto;
  border-bottom: 1px solid var(--rule);
}
.c-about-grid {
  display: grid; grid-template-columns: 1.4fr 1fr; gap: 48px;
}
.c-about-title {
  font-size: 44px; line-height: 1.08; font-weight: 700;
  color: var(--ink); margin: 0; letter-spacing: -1.2px;
}
.c-about-title .c-accent { color: var(--accent); }
.c-about-lede {
  color: var(--body); font-size: 16px; line-height: 1.75;
  max-width: 540px; margin: 26px 0 0;
}
.c-whoami {
  background: var(--panel); border: 1px solid var(--rule); padding: 22px;
  height: fit-content;
}
.c-whoami-head {
  font-family: var(--font-mono); font-size: 10.5px; color: var(--dim);
  letter-spacing: 1.5px; margin-bottom: 12px;
}
.c-whoami-table { width: 100%; font-size: 13px; border-collapse: collapse; }
.c-whoami-table td {
  padding: 8px 0; border-bottom: 1px solid var(--rule);
}
.c-whoami-table td:first-child {
  color: var(--dim); font-family: var(--font-mono); font-size: 11px;
}
.c-whoami-table td:last-child { color: var(--ink); text-align: right; }

.c-timeline { border-top: 1px solid var(--rule); }
.c-timeline-row {
  display: grid; grid-template-columns: 180px 1fr 1.5fr;
  gap: 28px; padding: 18px 0; align-items: baseline;
  border-bottom: 1px solid var(--rule);
}
.c-timeline-when { font-family: var(--font-mono); color: var(--accent); font-size: 13px; }
.c-timeline-role { color: var(--ink); font-size: 15px; font-weight: 600; }
.c-timeline-note { color: var(--body); font-size: 14px; }

.c-cols-4 { grid-template-columns: repeat(4, 1fr); }
.c-stack-card {
  background: var(--panel); border: 1px solid var(--rule);
  padding: 18px;
}
.c-stack-card > div { color: var(--ink); font-size: 13px; padding: 3px 0; }
.c-stack-key {
  font-family: var(--font-mono); color: var(--accent); font-size: 11px;
  letter-spacing: 1.5px; margin-bottom: 10px;
}

@media (max-width: 960px) {
  .c-about-grid { grid-template-columns: 1fr; }
  .c-about-title { font-size: 34px; }
  .c-cols-4 { grid-template-columns: repeat(2, 1fr); }
  .c-timeline-row { grid-template-columns: 1fr; gap: 4px; }
}
```

Strip every emoji from `about.md` body content. Section titles like `## 🚀 Current Role` should not exist anymore — the new structure replaces them.

---

## 5. Blog post layout (`_layouts/post.html`)

Replace its body with:

```html
---
layout: default
---

<article class="c-post">
  <header class="c-post-header">
    <div class="c-kicker">
      // {% if page.categories %}{{ page.categories | join: " · " | upcase }}{% else %}WRITING{% endif %}
    </div>
    <h1 class="c-post-h1">{{ page.title }}</h1>
    <div class="c-post-meta">
      <span>{{ page.date | date: "%Y-%m-%d" }}</span>
      <span class="c-meta-sep">│</span>
      {% assign words = content | number_of_words %}
      {% assign reading_time = words | divided_by: 200 | plus: 1 %}
      <span>{{ reading_time }} min read</span>
      <span class="c-meta-sep">│</span>
      <span>~{{ words }} words</span>
    </div>
  </header>

  <div class="c-post-body">
    {{ content }}
  </div>

  <footer class="c-post-footer">
    <a href="{{ '/blogs/' | relative_url }}" class="c-btn-ghost">← Back to archive</a>
  </footer>
</article>
```

CSS to append (also: **delete** any conflicting rules in `main.css` for `.post`, `.post-header`, `.post-hero-header`, `.post-meta-chip`, `.post-end-label`, `.post-back-btn` etc. — they're from the old design):

```css
.c-post { max-width: 760px; margin: 56px auto; padding: 0 32px; }
.c-post-h1 {
  font-size: 40px; line-height: 1.1; font-weight: 700;
  color: var(--ink); margin: 0 0 22px; letter-spacing: -1px;
}
.c-post-meta {
  padding: 14px 0; border-top: 1px solid var(--rule);
  border-bottom: 1px solid var(--rule);
  display: flex; gap: 18px; font-family: var(--font-mono);
  font-size: 12px; color: var(--dim);
}
.c-meta-sep { color: var(--faint); }
.c-post-body {
  color: var(--body); font-size: 16px; line-height: 1.8;
  margin-top: 32px;
}
.c-post-body h2 {
  font-size: 22px; color: var(--ink); font-weight: 600;
  margin: 36px 0 14px; letter-spacing: -0.3px;
}
.c-post-body h3 {
  font-size: 18px; color: var(--ink); font-weight: 600;
  margin: 28px 0 12px;
}
.c-post-body p { margin: 0 0 18px; }
.c-post-body a { color: var(--accent); text-decoration: none; border-bottom: 1px dashed var(--accent-dim); }
.c-post-body a:hover { border-bottom-style: solid; }
.c-post-body code {
  font-family: var(--font-mono); color: var(--accent);
  background: var(--panel); padding: 2px 6px; font-size: 14px;
}
.c-post-body pre {
  background: var(--panel); border: 1px solid var(--rule);
  border-left: 2px solid var(--accent);
  padding: 18px 20px; font-size: 13px; line-height: 1.75;
  overflow-x: auto; margin: 22px 0;
}
.c-post-body pre code {
  background: transparent; color: var(--ink); padding: 0;
}
.c-post-body blockquote {
  border-left: 2px solid var(--accent);
  background: var(--panel);
  padding: 14px 18px;
  margin: 22px 0; color: var(--body);
}
.c-post-body ul, .c-post-body ol { padding-left: 24px; margin: 0 0 18px; }
.c-post-body li { margin: 6px 0; }
.c-post-footer {
  margin-top: 56px; padding-top: 28px;
  border-top: 1px solid var(--rule);
}
```

---

## 6. Learning index (`_learning/index.md`)

Strip all emoji from titles. Replace the body with the same `c-section` + `c-cols-5` topic-grid structure used on the home page (see section 3). Drop the "Featured: New Addition" lozenge — if you want to highlight a topic, add a small `★ new` chip on the relevant `.c-topic-card` instead.

---

## 7. Cleanup

Delete from the repo (these are orphaned scaffolding):
- `test_style.html`
- `test-style.html`
- `prompt.md`
- `extract_log.txt`
- `extract_editorials.js`
- `fix_emojis.py`
- `assets/js/typing.js`

In `_layouts/default.html`:
- Remove the `<script>` for typing.js
- Remove the `<script>` blocks for theme toggle (init + click handler)
- Remove the `#theme-toggle` button from the header
- Keep everything else (Netlify Identity, search, scroll-to-top, custom_js loader)

In `assets/css/main.css`:
- After applying the changes above, do a search for these legacy classes and **delete** their rules: `.hero-section`, `.hero-title`, `.hero-subtitle`, `.hero-typed-text`, `.hero-typed-cursor`, `.hero-actions`, `.modern-section`, `.section-title`, `.stats-grid`, `.stat-card`, `.stat-number`, `.stat-label`, `.featured-project-card`, `.featured-project-title`, `.featured-project-desc`, `.featured-project-link`, `.dsa-hub-card`, `.dsa-stats`, `.dsa-stat-box`, `.nav-grid`, `.nav-card`, `.nav-card-title`, `.nav-card-desc`, `.btn-primary`, `.btn-secondary` (replace with `.c-btn-primary`/`.c-btn-ghost` site-wide), `.theme-toggle`, `.home-top`, `.hf-tabs`, `.hf-tab`, `.blog-hero`. They've all been replaced.

In `index.md`, `about.md`, `_learning/index.md`, `projects.md`, and any layout file: search-and-replace `btn-primary` → `c-btn-primary`, `btn-secondary` → `c-btn-ghost`.

Strip emoji from: nav labels (none — already clean), section titles in all `.md` files, footer "Connect" buttons, all `_layouts/*.html` files. Inside actual prose paragraphs of blog posts (`_posts/*.md`), leave emoji alone unless they were obviously decorative section headers.

**Do not touch** (out of scope for this pass):
- `assets/css/sd-module-*.css` and `assets/js/sd-module-*.js` — system design module pages, isolated visual language.
- `assets/css/dsa-*.css`, `assets/css/ai-ml-roadmap.css`, `assets/css/backend-roadmap.css`, `assets/css/roadmap-hub.css`, `assets/css/system-design-roadmap.css` and their JS — roadmap pages, can migrate later.
- `_editorials/*` content.
- `admin/` (Decap CMS) — works as-is.
- Post body content in `_posts/*.md`.
- `search.json`, `_config.yml` plugins, Gemfile.

---

## 8. Acceptance checklist

When done, verify:

1. Home page loads with the dark navy bg, packet animation visible in the hero, no light-theme flash on load.
2. No emoji visible in the global header, nav, footer, hero, or section titles on Home / About / Learning index.
3. Theme toggle button is gone from the header.
4. All four template types render cleanly:
   - `/` (home)
   - `/about/`
   - `/learning/`
   - any blog post URL e.g. `/blog/2025/01/05/two-pointer-technique/`
5. The single accent color (`#22d3ee`) is the only chromatic accent used. No pinks, no purples, no greens, no oranges except the rare `--warm` highlight (which should not appear on these four pages).
6. `prefers-reduced-motion: reduce` freezes the packet at mid-pipeline instead of animating.
7. Mobile viewport (≤960px): hero stacks, card grids collapse to 1–2 columns, nothing overflows.
8. The legacy `sd-module-*` and `dsa-roadmap` pages still load (they may look stylistically off vs. the new shell — that's expected, future-pass work).

Once all 8 are green, you're done. Commit as one PR titled "Redesign: Direction C — dark, signal-led, type-first" with a brief summary of the file list above.
