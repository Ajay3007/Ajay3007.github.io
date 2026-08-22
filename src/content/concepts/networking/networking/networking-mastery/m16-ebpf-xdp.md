---
title: "M16 - eBPF and XDP"
description: "NETWORKING MASTERY · PHASE 4 · MODULE 16 · WEEK 14 🔮 eBPF and XDP eBPF virtual machine · BPF maps · Verifier · XDP hook · TC eBPF · AF XDP · bpftool and libbpf Advanced…"
domain: networking
track: networking-mastery
order: 16
ownHeader: true
url: /learning/networking-mastery/m16-ebpf-xdp/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#1a2838 40%,#302060 75%,#1a1040 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#b090f8;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#d0c0f8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#e8d8ff}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#b090f8;border-bottom-color:#b090f8}
.tab-pane{display:none}.tab-pane.active{display:block}
.cp{border-radius:10px;border:1.5px solid var(--border-color,#e4e4e4);background:var(--card-bg,#fff);margin:1.2rem 0;overflow:hidden}
.cp-hdr{padding:.8rem 1.2rem;display:flex;align-items:center;gap:.7rem;border-bottom:1px solid var(--border-color,#eee)}
.cp-hdr .ico{font-size:1.2rem}
.cp-hdr h3{margin:0;font-size:1rem;font-weight:700;border:none;color:var(--text-color,#111)}
.cp-hdr .tag{margin-left:auto;font-size:.68rem;font-family:monospace;padding:2px 8px;border-radius:4px;font-weight:700;letter-spacing:.04em}
.cp-body{padding:1.1rem 1.2rem}
.cp-body p,.cp-body li{font-size:.9rem;line-height:1.7;color:var(--text-color,#222)}
.cp-body ul,.cp-body ol{margin:.4rem 0;padding-left:1.4rem}
.cp-body li{margin-bottom:.3rem}
.cp-body h4{font-size:.9rem;font-weight:700;color:var(--text-color,#111);margin:.9rem 0 .3rem}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #6040c0}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#d0c0f8;white-space:pre}
.cm{color:#705890}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#f0ecff;border:1.5px solid #6040c0;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#180c38;border-color:#8060d8}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#3820a0}[data-theme=dark] .ins strong{color:#b090f8}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#3820a0;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#5030b0}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #6040c0;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#6040c0;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#6040c0;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#6040c0;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 4 · MODULE 16 · WEEK 14</div>
  <div class="mod-title">🔮 eBPF and XDP</div>
  <div class="mod-subtitle">eBPF virtual machine · BPF maps · Verifier · XDP hook · TC eBPF · AF_XDP · bpftool and libbpf</div>
  <div class="mod-pills">
<span class="mod-pill">Advanced</span>
<span class="mod-pill">Prerequisite: M14 Linux Stack</span>
<span class="mod-pill">Kernel 5.x+</span>
<span class="mod-pill">Modern Networking Paradigm</span>
<span class="mod-pill">2 Labs</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">eBPF Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">eBPF Architecture</button>
  <button class="tab-btn" onclick="vt(event,'t2')">BPF Maps</button>
  <button class="tab-btn" onclick="vt(event,'t3')">XDP Programming</button>
  <button class="tab-btn" onclick="vt(event,'t4')">TC eBPF</button>
  <button class="tab-btn" onclick="vt(event,'t5')">AF_XDP</button>
  <button class="tab-btn" onclick="vt(event,'t6')">Tooling</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Checklist</button>
</div>
<!-- TAB 0 -->
<div id="t0" class="tab-pane active">
<p class="sep">eBPF — PROGRAMMABLE KERNEL WITHOUT KERNEL MODULES</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🔮</span><h3>What eBPF Is</h3><span class="tag tag-purple">OVERVIEW</span></div>
  <div class="cp-body">
<p>eBPF (extended Berkeley Packet Filter) is a revolutionary Linux kernel technology that allows you to run sandboxed programs inside the kernel without writing kernel modules or rebooting. eBPF programs are loaded from userspace, verified for safety by the kernel verifier, JIT-compiled to native machine code, and attached to hook points throughout the kernel.</p>
<p><strong>Why eBPF transformed networking:</strong></p>
<ul>
<li><strong>Performance</strong> — XDP eBPF programs run in the NIC driver, before sk_buff allocation. Drop speed: ~100ns per packet vs ~1µs in iptables</li>
<li><strong>Safety</strong> — the verifier proves the program terminates, accesses only valid memory, and doesn't crash the kernel. Safer than kernel modules</li>
<li><strong>Programmability</strong> — change packet processing logic at runtime without kernel recompile or reboot. Deploy new features in seconds</li>
<li><strong>Observability</strong> — instrument any kernel function without overhead of traditional probes; used by tools like bpftrace, Cilium, Falco, Pixie</li>
</ul>
<p><strong>Who uses eBPF in production:</strong> Cloudflare uses XDP to drop DDoS traffic at 100+ Gbps. Facebook uses eBPF for load balancing (Katran). Google uses it for security policy enforcement. Cilium uses eBPF to replace iptables in Kubernetes.</p>
  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📍</span><h3>eBPF Hook Points in the Network Stack</h3><span class="tag tag-blue">HOOKS</span></div>
  <div class="cp-body">
<table class="t-table">
<thead><tr><th>Hook Type</th><th>Location</th><th>Performance</th><th>Capabilities</th></tr></thead>
<tbody>
<tr><td><strong>XDP (Native)</strong></td><td>NIC driver, before sk_buff</td><td>~10-30 Mpps/core</td><td>DROP, PASS, TX, REDIRECT. Modify packet bytes. No sk_buff access.</td></tr>
<tr><td><strong>XDP (Generic)</strong></td><td>After sk_buff allocation</td><td>~5-10 Mpps/core</td><td>Same actions; works on any NIC (no driver support needed)</td></tr>
<tr><td><strong>TC (ingress)</strong></td><td>After sk_buff, before routing</td><td>~5 Mpps/core</td><td>Full sk_buff access, conntrack, modify headers, redirect to other interfaces</td></tr>
<tr><td><strong>TC (egress)</strong></td><td>After routing, before NIC</td><td>~5 Mpps/core</td><td>Modify outgoing packets, traffic shaping, redirect</td></tr>
<tr><td><strong>socket filter</strong></td><td>Socket recv path</td><td>Per-socket</td><td>Filter which packets delivered to socket (classic tcpdump use)</td></tr>
<tr><td><strong>cgroup/sock</strong></td><td>Per-cgroup socket operations</td><td>Per-operation</td><td>Control network access per container/cgroup (Cilium network policy)</td></tr>
<tr><td><strong>kprobe/tracepoint</strong></td><td>Any kernel function</td><td>Observability only</td><td>Read kernel data structures, send to userspace via maps</td></tr>
</tbody>
</table>
  </div>
</div>
</div>
<!-- TAB 1 -->
<div id="t1" class="tab-pane">
<p class="sep">eBPF ARCHITECTURE — VM, VERIFIER, JIT</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>eBPF Virtual Machine</h3><span class="tag tag-blue">ARCHITECTURE</span></div>
  <div class="cp-body">


```python
/* eBPF ISA (Instruction Set Architecture) */
64-bit RISC architecture
11 general-purpose 64-bit registers:
  r0:  return value / function return
  r1-r5: function arguments (calling convention)
  r6-r9: callee-saved (preserved across helper calls)
  r10: read-only frame pointer (stack base)

512 bytes of stack space per eBPF program
Pointer arithmetic allowed but bounds-checked by verifier
No unbounded loops (kernel ≥5.3 allows bounded loops)
Max instruction count: 1 million (kernel ≥5.2)

/* eBPF program lifecycle */

1. Write eBPF program in C with restricted syntax
   (No: user function calls, global vars, unbounded loops)

2. Compile with clang + libbpf:
   clang -O2 -target bpf -c prog.c -o prog.o

3. Load into kernel via bpf() syscall:
   bpf(BPF_PROG_LOAD, &attr, sizeof(attr))

4. Verifier validates:
   - All code paths terminate (DAG, no infinite loops)
   - All memory accesses in bounds
   - Helper function signatures correct
   - Pointer arithmetic safe
   If verification fails: EACCES/EINVAL with verifier log

5. JIT compiler: eBPF bytecode → native x86-64 machine code
   Zero interpretation overhead at runtime

6. Attach to hook point:
   XDP: bpf_set_link_xdp_fd(ifindex, prog_fd, flags)
   TC:  tc filter add dev eth0 ingress bpf obj prog.o

7. Program executes for every packet at hook point
   Returns action code (XDP_DROP, XDP_PASS, etc.)

/* eBPF helper functions */
# eBPF programs cannot call arbitrary kernel functions
# They call only whitelisted "helper functions"
bpf_map_lookup_elem()   # lookup in BPF map
bpf_map_update_elem()   # update BPF map
bpf_redirect()          # redirect packet to another interface
bpf_xdp_adjust_head()   # push/pop bytes at packet head
bpf_ktime_get_ns()      # current timestamp
bpf_trace_printk()      # debug print to /sys/kernel/debug/tracing/trace_pipe
bpf_perf_event_output() # send events to userspace
```


  </div>
</div>
</div>
<!-- TAB 2 -->
<div id="t2" class="tab-pane">
<p class="sep">BPF MAPS — KERNEL-USERSPACE SHARED STATE</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🗺️</span><h3>BPF Map Types</h3><span class="tag tag-teal">MAPS</span></div>
  <div class="cp-body">
<p>BPF maps are the primary mechanism for state sharing: eBPF programs (running in kernel) and userspace applications both access the same map. This enables per-flow counters, blocklists, connection tables, and configuration without stopping the packet processor.</p>


```c
/* BPF map types */
BPF_MAP_TYPE_HASH:       Hash table. Key→value lookup. Most common.
BPF_MAP_TYPE_ARRAY:      Fixed-size indexed array. Access by index.
BPF_MAP_TYPE_LPM_TRIE:  Longest Prefix Match. For IP prefix tables!
BPF_MAP_TYPE_PERCPU_HASH: Per-CPU hash (no lock contention)
BPF_MAP_TYPE_PERF_EVENT_ARRAY: Send events to userspace perf ring
BPF_MAP_TYPE_RINGBUF:    Lock-free ring buffer (kernel 5.8+)
BPF_MAP_TYPE_DEVMAP:     Interface index map for XDP_REDIRECT

/* Defining a map in eBPF C program */
struct {
    __uint(type,        BPF_MAP_TYPE_HASH);
    __uint(max_entries, 1024);
    __type(key,         __u32);     /* src IP */
    __type(value,       __u64);     /* packet count */
} pkt_count SEC(".maps");

/* Using the map in eBPF program */
__u32 src_ip = iph->saddr;
__u64 *count = bpf_map_lookup_elem(&pkt_count, &src_ip);
if (count)
    __sync_fetch_and_add(count, 1);
else {
    __u64 one = 1;
    bpf_map_update_elem(&pkt_count, &src_ip, &one, BPF_ANY);
}

/* Reading map from userspace (libbpf) */
struct bpf_object *obj = bpf_object__open("prog.o");
bpf_object__load(obj);
struct bpf_map *map = bpf_object__find_map_by_name(obj, "pkt_count");
int map_fd = bpf_map__fd(map);

__u32 key = inet_addr("192.168.1.5");
__u64 value;
bpf_map_lookup_elem(map_fd, &key, &value);
printf("Packets from 192.168.1.5: %llu\n", value);

/* BPF LPM trie for IP blocklist */
struct lpm_key {
    __u32 prefixlen;
    __u8  data[4];  /* IPv4 address */
};
/* Insert 192.168.0.0/16 → drop */
struct lpm_key key16 = { .prefixlen = 16, .data = {192, 168, 0, 0} };
__u32 action = XDP_DROP;
bpf_map_update_elem(lpm_fd, &key16, &action, BPF_ANY);
/* Any packet with src in 192.168.0.0/16 matches! */
```


  </div>
</div>
</div>
<!-- TAB 3 -->
<div id="t3" class="tab-pane">
<p class="sep">XDP PROGRAMMING — PACKET PROCESSING AT WIRE SPEED</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>Complete XDP Program — IP Firewall</h3><span class="tag tag-purple">XDP</span></div>
  <div class="cp-body">


```cpp
// xdp_firewall.c — drop packets from blocked IPs using BPF hash map
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_endian.h>

/* Map: blocked source IPs → 1 */
struct {
    __uint(type,        BPF_MAP_TYPE_HASH);
    __uint(max_entries, 65536);
    __type(key,         __u32);  /* IPv4 src addr */
    __type(value,       __u8);   /* 1 = blocked */
} blocklist SEC(".maps");

/* Map: per-IP packet counters */
struct {
    __uint(type,        BPF_MAP_TYPE_PERCPU_HASH);
    __uint(max_entries, 65536);
    __type(key,         __u32);
    __type(value,       __u64);
} pkt_stats SEC(".maps");

SEC("xdp")
int xdp_firewall_prog(struct xdp_md *ctx)
{
    void *data_end = (void *)(long)ctx->data_end;
    void *data     = (void *)(long)ctx->data;

    /* Parse Ethernet header */
    struct ethhdr *eth = data;
    if (data + sizeof(*eth) > data_end)
        return XDP_DROP;  /* malformed — drop */

    /* Only handle IPv4 */
    if (eth->h_proto != bpf_htons(ETH_P_IP))
        return XDP_PASS;

    /* Parse IP header */
    struct iphdr *iph = data + sizeof(*eth);
    if (data + sizeof(*eth) + sizeof(*iph) > data_end)
        return XDP_DROP;

    __u32 src = iph->saddr;

    /* Update per-IP packet counter */
    __u64 *stat = bpf_map_lookup_elem(&pkt_stats, &src);
    if (stat) {
        __sync_fetch_and_add(stat, 1);
    } else {
        __u64 one = 1;
        bpf_map_update_elem(&pkt_stats, &src, &one, BPF_NOEXIST);
    }

    /* Check blocklist */
    __u8 *blocked = bpf_map_lookup_elem(&blocklist, &src);
    if (blocked && *blocked == 1)
        return XDP_DROP;

    return XDP_PASS;
}

char _license[] SEC("license") = "GPL";

/* Compile and load */
// clang -O2 -target bpf -c xdp_firewall.c -o xdp_firewall.o
// ip link set dev eth0 xdp obj xdp_firewall.o sec xdp
// ip link set dev eth0 xdp off  # detach
```


  </div>
</div>
</div>
<!-- TAB 4 -->
<div id="t4" class="tab-pane">
<p class="sep">TC eBPF — FULL STACK ACCESS WITH sk_buff</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🚦</span><h3>TC BPF vs XDP</h3><span class="tag tag-teal">TC BPF</span></div>
  <div class="cp-body">
<p>TC (traffic control) eBPF programs run later in the stack than XDP — after sk_buff allocation. This gives them access to richer metadata: conntrack state, socket information, routing decisions, VLAN tags. They can also generate new packets and redirect to sockets.</p>


```python
/* TC BPF key differences from XDP */

Access to sk_buff → can read:
  - skb->mark, skb->priority (for QoS)
  - skb->sk (associated socket — if known)
  - conntrack state (via helper bpf_skb_get_tunnel_key)
  - Full packet headers (same as XDP) + can modify them
  - Can call bpf_sk_lookup_tcp() to find socket

Return values (different from XDP!):
  TC_ACT_OK (0):       pass to next TC filter/action
  TC_ACT_SHOT (2):     drop packet
  TC_ACT_REDIRECT (7): redirect to another interface or socket
  TC_ACT_STOLEN (4):   take ownership (used for skb→socket delivery)

/* TC BPF for packet marking (QoS) */
SEC("tc")
int mark_voip(struct __sk_buff *skb) {
    void *data_end = (void *)(long)skb->data_end;
    void *data     = (void *)(long)skb->data;
    struct iphdr *iph = data + sizeof(struct ethhdr);
    if ((__u8 *)iph + sizeof(*iph) > (__u8 *)data_end)
        return TC_ACT_OK;
    struct udphdr *udp = (void *)iph + iph->ihl * 4;
    if ((__u8 *)udp + sizeof(*udp) > (__u8 *)data_end)
        return TC_ACT_OK;
    /* Mark SIP (UDP 5060) and RTP (ports 10000-20000) for EF DSCP */
    __u16 dport = bpf_ntohs(udp->dest);
    if (iph->protocol == IPPROTO_UDP &&
        (dport == 5060 || (dport >= 10000 && dport struct ethhdr, h_dest) +
                            sizeof(struct ethhdr) + 1,
                            &(__u8){0xB8}, 1, 0);  /* DSCP EF = 46 
    }
    return TC_ACT_OK;
}

/* Attach TC eBPF */
# tc qdisc add dev eth0 clsact
# tc filter add dev eth0 ingress bpf obj tc_qos.o sec tc direct-action
# tc filter show dev eth0 ingress
```


  </div>
</div>
</div>
<!-- TAB 5 -->
<div id="t5" class="tab-pane">
<p class="sep">AF_XDP — ZERO-COPY USERSPACE PACKET PROCESSING</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>AF_XDP Architecture</h3><span class="tag tag-green">AF_XDP</span></div>
  <div class="cp-body">
<p>AF_XDP is a socket type that allows userspace applications to receive and send packets directly from/to NIC memory with zero kernel copies. Unlike DPDK, AF_XDP keeps the NIC under kernel control — only selected packet queues are redirected to userspace.</p>
<div class="cb"><pre><span class="cm">/* AF_XDP architecture */</span>
 
NIC Queue N → [XDP program runs in driver] → XDP_REDIRECT → AF_XDP socket
NIC Queue 0 → [passes to kernel network stack normally]
 
<span class="cm">/* UMEM — userspace memory region registered with kernel */</span>
void *umem_area = mmap(NULL, UMEM_SIZE, PROT_READ|PROT_WRITE,
                       MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
 
struct xsk_umem *umem;
xsk_umem__create(&umem, umem_area, UMEM_SIZE, &fill_ring, &comp_ring, NULL);
 
<span class="cm">/* Four rings between kernel and userspace */</span>
Fill ring   (userspace → kernel): "here are free buffers you can fill with RX packets"
Completion ring (kernel → userspace): "here are TX buffers I'm done with"
RX ring     (kernel → userspace): "here are received packets"
TX ring     (userspace → kernel): "here are packets to transmit"
 
<span class="cm">/* Receive loop */</span>
<span class="ck">while</span> (1) {
    rcvd = xsk_ring_cons__peek(&sock->rx, BATCH, &idx_rx);
    <span class="ck">for</span> (i = 0; i < rcvd; i++) {
        addr = xsk_ring_cons__rx_desc(&sock->rx, idx_rx + i)->addr;
        len  = xsk_ring_cons__rx_desc(&sock->rx, idx_rx + i)->len;
        pkt  = xsk_umem__get_data(sock->umem->buffer, addr);
        <span class="cm">/* pkt points directly to NIC DMA buffer — zero copy! */</span>
        process_packet(pkt, len);
    }
    xsk_ring_cons__release(&sock->rx, rcvd);
    <span class="cm">/* Refill fill ring so kernel has buffers for next batch */</span>
    replenish_fill_ring(sock, rcvd);
}
 
<span class="cm">/* XDP program to steer traffic to AF_XDP socket */</span>
<span class="ck">struct</span> {
    __uint(type,        BPF_MAP_TYPE_XSKMAP);
    __uint(max_entries, MAX_QUEUES);
    __type(key,         __u32);
    __type(value,       __u32);
} xsks_map SEC(<span class="cs">".maps"</span>);
 
SEC(<span class="cs">"xdp_sock"</span>)
<span class="ck">int</span> xdp_redirect_to_xsk(<span class="ck">struct</span> xdp_md *ctx) {
    __u32 queue = ctx->rx_queue_index;
    <span class="ck">if</span> (bpf_map_lookup_elem(&xsks_map, &queue))
        return bpf_redirect_map(&xsks_map, queue, XDP_PASS);
    return XDP_PASS;
}</pre></div>
  </div>
</div>
</div>
<!-- TAB 6 -->
<div id="t6" class="tab-pane">
<p class="sep">eBPF TOOLING — bpftool, libbpf, bpftrace</p>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>Essential eBPF Tools</h3><span class="tag tag-amber">TOOLING</span></div>
  <div class="cp-body">


```c
/* bpftool — Swiss Army knife for eBPF */

# List all loaded eBPF programs
bpftool prog list
bpftool prog show id 42

# Dump eBPF bytecode (disassemble)
bpftool prog dump xlated id 42

# Show JIT-compiled machine code
bpftool prog dump jited id 42

# List all BPF maps
bpftool map list
bpftool map dump id 7         # dump all entries
bpftool map lookup id 7 key 0x01 0x02 0x03 0x04   # lookup specific key
bpftool map update id 7 key 0x01 0x02 0x03 0x04 value 0x01  # add to blocklist

# Show XDP programs attached to interfaces
bpftool net list
ip link show  # also shows "xdp" flag if XDP is attached

# Perf output from bpf_trace_printk()
cat /sys/kernel/debug/tracing/trace_pipe

/* bpftrace — high-level eBPF tracing language */

# Trace every TCP connection
bpftrace -e 'kprobe:tcp_connect { printf("connect: pid=%d\n", pid); }'

# Count packets by protocol
bpftrace -e 'tracepoint:net:netif_receive_skb { @[args->protocol] = count(); }'

# Track kernel networking function latency
bpftrace -e '
kprobe:ip_rcv { @start[tid] = nsecs; }
kretprobe:ip_rcv /@start[tid]/ {
  @latency = hist(nsecs - @start[tid]);
  delete(@start[tid]);
}'

/* Cilium's eBPF-based Kubernetes networking */
# cilium status — health of eBPF programs
# cilium monitor — real-time packet events
# cilium bpf ct list global — connection tracking table
```


  </div>
</div>
</div>
<!-- TAB 7 -->
<div id="t7" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>Write and Load Your First XDP Program</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Write a functional XDP program that counts packets per source IP and drops packets from a blocklist.</p>
<div class="lab-step"><div class="sn">1</div><div>Install prerequisites: <code>sudo apt install clang llvm libbpf-dev linux-headers-$(uname -r) bpftool</code>. Verify: <code>clang --version</code> (need 10+) and <code>bpftool version</code>.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Write <code>xdp_counter.c</code> with the BPF_MAP_TYPE_PERCPU_HASH for per-IP counters. Implement the XDP program to increment the counter for each source IP. Compile: <code>clang -O2 -target bpf -c xdp_counter.c -o xdp_counter.o</code>.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Attach to a test interface (use veth from M14 Lab 2): <code>sudo ip link set veth0 xdp obj xdp_counter.o sec xdp</code>. Verify attachment: <code>ip link show veth0</code> should show "xdp" flag. Generate traffic (ping) and read counters: <code>sudo bpftool map dump name pkt_count</code>.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Add a blocklist map. Write a userspace control program (C with libbpf) that: opens the loaded BPF object, finds the blocklist map by name, inserts a test IP, verifies pings from that IP are dropped. Use <code>bpftool map update</code> as an alternative.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>bpftrace Network Observability</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Use bpftrace to instrument the kernel network stack without writing eBPF C code.</p>
<div class="lab-step"><div class="sn">1</div><div>Install bpftrace: <code>sudo apt install bpftrace</code>. Run the one-liner to count packets by protocol: <code>sudo bpftrace -e 'tracepoint:net:netif_receive_skb { @[args->skbaddr] = count(); }'</code>. While running, generate traffic and observe the output.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Trace TCP connection lifecycle: <code>sudo bpftrace -e 'kprobe:tcp_connect { printf("pid=%d comm=%s\n", pid, comm); }'</code>. Open several websites in a browser — you should see a connect event for each. Extend to also trace tcp_close.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Measure ip_rcv latency histogram: use the kprobe/kretprobe pattern from Tab 6. Run while doing iperf3. Output the latency histogram. Identify the median and 99th percentile kernel processing time per packet.</div></div>
  </div>
</div>
</div>
<!-- TAB 8 -->
<div id="t8" class="tab-pane">
<p class="sep">M16 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Know what eBPF is: sandboxed kernel programs, loaded from userspace, verified for safety, JIT compiled</li>
  <li>Know eBPF's 3 key properties: safety (verifier), performance (JIT, kernel execution), programmability (runtime updates)</li>
  <li>Know 7 eBPF hook types and their positions: XDP native/generic, TC ingress/egress, socket filter, cgroup/sock, kprobe/tracepoint</li>
  <li>Know eBPF VM: 11 registers (r0=return, r1-r5=args, r10=stack pointer), 512B stack, no unbounded loops</li>
  <li>Know eBPF program lifecycle: C source → clang (target bpf) → verifier → JIT → attach to hook</li>
  <li>Know what the verifier checks: all paths terminate, bounds-checked memory access, helper call validity</li>
  <li>Know eBPF helper functions: bpf_map_lookup/update_elem, bpf_redirect, bpf_xdp_adjust_head, bpf_trace_printk</li>
  <li>Know BPF map types: HASH, ARRAY, LPM_TRIE (IP prefix match!), PERCPU_HASH, PERF_EVENT_ARRAY, RINGBUF</li>
  <li>Know how maps enable kernel-userspace communication: both sides access same map via file descriptor</li>
  <li>Know XDP return codes: XDP_DROP, XDP_PASS, XDP_TX, XDP_REDIRECT</li>
  <li>Know XDP vs TC eBPF: XDP = before sk_buff (faster, less context); TC = has sk_buff (richer context, slower)</li>
  <li>Know TC return codes: TC_ACT_OK, TC_ACT_SHOT, TC_ACT_REDIRECT</li>
  <li>Know AF_XDP: NIC DMA → userspace UMEM (zero copy); 4 rings: fill, completion, RX, TX</li>
  <li>Know AF_XDP vs DPDK: AF_XDP keeps kernel driver control; DPDK takes exclusive NIC ownership</li>
  <li>Know bpftool: list/inspect programs and maps, dump bytecode, update map entries at runtime</li>
  <li>Know bpftrace: high-level tracing language, kprobe/tracepoint access, histogram output</li>
  <li>Completed Lab 1: wrote and loaded XDP packet counter + IP blocklist with libbpf</li>
  <li>Completed Lab 2: used bpftrace to trace TCP connections and measure ip_rcv latency</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M17 - High-Performance Networking with DPDK</strong> — your existing DPDK knowledge plus this eBPF foundation prepares you for the deepest performance engineering content in the curriculum.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/networking-mastery/m15-sockets/">← M15 Sockets</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m17-dpdk/">Next: M17 - DPDK →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
