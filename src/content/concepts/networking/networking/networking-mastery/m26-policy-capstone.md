---
title: "M26 - Policy Engine and NGFW Capstone"
description: "NETWORKING MASTERY · PHASE 6 · MODULE 26 · WEEKS 25–26 · CURRICULUM FINAL 🏆 Policy Engine and NGFW Capstone Rule compiler · Policy evaluation pipeline · First-match vs…"
domain: networking
track: networking-mastery
order: 26
ownHeader: true
url: /learning/networking-mastery/m26-policy-capstone/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#102040 25%,#1a3060 50%,#0a4070 75%,#052850 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#80c8ff;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#c0e8ff;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#e0f4ff}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#80c8ff;border-bottom-color:#80c8ff}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1a5090}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#c0e8ff;white-space:pre}
.cm{color:#406880}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#eaf4ff;border:1.5px solid #1a5090;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#081828;border-color:#2a70b0}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#0a3060}[data-theme=dark] .ins strong{color:#80c8ff}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#0a3060;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a5090}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #1a5090;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#1a5090;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.45rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.6}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#1a5090;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.48rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.55;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#1a5090;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
.curriculum-complete{background:linear-gradient(135deg,#0a2040,#103060,#1a5090);border-radius:12px;padding:1.8rem 2rem;margin:2rem 0;border:2px solid #3a80c0;color:#fff;text-align:center}
.curriculum-complete h2{margin:0 0 .6rem;font-size:1.4rem;font-weight:800;color:#fff;border:none}
.curriculum-complete p{margin:.4rem 0;font-size:.92rem;line-height:1.7;color:#c0e8ff}
.curriculum-complete .stats{display:flex;justify-content:center;gap:2rem;margin:1rem 0;flex-wrap:wrap}
.curriculum-complete .stat{text-align:center}
.curriculum-complete .stat .n{font-size:2rem;font-weight:800;color:#80d8ff;display:block}
.curriculum-complete .stat .l{font-size:.75rem;color:#a0c8e8;font-family:monospace;text-transform:uppercase;letter-spacing:.08em}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 6 · MODULE 26 · WEEKS 25–26 · CURRICULUM FINAL</div>
  <div class="mod-title">🏆 Policy Engine and NGFW Capstone</div>
  <div class="mod-subtitle">Rule compiler · Policy evaluation pipeline · First-match vs best-match · Zone-based policy · Logging and SIEM integration · Complete NGFW architecture · Capstone project</div>
  <div class="mod-pills">
    <span class="mod-pill">Advanced</span>
    <span class="mod-pill">Prerequisite: M23–M25</span>
    <span class="mod-pill">Curriculum Final Module</span>
    <span class="mod-pill">Capstone Project</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">Policy Engine Design</button>
  <button class="tab-btn" onclick="vt(event,'t1')">Rule Compilation</button>
  <button class="tab-btn" onclick="vt(event,'t2')">Policy Evaluation</button>
  <button class="tab-btn" onclick="vt(event,'t3')">Zone-Based Policy</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Logging and SIEM</button>
  <button class="tab-btn" onclick="vt(event,'t5')">Complete NGFW Architecture</button>
  <button class="tab-btn" onclick="vt(event,'t6')">Performance Benchmarking</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Capstone Project</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Checklist</button>
</div>
<div id="t0" class="tab-pane active">
<p class="sep">POLICY ENGINE — THE BRAIN OF THE NGFW</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏛️</span><h3>What a Policy Engine Does</h3><span class="tag tag-blue">OVERVIEW</span></div>
  <div class="cp-body">
    <p>The policy engine translates human-readable security rules into machine-executable lookup structures that can classify millions of packets per second. It is the authoritative decision-maker for every packet: permit, deny, inspect, rate-limit, NAT, or log.</p>
    <p>Policy engines face a fundamental tension: rules are specified in human terms (zones, users, applications, threat levels) that are rich and overlapping, but packet processing requires O(1) or O(log n) decisions per packet. The policy compiler's job is to resolve this tension by pre-computing decision structures at rule-load time, not at packet-time.</p>
    <div class="two-col">
      <div>
        <h4>Policy Inputs (Rule Fields)</h4>
        <ul>
          <li>Source zone / interface</li>
          <li>Destination zone / interface</li>
          <li>Source IP / prefix / address-object</li>
          <li>Destination IP / prefix / address-object</li>
          <li>Application (app_id from DPI)</li>
          <li>Service (port, protocol)</li>
          <li>User / user-group (from AD/LDAP)</li>
          <li>URL category (from URL filter DB)</li>
          <li>Threat level (from IPS score)</li>
          <li>Time-of-day / schedule</li>
        </ul>
      </div>
      <div>
        <h4>Policy Actions</h4>
        <ul>
          <li><strong>permit</strong> — forward without further inspection</li>
          <li><strong>deny</strong> — drop packet (silent)</li>
          <li><strong>reject</strong> — drop + send TCP RST or ICMP unreachable</li>
          <li><strong>inspect</strong> — continue to IPS + DLP engine</li>
          <li><strong>ssl-decrypt</strong> — force TLS inspection</li>
          <li><strong>nat</strong> — apply NAT rule</li>
          <li><strong>rate-limit</strong> — traffic shaping</li>
          <li><strong>log</strong> — record to SIEM</li>
          <li><strong>quarantine</strong> — redirect to captive portal</li>
        </ul>
      </div>
    </div>
  </div>
</div>
</div>
<div id="t1" class="tab-pane">
<p class="sep">RULE COMPILATION — FROM HUMAN RULES TO FAST LOOKUP STRUCTURES</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">⚙️</span><h3>Rule Compiler Architecture</h3><span class="tag tag-purple">COMPILATION</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Human-readable policy rule example */
Rule 47:
  from-zone: trust
  to-zone:   untrust
  source:    HR-Group-Subnet (10.10.50.0/24)
  dest:      any
  app:       social-media (facebook, instagram, twitter, tiktok)
  time:      work-hours (Mon-Fri 08:00-18:00)
  action:    deny
  log:       yes
 
/* Challenge: at packet time, we only have a five-tuple + app_id */
/* We need to evaluate 10K+ rules in nanoseconds */
/* Solution: compile rules into optimised lookup structures */
 
/* Step 1: Decompose rules into primitive match fields */
typedef struct compiled_rule {
    /* IP prefix ranges (compiled from address objects) */
    uint32_t src_ip_lo, src_ip_hi;
    uint32_t dst_ip_lo, dst_ip_hi;
    /* Port ranges */
    uint16_t src_port_lo, src_port_hi;
    uint16_t dst_port_lo, dst_port_hi;
    /* Protocol bitmap */
    uint32_t proto_mask;         /* bit per protocol number */
    /* Zone IDs */
    uint16_t src_zone_id;
    uint16_t dst_zone_id;
    /* App IDs (up to 32 apps per rule) */
    uint32_t app_id_bitmap[4];   /* 128 app IDs as bitmap */
    /* Action */
    uint8_t  action;
    uint8_t  log;
    uint8_t  ssl_inspect;
    uint8_t  ips_profile;
    /* Rule metadata */
    uint32_t rule_id;
    uint32_t hit_count;
    uint64_t last_hit_ns;
} compiled_rule_t;
 
/* Step 2: Build classifier structures */
 
/* For IP-range matching: interval tree or PATRICIA trie */
/* For most rules: two-level hash (zone pair → rule subset) */
 
typedef struct policy_table {
    /* Index 1: zone pair (src_zone × dst_zone) → rule_list */
    /* Typical: 10 zones → 100 zone pairs → small list per pair */
    rule_list_t zone_rules[MAX_ZONES][MAX_ZONES];
 
    /* For each zone pair: sorted by specificity for first-match */
    /* More specific rules listed first: /32 before /24 before /0 */
 
    /* Index 2: 5-tuple prefix hash for most common rules */
    /* Pre-computed: all /32 source + /32 dest combinations → direct action */
    rte_hash_t *exact_match_cache;
 
} policy_table_t;
 
/* Step 3: Fast-path lookup */
uint8_t policy_lookup(policy_table_t *pt, session_t *s) {
    /* Fast path: exact match cache (pre-populated for common flows) */
    uint8_t action;
    if (rte_hash_lookup_data(pt->exact_match_cache,
                              &s->key, (void **)&action) >= 0)
        return action;
 
    /* Slow path: walk rule list for this zone pair */
    rule_list_t *rl = &pt->zone_rules[s->src_zone][s->dst_zone];
    for (int i = 0; i < rl->n_rules; i++) {
        compiled_rule_t *r = &rl->rules[i];
        if (rule_matches(r, s)) {
            /* Add to exact match cache to speed up future identical flows */
            rte_hash_add_key_data(pt->exact_match_cache, &s->key,
                                  (void *)(uintptr_t)r->action);
            r->hit_count++;
            r->last_hit_ns = rte_get_tsc_cycles();
            return r->action;
        }
    }
    return ACTION_DEFAULT_DENY;  /* implicit deny at end of rule list */
}</pre></div>
    <div class="ins"><p>💡 <strong>Rule compilation is triggered by every policy change.</strong> The compilation step can take 100ms–10s depending on rule complexity. During this time, packets continue using the old policy table. The atomic pointer swap (same pattern as threat intel updates) ensures zero-disruption policy updates — critical for carrier-grade NGFWs.</p></div>
  </div>
</div>
</div>
<div id="t2" class="tab-pane">
<p class="sep">POLICY EVALUATION — FIRST-MATCH vs BEST-MATCH</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚖️</span><h3>Rule Matching Semantics</h3><span class="tag tag-blue">EVALUATION</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* First-match semantics (most NGFW products, iptables, Snort) */
/* Rules evaluated in order; FIRST matching rule wins */
/* Implication: rule ordering MATTERS CRITICALLY */
/* More specific rules must come BEFORE less specific rules */
 
/* Example — correct ordering (first-match) */
Rule 1: src=10.1.0.5/32   dst=8.8.8.8/32  proto=UDP port=53  → PERMIT
Rule 2: src=10.1.0.5/32   dst=any         proto=any           → DENY (block this host)
Rule 3: src=10.1.0.0/24   dst=any         proto=any           → PERMIT
Rule 99: src=any           dst=any                            → DENY (implicit)
 
/* Packet from 10.1.0.5 → 8.8.8.8:53 → matches Rule 1 → PERMIT */
/* Packet from 10.1.0.5 → 1.2.3.4    → matches Rule 2 → DENY */
/* Packet from 10.1.0.10 → anywhere   → matches Rule 3 → PERMIT */
 
/* If Rule 3 were placed before Rule 2: Rule 2 would never fire! */
 
/* Best-match semantics (BGP routing, some firewall vendors) */
/* Most specific matching rule wins (longest prefix) */
/* Rule ordering does NOT matter */
/* More complex to implement but harder to get wrong */
/* Used by: Juniper SRX (route-based mode), some SDN firewalls */
 
/* Shadow rule detection — compiler-time check */
/* Rule A is "shadowed" by Rule B if: */
/*   Rule B appears before Rule A AND Rule B matches all packets Rule A would match */
/* Shadow = Rule A can never fire (dead code) */
 
int detect_shadow(compiled_rule_t *rules, int n) {
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (rule_covers(rules[j], rules[i])) {
                fprintf(stderr, "Rule %d shadowed by Rule %d\n",
                        rules[i].rule_id, rules[j].rule_id);
                /* In production: warn admin and optionally remove shadow rule */
            }
        }
    }
}
 
/* Rule conflict detection */
/* Rule A and Rule B conflict if: same traffic can match both */
/* but they have different actions */
/* Resolution: first-match resolves automatically, but warn admin */
 
/* Policy diff — show changes between two policy versions */
void policy_diff(policy_table_t *old_pt, policy_table_t *new_pt) {
    /* For each rule in new: present in old? Same action? */
    /* For each rule in old: removed from new? */
    /* Output: added, removed, changed, reordered rules */
    /* Critical for audit trail: every policy change must be logged */
}</pre></div>
  </div>
</div>
</div>
<div id="t3" class="tab-pane">
<p class="sep">ZONE-BASED POLICY — ENTERPRISE SEGMENTATION</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔷</span><h3>Security Zones and Inter-Zone Policy</h3><span class="tag tag-teal">ZONES</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Security zones: logical groups of interfaces/subnets with same trust level */
 
Zone model (typical enterprise NGFW):
  INTERNET  — untrusted external connections (trust=0)
  DMZ       — public-facing servers: web, DNS, SMTP (trust=10)
  TRUST     — internal corporate network (trust=50)
  SERVERS   — internal server segment (trust=60)
  MGMT      — management network: SSH/SNMP to NGFW itself (trust=90)
  VPN       — remote access VPN clients (trust=40)
  GUEST     — guest WiFi (trust=5)
 
/* Default inter-zone policy (implicit) */
Same-zone:   PERMIT (traffic within same zone flows freely)
Cross-zone:  DENY (all inter-zone traffic denied unless explicitly permitted)
/* This is the zero-trust baseline */
 
/* Zone definitions in VPP / iproute2 terms */
typedef struct {
    char     name[32];
    uint8_t  zone_id;
    uint8_t  trust_level;       /* 0=untrusted, 100=fully trusted */
    uint32_t interfaces[16];    /* sw_if_index list */
    uint32_t subnets[16];       /* address ranges in this zone */
    uint8_t  n_interfaces;
    uint8_t  n_subnets;
} security_zone_t;
 
/* Zone determination for a packet */
uint8_t get_src_zone(session_t *s, security_zone_t *zones, int n_zones) {
    /* Check which interface the packet arrived on */
    uint32_t ingress_if = s->ingress_interface;
    for (int z = 0; z < n_zones; z++)
        for (int i = 0; i < zones[z].n_interfaces; i++)
            if (zones[z].interfaces[i] == ingress_if)
                return zones[z].zone_id;
    return ZONE_UNKNOWN;
}
 
/* Standard inter-zone policy matrix */
/*
  FROM/TO   INTERNET  DMZ    TRUST  SERVERS  MGMT   VPN   GUEST
  INTERNET    -       lim    deny   deny     deny   deny  deny
  DMZ         any     -      deny   lim      deny   deny  deny
  TRUST       lim     any    -      any      deny   -     deny
  SERVERS     deny    deny   any    -        deny   deny  deny
  MGMT        deny    deny   deny   deny     -      deny  deny
  VPN         lim     lim    any    lim      deny   -     deny
  GUEST       HTTP/S  deny   deny   deny     deny   deny  -
 
  lim = limited (specific ports only)
*/
 
/* Intra-zone security (lateral movement prevention) */
/* Even within TRUST zone, east-west traffic can be restricted */
/* Micro-segmentation: HR-VLAN cannot reach Finance-VLAN directly */
/* Implementation: sub-zones, or additional per-prefix rules */
 
/* Zone policy for your Jio NGFW project */
/* CUSTOMER-LAN: customer traffic requiring NGFW inspection */
/* CORE: peering/transit links */
/* MGMT: out-of-band management */
/* IDS-COPY: mirrored traffic for Suricata passive inspection */</pre></div>
  </div>
</div>
</div>
<div id="t4" class="tab-pane">
<p class="sep">LOGGING AND SIEM INTEGRATION</p>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">📊</span><h3>Structured Logging at NGFW Scale</h3><span class="tag tag-amber">LOGGING</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Log record schema — one record per session close */
typedef struct ngfw_log_record {
    /* Timestamps */
    uint64_t session_start_ns;
    uint64_t session_end_ns;
    uint32_t duration_ms;
 
    /* Five-tuple */
    char     src_ip[40];         /* text form */
    char     dst_ip[40];
    uint16_t src_port;
    uint16_t dst_port;
    uint8_t  proto;
    char     proto_str[8];       /* "TCP", "UDP", "ICMP" */
 
    /* Policy */
    uint32_t policy_id;
    char     policy_name[64];
    char     src_zone[32];
    char     dst_zone[32];
    char     action[16];         /* "permit", "deny", "reset" */
 
    /* Application */
    uint16_t app_id;
    char     app_name[64];       /* "HTTPS", "Netflix", "BitTorrent" */
    char     url_category[32];   /* "Streaming", "Social Media", etc. */
    char     url[512];           /* if HTTP inspection active */
 
    /* Traffic */
    uint64_t bytes_sent;
    uint64_t bytes_received;
    uint64_t pkts_sent;
    uint64_t pkts_received;
 
    /* Security */
    uint8_t  ssl_inspected;
    char     tls_sni[256];
    char     ja3_hash[33];
    uint16_t threat_id;
    char     threat_name[128];
    uint8_t  threat_severity;    /* 1=critical, 2=high, 3=medium, 4=low */
 
    /* NAT */
    char     nat_src_ip[40];
    uint16_t nat_src_port;
} ngfw_log_record_t;
 
/* High-performance logging architecture */
/* Problem: at 1M flows/second, synchronous write blocks forwarding */
/* Solution: lockless ring buffer → background logger thread */
 
#define LOG_RING_SIZE  (1 << 20)   /* 1M entries */
rte_ring_t *log_ring;
 
/* In forwarding thread (non-blocking) */
void session_close_log(session_t *s) {
    ngfw_log_record_t *rec = log_record_alloc();  /* from pool */
    session_to_log_record(s, rec);
    if (rte_ring_enqueue(log_ring, rec) != 0) {
        /* Ring full → drop log record (or overflow counter++) */
        log_record_free(rec);
    }
}
 
/* In logger thread (background) */
void *logger_thread(void *arg) {
    ngfw_log_record_t *recs[64];
    while (1) {
        int n = rte_ring_dequeue_burst(log_ring, (void **)recs, 64, NULL);
        if (n > 0) {
            /* Format as JSON and write to syslog / Kafka / Elasticsearch */
            for (int i = 0; i < n; i++) {
                char buf[4096];
                record_to_json(recs[i], buf, sizeof(buf));
                syslog_send(buf);          /* or Kafka / HTTP */
                log_record_free(recs[i]);
            }
        } else {
            rte_delay_us(100);  /* no-op if ring empty */
        }
    }
}
 
/* SIEM integration targets */
/* Kafka → Elasticsearch → Kibana (ELK stack): standard for large-scale */
/* Splunk: popular commercial SIEM */
/* Graylog: open-source alternative */
/* syslog-ng / rsyslog: for traditional syslog-based SIEMs */
 
/* CEF (Common Event Format) for interoperability */
/* "CEF:0|Jio|NGFW|1.0|100|Connection Denied|3|src=10.1.0.5 dst=8.8.8.8 ..." */</pre></div>
  </div>
</div>
</div>
<div id="t5" class="tab-pane">
<p class="sep">COMPLETE NGFW ARCHITECTURE — ALL MODULES INTEGRATED</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>Full NGFW Data Plane — Component Integration</h3><span class="tag tag-blue">ARCHITECTURE</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* Complete NGFW packet processing pipeline */
/* Built on VPP (from M18) with all modules integrated */
 
INGRESS PACKET (from NIC via DPDK)
  │
  ▼
[dpdk-input]          DPDK PMD, burst receive, mbuf allocation
  │
  ▼
[ethernet-input]      L2 demux, MAC learning, VLAN stripping
  │
  ▼
[ip4-input]           IP header validation, TTL check, checksum verify
                      IP defragmentation (reassemble before conntrack)
  │
  ▼
[ip4-unicast feature arc] ← VPP feature arc — ordered insertion points
  │
  ├── [ngfw-zone-lookup]          Classify src_zone and dst_zone
  │                               Set vnet_buffer meta: src/dst zone IDs
  │
  ├── [acl-plugin-in-ip4-fa]     Conntrack (M23): session lookup or create
  │                               TCP state machine
  │                               First-packet: evaluate policy (M26)
  │                               Cache: action in session entry
  │
  ├── [ngfw-nat-in2out]           NAT44-ED (M23): DNAT inbound
  │                               Rewrite dst_ip, dst_port, update checksums
  │
  ├── [ngfw-dpi-node]             DPI (M24): protocol dissection
  │                               App identification (app_id → session)
  │                               Hyperscan stream scan
  │
  ├── [ngfw-ips-node]             IPS (M25): Suricata rules inline
  │                               Threat intel IoC check
  │                               Beacon / anomaly scores
  │
  └── [ngfw-ssl-bump-node]        SSL inspection (M22): TLS MITM if required
                                  Generate forged cert, maintain two TLS legs
  │
  ▼
[ip4-lookup]          FIB lookup (M18 VPP FIB): find output interface
  │
  ▼
[ip4-rewrite]         Next-hop MAC rewrite (adjacency)
  │
  ▼
[ip4-output feature arc]
  │
  ├── [ngfw-nat-out2in]           NAT44-ED: SNAT outbound
  │                               Rewrite src_ip, src_port, checksums
  │
  └── [ngfw-log-node]             Session log (background ring buffer)
  │
  ▼
[interface-output]    TX queue, DPDK PMD transmit, batch to NIC
 
/* Control plane (separate from data plane) */
Control Plane Components:
  Policy Manager:      compile and install policy tables
  Threat Intel:        ingest feeds, maintain IoC databases
  Certificate Manager: generate inspection certs, manage CA
  Session Manager:     monitor session table, enforce limits
  Stats Collector:     per-rule hit counts, per-app bytes, per-zone traffic
  SIEM Exporter:       consume log ring, format, forward to Kafka/syslog
  REST API:            policy CRUD, stats queries, operational commands
  CLI:                 vppctl + custom NGFW CLI commands</pre></div>
<div class="cb"><pre>/* Performance targets for production NGFW on 10G dual-port Mellanox */
/* (Based on your team's ConnectX infrastructure) */
 
Throughput:         10 Gbps bidirectional (line rate)
Sessions:           1M concurrent
New sessions/sec:   100K/s (TCP with 3-way handshake)
DPI throughput:     5–8 Gbps (with Hyperscan, 1000 sigs)
SSL inspect:        2–4 Gbps (crypto is the bottleneck)
Latency (add):      <100µs for established flows (DPDK)
Latency (add):      <500µs for new flows (session creation + policy eval)
CPU cores needed:   6–10 worker cores + 2 management cores
Memory:             16GB (1M sessions + DPI state + threat intel)
 
/* VPP worker affinity */
/* Workers 0-3: packet processing (pinned to NUMA 0, same as NIC) */
/* Workers 4-5: SSL inspection offload (CPU-intensive) */
/* Worker 6:   management plane (policy updates, CLI) */
/* Worker 7:   logging + SIEM export */</pre></div>
  </div>
</div>
</div>
<div id="t6" class="tab-pane">
<p class="sep">PERFORMANCE BENCHMARKING — MEASURING NGFW THROUGHPUT</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">📏</span><h3>NGFW Performance Testing Methodology</h3><span class="tag tag-green">BENCHMARKING</span></div>
  <div class="cp-body">
<div class="cb"><pre>/* NGFW performance testing: RFC 2544 + security-specific extensions */
 
/* Tool: TRex (Cisco) — stateful traffic generator running on DPDK */
/* Alternative: Ixia, Spirent (commercial); MoonGen (academic) */
 
/* Test 1: Maximum Throughput (Raw forwarding, no inspection) */
/* Establish baseline: how fast can the data plane forward? */
/* Packet sizes: 64B, 128B, 256B, 512B, 1024B, 1518B */
/* Target: line rate (14.88 Mpps at 10Gbps for 64B packets) */
 
/* Test 2: Connections Per Second */
/* Generate new TCP connections rapidly */
/* Measure: how many SYN→SYN-ACK→ACK→FIN per second */
/* Bottleneck: session table insertion, policy evaluation */
/* Target: 100K+ CPS */
 
/* Test 3: Maximum Concurrent Sessions */
/* Fill session table: open millions of connections, keep alive */
/* Measure: throughput degradation as table fills */
/* Observe: when does hash collision rate become significant? */
 
/* Test 4: DPI Impact */
/* Repeat Test 1 with DPI enabled */
/* Compare throughput with DPI on vs off */
/* Test with: 100 sigs, 1000 sigs, 10000 sigs */
/* Measure: Gbps lost per 1000 additional signatures */
 
/* Test 5: SSL Inspection Throughput */
/* TLS 1.3 connections at various key sizes */
/* Compare: AES-128-GCM vs AES-256-GCM vs ChaCha20-Poly1305 */
/* With hardware offload (QAT or Mellanox IPsec): compare vs software */
 
/* TRex stateful test configuration */
/*
port: 0
  flows:
    - clients: 10.0.0.0/16       # 65K clients
      servers: 200.0.0.0/16      # 65K servers
      transport: tcp
      connections: 100000         # 100K concurrent
      cps: 10000                  # new connections per second
      http:                       # HTTP/1.1 traffic profile
        request_size: 512
        response_size: 4096
*/
 
/* Metrics to capture */
typedef struct perf_metrics {
    double   throughput_gbps;
    uint64_t pps;                /* packets per second */
    uint64_t cps;                /* connections per second */
    double   latency_avg_us;
    double   latency_p99_us;     /* 99th percentile latency */
    double   latency_p999_us;    /* 99.9th percentile */
    uint32_t drop_rate_ppm;      /* drops per million packets */
    uint32_t active_sessions;
    uint32_t session_table_util_pct;
    double   cpu_util_pct;
    double   dpi_scan_gbps;
} perf_metrics_t;
 
/* Monitoring during tests */
watch -n 1 'vppctl show run summary'      /* VPP node performance */
watch -n 1 'vppctl show interface'         /* TX/RX stats */
watch -n 1 'vppctl show nat44 summary'    /* NAT session stats */
perf stat -C 2,3,4,5 sleep 10             /* CPU hardware counters */
numastat -m                                /* NUMA memory access */</pre></div>
  </div>
</div>
</div>
<div id="t7" class="tab-pane">
<p class="sep">CAPSTONE PROJECT — YOUR TEAM'S NGFW</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏆</span><h3>Design Document: Jio NGFW — Capstone Project</h3><span class="tag tag-blue">CAPSTONE</span></div>
  <div class="cp-body">
    <p>Your capstone project is to produce a detailed technical design document for your team's NGFW, incorporating all the knowledge from this curriculum. This document should be usable as the actual technical specification for your R&D work.</p>
    <h4>Capstone Deliverable Structure</h4>
    <ol>
      <li><strong>Executive Summary</strong> — What the NGFW must do; performance targets; technology stack choices and rationale (VPP + DPDK + Mellanox ConnectX)</li>
      <li><strong>Data Plane Architecture</strong> — Complete VPP graph node pipeline diagram; all processing nodes, their order, and inter-node interfaces; how M18 VPP knowledge is applied</li>
      <li><strong>Connection Tracking Design</strong> — Session table implementation: hash table choice, session_t struct fields, timer wheel, per-protocol state machines; sizing for your expected traffic profile</li>
      <li><strong>NAT Implementation</strong> — Which NAT types required; NAPT pool sizing; DNAT rules for published services; hairpinning strategy; VPP NAT44-ED configuration</li>
      <li><strong>DPI Engine</strong> — Pattern matching library choice (Hyperscan); initial signature set; protocol dissectors; app ID signals; per-flow state allocation strategy; memory budget</li>
      <li><strong>Threat Detection</strong> — IPS integration (Suricata vs custom); threat intel feeds; beacon detection; DNS monitoring; alert thresholds and scoring</li>
      <li><strong>Policy Engine</strong> — Zone model (which zones, trust levels); rule schema; compilation strategy; first-match vs best-match decision; shadow rule detection</li>
      <li><strong>SSL Inspection</strong> — Which flows to inspect; CA hierarchy; certificate generation and caching; bypass list; ECH roadmap</li>
      <li><strong>Performance Model</strong> — Expected throughput per subsystem; CPU core allocation; memory budget; NUMA topology; Mellanox offload utilisation (XFRM, checksum, TSO)</li>
      <li><strong>Logging and Observability</strong> — Log schema; ring buffer sizing; SIEM target; operational metrics to expose</li>
    </ol>
<div class="cb"><pre>/* Capstone: suggested technology stack for Jio NGFW */
/*
  Data Plane:        FD.io VPP 23.x on DPDK 23.x
  NIC:               Mellanox ConnectX-6 Dx (100G, IPsec offload)
  OS:                Ubuntu 22.04 LTS with RT kernel patch
  Session Table:     clib_bihash_48_8 (VPP native)
  DPI Engine:        Intel Hyperscan / Vectorscan (open-source)
  IPS Rules:         Emerging Threats + custom Jio-specific rules
  Pattern Matching:  Hyperscan streaming mode (per-flow hs_stream)
  SSL Inspect:       OpenSSL 3.x for cert generation; BoringSSL option
  Threat Intel:      Feodo Tracker + AbuseCH + commercial feed TBD
  Policy:            Custom compiled rule engine in C
  Logging:           Ring buffer → Kafka → Elasticsearch
  API:               REST (gRPC protobuf for performance-sensitive ops)
  CLI:               vppctl + custom NGFW CLI (using vppctl framework)
  Testing:           TRex for traffic generation; Suricata for IDS validation
*/
 
/* Decision: why VPP over custom DPDK */
/* Custom DPDK requires reimplementing: IPv4/IPv6 forwarding, ARP/ND,   */
/* routing, fragmentation, GRE, VxLAN, MPLS, etc. — years of work       */
/* VPP provides all of these plus a plugin framework and graph engine     */
/* Estimated 12–18 months saved vs building raw DPDK pipeline from scratch */
/* VPP performance is within 5% of hand-optimised DPDK for most workloads */</pre></div>
  </div>
</div>
</div>
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Policy Engine with Rule Compiler</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a policy engine that compiles human-readable rules into a fast lookup structure. Implement shadow rule detection and a zone matrix.</p>
    <div class="lab-step"><div class="sn">1</div><div>Define a YAML rule format with fields: id, from-zone, to-zone, src, dst, app, service, time, action, log. Write a parser that reads 50 test rules and produces compiled_rule_t structs. Verify by printing each compiled rule — check that address-objects resolve to IP ranges correctly.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Implement shadow rule detection: for each rule pair (i, j) where i &lt; j, determine if rule i matches a superset of rule j's traffic. Use interval overlap for IP ranges and port ranges. Test with intentional shadowed rules: a /24 rule that blocks a host whose /32 PERMIT comes later.</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Build the zone-pair index: sort all compiled rules into buckets by (src_zone, dst_zone). For each zone pair, sort rules by specificity (/32 &gt; /24 &gt; /16 &gt; /0). Implement <code>policy_lookup()</code> as shown in Tab 1. Benchmark: 100K lookups against a 500-rule policy table. Target &lt;1µs per lookup.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Add the exact-match cache layer: after a slow-path lookup succeeds, cache (five-tuple → action) for fast future lookups. Use a fixed-size LRU cache (hash + doubly-linked list). Benchmark the cache hit rate for realistic traffic: simulate 10K active flows with 1M packets. What cache size gives >95% hit rate?</div></div>
    <div class="lab-step"><div class="sn">5</div><div>Implement zero-downtime policy update: compile the new policy in a background thread, then atomically swap the policy pointer used by the forwarding threads. Test by updating the policy 100 times while traffic flows through. Verify: no packet is processed with an inconsistent partial state; traffic forwarded correctly after each update.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Structured Logging and SIEM Integration</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Build a high-throughput logging pipeline from your NGFW data plane to Elasticsearch. Handle log ring overflow gracefully.</p>
    <div class="lab-step"><div class="sn">1</div><div>Implement the session log record struct and the ring-buffer-based logger from Tab 4. Test the ring buffer: producer writes at 100K records/second; consumer reads at 80K/second. Verify: ring eventually fills; overflow counter increments; producer does not block. Tune ring size so overflow &lt;0.1% at 2× expected rate.</div></div>
    <div class="lab-step"><div class="sn">2</div><div>Write a JSON serialiser for ngfw_log_record_t that produces valid CEF-compatible JSON. Include all fields: timestamps, five-tuple, policy, application, bytes, threat info. Test with jq to verify structure. Benchmark: how many records/second can your serialiser produce? Is it the bottleneck?</div></div>
    <div class="lab-step"><div class="sn">3</div><div>Set up a local Elasticsearch + Kibana stack with Docker. Write log records to Elasticsearch via the HTTP bulk API. Create a Kibana dashboard showing: top source IPs by bytes, top blocked destinations, alert count by severity over time, application distribution pie chart. Use your simulated traffic from earlier labs as input data.</div></div>
    <div class="lab-step"><div class="sn">4</div><div>Implement log filtering: not every session needs a full log entry. Define three log levels: (a) security events (threats, policy denies) — always log, (b) inspection events (SSL inspected, DPI result) — log if enabled per rule, (c) routine flows — log on close only if bytes > 1MB. Verify that log volume reduces by >80% for routine traffic while preserving all security events.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">CAPSTONE</span><h4>End-to-End NGFW Integration Test</h4></div>
  <div class="lab-body">
    <p><strong>Objective:</strong> Wire together all components built across M23–M26 into a single test harness. Verify the complete packet processing pipeline handles all scenarios correctly.</p>
    <div class="lab-step"><div class="sn">1</div><div><strong>Build integration harness:</strong> create a test driver that feeds raw packets into your pipeline (session table → policy engine → DPI → threat intel check → logging) and collects decisions and logs. Use pcap files from previous labs as input. For each packet, record the decision made and verify it matches your expected security policy.</div></div>
    <div class="lab-step"><div class="sn">2</div><div><strong>Scenario: SQL injection attack:</strong> feed HTTP traffic containing SQL injection strings. Verify: (a) conntrack creates session, (b) HTTP dissector parses the request, (c) Hyperscan/AC matches SQL injection signature, (d) session risk_score elevated, (e) policy engine blocks the session, (f) log record created with threat details. End-to-end from raw bytes to blocked session + SIEM alert.</div></div>
    <div class="lab-step"><div class="sn">3</div><div><strong>Scenario: DNS tunnelling:</strong> generate high-entropy DNS queries to a single parent domain at high rate. Verify: (a) DNS dissector extracts FQDN and query type, (b) entropy analyser scores it suspicious, (c) rate counter exceeds threshold, (d) alert generated, (e) subsequent queries from same source optionally blocked. Tune: what threshold minimises false positives for legitimate CDN queries?</div></div>
    <div class="lab-step"><div class="sn">4</div><div><strong>Scenario: NAPT + policy + logging together:</strong> generate HTTP traffic from 100 internal clients through your NAPT. Verify: each client gets a NAT port; policy permits HTTP to external; DPI identifies HTTP; logs show pre-NAT and post-NAT IPs; all 100 clients can access simultaneously without port exhaustion. This is the most common production NGFW configuration.</div></div>
    <div class="lab-step"><div class="sn">5</div><div><strong>Performance baseline:</strong> with all components active (conntrack + NAT + DPI + policy + logging), measure: maximum packets per second through your combined pipeline, latency for first packet of new session vs established session, memory usage with 10K sessions, CPU profile showing time in each component. This is your baseline for the capstone design document.</div></div>
    <div class="lab-step"><div class="sn">6</div><div><strong>Write your capstone design document</strong> following the structure in Tab 7. This should be a real document you can share with your team and use for the actual R&D planning. Include your measured performance numbers from step 5 as the baseline, and project how they scale with hardware (more cores, faster NICs, hardware crypto offload).</div></div>
  </div>
</div>
</div>
<div id="t9" class="tab-pane">
<p class="sep">M26 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know policy engine role: translate human rules into O(1)–O(log n) lookup structures for line-rate packet classification</li>
  <li>Know policy rule fields: src/dst zone, src/dst IP, application, service, user, URL category, time, threat level</li>
  <li>Know policy actions: permit, deny, reject, inspect, ssl-decrypt, nat, rate-limit, log, quarantine</li>
  <li>Know rule compilation steps: parse rules → resolve address objects → build compiled_rule_t → zone-pair index → exact-match cache</li>
  <li>Know first-match semantics: rule ordering critical; specific before general; shadow rules cannot fire</li>
  <li>Know best-match semantics: longest prefix wins regardless of order; harder to implement, harder to get wrong</li>
  <li>Know shadow rule detection: Rule A shadowed if earlier Rule B covers all of A's traffic</li>
  <li>Know zero-downtime policy update: compile in background thread, atomic pointer swap, brief grace period</li>
  <li>Know zone-based policy: security zones group interfaces by trust level; cross-zone traffic denied by default</li>
  <li>Know typical enterprise zones: INTERNET(0), GUEST(5), DMZ(10), VPN(40), TRUST(50), SERVERS(60), MGMT(90)</li>
  <li>Know intra-zone security and micro-segmentation for lateral movement prevention</li>
  <li>Know log record schema: timestamps, five-tuple, policy, application, bytes, NAT info, threat info</li>
  <li>Know ring-buffer logging architecture: forwarding thread enqueues non-blocking; background thread drains and formats</li>
  <li>Know why synchronous logging blocks forwarding: disk/network I/O is orders of magnitude slower than packet forwarding</li>
  <li>Know CEF format: Common Event Format for SIEM interoperability</li>
  <li>Know SIEM integration stack: ring buffer → Kafka → Elasticsearch → Kibana</li>
  <li>Know complete NGFW pipeline: dpdk-input → L2/L3 → conntrack → NAT-in → DPI → IPS → SSL-bump → FIB → rewrite → NAT-out → logging → TX</li>
  <li>Know NGFW performance targets on 10G Mellanox: 10 Gbps forwarding, 100K CPS, 1M sessions, &lt;100µs established flow latency</li>
  <li>Know VPP worker thread affinity model: NIC-local workers for forwarding, separate cores for SSL/logging</li>
  <li>Know RFC 2544 benchmarking: throughput, CPS, max sessions, latency, drop rate</li>
  <li>Know TRex as the standard DPDK-based stateful traffic generator for NGFW testing</li>
  <li>Know capstone document structure: executive summary, data plane architecture, conntrack, NAT, DPI, threat detection, policy, SSL, performance model, logging</li>
  <li>Completed Lab 1: policy engine with rule compiler, shadow detection, zone-pair index, exact-match cache, zero-downtime update</li>
  <li>Completed Lab 2: ring-buffer logging pipeline with Elasticsearch + Kibana dashboard</li>
  <li>Completed Capstone: end-to-end integration test; performance baseline measured; design document written</li>
</ul>
<div class="curriculum-complete">
  <h2>🎓 Networking Mastery Curriculum Complete</h2>
  <div class="stats">
    <div class="stat"><span class="n">26</span><span class="l">Modules</span></div>
    <div class="stat"><span class="n">6</span><span class="l">Phases</span></div>
    <div class="stat"><span class="n">26</span><span class="l">Weeks</span></div>
    <div class="stat"><span class="n">70+</span><span class="l">Labs</span></div>
  </div>
  <p>You have completed the full Networking Mastery curriculum — from OSI fundamentals through to a production NGFW data plane design. The journey covered: TCP/IP foundations, routing protocols, Linux networking, kernel bypass (eBPF, DPDK, VPP), security protocols (TLS, IPsec, PKI), and NGFW development (conntrack, NAT, DPI, IDS/IPS, policy engine).</p>
  <p>Your capstone project is the synthesis: a complete technical design for your team's NGFW that applies every technique from every module. Use it to guide your R&amp;D work. Update it as your team learns. Share it with colleagues joining the project.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/networking-mastery/m25-ids-ips/">← M25 IDS/IPS</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/">🏆 Curriculum Complete</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
