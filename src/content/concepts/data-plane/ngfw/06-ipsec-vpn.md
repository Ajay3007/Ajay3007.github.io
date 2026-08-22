---
title: "IPsec / VPN"
description: "🔐 IPsec / VPN — IKE Control Plane meets VPP Data Plane [Module 05](/learning/data-plane/ngfw/ips-integration/) covered inspection; this one covers the other big external…"
domain: data-plane
track: ngfw
order: 6
url: /learning/data-plane/ngfw/ipsec-vpn/
---

# 🔐 IPsec / VPN — IKE Control Plane meets VPP Data Plane

[Module 05](/learning/data-plane/ngfw/ips-integration/) covered inspection; this one covers the other big external engine: **encrypted VPN tunnels**. It's the clearest example in the whole platform of the **control-plane / data-plane split** from [Module 01](/learning/data-plane/ngfw/first-principles/) — and once you see how the two halves connect, the design of the rest of the box clicks into place.

The guiding question:

> **How do you do IPsec at line rate when the key negotiation is a slow, stateful cryptographic conversation — and the encryption has to happen on every single packet?**

The answer: split the job. A dedicated **IKE daemon** (StrongSwan's `charon`) does the negotiation; **VPP** does the encryption; and a **bridge plugin** carries the negotiated keys from one to the other.

---

## Table of Contents

- [IPsec in 90 Seconds](#ipsec-90s)
- [The Two-Part Problem](#two-part)
- [StrongSwan & the IKE Daemon](#strongswan)
- [The Bridge: Programming SAs into VPP](#bridge)
- [VICI: charon's Automation API](#vici)
- [Bringing a Tunnel Up](#bringup)
- [Driving IPsec from the VPP Console](#vpp-console)
- [The Data Plane Side](#data-plane-side)
- [Rekeying](#rekeying)
- [Key Takeaways](#key-takeaways)
- [What's Next](#whats-next)

---

## IPsec in 90 Seconds {#ipsec-90s}

**IPsec** is the standard suite for encrypting IP traffic between two endpoints — a **VPN tunnel**. Four terms cover almost everything you'll meet in the code:

| Term | Meaning |
|------|---------|
| **ESP** | *Encapsulating Security Payload* — the protocol that actually encrypts and authenticates each packet. |
| **SA** (Security Association) | The agreed keys + parameters for **one direction** of a tunnel. A working tunnel has a pair (in + out). Each SA has an **SPI** (a number in the packet identifying which SA to use). |
| **IKE** | *Internet Key Exchange* — the protocol two peers use to **authenticate each other and negotiate the SAs**. Modern version: IKEv2. |
| **Traffic selectors** | Which source/destination ranges are allowed into the tunnel. |

The essential asymmetry: **IKE runs occasionally** (bring a tunnel up, rekey it every few minutes), while **ESP runs on every packet**. That asymmetry is *why* the two live in different planes.

---

## The Two-Part Problem {#two-part}

Encrypting a packet is a data-plane job — it must happen at line rate for every packet, so it belongs in VPP alongside forwarding and NAT. But *negotiating* the keys is a completely different animal: a multi-round-trip, stateful, cryptographic handshake with the remote peer, involving Diffie-Hellman, authentication, retries, and timers. You would never want that logic on the packet hot path.

So the platform splits IPsec cleanly in two:

![IPsec control/data split](/assets/diagrams/learning/data-plane/ngfw/ipsec-control-data-split.svg){:class="diagram-img"}

*The IKE daemon (control plane) negotiates keys rarely; VPP (data plane) encrypts every packet. The kernel-vpp bridge plugin installs the negotiated keys into VPP.*

- **Control plane:** StrongSwan `charon` speaks IKEv2 to the remote peer and produces SAs.
- **Bridge:** a **kernel-vpp plugin** takes each negotiated SA and installs it into VPP.
- **Data plane:** VPP's `esp-encrypt` / `esp-decrypt` nodes do the actual crypto, using those SAs, at line rate.

Everything below is just the detail of those three boxes and the arrows between them.

---

## StrongSwan & the IKE Daemon {#strongswan}

**StrongSwan** is a mature open-source IPsec implementation; its IKE daemon is called **`charon`**. Reusing it is the same "don't reinvent a hard, security-critical thing" choice made for Snort. `charon` handles:

- the **IKEv2 handshake** with the peer (key exchange + mutual authentication, here via a pre-shared key),
- deriving the **ESP keys** and establishing the **child SAs**,
- **lifetimes and rekeying** — SAs expire on purpose, and charon renegotiates before they do,
- retries, dead-peer detection, and all the messy real-world edge cases.

In a stock setup, charon would install the SAs it negotiates into the **Linux kernel's** IPsec stack. But we don't want the *kernel* doing encryption — we want *VPP* doing it. That's what the bridge changes.

---

## The Bridge: Programming SAs into VPP {#bridge}

StrongSwan has a **pluggable "kernel" backend** — the component that receives negotiated SAs and installs them somewhere. Normally that "somewhere" is the Linux kernel. This platform swaps in a custom **kernel-vpp plugin** so that "somewhere" becomes **VPP**.

Concretely, when charon finishes a negotiation, the kernel-vpp plugin:

1. **Installs the SA into VPP** — adds the keys/SPIs to VPP's SA table so `esp-encrypt`/`esp-decrypt` can use them.
2. **Auto-binds the SA to the VPP tunnel interface** — so you don't have to run a manual "protect this tunnel" command in VPP; the plugin wires the SA to the right interface automatically (linked by a **`reqid`** shared between the StrongSwan child config and the VPP tunnel).
3. **Refreshes on rekey** — when charon rekeys (new keys, new SA indices), the plugin updates the binding so the tunnel keeps working seamlessly. This is the subtle part: SA indices change on every rekey, and the plugin keeps the interface↔SA binding correct across each refresh.

It supports both VPP tunnel styles — the older `ipip` tunnels and the preferred `ipsec` interface tunnels — configurable so both ends agree. The net effect: **charon thinks it's programming "the kernel," but the kernel is really VPP.** That's the whole trick, and it's why VPP can encrypt at line rate while StrongSwan handles all the IKE complexity.

---

## VICI: charon's Automation API {#vici}

How does anything *tell* charon to load a tunnel or rekey one? Through **VICI** — charon's *Versatile IKE Configuration Interface*, a local Unix-domain socket (`/var/run/charon.vici`) that exposes charon's operations to programs. Anything that speaks VICI can:

- `load_conn` — define an IKE connection + child SA (proposals, traffic selectors, reqid, lifetimes),
- `load_shared` — install a pre-shared key,
- `initiate` / `terminate` — bring a specific tunnel up or down,
- `rekey` — force a renegotiation,
- `list_sas`, `get-counters`, `stats` — read live tunnel state.

This platform drives VICI from **Python** using the `vici` library. Two scripts do the work:

- **`create_ipsec.py`** — the *setup* script. It opens the VICI socket, calls `load_conn` with the connection definition (IKE version, proposals, ESP proposals, traffic selectors auto-derived from the address family, `reqid`, rekey/lifetime), `load_shared` for the PSK, then `initiate` to bring the child SA up. There's a matching `delete` that terminates and unloads.
- **`swanctl_bridge.py`** — the *runtime* script. It wraps day-to-day operations: `list-sas` (formatted tunnel status), `rekey`, `terminate`, `initiate`, `stats`, `counters`, and `load-all`. Rekey/initiate/terminate are fired in the **background** (`timeout -1`) so the caller returns immediately rather than blocking on the negotiation.

Using VICI (rather than shelling out to the `swanctl` command for everything) means the platform gets structured request/response data back — which is what makes the nicely formatted status output possible.

---

## Bringing a Tunnel Up {#bringup}

Putting the pieces in motion, here's the full lifecycle from config to encrypted packets:

![Bringing a tunnel up](/assets/diagrams/learning/data-plane/ngfw/ipsec-tunnel-bringup.svg){:class="diagram-img"}

*Steps 1–4 are the control plane, step 5 is the bridge, steps 6–7 are the data plane doing the actual work.*

1. **Load the connection.** `create_ipsec.py` connects to VICI and calls `load_conn` (IKE + ESP proposals, traffic selectors, `reqid`) and `load_shared` (the PSK).
2. **Initiate the child SA.** `initiate({child})` tells charon to bring this tunnel up now.
3. **IKEv2 handshake.** charon talks to the peer over UDP 500/4500: `IKE_SA_INIT` (Diffie-Hellman) then `IKE_AUTH` (mutual authentication with the PSK).
4. **Child SA established.** Both ends now hold matching ESP keys and SPIs — one SA per direction.
5. **kernel-vpp installs the SA into VPP** ★ and auto-binds it to the tunnel interface (via `reqid`). *This is the moment a negotiated key becomes usable by the fast path.*
6. **Data plane ready.** Packets steered to IPsec (remember `out_sa_index` from the [decision node](/learning/data-plane/ngfw/packet-walkthrough/)) hit `esp-encrypt` with this SA and leave as ESP toward the peer.
7. **Rekey** happens automatically before the SA expires (next section).

The inbound direction mirrors this: an ESP packet arrives, `esp-decrypt` uses the inbound SA to recover the original packet, and it's then processed normally (reverse-NAT, forward) — exactly the return trip from [Module 04](/learning/data-plane/ngfw/packet-walkthrough/).

---

## Driving IPsec from the VPP Console {#vpp-console}

Here's a neat integration detail that ties the planes together for the *operator*. An admin usually lives on the **VPP console** (`vppctl`) — they shouldn't need to jump to a different tool to check tunnels. So the `ngfw_decision` plugin adds `ngfw_swanctl ...` CLI commands to VPP:

```
vpp# ngfw_swanctl show sas          # list active IKE + child SAs
vpp# ngfw_swanctl initiate <child>  # bring a tunnel up
vpp# ngfw_swanctl rekey child <name>
vpp# ngfw_swanctl stats             # charon daemon stats
```

Under the hood, each of these simply **`popen()`s** `python3 swanctl_bridge.py <verb>` and streams the script's output back to the VPP console. So the flow is:

**operator → VPP CLI → `popen` python bridge → VICI socket → charon.**

It's a deliberately thin shim — VPP doesn't reimplement IKE management; it just shells out to the Python that already knows how to talk to charon. This is a recurring theme worth internalizing: **when you need a capability that already exists in another process, bridge to it rather than rebuild it.** The whole platform is bridges.

---

## The Data Plane Side {#data-plane-side}

From the data plane's point of view, all this control-plane machinery boils down to one thing: **an SA sitting in VPP's SA table, ready to use.** When the decision node chose an IPsec action (Modules 03–04), it recorded an **`out_sa_index`** — an index into that table. At `esp-encrypt`, VPP looks up that SA, encrypts the packet with its keys, stamps the SPI, and sends it out the tunnel interface.

That's the beauty of the split: the hot path never touches IKE, PSKs, or negotiation. It does a **table lookup and a crypto operation** — fast, deterministic, and blissfully unaware of the multi-round-trip handshake that produced the keys. All the complexity was paid *once*, in the control plane, and cached as an SA the data plane can use millions of times.

---

## Rekeying {#rekeying}

IPsec SAs are **short-lived on purpose** — limiting a key's lifetime limits the damage if it's ever compromised, and caps how much data is encrypted under one key. So charon **rekeys**: before an SA expires (its `rekey_time`), it negotiates a fresh one.

Rekeying is exactly where a naive VPP integration would break, because **the new SA has a new index**, and the tunnel interface was bound to the *old* one. The kernel-vpp plugin handles this: on each rekey it installs the new SA and **re-binds** the tunnel interface to it, so traffic flips to the new keys with no manual step and no dropped tunnel. Getting this refresh-on-rekey binding right is one of the genuinely fiddly parts of the platform — and a good example of why the "boring" lifecycle details matter as much as the initial happy path.

---

## Key Takeaways {#key-takeaways}

1. IPsec splits naturally: **IKE negotiation is occasional (control plane); ESP encryption is per-packet (data plane).** That asymmetry drives the whole design.
2. **StrongSwan `charon`** does the IKEv2 handshake and produces **SAs** (keys + SPIs, one per direction); it's reused rather than reimplemented.
3. A **kernel-vpp bridge plugin** replaces StrongSwan's Linux-kernel backend so negotiated SAs are installed into **VPP** and **auto-bound** to the tunnel interface.
4. **VICI** is charon's automation socket; **`create_ipsec.py`** sets tunnels up (`load_conn` + `load_shared` + `initiate`) and **`swanctl_bridge.py`** runs day-to-day ops.
5. The VPP CLI exposes `ngfw_swanctl` commands that just **`popen` the Python bridge** — the operator drives IKE without leaving the console.
6. The data plane only ever sees an **SA in a table** referenced by `out_sa_index`; `esp-encrypt` does a lookup + crypto and forgets the rest.
7. **Rekeying** refreshes SAs periodically; the bridge re-binds the tunnel interface to each new SA so the tunnel survives seamlessly.

---

## What's Next {#whats-next}

We've now covered both external engines (IPS and IPsec) and the data plane that ties them together. The last mechanism to open is the **management plane**: how the Java bridge reads VPP's counters and stats (over JNI, the stats segment, and the binary API) and serves them northbound — turning all the per-packet activity we've traced into dashboards and alarms.

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="/learning/data-plane/ngfw/ips-integration/" style="display:inline-block;padding:10px 20px;background:#94a3b8;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← Module 05</a>
  <a href="/learning/data-plane/ngfw/" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">NGFW Home</a>
  <a href="/learning/data-plane/" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Data Plane 🏠</a>
</div>
