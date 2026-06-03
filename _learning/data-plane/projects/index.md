---
layout: default
title: "SASE DP — Hands-on C Projects"
permalink: /learning/data-plane/projects/
---

<section class="c-section" style="margin-top:0; padding-top:40px;">
  <div class="c-section-head">
    <div>
      <div class="c-kicker">// HANDS-ON</div>
      <h1 class="c-section-title">SASE Dataplane — 21 C Modules</h1>
    </div>
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
