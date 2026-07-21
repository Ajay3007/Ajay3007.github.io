# AxioByte Systems (@axiobyte.systems) — Content Tracker

Second channel: **networking & high-performance systems** explainers. 9:16 vertical, **75–90s deep** episodes, manim + v3 palette with a diagram/animation toolkit (nodes, animated packet-flows, layer stacks, sequence timelines, latency/throughput meters). Same 4-file deliverable per episode: `sysNN_video.py`, `coverNN_9x16.py`, `axiobyte_sys_NN_captions.txt`, `axiobyte_sys_NN_subtitles.srt`.

Status key: ✅ done · ▶️ next · ⬜ todo · 🎬 pilot

---

## Pillar 1 · High-Performance Data Plane  (launch pillar)

Ranked for standalone shareability + logical build-up. Difficulty is audience-depth, not gate.

| Ep | Title (working) | Core aha | Source modules | Status |
|----|-----------------|----------|----------------|--------|
| 1  | Why the kernel is slow for packets | interrupts + copies + context switches; DPDK bypasses the kernel | dpdk/module-p1-foundation, networking/m17-dpdk | ✅ |
| 2  | Zero-copy: a packet is just a pointer | mbuf + mempool; you pass a handle, never copy bytes | dpdk/module-p1-memory, projects/module-09-mempool-mbuf | ▶️ |
| 3  | Poll-mode: why 100% CPU is a *feature* | PMD busy-polls the NIC; no interrupts, no jitter | dpdk/module-p2-pmd, projects/module-10-port-init | ⬜ |
| 4  | NUMA: the wrong core kills your throughput | remote memory access halves packet rate; pin core↔NIC↔mem | dpdk/module-p3-perf, projects/module-14-numa-alloc | ⬜ |
| 5  | False sharing: two threads, one cache line | "different" variables on the same 64B line ping-pong | dpdk/module-p3-perf | ⬜ |
| 6  | The lock-free ring buffer | SPSC ring, head/tail, producers & consumers never block | dpdk/module-p2-rings, projects/module-03-ring-buffer | ⬜ |
| 7  | Huge pages: why 4KB pages throttle packets | TLB misses; 2MB/1GB pages cut page-table walks | dpdk/module-p1-memory | ⬜ |
| 8  | Batching: process packets in bursts | amortize per-packet overhead; rx_burst of 32 | dpdk/module-p2-pmd, projects/module-11-pipeline | ⬜ |
| 9  | RSS & multi-queue NICs | hash the 5-tuple → spread flows across cores, keep affinity | dpdk/module-p2-pmd | ⬜ |
| 10 | NGFW fast path vs slow path | first packet does the work; the flow's rest fly through | ngfw/03-vpp-data-plane, ngfw/04-packet-walkthrough | ⬜ |
| 11 | A packet's journey through an NGFW | parse → classify → policy → inspect → forward | ngfw/04-packet-walkthrough | ⬜ |
| 12 | Line-rate DPI (why regex is the wall) | Hyperscan: match thousands of patterns in one pass | projects/module-15/16-hyperscan, ngfw/05-ips-integration | ⬜ |
| 13 | VPP: process a *vector* of packets | one node handles a burst → instruction-cache warm, fewer calls | vpp/module-p2-vlib, networking/m18-vpp | ⬜ |
| 14 | Conntrack: how a firewall remembers | 5-tuple state table; stateful vs stateless | networking/m23-conntrack-nat | ⬜ |
| 15 | eBPF/XDP: your code in the NIC driver | the kernel's answer to bypass; drop/redirect before the stack | networking/m16-ebpf-xdp | ⬜ |
| 16 | IPsec at line rate (crypto is the ceiling) | per-packet encrypt/auth; offload & batching | ngfw/06-ipsec-vpn, networking/m21-ipsec | ⬜ |

---

## Later pillars (slate TBD after pillar 1 traction)

- **Packets & Protocols** — TCP handshake, flow control/HOL blocking, DNS chain, TLS 1.3, NAT, BGP, HTTP/1.1↔2↔3 (networking/ + backend/)
- **Cellular Core (4G/5G)** — attach procedure, control vs user plane, 5G-AKA, UPF/edge latency, VoLTE/VoNR (4g-5g/)
- **Backend & Distributed Systems** — gRPC vs REST, B-tree indexes, Kafka, JWT, CAP/consistency (backend/)

### Toolkit to build (shared, in each sys file until stable)
node/box · flow (animated packet-dots) · layers (encap stack) · sequence (handshake timeline) · meter (latency/throughput gauge) · reuse v3 glow + code panel (only when code earns it).
