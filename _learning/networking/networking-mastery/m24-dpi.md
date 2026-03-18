---
layout: default
title: "M24 - Deep Packet Inspection and Application Identification"
permalink: /learning/networking-mastery/m24-dpi/
---
<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#0a2a10 35%,#1a5a20 65%,#0a4018 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#80f090;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#b0f8c0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#d0ffd8}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#80f090;border-bottom-color:#80f090}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1a6a20}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#b0f0c0;white-space:pre}
.cm{color:#407840}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#edfff0;border:1.5px solid #1a6a20;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#081e08;border-color:#2a8a30}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#0a4010}[data-theme=dark] .ins strong{color:#80f090}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#0a5010;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a6a20}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #1a6a20;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#1a6a20;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.45rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.6}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#1a6a20;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.48rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.55;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1a6a20;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 6 · MODULE 24 · WEEK 23</div>
  <div class="mod-title">🔬 Deep Packet Inspection and Application Identification</div>
  <div class="mod-subtitle">DPI architecture · Pattern matching engines · Aho-Corasick · TLS fingerprinting · App identification · Evasion techniques · Hyperscan · Per-flow DPI state</div>
  <div class="mod-pills">
    <span class="mod-pill">Advanced</span>
    <span class="mod-pill">Prerequisite: M23 Conntrack</span>
    <span class="mod-pill">Core NGFW Differentiator</span>
    <span class="mod-pill">3 Labs</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">DPI Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">Pattern Matching Engines</button>
  <button class="tab-btn" onclick="vt(event,'t2')">Aho-Corasick</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Hyperscan</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Protocol Dissection</button>
  <button class="tab-btn" onclick="vt(event,'t5')">App Identification</button>
  <button class="tab-btn" onclick="vt(event,'t6')">TLS Fingerprinting</button>
  <button class="tab-btn" onclick="vt(event,'t7')">DPI Evasion</button>
  <button class="tab-btn" onclick="vt(event,'t8')">DPI in VPP</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'ta')">Checklist</button>
</div>


<div id="t0" class="tab-pane active">
<p class="sep">DPI — LOOKING INSIDE THE PACKET PAYLOAD</p>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔬</span><h3>What DPI Is and Why It Matters</h3><span class="tag tag-green">OVERVIEW</span></div>
  <div class="cp-body">
    <p>Deep Packet Inspection (DPI) is the analysis of packet payloads beyond the IP/TCP/UDP headers — examining application-layer content. Where conntrack tracks flow state, DPI understands what application is running inside the flow and what it's doing. DPI is what separates a "next-generation" firewall from a traditional stateful firewall.</p>
    <p><strong>What DPI enables that conntrack alone cannot:</strong></p>
    <ul>
      <li><strong>Application identification</strong> — distinguish Netflix vs YouTube vs general HTTPS, BitTorrent vs FTP, Zoom vs generic UDP</li>
      <li><strong>URL filtering with path accuracy</strong> — block example.com/malware.exe while allowing example.com/homepage</li>
      <li><strong>Malware payload detection</strong> — match signatures of known malware C2 protocols, exploit payloads, backdoor communication patterns</li>
      <li><strong>Data Loss Prevention (DLP)</strong> — detect credit card numbers, NIN/PAN, source code patterns, confidential keywords in cleartext traffic</li>
      <li><strong>Protocol anomaly detection</strong> — DNS over HTTPS that isn't really DNS, tunnelling in legitimate protocol wrappers (DNS tunnelling, ICMP tunnelling)</li>
      <li><strong>Bandwidth management</strong> — rate-limit P2P, throttle video streaming, prioritise VoIP — but only if you can tell them apart</li>
    </ul>
    <p><strong>DPI challenges:</strong> inspecting every byte of every packet at line rate (10–100 Gbps) while maintaining per-flow reassembled context is computationally expensive. The key is making the common case (established, known-good, classified flow) as fast as possible — and only doing deep work on new or suspicious flows.</p>
  </div>
</div>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>DPI Architecture — Three Inspection Layers</h3><span class="tag tag-blue">ARCHITECTURE</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Three-layer DPI architecture */

Layer 1: Protocol dissection (deterministic, fast)
  Parse packet structure according to known protocol specs.
  HTTP: parse method, URL, Host header, Content-Type.
  DNS:  parse QTYPE, QNAME, response codes.
  TLS:  parse ClientHello extensions (SNI, ALPN, cipher suites).
  Cost: O(header_length) — fast, deterministic.
  Accuracy: 100% for well-formed packets.

Layer 2: Signature matching (pattern matching engine)
  Match payload against a database of application/threat signatures.
  "GET /admin/login" + User-Agent: sqlmap → SQL injection scan
  "\x4d\x5a\x90" at offset 0 → Windows PE executable (malware download)
  Cost: O(payload_length × signature_complexity) — Hyperscan makes this fast.
  Accuracy: high for known threats; zero for novel/unknown.

Layer 3: Behavioural / heuristic analysis
  Track flow statistics over time: packet rates, sizes, timing, entropy.
  High-entropy payload + base32/hex subdomains → DNS tunnelling.
  Regular 30-second beacons to same IP → C2 communication.
  Cost: O(1) per packet with accumulated per-flow statistics.
  Accuracy: probabilistic; tune false-positive rate.

/* DPI integration with conntrack */

