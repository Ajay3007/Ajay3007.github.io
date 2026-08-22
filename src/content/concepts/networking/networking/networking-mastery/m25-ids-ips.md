---
title: "M25 - IDS/IPS and Threat Detection"
description: "NETWORKING MASTERY · PHASE 6 · MODULE 25 · WEEK 24 🚨 IDS/IPS and Threat Detection IDS vs IPS · Snort rule syntax · Suricata architecture · Anomaly detection · Beacon detection…"
domain: networking
track: networking-mastery
order: 25
url: /learning/networking-mastery/m25-ids-ips/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#2a0808 35%,#5a1010 65%,#400808 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#ff9090;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#ffd0d0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#ffe8e8}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#ff9090;border-bottom-color:#ff9090}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #901010}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#ffc8c8;white-space:pre}
.cm{color:#805050}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#fff0f0;border:1.5px solid #901010;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#200808;border-color:#b03030}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#600010}[data-theme=dark] .ins strong{color:#ff9090}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#700010;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#901010}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #901010;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#901010;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.45rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.6}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#901010;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.48rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.55;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#901010;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>

<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 6 · MODULE 25 · WEEK 24</div>
  <div class="mod-title">🚨 IDS/IPS and Threat Detection</div>
  <div class="mod-subtitle">IDS vs IPS · Snort rule syntax · Suricata architecture · Anomaly detection · Beacon detection · Threat intelligence · Network anomaly scoring · Alert tuning</div>
  <div class="mod-pills">
    <span class="mod-pill">Advanced</span>
    <span class="mod-pill">Prerequisite: M24 DPI</span>
    <span class="mod-pill">Defensive Security Core</span>
    <span class="mod-pill">3 Labs</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">IDS vs IPS</button>
  <button class="tab-btn" onclick="vt(event,'t1')">Snort Rules</button>
  <button class="tab-btn" onclick="vt(event,'t2')">Suricata Architecture</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Anomaly Detection</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Beacon Detection</button>
  <button class="tab-btn" onclick="vt(event,'t5')">Threat Intelligence</button>
  <button class="tab-btn" onclick="vt(event,'t6')">DNS Threat Detection</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Alert Tuning</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Checklist</button>
</div>


<div id="t0" class="tab-pane active">
<p class="sep">IDS vs IPS — DETECTION vs PREVENTION</p>

<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🚨</span><h3>IDS, IPS, and Their Role in NGFW</h3><span class="tag tag-red">OVERVIEW</span></div>
  <div class="cp-body">
    <p>An IDS (Intrusion Detection System) observes network traffic and generates alerts when suspicious patterns are found — it does not block. An IPS (Intrusion Prevention System) sits inline and can drop, reset, or redirect traffic in real time. Modern NGFWs incorporate IPS as a feature — the same engine that does conntrack and NAT also applies IPS rules inline.</p>
    <div class="two-col">
      <div>
        <h4>IDS (Detection Only)</h4>
        <ul>
          <li>Passive tap or SPAN port — not in traffic path</li>
          <li>No impact on network performance or availability</li>
          <li>Cannot block — only alert</li>
          <li>False positives: annoying but not disruptive</li>
          <li>Use: visibility and logging, SOC analytics</li>
          <li>Tools: Zeek (Bro), Suricata in IDS mode</li>
        </ul>
      </div>
      <div>
        <h4>IPS (Prevention Inline)</h4>
        <ul>
          <li>Inline in traffic path — all packets traverse it</li>
          <li>Can block, reset connections, quarantine</li>
          <li>False positives = blocking legitimate traffic (critical)</li>
          <li>False negatives = missed attacks (also critical)</li>
          <li>Performance matters: adds latency if slow</li>
          <li>Tools: Snort 3, Suricata in IPS mode, NGFW built-in IPS</li>
        </ul>
      </div>
    </div>
    <h4>Detection Methods — Complementary Approaches</h4>
    <table class="t-table">
      <thead><tr><th>Method</th><th>Detects</th><th>Misses</th><th>False Positive Rate</th></tr></thead>
      <tbody>
        <tr><td><strong>Signature-based</strong></td><td>Known malware, known exploits, known C2 protocols</td><td>Zero-day, novel variants, obfuscated/encrypted threats</td><td>Low (if signatures well-maintained)</td></tr>
        <tr><td><strong>Anomaly-based</strong></td><td>Novel attacks that deviate from baseline behaviour</td><td>Attacks that mimic normal traffic patterns</td><td>High (requires careful tuning)</td></tr>
        <tr><td><strong>Heuristic / behavioural</strong></td><td>Patterns of suspicious behaviour: port scans, beacons, lateral movement</td><td>Slow/stealthy attackers that stay under thresholds</td><td>Medium</td></tr>
        <tr><td><strong>Threat intelligence (IoC)</strong></td><td>Known bad IPs, domains, hashes, URLs</td><td>New IoCs not yet in feeds, fast-flux infrastructure</td><td>Very low (IoCs are highly specific)</td></tr>
      </tbody>
    </table>
  </div>
</div>
</div>


<div id="t1" class="tab-pane">
<p class="sep">SNORT/SURICATA RULE SYNTAX</p>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">📋</span><h3>Rule Anatomy and Key Options</h3><span class="tag tag-orange">RULES</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Snort/Suricata rule structure */
/* action proto src_ip src_port direction dst_ip dst_port (options) */

alert tcp $EXTERNAL_NET any -> $HOME_NET 22 (
    msg:"ET SCAN SSH Brute Force";
    flow:established,to_server;
    threshold:type both,track by_src,count 5,seconds 60;
    sid:2001219; rev:7;
    classtype:attempted-admin;
)

/* Rule header fields */
action:    alert|drop|pass|reject|rejectsrc|rejectdst|rejectboth
proto:     tcp|udp|icmp|ip|http|dns|tls|smb|dcerpc
direction: -> (one way) | <> (both directions)
src/dst:   IP/CIDR, negation with !, list [1.1.1.1, 2.2.2.2],
           variables: $HOME_NET, $EXTERNAL_NET, $HTTP_SERVERS, $SMTP_SERVERS

/* Critical options */

/* Content matching */
content:"malware.exe";          /* match literal bytes */
content:"|48 65 6c 6c 6f|";   /* hex bytes */
content:"SELECT";nocase;        /* case-insensitive */
content:"UNION"; distance:0; within:10; /* relative to last match */
pcre:"/SELECT.{0,10}FROM/is";  /* PCRE regex */

/* Flow control */
flow:established,to_server;   /* only on established, client→server */
flow:established,to_client;   /* server→client replies */
flow:stateless;                /* match even on non-established */

/* HTTP-specific options (Suricata HTTP engine) */
http.method; content:"POST";          /* match HTTP method */
http.uri; content:"/admin";           /* match URI path */
http.host; content:"evil.example";    /* match Host header */
http.user_agent; content:"sqlmap";    /* match User-Agent */
http.stat_code; content:"200";        /* match status code */
http.response_body; content:"error";  /* match response body */

/* TLS options */
tls.sni; content:"evil.onion";        /* match SNI */
tls.subject; content:"CN=Meterpreter"; /* match cert subject */
tls.issuerdn; content:"CN=evil-ca";   /* match cert issuer */
tls.fingerprint; content:"ab:cd:ef:..."; /* match cert fingerprint */
ja3_hash; content:"51c64c77e60f3980eea90869b68c58a8"; /* JA3 */
ja3s_hash; content:"...";              /* JA3S */

/* Thresholds and suppression */
threshold:type limit,track by_src,count 1,seconds 60;
/* Only alert once per source IP per 60s (suppress noisy alerts) */
threshold:type both,track by_src,count 10,seconds 1;
/* Alert if >10 in 1s (rate-based detection: port scan, brute force) */
threshold:type threshold,track by_src,count 5,seconds 10;
/* Alert every 5th occurrence per source per 10s */

/* Reference and classification */
reference:url,attack.mitre.org/techniques/T1021/;
classtype:attempted-user;    /* trojan-activity, attempted-recon, etc. */
priority:1;                  /* 1=high, 2=medium, 3=low */
sid:2100001;                 /* unique rule ID */
rev:3;                       /* revision number */</pre></div>
  </div>
</div>
</div>


<div id="t2" class="tab-pane">
<p class="sep">SURICATA — MULTI-THREADED IDS/IPS ENGINE</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>Suricata Architecture</h3><span class="tag tag-blue">ARCHITECTURE</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Suricata thread model */

Receive threads (RX):
  Read packets from NIC (AF_PACKET, AF_XDP, DPDK, PCAP)
  Decode: Ethernet → IP → TCP/UDP → application headers
  Distribute to worker threads (via flow hash for ordering)

Worker threads (decode + detect):
  Each thread handles a subset of flows
  Per-flow state: conntrack + app-layer parsers + detect engine
  Hyperscan/AC for payload inspection
  Produces: alert events, flow records, file extracts

Output threads:
  Write alerts: EVE JSON, Unified2 (for Snort-compatible output)
  Write flow records: NetFlow-like summaries
  Write extracted files: malware samples, documents from HTTP/SMTP

/* Suricata packet flow */
Packet → RX Thread → Flow Hash → Worker Thread:
  1. IP defragmentation (reassemble fragments)
  2. Stream tracking (TCP segment reassembly)
  3. App-layer detection (HTTP, TLS, DNS, SMTP, SMB parsers)
  4. Rule detection (Hyperscan + keyword matching)
  5. Action (alert/drop/pass)
  6. Logging (EVE JSON)

/* Suricata AF_XDP mode (high performance) */
suricata:
  af-xdp:
    interface: eth0
    threads: 4
    xdp-mode: driver
    use-mmap: yes
    ring-size: 2048

/* Suricata IPS mode (inline with NFQUEUE or AF_PACKET) */
# NFQUEUE mode: Netfilter sends packets to Suricata for verdict
iptables -A FORWARD -j NFQUEUE --queue-num 0

suricata:
  nfq:
    mode: accept
    fail-open: yes   /* pass traffic if Suricata crashes */

# AF_PACKET IPS mode (bypass when possible)
suricata:
  af-packet:
    - interface: eth0
      cluster-id: 99
      cluster-type: cluster_flow
      copy-mode: ips
      copy-iface: eth1   /* forward to eth1 if not dropped */

/* Suricata EVE JSON output — structured logging */
{
  "timestamp": "2024-01-15T10:23:45.123456+0000",
  "flow_id": 123456789,
  "event_type": "alert",
  "src_ip": "192.168.1.50",
  "src_port": 54321,
  "dest_ip": "198.51.100.5",
  "dest_port": 443,
  "proto": "TCP",
  "alert": {
    "action": "blocked",
    "gid": 1,
    "signature_id": 2019401,
    "rev": 4,
    "signature": "ET CNC Feodo Tracker Reported C2 in Use",
    "category": "A Network Trojan was Detected",
    "severity": 1
  },
  "tls": {
    "sni": "malicious.example.com",
    "version": "TLS 1.3",
    "ja3": { "hash": "51c64c77e60f3980eea90869b68c58a8" }
  },
  "app_proto": "tls"
}</pre></div>
  </div>
</div>
</div>


<div id="t3" class="tab-pane">
<p class="sep">ANOMALY DETECTION — STATISTICAL BASELINES AND DEVIATIONS</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Network Anomaly Detection Techniques</h3><span class="tag tag-purple">ANOMALY DETECTION</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Anomaly detection: build a model of "normal" and alert on deviations */

/* 1. Port scan detection */
/* Normal: one source contacts a few services */
/* Anomaly: one source contacts many distinct ports */

typedef struct {
    uint32_t src_ip;
    uint16_t ports_contacted[1024];  /* bitmap of dst_ports in last 60s */
    uint32_t unique_ports;
    uint64_t window_start_ns;
} portscan_tracker_t;

void portscan_update(portscan_tracker_t *t, uint16_t dst_port,
                     uint64_t now_ns) {
    /* Reset window if expired */
    if (now_ns - t->window_start_ns > 60e9) {
        memset(t->ports_contacted, 0, sizeof(t->ports_contacted));
        t->unique_ports = 0;
        t->window_start_ns = now_ns;
    }
    /* Add this port to bitmap */
    uint16_t b = dst_port / 8, bi = dst_port % 8;
    if (!(t->ports_contacted[b] & (1 << bi))) {
        t->ports_contacted[b] |= (1 << bi);
        t->unique_ports++;
    }
    if (t->unique_ports > 100)    /* threshold */
        alert(PORTSCAN, t->src_ip);
}

/* 2. DDoS detection — per-destination traffic volume */
/* Track bytes/packets to each destination per second */
/* Alert when rate exceeds N × average (N=10 for 10x normal) */

/* 3. DNS anomaly — high query rate or long labels (tunnelling) */
/* Normal DNS: 10–100 queries/minute from a host */
/* DNS tunnelling: hundreds/sec; query labels contain base32/hex data */

typedef struct {
    uint32_t src_ip;
    uint32_t queries_in_window;
    uint64_t window_start_ns;
    float    avg_label_length;   /* exponential moving average */
    float    label_entropy;      /* Shannon entropy of label chars */
} dns_tracker_t;

float shannon_entropy(const char *label, int len) {
    int freq[256] = {0};
    for (int i = 0; i < len; i++) freq[(unsigned char)label[i]]++;
    float h = 0;
    for (int i = 0; i < 256; i++) {
        if (freq[i]) {
            float p = (float)freq[i] / len;
            h -= p * log2f(p);
        }
    }
    return h;
}
/* DNS label entropy: normal words ~3.5 bits/char */
/* Base32 encoded data: ~4.7 bits/char (higher — more uniform distribution) */
/* Threshold: label entropy > 4.0 in labels > 15 chars → suspicious */

/* 4. Connection profile anomaly */
/* Build per-host baseline: typical ports, destinations, bytes/hour */
/* Alert when deviation exceeds Z-score threshold */
/* Implemented as exponential moving average + standard deviation */

float ewma_update(float prev_avg, float new_val, float alpha) {
    return alpha * new_val + (1 - alpha) * prev_avg;
}
/* alpha = 0.1 → slow learning (stable baseline) */
/* Z-score = (current - mean) / stddev; alert if > 3.0 */</pre></div>
  </div>
</div>
</div>


<div id="t4" class="tab-pane">
<p class="sep">BEACON DETECTION — FINDING C2 COMMUNICATION</p>

<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">📡</span><h3>Detecting Periodic C2 Callbacks</h3><span class="tag tag-red">BEACON DETECTION</span></div>
  <div class="cp-body">
    <p>Modern malware (Cobalt Strike, Metasploit, many RATs) uses periodic "beaconing" — the implant calls home to the C2 server on a fixed schedule. A Cobalt Strike beacon with a 60-second sleep plus 30% jitter will call home every 42–78 seconds. This regularity is detectable statistically.</p>
<div class="cb"><pre>/* Beacon detection algorithm */
/* For each (src_ip, dst_ip, dst_port) tuple that has multiple connections: */
/* Compute the inter-arrival times (IAT) between connection attempts */
/* A beacon has low variance in IAT (periodic) */

typedef struct {
    uint32_t src_ip;
    uint32_t dst_ip;
    uint16_t dst_port;
    uint64_t timestamps[64];   /* last 64 connection timestamps (ns) */
    uint32_t count;
} beacon_tracker_t;

typedef struct {
    float    period;       /* estimated beacon period in seconds */
    float    jitter;       /* standard deviation as fraction of period */
    float    score;        /* 0.0 = random, 1.0 = perfect beacon */
} beacon_result_t;

beacon_result_t detect_beacon(beacon_tracker_t *t) {
    if (t->count < 8) return (beacon_result_t){0};  /* not enough data */

    /* Compute inter-arrival times */
    float iats[63];
    int n = MIN(t->count - 1, 63);
    for (int i = 0; i < n; i++)
        iats[i] = (t->timestamps[i+1] - t->timestamps[i]) / 1e9;  /* seconds */

    /* Mean and standard deviation of IAT */
    float mean = 0, variance = 0;
    for (int i = 0; i < n; i++) mean += iats[i];
    mean /= n;
    for (int i = 0; i < n; i++) variance += (iats[i] - mean) * (iats[i] - mean);
    variance /= n;
    float stddev = sqrtf(variance);

    /* Coefficient of variation: stddev / mean */
    /* Perfect beacon: CV = 0 */
    /* Cobalt Strike with 30% jitter: CV ≈ 0.17 */
    /* Random HTTP browsing: CV ≈ 0.8–2.0 */
    float cv = stddev / mean;

    beacon_result_t r = {
        .period = mean,
        .jitter = cv,
        .score  = MAX(0.0f, 1.0f - (cv / 0.5f))  /* 1.0 if CV=0, 0 if CV>0.5 */
    };

    /* Alert thresholds */
    if (r.score > 0.7 && mean > 10.0f && mean < 3600.0f)
        alert_beacon(t->src_ip, t->dst_ip, t->dst_port, &r);

    return r;
}

/* Cobalt Strike beacon periods to watch for */
/* Default sleep: 60s */
/* Common configs: 5s, 30s, 60s, 300s, 3600s */
/* Jitter: 10–50% (controlled randomisation) */

/* HTTPS beacon evasion — how beacons hide */
/* Malleable C2 profiles: beacon looks like legitimate browser traffic */
/* User-Agent: Mozilla/5.0 (matching current Chrome) */
/* URIs: /jquery-3.3.1.min.js, /jquery.min.map, etc. */
/* Headers: matching legitimate CDN patterns */
/* Countermeasure: JA3 fingerprint + certificate check + timing analysis */</pre></div>
  </div>
</div>
</div>


<div id="t5" class="tab-pane">
<p class="sep">THREAT INTELLIGENCE — IOC CORRELATION</p>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🌐</span><h3>IoC Types, Sources, and Integration</h3><span class="tag tag-teal">THREAT INTEL</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* IoC types */
IP addresses:   Known C2 servers, malware infrastructure, botnets
Domains:        Malware domains, DGA domains, phishing domains
URLs:           Specific malicious URLs (drive-by download, phishing pages)
File hashes:    MD5/SHA256 of known malware binaries
JA3 hashes:     Malware TLS fingerprints
Certificate:    Fingerprints of rogue/malware certificates
Email headers:  From addresses, subject patterns for phishing
User-Agents:    Known malware/scanner User-Agent strings

/* Threat intel feed sources */
Open source:
  Feodo Tracker:    https://feodotracker.abuse.ch/  (Emotet, TrickBot C2)
  Abuse.ch URLHAUS: malware download URLs
  MalwareBazaar:    file hashes of known malware
  MISP:             community threat sharing platform
  AlienVault OTX:   open threat exchange IoCs
  EmergingThreats:  Suricata/Snort rule feed

Commercial:
  Recorded Future, CrowdStrike Intelligence, FireEye iSIGHT,
  IBM X-Force Exchange, VirusTotal Intelligence

/* Integration architecture */
typedef struct {
    /* IP blacklist — hash set for O(1) lookup */
    rte_hash_t   *bad_ips;      /* uint32_t → threat_info_t */

    /* Domain blacklist — trie for fast prefix/suffix matching */
    domain_trie_t *bad_domains;  /* "evil.com" → threat_info_t */

    /* URL blacklist — hash of full URLs */
    rte_hash_t   *bad_urls;

    /* JA3 blacklist — hash set */
    rte_hash_t   *bad_ja3;

    /* Metadata */
    uint64_t      last_update_ns;
    uint32_t      total_entries;
} threat_intel_db_t;

typedef struct {
    uint8_t  threat_type;    /* MALWARE_C2, PHISHING, BOTNET, SCANNER... */
    uint8_t  confidence;     /* 0–100 confidence score */
    uint32_t first_seen;     /* unix timestamp */
    uint32_t last_seen;
    char     malware_family[32];
} threat_info_t;

/* Inline check in NGFW forwarding path */
int check_threat_intel(session_t *s, threat_intel_db_t *db) {
    threat_info_t *ti;

    /* Check destination IP */
    if (rte_hash_lookup_data(db->bad_ips, &s->key.dst_ip, (void **)&ti) >= 0) {
        session_set_threat(s, ti);
        return 1;  /* block or alert */
    }

    /* Check JA3 (populated by TLS parser) */
    if (s->ja3[0] && rte_hash_lookup_data(db->bad_ja3, s->ja3, (void **)&ti) >= 0) {
        session_set_threat(s, ti);
        return 1;
    }

    return 0;
}

/* Feed update — live reload without restart */
/* Double-buffered: build new table in background, atomic swap */
void threat_intel_update(threat_intel_db_t **live, const char *feed_url) {
    threat_intel_db_t *new_db = download_and_parse_feed(feed_url);
    threat_intel_db_t *old_db = atomic_exchange(live, new_db);
    /* Wait for in-flight lookups to complete, then free old_db */
    rte_delay_us(1000);  /* 1ms grace period */
    threat_intel_db_free(old_db);
}</pre></div>
  </div>
</div>
</div>


<div id="t6" class="tab-pane">
<p class="sep">DNS THREAT DETECTION — DGA, TUNNELLING, FAST-FLUX</p>

<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🔍</span><h3>DNS as Both an Attack Vector and Detection Goldmine</h3><span class="tag tag-amber">DNS THREATS</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* DNS provides unique visibility: malware must resolve C2 domains */
/* Every DNS query is visible (unless DoH or encrypted DNS) */

/* 1. Domain Generation Algorithm (DGA) detection */
/* Malware generates hundreds of random domains per day */
/* Tries each until one resolves (C2 server registered one of them) */
/* Human-unreadable: "x7kqp2mntb.com", "ajwhfksdfh.net" */

/* DGA detection signals: */
/* - Domain > 15 chars in SLD (second-level domain) */
/* - High consonant-to-vowel ratio (no pronounceable words) */
/* - High character entropy (random character distribution) */
/* - Domain never seen before (no historical resolution) */
/* - Multiple NXDOMAIN responses in sequence */

/* Feature extraction for DGA classification */
typedef struct {
    char     domain[256];
    int      sld_length;       /* length of just the SLD (no TLD) */
    float    vowel_ratio;      /* vowels / total chars */
    float    entropy;          /* Shannon entropy of SLD characters */
    float    digit_ratio;      /* digits / total chars */
    int      unique_chars;     /* distinct characters used */
    int      max_run;          /* longest run of same character class */
} domain_features_t;

int is_dga(const domain_features_t *f) {
    /* Simple heuristic classifier */
    int score = 0;
    if (f->sld_length > 12) score += 2;
    if (f->entropy > 3.8)   score += 3;   /* high randomness */
    if (f->vowel_ratio < 0.25) score += 2; /* few vowels */
    if (f->digit_ratio > 0.3)  score += 1; /* many digits */
    if (f->unique_chars < 8)   score -= 1; /* might be normal */
    return score >= 5;   /* threshold */
    /* For production: use ML model (random forest) trained on labelled data */
}

/* 2. DNS tunnelling detection */
/* Data exfiltration or C2 via DNS TXT/NULL queries */
/* Payload encoded in subdomain: c29tZWRhdGE.evil.com */

/* DNS tunnelling signals: */
/* - Long FQDN (>50 chars including subdomain) */
/* - High-entropy subdomain (base32/hex encoded data) */
/* - TXT/NULL query types (not just A/AAAA) */
/* - High query rate to the same parent domain */
/* - DNS responses contain large TXT records */
/* - Asymmetric traffic: many queries, large responses */

void detect_dns_tunnel(dns_info_t *di, dns_tracker_t *t) {
    float label_h = shannon_entropy(di->subdomain, strlen(di->subdomain));

    /* Score this query */
    int score = 0;
    if (strlen(di->fqdn) > 50)    score += 3;
    if (label_h > 4.0)            score += 3;  /* high entropy label */
    if (di->qtype == DNS_TXT)     score += 2;
    if (di->qtype == DNS_NULL)    score += 3;
    if (t->queries_in_window > 60) score += 2;  /* high rate */

    if (score >= 6)
        alert(DNS_TUNNEL, di, score);
}

/* 3. Fast-flux DNS detection */
/* Botnet hides C2: domain has many A records, all short TTL, all IPs change */
/* Detection: multiple A records returned, TTL < 60s, IPs span many ASNs */

/* 4. DNS over HTTPS (DoH) bypass detection */
/* Clients send DNS queries to port 443 (HTTPS) to bypass DNS monitoring */
/* Detection: block well-known DoH resolvers (1.1.1.1:443/dns-query, 8.8.8.8:443) */
/* Force internal DNS: block outbound DNS except to corporate resolver */
/* Or: use SSL inspection to see DoH queries */</pre></div>
  </div>
</div>
</div>


<div id="t7" class="tab-pane">
<p class="sep">ALERT TUNING — MANAGING FALSE POSITIVES IN PRODUCTION</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🎚️</span><h3>False Positive Management and Rule Tuning</h3><span class="tag tag-blue">TUNING</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* The false positive problem */
/* A well-tuned IPS might have 0.01% false positive rate */
/* At 10 Gbps with 64-byte packets: 19.5 Mpps */
/* 0.01% = 1950 false blocks per second → completely unusable */
/* Tuning is as important as detection capability */

/* Step 1: Profile your traffic before enabling IPS */
/* Run in IDS mode for 2 weeks. Collect EVE JSON. Analyse alerts. */
/* Key question: which rules fire most? Are those FPs or TPs? */

/* Alert classification */
/* TP (True Positive):  Real attack. Alert is correct. */
/* FP (False Positive): Legitimate traffic wrongly alerted. */
/* FN (False Negative): Real attack missed (no alert). */
/* TN (True Negative):  Legitimate traffic, no alert. */

/* Tuning approaches */

1. Threshold tuning:
   /* Rule fires every packet — add threshold to reduce noise */
   alert:threshold:type limit,track by_src,count 1,seconds 300;
   /* Only alert once per source per 5 minutes */

2. Suppress rules for known-good sources:
   suppress gen_id 1, sig_id 2001219, track by_src, ip 10.1.0.0/24;
   /* Suppress SSH brute force rule for internal hosts */

3. Pass rules (whitelist before detect):
   pass tcp $TRUSTED_SCANNERS any -> $HOME_NET any
   /* Vulnerability scanner — don't alert on its port scans */

4. Score-based alerting:
   /* Don't block on single rule match */
   /* Accumulate score across multiple correlated events */
   /* Block only when score > threshold */

typedef struct {
    uint32_t src_ip;
    uint32_t score;          /* accumulated threat score */
    uint64_t reset_time_ns;  /* when to reset score */
    char     events[16][64]; /* last 16 contributing events */
} threat_score_t;

void threat_score_update(threat_score_t *ts, const char *sig, uint32_t weight) {
    ts->score += weight;
    /* Log contributing event */
    snprintf(ts->events[ts->score % 16], 64, "%s", sig);

    if (ts->score >= 100) {
        quarantine_host(ts->src_ip);   /* automatic response */
        ts->score = 0;
    }
}

/* Score weights */
/* JA3 matches known malware:  30 points */
/* DNS query to known-bad domain: 40 points */
/* Port scan (>50 ports/min):  20 points */
/* Connection to C2 IP:         70 points */
/* Lateral movement (SMB spray): 50 points */

/* 5. Exception list maintenance */
/* Keep a structured exception database */
/* Every exception needs: justification, owner, expiry date */
/* Exceptions without expiry become permanent security holes */

/* 6. Rule set management */
/* Emerging Threats Pro rules: ~40,000 rules */
/* Typical production deployment: enable 20% of rules */
/* Categories to always enable: malware, c2, exploit */
/* Categories to carefully evaluate: policy, info, dos */</pre></div>
  </div>
</div>
</div>


<div id="t8" class="tab-pane">

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Suricata IDS/IPS Deployment and Tuning</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Deploy Suricata in IDS mode, then IPS mode. Write custom rules. Tune false positives using real traffic.</p>
    <div class="lab-step"><div class="sn">1</div><div>Install Suricata: <code>sudo apt install suricata</code>. Configure to listen on your network interface in AF_PACKET mode. Enable EVE JSON logging to <code>/var/log/suricata/eve.json</code>. Download Emerging Threats Community rules: <code>sudo suricata-update</code>. Start in IDS mode: <code>sudo suricata -i eth0 --af-packet -D</code>.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Generate test traffic against a local web server: run nikto, sqlmap, and dirb against your test nginx. Monitor <code>tail -f /var/log/suricata/eve.json | jq 'select(.event_type=="alert")'</code>. Count alerts per rule category. Identify which rules fired: are they true positives (the tools triggered them) or false positives?</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Write 3 custom rules: (a) detect SSH login attempts (alert on "Failed password" string in SSH response — use content matching), (b) detect DNS queries for known-DGA-looking domains (use pcre for high-length low-vowel patterns), (c) detect HTTP exfiltration via large POST bodies (alert on Content-Length > 1MB to external). Add them to <code>/etc/suricata/rules/custom.rules</code>. Test each works.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Switch to IPS mode using NFQUEUE: <code>iptables -A FORWARD -j NFQUEUE --queue-num 0</code>. Restart Suricata with <code>-q 0</code>. Set one rule to "drop" instead of "alert". Verify traffic is blocked: <code>curl</code> to the blocked destination should fail. Verify legitimate traffic still flows. Observe latency impact: <code>ping</code> RTT before vs after enabling IPS.</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Tune false positives: run normal office traffic through Suricata for 1 hour. Count FPs. Suppress the top 3 noisy rules for known-good sources. Add threshold to the next 3 highest-volume rules. Document before/after alert volume. Achieve <100 alerts/hour from normal traffic.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Beacon Detection Engine</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a beacon detection engine that can identify Cobalt Strike default beacons in captured traffic, and test it against both real and simulated beacon traffic.</p>
    <div class="lab-step"><div class="sn">1</div><div>Implement the IAT (inter-arrival time) tracking structure from Tab 4. Process a pcap file: for each unique (src_ip, dst_ip, dst_port) tuple, record TCP SYN timestamps. Compute IAT statistics: mean, stddev, coefficient of variation. Print the top 10 most periodic flows.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Simulate a Cobalt Strike beacon: write a Python script that sends an HTTP GET to a local server every 60 seconds with 20% random jitter. Also send random non-beacon HTTP requests at variable intervals. Run your detector on the captured traffic. Does it correctly identify the periodic flow and ignore the random ones?</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Test against a free Cobalt Strike beacon pcap from a public malware pcap repository (e.g., malware-traffic-analysis.net). Extract connection timing. Does your detector identify the beacon? What is the minimum number of observations needed for reliable detection? Test with 5, 10, 20 observations.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Add evasion testing: modify the simulated beacon to use random sleep times (exponential distribution with same mean) instead of fixed interval with jitter. Does your detector still trigger? What statistical test (Kolmogorov-Smirnov, runs test) would better distinguish exponential-random from uniform-with-jitter? Implement one and compare.</div></div>
  </div>
</div>

<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Threat Intelligence Pipeline</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build an automated threat intel ingestion pipeline. Ingest IoCs from multiple feeds, deduplicate, and integrate with your session table for real-time checking.</p>
    <div class="lab-step"><div class="sn">1</div><div>Download and parse the Feodo Tracker C2 blocklist (abuse.ch). Parse the CSV format (IP, port, malware family, first/last seen). Load into an in-memory hash table. Measure: how many entries? What's the lookup latency? How often should it be refreshed (check feed update frequency)?</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Add domain-based IoC from URLhaus. Build a trie (or use a sorted array with binary search) for domain matching that handles: exact match ("evil.com"), subdomain wildcard match ("*.evil.com"), and TLD wildcard ("evil.*"). Test with 10K domains and 100K lookups.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Implement live feed update with zero downtime: build the new table in a background thread while the foreground thread continues using the old table. Use an atomic pointer swap to cut over. Verify: during the update cycle, no lookups fail. Measure update latency (time from feed download to active in production).</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Integrate with your M23 session table: in the session creation path, check the destination IP and port against your threat intel database. If found: log a detailed alert including threat type, malware family, and confidence score. If confidence > 80: set session action to BLOCK. Test by creating a session to a known-bad IP and verifying it's blocked.</div></div>
  </div>
</div>
</div>


<div id="t9" class="tab-pane">
<p class="sep">M25 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know IDS vs IPS: IDS passive/alert-only; IPS inline/can-block; false positives have different consequences (annoying vs disruptive)</li>
  <li>Know 4 detection methods: signature (known threats), anomaly (statistical deviation), heuristic/behavioural (patterns over time), threat intel/IoC (known-bad indicators)</li>
  <li>Know Snort/Suricata rule structure: action proto src_ip src_port direction dst_ip dst_port (options)</li>
  <li>Know content matching options: content, nocase, distance/within, pcre; hex bytes with pipes</li>
  <li>Know flow options: established,to_server; established,to_client; stateless</li>
  <li>Know HTTP-specific keywords: http.method, http.uri, http.host, http.user_agent, http.stat_code</li>
  <li>Know TLS keywords: tls.sni, tls.subject, tls.issuerdn, ja3_hash, ja3s_hash</li>
  <li>Know threshold options: type limit/both/threshold; track by_src/by_dst; count; seconds</li>
  <li>Know Suricata thread model: RX threads → worker threads (decode+detect) → output threads</li>
  <li>Know Suricata output modes: EVE JSON, Unified2; key EVE fields: flow_id, alert section, app_proto</li>
  <li>Know Suricata IPS modes: NFQUEUE (verdict-based), AF_PACKET IPS with copy-mode (bypass)</li>
  <li>Know port scan detection: count unique dst_ports per src_ip per window; alert when > threshold</li>
  <li>Know DNS anomaly signals: high query rate, high label entropy, TXT/NULL queries, long FQDNs</li>
  <li>Know Shannon entropy formula and typical values: random data ~8 bits/byte, English text ~4, base32 ~4.7</li>
  <li>Know DGA detection features: SLD length, vowel ratio, entropy, digit ratio, NXDOMAIN sequences</li>
  <li>Know beacon detection: IAT (inter-arrival time) statistics; coefficient of variation; CV < 0.3 = likely beacon</li>
  <li>Know Cobalt Strike default beacon period (60s) and jitter (30%) and resulting CV (~0.17)</li>
  <li>Know Malleable C2 profiles: beacons mimic legitimate browser traffic; JA3 + certificate + timing still detects</li>
  <li>Know IoC types: IP, domain, URL, file hash, JA3 hash, certificate fingerprint, User-Agent</li>
  <li>Know threat intel sources: Feodo Tracker, URLhaus, Emerging Threats, MISP, AlienVault OTX</li>
  <li>Know live feed update architecture: double-buffered tables, atomic pointer swap, grace period</li>
  <li>Know DNS tunnelling signals: long FQDNs, high-entropy subdomains, TXT/NULL types, high rate to same parent</li>
  <li>Know DoH bypass and countermeasures: block known DoH resolvers, force internal DNS, SSL inspection</li>
  <li>Know alert tuning approaches: threshold rules, suppress by source, pass rules for trusted hosts, score-based blocking</li>
  <li>Know false positive rate math: even 0.01% FP rate is catastrophic at NGFW line rates</li>
  <li>Know score-based blocking: accumulate points from multiple signals before taking action; prevents single-rule overblocking</li>
  <li>Completed Lab 1: Suricata IDS+IPS deployment; custom rules; false positive tuning to <100 alerts/hour</li>
  <li>Completed Lab 2: beacon detector with IAT statistics; tested against simulated and real Cobalt Strike traffic</li>
  <li>Completed Lab 3: multi-feed threat intel pipeline with live update and session table integration</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M26 - Policy Engine and Capstone</strong> — the final module bringing together all Phase 6 subsystems into a complete NGFW architecture, plus a capstone project designing your team's NGFW.</p>
</div>
</div>

<div class="mod-nav">
  <a href="/learning/networking-mastery/m24-dpi/">← M24 DPI</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m26-policy-capstone/">Next: M26 - Capstone →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
