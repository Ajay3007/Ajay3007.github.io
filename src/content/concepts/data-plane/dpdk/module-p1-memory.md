---
title: "DPDK P1 — Hugepages, mempool & mbuf"
description: "DPDK MASTERY · PHASE 1 OF 3 · MODULE B Hugepages, mempool mbuf Hugepage memory model · IOVA · rte mempool internals · rte mbuf anatomy · chained mbufs Ch 4 — Hugepages Memory…"
domain: data-plane
track: dpdk
order: 1
ownHeader: true
url: /learning/data-plane/dpdk/module-p1-memory/
---

<style>
:root{--dpdk-blue:#1a3a5c;--dpdk-teal:#1a7a6e}
.mod-header{background:linear-gradient(135deg,#030d1a 0%,#0a2040 60%,#1a4a70 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#5ab0d0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#a8cce0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#c8e4f4}
.tab-bar{display:flex;flex-wrap:wrap;gap:0;background:#0a2040;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#5dd0f0;border-bottom-color:#5dd0f0}
.tab-pane{display:none}
.tab-pane.active{display:block}
.p-blue{background:#eaf2fc;border-left:4px solid #2e6da4;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-teal{background:#e8f6f4;border-left:4px solid #1a7a6e;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-orange{background:#fdf0e8;border-left:4px solid #c05e1b;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-slate{background:#f4f6f8;border-left:4px solid #64748b;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-violet{background:#f3f0fc;border-left:4px solid #7c3aed;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
[data-theme=dark] .p-blue{background:#0d1e34;border-color:#4a90d9}
[data-theme=dark] .p-teal{background:#0d2020;border-color:#2a9a8e}
[data-theme=dark] .p-orange{background:#1e0d00;border-color:#e07830}
[data-theme=dark] .p-slate{background:#1a1e24;border-color:#8898aa}
[data-theme=dark] .p-violet{background:#180d30;border-color:#9d6bf0}
.p-blue h4,.p-teal h4,.p-orange h4,.p-slate h4,.p-violet h4{margin:0 0 .5rem;font-size:.9rem;font-weight:700}
.ins{background:#e8f5e9;border:1px solid #66bb6a;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.warn{background:#fff8e1;border:1px solid #ffca28;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.note{background:#e3f2fd;border:1px solid #42a5f5;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
[data-theme=dark] .ins{background:#0d2010;border-color:#388e3c}
[data-theme=dark] .warn{background:#1e1800;border-color:#f9a825}
[data-theme=dark] .note{background:#0d1e2e;border-color:#1976d2}
.cb{background:#0d1117;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;font-family:monospace;font-size:.82rem;line-height:1.7;color:#e6edf3;white-space:pre-wrap}
.cb .cm{color:#8b949e}.cb .ck{color:#ff7b72}.cb .cv{color:#79c0ff}.cb .cs{color:#a5d6ff}.cb .cn{color:#f2cc60}.cb .cf{color:#d2a8ff}.cb .co{color:#ffa657}.cb .cg{color:#3fb950}
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.8rem 0}
.t-table th{background:#0a2040;color:#7ab8d8;font-family:monospace;font-size:.75rem;font-weight:700;padding:.5rem .7rem;text-align:left;border-bottom:2px solid #1a4070}
.t-table td{padding:.45rem .7rem;border-bottom:1px solid var(--border-color,#e8e8e8);vertical-align:top}
.t-table tr:last-child td{border-bottom:none}
.t-table tr:hover td{background:var(--bg-color,#f8f9fa)}
.flow-list{list-style:none;padding:0;margin:.8rem 0}
.fl-step{display:flex;gap:.8rem;margin-bottom:.5rem;font-size:.88rem;line-height:1.6}
.fl-num{width:24px;height:24px;border-radius:50%;background:#2e6da4;color:#fff;font-size:.72rem;font-weight:800;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:.15rem}
.diagram-box{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;font-family:monospace;font-size:.78rem;line-height:1.8;color:#c9d1d9;overflow-x:auto;white-space:pre}
.lab-box{background:var(--card-bg,#fff);border:2px solid #2e6da4;border-radius:10px;overflow:hidden;margin:1rem 0}
.lab-hdr{background:#0a2040;color:#fff;padding:.7rem 1.2rem;font-weight:700;font-family:monospace;font-size:.9rem}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.5rem;font-size:.87rem}
.sn{background:#2e6da4;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:800;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{padding:.3rem 0;font-size:.87rem;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐ ";font-size:1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#0a2040;color:#fff !important;border-color:#0a2040}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">DPDK MASTERY · PHASE 1 OF 3 · MODULE B</div>
  <div class="mod-title">Hugepages, mempool &amp; mbuf</div>
  <div class="mod-subtitle">Hugepage memory model · IOVA · rte_mempool internals · rte_mbuf anatomy · chained mbufs</div>
  <div class="mod-pills">
    <span class="mod-pill">Ch 4 — Hugepages &amp; Memory</span>
    <span class="mod-pill">Ch 5 — rte_mempool</span>
    <span class="mod-pill">Ch 6 — rte_mbuf</span>
    <span class="mod-pill">C · DMA · NUMA</span>
    <span class="mod-pill">Weeks 3–5</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t-hp')">Hugepages</button>
  <button class="tab-btn" onclick="vt(event,'t-vm')">Virtual Memory</button>
  <button class="tab-btn" onclick="vt(event,'t-pool')">rte_mempool</button>
  <button class="tab-btn" onclick="vt(event,'t-mbuf')">rte_mbuf</button>
  <button class="tab-btn" onclick="vt(event,'t-chain')">Chained mbufs</button>
  <button class="tab-btn" onclick="vt(event,'t-qa')">Interview Q&amp;A</button>
  <button class="tab-btn" onclick="vt(event,'t-lab')">Lab</button>
</div>

<!-- TAB: Hugepages -->
<div id="t-hp" class="tab-pane active">

<div class="p-blue">
<h4>Why Hugepages Are Mandatory in DPDK</h4>
Two orthogonal requirements drive hugepage usage: <strong>(1) DMA stability</strong> — hugepages are pinned (mlock'd) so the NIC's IOVA is always valid; <strong>(2) TLB efficiency</strong> — 2MB pages mean 512× fewer TLB entries than 4KB pages, dramatically cutting TLB miss rate on the hot packet path.
</div>

<table class="t-table">
<thead><tr><th>Property</th><th>Normal 4KB Pages</th><th>DPDK Hugepages (2MB)</th></tr></thead>
<tbody>
<tr><td>Page size</td><td>4 KB</td><td>2 MB (or 1 GB)</td></tr>
<tr><td>Pinned in RAM</td><td>No — OS can swap to disk</td><td>Yes — mlock'd at allocation, never swapped</td></tr>
<tr><td>Physical address stable</td><td>No — IOVA becomes stale after swap</td><td>Yes — IOVA always valid for NIC DMA</td></tr>
<tr><td>TLB entries for 1 GB data</td><td>262,144 entries</td><td>512 entries (512× fewer misses)</td></tr>
<tr><td>Page fault on access</td><td>Possible — ~10 ms disk I/O</td><td>Never — pages pre-faulted at EAL init</td></tr>
<tr><td>DMA safety</td><td>Unsafe — may be freed under NIC</td><td>Safe — physical addr never changes</td></tr>
</tbody>
</table>

<div class="warn">&#9888;&#65039; <strong>The catastrophic swap scenario:</strong> NIC DMA uses physical addresses (IOVAs). If a page is swapped out, the physical frame is freed. The NIC's IOVA is now stale — it writes to wrong or freed memory. Even without corruption, one swap = ~10 ms pause. At 100G, the ring fills in ~80 µs. 10 ms = millions of dropped packets.</div>

<p class="sep">HUGEPAGE SETUP COMMANDS</p>

<div class="cb"><span class="cm"># Check available hugepage sizes</span>
ls /sys/kernel/mm/hugepages/

<span class="cm"># Allocate 1024 × 2MB hugepages (= 2 GB)</span>
echo 1024 &gt; /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages

<span class="cm"># Mount hugetlbfs (if not already mounted)</span>
mount -t hugetlbfs none /dev/hugepages

<span class="cm"># Verify allocation</span>
cat /proc/meminfo | grep Huge

<span class="cm"># DPDK EAL: use --socket-mem to specify per-NUMA-socket allocation</span>
./my_app -l 0-3 -n 4 --socket-mem 1024,1024  <span class="cm"># 1GB on socket 0, 1GB on socket 1</span></div>

<div class="note">&#128204; <strong>1GB hugepages:</strong> For very large mempools or when 2MB pages still have too many TLB entries. Requires kernel boot parameter <code>hugepagesz=1G hugepages=4</code>. EAL will prefer 1GB pages if available.</div>

</div><!-- /t-hp -->

<!-- TAB: Virtual Memory -->
<div id="t-vm" class="tab-pane">

<p class="sep">VIRTUAL MEMORY — PROCESS ISOLATION</p>

<div class="diagram-box">Virtual Memory vs Physical Memory — Process Isolation

Process A (virtual)       Process B (virtual)       Physical RAM
▲ HIGH ADDRESS            ▲ HIGH ADDRESS             ▲
  kernel space              kernel space              kernel code (shared)
  stack  0x7FFF…            stack  0x7FFF…            frame 1024 ← A stack
  heap   0x0810…            heap   0x0810…            frame 2048 ← B stack
  data   0x0805…            data   0x0805…            frame 5632 ← A heap
  code   0x0804…            code   0x0804…            frame 8192 ← B heap
▼ 0x0000                  ▼ 0x0000                    DPDK hugepages PINNED
                                                        — never swapped
                                                        — fixed IOVAs for NIC DMA

KEY INSIGHT: Both processes may use virtual address 0x08051000.
MMU translates: A → physical frame 5632 | B → physical frame 8192
Same virtual address. Completely different RAM. Complete isolation.</div>

<div class="p-teal">
<h4>Virtual Memory Segments</h4>
Every process has: <strong>code</strong> (text, read-only), <strong>data</strong> (BSS + initialized globals), <strong>heap</strong> (grows up via malloc/mmap), <strong>stack</strong> (grows down, per-thread), and <strong>kernel space</strong> (top of virtual address space, Ring 0 only). DPDK hugepage allocations live in a separate mmap'd region, pinned against eviction.
</div>

<p class="sep">NUMA MEMORY TOPOLOGY</p>

<div class="diagram-box">NUMA — Non-Uniform Memory Access

Socket 0                           Socket 1
  CPU cores 0-7                      CPU cores 8-15
  L1/L2/L3 cache                     L1/L2/L3 cache
  Local RAM (DDR channels 0-1)       Local RAM (DDR channels 2-3)
    ↑ low latency (~60 ns)             ↑ low latency (~60 ns)
  NIC port 0 (PCIe)                  NIC port 1 (PCIe)
    ↑ DMA into socket 0 RAM            ↑ DMA into socket 1 RAM

Cross-NUMA access (socket 0 CPU → socket 1 RAM): ~120 ns — 2× slower!

DPDK rule: ALWAYS allocate mempool on the same NUMA socket as the NIC.
  rte_pktmbuf_pool_create("POOL", N, CACHE_SZ, 0, sz, rte_eth_dev_socket_id(port))
                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^
                                                        returns NIC's socket — use it!</div>

</div><!-- /t-vm -->

<!-- TAB: rte_mempool -->
<div id="t-pool" class="tab-pane">

<div class="p-blue">
<h4>rte_mempool — The Allocation Eliminator</h4>
<code>rte_mempool</code> pre-allocates all packet buffers at startup. The hot data path never calls malloc/free — it calls <code>rte_mempool_get()</code> (which pops from a lock-free ring or per-lcore cache) and <code>rte_mempool_put()</code> (which pushes back). This is what enables zero-allocation-overhead packet processing.
</div>

<p class="sep">MEMPOOL INTERNAL ARCHITECTURE</p>

<div class="diagram-box">rte_mempool Architecture

                     rte_mempool header
                    ┌─────────────────────────────────────┐
                    │ name, size, elt_size, cache_size     │
                    │ count = total_elts - in_use_count    │
                    └───────────────┬─────────────────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              ▼                     ▼                     ▼
        Per-lcore cache        Per-lcore cache       Per-lcore cache
        (lcore 0)              (lcore 1)             (lcore 2)
        up to cache_size       up to cache_size      up to cache_size
        objects (stack)        objects (stack)       objects (stack)
              │                     │                     │
              └─────────────────────┴─────────────────────┘
                                    │ (cache miss → fallback)
                                    ▼
                         Common pool (rte_ring)
                         Lock-free MPMC ring
                         Contains all remaining objects</div>

<p class="sep">ALLOCATION PATH</p>

<ul class="flow-list">
<li class="fl-step"><span class="fl-num">1</span><div><strong>rte_mempool_get(pool, &amp;obj):</strong> Check per-lcore cache first (~3 cycles, no atomic)</div></li>
<li class="fl-step"><span class="fl-num">2</span><div><strong>Cache hit:</strong> Pop object from lcore-local stack. Return immediately. Zero contention.</div></li>
<li class="fl-step"><span class="fl-num">3</span><div><strong>Cache miss:</strong> Refill lcore cache in bulk from common pool ring (one CAS → batch transfer)</div></li>
<li class="fl-step"><span class="fl-num">4</span><div><strong>rte_mempool_put(pool, obj):</strong> Push to lcore cache. If cache full → flush bulk to common ring.</div></li>
</ul>

<div class="cb"><span class="cm">// Create a packet mempool</span>
<span class="ck">struct</span> rte_mempool *mbuf_pool = <span class="cf">rte_pktmbuf_pool_create</span>(
    <span class="cs">"MBUF_POOL"</span>,              <span class="cm">// unique name</span>
    <span class="cn">8192</span>,                      <span class="cm">// total number of mbufs</span>
    <span class="cn">256</span>,                       <span class="cm">// per-lcore cache size (objects)</span>
    <span class="cn">0</span>,                         <span class="cm">// private data size per element</span>
    <span class="cn">RTE_MBUF_DEFAULT_BUF_SIZE</span>, <span class="cm">// data buffer size (2048 bytes)</span>
    <span class="cf">rte_eth_dev_socket_id</span>(port_id)  <span class="cm">// NUMA socket — MUST match NIC</span>
);
<span class="ck">if</span> (!mbuf_pool)
    <span class="cf">rte_exit</span>(<span class="cn">EXIT_FAILURE</span>, <span class="cs">"Cannot create mbuf pool\n"</span>);

<span class="cm">// Manual get/put (for non-packet objects)</span>
<span class="ck">void</span> *obj;
<span class="cf">rte_mempool_get</span>(pool, &amp;obj);     <span class="cm">// borrow object</span>
<span class="cm">/* use obj */</span>
<span class="cf">rte_mempool_put</span>(pool, obj);      <span class="cm">// return object</span>

<span class="cm">// Bulk operations (preferred — reduces ring contention)</span>
<span class="ck">void</span> *objs[<span class="cn">32</span>];
<span class="cf">rte_mempool_get_bulk</span>(pool, objs, <span class="cn">32</span>);
<span class="cf">rte_mempool_put_bulk</span>(pool, objs, <span class="cn">32</span>);</div>

<table class="t-table">
<thead><tr><th>Pool Size</th><th>Use Case</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>1024 – 4096</td><td>Dev / light load</td><td>Small — may exhaust quickly under burst</td></tr>
<tr><td>8192</td><td>Standard — most DPDK examples</td><td>Good balance of memory vs exhaustion risk</td></tr>
<tr><td>65536+</td><td>High burst / 100G line rate</td><td>Large memory footprint but never exhausts under normal traffic</td></tr>
</tbody>
</table>

<div class="warn">&#9888;&#65039; <strong>Pool size must be power of 2 minus 1</strong> (e.g. 8191, not 8192) — rte_mempool internally uses a power-of-2 ring and the actual allocated count is <code>N+1</code> ring slots. The API accepts <code>N</code> and adjusts internally. Common mistake: using 8192 when you mean 8191.</div>

</div><!-- /t-pool -->

<!-- TAB: rte_mbuf -->
<div id="t-mbuf" class="tab-pane">

<div class="p-blue">
<h4>rte_mbuf — The Packet Carrier</h4>
<code>rte_mbuf</code> is the kernel's <code>sk_buff</code> equivalent. Every received packet is wrapped in an mbuf. It has a fixed header (metadata) followed by a contiguous data buffer (where packet bytes live). The key design decision: <strong>metadata and packet data are in the same hugepage allocation</strong> — one cache line prefetch gets both.
</div>

<p class="sep">MBUF MEMORY LAYOUT</p>

<div class="diagram-box">rte_mbuf Memory Layout (one hugepage allocation)

 ┌─────────────────────────────────────────────────────────────────┐
 │                   rte_mbuf header (~128 bytes)                  │
 │  buf_addr  ─────────────────────────────────────────────────►  │
 │  buf_iova  (physical address for NIC DMA)                       │
 │  data_off  (offset from buf_addr to first packet byte)          │
 │  pkt_len   (total packet length in bytes)                       │
 │  data_len  (data length in this segment)                        │
 │  nb_segs   (number of segments in chain)                        │
 │  port      (Rx port index)                                      │
 │  ol_flags  (offload flags: cksum, vlan, rss, etc.)              │
 │  hash.rss  (RSS hash value from NIC hardware)                   │
 │  vlan_tci  (VLAN tag if stripped by NIC)                        │
 │  next      (pointer to next segment, or NULL)                   │
 │  pool      (pointer back to mempool for free)                   │
 │  refcnt    (reference count — for cloning)                      │
 ├─────────────────────────────────────────────────────────────────┤
 │                   Headroom (RTE_PKTMBUF_HEADROOM = 128 bytes)   │
 │                   ← reserved for prepending headers             │
 ├──────────── ← buf_addr + data_off (= rte_pktmbuf_mtod result) ─┤
 │             [  Ethernet header (14B) │ IP (20B) │ TCP (20B) │…]│
 │                   Packet data (data_len bytes)                  │
 └─────────────────────────────────────────────────────────────────┘
 Total buffer: RTE_MBUF_DEFAULT_BUF_SIZE = 2048 bytes</div>

<p class="sep">KEY MBUF MACROS & FIELDS</p>

<div class="cb"><span class="cm">// Get pointer to packet data (most common operation)</span>
<span class="ck">struct</span> rte_ether_hdr *eth = <span class="cf">rte_pktmbuf_mtod</span>(mbuf, <span class="ck">struct</span> rte_ether_hdr *);
<span class="cm">// Expands to: (type)(mbuf-&gt;buf_addr + mbuf-&gt;data_off) — direct pointer into hugepage</span>

<span class="cm">// Access packet at byte offset</span>
<span class="ck">struct</span> rte_ipv4_hdr *ip = <span class="cf">rte_pktmbuf_mtod_offset</span>(mbuf, <span class="ck">struct</span> rte_ipv4_hdr *,
                                                   <span class="ck">sizeof</span>(<span class="ck">struct</span> rte_ether_hdr));

<span class="cm">// Packet length</span>
<span class="co">uint32_t</span> total_len  = mbuf-&gt;pkt_len;   <span class="cm">// total bytes across all segments</span>
<span class="co">uint16_t</span> seg_len    = mbuf-&gt;data_len;  <span class="cm">// bytes in this segment only</span>

<span class="cm">// Prepend a header (uses headroom)</span>
<span class="ck">struct</span> rte_ether_hdr *eth = (<span class="ck">struct</span> rte_ether_hdr *)
    <span class="cf">rte_pktmbuf_prepend</span>(mbuf, <span class="ck">sizeof</span>(<span class="ck">struct</span> rte_ether_hdr));
<span class="cm">// Returns NULL if no headroom available</span>

<span class="cm">// Append to tail</span>
<span class="ck">char</span> *tail = <span class="cf">rte_pktmbuf_append</span>(mbuf, <span class="cn">4</span>);  <span class="cm">// add 4 bytes at end</span>

<span class="cm">// Remove from front (advance data_off)</span>
<span class="cf">rte_pktmbuf_adj</span>(mbuf, <span class="ck">sizeof</span>(<span class="ck">struct</span> rte_ether_hdr));

<span class="cm">// Free mbuf back to pool</span>
<span class="cf">rte_pktmbuf_free</span>(mbuf);  <span class="cm">// also frees chained segments</span></div>

<table class="t-table">
<thead><tr><th>ol_flags Bit</th><th>Direction</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td><code>RTE_MBUF_F_RX_RSS_HASH</code></td><td>Rx</td><td>NIC computed RSS hash — value in <code>mbuf->hash.rss</code></td></tr>
<tr><td><code>RTE_MBUF_F_RX_IP_CKSUM_GOOD</code></td><td>Rx</td><td>NIC verified IP checksum — correct</td></tr>
<tr><td><code>RTE_MBUF_F_RX_IP_CKSUM_BAD</code></td><td>Rx</td><td>NIC verified IP checksum — bad (drop the packet)</td></tr>
<tr><td><code>RTE_MBUF_F_RX_VLAN</code></td><td>Rx</td><td>VLAN tag present — stripped to <code>mbuf->vlan_tci</code></td></tr>
<tr><td><code>RTE_MBUF_F_TX_IPV4</code></td><td>Tx</td><td>IPv4 packet — required when requesting Tx IP cksum offload</td></tr>
<tr><td><code>RTE_MBUF_F_TX_IP_CKSUM</code></td><td>Tx</td><td>Ask NIC to compute and insert IPv4 header checksum</td></tr>
<tr><td><code>RTE_MBUF_F_TX_TCP_CKSUM</code></td><td>Tx</td><td>Ask NIC to compute and insert TCP checksum</td></tr>
</tbody>
</table>

</div><!-- /t-mbuf -->

<!-- TAB: Chained mbufs -->
<div id="t-chain" class="tab-pane">

<div class="p-teal">
<h4>Chained mbufs — For Jumbo Frames</h4>
A single mbuf data buffer is 2048 bytes by default. Jumbo frames (up to 9000 bytes for 9K MTU) require <strong>chained mbufs</strong> — a linked list of mbufs where <code>mbuf->next</code> points to the continuation segment. The first segment's <code>pkt_len</code> holds the total, <code>nb_segs</code> holds the count.
</div>

<div class="diagram-box">Chained mbuf Layout (jumbo frame example: 5000 bytes)

 Segment 0 (head)          Segment 1               Segment 2
 ┌───────────────────┐     ┌───────────────────┐   ┌───────────────────┐
 │ pkt_len = 5000    │     │ pkt_len = 0        │   │ pkt_len = 0        │
 │ data_len = 1920   │     │ data_len = 1920    │   │ data_len = 1160   │
 │ nb_segs  = 3      │     │ nb_segs  = 0       │   │ nb_segs  = 0      │
 │ next ─────────────┼────►│ next ─────────────┼──►│ next = NULL       │
 │ [packet data...]  │     │ [packet data...]   │   │ [packet data...]  │
 └───────────────────┘     └───────────────────┘   └───────────────────┘
   1920 bytes                 1920 bytes               1160 bytes
   Total: 1920 + 1920 + 1160 = 5000 bytes</div>

<div class="cb"><span class="cm">// Check if mbuf is chained</span>
<span class="ck">if</span> (mbuf-&gt;nb_segs &gt; <span class="cn">1</span>) {
    <span class="cm">// Walk the chain</span>
    <span class="ck">struct</span> rte_mbuf *seg = mbuf;
    <span class="ck">while</span> (seg != NULL) {
        <span class="co">uint8_t</span> *data = <span class="cf">rte_pktmbuf_mtod</span>(seg, <span class="co">uint8_t</span> *);
        <span class="co">uint16_t</span> len  = seg-&gt;data_len;
        <span class="cm">/* process this segment */</span>
        seg = seg-&gt;next;
    }
}

<span class="cm">// Linearize (copy all segments into one) — expensive, avoid on hot path</span>
<span class="ck">char</span> buf[<span class="cn">9000</span>];
<span class="co">uint32_t</span> copied = <span class="cf">rte_pktmbuf_read</span>(mbuf, <span class="cn">0</span>, mbuf-&gt;pkt_len, buf);</div>

<div class="warn">&#9888;&#65039; <strong>Most DPDK applications avoid chained mbufs on the hot path.</strong> The preferred approach is to set <code>RTE_ETH_RX_OFFLOAD_SCATTER</code> and handle multi-segment mbufs only in the exception path. For performance-critical NFs, configure MTU ≤ single-segment buffer size and drop/reject jumbo frames at the port level.</div>

<p class="sep">MBUF CLONE vs REFERENCE COUNT</p>

<div class="p-slate">
<h4>rte_pktmbuf_clone() — Sharing Without Copy</h4>
Cloning creates a new mbuf header that <strong>shares the same data buffer</strong> as the original. The data buffer's reference count (<code>refcnt</code>) is incremented. <code>rte_pktmbuf_free()</code> on either clone decrements <code>refcnt</code> — the data buffer is only returned to the pool when <code>refcnt</code> reaches zero. Use case: multicast — send the same packet out multiple ports without copying the data.
</div>

<div class="cb"><span class="cm">// Clone for multicast (zero-copy)</span>
<span class="ck">struct</span> rte_mbuf *clone = <span class="cf">rte_pktmbuf_clone</span>(original, pool);
<span class="cm">// original->refcnt: 1 → 2 (shared data buffer)</span>

<span class="cf">rte_eth_tx_burst</span>(port_a, <span class="cn">0</span>, &amp;original, <span class="cn">1</span>);  <span class="cm">// refcnt: 2→1 after tx</span>
<span class="cf">rte_eth_tx_burst</span>(port_b, <span class="cn">0</span>, &amp;clone,    <span class="cn">1</span>);  <span class="cm">// refcnt: 1→0 after tx → buffer freed</span></div>

</div><!-- /t-chain -->

<!-- TAB: Interview Q&A -->
<div id="t-qa" class="tab-pane">

<div class="p-slate">
<h4>Q: Why can't DPDK use normal 4KB pages for packet buffers?</h4>
Two reasons: (1) <strong>DMA instability</strong> — 4KB pages can be swapped out by the OS at any time. The NIC's IOVA would become stale, causing DMA writes to wrong memory or segfaults. (2) <strong>TLB pressure</strong> — 1 GB of packet buffers needs 262,144 TLB entries with 4KB pages vs only 512 entries with 2MB hugepages. TLB misses on the hot path at 100G rates would dominate CPU time.
</div>

<div class="p-slate">
<h4>Q: What is the per-lcore cache in rte_mempool and why does it matter?</h4>
The per-lcore cache is a small, lcore-local stack of pre-fetched objects (typically 256 entries). Alloc/free to the lcore cache requires no atomic operations — it's just an array index increment/decrement. Only when the cache empties or overflows does it interact with the common pool ring (one CAS for a bulk transfer). This makes rte_mempool_get/put nearly as cheap as a stack pop on the hot path.
</div>

<div class="p-slate">
<h4>Q: What is rte_pktmbuf_mtod() and how does it work?</h4>
It's a macro: <code>(type)(mbuf->buf_addr + mbuf->data_off)</code>. <code>buf_addr</code> is the pointer to the start of the data buffer. <code>data_off</code> is the byte offset to the first packet byte (defaults to RTE_PKTMBUF_HEADROOM = 128 bytes, leaving space to prepend headers). The result is a typed pointer directly into hugepage memory — no copy, no syscall.
</div>

<div class="p-slate">
<h4>Q: What is headroom in an mbuf and when is it used?</h4>
Headroom is a reserved region at the start of the data buffer, before the packet data. Default: 128 bytes (<code>RTE_PKTMBUF_HEADROOM</code>). It's used when your NF needs to <strong>prepend a header</strong> to an incoming packet — e.g., adding a VXLAN or GRE encapsulation header. Instead of copying the entire packet to a new buffer, you use <code>rte_pktmbuf_prepend()</code> which decrements <code>data_off</code> to expand into the headroom. Zero allocation, zero copy.
</div>

<div class="p-slate">
<h4>Q: What happens when rte_mempool runs out of objects?</h4>
<code>rte_mempool_get()</code> returns -ENOBUFS (non-zero). For pktmbuf pools, the PMD reports this as <code>stats.rx_nombuf</code> and the packet is dropped by the NIC before it reaches the application. This is a critical metric to monitor — it means the application is not returning mbufs to the pool fast enough, or the pool is undersized. Fix: increase pool size, check for mbuf leaks (tx_burst without freeing unsent packets), or reduce processing latency.
</div>

<div class="p-slate">
<h4>Q: What is the difference between pkt_len and data_len?</h4>
<code>data_len</code>: bytes of packet data in <em>this segment only</em>.<br>
<code>pkt_len</code>: total bytes across <em>all segments</em> in the chain (only valid on the first segment/head mbuf).<br>
For single-segment mbufs (the common case), both are equal. For chained mbufs (jumbo frames), pkt_len = sum of all data_len values across all segments.
</div>

</div><!-- /t-qa -->

<!-- TAB: Lab -->
<div id="t-lab" class="tab-pane">

<div class="lab-box">
<div class="lab-hdr">&#128293; Lab 3: mbuf Inspector — Decode Every Field</div>
<div class="lab-body">
<p style="font-size:.87rem;margin:.3rem 0 .8rem">Create a DPDK application that receives one burst of packets and prints every mbuf field. The goal is to see the real hardware values — RSS hash, ol_flags, pkt_len — not just theoretical values.</p>

<div class="lab-step"><span class="sn">1</span><div>Create mempool with <code>rte_pktmbuf_pool_create()</code> on the NIC's socket</div></div>
<div class="lab-step"><span class="sn">2</span><div>Configure port: enable <code>RTE_ETH_RX_OFFLOAD_CHECKSUM</code> and <code>RTE_ETH_RX_OFFLOAD_RSS_HASH</code></div></div>
<div class="lab-step"><span class="sn">3</span><div>Receive one burst: <code>rte_eth_rx_burst(port, 0, pkts, 32)</code></div></div>
<div class="lab-step"><span class="sn">4</span><div>For each received mbuf print: <code>buf_addr</code>, <code>buf_iova</code>, <code>data_off</code>, <code>pkt_len</code>, <code>data_len</code>, <code>nb_segs</code>, <code>port</code>, <code>ol_flags</code> (as hex), <code>hash.rss</code>, <code>vlan_tci</code></div></div>
<div class="lab-step"><span class="sn">5</span><div>Use <code>rte_pktmbuf_mtod()</code> to get Ethernet header — print src and dst MAC</div></div>
<div class="lab-step"><span class="sn">6</span><div>Verify <code>RTE_MBUF_F_RX_IP_CKSUM_GOOD</code> is set on a valid IPv4 packet</div></div>
<div class="lab-step"><span class="sn">7</span><div>Check mempool stats after: <code>rte_mempool_avail_count(pool)</code> — should decrease by nb_rx</div></div>
<div class="lab-step"><span class="sn">8</span><div>Free all mbufs: <code>rte_pktmbuf_free(pkts[i])</code> — verify avail_count restored</div></div>
</div>
</div>

<div class="lab-box">
<div class="lab-hdr">&#128293; Lab 4: Pool Exhaustion Experiment</div>
<div class="lab-body">
<p style="font-size:.87rem;margin:.3rem 0 .8rem">Intentionally exhaust the mempool to observe the imissed counter. This teaches defensive mbuf management.</p>

<div class="lab-step"><span class="sn">1</span><div>Create a <em>small</em> pool: 64 mbufs total</div></div>
<div class="lab-step"><span class="sn">2</span><div>Receive packets in a loop — <strong>do not free them</strong></div></div>
<div class="lab-step"><span class="sn">3</span><div>After pool empties: poll <code>stats.rx_nombuf</code> via <code>rte_eth_stats_get()</code> — observe it increment</div></div>
<div class="lab-step"><span class="sn">4</span><div>Free all held mbufs — observe <code>rx_nombuf</code> stops incrementing</div></div>
<div class="lab-step"><span class="sn">5</span><div><strong>Lesson:</strong> Every code path that receives mbufs MUST free them or return them to TX. Mbuf leaks are the most common DPDK production bug.</div></div>
</div>
</div>

<p class="sep">MASTERY CHECKLIST</p>
<ul class="cl">
<li>Can explain the two reasons DPDK requires hugepages (DMA stability + TLB efficiency)</li>
<li>Can draw the rte_mempool architecture including per-lcore cache and common ring</li>
<li>Can draw the rte_mbuf memory layout with all key fields labeled</li>
<li>Can explain what rte_pktmbuf_mtod() expands to and why it's zero-copy</li>
<li>Can explain headroom: what it is, default value, and when prepend is used</li>
<li>Can explain pkt_len vs data_len and when they differ</li>
<li>Can explain what happens when the mempool runs out and how to diagnose it</li>
<li>Can explain rte_pktmbuf_clone() reference counting semantics</li>
</ul>

</div><!-- /t-lab -->

<div class="mod-nav">
  <a href="/learning/data-plane/dpdk/module-p1-foundation/">&#8592; P1A: Foundation &amp; EAL</a>
  <a href="/learning/data-plane/dpdk/dpdk-roadmap/">&#8593; Roadmap</a>
  <a class="nb" href="/learning/data-plane/dpdk/module-p2-pmd/">P2A: PMD &amp; Port Config &#8594;</a>
</div>

<script>
function vt(e,id){
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  e.target.classList.add('active');
}
</script>