First packet of new flow:
  1. conntrack: create session entry
  2. DPI: begin protocol dissection — what protocol is this?
  3. DPI: run signature pass on first N bytes
  4. If identified: update session->app_id, cache for fast path

Fast path (identified flow):
  1. conntrack: session lookup — found, app_id known
  2. Apply cached action (permit/block/rate-limit)
  3. DPI: optionally continue L3 analysis (malware scan in background)

/* DPI state per flow */
typedef struct dpi_state {
    uint16_t protocol;       /* partially identified protocol */
    uint8_t  depth;          /* how many bytes consumed so far */
    uint8_t  phase;          /* which parse phase we're in */
    void    *parser_state;   /* protocol-specific parser context */
    uint32_t reassembly_len; /* bytes in TCP reassembly buffer */
    uint8_t *reassembly_buf; /* TCP reassembly for multi-segment parsing */
} dpi_state_t;
/* Stored in session_t->dpi_state — persists for flow lifetime */</pre></div>
  </div>
</div>
</div>


<div id="t1" class="tab-pane">
<p class="sep">PATTERN MATCHING ENGINES</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>String Matching Algorithms Compared</h3><span class="tag tag-blue">ALGORITHMS</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Algorithm</th><th>Time Complexity</th><th>Best For</th><th>NGFW Use</th></tr></thead>
      <tbody>
        <tr><td><strong>Naive search</strong></td><td>O(n × m) per pattern</td><td>Single pattern, prototyping</td><td>Never — too slow at scale</td></tr>
        <tr><td><strong>Boyer-Moore-Horspool</strong></td><td>O(n/m) average, O(nm) worst</td><td>Single pattern, long patterns</td><td>Useful for specific long strings (file headers)</td></tr>
        <tr><td><strong>Aho-Corasick</strong></td><td>O(n + m + z) total (n=text, m=patterns, z=matches)</td><td>Multiple patterns simultaneously</td><td>Core of most open-source IDS (Snort, Suricata)</td></tr>
        <tr><td><strong>Wu-Manber</strong></td><td>O(n × B/m) typical</td><td>Many short patterns with same prefix</td><td>Virus scanning engines</td></tr>
        <tr><td><strong>Hyperscan (Intel)</strong></td><td>O(n) with SIMD acceleration</td><td>Large regex rule sets, SIMD parallelism</td><td>State-of-the-art for NGFW — Snort 3, VPP</td></tr>
        <tr><td><strong>RE2 / PCRE2</strong></td><td>O(n) RE2, O(2^n) worst PCRE</td><td>Complex regex — RE2 is linear guaranteed</td><td>Complex patterns; avoid PCRE in hot path</td></tr>
        <tr><td><strong>Bloom filter pre-filter</strong></td><td>O(1) per byte — probabilistic</td><td>Fast elimination of non-matching flows</td><td>First stage: if bloom says no-match, skip Aho-Corasick entirely</td></tr>
      </tbody>
    </table>

<div class="cb"><pre>/* Why Aho-Corasick is the standard for multi-pattern matching */

Problem: we have 50,000 signatures. For each packet payload:
  Naive:       50,000 × strlen(payload) operations → completely unusable
  Aho-Corasick: O(strlen(payload) + matches) — single pass through text
                 All 50,000 patterns matched simultaneously

How it works:
  1. Build a finite automaton (trie + failure links) from all patterns
  2. Feed the text through the automaton one byte at a time
  3. Automaton visits exactly one state per input byte
  4. On entering a match state: output all matching patterns
  5. No backtracking, no re-scanning

Build time:  O(total_pattern_bytes) — done once at startup
Memory:      O(total_pattern_bytes × alphabet_size)
Match time:  O(text_length + matches) — linear scan, ideal for DPI

/* Trade-off: AC uses a lot of memory (trie nodes × 256 transitions) */
/* For 50K signatures × 10 bytes average = 500KB × 256 = 128MB minimum */
/* Optimisation: use compressed transition tables for sparse alphabets */</pre></div>
  </div>
</div>
</div>


<div id="t2" class="tab-pane">
<p class="sep">AHO-CORASICK — BUILDING AND USING THE AUTOMATON</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>Aho-Corasick Implementation</h3><span class="tag tag-teal">IMPLEMENTATION</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Aho-Corasick trie node */
#define AC_ALPHABET  256
typedef struct ac_node {
    int          children[AC_ALPHABET]; /* -1 = no child */
    int          fail;                  /* failure link */
    int          output;                /* pattern ID or -1 */
    int          output_link;           /* chain of outputs at this state */
} ac_node_t;

typedef struct {
    ac_node_t *nodes;
    int        n_nodes;
    int        n_alloc;
    /* Pattern storage */
    const char **patterns;
    int          n_patterns;
} ac_trie_t;

/* Build phase 1: insert all patterns into the trie */
void ac_insert(ac_trie_t *ac, const char *pattern, int pat_id) {
    int cur = 0;  /* start at root */
    for (int i = 0; pattern[i]; i++) {
        unsigned char c = pattern[i];
        if (ac->nodes[cur].children[c] == -1) {
            /* Create new node */
            ac->nodes[cur].children[c] = ac->n_nodes++;
            memset(&ac->nodes[ac->n_nodes-1], -1, sizeof(ac_node_t));
        }
        cur = ac->nodes[cur].children[c];
    }
    ac->nodes[cur].output = pat_id;  /* mark as accepting state */
}

