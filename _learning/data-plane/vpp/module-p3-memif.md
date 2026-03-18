---
layout: default
title: "VPP P3B - memif and Shared Memory Interfaces"
permalink: /learning/data-plane/vpp/module-p3-memif/
---
<style>
.mod-header{background:linear-gradient(135deg,#0d1b2a 0%,#1a3a5c 60%,#5b3a8c 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#c0a8e8;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#d8c8f4;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ecdcff}
.tab-bar{display:flex;flex-wrap:wrap;background:#0d1b2a;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}.tab-btn.active{color:#b090e8;border-bottom-color:#b090e8}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.3rem}
.p-blue .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue .cp-hdr{background:#0d2030}
.p-teal .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}
.cb{background:#0d1b2a;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #5b3a8c}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#dcd0f8;white-space:pre}
.cm{color:#6a5a80}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.dpdk-box{background:#f0ecf8;border:1.5px solid #9b7bd0;border-left:4px solid #5b3a8c;border-radius:8px;padding:1rem 1.2rem;margin:1rem 0}
[data-theme=dark] .dpdk-box{background:#1a1028;border-color:#7060a8;border-left-color:#9b7bd0}
.dpdk-box .dh{font-size:.72rem;font-family:monospace;font-weight:700;letter-spacing:.08em;color:#5b3a8c;margin-bottom:.5rem;text-transform:uppercase}
[data-theme=dark] .dpdk-box .dh{color:#b090e8}
.dpdk-box ul{margin:0;padding-left:1.2rem}
.dpdk-box li{font-size:.87rem;line-height:1.65;color:var(--text-color,#222);margin-bottom:.25rem}
.ins{background:#e8f5f0;border:1.5px solid #1a7a6e;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2420;border-color:#2a9a8e}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#0e5248}[data-theme=dark] .ins strong{color:#5dd6c8}
.api-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.86rem}
.api-table th{background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.api-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.api-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.api-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a7a6e}
.proj-box{border:2px solid #5b3a8c;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.proj-hdr{background:#5b3a8c;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.proj-hdr .pn{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.proj-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.proj-body{padding:1.1rem 1.2rem}
.proj-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.ps{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.ps:last-of-type{border-bottom:none}
.ps .sn{background:#5b3a8c;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1a7a6e;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">VPP MASTERY · PHASE 3B · WEEKS 10–11</div>
  <div class="mod-title">🔗 memif - Shared Memory Interface</div>
  <div class="mod-subtitle">Server/client roles · Unix socket control path · Zero-copy shared memory · libmemif · DPDK net_memif PMD</div>
  <div class="mod-pills">
    <span class="mod-pill">src/plugins/memif/</span>
    <span class="mod-pill">extras/libmemif/</span>
    <span class="mod-pill">net_memif PMD</span>
    <span class="mod-pill">Project 5</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'ta')">Architecture</button>
  <button class="tab-btn" onclick="vt(event,'tb')">Shared Memory Layout</button>
  <button class="tab-btn" onclick="vt(event,'tc')">VPP CLI Setup</button>
  <button class="tab-btn" onclick="vt(event,'td')">libmemif API</button>
  <button class="tab-btn" onclick="vt(event,'te')">DPDK net_memif PMD</button>
  <button class="tab-btn" onclick="vt(event,'tf')">Project 5</button>
  <button class="tab-btn" onclick="vt(event,'tg')">Checklist</button>
</div>

<div id="ta" class="tab-pane active">
<p class="sep">MEMIF ARCHITECTURE</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🧩</span><h3>memif Design - Control Plane vs Data Plane</h3><span class="tag tag-purple">ARCHITECTURE</span></div>
  <div class="cp-body">
    <p>memif (memory interface) is a shared-memory, zero-copy interface for connecting two processes - most commonly two VPP instances or VPP + a DPDK application. It is the highest-performance inter-process interface available for container-to-container packet forwarding.</p>
    <p>memif has a strict two-plane design:</p>
    <ul>
      <li><strong>Control plane (Unix socket):</strong> Used once during connection setup. A <em>server</em> listens on a Unix socket; a <em>client</em> connects. They exchange memif_msg_t messages to negotiate region count, queue count, ring size, and buffer size. After handshake, the socket is idle.</li>
      <li><strong>Data plane (shared memory):</strong> After handshake, both sides mmap the same physical memory regions. TX/RX rings (ring buffers of memif_desc_t descriptors) in this shared memory allow zero-copy packet passing - no copies, no system calls, no kernel involvement.</li>
    </ul>
<div class="cb"><pre><span class="cm">/* memif topology */</span>

Process A (VPP master)              Process B (VPP slave / DPDK app)
┌──────────────────────┐            ┌──────────────────────┐
│  memif server        │            │  memif client        │
│  listen(/run/vpp/m0) │←─socket──→│  connect(/run/vpp/m0)│
│                      │  handshake │                      │
│  [shared mem region] │←─mmap────→│  [shared mem region] │
│  TX ring (A→B)       │            │  RX ring (reads A→B) │
│  RX ring (B→A)       │            │  TX ring (writes B→A)│
└──────────────────────┘            └──────────────────────┘

<span class="cm">/* Key properties */</span>
Zero copies:   packet data never leaves shared memory
No syscalls:   data path uses only memory reads/writes
Interrupt mode: optionally signal peer via eventfd (avoids busy poll)
Blocking:      VPP always uses polling (same as DPDK)</pre></div>
  </div>
</div>
</div>

<div id="tb" class="tab-pane">
<p class="sep">SHARED MEMORY RING LAYOUT</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🧮</span><h3>memif Ring and Descriptor Structure</h3><span class="tag tag-blue">INTERNALS</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm">/* Shared memory region layout */</span>
Region 0: Control - ring headers, metadata
  offset 0: memif_shm_t { cookie, version, ... }
  offset N: memif_ring_t[0] { head, tail, flags, desc[ring_size] }
  offset M: memif_ring_t[1] { ... }  <span class="cm">/* one ring per queue */</span>

Region 1+: Data - packet buffers
  Large contiguous buffer space subdivided into fixed-size slots
  Each slot = memif_buffer_size bytes (default 2048)

<span class="cm">/* Descriptor - one per buffer slot */</span>
<span class="ck">typedef struct</span> {
    <span class="ck">u16</span>  flags;         <span class="cm">/* MEMIF_DESC_FLAG_NEXT = chained buffer */</span>
    <span class="ck">u16</span>  region;        <span class="cm">/* which shared memory region holds the data */</span>
    <span class="ck">u32</span>  length;        <span class="cm">/* bytes of valid data */</span>
    <span class="ck">u32</span>  offset;        <span class="cm">/* byte offset within the region */</span>
    <span class="ck">u32</span>  metadata;      <span class="cm">/* opaque: user can store anything */</span>
} memif_desc_t;

<span class="cm">/* Ring header */</span>
<span class="ck">typedef struct</span> {
    <span class="ck">u16</span>  head;          <span class="cm">/* producer writes here */</span>
    <span class="ck">u16</span>  tail;          <span class="cm">/* consumer reads here */</span>
    <span class="ck">u16</span>  flags;         <span class="cm">/* MEMIF_RING_FLAG_MASK_INT: disable interrupts */</span>
    memif_desc_t desc[ring_size];
} memif_ring_t;

<span class="cm">/* TX side: advance head after filling descriptors */</span>
<span class="cm">/* RX side: read from tail, advance tail after processing */</span>
<span class="cm">/* ring is full when (head - tail) == ring_size */</span></pre></div>
    <div class="dpdk-box">
      <div class="dh">⚙️ DPDK PARALLEL - rte_ring vs memif ring</div>
      <ul>
        <li><strong>memif ring</strong> is semantically equivalent to an <code>rte_ring</code> of buffer descriptors shared between two processes. The key difference: rte_ring uses atomic CAS operations; memif uses plain memory reads/writes (single producer single consumer per queue - no atomics needed)</li>
        <li>memif is designed for <strong>SPSC (single producer single consumer)</strong> per queue - each queue pair has exactly one writer and one reader. For multi-queue, create multiple queue pairs</li>
        <li>memif's zero-copy model means the packet bytes sit in the shared region and are never copied between peers - analogous to what you'd achieve with DPDK's <code>rte_ring</code> of <code>rte_mbuf</code> pointers, but without the IPC overhead of separate mempools</li>
      </ul>
    </div>
  </div>
</div>
</div>

<div id="tc" class="tab-pane">
<p class="sep">VPP CLI SETUP</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">💻</span><h3>Complete memif CLI Reference</h3><span class="tag tag-teal">CLI</span></div>
  <div class="cp-body">
<div class="cb"><pre><span class="cm"># ── VPP INSTANCE A: server (master) ──</span>

<span class="cm"># Create a memif socket (path to Unix socket file)</span>
create memif socket id 1 filename /run/vpp/memif-a.sock

<span class="cm"># Create memif interface in server (master) mode</span>
create interface memif id 0 socket-id 1 master rx-queues 2 tx-queues 2 \
  ring-size 1024 buffer-size 2048

<span class="cm"># Bring up and configure</span>
set interface state memif0/0 up
set interface ip address memif0/0 10.10.0.1/30

<span class="cm"># ── VPP INSTANCE B: client (slave) ──</span>
create memif socket id 1 filename /run/vpp/memif-a.sock
create interface memif id 0 socket-id 1 slave rx-queues 2 tx-queues 2 \
  ring-size 1024 buffer-size 2048
set interface state memif0/0 up
set interface ip address memif0/0 10.10.0.2/30

<span class="cm"># Verify connection status</span>
show memif
<span class="cm"># Should show: id 0, socket memif-a.sock, state connected, role master</span>

show interface memif0/0
<span class="cm"># Should show: link-up, rx/tx packet counters</span>

<span class="cm"># ── Zero-copy mode (VPP ↔ VPP only) ──</span>
<span class="cm"># Both sides must use VPP's memif plugin</span>
<span class="cm"># Add 'zero-copy' to the create command:</span>
create interface memif id 1 socket-id 1 master zero-copy

<span class="cm"># ── L2 bridge use case (two memif ports in a VPP bridge domain) ──</span>
create bridge-domain 10 learn 1 forward 1 flood 1
set interface l2 bridge memif0/0 10
set interface l2 bridge memif0/1 10</pre></div>

    <table class="api-table">
      <thead><tr><th>CLI Command</th><th>Purpose</th></tr></thead>
      <tbody>
        <tr><td><code>show memif</code></td><td>All memif interfaces with socket path, role, connection state</td></tr>
        <tr><td><code>show memif socket</code></td><td>All registered memif sockets</td></tr>
        <tr><td><code>show memif &lt;if&gt;</code></td><td>Detailed: queue count, ring size, buffer size, descriptor counts</td></tr>
        <tr><td><code>delete memif &lt;if&gt;</code></td><td>Remove a memif interface (disconnects peer)</td></tr>
        <tr><td><code>delete memif socket id N</code></td><td>Remove a memif socket (must have no interfaces using it)</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>

<div id="td" class="tab-pane">
<p class="sep">LIBMEMIF - C API FOR THIRD-PARTY APPS</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📚</span><h3>libmemif API - Connect Any Process to VPP</h3><span class="tag tag-blue">LIBRARY</span></div>
  <div class="cp-body">
    <p>libmemif (<code>extras/libmemif/</code>) is a standalone C library that implements the memif protocol. Any process - DPDK app, Python via ctypes, Go via cgo - can use it to create a memif peer that connects to VPP without running a full VPP instance.</p>
<div class="cb"><pre><span class="cm">/* Include */</span>
<span class="cs">#include "libmemif.h"</span>

<span class="cm">/* Step 1: Initialise the library */</span>
memif_init(NULL, <span class="cs">"my_app"</span>, NULL, NULL, NULL);

<span class="cm">/* Step 2: Create a socket (path must match VPP's socket) */</span>
memif_socket_handle_t sock;
memif_socket_args_t sock_args = {
    .path = <span class="cs">"/run/vpp/memif-a.sock"</span>,
};
memif_create_socket(&sock, &sock_args, NULL);

<span class="cm">/* Step 3: Create the memif connection as client (slave) */</span>
memif_conn_handle_t conn;
memif_conn_args_t args = {
    .socket     = sock,
    .interface_id = 0,
    .is_master  = 0,        <span class="cm">/* 0 = client/slave */</span>
    .num_s2m_rings = 1,     <span class="cm">/* slave-to-master queues */</span>
    .num_m2s_rings = 1,
    .buffer_size   = 2048,
    .log2_ring_size = 10,   <span class="cm">/* ring_size = 1024 */</span>
};
memif_create(&conn, &args,
    on_connect_cb, on_disconnect_cb, on_interrupt_cb, NULL);

<span class="cm">/* Step 4: Poll the socket (drives connection setup) */</span>
<span class="ck">while</span> (running) {
    memif_poll_event(sock, 0 <span class="cm">/* timeout ms */</span>);
}

<span class="cm">/* Step 5: TX - after on_connect_cb fires */</span>
memif_buffer_t bufs[16];
<span class="ck">u16</span> n_alloc;
memif_buffer_alloc(conn, 0 <span class="cm">/* queue */</span>, bufs, 16, &n_alloc, 2048);
<span class="ck">for</span> (i = 0; i < n_alloc; i++) {
    <span class="cm">/* bufs[i].data points to the shared memory region */</span>
    memcpy(bufs[i].data, my_packet_data, my_packet_len);
    bufs[i].len = my_packet_len;
}
<span class="ck">u16</span> n_tx;
memif_tx_burst(conn, 0, bufs, n_alloc, &n_tx);

<span class="cm">/* Step 6: RX */</span>
memif_buffer_t rx_bufs[256];
<span class="ck">u16</span> n_rx;
memif_rx_burst(conn, 0, rx_bufs, 256, &n_rx);
<span class="ck">for</span> (i = 0; i < n_rx; i++) {
    process_packet(rx_bufs[i].data, rx_bufs[i].len);
}
memif_refill_queue(conn, 0, n_rx, 0);</pre></div>
    <p>libmemif also has Python bindings via ctypes: <code>extras/libmemif/python/libmemif.py</code>. This is what you use in Project 5 to build the Python control-plane client.</p>
  </div>
</div>
</div>

<div id="te" class="tab-pane">
<p class="sep">DPDK net_memif PMD - CONNECT TESTPMD TO VPP</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>net_memif PMD - testpmd ↔ VPP</h3><span class="tag tag-orange">DPDK INTEGRATION</span></div>
  <div class="cp-body">
    <p>DPDK's <code>net_memif</code> PMD (<code>drivers/net/memif/</code>) implements the memif protocol as a DPDK poll-mode driver. This means testpmd, your DPDK forwarding application, or any DPDK-based app can connect directly to VPP as a memif peer - without running a second VPP instance.</p>
<div class="cb"><pre><span class="cm"># ── VPP side: set up as master ──</span>
create memif socket id 1 filename /run/vpp/memif-dpdk.sock
create interface memif id 0 socket-id 1 master rx-queues 1 tx-queues 1
set interface state memif0/0 up

<span class="cm"># ── DPDK testpmd side: connect as slave ──</span>
dpdk-testpmd \
  --vdev="net_memif,socket=/run/vpp/memif-dpdk.sock,id=0,role=slave" \
  --no-pci \
  -- -i \
     --port-topology=chained \
     --rxq=1 --txq=1 \
     --nb-cores=1

<span class="cm"># ── In testpmd interactive shell ──</span>
testpmd> set fwd txonly
testpmd> start
<span class="cm"># Now VPP receives packets on memif0/0</span>
<span class="cm"># Check: vppctl show interface memif0/0</span>

<span class="cm"># ── For zero-copy (DPDK side must match VPP buffer layout) ──</span>
--vdev="net_memif,socket=/run/vpp/memif-dpdk.sock,id=0,role=slave,zero-copy=yes"
<span class="cm"># zero-copy requires DPDK mbufs sized to match VPP's buffer-size (2048)</span></pre></div>
    <table class="api-table">
      <thead><tr><th>net_memif PMD Option</th><th>Description</th><th>Must Match VPP</th></tr></thead>
      <tbody>
        <tr><td><code>socket</code></td><td>Path to Unix socket file</td><td>Yes - exact path</td></tr>
        <tr><td><code>id</code></td><td>memif interface ID</td><td>Yes - must match VPP's <code>id N</code></td></tr>
        <tr><td><code>role=slave</code></td><td>Client role (VPP is master)</td><td>Yes - roles must be opposite</td></tr>
        <tr><td><code>ring-size</code></td><td>Ring descriptor count</td><td>No - negotiated during handshake</td></tr>
        <tr><td><code>pkt-buffer-size</code></td><td>Buffer size in bytes</td><td>Recommended: match VPP's buffer-size</td></tr>
        <tr><td><code>zero-copy</code></td><td>Enable zero-copy mode</td><td>Both sides must agree</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>

<div id="tf" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr"><span class="pn">PROJECT 5</span><h4>memif vSwitch - 3-Container Topology</h4></div>
  <div class="proj-body">
    <p><strong>Objective:</strong> Build a 3-container virtual switch using VPP as the central switch with memif interfaces. Container A and Container C are DPDK testpmd instances connected to VPP via memif. A Python libmemif client from Container B monitors traffic on a third memif interface (mirror port).</p>
    <div class="ps"><div class="sn">1</div><div>Container A: run testpmd with net_memif PMD as slave connected to <code>/run/shared/memif-a.sock</code>. Container C: testpmd as slave on <code>/run/shared/memif-c.sock</code>. Use Docker volumes to share the socket directory.</div></div>
    <div class="ps"><div class="sn">2</div><div>VPP (Container B): create two memif sockets, create memif interfaces in master mode for each socket, create a bridge domain, add both interfaces as L2 bridge members. Verify connectivity A→C with testpmd txonly/rxonly.</div></div>
    <div class="ps"><div class="sn">3</div><div>Add a third memif interface to VPP as a "mirror port". Use a feature arc or a custom tap-output node to copy each forwarded packet's metadata (src MAC, dst MAC, length) to the mirror memif.</div></div>
    <div class="ps"><div class="sn">4</div><div>Write a Python script using libmemif Python bindings that connects to the mirror memif socket and prints per-second packet counts, unique source MACs seen, and bytes forwarded. Run it while A→C traffic is flowing.</div></div>
    <div class="ps"><div class="sn">5</div><div>Benchmark: send at increasing rates (100Kpps → 1Mpps → 5Mpps) from testpmd. Record the maximum forwarding rate VPP sustains without packet drops (check <code>show error</code> for drops). Note the VPP CPU utilisation at each rate.</div></div>
    <div class="ps"><div class="sn">6</div><div>Test zero-copy mode: enable <code>zero-copy</code> on all memif interfaces (both VPP and testpmd sides). Re-run the benchmark. Compare peak throughput and CPU usage with and without zero-copy.</div></div>
  </div>
</div>
</div>

<div id="tg" class="tab-pane">
<p class="sep">P3B COMPLETION CHECKLIST</p>
<ul class="cl">
  <li>Understand memif's two-plane design: Unix socket control path vs shared memory data path</li>
  <li>Know server/master vs client/slave roles and which side listens on the socket</li>
  <li>Understand the memif ring structure: head/tail pointers, descriptor array, region reference</li>
  <li>Know the SPSC constraint per queue and how to scale with multiple queue pairs</li>
  <li>Can set up a memif connection in VPP (both sides) using CLI commands</li>
  <li>Know the difference between standard and zero-copy mode and when zero-copy applies</li>
  <li>Can write a basic libmemif C client: init, create socket, create conn, tx_burst, rx_burst</li>
  <li>Know the DPDK net_memif PMD options: socket, id, role, and how they pair with VPP config</li>
  <li>Know the relevant CLI: show memif, show memif socket, show interface memif0/0</li>
  <li>Completed Project 5: 3-container memif vSwitch with Python monitoring client</li>
</ul>
<div class="ins" style="margin-top:1.2rem;">
  <p>✅ Next: <strong>P3C - TAP v2, AF_XDP, vhost-user, and AF_PACKET</strong>. These complete your knowledge of every interface type in VPP's arsenal.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/data-plane/vpp/module-p3-dpdk/' | relative_url }}">← DPDK Plugin</a>
  <a href="{{ '/learning/data-plane/vpp/vpp-roadmap/' | relative_url }}">🗺️ Roadmap</a>
  <a class="nb" href="{{ '/learning/data-plane/vpp/module-p3-tap-afxdp/' | relative_url }}">Next: TAP · AF_XDP →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active');}
</script>
