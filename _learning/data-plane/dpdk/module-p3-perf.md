---
layout: learning
title: "DPDK P3 — Packet Patterns, Tuning & Debugging"
permalink: /learning/data-plane/dpdk/module-p3-perf/
---
<style>
.mod-header{background:linear-gradient(135deg,#1a0800 0%,#3a1200 60%,#6a2800 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#f0a060;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#f0c8a0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#fce0c0}
.tab-bar{display:flex;flex-wrap:wrap;gap:0;background:#3a1200;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#f0a060;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#ffcc80;border-bottom-color:#ffcc80}
.tab-pane{display:none}
.tab-pane.active{display:block}
.p-orange{background:#fdf0e8;border-left:4px solid #c05e1b;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-blue{background:#eaf2fc;border-left:4px solid #2e6da4;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-teal{background:#e8f6f4;border-left:4px solid #1a7a6e;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-slate{background:#f4f6f8;border-left:4px solid #64748b;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
.p-red{background:#fef2f2;border-left:4px solid #dc2626;border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin:.8rem 0}
[data-theme=dark] .p-orange{background:#1e0d00;border-color:#e07830}
[data-theme=dark] .p-blue{background:#0d1e34;border-color:#4a90d9}
[data-theme=dark] .p-teal{background:#0d2020;border-color:#2a9a8e}
[data-theme=dark] .p-slate{background:#1a1e24;border-color:#8898aa}
[data-theme=dark] .p-red{background:#200808;border-color:#dc2626}
.p-orange h4,.p-blue h4,.p-teal h4,.p-slate h4,.p-red h4{margin:0 0 .5rem;font-size:.9rem;font-weight:700}
.ins{background:#e8f5e9;border:1px solid #66bb6a;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.warn{background:#fff8e1;border:1px solid #ffca28;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
.note{background:#e3f2fd;border:1px solid #42a5f5;border-radius:8px;padding:.8rem 1rem;margin:.8rem 0;font-size:.88rem}
[data-theme=dark] .ins{background:#0d2010;border-color:#388e3c}
[data-theme=dark] .warn{background:#1e1800;border-color:#f9a825}
[data-theme=dark] .note{background:#0d1e2e;border-color:#1976d2}
.cb{background:#0d1117;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;font-family:monospace;font-size:.82rem;line-height:1.7;color:#e6edf3;white-space:pre-wrap}
.cb .cm{color:#8b949e}.cb .ck{color:#ff7b72}.cb .cv{color:#79c0ff}.cb .cs{color:#a5d6ff}.cb .cn{color:#f2cc60}.cb .cf{color:#d2a8ff}.cb .co{color:#ffa657}.cb .cg{color:#3fb950}
.t-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.8rem 0}
.t-table th{background:#3a1200;color:#f0a060;font-family:monospace;font-size:.75rem;font-weight:700;padding:.5rem .7rem;text-align:left;border-bottom:2px solid #6a2800}
.t-table td{padding:.45rem .7rem;border-bottom:1px solid var(--border-color,#e8e8e8);vertical-align:top}
.t-table tr:last-child td{border-bottom:none}
.t-table tr:hover td{background:var(--bg-color,#f8f9fa)}
.diagram-box{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;font-family:monospace;font-size:.78rem;line-height:1.8;color:#c9d1d9;overflow-x:auto;white-space:pre}
.lab-box{background:var(--card-bg,#fff);border:2px solid #c05e1b;border-radius:10px;overflow:hidden;margin:1rem 0}
.lab-hdr{background:#3a1200;color:#fff;padding:.7rem 1.2rem;font-weight:700;font-family:monospace;font-size:.9rem}
.lab-body{padding:1rem 1.2rem}
.lab-step{display:flex;gap:.8rem;margin-bottom:.5rem;font-size:.87rem}
.sn{background:#c05e1b;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.7rem;font-weight:800;flex-shrink:0;margin-top:.1rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{padding:.3rem 0;font-size:.87rem;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:"☐ ";font-size:1rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#3a1200;color:#fff !important;border-color:#3a1200}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">DPDK MASTERY · PHASE 3 OF 3 · MODULE B</div>
  <div class="mod-title">Packet Patterns, Tuning &amp; Debugging</div>
  <div class="mod-subtitle">Prefetching · batching · CPU isolation · hugepage sizing · benchmarking · pitfall diagnosis</div>
  <div class="mod-pills">
    <span class="mod-pill">Ch 16 — Packet Processing Patterns</span>
    <span class="mod-pill">Ch 17 — Performance Tuning</span>
    <span class="mod-pill">Ch 18 — Debugging &amp; Pitfalls</span>
    <span class="mod-pill">C · perf · pktgen · SASE-DP</span>
    <span class="mod-pill">Weeks 13–14+</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t-patterns')">Packet Patterns</button>
  <button class="tab-btn" onclick="vt(event,'t-prefetch')">Prefetching</button>
  <button class="tab-btn" onclick="vt(event,'t-tuning')">CPU Tuning</button>
  <button class="tab-btn" onclick="vt(event,'t-bench')">Benchmarking</button>
  <button class="tab-btn" onclick="vt(event,'t-debug')">Debugging</button>
  <button class="tab-btn" onclick="vt(event,'t-pitfalls')">Common Pitfalls</button>
  <button class="tab-btn" onclick="vt(event,'t-qa')">Interview Q&amp;A</button>
  <button class="tab-btn" onclick="vt(event,'t-lab')">Lab &amp; Checklist</button>
</div>

<!-- TAB: Packet Patterns -->
<div id="t-patterns" class="tab-pane active">

<p class="sep">CANONICAL PACKET PROCESSING PATTERNS</p>

<div class="p-orange">
<h4>Pattern 1: Receive → Process → Transmit (Basic RTC)</h4>
The simplest pattern. Each lcore handles one or more NIC queues. Good for stateless forwarding, filtering, and routing.
</div>

<div class="cb"><span class="cm">// Pattern 1: Basic receive-process-transmit</span>
<span class="ck">static</span> <span class="co">int</span> <span class="cf">lcore_main</span>(<span class="ck">void</span> *arg) {
    <span class="co">uint16_t</span> port = (<span class="co">uintptr_t</span>)arg;
    <span class="co">uint16_t</span> queue = <span class="cf">rte_lcore_id</span>();
    <span class="ck">struct</span> rte_mbuf *pkts[<span class="cn">BURST_SIZE</span>];

    <span class="ck">while</span> (<span class="cn">1</span>) {
        <span class="co">uint16_t</span> nb_rx = <span class="cf">rte_eth_rx_burst</span>(port, queue, pkts, <span class="cn">BURST_SIZE</span>);
        <span class="ck">if</span> (<span class="cf">unlikely</span>(nb_rx == <span class="cn">0</span>)) <span class="ck">continue</span>;

        <span class="ck">for</span> (<span class="co">uint16_t</span> i = <span class="cn">0</span>; i &lt; nb_rx; i++)
            <span class="cf">process_packet</span>(pkts[i]);

        <span class="co">uint16_t</span> nb_tx = <span class="cf">rte_eth_tx_burst</span>(port ^ <span class="cn">1</span>, queue, pkts, nb_rx);
        <span class="ck">for</span> (<span class="co">uint16_t</span> i = nb_tx; i &lt; nb_rx; i++)
            <span class="cf">rte_pktmbuf_free</span>(pkts[i]);  <span class="cm">// free unsent</span>
    }
    <span class="ck">return</span> <span class="cn">0</span>;
}</div>

<div class="p-teal">
<h4>Pattern 2: Batch Processing with Classification</h4>
Classify the entire burst first, then process each category. Better cache utilization — same code path runs on multiple packets before switching to the next path (instruction cache stays warm).
</div>

<div class="cb"><span class="cm">// Pattern 2: classify burst → process by type</span>
<span class="ck">struct</span> rte_mbuf *tcp_pkts[<span class="cn">BURST_SIZE</span>], *udp_pkts[<span class="cn">BURST_SIZE</span>], *other[<span class="cn">BURST_SIZE</span>];
<span class="co">uint16_t</span> nb_tcp = <span class="cn">0</span>, nb_udp = <span class="cn">0</span>, nb_other = <span class="cn">0</span>;

<span class="ck">for</span> (<span class="co">uint16_t</span> i = <span class="cn">0</span>; i &lt; nb_rx; i++) {
    <span class="ck">struct</span> rte_ipv4_hdr *ip = <span class="cf">rte_pktmbuf_mtod_offset</span>(pkts[i], <span class="ck">struct</span> rte_ipv4_hdr *,
                                                       <span class="ck">sizeof</span>(<span class="ck">struct</span> rte_ether_hdr));
    <span class="ck">if</span>      (ip-&gt;next_proto_id == <span class="cn">IPPROTO_TCP</span>) tcp_pkts[nb_tcp++] = pkts[i];
    <span class="ck">else if</span> (ip-&gt;next_proto_id == <span class="cn">IPPROTO_UDP</span>) udp_pkts[nb_udp++] = pkts[i];
    <span class="ck">else</span>                                         other[nb_other++]   = pkts[i];
}

<span class="cf">process_tcp_batch</span>(tcp_pkts, nb_tcp);    <span class="cm">// one code path, warm I-cache</span>
<span class="cf">process_udp_batch</span>(udp_pkts, nb_udp);
<span class="cf">rte_pktmbuf_free_bulk</span>(other, nb_other); <span class="cm">// drop unknown</span></div>

</div><!-- /t-patterns -->

<!-- TAB: Prefetching -->
<div id="t-prefetch" class="tab-pane">

<div class="p-orange">
<h4>Software Prefetching — The 4-Packet Lookahead</h4>
At 100G/64B, CPU has ~6.7 ns per packet. An L3 cache miss costs ~40 cycles (~13 ns) — more than the entire packet budget. Prefetching hides this latency by telling the CPU to fetch data for a future packet while processing the current one.
</div>

<div class="note">&#128204; <strong>Prefetch distance:</strong> Typically 4 packets ahead. Too small = cache miss still hurts. Too large = cache pollution (prefetched data evicted before used). 4 is the DPDK convention validated across Intel E810, i40e, and mlx5.</div>

<div class="cb"><span class="cm">// 4-packet prefetch pattern — the DPDK standard technique</span>
<span class="ck">for</span> (<span class="co">uint16_t</span> i = <span class="cn">0</span>; i &lt; nb_rx; i++) {
    <span class="cm">/* Prefetch 4 packets ahead: fetch the mbuf header */</span>
    <span class="ck">if</span> (i + <span class="cn">4</span> &lt; nb_rx)
        <span class="cf">rte_prefetch0</span>(<span class="cf">rte_pktmbuf_mtod</span>(pkts[i + <span class="cn">4</span>], <span class="ck">void</span> *));

    <span class="cm">/* Process current packet — prefetch for i+4 is in flight */</span>
    <span class="ck">struct</span> rte_ether_hdr *eth = <span class="cf">rte_pktmbuf_mtod</span>(pkts[i], <span class="ck">struct</span> rte_ether_hdr *);
    <span class="cm">/* ... process packet[i] ... */</span>
}

<span class="cm">// rte_prefetch0 = prefetch to L1 cache (highest priority)</span>
<span class="cm">// rte_prefetch1 = prefetch to L2 cache</span>
<span class="cm">// rte_prefetch2 = prefetch to L3 cache</span>
<span class="cm">// Use prefetch0 for hot packet data — you'll access it very soon</span></div>

<div class="p-teal">
<h4>What to Prefetch</h4>
<ul style="margin:.3rem 0 0;font-size:.87rem;line-height:1.8">
<li><strong>Packet data</strong>: <code>rte_pktmbuf_mtod(pkts[i+4], void*)</code> — the Ethernet/IP/TCP header bytes</li>
<li><strong>Flow table entry</strong>: if doing hash lookup, prefetch the expected hash bucket for the next packet before doing the lookup for the current packet</li>
<li><strong>mbuf metadata</strong>: <code>rte_prefetch0(pkts[i+4])</code> — prefetch the mbuf struct itself if you access many fields</li>
</ul>
Do NOT prefetch unconditionally for every array position — only prefetch data you will actually access soon.
</div>

</div><!-- /t-prefetch -->

<!-- TAB: CPU Tuning -->
<div id="t-tuning" class="tab-pane">

<p class="sep">SYSTEM-LEVEL TUNING FOR DPDK</p>

<table class="t-table">
<thead><tr><th>Tuning Area</th><th>Command / Setting</th><th>Effect</th></tr></thead>
<tbody>
<tr><td><strong>CPU isolation</strong></td><td><code>isolcpus=4-15</code> in kernel cmdline</td><td>Removes cpus 4-15 from OS scheduler — dedicated to DPDK polling lcores</td></tr>
<tr><td><strong>IRQ affinity</strong></td><td><code>irqbalance --banirq=&lt;irqs&gt;</code> or <code>/proc/irq/N/smp_affinity</code></td><td>Move NIC IRQs away from DPDK lcores (IRQs still fire on control plane CPUs)</td></tr>
<tr><td><strong>CPU frequency scaling</strong></td><td><code>cpupower frequency-set -g performance</code></td><td>Disable P-states / frequency scaling — DPDK needs consistent cycle budget</td></tr>
<tr><td><strong>Turbo Boost</strong></td><td><code>echo 1 &gt; /sys/devices/system/cpu/intel_pstate/no_turbo</code></td><td>Disable turbo for consistent throughput (turbo causes frequency jumps → latency variance)</td></tr>
<tr><td><strong>Hugepages at boot</strong></td><td><code>hugepagesz=2M hugepages=2048</code> in kernel cmdline</td><td>Pre-allocate at boot — avoids fragmentation that makes runtime allocation fail</td></tr>
<tr><td><strong>NUMA balancing</strong></td><td><code>echo 0 &gt; /proc/sys/kernel/numa_balancing</code></td><td>Disable automatic NUMA page migration — DPDK pages must stay pinned</td></tr>
<tr><td><strong>Transparent hugepages</strong></td><td><code>echo never &gt; /sys/kernel/mm/transparent_hugepage/enabled</code></td><td>Disable THP — it can cause latency spikes when pages are promoted/demoted</td></tr>
</tbody>
</table>

<div class="ins">&#9989; <strong>Production checklist for 100G DPDK on dual-socket server:</strong>
Isolate DPDK lcores with <code>isolcpus</code> → set <code>performance</code> governor → disable turbo → pre-allocate hugepages at boot → disable NUMA balancing → disable transparent hugepages → bind NIC to vfio-pci → verify all DPDK lcores and mempool on same NUMA socket as NIC.</div>

<p class="sep">BURST SIZE TUNING APPROACH</p>

<div class="cb"><span class="cm">// Measure throughput vs latency at different burst sizes using rte_rdtsc()</span>
<span class="co">uint64_t</span> t0 = <span class="cf">rte_rdtsc</span>();
<span class="co">uint16_t</span> nb_rx = <span class="cf">rte_eth_rx_burst</span>(port, queue, pkts, burst_size);
<span class="co">uint64_t</span> rx_cycles = <span class="cf">rte_rdtsc</span>() - t0;

<span class="co">uint64_t</span> t1 = <span class="cf">rte_rdtsc</span>();
<span class="ck">for</span> (<span class="co">uint16_t</span> i = <span class="cn">0</span>; i &lt; nb_rx; i++) <span class="cf">process_packet</span>(pkts[i]);
<span class="co">uint64_t</span> proc_cycles = <span class="cf">rte_rdtsc</span>() - t1;

<span class="cm">// Track per-packet cycle budget: proc_cycles / nb_rx</span>
<span class="cm">// At 3GHz, 6.7ns budget = 20 cycles per packet at 100G/64B</span></div>

</div><!-- /t-tuning -->

<!-- TAB: Benchmarking -->
<div id="t-bench" class="tab-pane">

<div class="p-orange">
<h4>DPDK Testpmd — Built-In Benchmark Tool</h4>
<code>dpdk-testpmd</code> is DPDK's reference forwarding application for benchmarking NIC and PMD performance. Always establish a testpmd baseline before profiling your own application.
</div>

<div class="cb"><span class="cm"># Start testpmd in io forwarding mode (max throughput benchmark)</span>
dpdk-testpmd -l 0-3 -n 4 -a 0000:03:00.0 -- \
    --nb-cores=2 --rxq=2 --txq=2 \
    --burst=32 --forward-mode=io \
    --auto-start

<span class="cm"># In testpmd CLI:</span>
show port stats all     <span class="cm"># throughput + packet counts</span>
show port xstats all    <span class="cm"># extended NIC counters (imissed, nombuf, etc.)</span>
show fwd stats all      <span class="cm"># forwarding engine stats</span>
clear port stats all    <span class="cm"># reset counters</span></div>

<p class="sep">KEY BENCHMARK METRICS</p>

<table class="t-table">
<thead><tr><th>Metric</th><th>Tool</th><th>Healthy Range</th><th>Concern</th></tr></thead>
<tbody>
<tr><td>RX throughput (Mpps)</td><td>testpmd stats</td><td>Near line rate</td><td>More than 5% below line rate</td></tr>
<tr><td><code>imissed</code></td><td><code>show port xstats</code></td><td>0</td><td>Any non-zero = ring full → drops</td></tr>
<tr><td><code>rx_nombuf</code></td><td><code>show port xstats</code></td><td>0</td><td>Any non-zero = mbuf leak or pool too small</td></tr>
<tr><td>CPU utilization</td><td><code>top -H</code> or <code>htop</code></td><td>~100% on DPDK lcores</td><td>Below 99% = wasted polling; above 100% = overload</td></tr>
<tr><td>NUMA local memory %</td><td><code>numastat -p &lt;pid&gt;</code></td><td>&gt;99%</td><td>High remote% = cross-NUMA allocation bug</td></tr>
<tr><td>Per-packet cycles</td><td><code>rte_rdtsc()</code> delta / nb_rx</td><td>Depends on NF complexity</td><td>Compare to 100G budget: ~20 cycles/packet</td></tr>
</tbody>
</table>

<div class="cb"><span class="cm"># Profile DPDK application with perf</span>
perf stat -C 4,5,6,7 -e cycles,instructions,cache-misses,LLC-load-misses \
    -p $(pgrep my_dpdk_app) sleep 10

<span class="cm"># LLC-load-misses high → data not cache-resident → check NUMA alignment</span>
<span class="cm"># High IPC (instructions/cycle) → good — compute-bound, not memory-bound</span>
<span class="cm"># Low IPC → memory-bound → check hugepages, prefetching, NUMA</span></div>

</div><!-- /t-bench -->

<!-- TAB: Debugging -->
<div id="t-debug" class="tab-pane">

<p class="sep">DPDK DEBUGGING TOOLKIT</p>

<div class="p-red">
<h4>Symptom: Application Stops Receiving Packets</h4>
<strong>Diagnosis steps (in order):</strong>
<ol style="margin:.3rem 0 0;font-size:.87rem;line-height:1.8">
<li>Check <code>stats.imissed</code> — if non-zero: ring full, application too slow. Increase nb_rx_desc or add lcores.</li>
<li>Check <code>stats.rx_nombuf</code> — if non-zero: mempool exhausted. Find the mbuf leak.</li>
<li>Check <code>rte_mempool_avail_count(pool)</code> over time — if it trends to zero: leak confirmed.</li>
<li>Check all code paths: every <code>rx_burst</code> must eventually <code>rte_pktmbuf_free()</code> or <code>tx_burst</code> with free of unsent.</li>
</ol>
</div>

<div class="cb"><span class="cm">// Mbuf accounting helper — call periodically</span>
<span class="ck">void</span> <span class="cf">check_pool_health</span>(<span class="ck">struct</span> rte_mempool *pool, <span class="ck">const</span> <span class="ck">char</span> *tag) {
    <span class="co">unsigned</span> avail = <span class="cf">rte_mempool_avail_count</span>(pool);
    <span class="co">unsigned</span> total = <span class="cf">rte_mempool_in_use_count</span>(pool) + avail;
    <span class="co">float</span>    used_pct = (<span class="co">float</span>)(total - avail) * <span class="cn">100.0</span>f / total;
    <span class="cf">printf</span>(<span class="cs">"[%s] Pool avail: %u/%u (%.1f%% in use)\n"</span>, tag, avail, total, used_pct);
    <span class="ck">if</span> (used_pct &gt; <span class="cn">90.0</span>f)
        <span class="cf">RTE_LOG</span>(<span class="cn">WARNING</span>, USER1, <span class="cs">"Pool nearly exhausted — check for mbuf leaks!\n"</span>);
}</div>

<p class="sep">DPDK LOGGING</p>

<div class="cb"><span class="cm">// Log levels: EMERG(1) ALERT(2) CRIT(3) ERR(4) WARNING(5) NOTICE(6) INFO(7) DEBUG(8)</span>
<span class="cf">rte_log_set_level</span>(<span class="cf">RTE_LOGTYPE_USER1</span>, <span class="cn">RTE_LOG_DEBUG</span>);

<span class="cm">// Log from your application</span>
<span class="cf">RTE_LOG</span>(<span class="cn">INFO</span>,    <span class="cn">USER1</span>, <span class="cs">"Port %u: %u packets received\n"</span>, port_id, nb_rx);
<span class="cf">RTE_LOG</span>(<span class="cn">WARNING</span>, <span class="cn">USER1</span>, <span class="cs">"Tx ring full on port %u queue %u\n"</span>, port_id, queue_id);
<span class="cf">RTE_LOG</span>(<span class="cn">ERR</span>,     <span class="cn">USER1</span>, <span class="cs">"Mbuf pool exhausted: avail=%u\n"</span>, avail);

<span class="cm">// Enable PMD debug logging at startup</span>
<span class="cm">// ./my_app --log-level=pmd:8    (debug for all PMDs)</span>
<span class="cm">// ./my_app --log-level=pmd.net.mlx5:8  (debug for mlx5 PMD only)</span></div>

</div><!-- /t-debug -->

<!-- TAB: Common Pitfalls -->
<div id="t-pitfalls" class="tab-pane">

<p class="sep">THE DPDK PRODUCTION PITFALL CATALOG</p>

<table class="t-table">
<thead><tr><th>#</th><th>Pitfall</th><th>Symptom</th><th>Root Cause</th><th>Fix</th></tr></thead>
<tbody>
<tr><td>1</td><td><strong>Mbuf leak</strong></td><td>rx_nombuf increments; app stops receiving</td><td>tx_burst doesn't free unsent pkts; early-return without free</td><td>Always free <code>pkts[nb_tx..n-1]</code> after tx_burst; audit every return path</td></tr>
<tr><td>2</td><td><strong>Non-power-of-2 workers</strong></td><td>CPU load imbalance; throughput ceiling</td><td>RETA divided unevenly across workers</td><td>Always use power-of-2 worker count or manually program RETA</td></tr>
<tr><td>3</td><td><strong>Cross-NUMA allocation</strong></td><td>Lower throughput than testpmd baseline; high LLC misses</td><td>Mempool/ring/queue on wrong socket</td><td>Always use <code>rte_eth_dev_socket_id(port)</code> for pool and queue setup</td></tr>
<tr><td>4</td><td><strong>Secondary calls pool_create</strong></td><td>EEXIST error; secondary crashes at startup</td><td>Secondary tries to create pool already owned by primary</td><td>Always use <code>rte_mempool_lookup()</code> in secondary processes</td></tr>
<tr><td>5</td><td><strong>Accessing mbuf after tx_burst</strong></td><td>Random data corruption; segfaults</td><td>PMD frees mbuf asynchronously after tx_burst</td><td>Never access an mbuf after passing it to tx_burst</td></tr>
<tr><td>6</td><td><strong>Hugepages not allocated at boot</strong></td><td>EAL init fails; "Cannot reserve memory" error</td><td>Runtime hugepage allocation fails due to memory fragmentation</td><td>Always pre-allocate hugepages in kernel cmdline: <code>hugepages=N</code></td></tr>
<tr><td>7</td><td><strong>Small mempool + large descriptor ring</strong></td><td>rx_nombuf immediately at startup</td><td>Pool smaller than ring × number of queues × burst_size</td><td>Pool size must be &gt; (nb_rx_desc × nb_rx_queues × 2) — leave 2× headroom</td></tr>
<tr><td>8</td><td><strong>Missing tx_free after ring full</strong></td><td>Slow mbuf leak; intermittent rx_nombuf</td><td>tx_burst returns nb_tx &lt; nb_pkts; caller doesn't free excess</td><td>Always check: <code>if (nb_tx &lt; nb_pkts) rte_pktmbuf_free_bulk(pkts+nb_tx, nb_pkts-nb_tx)</code></td></tr>
<tr><td>9</td><td><strong>False sharing on per-lcore counters</strong></td><td>Lower throughput than expected; perf shows cache-to-cache transfers</td><td>Per-lcore stats arrays not cache-line aligned</td><td>Use <code>__rte_cache_aligned</code> on per-lcore structs</td></tr>
<tr><td>10</td><td><strong>CPU not isolated</strong></td><td>High latency variance; p99 much higher than p50</td><td>OS scheduler interrupts DPDK polling lcores</td><td>Add <code>isolcpus=&lt;dpdk-cores&gt;</code> to kernel cmdline</td></tr>
</tbody>
</table>

<div class="warn">&#9888;&#65039; <strong>Pitfall #7 — Pool Sizing Formula:</strong> Minimum pool size = <code>nb_rx_desc × nb_rx_queues + nb_tx_desc × nb_tx_queues + nb_lcores × cache_size + burst_size</code>. Add 2× safety margin. Use 8191 (not 8192 — rte_mempool adjusts to power-of-2 minus one internally).</div>

</div><!-- /t-pitfalls -->

<!-- TAB: Interview Q&A -->
<div id="t-qa" class="tab-pane">

<div class="p-slate">
<h4>Q: What is software prefetching in DPDK and how many packets ahead should you prefetch?</h4>
Software prefetching tells the CPU to load a cache line into cache before the data is needed, hiding the ~13 ns L3 miss latency. The standard DPDK pattern prefetches 4 packets ahead: while processing packet <em>i</em>, issue <code>rte_prefetch0(rte_pktmbuf_mtod(pkts[i+4], void*))</code>. By the time processing of packets i+1 through i+3 completes, packet i+4's data is in L1 cache with near-zero access cost. Too small (1-2) = miss still hurts; too large (8+) = data evicted before use.
</div>

<div class="p-slate">
<h4>Q: How do you diagnose and fix high imissed counter?</h4>
<code>imissed</code> means the NIC dropped packets because the Rx ring had no empty descriptors — software was too slow to drain it. Diagnosis: confirm with <code>rte_eth_stats_get()</code> and observe it incrementing under load. Fixes (in order of impact): (1) Increase <code>nb_rx_desc</code> (bigger ring = more burst capacity); (2) Increase burst size so each rx_burst call drains more; (3) Reduce per-packet processing time; (4) Add more worker lcores via rte_distributor.
</div>

<div class="p-slate">
<h4>Q: What is the DPDK pool sizing formula?</h4>
Minimum pool size = (nb_rx_desc × nb_rx_queues) + (nb_tx_desc × nb_tx_queues) + (nb_lcores × cache_size) + burst_size, multiplied by a safety margin of ~2×. The rx_desc slots need mbufs to refill; tx_desc slots hold mbufs until NIC sends them; the per-lcore cache pre-fetches from the common pool. Undersized pools cause immediate rx_nombuf at startup under load.
</div>

<div class="p-slate">
<h4>Q: What does CPU isolation (isolcpus) do and why does DPDK need it?</h4>
<code>isolcpus=4-15</code> in the kernel boot parameters removes CPUs 4-15 from the OS scheduler's CPU pool. No kernel threads, IRQs, or user-space tasks will be scheduled on those CPUs without explicit affinity pinning. DPDK needs this because its polling loops must run continuously — even a 1 ms scheduler preemption loses ~148,000 packets at 100G/64B. With isolcpus, DPDK lcores run uninterrupted at 100% CPU consumption, which is intentional and correct.
</div>

<div class="p-slate">
<h4>Q: How do you find a mbuf leak in a DPDK application?</h4>
(1) Monitor <code>rte_mempool_avail_count(pool)</code> over time — a leak shows as a monotonic decrease toward zero. (2) Check <code>stats.rx_nombuf</code> — when it becomes non-zero, the pool is exhausted. (3) Audit every code path: every packet received via rx_burst must eventually be freed via rte_pktmbuf_free() or passed to tx_burst with unsent packets freed. Common sources: early return on error without freeing; tx_burst return value not checked; chained mbufs partially freed.
</div>

</div><!-- /t-qa -->

<!-- TAB: Lab & Checklist -->
<div id="t-lab" class="tab-pane">

<div class="lab-box">
<div class="lab-hdr">&#128293; Lab 10: End-to-End URL Filter Dataplane Skeleton</div>
<div class="lab-body">
<p style="font-size:.87rem;margin:.3rem 0 .8rem">Build a minimal version of the SASE-DP URL filter pipeline: RX → DNS extract → allow/block decision → TX or DROP. Apply all Phase 3 techniques.</p>

<div class="lab-step"><span class="sn">1</span><div><strong>Setup:</strong> Primary process owns NIC, creates pool and distributor with 4 workers. Apply isolcpus tuning.</div></div>
<div class="lab-step"><span class="sn">2</span><div><strong>RX coordinator:</strong> rx_burst → set hash.usr = hash.rss → distributor_process()</div></div>
<div class="lab-step"><span class="sn">3</span><div><strong>Worker loop:</strong> distributor_get_pkt() → classify packet type (DNS/UDP/53, HTTP/TCP/80, HTTPS/TCP/443, other) → route to processing function</div></div>
<div class="lab-step"><span class="sn">4</span><div><strong>DNS processing:</strong> parse UDP payload → extract queried domain name → check against a simple blocked-domain hash table (use rte_hash)</div></div>
<div class="lab-step"><span class="sn">5</span><div><strong>Add prefetch:</strong> prefetch packet data 4 ahead in the worker loop</div></div>
<div class="lab-step"><span class="sn">6</span><div><strong>Add pool health monitoring:</strong> every 1M packets, log avail_count and verify no leak</div></div>
<div class="lab-step"><span class="sn">7</span><div><strong>Benchmark:</strong> run dpdk-testpmd baseline, then your filter, compare throughput and imissed</div></div>
<div class="lab-step"><span class="sn">8</span><div><strong>Add rte_flow rule:</strong> steer DNS traffic (UDP/53) to queue 0 in hardware — measure CPU % reduction</div></div>
</div>
</div>

<p class="sep">FULL DPDK MASTERY CHECKLIST</p>

<div style="font-size:.8rem;font-family:monospace;color:var(--light-text,#666);margin-bottom:.5rem">Phase 1 — Foundation &amp; Memory</div>
<ul class="cl">
<li>Explain 6 categories of kernel overhead and DPDK's solution for each</li>
<li>Draw DPDK software stack from NIC hardware to user application</li>
<li>Explain EAL init: hugepages, lcore pinning, PCI probe</li>
<li>Explain hugepages: why needed, DMA stability, TLB efficiency</li>
<li>Draw rte_mempool architecture: per-lcore cache + common ring</li>
<li>Draw rte_mbuf layout: all key fields including buf_addr, data_off, pkt_len, ol_flags</li>
<li>Explain rte_pktmbuf_mtod() — what it expands to, why it's zero-copy</li>
</ul>

<div style="font-size:.8rem;font-family:monospace;color:var(--light-text,#666);margin:.8rem 0 .5rem">Phase 2 — Core Mechanics</div>
<ul class="cl">
<li>Explain DD bit — what it is, why polling beats interrupts</li>
<li>Draw Rx descriptor ring lifecycle (6 steps)</li>
<li>Write safe tx_burst with unsent-packet free pattern</li>
<li>List 10-step port configuration sequence in order</li>
<li>Explain RSS: Toeplitz hash, RETA, symmetric key, power-of-2 requirement</li>
<li>Draw rte_ring CAS protocol for MPMC enqueue</li>
<li>Explain bulk vs burst semantics, SPSC vs MPMC tradeoffs</li>
<li>Compare run-to-completion vs pipeline architectures</li>
</ul>

<div style="font-size:.8rem;font-family:monospace;color:var(--light-text,#666);margin:.8rem 0 .5rem">Phase 3 — Advanced &amp; Production</div>
<ul class="cl">
<li>Explain primary/secondary model — who creates, who looks up, gotchas</li>
<li>Write a complete rte_flow rule (pattern + action + validate + create)</li>
<li>Explain NUMA remote access penalty and correct allocation pattern</li>
<li>Explain false sharing and demonstrate __rte_cache_aligned fix</li>
<li>Explain 4-packet prefetch pattern — what to prefetch, why 4 ahead</li>
<li>Diagnose imissed vs rx_nombuf: different causes and different fixes</li>
<li>Apply production tuning: isolcpus, performance governor, NUMA balancing off</li>
<li>Identify and fix all 10 pitfalls in the production pitfall catalog</li>
</ul>

</div><!-- /t-lab -->

<div class="mod-nav">
  <a href="{{ '/learning/data-plane/dpdk/module-p3-advanced/' | relative_url }}">&#8592; P3A: Multi-Process &amp; rte_flow</a>
  <a href="{{ '/learning/data-plane/dpdk/dpdk-roadmap/' | relative_url }}">&#8593; DPDK Roadmap</a>
  <a class="nb" href="{{ '/learning/data-plane/dpdk/' | relative_url }}">DPDK Hub &#8594;</a>
</div>

<script>
function vt(e,id){
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  e.target.classList.add('active');
}
</script>