/* Build phase 2: compute failure links (BFS) */
void ac_build_failure(ac_trie_t *ac) {
    int queue[1024*1024], head = 0, tail = 0;

    /* Root's children: fail link → root */
    for (int c = 0; c < AC_ALPHABET; c++) {
        int ch = ac->nodes[0].children[c];
        if (ch != -1) {
            ac->nodes[ch].fail = 0;
            queue[tail++] = ch;
        } else {
            ac->nodes[0].children[c] = 0;  /* loop at root */
        }
    }

    while (head < tail) {
        int u = queue[head++];
        /* Output link: chain patterns matched at suffix of current prefix */
        int fl = ac->nodes[u].fail;
        if (ac->nodes[fl].output != -1)
            ac->nodes[u].output_link = fl;
        else
            ac->nodes[u].output_link = ac->nodes[fl].output_link;

        for (int c = 0; c < AC_ALPHABET; c++) {
            int v = ac->nodes[u].children[c];
            if (v != -1) {
                ac->nodes[v].fail = ac->nodes[ac->nodes[u].fail].children[c];
                queue[tail++] = v;
            } else {
                /* Shortcut: direct goto fail's transition */
                ac->nodes[u].children[c] = ac->nodes[ac->nodes[u].fail].children[c];
            }
        }
    }
}

/* Search: feed text through automaton */
typedef void (*match_cb)(int pat_id, int offset, void *ctx);

void ac_search(ac_trie_t *ac, const uint8_t *text, size_t len,
               match_cb cb, void *ctx) {
    int state = 0;
    for (size_t i = 0; i < len; i++) {
        state = ac->nodes[state].children[text[i]];
        /* Report all matches ending at position i */
        int s = state;
        while (s != -1 && ac->nodes[s].output != -1) {
            cb(ac->nodes[s].output, i, ctx);
            s = ac->nodes[s].output_link;
        }
    }
}

/* Per-flow DPI: carry state across TCP segments */
/* The automaton state at the end of segment N is the start state for N+1 */
void dpi_process_segment(dpi_state_t *dpi, const uint8_t *data, size_t len) {
    /* Resume from where we left off in this flow */
    ac_search_stateful(&dpi->ac_state, data, len, match_cb, dpi);
    /* dpi->ac_state is preserved between calls */
}</pre></div>
    <div class="ins"><p>💡 <strong>Carrying automaton state across TCP segments is essential for NGFW DPI.</strong> An attacker can split a signature like <code>SELECT * FROM users</code> across two TCP segments with the split in the middle — segment 1 ends with "SELECT * FR" and segment 2 starts with "OM users". A DPI engine that only inspects individual packets never sees the complete signature. The correct approach: save the automaton state at the end of each segment and restore it at the start of the next segment of the same flow.</p></div>
  </div>
</div>
</div>


<div id="t3" class="tab-pane">
<p class="sep">HYPERSCAN — INTEL'S SIMD-ACCELERATED REGEX ENGINE</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Hyperscan Architecture and NGFW Integration</h3><span class="tag tag-purple">HYPERSCAN</span></div>
  <div class="cp-body">
    <p>Hyperscan (open-sourced by Intel in 2015, now a Linux Foundation project as Vectorscan) is the most advanced pattern matching library for network security. It compiles regular expressions and string patterns into SIMD-accelerated finite automata that run at near-memory-bandwidth speed.</p>
<div class="cb"><pre>/* Hyperscan: key features */
- Compiles regex patterns to SIMD automata at startup
- Uses SSE4.2 / AVX2 / AVX-512 to match 16/32/64 bytes per cycle
- Supports complex PCRE-like patterns: anchors, character classes,
  quantifiers, lookaheads (subset)
- Streaming mode: maintains state across packet boundaries (critical for NGFW)
- Block mode: one-shot match on a buffer
- Vectored mode: match across a list of non-contiguous buffers
- Reports all matches (not just first)

/* Hyperscan NGFW integration */
#include <hs/hs.h>

/* Compile patterns at startup */
const char *patterns[] = {
    "(?i)select.{0,20}from.{0,20}where",   /* SQL injection */
    "(?i)<script[^>]*>",                    /* XSS */
    "X5O!P%@AP\\[4\\\\PZX54\\(P\\^\\)7CC\\)7}",  /* EICAR test virus */
    "\\bpassword\\b.{0,10}=",              /* credential in cleartext */
    "(?i)cmd\\.exe|/bin/sh|powershell",    /* command execution */
};
const unsigned int flags[] = {
    HS_FLAG_CASELESS|HS_FLAG_SOM_LEFTMOST,
    HS_FLAG_CASELESS,
    0,
    HS_FLAG_CASELESS,
    HS_FLAG_CASELESS,
};
const unsigned int ids[] = { SIG_SQLI, SIG_XSS, SIG_EICAR, SIG_DLP_CRED, SIG_CMDINJ };

hs_database_t *db;
hs_compile_error_t *err;
hs_compile_multi(patterns, flags, ids,
    sizeof(patterns)/sizeof(*patterns), HS_MODE_STREAM, NULL, &db, &err);

/* Per-connection: create a scratch space (thread-local) and stream */
hs_scratch_t *scratch;
hs_alloc_scratch(db, &scratch);

hs_stream_t *stream;   /* one stream per TCP connection */
hs_open_stream(db, 0, &stream);

