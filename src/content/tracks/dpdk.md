---
title: "DPDK"
tagline: "Poll-mode drivers, mempools and line-rate pipelines."
description: "DPDK MASTERY · FULL ROADMAP · 3 PHASES & 9889; DPDK Learning Roadmap 3–4 months · Intel / Mellanox NICs · C · 6 modules · 7 mini-projects · Production SASE-DP context 3 Phases…"
domain: data-plane
order: 2
status: active
url: /learning/data-plane/dpdk/dpdk-roadmap/
---

<style>
.rmap-hero{background:linear-gradient(135deg,#030d1a 0%,#0a2040 60%,#1a5a7a 100%);border-radius:12px;padding:2rem 2rem 1.5rem;color:#fff;margin-bottom:2rem}
.rmap-hero h1{font-size:1.8rem;font-weight:800;color:#fff;border:none;margin:.3rem 0 .5rem}
.rmap-hero p{color:#7ab8d8;font-size:.92rem;margin:0}
.phase-timeline{position:relative;margin:2rem 0}
.phase-timeline::before{content:'';position:absolute;left:28px;top:0;bottom:0;width:3px;background:linear-gradient(180deg,#2e6da4,#1a7a6e,#c05e1b);border-radius:2px}
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
.mod-nav .nb{background:#0a2040;color:#fff !important;border-color:#0a2040}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="rmap-hero">
  <div style="font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#5ab0d0;text-transform:uppercase;margin-bottom:.5rem">DPDK MASTERY · FULL ROADMAP · 3 PHASES</div>
  <h1>&#9889; DPDK Learning Roadmap</h1>
  <p>3–4 months · Intel / Mellanox NICs · C · 6 modules · 7 mini-projects · Production SASE-DP context</p>
</div>

<div class="summary-grid">
  <div class="sg-card"><span class="sg-num" style="color:#2e6da4">3</span><span class="sg-lbl">Phases</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#1a7a6e">6</span><span class="sg-lbl">Modules</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#c05e1b">7</span><span class="sg-lbl">Projects</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#5b3a8c">14+</span><span class="sg-lbl">Weeks</span></div>
  <div class="sg-card"><span class="sg-num" style="color:#0a6a40">SASE</span><span class="sg-lbl">Capstone</span></div>
</div>

<p class="sep">PHASE TIMELINE</p>

<div class="phase-timeline">

  <!-- PHASE 1 -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#2e6da4">1</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Foundation &amp; Memory</div>
        <span class="pt-weeks" style="background:#d8eaf8;color:#1a3a6c">Weeks 1–5</span>
      </div>
      <div class="pt-desc">
        Why the Linux kernel packet path fails at 100G — interrupts, sk_buff, memory copies, context switches.
        DPDK's answer: Poll Mode Drivers, hugepages, zero-copy, user-space NIC ownership.
        Full DPDK software stack from PMD → ethdev → rte_mempool → rte_mbuf → EAL.
        PCIe device binding with VFIO and IOMMU. Hugepage anatomy, IOVA, DMA mapping.
        <strong>rte_mempool</strong> pre-allocation mechanics (per-lcore cache, bulk get/put).
        <strong>rte_mbuf</strong> layout: buf_addr, data_off, pkt_len, ol_flags, headroom, chained mbufs.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="/learning/data-plane/dpdk/module-p1-foundation/"
           style="background:#eaf2fc;color:#1a3a6c;border-color:#b0ccec">&#128295; Foundation &amp; EAL</a>
        <a class="pt-mod" href="/learning/data-plane/dpdk/module-p1-memory/"
           style="background:#eaf2fc;color:#1a3a6c;border-color:#b0ccec">&#128190; Hugepages, mempool &amp; mbuf</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">kernel path overheads</span>
        <span class="skill-tag">PMD polling</span>
        <span class="skill-tag">rte_eal_init()</span>
        <span class="skill-tag">VFIO-PCI</span>
        <span class="skill-tag">IOMMU</span>
        <span class="skill-tag">hugepages</span>
        <span class="skill-tag">IOVA</span>
        <span class="skill-tag">rte_mempool</span>
        <span class="skill-tag">rte_mbuf</span>
        <span class="skill-tag">zero-copy</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#e8f0f8;color:#1a3a6c">&#128230; Project 1: DPDK Hello World + EAL Probe</span>
        <span class="proj-chip" style="background:#e8f0f8;color:#1a3a6c">&#128230; Project 2: mbuf Inspector — Decode Every Field</span>
      </div>
    </div>
  </div>

  <!-- PHASE 2 -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#1a7a6e">2</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Core Mechanics</div>
        <span class="pt-weeks" style="background:#d8f0ee;color:#0e4040">Weeks 6–10</span>
      </div>
      <div class="pt-desc">
        Two modules covering DPDK's complete runtime machinery.
        <strong>PMD &amp; Port Config</strong>: NIC descriptor rings, DD bit handshake, rx_burst / tx_burst hot path,
        full port configuration sequence (dev_configure → queue_setup → dev_start), offloads, stats.
        <strong>RSS</strong>: Toeplitz hash in hardware, RETA table, symmetric RSS key, power-of-2 worker count requirement.
        <strong>rte_ring</strong>: lock-free SPSC/MPMC circular buffer, CAS mechanics, bulk enqueue/dequeue.
        <strong>rte_distributor</strong>: fan-out from one RX core to N workers, work tagging, flow affinity.
        <strong>Application Models</strong>: run-to-completion vs pipeline, when to use each.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="/learning/data-plane/dpdk/module-p2-pmd/"
           style="background:#eaf6f4;color:#0e4848;border-color:#90c8c0">&#128268; PMD &amp; Port Config</a>
        <a class="pt-mod" href="/learning/data-plane/dpdk/module-p2-rings/"
           style="background:#eaf6f4;color:#0e4848;border-color:#90c8c0">&#128260; rte_ring, Distributor &amp; App Models</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">rte_eth_rx_burst</span>
        <span class="skill-tag">DD bit</span>
        <span class="skill-tag">descriptor rings</span>
        <span class="skill-tag">RSS Toeplitz</span>
        <span class="skill-tag">RETA</span>
        <span class="skill-tag">symmetric RSS</span>
        <span class="skill-tag">rte_ring CAS</span>
        <span class="skill-tag">MPMC</span>
        <span class="skill-tag">rte_distributor</span>
        <span class="skill-tag">pipeline model</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#e0f4f0;color:#0e4040">&#128230; Project 3: L2 Forwarder with RSS Verification</span>
        <span class="proj-chip" style="background:#e0f4f0;color:#0e4040">&#128230; Project 4: Ring-Based Worker Pipeline</span>
      </div>
      <div class="dep-note">&#9888;&#65039; Phase 1 memory knowledge is prerequisite — PMD and ring patterns build directly on mempool and mbuf internals.</div>
    </div>
  </div>

  <!-- PHASE 3 -->
  <div class="pt-phase">
    <div class="pt-dot" style="background:#c05e1b">3</div>
    <div class="pt-body">
      <div class="pt-header">
        <div class="pt-title">Advanced Topics &amp; Production</div>
        <span class="pt-weeks" style="background:#faeee4;color:#6a2800">Weeks 11–14+</span>
      </div>
      <div class="pt-desc">
        Production-grade DPDK design and operations.
        <strong>Multi-Process</strong>: primary/secondary model, shared mempools and rings, named object lookup,
        hot-restart secondaries — exactly the pattern used in Jio SASE-DP.
        <strong>rte_flow</strong>: hardware flow classification and queue steering with zero CPU cost,
        match / action model, flow priority and groups.
        <strong>NUMA</strong>: socket-aware allocation, lcore binding, cache-line alignment, false sharing.
        <strong>Packet Processing Patterns</strong>: prefetching, batching, branch elimination.
        <strong>Performance Tuning</strong>: CPU isolation, hugepage sizing, burst tuning, PMD stats, benchmarking.
        <strong>Debugging</strong>: mbuf leaks, imissed counter, mempool exhaustion, common pitfalls.
      </div>
      <div class="pt-modules">
        <a class="pt-mod" href="/learning/data-plane/dpdk/module-p3-advanced/"
           style="background:#faeee4;color:#6a2800;border-color:#e8b890">&#127760; Multi-Process, rte_flow &amp; NUMA</a>
        <a class="pt-mod" href="/learning/data-plane/dpdk/module-p3-perf/"
           style="background:#faeee4;color:#6a2800;border-color:#e8b890">&#128200; Patterns, Tuning &amp; Debugging</a>
      </div>
      <div class="pt-skills">
        <span class="skill-tag">primary/secondary</span>
        <span class="skill-tag">rte_mempool_lookup</span>
        <span class="skill-tag">rte_flow_create</span>
        <span class="skill-tag">FDIR</span>
        <span class="skill-tag">NUMA-aware alloc</span>
        <span class="skill-tag">cache-line align</span>
        <span class="skill-tag">prefetch</span>
        <span class="skill-tag">isolcpus</span>
        <span class="skill-tag">imissed</span>
        <span class="skill-tag">mbuf leak</span>
      </div>
      <div>
        <span class="proj-chip" style="background:#faeee4;color:#6a2800">&#128230; Project 5: Multi-Process SASE-DP Skeleton</span>
        <span class="proj-chip" style="background:#faeee4;color:#6a2800">&#128230; Project 6: rte_flow Hardware Classifier</span>
        <span class="proj-chip" style="background:#faeee4;color:#6a2800">&#128230; Project 7: End-to-End URL Filter Dataplane</span>
      </div>
    </div>
  </div>

</div>

<p class="sep">ALL MINI-PROJECTS</p>

| # | Project | Phase | Key Skills |
|---|---------|-------|------------|
| 1 | DPDK Hello World + EAL Probe | P1 | rte_eal_init, lcore enumeration, hugepage check |
| 2 | mbuf Inspector — Decode Every Field | P1 | rte_mbuf layout, ol_flags, pkt_len, headroom |
| 3 | L2 Forwarder with RSS Verification | P2 | rx_burst, tx_burst, MAC swap, RSS queue affinity |
| 4 | Ring-Based Worker Pipeline | P2 | rte_ring SPSC, producer/consumer cores, backpressure |
| 5 | Multi-Process SASE-DP Skeleton | P3 | primary/secondary, named pool lookup, hot-restart |
| 6 | rte_flow Hardware Classifier | P3 | rte_flow_create, 5-tuple matching, queue steering |
| 7 | End-to-End URL Filter Dataplane | P3 | Full pipeline: RX → classify → filter → TX → stats |

<div class="mod-nav">
  <a href="/learning/data-plane/dpdk/">&#8592; DPDK Hub</a>
  <a class="nb" href="/learning/data-plane/dpdk/module-p1-foundation/">Start: Phase 1 &#8594;</a>
</div>
