---
layout: learning
title: "VPP P3C - TAP, AF_XDP, vhost-user, AF_PACKET"
permalink: /learning/data-plane/vpp/module-p3-tap-afxdp/
---
<style>
.mod-header{background:linear-gradient(135deg,#0d1b2a 0%,#1e3a1e 60%,#2a8c2a 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#a0e8a0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#c0f0c0;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#d8f8d8}
.tab-bar{display:flex;flex-wrap:wrap;background:#0d1b2a;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}.tab-btn.active{color:#60d890;border-bottom-color:#60d890}
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
.p-green .cp-hdr{background:#e2f0e8}[data-theme=dark] .p-green .cp-hdr{background:#0a2018}
.p-purple .cp-hdr{background:#ede8f5}[data-theme=dark] .p-purple .cp-hdr{background:#1e1028}
.tag-blue{background:#d0e8f8;color:#1a4a7c}.tag-teal{background:#c8e8e4;color:#0e5248}
.tag-orange{background:#fad8c0;color:#8c3a0a}.tag-green{background:#c8e8d4;color:#0e4a28}
.tag-purple{background:#e0d4f4;color:#3a1a6c}
.cb{background:#0d1b2a;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #2a8c2a}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#c8f0c8;white-space:pre}
.cm{color:#4a7a4a}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#e8f5f0;border:1.5px solid #1a7a6e;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2420;border-color:#2a9a8e}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#0e5248}[data-theme=dark] .ins strong{color:#5dd6c8}
.warn{background:#fef6e4;border:1.5px solid #e0a820;border-left:4px solid #c07800;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .warn{background:#2a1e00;border-color:#a07000;border-left-color:#d09000}
.warn p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.cmp-table{width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem}
.cmp-table th{background:#1a3a5c;color:#fff;padding:.55rem .8rem;text-align:left;font-size:.77rem;font-weight:700;font-family:monospace;letter-spacing:.04em}
.cmp-table td{padding:.5rem .8rem;border-bottom:1px solid var(--border-color,#e0e0e0);color:var(--text-color,#222);vertical-align:top;line-height:1.5;font-size:.85rem}
.cmp-table tr:nth-child(even) td{background:var(--bg-color,#f8f8f8)}
.cmp-table code{font-size:.78rem;background:rgba(0,0,0,.06);padding:1px 5px;border-radius:3px;color:#1a7a6e}
.good{color:#1a7a3a;font-weight:600}.bad{color:#8c2020;font-weight:600}.mid{color:#c05e1b;font-weight:600}
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
  <div class="mod-eyebrow">VPP MASTERY · PHASE 3C · WEEKS 11–13</div>
  <div class="mod-title">🐧 TAP · AF_XDP · vhost-user · AF_PACKET</div>
  <div class="mod-subtitle">Linux kernel integration · eBPF bypass · VM connectivity · Full interface comparison matrix</div>
  <div class="mod-pills">
    <span class="mod-pill">src/vnet/devices/tap/</span>
    <span class="mod-pill">src/plugins/af_xdp/</span>
    <span class="mod-pill">src/vnet/devices/virtio/</span>
    <span class="mod-pill">linux-cp plugin</span>
  </div>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'ta')">Comparison Matrix</button>
  <button class="tab-btn" onclick="vt(event,'tb')">TAP v2 &amp; linux-cp</button>
  <button class="tab-btn" onclick="vt(event,'tc')">AF_XDP</button>
  <button class="tab-btn" onclick="vt(event,'td')">vhost-user</button>
  <button class="tab-btn" onclick="vt(event,'te')">AF_PACKET</button>
  <button class="tab-btn" onclick="vt(event,'tf')">Checklist</button>
</div>

<!-- COMPARISON -->
<div id="ta" class="tab-pane active">
<p class="sep">ALL VPP INTERFACE TYPES - SELECTION MATRIX</p>
<table class="cmp-table">
  <thead><tr><th>Property</th><th>DPDK</th><th>memif</th><th>TAP v2</th><th>AF_XDP</th><th>vhost-user</th><th>AF_PACKET</th></tr></thead>
  <tbody>
    <tr><td><strong>Max throughput</strong></td><td><span class="good">Line rate</span></td><td><span class="good">8–12 Mpps</span></td><td><span class="mid">500K–2Mpps</span></td><td><span class="mid">2–8 Mpps</span></td><td><span class="good">5–10 Mpps</span></td><td><span class="bad">&lt;500Kpps</span></td></tr>
    <tr><td><strong>Kernel bypass</strong></td><td><span class="good">Full</span></td><td><span class="good">Full</span></td><td><span class="bad">No</span></td><td><span class="mid">Partial (eBPF)</span></td><td><span class="good">Full</span></td><td><span class="bad">No</span></td></tr>
    <tr><td><strong>Linux stack access</strong></td><td><span class="bad">No</span></td><td><span class="bad">No</span></td><td><span class="good">Yes</span></td><td><span class="good">Yes</span></td><td><span class="bad">VM side only</span></td><td><span class="good">Yes</span></td></tr>
    <tr><td><strong>Zero-copy</strong></td><td><span class="good">Yes</span></td><td><span class="good">Optional</span></td><td><span class="bad">No</span></td><td><span class="good">Yes (UMEM)</span></td><td><span class="mid">Partial</span></td><td><span class="bad">No</span></td></tr>
    <tr><td><strong>VM/QEMU support</strong></td><td><span class="bad">No</span></td><td><span class="bad">No</span></td><td><span class="bad">No</span></td><td><span class="bad">No</span></td><td><span class="good">Yes</span></td><td><span class="bad">No</span></td></tr>
    <tr><td><strong>Setup complexity</strong></td><td><span class="mid">Medium</span></td><td><span class="good">Low</span></td><td><span class="good">Low</span></td><td><span class="mid">Medium</span></td><td><span class="mid">Medium</span></td><td><span class="good">Trivial</span></td></tr>
    <tr><td><strong>Primary use</strong></td><td>Physical NIC</td><td>Container-to-container</td><td>Management plane, Linux integration</td><td>High-perf + kernel visibility</td><td>QEMU/KVM VM</td><td>Dev/test</td></tr>
    <tr><td><strong>VPP source</strong></td><td><code>plugins/dpdk/</code></td><td><code>plugins/memif/</code></td><td><code>vnet/devices/tap/</code></td><td><code>plugins/af_xdp/</code></td><td><code>vnet/devices/virtio/</code></td><td><code>vnet/devices/af_packet/</code></td></tr>
  </tbody>
</table>
<div class="ins">
  <p>💡 <strong>Decision rule for your Docker + Mellanox environment:</strong> Physical traffic → DPDK. Container-to-container fast path → memif. Management/control plane access to Linux → TAP v2 or linux-cp. Testing without hugepages → AF_PACKET. VMs → vhost-user. You want NIC speed + Linux visibility → AF_XDP.</p>
</div>
</div>

<!-- TAP v2 -->
<div id="tb" class="tab-pane">
<p class="sep">TAP v2 AND linux-cp PLUGIN</p>

<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🐧</span><h3>TAP v2 - VPP ↔ Linux Kernel Bridge</h3><span class="tag tag-green">INTERNALS</span></div>
  <div class="cp-body">
    <p>TAP v2 creates a Linux virtual interface visible to the kernel alongside a VPP interface. It uses <strong>virtio vrings</strong> shared between VPP and the kernel's TUN/TAP driver - the same in-kernel virtio used by VMs, re-used for host networking. This gives the Linux kernel full visibility into traffic passing through VPP.</p>
    <p><strong>Primary use cases:</strong></p>
    <ul>
      <li>Management-plane traffic - SSH into a node via VPP-terminated interface</li>
      <li>Running OSPFd/BGPd (e.g., FRRouting) on Linux while VPP handles the data plane</li>
      <li>Control-plane protocols that need the kernel socket API</li>
      <li>Sending packets from a VPP node to a regular Linux process</li>
    </ul>
<div class="cb"><pre><span class="cm"># Create TAP - VPP side gets tapN, Linux side gets vpp0 (or custom name)</span>
create tap id 0 host-if-name vpp0 host-ip4-addr 10.10.0.2/30

<span class="cm"># TAP with custom MAC, MTU, and namespace</span>
create tap id 1 \
  host-if-name vpp-ctrl \
  host-ip4-addr 192.168.1.10/24 \
  host-mac-addr aa:bb:cc:dd:ee:ff \
  host-mtu-size 1500 \
  host-ns myns

<span class="cm"># Bring up VPP side and assign L3</span>
set interface state tap0 up
set interface ip address tap0 10.10.0.1/30

<span class="cm"># Verify both sides</span>
show interface          <span class="cm"># VPP side: tap0 should be up</span>
show tap tap0           <span class="cm"># virtio queue details</span>

<span class="cm"># Linux side (inside the container):</span>
<span class="cm"># ip link show vpp0    - interface should be visible</span>
<span class="cm"># ping 10.10.0.1       - reaches VPP tap0 interface</span></pre></div>
  </div>
</div>

<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">🔗</span><h3>linux-cp Plugin - Mirroring DPDK Interfaces to Linux</h3><span class="tag tag-teal">LINUX-CP</span></div>
  <div class="cp-body">
    <p>The <strong>linux-cp</strong> (Linux Control Plane) plugin (<code>src/plugins/linux-cp/</code>) solves a harder problem: you want DPDK to handle the fast path, but you also want Linux to see the same interfaces for control-plane routing protocols (FRR, Bird). linux-cp mirrors each VPP DPDK interface to a Linux netdev - punting control-plane traffic (ARP, OSPF hellos, BGP) to Linux while VPP handles the forwarding plane.</p>
<div class="cb"><pre><span class="cm"># Enable linux-cp for a DPDK interface</span>
lcp create GigabitEthernet0/8/0 host-if lcp-eth0

<span class="cm"># Linux now sees lcp-eth0 as a real interface</span>
<span class="cm"># Linux side: ip addr add 10.0.0.1/24 dev lcp-eth0</span>
<span class="cm"># FRR OSPF runs on lcp-eth0</span>
<span class="cm"># VPP data plane handles all forwarded traffic at line rate</span>

show lcp              <span class="cm"># list all linux-cp mirrors</span>
lcp default netns myns  <span class="cm"># create mirrors in a specific network namespace</span></pre></div>
    <div class="ins">
      <p>💡 <strong>linux-cp vs TAP v2:</strong> TAP creates a NEW interface that only exists in VPP + Linux. linux-cp creates a Linux mirror of an <em>existing</em> DPDK interface. For a router deployment where you want FRR running alongside VPP on the same physical ports, linux-cp is the right tool. For a container needing management access, TAP is simpler.</p>
    </div>
  </div>
</div>
</div>

<!-- AF_XDP -->
<div id="tc" class="tab-pane">
<p class="sep">AF_XDP - HIGH-PERFORMANCE WITH KERNEL VISIBILITY</p>

<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>AF_XDP Architecture - XSK + UMEM</h3><span class="tag tag-blue">ARCHITECTURE</span></div>
  <div class="cp-body">
    <p>AF_XDP (eXpress Data Path socket) lets a userspace process receive and transmit packets from a NIC queue without full DPDK kernel bypass. An eBPF XDP program in the kernel redirects selected packets from the NIC into a <strong>UMEM</strong> (userspace memory region), from which the AF_XDP socket reads them. The rest of the NIC's traffic continues through the normal kernel path.</p>
    <p>This gives you: kernel-controlled NIC (no VFIO binding, kernel still owns the interface), with near-DPDK performance for the traffic you redirect to userspace.</p>

<div class="cb"><pre><span class="cm">/* AF_XDP components */</span>

NIC → XDP eBPF hook → XDP_REDIRECT → UMEM (shared memory)
                                         ↑
                                    AF_XDP socket (VPP)
                                    reads RX ring
                                    writes TX ring

<span class="cm">/* UMEM: a single large memory region, subdivided into frames */</span>
UMEM frame size = 4096 (one per packet)
Fill ring:    VPP refills with free frame addresses
Completion ring: kernel notifies which TX frames are done
RX ring:      kernel deposits received frame addresses
TX ring:      VPP places frames to transmit</pre></div>

    <p><strong>VPP AF_XDP plugin setup:</strong></p>
<div class="cb"><pre><span class="cm"># Create AF_XDP interface on eth0 (NIC still owned by kernel mlx5_core)</span>
create interface af-xdp host-if eth0 name afxdp0

<span class="cm"># Or in startup.conf for persistent config</span>

<span class="cm"># startup.conf stanza</span>
<span class="cm"># (AF_XDP is configured via CLI/API, not startup.conf)</span>

<span class="cm"># Bring up and configure</span>
set interface state afxdp0 up
set interface ip address afxdp0 10.0.0.1/24

<span class="cm"># Verify</span>
show interface afxdp0
show af-xdp interface</pre></div>

    <table class="cmp-table">
      <thead><tr><th>AF_XDP Mode</th><th>Description</th><th>Performance</th><th>Requirement</th></tr></thead>
      <tbody>
        <tr><td><code>native</code> (XDP_DRV)</td><td>XDP runs in NIC driver, before SKB allocation</td><td><span class="good">Best - near DPDK</span></td><td>Driver must support native XDP (mlx5 does)</td></tr>
        <tr><td><code>generic</code> (XDP_SKB)</td><td>XDP runs after SKB allocation in generic kernel code</td><td><span class="mid">~2× slower than native</span></td><td>Any driver - universal fallback</td></tr>
        <tr><td><code>zero-copy</code></td><td>NIC DMA directly into UMEM - no copy between kernel and userspace</td><td><span class="good">Highest</span></td><td>Driver must support zero-copy XDP (mlx5 on kernel 5.3+)</td></tr>
      </tbody>
    </table>

    <div class="ins">
      <p>💡 <strong>AF_XDP on Mellanox ConnectX-5:</strong> mlx5 supports native XDP and zero-copy XDP on Linux 5.3+. Your AMD + Docker environment should support this - check kernel version with <code>uname -r</code>. With zero-copy mode, AF_XDP throughput approaches DPDK for single-queue workloads while the NIC remains visible to <code>ip link</code> and <code>ethtool</code>.</p>
    </div>
  </div>
</div>
</div>

<!-- VHOST-USER -->
<div id="td" class="tab-pane">
<p class="sep">VHOST-USER - VIRTUAL MACHINE CONNECTIVITY</p>

<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🖥️</span><h3>vhost-user Architecture - VPP ↔ QEMU VM</h3><span class="tag tag-purple">ARCHITECTURE</span></div>
  <div class="cp-body">
    <p>vhost-user is the standard mechanism for connecting a QEMU/KVM virtual machine to VPP at high performance. The VM sees a virtio-net device (standard paravirtualized NIC). The vhost-user protocol moves the virtio vring management from the kernel (<code>vhost-net</code>) into VPP userspace, enabling zero-copy forwarding between VPP and the VM.</p>

<div class="cb"><pre><span class="cm"># ── VPP side: create vhost-user server ──</span>
create vhost-user socket /run/vpp/vm0.sock server

<span class="cm"># The socket is created by VPP (server mode)</span>
<span class="cm"># QEMU connects to it as client</span>

set interface state VirtualEthernet0/0/0 up
set interface ip address VirtualEthernet0/0/0 192.168.100.1/24

<span class="cm"># ── QEMU side: connect VM to VPP ──</span>
qemu-system-x86_64 \
  -m 2G -smp 2 \
  -chardev socket,id=char0,path=/run/vpp/vm0.sock \
  -netdev vhost-user,id=net0,chardev=char0,vhostforce \
  -device virtio-net-pci,netdev=net0,mac=52:54:00:01:02:03 \
  ...

<span class="cm"># Inside the VM: the interface appears as eth0 or ens3</span>
<span class="cm"># Configure with: ip addr add 192.168.100.2/24 dev eth0</span>
<span class="cm"># Ping VPP: ping 192.168.100.1</span>

<span class="cm"># For multi-queue (improves VM throughput significantly)</span>
create vhost-user socket /run/vpp/vm0.sock server \
  rx-queue-size 1024 tx-queue-size 1024

<span class="cm"># QEMU multi-queue requires:</span>
<span class="cm"># -device virtio-net-pci,netdev=net0,mq=on,vectors=10</span>
<span class="cm"># -netdev vhost-user,id=net0,chardev=char0,queues=4</span>

show vhost-user    <span class="cm"># VPP: show all vhost-user interfaces and queue state</span></pre></div>

    <p><strong>Performance optimisation for vhost-user:</strong></p>
    <ul>
      <li>Use <strong>huge pages in the VM</strong> - map VM memory with 2MB pages for fewer TLB misses in VPP's shared memory access</li>
      <li><strong>CPU pinning</strong> - pin QEMU vCPUs to cores that are NUMA-local to the VPP worker thread handling the vhost interface</li>
      <li><strong>Multi-queue</strong> - configure multiple vhost queues (equal to vCPU count) for parallel TX/RX</li>
      <li><strong>Packed virtqueue</strong> - newer QEMU/kernel supports packed vring format, reducing cache traffic vs split-ring. Enable with <code>packed=on</code> in QEMU device args</li>
    </ul>
  </div>
</div>
</div>

<!-- AF_PACKET -->
<div id="te" class="tab-pane">
<p class="sep">AF_PACKET - DEVELOPMENT AND TESTING</p>

<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">🔬</span><h3>AF_PACKET - When You Don't Have Hugepages</h3><span class="tag tag-orange">DEV/TEST</span></div>
  <div class="cp-body">
    <p>AF_PACKET connects VPP to a Linux network interface via the kernel's <code>AF_PACKET</code> socket family (raw socket that receives all frames). It requires no hugepages, no VFIO, no special setup - just a Linux interface name. This makes it invaluable for development in environments where you can't provision hugepages (shared build servers, CI, laptops).</p>
    <p><strong>Performance is low</strong> - each packet crosses the kernel socket boundary. Use only for:</p>
    <ul>
      <li>Functional testing of plugins before deploying to DPDK hardware</li>
      <li>CI/CD pipelines where test performance doesn't matter</li>
      <li>VPP development on a laptop without DPDK-capable NIC</li>
      <li>Quick experiments with VPP's L2/L3 features</li>
    </ul>

<div class="cb"><pre><span class="cm"># Create AF_PACKET interface on Linux interface eth0</span>
create host-interface name eth0

<span class="cm"># Configure and bring up</span>
set interface state host-eth0 up
set interface ip address host-eth0 10.0.0.1/24

show interface host-eth0
show af-packet interfaces

<span class="cm"># Use with veth pairs for container testing without real NICs</span>
<span class="cm"># (run on Linux host, not inside container):</span>
ip link add vpp0 type veth peer name vpp1
ip link set vpp0 up
ip link set vpp1 up
<span class="cm"># VPP: create host-interface name vpp0</span>
<span class="cm"># External process uses vpp1</span></pre></div>

    <div class="warn">
      <p>⚠️ <strong>Do not performance-test with AF_PACKET.</strong> AF_PACKET throughput (~100–500Kpps) is not representative of VPP's real capabilities. All performance benchmarking must use DPDK, memif, or AF_XDP. Use AF_PACKET only to verify functional correctness - that packets are processed correctly, not how fast they're processed.</p>
    </div>
  </div>
</div>
</div>

<!-- CHECKLIST -->
<div id="tf" class="tab-pane">
<p class="sep">P3C COMPLETION CHECKLIST</p>
<ul class="cl">
  <li>Can select the right interface type for a given scenario using the comparison matrix</li>
  <li>Understand TAP v2 internals: virtio vrings shared between VPP and kernel tun/tap driver</li>
  <li>Can create a TAP interface with custom host-if-name, IP, and namespace</li>
  <li>Know the difference between TAP v2 (new interface) and linux-cp (mirror of DPDK interface)</li>
  <li>Know when to use linux-cp: routing daemon (FRR) alongside DPDK-accelerated VPP</li>
  <li>Understand AF_XDP three components: eBPF XDP hook, UMEM, XSK rings</li>
  <li>Know the three AF_XDP modes: native, generic, zero-copy - and which mlx5 supports</li>
  <li>Know AF_XDP's key advantage: NIC stays in kernel while giving near-DPDK speed</li>
  <li>Understand vhost-user architecture: virtio vring moved from kernel to VPP userspace</li>
  <li>Can configure VPP as vhost-user server and write the matching QEMU command line</li>
  <li>Know vhost-user performance tuning: huge pages in VM, CPU pinning, multi-queue, packed vring</li>
  <li>Understand AF_PACKET's role: dev/test only, no hugepages, not for performance measurement</li>
  <li>Completed Project 4 (interface comparison lab from P3A)</li>
</ul>
<div class="ins" style="margin-top:1.2rem;">
  <p>✅ Phase 3 complete. You now know every VPP interface type in depth. Move to <strong>Phase 4 - Plugin Development</strong>, where you build production-quality plugins using everything learned so far.</p>
</div>
</div>

<div class="mod-nav">
  <a href="{{ '/learning/data-plane/vpp/module-p3-memif/' | relative_url }}">← memif</a>
  <a href="{{ '/learning/data-plane/vpp/vpp-roadmap/' | relative_url }}">🗺️ Roadmap</a>
  <a class="nb" href="{{ '/learning/data-plane/vpp/module-p4-plugin-dev/' | relative_url }}">Next: Plugin Dev →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active');}
</script>