/* Per-packet: scan the payload */
static int on_match(unsigned int id, unsigned long long from,
                    unsigned long long to, unsigned int flags, void *ctx) {
    dpi_result_t *r = (dpi_result_t *)ctx;
    r->matched_sig = id;
    r->match_offset = to;
    return 0;   /* 0 = continue; 1 = stop after first match */
}

hs_scan_stream(stream, (const char *)payload, payload_len,
               0, scratch, on_match, &result);

/* On connection close: */
hs_close_stream(stream, scratch, on_match, &result);
hs_free_scratch(scratch);

/* Performance: 3–10 Gbps per core for typical NGFW signature sets */
/* Hyperscan consistently outperforms Aho-Corasick for regex patterns */
/* Fallback: PCRE for patterns Hyperscan can't compile (rare edge cases) */</pre></div>
  </div>
</div>
</div>


<div id="t4" class="tab-pane">
<p class="sep">PROTOCOL DISSECTION — STRUCTURED PAYLOAD PARSING</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>HTTP and DNS Dissectors</h3><span class="tag tag-blue">DISSECTORS</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* HTTP/1.1 dissector — parse request line and headers */
typedef struct {
    char     method[8];       /* GET, POST, PUT, etc. */
    char     url[2048];       /* full URL path + query string */
    char     host[256];       /* Host header */
    char     user_agent[512];
    char     content_type[128];
    uint32_t content_length;
    int      is_complete;     /* headers fully received */
} http_request_t;

int http_dissect_request(const uint8_t *data, size_t len,
                          http_request_t *req, dpi_state_t *dpi) {
    /* Find end of headers: \r\n\r\n */
    const uint8_t *hdr_end = memmem(data, len, "\r\n\r\n", 4);
    if (!hdr_end) {
        /* Headers not complete yet — buffer and wait for more data */
        buffer_append(dpi, data, len);
        return HTTP_NEED_MORE;
    }

    /* Parse request line: "GET /path HTTP/1.1\r\n" */
    const char *p = (const char *)data;
    const char *sp1 = memchr(p, ' ', hdr_end - (uint8_t *)p);
    if (!sp1) return HTTP_PARSE_ERROR;
    memcpy(req->method, p, sp1 - p);

    const char *sp2 = memchr(sp1 + 1, ' ', hdr_end - (uint8_t *)(sp1+1));
    if (!sp2) return HTTP_PARSE_ERROR;
    memcpy(req->url, sp1 + 1, sp2 - sp1 - 1);

    /* Parse headers line by line */
    const char *line = strchr(p, '\n') + 1;
    while (line < (const char *)hdr_end) {
        const char *eol = memchr(line, '\r', hdr_end - (uint8_t *)line);
        if (!eol) break;

        if (strncasecmp(line, "Host:", 5) == 0)
            memcpy(req->host, line + 6, MIN(eol - line - 6, 255));
        else if (strncasecmp(line, "User-Agent:", 11) == 0)
            memcpy(req->user_agent, line + 12, MIN(eol - line - 12, 511));
        else if (strncasecmp(line, "Content-Length:", 15) == 0)
            req->content_length = atoi(line + 16);

        line = eol + 2;  /* skip \r\n */
    }
    req->is_complete = 1;
    return HTTP_OK;
}

/* DNS dissector — fast path for the most common DPI target */
int dns_dissect(const uint8_t *data, size_t len, dns_info_t *di) {
    if (len < 12) return DNS_TOO_SHORT;
    const uint16_t *hdr = (const uint16_t *)data;
    di->txid    = ntohs(hdr[0]);
    uint16_t flags = ntohs(hdr[1]);
    di->is_response = (flags >> 15) & 1;
    di->rcode       = flags & 0xF;
    di->qdcount     = ntohs(hdr[2]);

    /* Parse QNAME from question section (offset 12) */
    int off = 12;
    char *qn = di->qname;
    while (off < len && data[off]) {
        uint8_t label_len = data[off++];
        if (label_len & 0xC0) { off++; break; }  /* compression pointer */
        if (qn > di->qname) *qn++ = '.';
        memcpy(qn, data + off, label_len);
        qn += label_len; off += label_len;
    }
    *qn = '\0';

    di->qtype  = (off + 3 < len) ? ntohs(*(uint16_t *)(data + off + 1)) : 0;
    di->qclass = (off + 5 < len) ? ntohs(*(uint16_t *)(data + off + 3)) : 0;
    return DNS_OK;
}</pre></div>
  </div>
</div>
</div>


<div id="t5" class="tab-pane">
<p class="sep">APPLICATION IDENTIFICATION</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🏷️</span><h3>Multi-Layer App ID Engine</h3><span class="tag tag-purple">APP ID</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Application identification: multiple signals combined */

Signal 1: Well-known ports (quick heuristic, not reliable)
  dst_port 80  → likely HTTP (but could be anything)
  dst_port 443 → likely HTTPS/TLS
  dst_port 53  → likely DNS
  dst_port 22  → likely SSH
Reliability: 60-70% (many apps use non-standard ports)

Signal 2: Protocol banner / handshake signature
  "SSH-2.0-"        → SSH
  "GET / HTTP/1"    → HTTP/1.1
  "\x16\x03\x03"   → TLS 1.2 (ContentType=22, Version=3.3)
  "\x16\x03\x01"   → TLS 1.0 ClientHello (even for TLS 1.3 compat)
  DNS message structure at offset 0

