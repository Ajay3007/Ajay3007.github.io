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
        ENGINEER · DATA PLANE · NAVI MUMBAI
      </div>
      <h1 class="c-hero-title">
        I make packets<br>
        move <span class="c-hl">fast</span>, and<br>
        write about <em>why.</em>
      </h1>
      <p class="c-hero-lede">
        Ajay Kumar Gupt — Software Engineer at Jio Platforms.
        Five years on DPDK, VPP and Hyperscan, building deep packet
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
