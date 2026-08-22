---
title: "M23 - Connection Tracking and NAT"
description: "NETWORKING MASTERY · PHASE 6 · MODULE 23 · WEEK 22 🔗 Connection Tracking and NAT Stateful inspection fundamentals · Five-tuple tracking · TCP/UDP/ICMP state machines · Session…"
domain: networking
track: networking-mastery
order: 23
ownHeader: true
url: /learning/networking-mastery/m23-conntrack-nat/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#1a0a1a 35%,#3a0050 65%,#200040 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#e090ff;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#f0d0ff;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#fce8ff}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#e090ff;border-bottom-color:#e090ff}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700;letter-spacing:.04em}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul,.cp-body ol{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.35rem}
.cp-body h4{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin:1rem 0 .3rem}
.p-blue .cp-hdr{background:#e8f1f9}[data-theme=dark] .p-blue .cp-hdr{background:#0d2030}
.p-teal .cp-hdr{background:#e0f0ee}[data-theme=dark] .p-teal .cp-hdr{background:#0a2420}
.p-orange .cp-hdr{background:#faeee4}[data-theme=dark] .p-orange .cp-hdr{background:#2a1808}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-red .cp-hdr{background:#faeaea}[data-theme=dark] .p-red .cp-hdr{background:#2a0808}
.p-amber .cp-hdr{background:#fdf4dc}[data-theme=dark] .p-amber .cp-hdr{background:#2a1e00}
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-purple{background:#e0d4f4;color:#3a1a6c}
.tag-green{background:#c8e8d4;color:#0e4a28}.tag-red{background:#f4d0d0;color:#6c1a1a}
.tag-amber{background:#fae8a0;color:#5a3800}
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #8020c0}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#f0d0ff;white-space:pre}
.cm{color:#806090}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#f8f0ff;border:1.5px solid #8020c0;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#200030;border-color:#a050e0}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#5010a0}[data-theme=dark] .ins strong{color:#e090ff}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#5010a0;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#8020c0}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #8020c0;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#8020c0;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.45rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.6}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#8020c0;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.48rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.55;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#8020c0;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 6 · MODULE 23 · WEEK 22</div>
  <div class="mod-title">🔗 Connection Tracking and NAT</div>
  <div class="mod-subtitle">Stateful inspection fundamentals · Five-tuple tracking · TCP/UDP/ICMP state machines · Session table design · NAT types · NAPT mechanics · VPP NAT44-ED · SYN cookies · Attack hardening</div>
  <div class="mod-pills">
    <span class="mod-pill">Advanced</span>
    <span class="mod-pill">Prerequisite: M05 TCP · M10 Routing</span>
    <span class="mod-pill">NGFW Core Data Structure</span>
    <span class="mod-pill">3 Labs</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">Stateful Inspection</button>
  <button class="tab-btn" onclick="vt(event,'t1')">Session Table Design</button>
  <button class="tab-btn" onclick="vt(event,'t2')">TCP State Machine</button>
  <button class="tab-btn" onclick="vt(event,'t3')">UDP and ICMP Tracking</button>
  <button class="tab-btn" onclick="vt(event,'t4')">NAT Fundamentals</button>
  <button class="tab-btn" onclick="vt(event,'t5')">NAPT Mechanics</button>
  <button class="tab-btn" onclick="vt(event,'t6')">ALG and NAT Traversal</button>
  <button class="tab-btn" onclick="vt(event,'t7')">VPP NAT44-ED</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Attacks and Hardening</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'ta')">Checklist</button>
</div>


<div id="t0" class="tab-pane active">
<p class="sep">WHY STATEFUL INSPECTION — THE FOUNDATION OF NGFW</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>Stateless vs Stateful Packet Filtering</h3><span class="tag tag-purple">CONCEPT</span></div>
  <div class="cp-body">
    <p>The first generation of firewalls was stateless — each packet was evaluated in isolation. A rule "allow TCP dst-port 80" permits any TCP packet with that destination port, including crafted RSTs, out-of-sequence data, and attack payloads. The attacker simply sets dst_port=80 and everything passes.</p>
    <p>Stateful inspection tracks the state of every network flow. A packet is only forwarded if it represents a valid state transition in a known, existing connection — a SYN-ACK without a preceding SYN is dropped, a RST from a server with no known session is dropped, data from an address that hasn't completed the handshake is dropped.</p>
    <div class="two-col">
      <div>
        <h4>Stateless Filter Weaknesses</h4>
        <ul>
          <li>Cannot distinguish new vs established connections</li>
          <li>Cannot detect TCP sequence number anomalies</li>
          <li>Cannot track UDP "sessions" (no inherent state)</li>
          <li>Cannot enforce return-traffic matching</li>
          <li>Easily evaded by packets that match rule syntax but violate protocol semantics</li>
        </ul>
      </div>
      <div>
        <h4>Stateful Inspection Advantages</h4>
        <ul>
          <li>Validates every packet against valid protocol state</li>
          <li>Automatically permits return traffic for established connections</li>
          <li>Detects SYN floods, RST injection, sequence attacks</li>
          <li>Enables per-flow policy: inspect, permit, deny based on full session context</li>
          <li>Foundation for all NGFW L7 features: app ID, DPI, TLS inspection, QoS</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📐</span><h3>The Five-Tuple — Unique Flow Identifier</h3><span class="tag tag-blue">FIVE-TUPLE</span></div>
  <div class="cp-body">
    <p>Every TCP/UDP flow is uniquely identified by five fields. The conntrack engine uses this five-tuple as the hash key to locate the flow's state entry in the session table.</p>
<div class="cb"><pre>/* Five-tuple: the universal flow key */
src_ip    — Source IP address       (4B IPv4, 16B IPv6)
dst_ip    — Destination IP address
src_port  — Source TCP/UDP port     (2B)
dst_port  — Destination TCP/UDP port
protocol  — IP protocol             (6=TCP, 17=UDP, 1=ICMP, 50=ESP)
 
/* CRITICAL: both directions of a flow must hash to the same entry */
/* Forward:  (client_ip, client_port, server_ip, server_port, proto) */
/* Reverse:  (server_ip, server_port, client_ip, client_port, proto) */
/* Solution: canonical form — sort so "smaller" endpoint is always first */
 
typedef struct {
    uint8_t  src_ip[16];   /* zero-pad IPv4 to 16B for uniform handling */
    uint8_t  dst_ip[16];
    uint16_t src_port;
    uint16_t dst_port;
    uint8_t  proto;
    uint8_t  pad[3];       /* 40 bytes total — fits 2x AVX2 registers */
} flow_key_t;
 
void normalise_key(flow_key_t *k, int *is_initiator) {
    int cmp = memcmp(k->src_ip, k->dst_ip, 16);
    if (cmp > 0 || (cmp == 0 && k->src_port > k->dst_port)) {
        /* swap to canonical form */
        uint8_t tmp[16]; memcpy(tmp, k->src_ip, 16);
        memcpy(k->src_ip, k->dst_ip, 16);
        memcpy(k->dst_ip, tmp, 16);
        uint16_t p = k->src_port; k->src_port = k->dst_port; k->dst_port = p;
        *is_initiator = 0;   /* this is the return direction */
    } else {
        *is_initiator = 1;
    }
}
 
/* For ICMP: no ports — encode type/identifier in port fields */
/* Echo request (type=8): src_port=identifier, dst_port=type */
/* ICMP error: extract inner IP header five-tuple from payload */</pre></div>
  </div>
</div>
</div>


<div id="t1" class="tab-pane">
<p class="sep">SESSION TABLE — DESIGN FOR CORRECTNESS AND SPEED</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🗄️</span><h3>Session Entry Structure — Every Field Explained</h3><span class="tag tag-blue">DATA STRUCTURE</span></div>
  <div class="cp-body">
<div class="cb"><pre>typedef struct session {
    /* ── Lookup key (must match hash table key size) ─── */
    flow_key_t   key;            /* canonical five-tuple, 40B */
 
    /* ── Protocol state ─────────────────────────────── */
    uint8_t      proto;          /* IPPROTO_TCP, _UDP, _ICMP */
    uint8_t      tcp_state;      /* TCP_S_SYN_SENT .. TCP_S_CLOSED */
    uint8_t      flags;          /* F_NAT, F_TLS_INSPECT, F_LOG */
 
    /* ── TCP sequence tracking ───────────────────────── */
    uint32_t     fwd_seq;        /* highest seq seen (forward) */
    uint32_t     rev_seq;        /* highest seq seen (reverse) */
    uint32_t     fwd_ack;        /* last ACK seen (forward) */
    uint32_t     rev_ack;
    uint32_t     fwd_window;     /* advertised receive window */
    uint32_t     rev_window;
    uint8_t      fwd_wscale;     /* window scale factor (TCP option) */
    uint8_t      rev_wscale;
 
    /* ── Timestamps ──────────────────────────────────── */
    uint64_t     created_ns;     /* session birth (CLOCK_MONOTONIC) */
    uint64_t     last_seen_ns;   /* last packet timestamp */
    uint32_t     timeout_s;      /* per-protocol inactivity timeout */
    uint32_t     expire_tick;    /* timer wheel bucket */
 
    /* ── Traffic counters ────────────────────────────── */
    uint64_t     fwd_pkts;
    uint64_t     fwd_bytes;
    uint64_t     rev_pkts;
    uint64_t     rev_bytes;
 
    /* ── NAT rewrite (populated if F_NAT set) ────────── */
    uint32_t     nat_src_ip;     /* translated src IP (SNAT) */
    uint16_t     nat_src_port;   /* translated src port (NAPT) */
    uint32_t     nat_dst_ip;     /* translated dst IP (DNAT) */
    uint16_t     nat_dst_port;   /* translated dst port (DNAT) */
 
    /* ── Application layer ───────────────────────────── */
    uint16_t     app_id;         /* identified app: HTTP=1, TLS=2, DNS=3... */
    uint8_t      risk_score;     /* 0–100 threat score from DPI */
    void        *dpi_state;      /* DPI engine per-flow state machine */
 
    /* ── Policy result (cached after first policy eval) ─ */
    uint32_t     policy_id;      /* matched ACL rule index */
    uint8_t      action;         /* ACTION_PERMIT, _DENY, _INSPECT */
    uint8_t      ssl_inspect;    /* 1 = TLS MITM proxy active */
 
    /* ── Linked list for timer wheel ─────────────────── */
    struct session *tw_next;
    struct session *tw_prev;
 
} __attribute__((packed)) session_t;
/* Target size: ≤ 256 bytes per session */
/* 1M sessions × 256B = 256MB — fits in L3 cache on server CPUs */
/* Typical enterprise NGFW: 500K–4M concurrent sessions */</pre></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Hash Table and Memory Pool — Lock-Free Design</h3><span class="tag tag-teal">HASH TABLE</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Option 1: VPP clib_bihash_48_8 (production choice) */
clib_bihash_48_8_t session_table;
clib_bihash_init_48_8(&session_table, "sessions", 1<<20, 512<<20);
 
/* Lookup */
clib_bihash_kv_48_8_t kv;
memcpy(kv.key, &flow_key, 48);
if (!clib_bihash_search_48_8(&session_table, &kv, &kv)) {
    session_t *s = pool_elt_at_index(session_pool, (uint32_t)kv.value);
    /* fast path: cached policy, cached NAT mapping */
}
 
/* Option 2: DPDK rte_hash with lock-free concurrent access */
struct rte_hash_parameters p = {
    .name       = "sessions",
    .entries    = 1<<20,
    .key_len    = sizeof(flow_key_t),
    .hash_func  = rte_jhash,
    .extra_flag = RTE_HASH_EXTRA_FLAGS_RW_CONCURRENCY_LF,
    .socket_id  = rte_socket_id(),
};
struct rte_hash *ht = rte_hash_create(&p);
 
/* Bulk lookup — SIMD, 8 flows simultaneously */
const void *keys[8] = {&k0,&k1,&k2,&k3,&k4,&k5,&k6,&k7};
int32_t positions[8];
uint64_t hit_mask = rte_hash_lookup_bulk(ht, keys, 8, positions);
/* bit i set in hit_mask → flow i found; positions[i] = session index */
 
/* Memory pool: pre-allocated array, no malloc per session */
session_t *session_pool = rte_malloc_socket("sessions",
    MAX_SESSIONS * sizeof(session_t), 64, rte_eth_dev_socket_id(0));
 
/* Per-NUMA-socket pools: each socket has its own pool and hash table */
/* Workers pinned to same socket as their NIC → zero cross-NUMA memory */</pre></div>
    <div class="ins"><p>💡 <strong>Two critical performance design choices:</strong> (1) Use a pre-allocated memory pool indexed by integer — malloc/free per session causes heap fragmentation and cache thrashing at scale. (2) Per-NUMA-socket tables with per-CPU-core session creation — eliminate cross-socket locking entirely. VPP's clib_bihash is designed exactly for this access pattern.</p></div>
  </div>
</div>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">⏱️</span><h3>Timer Wheel — O(1) Session Expiry</h3><span class="tag tag-green">TIMEOUTS</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Protocol / State</th><th>Timeout</th><th>Rationale</th></tr></thead>
      <tbody>
        <tr><td>TCP SYN (half-open)</td><td>10–30s</td><td>SYN flood defence — expire incomplete handshakes quickly</td></tr>
        <tr><td>TCP ESTABLISHED</td><td>3600–86400s</td><td>Long-lived HTTP/2, SSH; keepalives refresh timeout</td></tr>
        <tr><td>TCP FIN_WAIT / TIME_WAIT</td><td>120–240s</td><td>RFC 793 minimum 2×MSL; allow delayed packets</td></tr>
        <tr><td>UDP generic</td><td>30–60s</td><td>Most UDP is short request-response</td></tr>
        <tr><td>UDP DNS</td><td>10–20s</td><td>Single exchange; keep short</td></tr>
        <tr><td>UDP QUIC</td><td>120–300s</td><td>Connection migration; mobile clients change IPs</td></tr>
        <tr><td>ICMP Echo</td><td>10–30s</td><td>Ping timeout window</td></tr>
        <tr><td>ICMP Error</td><td>5s</td><td>One-shot messages; no reply expected</td></tr>
      </tbody>
    </table>
<div class="cb"><pre>/* Timer wheel — O(1) insert and expire */
/* 65536 buckets with 1-second resolution = ~18 hours of range */
#define WHEEL_SIZE  65536
typedef struct {
    session_t *buckets[WHEEL_SIZE];   /* linked list head per bucket */
    uint32_t   current_tick;
} timer_wheel_t;
 
void session_refresh(session_t *s, timer_wheel_t *tw, uint32_t timeout_s) {
    /* Remove from current bucket */
    if (s->tw_prev) s->tw_prev->tw_next = s->tw_next;
    if (s->tw_next) s->tw_next->tw_prev = s->tw_prev;
 
    /* Insert into new bucket */
    s->expire_tick = tw->current_tick + timeout_s;
    uint32_t b = s->expire_tick & (WHEEL_SIZE - 1);
    s->tw_next = tw->buckets[b];
    s->tw_prev = NULL;
    if (tw->buckets[b]) tw->buckets[b]->tw_prev = s;
    tw->buckets[b] = s;
}
 
/* Called once per second from background thread */
void timer_wheel_advance(timer_wheel_t *tw, session_table_t *st) {
    tw->current_tick++;
    uint32_t b = tw->current_tick & (WHEEL_SIZE - 1);
    session_t *s = tw->buckets[b];
    tw->buckets[b] = NULL;
    while (s) {
        session_t *next = s->tw_next;
        if (s->expire_tick == tw->current_tick) {
            session_destroy(st, s);   /* remove from hash, return to pool */
        } else {
            /* Re-insert (bucket collision from previous wrap) */
            session_refresh(s, tw, s->expire_tick - tw->current_tick);
        }
        s = next;
    }
}</pre></div>
  </div>
</div>
</div>


<div id="t2" class="tab-pane">
<p class="sep">TCP STATE MACHINE — NGFW SEQUENCE TRACKING</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔄</span><h3>TCP Conntrack States and Transitions</h3><span class="tag tag-blue">TCP STATES</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* TCP states from NGFW perspective (observer, not endpoint) */
typedef enum {
    TCP_S_NONE = 0,    /* no session — first packet */
    TCP_S_SYN_SENT,    /* SYN seen from initiator */
    TCP_S_SYN_RCVD,    /* SYN+ACK seen from responder */
    TCP_S_ESTABLISHED, /* ACK completing 3-way handshake */
    TCP_S_FIN_WAIT_1,  /* FIN from initiator */
    TCP_S_FIN_WAIT_2,  /* FIN ACKed by responder */
    TCP_S_CLOSE_WAIT,  /* FIN from responder (responder closing first) */
    TCP_S_LAST_ACK,    /* FIN from initiator after CLOSE_WAIT */
    TCP_S_TIME_WAIT,   /* waiting for stray packets */
    TCP_S_CLOSED,      /* RST received or graceful close complete */
} tcp_state_t;
 
/* State transition table */
uint8_t tcp_next_state[TCP_S_CLOSED+1][2 /*dir*/][64 /*flags*/];
 
/* Build the table at init (simplified) */
void tcp_init_transitions(void) {
    /* SYN from initiator → create session, SYN_SENT */
    /* Handled at session creation, not in table */
 
    /* SYN+ACK from responder → SYN_RCVD */
    tcp_next_state[TCP_S_SYN_SENT][0/*rev*/][TH_SYN|TH_ACK] = TCP_S_SYN_RCVD;
 
    /* ACK from initiator → ESTABLISHED */
    tcp_next_state[TCP_S_SYN_RCVD][1/*fwd*/][TH_ACK] = TCP_S_ESTABLISHED;
 
    /* FIN from initiator → FIN_WAIT_1 */
    tcp_next_state[TCP_S_ESTABLISHED][1/*fwd*/][TH_FIN]     = TCP_S_FIN_WAIT_1;
    tcp_next_state[TCP_S_ESTABLISHED][1/*fwd*/][TH_FIN|TH_ACK] = TCP_S_FIN_WAIT_1;
 
    /* ACK of FIN → FIN_WAIT_2 */
    tcp_next_state[TCP_S_FIN_WAIT_1][0/*rev*/][TH_ACK]      = TCP_S_FIN_WAIT_2;
 
    /* RST → CLOSED from any state */
    for (int st = 0; st <= TCP_S_CLOSED; st++) {
        tcp_next_state[st][0][TH_RST] = TCP_S_CLOSED;
        tcp_next_state[st][1][TH_RST] = TCP_S_CLOSED;
    }
    /* ... more transitions ... */
}
 
/* Fast-path state lookup */
uint8_t new_state = tcp_next_state[s->tcp_state][is_initiator][tcp_flags & 0x3f];
if (new_state != s->tcp_state) {
    s->tcp_state = new_state;
    if (new_state == TCP_S_CLOSED)
        session_schedule_destroy(s, 5);   /* brief grace period */
}</pre></div>
  </div>
</div>

<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>TCP Sequence Number Validation</h3><span class="tag tag-red">SEQ VALIDATION</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Sequence validation: reject RST injection and data injection attacks */
/* Only accept packets whose sequence number falls within expected window */
 
int tcp_seq_in_window(session_t *s, const struct tcphdr *th,
                      uint16_t data_len, int is_fwd) {
    uint32_t seq    = ntohl(th->th_seq);
    uint32_t ack    = ntohl(th->th_ack);
    uint32_t e_seq  = is_fwd ? s->fwd_seq  : s->rev_seq;   /* expected */
    uint32_t window = is_fwd ? s->rev_window : s->fwd_window; /* peer window */
 
    /* Allow [e_seq - window, e_seq + window] accounting for 32-bit wrap */
    int32_t lo = (int32_t)(seq - (e_seq - window));
    int32_t hi = (int32_t)(seq + data_len - (e_seq + window));
 
    if (lo < 0 || hi > 0) {
        /* Out of window */
        if (th->th_flags & TH_RST) {
            /* RST injection — drop silently, increment counter */
            s->rst_inject_count++;
            return 0;
        }
        /* Data outside window — could be retransmit or injection */
        /* Log and drop; don't tear down session */
        return 0;
    }
 
    /* Update tracked sequence numbers */
    if (is_fwd) {
        if (SEQ_GT(seq + data_len, s->fwd_seq))
            s->fwd_seq = seq + data_len;
        if (th->th_flags & TH_ACK)
            s->fwd_ack = ack;
    } else {
        if (SEQ_GT(seq + data_len, s->rev_seq))
            s->rev_seq = seq + data_len;
        if (th->th_flags & TH_ACK)
            s->rev_ack = ack;
    }
    return 1;
}
 
/* Window scale option — must be parsed from SYN/SYN-ACK */
/* Effective window = advertised_window << window_scale */
/* Not parsing window scale → sequence window may be too narrow */
/* Result: false positives on legitimate high-BDP connections */</pre></div>
  </div>
</div>
</div>


<div id="t3" class="tab-pane">
<p class="sep">UDP AND ICMP TRACKING</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📡</span><h3>UDP Pseudo-Session Tracking</h3><span class="tag tag-teal">UDP</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* UDP has no handshake — NGFW creates pseudo-session on first permitted datagram */
 
typedef enum {
    UDP_S_NEW,      /* first packet seen, no reply yet */
    UDP_S_REPLIED,  /* return packet seen — bidirectional confirmed */
    UDP_S_CLOSING   /* idle → pending removal */
} udp_state_t;
 
/* Per-protocol timeouts */
static const struct {
    uint16_t dst_port;
    uint32_t timeout_s;
} udp_port_timeouts[] = {
    { 53,   10  },   /* DNS — short, single exchange */
    { 67,   30  },   /* DHCP */
    { 123,  60  },   /* NTP */
    { 500,  3600},   /* IKEv2 */
    { 4500, 3600},   /* IKE NAT-T */
    { 5060, 300 },   /* SIP registration */
    { 0,    30  },   /* default */
};
 
uint32_t udp_timeout(uint16_t dst_port) {
    for (int i = 0; udp_port_timeouts[i].dst_port; i++)
        if (udp_port_timeouts[i].dst_port == dst_port)
            return udp_port_timeouts[i].timeout_s;
    return 30;
}
 
/* QUIC sessions (UDP 443) require special handling */
/* QUIC Connection IDs survive IP address changes (mobile handoff) */
/* Proper QUIC tracking: parse QUIC header → extract Connection ID */
/* Create secondary index: connection_id → session */
/* On IP change: update session's five-tuple but keep DPI state */
 
/* UDP session creation in forwarding loop */
if (!session_lookup(&key)) {
    if (policy_permits(&key)) {
        session_t *s = session_create(&key, IPPROTO_UDP,
            udp_timeout(ntohs(udph->dest)));
        /* On first packet from responder: s->state = UDP_S_REPLIED */
        /* This is the confirmation that remote is responding */
    } else {
        drop_packet(m);
    }
}</pre></div>
  </div>
</div>

<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">📶</span><h3>ICMP Tracking — Echo and Error Correlation</h3><span class="tag tag-amber">ICMP</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* ICMP Echo tracking: identifier field plays role of session ID */
/* Request: type=8, code=0, id=PID, seq=N */
/* Reply:   type=0, code=0, id=PID, seq=N */
 
/* Encode ICMP into flow_key_t */
void icmp_to_key(const struct iphdr *iph,
                 const struct icmphdr *ich, flow_key_t *k) {
    memset(k, 0, sizeof(*k));
    k->src_ip[12] = iph->saddr >> 24; /* ... */
    k->dst_ip[12] = iph->daddr >> 24; /* ... */
    k->proto      = IPPROTO_ICMP;
    if (ich->type == ICMP_ECHO || ich->type == ICMP_ECHOREPLY) {
        /* Use identifier as src_port, type as dst_port */
        k->src_port = ntohs(ich->un.echo.id);
        k->dst_port = (ich->type == ICMP_ECHO) ? 8 : 0;
        /* Normalise: request and reply must share key */
        /* After normalise, ECHO and ECHOREPLY map to same entry */
    }
}
 
/* ICMP error correlation — find the session that triggered the error */
void icmp_error_correlate(const struct icmphdr *ich, size_t len,
                           session_t **orig_session) {
    /* ICMP error payload: original IP header + first 8B of transport */
    const struct iphdr *inner = (const struct iphdr *)(ich + 1);
    if (len < sizeof(*ich) + sizeof(*inner) + 8) { *orig_session = NULL; return; }
 
    flow_key_t inner_key;
    const uint8_t *inner_l4 = (const uint8_t *)inner + inner->ihl * 4;
    inner_key.proto    = inner->protocol;
    /* ... fill src/dst IP from inner header ... */
    if (inner->protocol == IPPROTO_TCP || inner->protocol == IPPROTO_UDP) {
        inner_key.src_port = ntohs(*(uint16_t *)(inner_l4 + 0));
        inner_key.dst_port = ntohs(*(uint16_t *)(inner_l4 + 2));
    }
    normalise_key(&inner_key, NULL);
    *orig_session = session_lookup(&inner_key);
}
 
/* ICMP policy */
/* Echo request/reply: permit if within session */
/* ICMP unreachable / TTL exceeded: permit only if correlates to a session */
/* ICMP Redirect (type=5): ALWAYS DROP — routing attack vector */
/* ICMP Timestamp (type=13): drop unless explicitly permitted */</pre></div>
  </div>
</div>
</div>


<div id="t4" class="tab-pane">
<p class="sep">NAT FUNDAMENTALS — TYPES AND POLICY</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔀</span><h3>NAT Type Taxonomy</h3><span class="tag tag-purple">NAT TYPES</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* 1. Static NAT (1:1 bidirectional mapping) */
/*    Private IP ←→ Public IP, permanent */
/*    Use: servers that need a consistent public address */
192.168.1.100 ←→ 203.0.113.100
 
/* 2. Dynamic NAT (pool-based, no port sharing) */
/*    Each private IP gets one public IP from a pool */
/*    Pool exhausted → new connections fail */
/*    Rarely used today — NAPT replaced it */
 
/* 3. NAPT / PAT (many-to-one with port multiplexing) */
/*    The standard for home/enterprise edge */
192.168.1.10:4501 → 203.0.113.1:10001
192.168.1.20:4502 → 203.0.113.1:10002
192.168.1.30:4501 → 203.0.113.1:10003  /* same client port OK — different IP */
 
/* 4. DNAT (Destination NAT) — server publishing */
/*    Rewrite destination; used for load balancing, port forwarding */
dst:203.0.113.1:80 → dst:10.0.0.5:8080
 
/* 5. Twice NAT (full NAT) */
/*    Rewrite both src and dst — overlapping address spaces */
src:10.0.0.5 dst:10.0.0.1 → src:172.16.0.5 dst:172.16.0.1
 
/* NAT and conntrack coupling */
/* NAT must use conntrack because it needs to:                */
/* 1. Know which translation to apply to RETURN traffic       */
/* 2. Apply the REVERSE translation (DNAT reply → SNAT)       */
/* 3. Persist the mapping for the lifetime of the session      */
/* Session entry stores both original and translated addresses */
 
/* Netfilter hook points for NAT */
/* SNAT: POSTROUTING hook — after routing decision, before NIC */
/* DNAT: PREROUTING hook — before routing decision             */
/* VPP NAT44-ED: processes both directions in ip4-unicast arc  */</pre></div>
  </div>
</div>
</div>


<div id="t5" class="tab-pane">
<p class="sep">NAPT MECHANICS — PORT ALLOCATION AND PACKET REWRITE</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔌</span><h3>Port Pool and Packet Rewrite</h3><span class="tag tag-blue">NAPT</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Port pool — bitmap allocator, O(1) amortised */
typedef struct {
    uint32_t public_ip;
    uint16_t port_start;   /* 1024 */
    uint16_t port_end;     /* 65535 */
    uint8_t  bitmap[8192]; /* 64512 ports / 8 = 8064 bytes */
    uint16_t next_hint;    /* round-robin start hint */
    uint32_t in_use;       /* current count */
} nat_port_pool_t;
 
uint16_t nat_alloc_port(nat_port_pool_t *pool) {
    uint16_t start = pool->next_hint;
    for (int i = 0; i < 64512; i++) {
        uint16_t p   = pool->port_start + ((start + i) % 64512);
        uint32_t off = (p - pool->port_start);
        uint32_t by  = off / 8, bi = off % 8;
        if (!(pool->bitmap[by] & (1u << bi))) {
            pool->bitmap[by] |= (1u << bi);
            pool->next_hint = (start + i + 1) % 64512;
            pool->in_use++;
            return p;
        }
    }
    return 0;  /* port exhaustion */
}
 
void nat_free_port(nat_port_pool_t *pool, uint16_t port) {
    uint32_t off = port - pool->port_start;
    pool->bitmap[off / 8] &= ~(1u << (off % 8));
    pool->in_use--;
}
 
/* Packet rewrite — what changes in each direction */
/*
  Outbound SNAT:
    IP  header: src_addr = nat_src_ip     (was private IP)
    TCP header: src_port = nat_src_port   (was ephemeral port)
    Checksums:  both IP and TCP/UDP must be updated
 
  Inbound reverse:
    IP  header: dst_addr = orig_src_ip    (restore private IP)
    TCP header: dst_port = orig_src_port  (restore original port)
    Checksums:  updated
 
  DNAT outbound:
    IP  header: dst_addr = real_server_ip
    TCP header: dst_port = real_server_port
 
  DNAT inbound (reply):
    IP  header: src_addr = public_vip_ip
    TCP header: src_port = published_port
*/
 
/* Incremental checksum update (RFC 1624) */
/* Much faster than full recalculation — only 1-2 words changed */
static inline uint16_t csum_update_u32(uint16_t old_csum,
                                        uint32_t old_val, uint32_t new_val) {
    uint32_t s = (uint16_t)~old_csum;
    s += (uint16_t)~(old_val & 0xFFFF) + (uint16_t)~(old_val >> 16);
    s += (uint16_t)(new_val & 0xFFFF)  + (uint16_t)(new_val >> 16);
    while (s >> 16) s = (s & 0xFFFF) + (s >> 16);
    return (uint16_t)~s;
}
 
void nat_rewrite_outbound(struct iphdr *iph, struct tcphdr *th,
                           uint32_t new_sip, uint16_t new_sport) {
    uint32_t old_sip   = iph->saddr;
    uint16_t old_sport = th->source;
 
    iph->saddr  = htonl(new_sip);
    th->source  = htons(new_sport);
 
    /* Update IP checksum (covers IP header — 32-bit addr field) */
    iph->check = csum_update_u32(iph->check, old_sip, new_sip);
 
    /* Update TCP/UDP checksum (pseudo-header includes src IP + port) */
    th->check = csum_update_u32(th->check, old_sip, new_sip);
    th->check = csum_update_u32(th->check,
                                (uint32_t)ntohs(old_sport),
                                (uint32_t)new_sport);
}
/* Hardware offload (DPDK RTE_MBUF_F_TX_IP_CKSUM) avoids software calc */</pre></div>
  </div>
</div>
</div>


<div id="t6" class="tab-pane">
<p class="sep">ALG — APPLICATION LEVEL GATEWAYS</p>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>Why Protocols Break NAT and How ALGs Fix Them</h3><span class="tag tag-orange">ALG</span></div>
  <div class="cp-body">
    <p>Protocols that embed IP addresses or ports in their application payload break NAT — the outer IP header is rewritten correctly, but the embedded address in the payload still points to the private IP the remote host cannot reach. An ALG must inspect and rewrite the payload to fix this.</p>
<div class="cb"><pre>/* Protocols requiring ALG */
/* FTP (see M09): PORT/PASV commands contain IP:port */
/* SIP/VoIP:       SDP body contains media IP:port    */
/* H.323:          Q.931/H.245 contain internal IPs   */
 
/* SIP ALG — the most complex common ALG */
 
Incoming INVITE from UA behind NAT:
  INVITE sip:bob@remote.com SIP/2.0
  Contact: sip:alice@192.168.1.5:5060     ← private IP!
  Via: SIP/2.0/UDP 192.168.1.5:5060       ← private IP!
  Content-Type: application/sdp
  Content-Length: 128
 
  v=0
  o=alice 1234 5678 IN IP4 192.168.1.5    ← private IP in SDP!
  c=IN IP4 192.168.1.5                    ← private IP!
  m=audio 16384 RTP/AVP 0                ← media port
 
ALG processing:
  1. Detect SIP (port 5060 or inspect INVITE/REGISTER keywords)
  2. Buffer TCP stream for full SIP message (may span segments)
  3. Parse Contact and Via headers → replace 192.168.1.5 with public IP
  4. Parse SDP body → replace IP in c= and o= lines
  5. Allocate NAT port for RTP media:
     203.0.113.1:20000 ← 192.168.1.5:16384
  6. Replace 16384 with 20000 in m= line
  7. Recalculate Content-Length (body size changed!)
  8. Adjust TCP sequence numbers if body size changed
  9. Update IP/TCP checksums
 
typedef struct sip_alg {
    uint8_t  *buf;          /* TCP reassembly buffer */
    uint32_t  buf_len;
    int32_t   seq_delta;    /* cumulative sequence number adjustment */
    uint32_t  media_ip;     /* original media IP (to replace) */
    uint16_t  media_port;   /* original media port */
    uint16_t  nat_port;     /* allocated NAT port for media stream */
} sip_alg_t;
 
/* Modern alternative: STUN/ICE (RFC 5389/8445) */
/* Application-level NAT traversal — no ALG needed */
/* Client queries public STUN server → learns public IP:port */
/* Encodes public address in SDP → remote can connect directly */
/* WebRTC uses ICE exclusively — no SIP ALG involvement */</pre></div>
  </div>
</div>
</div>


<div id="t7" class="tab-pane">
<p class="sep">VPP NAT44-ED — PRODUCTION IMPLEMENTATION</p>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>VPP NAT44-ED Architecture</h3><span class="tag tag-green">VPP NAT</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* NAT44-ED: Endpoint-Dependent — key includes destination address */
/* Advantage: same client port can be used for different destinations */
/* Required for: hairpinning, multiple ISP links, port-restricted NAT */
 
/* VPP NAT44-ED session key (endpoint-dependent) */
typedef struct {
    ip4_address_t local_addr;   /* pre-NAT source IP */
    ip4_address_t ext_addr;     /* destination IP (the "endpoint") */
    u16 local_port;
    u16 ext_port;
    u8  proto;
    u8  pad[3];
} ed_key_t;   /* 14 bytes padded to 16 */
 
/* Two-level lookup for ED NAT */
/* Table 1: (local_ip, local_port, ext_ip, ext_port, proto) → session */
/* Table 2: (nat_ip,   nat_port,   ext_ip, ext_port, proto) → session */
/* Both tables point to same session pool entry */
 
/* VPP NAT configuration */
nat44 enable sessions 1048576    /* 1M session table */
nat44 add pool address 203.0.113.1
nat44 add pool address 203.0.113.2  /* multiple public IPs for load */
set interface nat44 in tap0 out tap1
nat44 add interface address tap1   /* masquerade mode */
 
/* Static DNAT mapping */
nat44 add static mapping tcp local 10.0.0.5 8080 external 203.0.113.1 80
 
/* Per-worker session distribution */
/* VPP: each worker thread has its own session cache slice */
/* New session → hash five-tuple → assign to worker thread */
/* All subsequent packets of same flow → same worker (RSS ensures this) */
 
/* Monitoring */
show nat44 sessions                   /* active session count and list */
show nat44 sessions detail            /* full field dump */
show nat44 summary                    /* pool usage, allocations */
show nat44 addresses                  /* public IP pool */
show errors                           /* NAT error counters */
 
/* VPP NAT error counters */
nat44-ed-in2out: packet does not match existing session: new connections
nat44-ed-in2out: out of ports: port pool exhausted
nat44-ed-in2out: TCP RST packet without session: likely stale RST
nat44-ed-out2in: unknown session: return packet with no matching session
 
/* Debugging a specific session */
nat44 del session in 10.0.0.5:54321 out 203.0.113.1:12345 tcp
/* Manually remove a stale session */</pre></div>
  </div>
</div>
</div>


<div id="t8" class="tab-pane">
<p class="sep">ATTACKS AND HARDENING</p>

<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>Attack Taxonomy and Mitigations</h3><span class="tag tag-red">SECURITY</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Attack</th><th>Mechanism</th><th>Impact</th><th>Mitigation</th></tr></thead>
      <tbody>
        <tr><td><strong>SYN Flood</strong></td><td>Spoofed SYNs → half-open sessions → session table exhaustion</td><td>DoS — all new connections rejected</td><td>SYN cookies; rate limit per source; half-open session cap</td></tr>
        <tr><td><strong>Session Table Exhaustion</strong></td><td>Many short-lived connections filling the table</td><td>New connections dropped globally</td><td>Per-source rate limit; aggressive half-open timeout; alert at 80% fill</td></tr>
        <tr><td><strong>RST Injection</strong></td><td>Crafted RST with valid five-tuple → session torn down</td><td>Disrupts legitimate connections; BGP attacks</td><td>Sequence number validation — RST must be within window</td></tr>
        <tr><td><strong>NAT Port Exhaustion</strong></td><td>Source opens 64K connections → port pool drained</td><td>Further outbound connections fail</td><td>Per-source connection limit; monitor port pool; alert</td></tr>
        <tr><td><strong>NAT Slipstreaming</strong></td><td>Browser crafts HTTP request that tricks SIP/FTP ALG → arbitrary port opened</td><td>External attacker reaches internal services</td><td>Disable unused ALGs; validate ALG content; block inbound 5060/21</td></tr>
        <tr><td><strong>IP Fragmentation Bypass</strong></td><td>Fragment 1 with no ports passes filter; fragment 2 contains attack in offset</td><td>Policy bypass</td><td>Reassemble ALL fragments before conntrack lookup</td></tr>
        <tr><td><strong>Overlapping Fragments</strong></td><td>Send two overlapping fragments with different content — OS and NGFW reassemble differently</td><td>IDS/NGFW evasion</td><td>Drop overlapping fragments; or enforce first/last-fragment policy</td></tr>
        <tr><td><strong>Teardrop / Tiny Fragment</strong></td><td>Fragment so small that TCP header split across two fragments</td><td>Stack crash (historical); policy bypass</td><td>Drop fragments too small to contain complete L4 header</td></tr>
      </tbody>
    </table>

<div class="cb"><pre>/* SYN Cookie — no state until 3-way handshake verified */
/* ISN = HMAC(4-tuple + timestamp) — encodes connection info */
 
uint32_t syn_cookie_gen(uint32_t sip, uint32_t dip,
                         uint16_t sport, uint16_t dport,
                         uint32_t ts_tick, const uint8_t *key) {
    uint8_t data[14];
    memcpy(data,      &sip,   4);
    memcpy(data + 4,  &dip,   4);
    memcpy(data + 8,  &sport, 2);
    memcpy(data + 10, &dport, 2);
    memcpy(data + 12, &ts_tick, 2);   /* low 16 bits of time */
    uint8_t mac[32];
    HMAC_SHA256(key, 32, data, sizeof(data), mac);
    return ntohl(*(uint32_t *)mac) ^ (ts_tick & 0xFFFF);
}
 
/* On receiving ACK for SYN-ACK: */
int syn_cookie_verify(uint32_t client_ack, ...) {
    /* client sends ACK = cookie + 1 */
    uint32_t expected = syn_cookie_gen(...) + 1;
    return (client_ack == expected);
}
/* If valid: create session entry NOW — entire SYN phase was stateless */
/* SYN cookies sacrifice MSS options (encoded as upper 3 bits of ISN) */
 
/* Half-open connection limit */
#define MAX_HALF_OPEN  100000   /* global limit */
#define MAX_PER_SOURCE 100      /* per source IP limit */
 
atomic_uint half_open_count = 0;
 
int session_allow_new_syn(uint32_t src_ip) {
    if (atomic_load(&half_open_count) >= MAX_HALF_OPEN)
        return 0;   /* global limit — trigger SYN cookies */
    if (src_rate_get(src_ip) > MAX_PER_SOURCE)
        return 0;   /* per-source limit */
    atomic_fetch_add(&half_open_count, 1);
    return 1;
}</pre></div>
  </div>
</div>
</div>


<div id="t9" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>High-Performance Session Table in C</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a complete session table with five-tuple hashing, TCP state machine, timer-wheel timeout management, and SYN cookie defence. Benchmark at realistic NGFW throughput.</p>
    <div class="lab-step"><div class="sn">1</div><div><strong>Canonical normalisation:</strong> implement <code>normalise_key()</code> and unit-test it exhaustively: verify that (A:1234→B:80,TCP) and (B:80→A:1234,TCP) produce the same canonical key. Test with IPv4 and IPv6 addresses. This is the most common conntrack bug — get it right before building anything else.</div></div>
    <div class="lab-step"><div class="sn">2</div><div><strong>Hash table:</strong> implement an open-addressing hash table with Robin Hood probing and a pre-allocated session pool. Target: 1M entries, load factor capped at 70%. Write a benchmark: insert 700K sessions, then perform 10M lookups (80% hits, 20% misses). Measure average lookup latency with <code>clock_gettime(CLOCK_MONOTONIC)</code>. Target: &lt;100ns average.</div></div>
    <div class="lab-step"><div class="sn">3</div><div><strong>TCP state machine:</strong> implement as a transition table (not if/else). Test every state×direction×flags combination. Specific tests: SYN-ACK without prior SYN → DROP; RST with out-of-window sequence → DROP (count injection attempt); FIN in ESTABLISHED → transition to FIN_WAIT_1; duplicate SYN in ESTABLISHED → log anomaly, DROP.</div></div>
    <div class="lab-step"><div class="sn">4</div><div><strong>Timer wheel:</strong> implement 65536-bucket timer wheel. Test: create 100K sessions with varying timeouts (5s–3600s), advance the clock second by second, verify sessions expire at exactly the right tick. Measure: how long does advancing the timer wheel take per second? Should be O(expired_sessions) not O(all_sessions).</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>SYN cookie:</strong> implement HMAC-SHA256-based SYN cookie generation and verification. Simulate a SYN flood: 500K SYNs from random spoofed IPs, no session entries created. Send SYN-ACK with cookie. Then send 1K valid ACKs — verify sessions created only for those. Measure session table depth during flood vs without cookies.</div></div>
    <div class="lab-step"><div class="sn">6</div><div><strong>Integration:</strong> combine all components. Process a 10,000-packet pcap through your session table: create sessions on SYN, track state through handshake and data, expire on FIN/RST. Print the final session table contents and verify they match what Wireshark shows for the same pcap. Use <code>tcpdump -r test.pcap -tttt</code> to generate your test data.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>NAPT Packet Rewriter</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Implement a working NAPT engine using AF_PACKET, with correct incremental checksum updates. Verify with real HTTP traffic flowing through it.</p>
    <div class="lab-step"><div class="sn">1</div><div><strong>Port pool:</strong> implement the bitmap-based port allocator. Test: allocate 64,000 ports, verify no duplicates (use a set to check). Free 32,000 random ports. Re-allocate 32,000 — verify freed slots are reused. Benchmark: 1M allocations/second target.</div></div>
    <div class="lab-step"><div class="sn">2</div><div><strong>Incremental checksum:</strong> implement <code>csum_update_u32()</code> from Tab 5. Test against full checksum recalculation: for 10,000 random packets, verify that incremental update gives the same result as recalculating from scratch. Any mismatch means a bug — connections will silently break in production.</div></div>
    <div class="lab-step"><div class="sn">3</div><div><strong>AF_PACKET forwarder:</strong> using the namespace topology from M14 Lab 2, receive packets on the inside interface (AF_PACKET), look up the session table, rewrite headers for NAPT, and inject out the outside interface. Handle both TCP and UDP. Test with curl and ping through your NAPT.</div></div>
    <div class="lab-step"><div class="sn">4</div><div><strong>DNAT rule:</strong> add a static DNAT mapping: external port 8080 → internal 10.1.0.5:80. Implement as a pre-lookup check: if dst_ip == external_ip and dst_port == 8080 → rewrite before session lookup. Verify with: <code>curl http://external_ip:8080</code> reaching the internal web server.</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Fragment handling:</strong> test with fragmented packets: <code>ping -s 3000 -M dont 10.2.0.2</code> (sends oversized packets that will be fragmented). Verify that your NAPT correctly handles fragment 1 (has TCP/UDP header) and fragment 2+ (no transport header — use session from fragment 1). Incorrect handling here is a common security bypass.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>VPP NAT44-ED Deep Inspection</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Configure VPP NAT44-ED in detail, inspect session internals, test edge cases, and compare with your Lab 1 implementation.</p>
    <div class="lab-step"><div class="sn">1</div><div>Configure VPP with tap interfaces as in M18. Enable NAT44-ED with 1M session table. Generate diverse traffic: HTTP, HTTPS, DNS, ICMP ping. Run <code>vppctl show nat44 sessions detail</code> — capture the output. For each session, identify: ED key fields, state, byte counters, NAT port allocation. Compare to your Lab 1 session_t layout.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Test port exhaustion: write a client that opens connections in a tight loop. Monitor <code>vppctl show nat44 addresses</code> for port pool fill level. Identify the exact error counter that increments on exhaustion (<code>show errors | grep nat44</code>). What happens to existing connections when new ones fail? Is there any prioritisation?</div></div>
    <div class="lab-step"><div class="sn">3</div><div>DNAT + SNAT simultaneously: configure a DNAT rule so external port 80 reaches an internal server, while that server makes outbound connections that are SNAT'd. Make the server send an HTTP request while serving an incoming one. Capture on both inside and outside interfaces. Trace the four-tuple rewriting for each direction.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Hairpinning: can a host on the inside reach the published DNAT address (the external VIP) from inside? Configure appropriately and test. This requires VPP to apply DNAT for inside→inside traffic through the NAT — most NATs get this wrong. Document VPP's behaviour and how to fix it if it fails.</div></div>
  </div>
</div>
</div>


<div id="ta" class="tab-pane">
<p class="sep">M23 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know why stateful inspection beats stateless: validates protocol state, blocks crafted packets, auto-permits return traffic, enables per-flow L7 features</li>
  <li>Know the five-tuple: src_ip, dst_ip, src_port, dst_port, protocol — and that both flow directions must map to the same session entry</li>
  <li>Know canonical normalisation: why it's needed, how to implement it (compare and swap if needed), and what bugs occur without it</li>
  <li>Know session_t key fields: five-tuple, TCP state, seq/ack/window tracking, timestamps, counters, NAT mapping, app_id, policy_id, DPI state pointer</li>
  <li>Know session sizing guidance: 256 bytes × 1M sessions = 256MB; typical NGFW 500K–4M sessions</li>
  <li>Know why memory pool beats malloc/free: no fragmentation, O(1) alloc, better cache locality</li>
  <li>Know hash table requirements: O(1) lookup, lock-free concurrent access, cache-friendly layout</li>
  <li>Know clib_bihash and rte_hash as the two primary production choices</li>
  <li>Know timer wheel: O(1) session expiry; 65536 buckets at 1s resolution = 18h range</li>
  <li>Know per-protocol timeouts: TCP SYN 30s, TCP ESTAB 3600s, UDP 30s, UDP DNS 10s, ICMP 10s</li>
  <li>Know TCP conntrack states and transitions: NONE → SYN_SENT → SYN_RCVD → ESTABLISHED → FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT → CLOSED</li>
  <li>Know TCP sequence validation: accept only within window; RST with wrong seq = injection attack → drop</li>
  <li>Know window scale option must be parsed from SYN — else window is too narrow and false positives occur</li>
  <li>Know UDP pseudo-session: created on first permitted datagram, transitions NEW → REPLIED on first return</li>
  <li>Know QUIC special handling: Connection IDs survive IP change; 5-tuple keyed sessions break on mobile handoff</li>
  <li>Know ICMP Echo tracking: identifier field is the session discriminator; must decode type/code to normalise direction</li>
  <li>Know ICMP error correlation: extract inner IP five-tuple from ICMP error payload to find the triggered session</li>
  <li>Know ICMP Redirect (type 5) must always be dropped — routing attack vector</li>
  <li>Know 5 NAT types: static 1:1, dynamic pool, NAPT/PAT, DNAT, twice-NAT</li>
  <li>Know NAPT port pool: bitmap allocator, 64K ports per public IP per protocol, round-robin allocation</li>
  <li>Know NAPT packet rewrite: which fields change (src_ip, src_port for SNAT; dst_ip, dst_port for DNAT) and why checksums must be updated</li>
  <li>Know incremental checksum update (RFC 1624): faster than full recalculation; critical correctness requirement</li>
  <li>Know why ALGs exist: embedded IP:port in payload breaks NAT; ALG patches payload content</li>
  <li>Know SIP ALG complexity: must patch SDP body, Content-Length, multiple headers, TCP seq numbers on size change</li>
  <li>Know VPP NAT44-ED: endpoint-dependent keying; two lookup tables; worker-thread per-session distribution</li>
  <li>Know VPP NAT commands: show nat44 sessions, show nat44 summary, nat44 add static mapping</li>
  <li>Know SYN cookie: ISN = HMAC(4-tuple + timestamp); no state during SYN flood; session created on ACK verification</li>
  <li>Know 8 conntrack/NAT attacks and mitigations: SYN flood, table exhaustion, RST injection, port exhaustion, NAT slipstreaming, fragmentation bypass, overlapping fragment, tiny fragment</li>
  <li>Completed Lab 1: session table with hash, TCP FSM, timer wheel, SYN cookies — benchmarked and integration-tested</li>
  <li>Completed Lab 2: NAPT engine with bitmap port pool, incremental checksum, AF_PACKET forwarding, DNAT rule, fragment handling</li>
  <li>Completed Lab 3: VPP NAT44-ED configuration, session inspection, port exhaustion test, hairpinning test</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M24 - Deep Packet Inspection and Application Identification</strong> — building L7 inspection on top of the conntrack session table foundation you now fully understand.</p>
</div>
</div>

<div class="mod-nav">
  <a href="/learning/networking-mastery/m22-ssl-inspection/">← M22 SSL Inspection</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m24-dpi/">Next: M24 - DPI →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