Signal 3: TLS SNI / ALPN (for HTTPS flows without inspection)
  SNI "netflix.com"        → Netflix
  SNI "api.whatsapp.com"   → WhatsApp
  ALPN "h3"                → HTTP/3
  ALPN "h2"                → HTTP/2

Signal 4: Certificate Subject / Issuer
  cert issued by "Let's Encrypt" to "*.zoom.us" → Zoom
  cert issued by "DigiCert" to "*.facebook.com" → Facebook

Signal 5: JA3 TLS fingerprint
  JA3 = MD5(SSLVersion,Ciphers,Extensions,EllipticCurves,CurveFormats)
  Each TLS client library has a characteristic fingerprint
  Known malware JA3: "51c64c77e60f3980eea90869b68c58a8" → Metasploit
  Firefox JA3: distinct from Chrome, distinct from curl

Signal 6: Deep payload (requires inspection)
  HTTP Host header → exact destination domain
  HTTP User-Agent  → client application
  BitTorrent handshake "\x13BitTorrent protocol" → P2P

/* App ID state machine */
typedef enum {
    APPID_UNKNOWN,
    APPID_DETECTING,    /* partial identification in progress */
    APPID_IDENTIFIED,   /* confident identification */
    APPID_ENCRYPTED,    /* TLS — can't inspect further without SSL bump */
} appid_state_t;

uint16_t identify_application(session_t *s, const uint8_t *payload,
                               uint16_t plen, int is_fwd) {
    dpi_state_t *dpi = s->dpi_state;

    /* Fast: check if already identified */
    if (s->app_id != APPID_UNKNOWN) return s->app_id;

    /* Layer 1: port-based heuristic */
    uint16_t hint = port_to_appid(s->key.dst_port);

    /* Layer 2: TLS check — first 3 bytes */
    if (plen >= 3 && payload[0] == 0x16 &&
        (payload[1] == 3) && (payload[2] <= 4)) {
        dpi->is_tls = 1;
        /* Parse SNI from ClientHello if it's a handshake record */
        if (payload[5] == 1 /* ClientHello */) {
            char sni[256];
            if (tls_extract_sni(payload, plen, sni)) {
                s->app_id = sni_to_appid(sni);
                return s->app_id;
            }
        }
        return APPID_ENCRYPTED;
    }

    /* Layer 3: protocol signature matching */
    s->app_id = signature_match(payload, plen, hint);
    return s->app_id;
}</pre></div>
  </div>
</div>
</div>


<div id="t6" class="tab-pane">
<p class="sep">TLS FINGERPRINTING — IDENTIFYING WITHOUT DECRYPTION</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔏</span><h3>JA3, JA3S, JA4 and JARM</h3><span class="tag tag-teal">TLS FINGERPRINTING</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* JA3 — TLS ClientHello fingerprint */
/* Identifies the TLS CLIENT LIBRARY regardless of what's inside TLS */

JA3 = MD5(SSLVersion + "," + Ciphers + "," + Extensions + "," +
           EllipticCurves + "," + EllipticCurvePointFormats)

Fields extracted from TLS ClientHello:
  SSLVersion:              TLS record version (e.g., 771 = TLS 1.2 compat)
  Ciphers:                 cipher suite IDs, hyphen-separated, sorted
  Extensions:              extension type codes, hyphen-separated
  EllipticCurves:          supported groups extension values
  EllipticCurvePointFormats: point format extension values

/* JA3 construction example */
ClientHello has:
  Version: 0x0303 (771)
  Ciphers: [0x1301, 0x1302, 0x1303, 0xc02b, 0xc02c, ...]
  Extensions: [0, 5, 10, 11, 13, 17, 23, 35, 51, 65281, ...]
  Supported Groups: [0x001d, 0x0017, 0x0018, ...]  (X25519, P-256, P-384)
  Point Formats: [0]  (uncompressed)

JA3_string = "771,4865-4866-4867-49195-49196,...,0-5-10-11-13-17-23-35-51-65281,...,29-23-24,...,0"
JA3_hash   = MD5(JA3_string) = "bfbe6f6dba10b5d82e96766f4de6d75a"

/* Computing JA3 from libpcap capture */
#include <pcap.h>
/* Parse TLS record: type=22 (handshake), find ClientHello (type=1) */
/* Extract all fields, build string, MD5 */

/* JA3S — Server fingerprint */
JA3S = MD5(SSLVersion + "," + Cipher + "," + Extensions)
/* Identifies the TLS SERVER implementation */
/* JA3 + JA3S pair = unique fingerprint of a specific client-server pair */

/* JA4 (2023, John Althouse) — improvements over JA3 */
/* Format: TLSVersion_SNI_NumCiphers_NumExtensions_ALPN_hash(ciphers)_hash(extensions) */
/* More human-readable, more stable, better collision resistance */
JA4 = "t13d1516h2_8daaf6152771_02713d6af862"
/* t=TLS, 13=1.3, d=SNI present, 1516=1.3 first two cipher bytes, h2=ALPN */

/* JARM — Active TLS server fingerprinting */
/* Send 10 specially crafted ClientHellos to target server */
/* Hash the sequence of ServerHellos received */
/* Identifies: server TLS library, version, configuration */
/* Useful for: identifying C2 servers, distinguishing Cobalt Strike from nginx */
jarm "104.244.42.1" → "2ad2ad0002ad2ad00042d42d000000506d7c848..." → Cloudflare
jarm "52.x.x.x"     → "07d14d16d21d21d07c07d14d07d21d56c8798..." → Cobalt Strike

