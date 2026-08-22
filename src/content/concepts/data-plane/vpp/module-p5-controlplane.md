---
title: "VPP P5 - Control Plane and GoVPP"
description: "VPP MASTERY · PHASE 5 · WEEKS 19–22+ 🎛️ Control Plane GoVPP GoVPP binary API client · Stats API · vpp papi · Observability · NUMA tuning · Production patterns…"
domain: data-plane
track: vpp
order: 5
ownHeader: true
url: /learning/data-plane/vpp/module-p5-controlplane/
---

<style>
.mod-header{background:linear-gradient(135deg,#0d1b2a 0%,#1a6b3c 60%,#1e8a4e 100%);border-radius:12px 12px 0 0;padding:1.8rem 2rem 1.4rem;color:#fff;margin-bottom:0}
.mod-eyebrow{font-size:.7rem;font-family:monospace;letter-spacing:.12em;color:#a0f0c0;text-transform:uppercase;margin-bottom:.5rem}
.mod-title{font-size:2rem;font-weight:800;color:#fff;margin:.2rem 0 .6rem;letter-spacing:-.02em;border:none}
.mod-subtitle{color:#c0f4d8;font-size:.95rem;margin-bottom:1rem}
.mod-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}
.mod-pill{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:3px 12px;font-size:.72rem;font-family:monospace;color:#d8fff0}
.tab-bar{display:flex;flex-wrap:wrap;background:#0d1b2a;border-radius:0 0 8px 8px;overflow-x:auto;margin-bottom:2rem}
.tab-btn{padding:.65rem 1.1rem;font-size:.8rem;font-weight:600;font-family:monospace;color:#7ab8d8;background:transparent;border:none;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;transition:color .15s,border-color .15s}
.tab-btn:hover{color:#fff}.tab-btn.active{color:#5dd890;border-bottom-color:#5dd890}
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
.cb{background:#0d1b2a;border-radius:8px;padding:1rem 1.2rem;margin:.8rem 0;overflow-x:auto;border-left:3px solid #1a8a4e}
.cb pre{margin:0;font-family:'Courier New',monospace;font-size:.82rem;line-height:1.65;color:#c0f0d0;white-space:pre}
.cm{color:#4a7a4a}.ck{color:#7ab8d8}.cv{color:#f0c080}.cs{color:#f0a060}
.ins{background:#e8f5f0;border:1.5px solid #1a7a6e;border-radius:8px;padding:.9rem 1.1rem;margin:1rem 0}
[data-theme=dark] .ins{background:#0a2420;border-color:#2a9a8e}
.ins p{margin:0;font-size:.88rem;line-height:1.65;color:var(--text-color,#222)}
.ins strong{color:#0e5248}[data-theme=dark] .ins strong{color:#5dd6c8}
.proj-box{border:2px solid #1a7a6e;border-radius:10px;overflow:hidden;margin:1.5rem 0;background:var(--card-bg,#fff)}
.proj-hdr{background:#1a7a6e;padding:.75rem 1.2rem;display:flex;align-items:center;gap:.8rem}
.proj-hdr .pn{background:rgba(255,255,255,.2);border-radius:6px;padding:2px 10px;font-family:monospace;font-size:.8rem;font-weight:700;color:#fff}
.proj-hdr h4{margin:0;color:#fff;font-size:1rem;font-weight:700}
.proj-body{padding:1.1rem 1.2rem}
.proj-body p{font-size:.88rem;line-height:1.65;color:var(--text-color,#333);margin-bottom:.5rem}
.ps{display:flex;gap:.7rem;align-items:flex-start;padding:.4rem 0;border-bottom:1px dashed var(--border-color,#eee);font-size:.87rem;color:var(--text-color,#333);line-height:1.55}
.ps:last-of-type{border-bottom:none}
.ps .sn{background:#1a7a6e;color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;flex-shrink:0;margin-top:.05rem}
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
  <div class="mod-eyebrow">VPP MASTERY · PHASE 5 · WEEKS 19–22+</div>
  <div class="mod-title">🎛️ Control Plane &amp; GoVPP</div>
  <div class="mod-subtitle">GoVPP binary API client · Stats API · vpp_papi · Observability · NUMA tuning · Production patterns</div>
  <div class="mod-pills">
<span class="mod-pill">github.com/FDio/govpp</span>
<span class="mod-pill">Stats API</span>
<span class="mod-pill">vpp_papi</span>
<span class="mod-pill">Projects 8 &amp; 9</span>
  </div>
</div>
<div class="tab-bar">
  <button class="tab-btn active" onclick="vt(event,'ta')">GoVPP Basics</button>
  <button class="tab-btn" onclick="vt(event,'tb')">GoVPP Advanced</button>
  <button class="tab-btn" onclick="vt(event,'tc')">Stats API</button>
  <button class="tab-btn" onclick="vt(event,'td')">vpp_papi (Python)</button>
  <button class="tab-btn" onclick="vt(event,'te')">Performance Tuning</button>
  <button class="tab-btn" onclick="vt(event,'tf')">Projects</button>
  <button class="tab-btn" onclick="vt(event,'tg')">Checklist</button>
</div>
<!-- GOVPP BASICS -->
<div id="ta" class="tab-pane active">
<p class="sep">GOVPP - GO CLIENT FOR VPP BINARY API</p>
<div class="cp p-green">
  <div class="cp-hdr"><span class="ico">🐹</span><h3>GoVPP Architecture and Setup</h3><span class="tag tag-green">GOVPP</span></div>
  <div class="cp-body">
<p>GoVPP (<code>github.com/FDio/govpp</code>) is the official Go library for VPP's binary API. It connects to VPP via a Unix socket or shared memory, sends request messages, and receives reply/notification messages. GoVPP auto-generates Go structs from VPP's <code>.api.json</code> files - so every VPP API is accessible with full type safety.</p>


```python
// ── go.mod setup ──
// go get go.fd.io/govpp@latest

package main

import (
    "context"
    "fmt"
    "log"

    "go.fd.io/govpp"
    "go.fd.io/govpp/api"
    "go.fd.io/govpp/binapi/interface_types"
    "go.fd.io/govpp/binapi/interfaces"
    "go.fd.io/govpp/binapi/ip"
    "go.fd.io/govpp/binapi/ip_types"
    "go.fd.io/govpp/core"
)

func main() {
    // Connect to VPP binary API socket
    conn, err := govpp.Connect("/run/vpp/api.sock")
    if err != nil {
        log.Fatalf("connect: %v", err)
    }
    defer conn.Disconnect()

    // Open a channel - each goroutine should have its own channel
    ch, err := conn.NewAPIChannel()
    if err != nil {
        log.Fatalf("channel: %v", err)
    }
    defer ch.Close()

    // ── Example 1: Show VPP version ──
    req := &vpe.ShowVersion{}
    reply := &vpe.ShowVersionReply{}
    if err := ch.SendRequest(req).ReceiveReply(reply); err != nil {
        log.Fatalf("ShowVersion: %v", err)
    }
    fmt.Printf("VPP version: %s\n", reply.Version)
}
```


  </div>
</div>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">🔌</span><h3>Interface Operations</h3><span class="tag tag-blue">API PATTERNS</span></div>
  <div class="cp-body">


```yaml
// ── List all interfaces ──
reqCtx := ch.SendMultiRequest(&interfaces.SwInterfaceDump{
    SwIfIndex: interface_types.InterfaceIndex(^uint32(0)), // ~0 = all
})
for {
    details := &interfaces.SwInterfaceDetails{}
    stop, err := reqCtx.ReceiveReply(details)
    if stop { break }
    if err != nil { log.Fatalf("recv: %v", err) }
    fmt.Printf("  [%d] %s  admin:%v link:%v\n",
        details.SwIfIndex,
        details.InterfaceName,
        details.AdminUpDown, details.LinkUpDown)
}

// ── Set interface state up ──
_, err = ch.SendRequest(&interfaces.SwInterfaceSetFlags{
    SwIfIndex: interface_types.InterfaceIndex(swIfIndex),
    Flags:     interface_types.IF_STATUS_API_FLAG_ADMIN_UP,
}).ReceiveReply(&interfaces.SwInterfaceSetFlagsReply{})

// ── Add IPv4 address ──
_, err = ch.SendRequest(&interfaces.SwInterfaceAddDelAddress{
    SwIfIndex: interface_types.InterfaceIndex(swIfIndex),
    IsAdd:     true,
    Prefix: ip_types.AddressWithPrefix{
        Address: ip_types.Address{
            Af: ip_types.ADDRESS_IP4,
            Un: ip_types.AddressUnionIP4(ip_types.IP4Address{10, 0, 0, 1}),
        },
        Len: 24,
    },
}).ReceiveReply(&interfaces.SwInterfaceAddDelAddressReply{})

// ── Add a static route ──
_, err = ch.SendRequest(&ip.IPRouteAddDel{
    IsAdd: true,
    Route: ip.IPRoute{
        TableID: 0,
        Prefix: ip_types.Prefix{
            Address: ip_types.Address{
                Af: ip_types.ADDRESS_IP4,
                Un: ip_types.AddressUnionIP4(ip_types.IP4Address{10, 1, 0, 0}),
            },
            Len: 24,
        },
        Paths: []ip.FibPath{{
            SwIfIndex: interface_types.InterfaceIndex(swIfIndex),
            Proto:     ip.FIB_API_PATH_NH_PROTO_IP4,
            Nh: ip.FibPathNh{
                Address: ip_types.AddressUnionIP4(
                    ip_types.IP4Address{10, 0, 0, 2}),
            },
            Weight:     1,
            Preference: 0,
        }},
    },
}).ReceiveReply(&ip.IPRouteAddDelReply{})
```


  </div>
</div>
</div>
<!-- GOVPP ADVANCED -->
<div id="tb" class="tab-pane">
<p class="sep">GOVPP - NOTIFICATIONS AND CHANNELS</p>
<div class="cp p-teal">
  <div class="cp-hdr"><span class="ico">📨</span><h3>Event Subscriptions and Multi-Channel Patterns</h3><span class="tag tag-teal">ADVANCED</span></div>
  <div class="cp-body">


```yaml
// ── Subscribe to interface state change events ──
notifChan := make(chan api.Message, 100)
sub, err := conn.WatchEvent(context.Background(), (*interfaces.SwInterfaceEvent)(nil))
if err != nil { log.Fatalf("subscribe: %v", err) }

// Enable notifications (VPP won't send events without this)
ch.SendRequest(&interfaces.WantInterfaceEvents{
    EnableDisable: 1,
    PID:           uint32(os.Getpid()),
}).ReceiveReply(&interfaces.WantInterfaceEventsReply{})

// Process events in a goroutine
go func() {
    for {
        msg, ok := // ── Multi-channel pattern: one channel per worker goroutine ──
type VPPWorker struct {
    ch api.Channel
}

func NewWorker(conn api.Connection) (*VPPWorker, error) {
    ch, err := conn.NewAPIChannel()
    if err != nil { return nil, err }
    return &VPPWorker{ch: ch}, nil
}

// Each goroutine has its OWN channel - no sharing, no locking
for i := 0; i // ── Bulk route programming - batch via channel ──
func (w *VPPWorker) programRoutes(routes []Route) error {
    for _, r := range routes {
        req := buildIPRouteAddDel(r)
        reply := &ip.IPRouteAddDelReply{}
        if err := w.ch.SendRequest(req).ReceiveReply(reply); err != nil {
            return err
        }
        if reply.Retval != 0 {
            return fmt.Errorf("route add retval %d", reply.Retval)
        }
    }
    return nil
}
```


  </div>
</div>
</div>
<!-- STATS API -->
<div id="tc" class="tab-pane">
<p class="sep">STATS API - HIGH-FREQUENCY TELEMETRY</p>
<div class="cp p-orange">
  <div class="cp-hdr"><span class="ico">📊</span><h3>VPP Stats Segment - Zero-Copy Telemetry</h3><span class="tag tag-orange">STATS</span></div>
  <div class="cp-body">
<p>The Stats API is VPP's high-performance telemetry interface. It exposes per-node, per-interface, per-worker, and per-error counters via a <strong>shared memory segment</strong> - no IPC, no socket round-trip. A monitoring agent can read millions of counters per second without impacting the VPP dataplane.</p>


```python
// ── GoVPP Stats client ──
import "go.fd.io/govpp/adapter/statsclient"

func monitorVPP() {
    // Connect to stats segment (separate from binary API socket)
    client := statsclient.NewStatsClient("/run/vpp/stats.sock")
    if err := client.Connect(); err != nil {
        log.Fatalf("stats connect: %v", err)
    }
    defer client.Disconnect()

    // ── Poll interface counters ──
    ifCounters, err := client.GetInterfaceCounters()
    for _, ifc := range ifCounters {
        fmt.Printf("%-30s  rx: %8d pkts %12d bytes  tx: %8d pkts %12d bytes\n",
            ifc.InterfaceName,
            ifc.RxPackets, ifc.RxBytes,
            ifc.TxPackets, ifc.TxBytes)
    }

    // ── Poll per-node stats (show run equivalent) ──
    nodeCounters, err := client.GetNodeCounters()
    for _, nc := range nodeCounters {
        if nc.Calls == 0 { continue }
        fmt.Printf("%-40s  calls:%8d vectors:%8d vecs/call:%.1f\n",
            nc.NodeName, nc.Calls, nc.Vectors,
            float64(nc.Vectors)/float64(nc.Calls))
    }

    // ── Poll error counters (show error equivalent) ──
    errCounters, err := client.GetErrorCounters()
    for _, ec := range errCounters {
        if ec.Value == 0 { continue }
        fmt.Printf("%-50s  %d\n", ec.CounterName, ec.Value)
    }

    // ── Continuous monitoring loop ──
    ticker := time.NewTicker(1 * time.Second)
    for range ticker.C {
        // Stats segment uses version counter for consistency
        // GetInterfaceCounters handles the epoch check internally
        ifc, _ := client.GetInterfaceCounters()
        exportMetrics(ifc)  // Prometheus, InfluxDB, etc.
    }
}
```


<div class="ins">
<p>💡 <strong>Stats segment vs binary API for telemetry:</strong> The Stats API reads from shared memory - it costs ~1 microsecond per read. The binary API requires a socket round-trip - ~50–100 microseconds. For polling counters at 1Hz or faster, always use the Stats API. Use the binary API only for configuration operations (add route, set interface state).</p>
</div>
  </div>
</div>
</div>
<!-- VPP_PAPI -->
<div id="td" class="tab-pane">
<p class="sep">VPP_PAPI - PYTHON BINDINGS</p>
<div class="cp p-purple">
  <div class="cp-hdr"><span class="ico">🐍</span><h3>vpp_papi - Scripting and Automation</h3><span class="tag tag-purple">PYTHON</span></div>
  <div class="cp-body">
<p>vpp_papi (<code>src/vpp-api/python/vpp_papi/</code>) provides Python bindings for VPP's binary API. It is the same library used by VPP's Python test framework. Use it for automation scripts, management integrations, and quick prototyping.</p>


```python
from vpp_papi import VPPApiClient
import socket

# Connect to VPP
vpp = VPPApiClient(apifiles=["/usr/share/vpp/api/core/"],
                   server_address="/run/vpp/api.sock")
vpp.connect("my-python-agent")

# ── Show version ──
rv = vpp.api.show_version()
print(f"VPP: {rv.version}")

# ── List interfaces ──
for intf in vpp.api.sw_interface_dump():
    print(f"  [{intf.sw_if_index}] {intf.interface_name.rstrip(chr(0))} "
          f"link={'up' if intf.link_up_down else 'down'}")

# ── Create a TAP interface ──
rv = vpp.api.tap_create_v3(
    id=0,
    host_if_name_set=True,
    host_if_name=b"vpp0\x00",
    host_ip4_prefix_set=True,
    host_ip4_prefix={
        "address": {"af": "ADDRESS_IP4",
                    "un": {"ip4": socket.inet_aton("10.10.0.2")}},
        "len": 30
    }
)
print(f"TAP created: sw_if_index={rv.sw_if_index}")

# ── Add an IP route ──
vpp.api.ip_route_add_del(
    is_add=True,
    route={
        "prefix": {"address": {"af": "ADDRESS_IP4",
                               "un": {"ip4": socket.inet_aton("10.1.0.0")}},
                   "len": 24},
        "paths": [{"sw_if_index": rv.sw_if_index,
                   "proto": "FIB_API_PATH_NH_PROTO_IP4",
                   "nh": {"address": {"ip4": socket.inet_aton("10.10.0.1")}},
                   "weight": 1, "preference": 0}]
    }
)

# ── Subscribe to interface events ──
@vpp.register_event_callback
def on_interface_event(msg_name, msg):
    if msg_name == "sw_interface_event":
        print(f"Interface {msg.sw_if_index} link {'up' if msg.link_up_down else 'down'}")

vpp.api.want_interface_events(enable_disable=1, pid=0)

vpp.disconnect()
```


  </div>
</div>
</div>
<!-- PERFORMANCE TUNING -->
<div id="te" class="tab-pane">
<p class="sep">PERFORMANCE TUNING AND PRODUCTION PATTERNS</p>
<div class="cp p-blue">
  <div class="cp-hdr"><span class="ico">⚡</span><h3>NUMA Awareness and CPU Topology</h3><span class="tag tag-blue">PERFORMANCE</span></div>
  <div class="cp-body">
<p>VPP performance is highly sensitive to NUMA placement. Accessing memory across NUMA nodes adds ~100ns latency and reduces throughput by 30–50%. The goal is to keep NIC, hugepages, CPU cores, and worker threads all on the same NUMA node.</p>


```bash
# Step 1: Find which NUMA node your Mellanox NIC is on
cat /sys/bus/pci/devices/0000:03:00.0/numa_node
# e.g. output: 0  → NUMA 0

# Step 2: Find NUMA-local CPU cores
lscpu | grep -A5 "NUMA node0"
# e.g. NUMA node0 CPU(s): 0-11,24-35

# Step 3: Configure startup.conf to use NUMA-local cores
cpu {
  main-core 0          # core 0 on NUMA 0
  corelist-workers 2-5 # cores 2-5 on NUMA 0
}
dpdk {
  socket-mem 4096,0    # 4GB on NUMA 0, 0 on NUMA 1
}
buffers {
  buffers-per-numa 262144   # 256K buffers on NUMA 0
}

# Step 4: Verify with VPP
# vppctl: show interface rx-placement
# Verify each queue is on the worker thread whose core is NUMA-local to the NIC
```



<table class="cp-body" style="padding:0">
<tr><td>
<table style="width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.86rem">
<thead><tr><th style="background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-family:monospace">Tuning Area</th><th style="background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-family:monospace">Recommendation</th><th style="background:#1a3a5c;color:#fff;padding:.5rem .9rem;text-align:left;font-size:.77rem;font-family:monospace">How to Verify</th></tr></thead>
<tbody>
<tr><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">NUMA placement</td><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">NIC, hugepages, and workers all on same NUMA node</td><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">numastat, show interface rx-placement</td></tr>
<tr style="background:var(--bg-color,#f8f8f8)"><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">Workers = queues</td><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">num-rx-queues == num worker threads for full saturation</td><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">show run - vectors/call should be 64–256</td></tr>
<tr><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">Huge pages size</td><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">1GB pages preferred over 2MB at high load (fewer TLB misses)</td><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">perf stat -e dTLB-load-misses</td></tr>
<tr style="background:var(--bg-color,#f8f8f8)"><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">CPU isolation</td><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">isolcpus=2-5 in kernel cmdline; no other processes on worker cores</td><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">cat /sys/devices/system/cpu/isolated</td></tr>
<tr><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">IRQ affinity</td><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">Move all NIC IRQs to non-worker cores (set_irq_affinity.sh)</td><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">cat /proc/irq/*/smp_affinity_list</td></tr>
<tr style="background:var(--bg-color,#f8f8f8)"><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">Buffer sizing</td><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">buffers-per-numa ≥ 2× (num_workers × (rx_desc + tx_desc))</td><td style="padding:.48rem .9rem;border-bottom:1px solid var(--border-color,#eee);color:var(--text-color,#222)">show buffers - free% should stay above 20%</td></tr>
<tr><td style="padding:.48rem .9rem;color:var(--text-color,#222)">Turbo / C-states</td><td style="padding:.48rem .9rem;color:var(--text-color,#222)">Disable CPU power management (cpufreq governor=performance)</td><td style="padding:.48rem .9rem;color:var(--text-color,#222)">cpupower frequency-info</td></tr>
</tbody>
</table>
</td></tr>
</table>
  </div>
</div>
</div>
<!-- PROJECTS -->
<div id="tf" class="tab-pane">
<div class="proj-box">
  <div class="proj-hdr"><span class="pn">PROJECT 8</span><h4>GoVPP Control Plane Agent</h4></div>
  <div class="proj-body">
<p><strong>Objective:</strong> Build a Go agent that manages a VPP instance - configures interfaces, programs routes, polls stats, and exposes a REST API for a management frontend.</p>
<div class="ps"><div class="sn">1</div><div>Implement <code>Connect(socketPath string)</code> that establishes GoVPP connection and opens a pool of channels (one per goroutine). Handle reconnect with exponential backoff on disconnect.</div></div>
<div class="ps"><div class="sn">2</div><div>Implement <code>ConfigureInterface(name string, ip string, prefix int)</code>: list interfaces, find by name, set admin-up, add IP address. Return error if interface not found.</div></div>
<div class="ps"><div class="sn">3</div><div>Implement <code>ProgramRoutes(routes []Route)</code>: batch-program a list of static routes using a dedicated goroutine + channel. Measure time to program 1000 routes and report routes/second.</div></div>
<div class="ps"><div class="sn">4</div><div>Implement a Stats poller: connect to Stats segment, poll interface counters every 1 second, compute RX/TX PPS (delta / interval), expose via Prometheus HTTP endpoint at <code>:9090/metrics</code>.</div></div>
<div class="ps"><div class="sn">5</div><div>Implement event subscription: subscribe to <code>SwInterfaceEvent</code>, log all link state changes with timestamp. Test by toggling an interface up/down via vppctl and verifying the agent logs the event.</div></div>
<div class="ps"><div class="sn">6</div><div>Add a REST API: <code>GET /interfaces</code> returns JSON list of all VPP interfaces with counters. <code>POST /routes</code> programs a new route. <code>DELETE /routes/{prefix}</code> removes it. Test with curl.</div></div>
  </div>
</div>
<div class="proj-box">
  <div class="proj-hdr"><span class="pn">PROJECT 9</span><h4>End-to-End Production Topology</h4></div>
  <div class="proj-body">
<p><strong>Objective:</strong> Integrate all phases into a complete topology: VPP + DPDK physical ports + memif container connections + linux-cp for control plane + GoVPP management agent + observability.</p>
<div class="ps"><div class="sn">1</div><div>Design the topology: 2 DPDK ports (physical NIC), 2 memif ports (connecting to application containers), 1 TAP for management. VPP acts as the central packet forwarder.</div></div>
<div class="ps"><div class="sn">2</div><div>Deploy linux-cp mirroring both DPDK interfaces to Linux for FRRouting OSPF. Verify FRR forms OSPF adjacency and installs routes. VPP dataplane uses these routes for forwarding.</div></div>
<div class="ps"><div class="sn">3</div><div>Enable the classify plugin (from Phase 4) on ip4-unicast arc. Program DROP rules for RFC-1918 sources via the GoVPP agent's REST API. Verify drops with show error.</div></div>
<div class="ps"><div class="sn">4</div><div>Deploy the Prometheus + Grafana stack. Import the GoVPP agent's metrics. Build a dashboard showing: RX/TX PPS per interface, vectors/call for dpdk-input, buffer utilisation, error counter rates.</div></div>
<div class="ps"><div class="sn">5</div><div>Run a 30-minute traffic test at 50% line rate. Verify: zero packet loss (<code>show error</code>), stable vectors/call for dpdk-input (32–256), free buffer% stays above 30%, FRR OSPF adjacency stays up throughout.</div></div>
  </div>
</div>
</div>
<!-- CHECKLIST -->
<div id="tg" class="tab-pane">
<p class="sep">P5 COMPLETION CHECKLIST</p>
<ul class="cl">
  <li>Can connect to VPP from Go using GoVPP, open channels, and send request/reply messages</li>
  <li>Know the multi-channel pattern: one channel per goroutine, no sharing</li>
  <li>Can implement interface dump, set interface state, add IP address in Go</li>
  <li>Can implement IP route add/delete with correct ip_types structures</li>
  <li>Can subscribe to VPP events (want_interface_events) and handle them in a goroutine</li>
  <li>Understand the Stats API architecture: shared memory, zero IPC cost</li>
  <li>Can connect to Stats segment and poll interface, node, and error counters</li>
  <li>Know when to use Stats API vs binary API (telemetry vs configuration)</li>
  <li>Can write a vpp_papi Python script: connect, API call, event subscription</li>
  <li>Know the 7 key NUMA/performance tuning areas and the CLI to verify each</li>
  <li>Understand workers=queues constraint and how to size buffers-per-numa</li>
  <li>Completed Project 8 (GoVPP agent with Prometheus) and Project 9 (full production topology)</li>
</ul>
<div class="ins" style="margin-top:1.2rem;">
  <p>🎉 <strong>Phase 5 complete.</strong> You can now build production VPP deployments end-to-end: from DPDK physical interfaces through custom plugins to a fully automated GoVPP control plane with observability. <strong>Bonus:</strong> continue to the Host Stack module to explore VPP's TCP/Session layer, VCL, and application namespaces.</p>
</div>
</div>
<div class="mod-nav">
  <a href="/learning/data-plane/vpp/module-p4-plugin-dev/">← Plugin Dev</a>
  <a href="/learning/data-plane/vpp/vpp-roadmap/">🗺️ Roadmap</a>
  <a class="nb" href="/learning/data-plane/vpp/module-hoststack/">🌐 Host Stack (Bonus) →</a>
</div>
<script>
function vt(e,id){document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));e.target.classList.add('active');document.getElementById(id).classList.add('active');}
</script>
