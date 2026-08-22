---
title: "VPP Mastery"
description: "DATA PLANE FD.io VPP DPDK 3–4 MONTHS 5 PHASES · 9 PROJECTS ⚡ VPP Mastery A structured, hands-on curriculum for engineers who want to go deep on FD.io Vector Packet Processor -…"
domain: data-plane
track: vpp
order: 0
ownHeader: true
url: /learning/data-plane/vpp/
---

<style>
/* ── VPP Hub Styles ─────────────────────────────────────────── */
.vpp-hero {
  background: linear-gradient(135deg, #0d1b2a 0%, #1a3a5c 60%, #1a7a6e 100%);
  border-radius: 12px;
  padding: 2.5rem 2rem;
  margin-bottom: 2rem;
  color: #fff;
  position: relative;
  overflow: hidden;
}
.vpp-hero::before {
  content: '';
  position: absolute;
  top: -40px; right: -40px;
  width: 200px; height: 200px;
  border-radius: 50%;
  background: rgba(26,122,110,0.18);
}
.vpp-hero-badge {
  display: inline-flex;
  gap: .5rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
}
.vpp-badge {
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.2);
  border-radius: 20px;
  padding: 3px 12px;
  font-size: .75rem;
  font-family: monospace;
  color: #a8d4f0;
  letter-spacing: .04em;
}
.vpp-hero h1 {
  font-size: 2.4rem;
  font-weight: 800;
  margin: .5rem 0;
  letter-spacing: -.02em;
  color: #fff;
  border: none;
}
.vpp-hero p {
  font-size: 1rem;
  color: #c8dff0;
  max-width: 640px;
  line-height: 1.6;
  margin-bottom: 1.2rem;
}
.vpp-stats {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  margin-top: 1.2rem;
}
.vpp-stat { text-align: center; }
.vpp-stat-num {
  font-size: 1.8rem;
  font-weight: 800;
  color: #5dd6c8;
  display: block;
  line-height: 1;
}
.vpp-stat-lbl {
  font-size: .72rem;
  color: #90bcd4;
  text-transform: uppercase;
  letter-spacing: .06em;
}
.vpp-cta {
  display: inline-block;
  background: #1a7a6e;
  color: #fff !important;
  border-radius: 8px;
  padding: .55rem 1.4rem;
  font-weight: 700;
  font-size: .9rem;
  text-decoration: none !important;
  margin-top: 1rem;
  transition: background .2s;
}
.vpp-cta:hover { background: #22998a; }

/* Phase cards */
.phase-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.2rem;
  margin: 1.5rem 0;
}
.phase-card {
  border-radius: 10px;
  border: 1.5px solid var(--border-color, #e0e0e0);
  background: var(--card-bg, #fff);
  overflow: hidden;
  transition: box-shadow .2s, transform .2s;
}
.phase-card:hover {
  box-shadow: 0 6px 24px rgba(0,0,0,.1);
  transform: translateY(-2px);
}
.phase-card-header {
  padding: .9rem 1.2rem;
  display: flex;
  align-items: center;
  gap: .8rem;
}
.phase-num {
  width: 36px; height: 36px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-weight: 800; font-size: 1rem; color: #fff;
  flex-shrink: 0;
}
.phase-card-header h3 {
  margin: 0;
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-color, #222);
  border: none;
}
.phase-meta {
  font-size: .72rem;
  color: var(--light-text, #666);
  font-family: monospace;
}
.phase-card-body {
  padding: .8rem 1.2rem 1rem;
  border-top: 1px solid var(--border-color, #eee);
}
.phase-card-body p {
  font-size: .88rem;
  color: var(--text-color, #333);
  line-height: 1.6;
  margin: 0 0 .8rem;
}
.module-links { display: flex; flex-direction: column; gap: .35rem; }
.module-link {
  display: flex;
  align-items: center;
  gap: .5rem;
  padding: .35rem .6rem;
  border-radius: 6px;
  background: var(--bg-color, #f8f8f8);
  font-size: .83rem;
  color: var(--text-color, #333);
  text-decoration: none !important;
  border: 1px solid var(--border-color, #e8e8e8);
  transition: background .15s;
}
.module-link:hover { background: var(--card-bg, #fff); }
.module-link .ml-icon { font-size: .9rem; }
.module-link .ml-text { flex: 1; font-weight: 500; }
.module-link .ml-tag {
  font-size: .68rem;
  font-family: monospace;
  background: rgba(0,0,0,.06);
  border-radius: 4px;
  padding: 1px 6px;
  color: var(--light-text, #666);
}

/* Tech tags */
.tech-tags { display: flex; flex-wrap: wrap; gap: .4rem; margin: 1rem 0; }
.tech-tag {
  padding: 3px 10px;
  border-radius: 12px;
  font-size: .75rem;
  font-family: monospace;
  font-weight: 600;
  background: #e8f4fd;
  color: #1a5c8c;
  border: 1px solid #b8d8f0;
}
[data-theme="dark"] .tech-tag {
  background: #0d2a3d;
  color: #7dc4f0;
  border-color: #1a4060;
}

/* Section headings */
.hub-section-title {
  font-size: .72rem;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: var(--light-text, #888);
  font-weight: 700;
  font-family: monospace;
  margin: 2rem 0 .8rem;
  padding-bottom: .4rem;
  border-bottom: 1px solid var(--border-color, #eee);
}
</style>
<div class="vpp-hero">
  <div class="vpp-hero-badge">
    <span class="vpp-badge">DATA PLANE</span>
    <span class="vpp-badge">FD.io VPP</span>
    <span class="vpp-badge">DPDK</span>
    <span class="vpp-badge">3–4 MONTHS</span>
    <span class="vpp-badge">5 PHASES · 9 PROJECTS</span>
  </div>
  <h1>⚡ VPP Mastery</h1>
  <p>A structured, hands-on curriculum for engineers who want to go deep on <strong>FD.io Vector Packet Processor</strong> - from core architecture through plugin development and control-plane automation. Built for engineers with DPDK background, running on Docker + AMD + Mellanox.</p>
  <div class="vpp-stats">
    <div class="vpp-stat"><span class="vpp-stat-num">5</span><span class="vpp-stat-lbl">Phases</span></div>
    <div class="vpp-stat"><span class="vpp-stat-num">10</span><span class="vpp-stat-lbl">Modules</span></div>
    <div class="vpp-stat"><span class="vpp-stat-num">9</span><span class="vpp-stat-lbl">Projects</span></div>
    <div class="vpp-stat"><span class="vpp-stat-num">3–4</span><span class="vpp-stat-lbl">Months</span></div>
  </div>
  <a href="/learning/data-plane/vpp/vpp-roadmap/" class="vpp-cta">🗺️ View Full Roadmap →</a>
</div>
<div class="tech-tags">
  <span class="tech-tag">C / C++</span>
  <span class="tech-tag">DPDK</span>
  <span class="tech-tag">memif</span>
  <span class="tech-tag">TAP v2</span>
  <span class="tech-tag">vhost-user</span>
  <span class="tech-tag">AF_XDP</span>
  <span class="tech-tag">GoVPP</span>
  <span class="tech-tag">Docker</span>
  <span class="tech-tag">Mellanox mlx5</span>
  <span class="tech-tag">vppinfra</span>
  <span class="tech-tag">vlib</span>
  <span class="tech-tag">vnet</span>
</div>
<p class="hub-section-title">LEARNING PHASES</p>
<div class="phase-grid">
  <div class="phase-card">
    <div class="phase-card-header">
      <div class="phase-num" style="background:#2e6da4;">1</div>
      <div>
        <h3>Foundation &amp; Environment</h3>
        <div class="phase-meta">WEEKS 1–3 · 1 MODULE</div>
      </div>
    </div>
    <div class="phase-card-body">
      <p>Scalar vs vector processing, VPP layer taxonomy, build from source, Docker + Mellanox setup, startup.conf, vppctl CLI, first packet trace.</p>
      <div class="module-links">
        <a class="module-link" href="/learning/data-plane/vpp/module-p1-foundation/">
          <span class="ml-icon">⚡</span>
          <span class="ml-text">Foundation &amp; Environment</span>
          <span class="ml-tag">P1</span>
        </a>
      </div>
    </div>
  </div>
  <div class="phase-card">
    <div class="phase-card-header">
      <div class="phase-num" style="background:#1a7a6e;">2</div>
      <div>
        <h3>Core VPP Internals</h3>
        <div class="phase-meta">WEEKS 4–8 · 3 MODULES</div>
      </div>
    </div>
    <div class="phase-card-body">
      <p>vppinfra data structures, vlib dispatch loop and buffers, vnet interface abstraction, FIB, feature arcs, multi-threading.</p>
      <div class="module-links">
        <a class="module-link" href="/learning/data-plane/vpp/module-p2-vppinfra/">
          <span class="ml-icon">🧱</span>
          <span class="ml-text">vppinfra - Core Library</span>
          <span class="ml-tag">P2A</span>
        </a>
        <a class="module-link" href="/learning/data-plane/vpp/module-p2-vlib/">
          <span class="ml-icon">⚙️</span>
          <span class="ml-text">vlib - Graph Dispatcher</span>
          <span class="ml-tag">P2B</span>
        </a>
        <a class="module-link" href="/learning/data-plane/vpp/module-p2-vnet/">
          <span class="ml-icon">🌐</span>
          <span class="ml-text">vnet - Networking Layer</span>
          <span class="ml-tag">P2C</span>
        </a>
      </div>
    </div>
  </div>
  <div class="phase-card">
    <div class="phase-card-header">
      <div class="phase-num" style="background:#c05e1b;">3</div>
      <div>
        <h3>Interface Technologies</h3>
        <div class="phase-meta">WEEKS 9–13 · 3 MODULES</div>
      </div>
    </div>
    <div class="phase-card-body">
      <p>DPDK plugin internals, memif zero-copy shared memory, TAP v2, linux-cp, vhost-user, AF_XDP, AF_PACKET - every VPP interface type.</p>
      <div class="module-links">
        <a class="module-link" href="/learning/data-plane/vpp/module-p3-dpdk/">
          <span class="ml-icon">🔌</span>
          <span class="ml-text">DPDK Plugin Deep Dive</span>
          <span class="ml-tag">P3A</span>
        </a>
        <a class="module-link" href="/learning/data-plane/vpp/module-p3-memif/">
          <span class="ml-icon">🔗</span>
          <span class="ml-text">memif &amp; Shared Memory</span>
          <span class="ml-tag">P3B</span>
        </a>
        <a class="module-link" href="/learning/data-plane/vpp/module-p3-tap-afxdp/">
          <span class="ml-icon">🐧</span>
          <span class="ml-text">TAP · AF_XDP · vhost-user</span>
          <span class="ml-tag">P3C</span>
        </a>
      </div>
    </div>
  </div>
  <div class="phase-card">
    <div class="phase-card-header">
      <div class="phase-num" style="background:#5b3a8c;">4</div>
      <div>
        <h3>Plugin Development</h3>
        <div class="phase-meta">WEEKS 14–18 · 1 MODULE</div>
      </div>
    </div>
    <div class="phase-card-body">
      <p>Writing graph nodes, dual/quad-loop pattern, binary API (.api files), CLI commands, feature arc registration, VPP test framework.</p>
      <div class="module-links">
        <a class="module-link" href="/learning/data-plane/vpp/module-p4-plugin-dev/">
          <span class="ml-icon">🔨</span>
          <span class="ml-text">Plugin Development</span>
          <span class="ml-tag">P4</span>
        </a>
      </div>
    </div>
  </div>
  <div class="phase-card">
    <div class="phase-card-header">
      <div class="phase-num" style="background:#1e6b3c;">5</div>
      <div>
        <h3>Control Plane &amp; Advanced</h3>
        <div class="phase-meta">WEEKS 19–22+ · 2 MODULES</div>
      </div>
    </div>
    <div class="phase-card-body">
      <p>GoVPP binary API client, Stats API, vpp_papi Python bindings, observability, performance tuning, NUMA awareness, production patterns. Bonus: VPP Host Stack — TCP/Session layer, VCL, application namespaces.</p>
      <div class="module-links">
        <a class="module-link" href="/learning/data-plane/vpp/module-p5-controlplane/">
          <span class="ml-icon">🎛️</span>
          <span class="ml-text">Control Plane &amp; GoVPP</span>
          <span class="ml-tag">P5A</span>
        </a>
        <a class="module-link" href="/learning/data-plane/vpp/module-hoststack/">
          <span class="ml-icon">🌐</span>
          <span class="ml-text">Host Stack — TCP &amp; Session Layers</span>
          <span class="ml-tag">P5B · Bonus</span>
        </a>
      </div>
    </div>
  </div>
</div>
<p class="hub-section-title">MINI-PROJECTS OVERVIEW</p>

| # | Project | Phase | Core Skill |
|---|---------|-------|------------|
| 1 | VPP Container Lab - First Packet | P1 | Build, startup.conf, packet trace |
| 2 | Graph Node Inspector | P2B | vlib dispatch loop, show run |
| 3 | Custom Buffer Inspector Node | P2B | First plugin, dual-loop, tracing |
| 4 | Interface Technology Comparison | P3 | DPDK vs memif vs TAP throughput |
| 5 | memif vSwitch | P3B | Multi-container topology, L2 bridge |
| 6 | Packet Classifier Plugin | P4 | bihash, feature arc, binary API |
| 7 | Stateful Connection Tracker | P4 | Per-flow state, thread safety |
| 8 | GoVPP Control Plane Agent | P5 | GoVPP, Stats API, REST |
| 9 | End-to-End Production Topology | P5 | Integration of all phases |

<p class="hub-section-title">REFERENCES</p>

- [FDio/vpp - GitHub](https://github.com/FDio/vpp){:target="_blank" rel="noopener"}
- [VPP Official Docs (v25.10)](https://docs.fd.io/vpp/25.10/index.html){:target="_blank" rel="noopener"}
- [GoVPP - GitHub](https://github.com/FDio/govpp){:target="_blank" rel="noopener"}
- [DPDK memif PMD](https://doc.dpdk.org/guides/nics/memif.html){:target="_blank" rel="noopener"}

[← Data Plane Hub](/learning/data-plane/)&nbsp;&nbsp;[🗺️ Full Roadmap](/learning/data-plane/vpp/vpp-roadmap/)
