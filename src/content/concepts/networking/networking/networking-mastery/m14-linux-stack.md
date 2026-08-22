---
title: "M14 - Linux Network Stack"
description: "NETWORKING MASTERY · PHASE 4 · MODULE 14 · WEEK 12 🐧 Linux Network Stack sk buff · NIC RX/TX path · Netfilter/iptables · Namespaces · tc qdisc · RSS and XPS · Kernel bypass…"
domain: networking
track: networking-mastery
order: 14
ownHeader: true
url: /learning/networking-mastery/m14-linux-stack/
---

<style>
.mod-header{background:linear-gradient(135deg,#0a1628 0%,#1a2a1c 40%,#2a4a1c 70%,#1a3a0c 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#a0d870;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#c8f090;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#d8f8a8}
.tab-bar{display:flex;flex-wrap:wrap;background:#0a1628;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}
.tab-btn.active{color:#a0d870;border-bottom-color:#a0d870}
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
.cb{background:#0a1628;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #4a8a20}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#c8f090;white-space:pre}
.cm{color:#507830}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#f0f8e8;border:1.5px solid #4a8a20;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#101e08;border-color:#6aaa30}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#2a5a00}[data-theme=dark] .ins strong{color:#a0d870}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.t-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.t-table th{background:#2a5a00;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.t-table td{padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222);vertical-align:top}
.t-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.t-table code{font-size:.79rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#3a7a00}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1rem 0}
@media(max-width:560px){.two-col{grid-template-columns:1fr}}
.lab-box{border:2px solid #4a8a20;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.lab-hdr{background:#4a8a20;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.lab-hdr .lab-n{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.lab-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.lab-body{padding:1.1rem 1.2rem}
.lab-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.lab-step{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.lab-step:last-of-type{border-bottom:none}
.lab-step .sn{background:#4a8a20;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
.cl{list-style:none;padding:0;margin:.5rem 0}
.cl li{display:flex;align-items:flex-start;gap:.6rem;padding:.45rem .6rem;font-size:.87rem;color:var(--text-color,#222);line-height:1.5;border-bottom:1px solid var(--border-color,#f0f0f0)}
.cl li:last-child{border-bottom:none}
.cl li::before{content:'☐';font-size:1rem;flex-shrink:0;color:#4a8a20;margin-top:-.05rem}
.mod-nav{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem;margin-top:2.5rem;padding-top:1.2rem;border-top:1px solid var(--border-color,#eee)}
.mod-nav a{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem 1rem;border-radius:7px;background:var(--card-bg,#f5f5f5);border:1px solid var(--border-color,#ddd);font-size:.85rem;font-weight:600;color:var(--text-color,#333) !important;text-decoration:none !important;transition:background .15s}
.mod-nav a:hover{background:var(--bg-color,#ebebeb)}
.mod-nav .nb{background:#1a3a5c;color:#fff !important;border-color:#1a3a5c}
.mod-nav .nb:hover{background:#245280}
.sep{font-size:.7rem;font-family:monospace;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--light-text,#888);margin:2rem 0 .8rem;padding-bottom:.35rem;border-bottom:1px solid var(--border-color,#eee)}
</style>
<div class="mod-header">
  <div class="mod-eyebrow">NETWORKING MASTERY · PHASE 4 · MODULE 14 · WEEK 12</div>
  <div class="mod-title">🐧 Linux Network Stack</div>
  <div class="mod-subtitle">sk_buff · NIC RX/TX path · Netfilter/iptables · Namespaces · tc qdisc · RSS and XPS · Kernel bypass concepts</div>
  <div class="mod-pills">
<span class="mod-pill">Advanced</span>
<span class="mod-pill">Prerequisite: M05 TCP, M10 Routing</span>
<span class="mod-pill">Kernel 5.x+</span>
<span class="mod-pill">Essential for DPDK/VPP Context</span>
<span class="mod-pill">3 Labs</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'t0')">Stack Overview</button>
  <button class="tab-btn" onclick="vt(event,'t1')">sk_buff</button>
  <button class="tab-btn" onclick="vt(event,'t2')">RX Path</button>
  <button class="tab-btn" onclick="vt(event,'t3')">TX Path</button>
  <button class="tab-btn" onclick="vt(event,'t4')">Netfilter</button>
  <button class="tab-btn" onclick="vt(event,'t5')">Namespaces</button>
  <button class="tab-btn" onclick="vt(event,'t6')">Traffic Control</button>
  <button class="tab-btn" onclick="vt(event,'t7')">Kernel Bypass</button>
  <button class="tab-btn" onclick="vt(event,'t8')">Labs</button>
  <button class="tab-btn" onclick="vt(event,'t9')">Checklist</button>
</div>
<!-- TAB 0 -->
<div id="t0" class="tab-pane active">
<p class="sep">THE LINUX NETWORK STACK — 5 MILLION LINES OF KERNEL CODE</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🗺️</span><h3>End-to-End Packet Journey Through the Kernel</h3><span class="tag tag-green">OVERVIEW</span></div>
  <div class="cp-body">
<p>When a packet arrives at a Linux machine, it traverses roughly 12 distinct subsystems before reaching a userspace application. Understanding this path is foundational for DPDK/VPP work — the entire value proposition of kernel bypass is eliminating the overhead of these steps.</p>


```sql
/* Inbound packet journey — NIC to application */

1. NIC hardware receives frame, places in RX ring buffer (DMA)
2. NIC raises hardware interrupt (IRQ)
3. NIC driver ISR: disable NIC IRQ, schedule NAPI poll (softirq NET_RX)
4. NAPI poll: driver pulls packets from RX ring → builds sk_buff objects
5. netif_receive_skb(): packet enters kernel network stack
6. Protocol demultiplexing: Ethernet → IP → TCP/UDP
7. Netfilter hooks: PRE_ROUTING → FORWARD/INPUT → POST_ROUTING
8. IP routing: FIB lookup, determine local delivery or forward
9. Transport layer: TCP reassembly / UDP delivery
10. Socket receive buffer: sk_buff copied to socket's sk_rcvbuf
11. Wakeup sleeping process (epoll/select/read)
12. copy_to_user(): kernel→userspace data copy

/* Where cycles are spent (approximate) */
Driver/NAPI:           ~5%   (hardware-accelerated on modern NICs)
sk_buff allocation:    ~15%  (alloc/free + cache misses)
Protocol processing:   ~20%  (IP/TCP checksum, state machine)
Netfilter:             ~25%  (each hook traverses rule list)
Memory copies:         ~35%  (DMA buffer → sk_buff → socket buf → userspace)

/* DPDK bypass eliminates steps 2-12 entirely */
# Packet goes: NIC DMA → hugepage memory → userspace application
# Zero interrupts, zero copies, zero kernel involvement
```


  </div>
</div>
</div>
<!-- TAB 1 -->
<div id="t1" class="tab-pane">
<p class="sep">sk_buff — THE KERNEL'S PACKET ABSTRACTION</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">📦</span><h3>sk_buff Structure</h3><span class="tag tag-blue">sk_buff</span></div>
  <div class="cp-body">
<p>The <code>sk_buff</code> (socket buffer) is the central data structure for all packets in the Linux kernel. Every packet in flight is represented as an sk_buff. Understanding it explains how the kernel avoids copying data as headers are added/removed.</p>


```c
/* sk_buff key fields (simplified from include/linux/skbuff.h) */
struct sk_buff {
    /* Pointers into the data buffer */
    unsigned char   *head;      /* start of allocated buffer */
    unsigned char   *data;      /* start of valid data (moves on push/pull) */
    unsigned char   *tail;      /* end of valid data */
    unsigned char   *end;       /* end of allocated buffer */

    /* len = tail - data = bytes of valid packet data */
    unsigned int     len;
    unsigned int     data_len;  /* bytes in page fragments (non-linear data) */

    /* Protocol info */
    __be16           protocol;  /* ETH_P_IP, ETH_P_IPV6, etc. */
    __u8             pkt_type;  /* PACKET_HOST, BROADCAST, MULTICAST */

    /* Device info */
    struct net_device *dev;     /* ingress/egress network interface */

    /* Checksums */
    __wsum           csum;
    __u8             ip_summed; /* CHECKSUM_NONE/PARTIAL/COMPLETE/UNNECESSARY */

    /* Netfilter connection tracking */
    struct nf_conntrack *nfct;

    /* Transport header pointers */
    union { struct tcphdr *th; struct udphdr *uh; ... } h; /* L4 header */
    union { struct iphdr *iph; struct ipv6hdr *ipv6h; ... } nh; /* L3 */
    union { struct ethhdr *ethernet; unsigned char *raw; } mac; /* L2 */
};

/* Header manipulation — NO data copy required */
skb_push(skb, hdr_len);  /* data -= hdr_len  (add header at front) */
skb_pull(skb, hdr_len);  /* data += hdr_len  (remove header at front) */
skb_put(skb,  data_len); /* tail += data_len (add data at end) */
skb_trim(skb, len);      /* tail = data + len (remove tail data) */
```


<div class="ins"><p>💡 <strong>Why sk_buff is efficient:</strong> When TCP adds a header to a payload, it calls <code>skb_push()</code> which just moves the <code>data</code> pointer backwards — no memcpy. The physical data stays in place. This is possible because the buffer was allocated with headroom specifically for headers. The same principle applies for all layers adding/removing headers as the packet traverses up/down the stack.</p></div>
  </div>
</div>
</div>
<!-- TAB 2 -->
<div id="t2" class="tab-pane">
<p class="sep">RECEIVE PATH — NIC INTERRUPT TO SOCKET BUFFER</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📥</span><h3>NAPI — New API for High-Speed Packet Reception</h3><span class="tag tag-teal">NAPI</span></div>
  <div class="cp-body">
<p>The original interrupt-per-packet model fails at high packet rates — at 10 Gbps with 64-byte packets, you get 14.8 million interrupts per second, consuming 100% CPU just acknowledging interrupts. NAPI (New API) solves this with interrupt coalescing:</p>


```python
/* NAPI receive flow */

Packet arrives → NIC raises IRQ
  ↓
ISR (interrupt context, runs fast):
  napi_schedule(&napi);    /* queue NAPI poll for softirq */
  napi_disable_irq();      /* DISABLE further NIC interrupts */
  ↓
NET_RX softirq (process context, can be deferred):
  driver->poll(napi, budget=64);  /* pull up to 64 packets per poll */
    for each packet in RX ring:
        alloc sk_buff
        DMA: NIC buffer → sk_buff->data
        refill RX ring with new DMA buffer
        netif_receive_skb(skb)  → up the stack
    if ring empty:
        napi_complete();         /* re-enable NIC interrupts */
    if budget exhausted (ring still has packets):
        return budget;           /* reschedule next softirq tick */

/* Interrupt coalescing (ethtool) */
ethtool -C eth0 rx-usecs 50      # coalesce for 50µs before interrupt
ethtool -C eth0 rx-frames 32     # or coalesce 32 frames
ethtool -S eth0 | grep -i drop   # NIC-level drop counters

/* RSS — Receive Side Scaling (multi-queue) */
# Modern NICs have multiple RX queues
# RSS hashes flow 5-tuple → assigns to queue
# Each queue has its own NAPI instance → different CPU core
# Enables true parallel packet processing
ethtool -l eth0          # show number of RX/TX queues
ethtool -L eth0 combined 8  # set 8 combined queues
cat /proc/interrupts | grep eth0  # shows per-queue IRQ counts
```


  </div>
</div>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🔧</span><h3>RX Ring Buffer and DMA</h3><span class="tag tag-green">RX RING</span></div>
  <div class="cp-body">


```python
/* NIC RX ring buffer structure */
The ring buffer is a circular array of DMA descriptors.
Each descriptor contains:
  - Physical address of a pre-allocated sk_buff data buffer
  - Buffer length
  - Status flags (owned by NIC vs owned by CPU)

NIC owns descriptor: fills buffer with incoming packet, sets status=done, raises IRQ
CPU owns descriptor: NAPI pulls packet, allocates new sk_buff, refills descriptor

/* Key: buffers pre-allocated before packet arrives */
# Driver pre-populates ring with empty sk_buffs on startup
# NIC writes directly into these buffers via DMA (zero-copy from NIC perspective)
# AFTER NAPI pulls the packet, driver allocates a NEW sk_buff to refill the slot

/* Tuning the ring buffer size */
ethtool -g eth0                   # show current ring sizes
ethtool -G eth0 rx 4096 tx 4096  # set 4096-entry ring
# Larger ring: fewer drops under burst, more memory used
# Smaller ring: less latency (data sits in ring shorter time)

/* Drop diagnosis */
cat /proc/net/dev                 # interface stats including drops
ip -s link show eth0              # TX/RX errors and drops
ethtool -S eth0 | grep drop       # NIC-level drop counters
ss -s                             # socket-level stats
```


  </div>
</div>
</div>
<!-- TAB 3 -->
<div id="t3" class="tab-pane">
<p class="sep">TRANSMIT PATH — APPLICATION TO WIRE</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">📤</span><h3>TX Path — Socket to NIC</h3><span class="tag tag-purple">TX PATH</span></div>
  <div class="cp-body">


```sql
/* TX path: application write() → NIC */

1. Application: write(fd, data, len)  or  send(fd, data, len, flags)
2. copy_from_user(): data copied from userspace to kernel sk_buff
3. TCP/UDP: segment, add transport header, update sequence numbers
4. IP: add IP header, route lookup (FIB), fragment if needed
5. Netfilter OUTPUT hook
6. IP routing OUTPUT: select egress interface
7. Netfilter POSTROUTING hook
8. Neighbour (ARP) cache lookup for next-hop MAC
9. L2: add Ethernet header (src MAC = interface MAC, dst = next-hop MAC)
10. qdisc (traffic control): enqueue to output queue
11. dev_hard_start_xmit(): hand to driver TX ring
12. NIC DMA: reads from TX ring, sends on wire
13. Interrupt: NIC signals TX complete → free sk_buff

/* XPS — Transmit Packet Steering */
# Like RSS for TX: map CPU cores to TX queues
# Ensures TX and RX of a flow use the same CPU → better cache locality
ls /sys/class/net/eth0/queues/tx-0/xps_cpus  # affinity mask for TX queue 0

/* TSO — TCP Segmentation Offload */
# Application writes large buffer (64KB)
# Without TSO: kernel segments into MTU-sized sk_buffs, adds TCP/IP hdr each
# With TSO: kernel sends one large sk_buff, NIC hardware segments
# Saves CPU: N segments → 1 kernel operation, NIC does N hardware operations
ethtool -K eth0 tso on    # enable TSO
ethtool -K eth0 gso on    # Generic Segmentation Offload (software TSO)
ethtool -K eth0 gro on    # Generic Receive Offload (coalesce on RX)
```


  </div>
</div>
</div>
<!-- TAB 4 -->
<div id="t4" class="tab-pane">
<p class="sep">NETFILTER — KERNEL PACKET FILTERING FRAMEWORK</p>
<div class="cp p-red">
  <div class="cp-hdr"><span class="ico">🔥</span><h3>Netfilter Hooks and iptables</h3><span class="tag tag-red">NETFILTER</span></div>
  <div class="cp-body">
<p>Netfilter is the kernel framework for packet filtering, NAT, and connection tracking. iptables (and the modern nftables) is the userspace tool that configures Netfilter rules. Understanding hook points is essential for firewall development.</p>


```python
/* Netfilter hook points */

Incoming packet:
  NIC → [PREROUTING] → routing decision →
    if local:  [INPUT] → socket
    if forward:[FORWARD] → [POSTROUTING] → NIC

Outgoing packet:
  socket → [OUTPUT] → [POSTROUTING] → NIC

/* Five hook points */
NF_INET_PRE_ROUTING:   After L2 demux, before routing. Used for DNAT.
NF_INET_INPUT:         After routing, for locally-destined packets.
NF_INET_FORWARD:       For packets being forwarded (not local).
NF_INET_OUTPUT:        Locally-generated packets, before routing.
NF_INET_POST_ROUTING:  After routing, before sending. Used for SNAT/masquerade.

/* iptables tables (each hooks into specific netfilter hooks) */
filter:   INPUT, FORWARD, OUTPUT — packet accept/drop decisions
nat:      PREROUTING (DNAT), OUTPUT (DNAT), POSTROUTING (SNAT)
mangle:   all 5 hooks — modify packet headers (TTL, TOS, marks)
raw:      PREROUTING, OUTPUT — bypass conntrack (NOTRACK)
security: INPUT, FORWARD, OUTPUT — SELinux mandatory access control

/* iptables command structure */
iptables -t TABLE -A CHAIN -m match --opt val -j TARGET

/* Common rules */
iptables -A INPUT -p tcp --dport 22 -j ACCEPT           # allow SSH
iptables -A INPUT -m state --state ESTABLISHED -j ACCEPT # stateful accept
iptables -A INPUT -j DROP                               # default deny
iptables -t nat -A POSTROUTING -s 10.0.0.0/8 -j MASQUERADE  # NAT
iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to 10.0.0.5:8080

/* conntrack — connection tracking */
conntrack -L                  # list all tracked connections
conntrack -D -s 192.168.1.5   # delete connections from this source
cat /proc/sys/net/netfilter/nf_conntrack_count    # current count
cat /proc/sys/net/netfilter/nf_conntrack_max      # maximum
# conntrack table full → all new connections dropped (NOTRACK bypass for DoS)

/* nftables — modern replacement for iptables */
nft list ruleset
nft add table inet filter
nft add chain inet filter input  { type filter hook input priority 0\; policy drop\; }
nft add rule inet filter input tcp dport 22 accept
```


  </div>
</div>
</div>
<!-- TAB 5 -->
<div id="t5" class="tab-pane">
<p class="sep">NETWORK NAMESPACES — LINUX NETWORK VIRTUALISATION</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🏗️</span><h3>Network Namespaces</h3><span class="tag tag-teal">NAMESPACES</span></div>
  <div class="cp-body">
<p>Linux network namespaces provide complete network stack isolation: each namespace has its own interfaces, routing table, iptables rules, ARP cache, and socket namespace. This is the foundation of Docker container networking, Kubernetes pod networking, and network function testing.</p>


```bash
/* Network namespace fundamentals */

# Create namespace
ip netns add ns1
ip netns add ns2

# Create a veth pair (virtual ethernet — always come in pairs)
ip link add veth0 type veth peer name veth1

# Move one end into each namespace
ip link set veth0 netns ns1
ip link set veth1 netns ns2

# Configure IPs in each namespace
ip netns exec ns1 ip addr add 10.0.0.1/24 dev veth0
ip netns exec ns1 ip link set veth0 up
ip netns exec ns2 ip addr add 10.0.0.2/24 dev veth1
ip netns exec ns2 ip link set veth1 up

# Test connectivity
ip netns exec ns1 ping 10.0.0.2

# Connect namespace to external network via bridge
ip link add br0 type bridge
ip link set br0 up
ip link add veth-ext type veth peer name veth-br
ip link set veth-br master br0
ip link set veth-ext netns ns1
ip netns exec ns1 ip addr add 192.168.1.10/24 dev veth-ext

# Run a process in a namespace
ip netns exec ns1 bash              # shell in ns1
ip netns exec ns1 tcpdump -i veth0  # capture in ns1

# Inspect
ip netns list
ip netns exec ns1 ip route show
ip netns exec ns1 ip link show

/* Docker uses namespaces internally */
# Each container gets its own netns
# docker inspect container | grep -i pid
# nsenter -t PID -n ip addr  → enter container's netns
```


  </div>
</div>
</div>
<!-- TAB 6 -->
<div id="t6" class="tab-pane">
<p class="sep">TRAFFIC CONTROL — QDISC AND SHAPING</p>
<div class="cp p-amber">
  <div class="cp-hdr"><span class="ico">🚦</span><h3>Linux tc — Traffic Control</h3><span class="tag tag-amber">TC</span></div>
  <div class="cp-body">
<p>Linux tc (traffic control) implements packet scheduling, shaping, and classification on the output path. It is the kernel's QoS subsystem and also serves as the attachment point for eBPF programs. Understanding qdiscs is important for both performance tuning and network emulation (netem).</p>


```bash
/* Qdisc types */
pfifo_fast:   Default. Three-band FIFO based on IP TOS. Fast but simple.
fq_codel:     Fair Queue CoDel. Modern default. Fair per-flow + AQM.
tbf:          Token Bucket Filter. Rate limiting.
htb:          Hierarchical Token Bucket. Traffic shaping with classes.
netem:        Network Emulator. Add delay, loss, reorder, corrupt.
fq:           Fair Queue. Per-flow scheduling. Used with BBR.
cake:         Combined AQM and FQ. Best for home/edge routers.

/* netem — network emulation for testing */
# Add 100ms delay to all outgoing packets on eth0
tc qdisc add dev eth0 root netem delay 100ms

# Add delay + jitter (uniform distribution ±20ms)
tc qdisc add dev eth0 root netem delay 100ms 20ms

# Add 1% random packet loss
tc qdisc add dev eth0 root netem loss 1%

# Add 1% duplication + 0.5% corruption
tc qdisc add dev eth0 root netem duplicate 1% corrupt 0.5%

# Combine: 50ms delay + 10ms jitter + 0.5% loss
tc qdisc replace dev eth0 root netem delay 50ms 10ms loss 0.5%

# Remove
tc qdisc del dev eth0 root

/* HTB — rate limiting / shaping */
# Limit eth0 to 10Mbps
tc qdisc add dev eth0 root handle 1: htb default 10
tc class add dev eth0 parent 1: classid 1:10 htb rate 10mbit

/* View current qdisc */
tc qdisc show dev eth0
tc -s qdisc show dev eth0   # with statistics (packets, drops)
```


  </div>
</div>
</div>
<!-- TAB 7 -->
<div id="t7" class="tab-pane">
<p class="sep">KERNEL BYPASS — WHY AND HOW</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>The Case for Kernel Bypass</h3><span class="tag tag-blue">BYPASS</span></div>
  <div class="cp-body">
<p>The Linux kernel network stack was designed for generality, not for the highest possible forwarding performance. At line rate on a 100G NIC (148 Mpps for 64-byte packets), the overhead of interrupts, sk_buff allocation, netfilter traversal, and multiple memory copies becomes the bottleneck. Kernel bypass eliminates this overhead.</p>


```python
/* Performance comparison */
Linux kernel stack:      ~1-3 Mpps per core (64-byte packets)
DPDK (PMD polling):     ~30-80 Mpps per core
VPP (vector processing): ~30-100 Mpps per core
XDP (eBPF in driver):   ~10-30 Mpps per core (with kernel features)

/* Kernel bypass mechanisms */

1. DPDK (Data Plane Development Kit):
   - PMD (Poll Mode Driver) replaces kernel driver
   - Application polls NIC directly — no interrupts ever
   - Hugepage memory for packet buffers (no TLB misses)
   - Runs in userspace — full application control
   Con: NIC is dedicated to DPDK, kernel cannot use it

2. AF_XDP (eXpress Data Path socket):
   - Kernel feature (5.x+)
   - Selective bypass: some queues to XDP, others to kernel
   - eBPF program in driver decides: XDP socket or kernel
   - Zero-copy between NIC and userspace possible
   - NIC still managed by kernel driver

3. XDP (eXpress Data Path):
   - eBPF program runs at NIC driver level (before sk_buff)
   - Can DROP, PASS, TX, REDIRECT
   - Native XDP: runs in driver ISR (fastest)
   - Generic XDP: runs after sk_buff allocation (slower, any NIC)
   - Use case: fast packet filtering, DDoS mitigation, load balancing

4. io_uring (for sockets):
   - Async I/O interface for socket operations
   - Reduces syscall overhead for high-connection-count servers

/* XDP program example (simplified) */
SEC("xdp")
int xdp_drop_icmp(struct xdp_md *ctx) {
    void *data     = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    struct ethhdr *eth = data;
    if (data + sizeof(*eth) > data_end) return XDP_DROP;
    if (eth->h_proto != htons(ETH_P_IP)) return XDP_PASS;
    struct iphdr *ip = data + sizeof(*eth);
    if (data + sizeof(*eth) + sizeof(*ip) > data_end) return XDP_DROP;
    if (ip->protocol == IPPROTO_ICMP) return XDP_DROP;
    return XDP_PASS;
}
```


  </div>
</div>
</div>
<!-- TAB 8 -->
<div id="t8" class="tab-pane">
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 1</span><h4>sk_buff Tracing and Stack Profiling</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Use kernel tracing tools to observe the packet path in real time.</p>
<div class="lab-step"><div class="sn">1</div><div>Trace packet path with perf: <code>sudo perf stat -e net:net_dev_xmit,net:netif_receive_skb,net:napi_poll ping -c 100 google.com</code>. Count the kernel events fired per ping packet. Calculate overhead per packet in nanoseconds.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Observe conntrack table: <code>watch -n1 'cat /proc/sys/net/netfilter/nf_conntrack_count'</code>. Run a web benchmark (<code>ab -n 10000 http://localhost/</code>) and watch the count grow. Observe TTL-based cleanup afterward.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Tune NAPI: <code>ethtool -C eth0 rx-usecs 0 rx-frames 1</code> (minimum coalescing = one interrupt per packet). Measure latency with <code>ping -i 0.01</code>. Then set <code>rx-usecs 1000</code> (batch). Measure throughput with iperf3. Document the latency vs throughput tradeoff.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Profile with perf top: <code>sudo perf top -e cycles:k</code> while running iperf3. Identify which kernel functions consume most cycles during heavy network load (look for napi_poll, __netif_receive_skb, ip_rcv, tcp_rcv_established).</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 2</span><h4>Network Namespaces — Build a Virtual Network</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Build a 3-namespace virtual network with a bridge router in the middle. Use this topology for all future protocol labs.</p>
<div class="lab-step"><div class="sn">1</div><div>Create namespaces ns-client, ns-router, ns-server. Create veth pairs: veth-c0/veth-r0 (client↔router) and veth-r1/veth-s0 (router↔server). Move veth-c0 to ns-client, veth-s0 to ns-server, veth-r0 and veth-r1 to ns-router.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Assign IPs: ns-client: 10.1.0.2/24 on veth-c0; ns-router: 10.1.0.1/24 on veth-r0 and 10.2.0.1/24 on veth-r1; ns-server: 10.2.0.2/24 on veth-s0. Enable forwarding in ns-router: <code>ip netns exec ns-router sysctl net.ipv4.ip_forward=1</code>.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Add routes: ns-client default via 10.1.0.1; ns-server default via 10.2.0.1. Test: <code>ip netns exec ns-client ping 10.2.0.2</code>. Capture in ns-router to verify forwarding: <code>ip netns exec ns-router tcpdump -i any icmp</code>.</div></div>
<div class="lab-step"><div class="sn">4</div><div>Add iptables rules in ns-router: allow ESTABLISHED/RELATED, allow ICMP, block TCP 23 (telnet), log dropped packets. Test each rule. This is your personal NGFW testbed — reuse for Phase 5/6 labs.</div></div>
  </div>
</div>
<div class="lab-box">
  <div class="lab-hdr"><span class="lab-n">LAB 3</span><h4>Network Emulation with netem</h4></div>
  <div class="lab-body">
<p><strong>Objective:</strong> Use netem to simulate WAN conditions and measure TCP behaviour under loss and delay.</p>
<div class="lab-step"><div class="sn">1</div><div>In your namespace topology from Lab 2, add 50ms delay to ns-router's veth-r0: <code>ip netns exec ns-router tc qdisc add dev veth-r0 root netem delay 50ms</code>. Run ping and iperf3. Record RTT and throughput.</div></div>
<div class="lab-step"><div class="sn">2</div><div>Add progressive loss: 0%, 0.1%, 0.5%, 1%, 5%. For each, measure TCP throughput with iperf3 (-t 10 -P 4). Plot the results. At what loss rate does TCP throughput degrade significantly? Compare with QUIC if available.</div></div>
<div class="lab-step"><div class="sn">3</div><div>Simulate packet reordering (typical with ECMP): <code>netem delay 50ms 10ms distribution normal reorder 25% 50%</code>. Observe TCP reorder counter: <code>ss -ti | grep reord</code>. Explain why reordering triggers spurious retransmits.</div></div>
  </div>
</div>
</div>
<!-- TAB 9 -->
<div id="t9" class="tab-pane">
<p class="sep">M14 MASTERY CHECKLIST</p>
<ul class="cl">
  <li>Can describe the 12-step packet journey from NIC hardware to userspace application</li>
  <li>Know where cycles are spent: sk_buff alloc (15%), netfilter (25%), copies (35%)</li>
  <li>Know sk_buff key fields: head/data/tail/end pointers, len, dev, protocol, nfct</li>
  <li>Know how skb_push/pull/put/trim avoid data copies by moving pointers only</li>
  <li>Know NAPI: interrupt coalescing, disable-IRQ-then-poll, budget parameter, re-enable on ring empty</li>
  <li>Know why old interrupt-per-packet fails at 10G+: 14.8 Mpps = 14.8M IRQs/s</li>
  <li>Know RSS: multiple RX queues, flow-hash to queue, per-queue NAPI on separate CPU</li>
  <li>Know TSO/GSO/GRO: hardware/software segmentation offloads reduce CPU overhead</li>
  <li>Know the 5 Netfilter hook points: PREROUTING, INPUT, FORWARD, OUTPUT, POSTROUTING</li>
  <li>Know iptables tables and which hooks they attach to: filter, nat, mangle, raw</li>
  <li>Know conntrack: state table for stateful firewall; conntrack full → new connections dropped</li>
  <li>Know nftables as modern replacement for iptables</li>
  <li>Know network namespaces: isolated network stack per namespace; veth pairs to connect</li>
  <li>Know how Docker/Kubernetes use namespaces: each container/pod gets own netns</li>
  <li>Know tc qdisc types: pfifo_fast, fq_codel, htb, netem, tbf</li>
  <li>Know netem for testing: delay, jitter, loss, reorder, corrupt emulation</li>
  <li>Know kernel bypass options: DPDK (poll mode, dedicated NIC), AF_XDP (selective bypass), XDP (eBPF in driver)</li>
  <li>Know performance numbers: kernel stack ~1-3 Mpps/core, DPDK ~30-80 Mpps/core</li>
  <li>Know XDP return codes: XDP_DROP, XDP_PASS, XDP_TX, XDP_REDIRECT</li>
  <li>Completed Lab 1: profiled kernel network path with perf, observed conntrack, tuned NAPI coalescing</li>
  <li>Completed Lab 2: built 3-namespace virtual network with routing and iptables</li>
  <li>Completed Lab 3: emulated WAN conditions with netem, measured TCP under delay and loss</li>
</ul>
<div class="ins" style="margin-top:1.2rem">
  <p>✅ <strong>When complete:</strong> Move to <strong>M15 - Socket Programming</strong> — now that you understand the kernel stack these sockets interact with, the API will make much deeper sense.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/networking-mastery/m13-tunneling/">← M13 Tunneling</a>
  <a href="/learning/networking-mastery/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/networking-mastery/m15-sockets/">Next: M15 - Sockets →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active')}
</script>