/* NGFW JA3 database */
known_malware_ja3 = {
    "51c64c77e60f3980eea90869b68c58a8": "Metasploit/Meterpreter",
    "e7d705a3286e19ea42f587b344ee6865": "TrickBot trojan",
    "6734f37431670b3ab4292b8f60f29984": "Emotet C2",
    "a0e9f5d64349fb13191bc781f81f42e1": "Cobalt Strike default profile",
}
/* Alert if outbound TLS has a JA3 matching a known malware fingerprint */</pre></div>
  </div>
</div>
</div>


<div id="t7" class="tab-pane">
<p class="sep">DPI EVASION TECHNIQUES AND COUNTERMEASURES</p>

<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">⚠️</span><h3>How Attackers Evade DPI</h3><span class="tag tag-red">EVASION</span></div>
  <div class="cp-body">
    <table class="t-table">
      <thead><tr><th>Evasion Technique</th><th>How It Works</th><th>Countermeasure</th></tr></thead>
      <tbody>
        <tr><td><strong>Signature splitting</strong></td><td>Split a known signature across two TCP segments so no single packet contains the full match: "SELECT * FR" + "OM users --"</td><td>TCP stream reassembly before pattern matching. Carry Aho-Corasick/Hyperscan state across segments.</td></tr>
        <tr><td><strong>Fragmentation</strong></td><td>Split signature across IP fragments. DPI engine only sees fragments, not reassembled payload.</td><td>IP reassembly before DPI. Track fragment IDs; buffer until complete packet.</td></tr>
        <tr><td><strong>Encoding variations</strong></td><td>URL-encode (%41 = A), double-encode, Unicode normalisation. "SELECT" → "%53ELECT" → not matched by literal signature.</td><td>Normalise payload before matching: URL-decode, HTML-decode, Unicode normalise. Multi-layer decode loop.</td></tr>
        <tr><td><strong>Case variations</strong></td><td>"sElEcT * fRoM" — case-insensitive matching not applied.</td><td>Use case-insensitive flags in all pattern matches. HYPERSCAN: HS_FLAG_CASELESS.</td></tr>
        <tr><td><strong>Insertion attacks</strong></td><td>Send a packet with bad checksum or TTL=1 between the split signature — DPI engine sees the bad packet; the endpoint ignores it and reassembles the signature cleanly.</td><td>Normalise TTL (set consistent value), validate checksums before DPI. Drop or ignore bad-checksum packets before inspection.</td></tr>
        <tr><td><strong>Tunnelling</strong></td><td>Wrap C2 traffic in allowed protocol (DNS, HTTPS, ICMP). DPI sees allowed outer protocol, not C2 inner content.</td><td>Behavioural analysis: query frequency, label entropy (DNS tunnelling), timing patterns. Without SSL inspection: JA3 + certificate analysis.</td></tr>
        <tr><td><strong>Protocol switching</strong></td><td>Use a port or protocol the NGFW treats as trusted: port 443, HTTP/2, QUIC. Hope inspection is less thorough or disabled.</td><td>Apply same DPI rules regardless of port. Force HTTPS inspection. Block QUIC UDP 443 if inspection not available.</td></tr>
        <tr><td><strong>Polymorphic payload</strong></td><td>Malware generates unique C2 protocol per infection using a cryptographic key. No fixed signature exists.</td><td>Behavioural detection: beacon timing analysis, connection frequency, data volume patterns, ML anomaly detection.</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>


<div id="t8" class="tab-pane">
<p class="sep">DPI IN VPP — INTEGRATION ARCHITECTURE</p>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>VPP DPI Plugin Architecture</h3><span class="tag tag-green">VPP DPI</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* DPI in VPP: custom graph node in ip4-unicast feature arc */

Pipeline with DPI:
  dpdk-input → ethernet-input → ip4-input
    → acl-plugin-in-ip4-fa (conntrack, first pass ACL)
    → ngfw-dpi-node         (L7 identification and signature match)
    → ip4-lookup → ip4-rewrite → interface-output

/* DPI node implementation pattern */
VLIB_NODE_FN(ngfw_dpi_node)(vlib_main_t *vm,
                              vlib_node_runtime_t *node,
                              vlib_frame_t *frame)
{
    u32 n_left = frame->n_vectors;
    u32 *from  = vlib_frame_vector_args(frame);
    u16 nexts[VLIB_FRAME_SIZE];

    while (n_left >= 4) {
        vlib_prefetch_buffer_with_index(vm, from[2], LOAD);
        vlib_prefetch_buffer_with_index(vm, from[3], LOAD);

        vlib_buffer_t *b0 = vlib_get_buffer(vm, from[0]);
        vlib_buffer_t *b1 = vlib_get_buffer(vm, from[1]);

        /* Get session from buffer metadata (set by acl-plugin) */
        u32 sess_idx0 = vnet_buffer2(b0)->session_index;
        u32 sess_idx1 = vnet_buffer2(b1)->session_index;
        session_t *s0 = pool_elt_at_index(session_pool, sess_idx0);
        session_t *s1 = pool_elt_at_index(session_pool, sess_idx1);

        /* Get payload */
        ip4_header_t *ip0 = vlib_buffer_get_current(b0);
        uint8_t *payload0 = (uint8_t *)ip0 + ip0->ip_version_and_header_length * 4;
        /* ... (skip TCP/UDP header) ... */

        /* Classify if not yet done */
        if (s0->app_id == APPID_UNKNOWN)
            s0->app_id = dpi_classify(s0, payload0, payload_len0);

        /* Signature match */
        dpi_result_t r0 = {0};
        if (s0->dpi_state)
            hs_scan_stream(s0->dpi_state->hs_stream,
                           (const char *)payload0, payload_len0,
                           0, dpi_scratch, dpi_on_match, &r0);

        nexts[0] = r0.blocked ? NGFW_DPI_NEXT_DROP : NGFW_DPI_NEXT_PERMIT;
        nexts[1] = /* similar for b1 */;

        from += 2; n_left -= 2; nexts += 2;
    }
    /* scalar tail */

    vlib_buffer_enqueue_to_next(vm, node,
        vlib_frame_vector_args(frame), nexts, frame->n_vectors);
    return frame->n_vectors;
}

