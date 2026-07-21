---
layout: default
title: Packet Walkthrough
permalink: /learning/data-plane/ngfw/packet-walkthrough/
---

# 🚶 Packet Walkthrough — One Connection, End to End

[Module 03]({{ '/learning/data-plane/ngfw/vpp-data-plane/' | relative_url }}) gave us the mechanism: a graph of nodes, a feature arc, and a note carried in `opaque2`. This module turns that mechanism into a **story**. We'll follow one packet from the wire to the far side of a VPN tunnel, watch the decision get made, watch the note evolve, and then look at every *other* path the same pipeline can take — including how the reply gets home.

If Module 03 was "here are the parts," this is "here's the machine running."

---

## Table of Contents

- [The Setup](#setup)
- [The Journey, Step by Step](#journey)
- [The Six Possible Paths](#six-paths)
- [When Things Get Dropped](#drops)
- [The Return Trip](#return-trip)
- [IPv6: the Mirror World](#ipv6)
- [How to Watch This Happen](#watch)
- [Key Takeaways](#key-takeaways)
- [What's Next](#whats-next)

---

## The Setup {#setup}

Our example: a host on the **inside** network opens a connection to a service that lives across a **site-to-site VPN tunnel**. So this packet must be **inspected** (it's going somewhere sensitive), **NAT'd** (the inside address is private), and **encrypted** (it's leaving over IPsec). That's the richest path through the firewall, which makes it the best one to trace.

Concretely, the platform is configured so that:

- The **inbound interface** is a VLAN sub-interface with the firewall feature arc enabled (`ngfw-decision`, `snort`, `ngfw-post-snort` on `ip4-unicast`).
- An **ACL rule** matches this flow and carries the steering tag **`SNORT_NAT_IPSEC`** — "inspect it, translate it, encrypt it."
- An **IPsec Security Association (SA)** for the tunnel has already been negotiated by the control plane (Module 02) and installed in the data plane.
- The **VPN-out interface** is where encrypted packets leave.

---

## The Journey, Step by Step {#journey}

![One Packet's Journey]({{ '/assets/diagrams/learning/data-plane/ngfw/packet-journey.svg' | relative_url }}){:class="diagram-img"}

*The left column is the sequence of graph nodes; the right column shows the per-packet note in `opaque2` changing as the packet moves.*

**Step 0 — Ingress.** The packet lands on the inbound VLAN sub-interface. DPDK's poll-mode driver picks it up (no interrupt) and hands it, as part of a batch, into the graph. At this moment it's just bytes with a 5-tuple: *source IP:port → destination IP:port, protocol*.

**Step 1 — `ip4-input`.** VPP's standard IPv4 entry node validates the header — checksum, length, TTL — and places the packet onto the `ip4-unicast` feature arc. From here on, the packet visits whichever arc features are enabled on this interface, in their registered order.

**Step 2 — `acl-plugin`.** The ACL feature matches the packet against the rule set. Our rule hits, and its steering tag — `SNORT_NAT_IPSEC` — is written into the first four bytes of the packet's `opaque2` scratch area. The ACL has now answered *"which rule matched and what does it want?"* but hasn't acted.

> 📝 **opaque2 now:** `[SNORT_NAT_IPSEC][ - ][ - ][ - ]`

**Step 3 — `ngfw-decision`.** Registered `runs_after` the ACL and `runs_before` Snort, this node reads the tag and translates it into an internal **action**: *snort-then-nat-then-ipsec*. Because that action requires inspection, the node does **not** short-circuit. Instead it:

- writes the **note** the post-Snort node will need — `{ cookie = 0xAB, post_action = NAT, out_sa_index = <the tunnel SA> }` — into `opaque2` (after the ACL tag, which stays at offset 0), and
- calls `vnet_feature_next()` to let the arc **continue** naturally to Snort.

> 📝 **opaque2 now:** `[SNORT_NAT_IPSEC][cookie 0xAB][post=NAT][sa=#]`

**Step 4 — `snort-ip4-input`.** The packet is handed to the Snort IPS for deep inspection (the *how* — shared memory and the DAQ — is [Module 05]({{ '/learning/data-plane/ngfw/ips-integration/' | relative_url }})). Snort scans the payload against its signatures and renders a **verdict**. Two outcomes:

- **PASS** → the packet continues down the arc to the next feature.
- **DROP** → the packet is sent straight to `error-drop` and **never comes back** to our nodes. (This is correct IPS behavior — a malicious packet is gone.)

Our packet is clean, so: **PASS**.

**Step 5 — `ngfw-post-snort`.** Registered `runs_after` Snort, this node runs only for survivors. It checks the **cookie**: is `opaque2` carrying our `0xAB` marker? Yes — so this is a packet *we* tagged. It reads `post_action = NAT`, steers the packet toward the NAT node, and **consumes the cookie** (sets it to 0) so nothing can accidentally reprocess it.

> 📝 **opaque2 now:** cookie cleared — the note has done its job.

**Step 6 — `nat44`.** The NAT node rewrites the private source address/port to a public one and **creates a session** — a flow-table entry keyed by the 5-tuple. That session is what lets the *reply* find its way back later (stateful NAT, exactly the Gen-2 idea from [Module 01]({{ '/learning/data-plane/ngfw/first-principles/' | relative_url }})).

**Step 7 — `esp4-encrypt`.** Because the destination is across the tunnel, the packet is routed into IPsec encryption. The SA index recorded earlier tells this node **which keys** to use; it wraps the packet in ESP and encrypts the payload.

**Step 8 — Egress.** The encrypted packet leaves on the VPN-out VLAN sub-interface, headed for the tunnel peer. Journey complete.

The whole trip was: **classify → decide → inspect → act → translate → encrypt → forward**, with a tiny note ferrying the "what to do after Snort" decision across the three nodes that couldn't all run at once.

---

## The Six Possible Paths {#six-paths}

Our packet took the deepest path, but the *same* pipeline produces six different journeys depending on the ACL tag. This is the whole policy surface in one picture:

![Steering Tag to Pipeline Path]({{ '/assets/diagrams/learning/data-plane/ngfw/steering-decision-tree.svg' | relative_url }}){:class="diagram-img"}

*One ACL classification, six outcomes. The tag decides which nodes the packet visits.*

| Steering tag | Path | Meaning |
|--------------|------|---------|
| `NONE` | → `ip4-lookup` | No special handling — route normally (the default). |
| `NAT_PASS` | → `nat44` → `ip4-lookup` | Translate, then forward (e.g. straight to the internet). |
| `SNORT_NAT` | → `snort` → `nat44` → `ip4-lookup` | Inspect, translate, forward. |
| `SNORT_NAT_IPSEC` | → `snort` → `nat44` → `esp4-encrypt` | **Our example:** inspect, translate, encrypt out the tunnel. |
| `NAT_IPSEC` | → `nat44` → `esp4-encrypt` | Translate and encrypt, *without* inspection (trusted flow). |
| `DROP` | → `error-drop` | Discard immediately. |

Notice how much is **reused**: NAT, Snort, and encryption are the same nodes every time — only the *order and inclusion* change, driven by the tag. That reuse is exactly what the feature-arc + `opaque2` design buys you. Adding a seventh path is mostly a matter of defining a new tag→action mapping, not new machinery.

---

## When Things Get Dropped {#drops}

A firewall is defined as much by what it *stops* as what it passes. There are two distinct drop points on this pipeline, and it's worth knowing which is which when you're debugging:

1. **Policy drop (`ngfw-decision`, step 3).** If the matched rule's tag is `DROP`, the decision node sends the packet directly to `error-drop`. It never reaches Snort. This is a *policy* decision — "we don't allow this flow at all."
2. **Inspection drop (Snort, step 4).** If Snort's verdict is DROP, the Snort machinery routes the packet to `error-drop` before it can return to `ngfw-post-snort`. This is a *threat* decision — "this flow is allowed in principle, but this packet is malicious."

Both increment counters you can read (`show node counters`), so "was it blocked by policy or by the IPS?" is answerable at a glance — they're different counters on different nodes. There are also safety drops: e.g. if an IPsec action is selected but the SA index is missing, the post-Snort node drops rather than forward the packet **unencrypted** — a fail-closed choice.

---

## The Return Trip {#return-trip}

Traffic is a two-way street, and the reply takes a *different* path — this trips up a lot of newcomers.

When the far-side service answers, its packet arrives **encrypted** on the VPN-out interface:

1. **Inbound decrypt.** An ESP packet is recognized and sent to IPsec **decrypt**, using the inbound SA. Out comes the original reply packet.
2. **Reverse NAT.** The NAT node looks up the **session** created on the way out (step 6) and translates the public destination back to the original private inside address. Because the session already exists, this is a fast table hit — no policy re-evaluation needed.
3. **Forward inside.** A route lookup sends the reply to the inside host.

The key insight: the **outbound path sets up state** (a NAT session, the SAs), and the **inbound path rides that state**. This is stateful firewalling in action — the reply is allowed *because* the request created the context for it, not because a rule explicitly permits it. Break the outbound state and the return traffic has nowhere to land.

---

## IPv6: the Mirror World {#ipv6}

Everything above has an IPv6 twin. The platform registers **mirror nodes** — `ngfw-decision-ip6`, `ngfw-post-snort-feature-ip6` — on the **`ip6-unicast`** arc, and uses **`nat66`** and `esp6-encrypt`. The *logic* is identical; only the address structures and a few node names change. When you read the code, expect to see IPv4 and IPv6 handled as parallel paths rather than one unified path — a common and pragmatic choice in packet engines, because the header formats differ enough that merging them would cost more than it saves.

---

## How to Watch This Happen {#watch}

You don't have to take this walkthrough on faith — VPP will replay it for you. To trace our exact scenario live:

```
vpp# trace add dpdk-input 100          # capture the next 100 packets from the NIC
   ... send the connection ...
vpp# show trace                        # read each packet's node-by-node path
```

A single traced packet prints the nodes it visited and, at each custom node, the decision it recorded — the matched rule, the action, the ACL tag, the chosen next node. To see aggregate behavior instead of individual packets:

```
vpp# show node counters                # per-node: passed / dropped / to-snort / to-ipsec ...
vpp# show runtime                       # per-node clocks-per-packet — find the hot nodes
vpp# show nat44 sessions                # the flow state that lets replies home
```

When a flow misbehaves, this is the loop: `trace add`, reproduce, `show trace`, and read *which node* made *which* decision. The pipeline is glass-boxed by design.

---

## Key Takeaways {#key-takeaways}

1. The richest path — **inspect → NAT → encrypt** — visits ACL, decision, Snort, post-Snort, NAT, and ESP-encrypt nodes in order, coordinated by the `opaque2` note.
2. The **ACL tag** chosen at classification determines which of **six paths** the packet takes; the nodes themselves are reused across all of them.
3. There are **two drop points** — policy (at the decision node) and threat (at Snort) — plus fail-closed safety drops; they're distinct counters, so you can tell them apart.
4. The **outbound path builds state** (NAT session + SAs); the **return path rides it** (decrypt + reverse-NAT). That's stateful firewalling made concrete.
5. **IPv6 is a parallel mirror** — same logic, `-ip6` nodes and `nat66`.
6. The entire journey is **observable live** with `trace add` / `show trace` / `show node counters` — debug by watching, not guessing.

---

## What's Next {#whats-next}

We've treated Snort as a black box that returns a verdict. The next module opens it: how VPP hands packets to a *separate* Snort process over **shared memory and the DAQ**, and how the verdict travels back — the most intricate inter-process channel in the whole platform.

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/learning/data-plane/ngfw/vpp-data-plane/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#94a3b8;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← Module 03</a>
  <a href="{{ '/learning/data-plane/ngfw/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">NGFW Home</a>
  <a href="{{ '/learning/data-plane/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Data Plane 🏠</a>
</div>
