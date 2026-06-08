---
layout: default
title: "Dataplane Learning — Hands-on C Projects"
permalink: /learning/data-plane/projects/
---

<section class="c-section" style="margin-top:0; padding-top:40px;">
  <div class="c-section-head" style="display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:1rem;">
    <div>
      <div class="c-kicker">// HANDS-ON</div>
      <h1 class="c-section-title">Dataplane Learning — 21 C Modules</h1>
    </div>
    <a href="https://github.com/Ajay3007/dataplane-learning" target="_blank" rel="noopener noreferrer"
       style="display:inline-flex;align-items:center;gap:0.5rem;padding:10px 18px;background:#1a1f36;color:#fff;border-radius:6px;text-decoration:none;font-size:.9rem;white-space:nowrap;border:1px solid #00d4ff;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
      View on GitHub
    </a>
  </div>
  <p style="color:var(--text-secondary,#4a5568);max-width:680px;margin-bottom:2rem;">
    Build a production-grade URL filtering engine from scratch — from a bare config parser
    all the way to a full DPDK multi-lcore pipeline with Hyperscan pattern matching,
    Kafka CDR export, and DNS sinkholing. Each module is a standalone C program
    with downloadable source files.
  </p>

  <h2 style="margin-top:2.5rem;margin-bottom:1rem;font-size:1.1rem;color:var(--secondary-color,#00d4ff);letter-spacing:.08em;text-transform:uppercase;">Phase 1 — C Foundations (Modules 01–07)</h2>
  <p style="color:var(--text-secondary,#4a5568);margin-bottom:1.25rem;font-size:.93rem;">Pure C — no external dependencies. Build and run on any Linux box.</p>
  <div class="c-card-grid c-cols-5" style="margin-bottom:2.5rem;">
    <a href="{{ '/learning/data-plane/projects/module-01-config-parser/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>01</span></div>
      <div class="c-topic-name">Config Parser</div>
      <div class="c-topic-note">INI parser driving all subsystem init</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-02-logger/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>02</span></div>
      <div class="c-topic-name">Logger</div>
      <div class="c-topic-note">Thread-safe, level-filtered, dual output</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-03-ring-buffer/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>03</span></div>
      <div class="c-topic-name">Ring Buffer</div>
      <div class="c-topic-note">Lock-free SPSC — manual rte_ring</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-04-hash-map/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>04</span></div>
      <div class="c-topic-name">Hash Map</div>
      <div class="c-topic-note">Open-addressing — manual rte_hash</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-05-packet-structs/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>05</span></div>
      <div class="c-topic-name">Packet Structs</div>
      <div class="c-topic-note">ETH/IP/UDP/TCP header parsing</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-06-dns-parser/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>06</span></div>
      <div class="c-topic-name">DNS Parser</div>
      <div class="c-topic-note">Wire format, compression, TCP/UDP</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-07-tls-sni/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>07</span></div>
      <div class="c-topic-name">TLS SNI Extractor</div>
      <div class="c-topic-note">ClientHello parsing + Hyperscan offsets</div>
    </a>
  </div>

  <h2 style="margin-top:2.5rem;margin-bottom:1rem;font-size:1.1rem;color:var(--secondary-color,#00d4ff);letter-spacing:.08em;text-transform:uppercase;">Phase 2 — DPDK Infrastructure (Modules 08–14)</h2>
  <p style="color:var(--text-secondary,#4a5568);margin-bottom:1.25rem;font-size:.93rem;">Reference code — requires DPDK. Read alongside the DPDK documentation.</p>
  <div class="c-card-grid c-cols-5" style="margin-bottom:2.5rem;">
    <a href="{{ '/learning/data-plane/projects/module-08-dpdk-eal-init/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>08</span></div>
      <div class="c-topic-name">EAL Init</div>
      <div class="c-topic-note">Hugepages, lcore launch, shutdown</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-09-mempool-mbuf/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>09</span></div>
      <div class="c-topic-name">Mempool + mbuf</div>
      <div class="c-topic-note">Pre-alloc, layout, HW checksum offload</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-10-port-init/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>10</span></div>
      <div class="c-topic-name">Port Init</div>
      <div class="c-topic-note">RSS, descriptors, offload capability</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-11-pipeline/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>11</span></div>
      <div class="c-topic-name">Pipeline</div>
      <div class="c-topic-note">RX→worker→TX multi-lcore skeleton</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-12-rte-hash/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>12</span></div>
      <div class="c-topic-name">rte_hash CRUD</div>
      <div class="c-topic-note">Bulk lookup, CRC32, NUMA, RW concurrency</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-13-atomic-stats/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>13</span></div>
      <div class="c-topic-name">Atomic Stats</div>
      <div class="c-topic-note">False sharing, memory ordering, rate calc</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-14-numa-alloc/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>14</span></div>
      <div class="c-topic-name">NUMA Alloc</div>
      <div class="c-topic-note">Socket placement, rte_malloc, memzone</div>
    </a>
  </div>

  <h2 style="margin-top:2.5rem;margin-bottom:1rem;font-size:1.1rem;color:var(--secondary-color,#00d4ff);letter-spacing:.08em;text-transform:uppercase;">Phase 3 — SASE Engine (Modules 15–18)</h2>
  <p style="color:var(--text-secondary,#4a5568);margin-bottom:1.25rem;font-size:.93rem;">Hyperscan required for 15–17. Module 18 is pure C.</p>
  <div class="c-card-grid c-cols-5" style="margin-bottom:2.5rem;">
    <a href="{{ '/learning/data-plane/projects/module-15-hyperscan-compile/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>15</span></div>
      <div class="c-topic-name">HS Compile</div>
      <div class="c-topic-note">Regex + literal DB, parseFile, serialize</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-16-hyperscan-scan/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>16</span></div>
      <div class="c-topic-name">HS Scan</div>
      <div class="c-topic-note">Scratch clone, onMatch, SNI offsets</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-17-policy-lookup/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>17</span></div>
      <div class="c-topic-name">Policy Lookup</div>
      <div class="c-topic-note">Two-tier hash+HS, multi-group, malicious</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-18-dns-sinkhole/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>18</span></div>
      <div class="c-topic-name">DNS Sinkhole</div>
      <div class="c-topic-note">In-place mbuf rewrite, answer injection</div>
    </a>
  </div>

  <h2 style="margin-top:2.5rem;margin-bottom:1rem;font-size:1.1rem;color:var(--secondary-color,#00d4ff);letter-spacing:.08em;text-transform:uppercase;">Phase 4 — Integration (Modules 19–21)</h2>
  <p style="color:var(--text-secondary,#4a5568);margin-bottom:1.25rem;font-size:.93rem;">librdkafka required for 19–20. Module 21 is standalone.</p>
  <div class="c-card-grid c-cols-5" style="margin-bottom:2.5rem;">
    <a href="{{ '/learning/data-plane/projects/module-19-kafka-producer/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>19</span></div>
      <div class="c-topic-name">Kafka Producer</div>
      <div class="c-topic-note">CDR export, batching, delivery callbacks</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-20-kafka-consumer/' | relative_url }}" class="c-topic-card">
      <div class="c-topic-meta"><span>20</span></div>
      <div class="c-topic-name">Kafka Consumer</div>
      <div class="c-topic-note">SYNC_COMPLETE protocol, RCU QSBR write</div>
    </a>
    <a href="{{ '/learning/data-plane/projects/module-21-full-pipeline/' | relative_url }}" class="c-topic-card" style="border-color:var(--accent-color,#ff6b9d);">
      <div class="c-topic-meta"><span>21</span></div>
      <div class="c-topic-name">Full Pipeline</div>
      <div class="c-topic-note">All 20 modules assembled + annotated</div>
    </a>
  </div>
</section>
