---
layout: learning
title: IPS Integration (Snort + DAQ)
permalink: /learning/data-plane/ngfw/ips-integration/
---

# 🔬 IPS Integration — Snort over Shared Memory

In [Module 04]({{ '/learning/data-plane/ngfw/packet-walkthrough/' | relative_url }}), Snort was a black box: a packet went in, a verdict came out. This module opens the box. It's the most intricate channel in the whole platform, and it answers a genuinely hard question:

> **How do you let a separate, general-purpose intrusion-prevention program inspect every packet — at line rate — without copying packets, without parsing log files, and without one process blocking the other?**

The answer is a carefully designed **shared-memory** interface with a small twist inside Snort itself. Understanding it will teach you a pattern you'll reuse for any high-speed process-to-process channel.

---

## Table of Contents

- [Why Snort Is a Separate Process](#why-separate)
- [The DAQ: Snort's Pluggable Input](#the-daq)
- [The Shared-Memory Design](#shared-memory)
- [Descriptors and the Buffer Pool](#descriptors)
- [The Connection Handshake](#handshake)
- [How the Verdict Comes Back](#verdict)
- [Multiple Instances & Scaling](#scaling)
- [What VPP Learns: Verdicts, SIDs, AppIDs](#stats)
- [Resilience: When Snort Dies](#resilience)
- [Key Takeaways](#key-takeaways)
- [What's Next](#whats-next)

---

## Why Snort Is a Separate Process {#why-separate}

Snort 3 is a large, mature C++ intrusion-prevention engine with its own rule language, detection tree, and application-identification (AppID) subsystem. Two options exist for using it inside a VPP-based firewall:

1. **Rewrite Snort's detection logic as a VPP plugin.** Enormous effort, and you'd forever chase upstream Snort's rule and signature updates.
2. **Run real Snort as-is, and feed it packets from VPP.** Reuse a battle-tested engine; inherit its rules and community updates for free.

The platform chooses option 2 — the theme from [Module 02]({{ '/learning/data-plane/ngfw/architecture-overview/' | relative_url }}): *VPP provides the fast path; proven engines provide the smarts; a thin bridge connects them.* But option 2 has a cost: Snort runs in **its own process**, with its own memory. Getting millions of packets per second across that process boundary is the entire challenge — and a naive approach (a socket per packet, or writing packets to a file) would be thousands of times too slow.

---

## The DAQ: Snort's Pluggable Input {#the-daq}

Snort was designed to be fed by different packet sources — a live NIC, a pcap file, an inline bridge. It abstracts "where packets come from" behind an interface called the **DAQ (Data AcQuisition module)**. A DAQ is a plugin that knows how to *receive* packets, hand them to Snort, and *apply* the verdict Snort returns.

This platform ships a **custom `vpp` DAQ module**. Snort is launched with `--daq vpp`, and from Snort's point of view it's just "reading packets from the VPP source." Under the hood, the VPP DAQ speaks the shared-memory protocol to VPP. This is the clean seam that makes the integration possible: **VPP didn't have to change how Snort works, and Snort didn't have to know it's talking to VPP** — the DAQ absorbs the impedance mismatch.

You saw the launch side of this in the startup flow: each Snort instance is started with `--daq vpp`, a DAQ directory, and the socket path.

---

## The Shared-Memory Design {#shared-memory}

Here's the core mechanism. VPP and each Snort process **share a region of memory** (mapped into both address spaces). Packets never travel through a socket or a pipe — they sit in shared memory, and the two sides exchange tiny **descriptors** that *point* at them.

![VPP to Snort over Shared Memory]({{ '/assets/diagrams/learning/data-plane/ngfw/snort-shared-memory.svg' | relative_url }}){:class="diagram-img"}

*A per-thread queue pair carries descriptors out to Snort and verdicts back. The packet bytes live in a shared buffer pool and are referenced by offset — zero copy.*

The shared region has two parts:

- **A buffer pool** — where the actual packet bytes live.
- **One or more queue pairs** — the signalling rings that pass work back and forth.

A **queue pair** is exactly two ring buffers:

- an **enqueue ring** — VPP → Snort ("here's a packet to inspect"), and
- a **dequeue ring** — Snort → VPP ("here's my verdict").

Crucially, there is **one queue pair per VPP worker thread**. Because each worker owns its own ring, there's **no lock contention** between workers — each is a single-producer/single-consumer (SPSC) channel, and the only cross-process synchronization is a pair of **head/tail indices** per ring. This is the same lock-free ring-buffer idea you built by hand in the [data-plane exercises]({{ '/learning/data-plane/projects/' | relative_url }}) — here it spans two processes.

---

## Descriptors and the Buffer Pool {#descriptors}

The thing that actually moves through the rings is a small **descriptor**, roughly:

```c
struct descriptor {
    offset;          /* where in the buffer pool the packet bytes are */
    length;          /* how many bytes */
    buffer_pool_id;  /* which pool */
    metadata;        /* a 16-byte union — see below */
};
```

The descriptor is tiny; the packet it refers to might be 1500 bytes, but only the **offset** crosses the ring. Snort resolves the offset into its own view of the shared buffer pool and reads the packet **in place** — that's what "zero copy" means. No memcpy per packet; the bytes are written once (by the NIC/VPP) and read where they lie.

The **metadata** field is a neat space-saving trick: it's a **union** that means different things in each direction.

- **On the way in (VPP → Snort):** it carries packet context — flags, a flow id, the ingress interface.
- **On the way back (Snort → VPP):** the *same 16 bytes* are overwritten with the **result** — the verdict, an AppID, and up to ten matched rule IDs (SIDs) with their per-rule verdicts.

Reusing one small, fixed-size slot for both directions keeps the descriptor to a single cache-line-friendly size — the kind of micro-decision that matters when you touch a struct tens of millions of times a second.

---

## The Connection Handshake {#handshake}

Before any packets flow, Snort's DAQ and VPP negotiate over a Unix-domain **control socket** (the `snort.sock` you saw in the startup config). It's a short, versioned request/reply handshake:

1. **CONNECT** — "I'm a VPP DAQ, protocol version N, here's my mode (inline/passive)." VPP replies with how many buffer pools exist.
2. **GET_BUFFER_POOL** — Snort asks for each pool's size, then **mmaps** it into its own address space. Now both processes see the same packet bytes.
3. **GET_INPUT** — Snort names the instance it's attaching to (e.g. `snort0`) and learns how many queue pairs that instance has.
4. **ATTACH_QPAIR** — Snort claims a queue pair and receives the **offsets** of its header, enqueue ring, and dequeue ring within the shared region.

After the handshake, the socket goes quiet — it's **not** on the packet hot path. All per-packet work happens through the shared-memory rings. (The socket is later reused only for occasional control, like triggering a rule reload.) This "**slow socket to set up, fast shared memory to run**" split is a recurring high-performance pattern — the same shape as the control-plane/data-plane split in the firewall as a whole.

---

## How the Verdict Comes Back {#verdict}

This is the cleverest part, and it lives partly **inside Snort itself**. Ordinarily, when Snort matches a rule it writes an **alert to a log file**. But VPP can't read a log file in real time to decide a packet's fate — it needs the verdict *now*, bound to *this* descriptor.

So Snort is **patched** to hand results straight back through the DAQ instead of (only) logging them:

![How a Verdict Gets Back to VPP]({{ '/assets/diagrams/learning/data-plane/ngfw/snort-verdict-roundtrip.svg' | relative_url }}){:class="diagram-img"}

*Patched Snort writes match results into thread-local storage; the DAQ's finalize step copies them into the shared descriptor and signals VPP.*

Walk the round trip:

1. **VPP enqueues** a descriptor on the worker's enqueue ring and bumps the head.
2. **Snort's DAQ dequeues** it, resolves the offset, and presents the packet to Snort's detection engine.
3. **Snort evaluates the rules.** On a match, a patched hook in the detection path (`fpLogEvent`) writes the result to **thread-local storage** — not a file:
   - `snort_sid_entries[]` — the matched rule SID(s) and each one's translated verdict,
   - `snort_sid_count` — how many matched (capped at ten),
   - `snort_detected_appid` — the identified application.
4. **AppID (optional).** A custom DataBus handler catches application-identification events and updates the thread-local AppID (so you learn "this was HTTP / SSL / a specific app").
5. **The hand-off — `daq_vpp_msg_finalize()`.** ★ When Snort finishes the packet and returns control to the DAQ, this function **reads the thread-local values and copies them into the descriptor's metadata union** (verdict + AppID + SIDs), then **resets** the thread-local counters for the next packet. *This is the exact boundary where Snort's world becomes VPP's world.*
6. **Signal.** The DAQ atomically bumps the dequeue-ring head and **wakes VPP** — either VPP is polling the ring, or Snort pokes an **`eventfd` (`deq_fd`)** to wake it (interrupt mode). Polling trades CPU for latency; interrupts do the reverse — the platform can switch between them at runtime.
7. **VPP reads the verdict.** The VPP dequeue node reads the metadata: **PASS** → the packet continues the feature arc (on to `ngfw-post-snort`, per Module 04); **BLOCK** → it's routed to `error-drop`.

Why thread-local storage? Because Snort is **multi-threaded**, and each thread inspects a different packet at the same time. Thread-local variables give each thread its own private scratch space, so two threads writing verdicts simultaneously never collide. The DAQ, running on that same thread when it finalizes, reads exactly that thread's result.

The whole round trip touches **no log file and no per-packet socket** — just a shared-memory descriptor and, at most, one `eventfd` wake. That's what makes inline inspection viable at these rates.

---

## Multiple Instances & Scaling {#scaling}

Inspection is expensive, so it's the first thing you scale. The platform runs **several Snort instances**, each a separate process pinned to its own CPU core, and each backed by its own shared-memory instance. The VPP CLI drives this:

```
vpp# snort create-instance name snort0 queue-size 1024 on-disconnect drop
vpp# snort attach instance snort0 interface <iface> input
```

The startup script generates one `create-instance` + `attach` per instance from a single "how many Snort instances?" parameter — so scaling inspection throughput is a config change, not a code change. Each VPP worker thread maps to a queue pair, and packets are steered to an instance for inspection; more instances on more cores means more parallel inspection.

The plugin also mirrors everything for **IPv6**: it registers `snort-ip6-input` on the `ip6-unicast` arc, and attaching Snort to an interface enables both the v4 and v6 inspection paths automatically.

---

## What VPP Learns: Verdicts, SIDs, AppIDs {#stats}

Because the verdict metadata flows back into VPP, VPP can build **security telemetry** without touching Snort's logs:

- **Verdict counters** — totals per outcome: PASS, BLOCK, REPLACE, WHITELIST, BLACKLIST, IGNORE.
- **SID mapping** — which rule signature IDs are firing, and how often (which threats are being seen).
- **AppID mapping** — which applications the traffic is, resolved against the OpenAppID database to friendly names (e.g. `http`, `ssl`, a specific app).

These are visible from the VPP CLI (`show snort counters`, `show snort stats`) and — importantly — this is exactly the data the [management bridge]({{ '/learning/data-plane/ngfw/architecture-overview/' | relative_url }}) reads and pushes northbound. The IPS verdict you traced in Module 04 is the *same* number an operator sees on a dashboard; this is where it originates.

---

## Resilience: When Snort Dies {#resilience}

A separate process can crash. What happens to traffic if a Snort instance dies mid-flight? That's the **`on-disconnect` policy**, set per instance:

- **`drop`** — fail *closed*: if the inspector is gone, drop the packets it would have inspected. Safer; no uninspected traffic slips through.
- **`pass`** — fail *open*: bypass inspection and keep forwarding. Preserves connectivity at the cost of temporarily uninspected traffic.

Which one is "right" is a policy decision, not a technical one — it's the classic security-vs-availability trade-off, made explicit as a knob. The fact that it's a per-instance setting is a good example of the platform surfacing a genuine operational choice instead of hard-coding it.

---

## Key Takeaways {#key-takeaways}

1. Snort runs as a **separate process** so the platform reuses a mature IPS instead of reimplementing detection — at the cost of a hard process-boundary problem.
2. The **DAQ** is Snort's pluggable input abstraction; a custom `vpp` DAQ lets Snort read from VPP without either side being rewritten.
3. Packets cross via **shared memory**: a **buffer pool** holds the bytes (zero copy), and **per-worker queue pairs** (enqueue + dequeue rings) pass small **descriptors** — lock-free SPSC, synchronized only by head/tail indices.
4. The descriptor's **metadata union** is reused: packet context inbound, **verdict + SID + AppID** outbound.
5. A short **socket handshake** (connect → map pools → get input → attach queue pair) sets things up; after that the socket is off the hot path.
6. Patched Snort writes results to **thread-local storage**, and **`daq_vpp_msg_finalize()`** copies them into the shared descriptor and signals VPP (poll or `eventfd`) — the precise Snort→VPP boundary.
7. Inspection **scales by running more instances** on more cores (a config knob); everything mirrors for IPv6.
8. Verdict/SID/AppID telemetry flows back into VPP counters and onward to management; an **`on-disconnect` policy** (drop vs pass) makes the fail-closed/fail-open choice explicit.

---

## What's Next {#whats-next}

We've covered how the data plane inspects. The next module turns to the other big external engine: **IPsec/VPN** — how the control plane negotiates tunnel keys with a separate IKE daemon (StrongSwan) and programs them into VPP so the data plane can encrypt at line rate.

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/learning/data-plane/ngfw/packet-walkthrough/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#94a3b8;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← Module 04</a>
  <a href="{{ '/learning/data-plane/ngfw/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">NGFW Home</a>
  <a href="{{ '/learning/data-plane/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Data Plane 🏠</a>
</div>
