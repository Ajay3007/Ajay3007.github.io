---
layout: learning
title: "VPP Mastery Roadmap"
permalink: /learning/data-plane/vpp/vpp-roadmap/
---
<style>
.rmap-hero{background:linear-gradient(135deg,#0d1b2a 0%,#1a3a5c 60%,#1a7a6e 100%);border-radius:12px;padding:2rem 2rem 1.5rem;color:#fff;margin-bottom:2rem}
.rmap-hero h1{font-size:1.8rem;font-weight:800;color:#fff;border:none;margin:.3rem 0 .5rem}
.rmap-hero p{color:#a8d0e8;font-size:.92rem;margin:0}
.phase-timeline{position:relative;margin:2rem 0}
.phase-timeline::before{content:'';position:absolute;left:28px;top:0;bottom:0;width:3px;background:linear-gradient(180deg,#1a3a5c,#1a7a6e,#c05e1b,#5b3a8c,#1e6b3c);border-radius:2px}
.pt-phase{display:flex;gap:1.2rem;margin-bottom:1.8rem;position:relative}
.pt-dot{width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.3rem;font-weight:800;color:#fff;flex-shrink:0;z-index:1;border:3px solid #fff;box-shadow:0 2px 8px rgba(0,0,0,.2)}
.pt-body{flex:1;background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:10px;padding:1rem 1.2rem;margin-top:.3rem}
.pt-header{display:flex;align-items:flex-start;gap:.8rem;flex-wrap:wrap;margin-bottom:.6rem}
.pt-title{font-size:1.05rem;font-weight:700;color:var(--text-color,#111);margin:0}
.pt-weeks{font-size:.72rem;font-family:monospace;padding:3px 10px;border-radius:12px;font-weight:700;white-space:nowrap;margin-top:.1rem}
.pt-desc{font-size:.87rem;color:var(--text-color,#444);line-height:1.65;margin-bottom:.8rem}
.pt-modules{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:.8rem}
.pt-mod{display:inline-flex;align-items:center;gap:.35rem;padding:.3rem .7rem;border-radius:6px;font-size:.8rem;font-family:monospace;font-weight:600;text-decoration:none !important;border:1.5px solid;transition:opacity .15s}
.pt-mod:hover{opacity:.8}
.pt-skills{display:flex;flex-wrap:wrap;gap:.35rem}
.skill-tag{font-size:.72rem;background:var(--bg-color,#f0f0f0);color:var(--light-text,#555);border-radius:4px;padding:2px 8px;font-family:monospace}
.proj-chip{display:inline-flex;align-items:center;gap:.35rem;font-size:.78rem;font-family:monospace;padding:3px 10px;border-radius:6px;font-weight:600;margin-top:.5rem}
.dep-note{font-size:.8rem;color:var(--light-text,#666);background:var(--bg-color,#f5f5f5);border-radius:6px;padding:.4rem .7rem;margin-top:.6rem;border-left:3px solid #1a7a6e;line-height:1.5}
[data-theme=dark] .dep-note{background:#0d2020;border-left-color:#2a9a8e}
.summary-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:.8rem;margin:1.5rem 0}
.sg-card{background:var(--card-bg,#fff);border:1.5px solid var(--border-color,#e4e4e4);border-radius:8px;padding:.8rem 1rem;text-align:center}
.sg-num{font-size:1.8rem;font-weight:800;display:block;line-height:1}
.sg-lbl{font-size:.72rem;color:var(--light-text,#666);text-transform:uppercase;letter-spacing:.06em;font-family:monospace;display:block;margin-top:.2rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="rmap-hero">
  <div style="font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#7ab8d8;text-transform:uppercase;margin-bottom:.5rem">VPP MASTERY · FULL ROADMAP · 5 PHASES</div>
  <h1>⚡ VPP Learning Roadmap</h1>
  <p>3–4 months · Docker + AMD + Mellanox · C/C++/Go · 9 mini-projects</p>
</div>

<div class="summary-grid">
  <div class="sg-card"><span class="sg-num" style="color:#2e6da4">5</span><span class="sg-lbl">Phases</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#1a7a6e">10</span><span class="sg-lbl">Modules</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#c05e1b">9</span><span class="sg-lbl">Projects</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#5b3a8c">22+</span><span class="sg-lbl">Weeks</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#1e6b3c">GoVPP</span><span class="sg-lbl">Capstone</span></div>
</div>

<p class="sep">PHASE TIMELINE</p>

<div class="phase-timeline">

  <!-- PHASE 1 -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#2e6da4">1</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Foundation &amp; Environment</div>
        <span class="pt-weeks" style="background:#d8eaf8;color:#1a3a6c">Weeks 1–3</span>
      </div>
      <div class="pt-desc">
        Scalar vs vector processing. VPP's 5-layer architecture (VPPInfra → vlib → vnet → plugins → binary). Build from source. Docker + AMD + Mellanox setup with hugepages and VFIO. Write your first startup.conf. Use vppctl CLI. Capture and decode your first packet trace.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="{{ '/learning/data-plane/vpp/module-p1-foundation/' | relative_url }}"
           style="background:#eaf2fc;color:#1a3a6c;border-color:#b0ccec">⚡ Foundation &amp; Environment</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">scalar vs vector</span>
        <span class="skill-tag">startup.conf</span>
        <span class="skill-tag">vppctl</span>
        <span class="skill-tag">show run</span>
        <span class="skill-tag">packet trace</span>
        <span class="skill-tag">Docker + Mellanox</span>
      </div>
      <div><span class="proj-chip" style="background:#e8f0f8;color:#1a3a6c">📦 Project 1: First Packet Trace</span></div>
    </div>
  </div>

  <!-- PHASE 2 -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#1a7a6e">2</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Core VPP Internals</div>
        <span class="pt-weeks" style="background:#d8f0ee;color:#0e4040">Weeks 4–8</span>
      </div>
      <div class="pt-desc">
        Three modules covering VPP's complete software stack from the bottom up.
        <strong>vppinfra</strong>: vec, pool, bihash, clib_mem, format/unformat.
        <strong>vlib</strong>: node types, dispatch loop, buffer management, dual-loop pattern, tracing, multi-threading.
        <strong>vnet</strong>: sw_if_index, feature arcs, FIB/DPO, adjacency, L2 bridge domains.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="{{ '/learning/data-plane/vpp/module-p2-vppinfra/' | relative_url }}"
           style="background:#eaf6f4;color:#0e4848;border-color:#90c8c0">🧱 vppinfra</a>
        <a class="pt-mod" href="{{ '/learning/data-plane/vpp/module-p2-vlib/' | relative_url }}"
           style="background:#eaf6f4;color:#0e4848;border-color:#90c8c0">⚙️ vlib</a>
        <a class="pt-mod" href="{{ '/learning/data-plane/vpp/module-p2-vnet/' | relative_url }}"
           style="background:#eaf6f4;color:#0e4848;border-color:#90c8c0">🌐 vnet</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">vec / pool / bihash</span>
        <span class="skill-tag">VLIB_REGISTER_NODE</span>
        <span class="skill-tag">dual-loop</span>
        <span class="skill-tag">vlib_buffer_t</span>
        <span class="skill-tag">feature arcs</span>
        <span class="skill-tag">FIB/DPO</span>
        <span class="skill-tag">thread safety</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#e0f4f0;color:#0e4040">📦 Project 2: Graph Node Inspector</span>
        <span class="proj-chip" style="background:#e0f4f0;color:#0e4040">📦 Project 3: Custom Buffer Inspector Node</span>
      </div>
      <div class="dep-note">⚠️ This phase is the prerequisite for everything that follows. Do not skip any module - plugin development (Phase 4) directly uses all three.</div>
    </div>
  </div>

  <!-- PHASE 3 -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#c05e1b">3</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Interface Technologies</div>
        <span class="pt-weeks" style="background:#faeee4;color:#6a2800">Weeks 9–13</span>
      </div>
      <div class="pt-desc">
        Every interface type VPP supports, in depth. <strong>DPDK plugin</strong>: dpdk-input node internals, mbuf/vlib_buffer shared memory bridge, Mellanox mlx5 specifics. <strong>memif</strong>: shared-memory zero-copy architecture, libmemif API, DPDK net_memif PMD. <strong>TAP v2, AF_XDP, vhost-user, AF_PACKET</strong>: Linux integration, eBPF/XSK, VM connectivity, full comparison matrix.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="{{ '/learning/data-plane/vpp/module-p3-dpdk/' | relative_url }}"
           style="background:#faeee4;color:#6a2800;border-color:#e8b890">🔌 DPDK Plugin</a>
        <a class="pt-mod" href="{{ '/learning/data-plane/vpp/module-p3-memif/' | relative_url }}"
           style="background:#faeee4;color:#6a2800;border-color:#e8b890">🔗 memif</a>
        <a class="pt-mod" href="{{ '/learning/data-plane/vpp/module-p3-tap-afxdp/' | relative_url }}"
           style="background:#faeee4;color:#6a2800;border-color:#e8b890">🐧 TAP · AF_XDP · vhost</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">dpdk-input</span>
        <span class="skill-tag">mbuf↔vlib bridge</span>
        <span class="skill-tag">mlx5 iova-mode va</span>
        <span class="skill-tag">memif server/client</span>
        <span class="skill-tag">libmemif</span>
        <span class="skill-tag">TAP v2</span>
        <span class="skill-tag">linux-cp</span>
        <span class="skill-tag">AF_XDP/UMEM</span>
        <span class="skill-tag">vhost-user</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#faeee4;color:#6a2800">📦 Project 4: Interface Throughput Comparison</span>
        <span class="proj-chip" style="background:#faeee4;color:#6a2800">📦 Project 5: memif vSwitch</span>
      </div>
    </div>
  </div>

  <!-- PHASE 4 -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#5b3a8c">4</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Plugin Development</div>
        <span class="pt-weeks" style="background:#ede8f5;color:#3a1a6c">Weeks 14–18</span>
      </div>
      <div class="pt-desc">
        Writing production-quality VPP plugins. Graph node anatomy, dual/quad-loop pattern, binary API (.api files, message handlers, vat2), CLI commands, error handling, feature arc registration. Testing with VPP's Python test framework (<code>vpp_unittest</code>). Two projects: a packet classifier with bihash lookups, and a stateful connection tracker with per-flow state and timer-based expiry.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="{{ '/learning/data-plane/vpp/module-p4-plugin-dev/' | relative_url }}"
           style="background:#ede8f5;color:#3a1a6c;border-color:#c0a8e8">🔨 Plugin Development</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">VLIB_REGISTER_NODE</span>
        <span class="skill-tag">.api files</span>
        <span class="skill-tag">message handlers</span>
        <span class="skill-tag">VLIB_CLI_COMMAND</span>
        <span class="skill-tag">VNET_FEATURE_INIT</span>
        <span class="skill-tag">vpp_unittest</span>
        <span class="skill-tag">VppTestCase</span>
        <span class="skill-tag">pool + bihash</span>
        <span class="skill-tag">tw_timer</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#ede8f5;color:#3a1a6c">📦 Project 6: Packet Classifier Plugin</span>
        <span class="proj-chip" style="background:#ede8f5;color:#3a1a6c">📦 Project 7: Stateful Connection Tracker</span>
      </div>
      <div class="dep-note">⚠️ Requires solid Phase 2 knowledge: dual-loop pattern (vlib P2B), bihash/pool (vppinfra P2A), feature arcs (vnet P2C).</div>
    </div>
  </div>

  <!-- PHASE 5 -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#1e6b3c">5</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Control Plane &amp; Advanced</div>
        <span class="pt-weeks" style="background:#e2f0e8;color:#0e3a1e">Weeks 19–22+</span>
      </div>
      <div class="pt-desc">
        Programmatic control of VPP from external processes. GoVPP binary API client with auto-generated bindings. VPP Stats API (shared memory, counters, interface stats). vpp_papi Python bindings. Observability: event logger, perfmon plugin, NUMA-aware tuning. Production deployment patterns. End-to-end capstone integrating all phases. <strong>Bonus:</strong> VPP Host Stack — TCP/Session layer, VCL, application namespaces, and vcl-ldpreload.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="{{ '/learning/data-plane/vpp/module-p5-controlplane/' | relative_url }}"
           style="background:#e2f0e8;color:#0e3a1e;border-color:#8ec8a8">🎛️ Control Plane &amp; GoVPP</a>
        <a class="pt-mod" href="{{ '/learning/data-plane/vpp/module-hoststack/' | relative_url }}"
           style="background:#e8f0fa;color:#1a3a6c;border-color:#90acd8">🌐 Host Stack — TCP &amp; Session Layers <span style="font-size:.68rem;opacity:.75;margin-left:.3rem">Bonus</span></a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">GoVPP</span>
        <span class="skill-tag">binapi-generator</span>
        <span class="skill-tag">Stats API</span>
        <span class="skill-tag">vpp_papi</span>
        <span class="skill-tag">event logger</span>
        <span class="skill-tag">perfmon</span>
        <span class="skill-tag">NUMA tuning</span>
        <span class="skill-tag">cpu pinning</span>
        <span class="skill-tag">session layer</span>
        <span class="skill-tag">VCL</span>
        <span class="skill-tag">vcl-ldpreload</span>
        <span class="skill-tag">app namespaces</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#e2f0e8;color:#0e3a1e">📦 Project 8: GoVPP Control Plane Agent</span>
        <span class="proj-chip" style="background:#e2f0e8;color:#0e3a1e">📦 Project 9: End-to-End Production Topology</span>
      </div>
    </div>
  </div>

</div>

<p class="sep">ALL MINI-PROJECTS</p>

| # | Project | Phase | Key Skills |
|---|---------|-------|------------|
| 1 | VPP Container Lab - First Packet | P1 | Build, Docker, startup.conf, trace |
| 2 | Graph Node Inspector | P2B | pg-input, show run, GDB dispatch loop |
| 3 | Custom Buffer Inspector Node | P2B | First plugin, trace, feature arc, CLI |
| 4 | Interface Technology Comparison | P3A | DPDK vs memif vs TAP throughput |
| 5 | memif vSwitch | P3B | 3-container topology, libmemif Python |
| 6 | Packet Classifier Plugin | P4 | bihash lookup, binary API, test suite |
| 7 | Stateful Connection Tracker | P4 | Per-flow pool, tw_timer, thread safety |
| 8 | GoVPP Control Plane Agent | P5 | GoVPP, Stats API, REST endpoint |
| 9 | End-to-End Production Topology | P5 | Full integration, tuning, benchmark |

<div class="mod-nav">
  <a href="{{ '/learning/data-plane/vpp/' | relative_url }}">← VPP Hub</a>
  <a class="nb" href="{{ '/learning/data-plane/vpp/module-p1-foundation/' | relative_url }}">Start: Phase 1 →</a>
</div>