/* Per-flow Hyperscan stream allocation */
void dpi_session_create(session_t *s) {
    dpi_state_t *dpi = clib_mem_alloc(sizeof(dpi_state_t));
    hs_open_stream(dpi_db, 0, &dpi->hs_stream);
    s->dpi_state = dpi;
}

void dpi_session_destroy(session_t *s) {
    dpi_state_t *dpi = s->dpi_state;
    hs_close_stream(dpi->hs_stream, dpi_scratch, NULL, NULL);
    clib_mem_free(dpi);
    s->dpi_state = NULL;
}

/* Performance considerations */
/* Hyperscan stream allocation: ~microseconds — do at session creation */
/* Per-packet scan: microseconds for typical payloads at 1K+ signatures */
/* For 4M sessions: 4M × ~256B hs_stream = ~1GB memory for DPI state */
/* Mitigation: only enable stream DPI on unclassified/suspicious flows */
/* Once app_id known: only run signatures relevant to that app */</pre></div>
  </div>
</div>
</div>


<div id="t9" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Aho-Corasick Multi-Pattern Matching Engine</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a complete Aho-Corasick engine from scratch. Test it against a realistic DPI signature set. Verify cross-segment matching works correctly.</p>
    <div class="lab-step"><div class="sn">1</div><div>Implement the trie insertion and failure link computation (BFS) as shown in Tab 2. Use a flat array of ac_node_t structs with pre-allocated pool — avoid dynamic allocation per node. Test with a simple set: patterns "he", "she", "his", "hers". Verify they match correctly in "ushers": matches at positions 1(she), 2(he), 5(hers).</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Add 100 real NGFW-style patterns: SQL injection keywords, XSS patterns, file headers (PE: MZ\x90, ELF: \x7fELF, PDF: %PDF), and common malware strings. Load them into your AC engine. Run on a 1MB HTTP log file and count match frequencies per signature.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Implement stateful cross-segment matching: split a known SQL injection string "UNION SELECT password FROM users" into 8 random-length chunks. Verify that processing all chunks sequentially with the saved automaton state produces the same match as processing the full string. Then test with a signature that starts at the end of chunk 3 and ends at the start of chunk 4 — this is the critical evasion scenario.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Benchmark: build AC trie for 1000 patterns (varying lengths 5–30 bytes). Process 10MB of mixed HTTP/DNS/TLS traffic at maximum speed. Measure: throughput in MB/s, average matches per KB, memory usage for the trie. Then compare with a naive multi-pattern search (nested loops) — document the speedup.</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Evasion test:</strong> take 5 known signatures and create evaded variants: (a) URL-encode one character, (b) split across two segments, (c) change case, (d) insert extra whitespace. Which evasions bypass your current engine? What changes would detect each? Implement URL decode as a pre-processing step and rerun.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>HTTP and DNS Protocol Dissector</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build production-quality HTTP and DNS dissectors. Integrate with your M23 session table. Test on real captured traffic.</p>
    <div class="lab-step"><div class="sn">1</div><div>Implement the HTTP/1.1 request dissector from Tab 4. Test exhaustively: normal GET/POST, chunked encoding, headers split across packets, 100-continue handshake, pipelining (multiple requests in one TCP segment). For each case, verify the dissector correctly extracts method, URL, Host, User-Agent, Content-Type.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Add HTTP response dissection: parse status code, Content-Type, Content-Length, Set-Cookie, Location (for redirects). Test on responses to your requests from Lab 2. For a 301 redirect, verify the Location header is parsed and the dissector could follow it (implement redirect tracking in session).</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Implement the DNS dissector from Tab 4. Handle: A, AAAA, CNAME, MX, TXT queries; label compression pointers (RFC 1035 §4.1.4); truncated responses (TC=1 flag); EDNS0 OPT pseudo-RR; DNSSEC-related record types. Test against a 10,000-packet DNS capture from a real network.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>DLP rule: scan HTTP POST bodies for patterns matching credit card numbers (Luhn algorithm), Indian PAN numbers (ABCDE1234F format), and Aadhaar numbers (12-digit). Generate test HTTP traffic that contains these patterns. Verify detection. Implement the Luhn checksum verifier to reduce false positives.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Integrate with your M23 session table: when the HTTP dissector identifies an application (Host header → known service), update session->app_id. When DNS reveals a new domain being queried, look it up in a threat intel database (use a simple in-memory hash of known-bad domains). Log a threat if found.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>TLS Fingerprinting and JA3 Calculator</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Implement JA3 fingerprinting from raw TLS ClientHello packets. Build a database of known fingerprints and test against real traffic.</p>
    <div class="lab-step"><div class="sn">1</div><div>Write a TLS ClientHello parser: given the raw bytes of a TLS record (type=22, msg_type=1), extract all the fields needed for JA3: SSL version, cipher suites list, extension type list, supported groups, EC point formats. Handle: extensions in any order, missing extensions (set to empty string), GREASE values (0x?A?A) which must be excluded from JA3.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Implement JA3 string construction and MD5 hashing. Verify your implementation against known test vectors: capture a ClientHello from Chrome, Firefox, and curl. Compute JA3 hashes. Compare with online JA3 calculators (ja3er.com or Wireshark's ja3 dissector plugin) to verify correctness.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Build a JA3 threat database: download the ja3-fingerprints.csv from a public repository (GitHub: salesforce/ja3). Load into a hash table. Process a 100,000-packet TLS pcap. For each ClientHello, compute JA3 and look up in your database. Report: how many distinct JA3 hashes? How many match known malware families? How many are unrecognised?</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Also extract JA3S (server fingerprint) from ServerHello packets. Track JA3+JA3S pairs per connection. Look for anomalies: the same JA3 (same client) connecting to many different servers — could be a malware scanner. Implement a simple anomaly score: JA3s with >100 unique server contacts in 1 hour get flagged.</div></div>
  </div>
</div>
</div>


<div id="ta" class="tab-pane">
<p class="sep">M24 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know what DPI enables beyond conntrack: app identification, URL path filtering, malware payload detection, DLP, protocol anomaly detection, bandwidth management</li>
  <li>Know the 3 DPI inspection layers: protocol dissection (structured parsing), signature matching (pattern engine), behavioural heuristics (statistics over time)</li>
  <li>Know why per-flow DPI state is necessary: TCP stream reassembly, cross-segment signature matching, protocol parser continuation</li>
  <li>Know the 7 pattern matching algorithms and when to use each: naive, Boyer-Moore, Aho-Corasick, Wu-Manber, Hyperscan, RE2, Bloom filter</li>
  <li>Know Aho-Corasick complexity: O(n+m+z) for n=text, m=total pattern bytes, z=matches — linear in text length regardless of number of patterns</li>
  <li>Know AC construction phases: trie insertion, BFS failure link computation, shortcut transition filling</li>
  <li>Know why carrying AC state across TCP segments matters: split-signature evasion attack</li>
  <li>Know Hyperscan: Intel/Linux Foundation library, SIMD-accelerated regex, streaming mode for NGFW, HS_MODE_STREAM, per-flow hs_stream_t</li>
  <li>Know Hyperscan flags: HS_FLAG_CASELESS, HS_FLAG_SOM_LEFTMOST, HS_FLAG_DOTALL</li>
  <li>Know HTTP dissector requirements: handle headers split across segments, chunked encoding, pipelining, 100-continue</li>
  <li>Know DNS dissector requirements: label compression pointers (0xC0 prefix), EDNS0 OPT RR, query/response correlation</li>
  <li>Know the 6 App ID signals: port hint, banner/handshake, TLS SNI/ALPN, certificate subject, JA3 fingerprint, deep payload</li>
  <li>Know JA3 construction: MD5 of (SSLVersion,Ciphers,Extensions,Groups,PointFormats) with GREASE values excluded</li>
  <li>Know JA3S: server-side fingerprint from ServerHello; JA3+JA3S pair identifies specific client-server pair</li>
  <li>Know JA4: improved fingerprint format (2023); more human-readable; less collision-prone than JA3</li>
  <li>Know JARM: active TLS server fingerprinting; identifies C2 servers by their TLS configuration</li>
  <li>Know 8 DPI evasion techniques and their countermeasures: splitting, fragmentation, encoding, case, insertion, tunnelling, protocol switching, polymorphic</li>
  <li>Know normalisation chain before pattern matching: IP reassembly → TCP stream reassembly → URL decode → HTML decode → case fold</li>
  <li>Know VPP DPI integration: custom node in ip4-unicast arc; per-flow hs_stream; lazy allocation (only for unclassified flows)</li>
  <li>Know Hyperscan memory cost: ~256B per stream × number of concurrent sessions; selective activation strategy</li>
  <li>Completed Lab 1: Aho-Corasick engine with cross-segment state; evasion testing; benchmark vs naive</li>
  <li>Completed Lab 2: HTTP+DNS dissectors; DLP credit card/PAN detection; session app_id integration</li>
  <li>Completed Lab 3: JA3 calculator with GREASE filtering; threat database lookup; JA3S anomaly detection</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M25 - IDS/IPS and Threat Detection</strong> — combining DPI signature matching with network anomaly detection and threat intelligence correlation.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/networking-mastery/m23-conntrack-nat/' | relative_url }}">← M23 Conntrack/NAT</a>
  <a href="{{ '/learning/networking-mastery/' | relative_url }}">🗺️ Roadmap</a>
  <a class="nb" href="{{ '/learning/networking-mastery/m25-ids-ips/' | relative_url }}">Next: M25 - IDS/IPS →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
