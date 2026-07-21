---
layout: default
title: NGFW (Next-Generation Firewall)
permalink: /learning/data-plane/ngfw/
---

# 🛡️ NGFW — Next-Generation Firewall

A modern firewall is no longer a simple packet filter — it inspects, decrypts, translates, and forwards traffic at line rate, all at once. This track takes you from **what a firewall is** all the way to **how a real one is engineered**, using a concrete design built on the open-source **VPP** data plane, with **Snort** for intrusion prevention and **StrongSwan** for VPN. Across **eight self-contained modules** you'll follow a single packet from wire to tunnel, meet every moving part, and finish ready to read the code and make your first change — no prior firewall or data-plane experience assumed. The one idea that ties it all together: **a fast C data plane, proven engines beside it, and thin, well-defined bridges connecting everything.**

This section is the **capstone** of the Data Plane track: it assumes you have met (or are learning) the [DPDK]({{ '/learning/data-plane/dpdk/' | relative_url }}) and [VPP]({{ '/learning/data-plane/vpp/' | relative_url }}) building blocks, and shows how they combine into a complete security appliance.

> **Note on scope.** These notes describe a *generic* NGFW architecture and the open-source technologies it is built from (VPP, DPDK, Snort, StrongSwan). Addresses, product names, and vendor-specific details are illustrative only.

---

## Learning Path

| # | Module | What you'll learn |
|---|--------|-------------------|
| **01** | [**NGFW from First Principles**]({{ '/learning/data-plane/ngfw/first-principles/' | relative_url }}) | What a firewall is, the four generations, what makes one "next-gen", and the three-plane model. |
| **02** | [**Architecture Overview**]({{ '/learning/data-plane/ngfw/architecture-overview/' | relative_url }}) | The three planes of a real NGFW platform, the component inventory, the inter-process channels, and startup order. |
| **03** | [**The VPP Data Plane**]({{ '/learning/data-plane/ngfw/vpp-data-plane/' | relative_url }}) | The packet graph, vector processing, node anatomy, feature arcs, and how nodes pass decisions via buffer metadata. |
| **04** | [**Packet Walkthrough**]({{ '/learning/data-plane/ngfw/packet-walkthrough/' | relative_url }}) | One connection end to end: classify → decide → IPS → NAT → IPsec → egress, the six paths, drops, and the return trip. |
| **05** | [**IPS Integration (Snort + DAQ)**]({{ '/learning/data-plane/ngfw/ips-integration/' | relative_url }}) | Feeding a separate Snort process at line rate: shared-memory queue pairs, zero-copy descriptors, the handshake, and the verdict round-trip. |
| **06** | [**IPsec / VPN**]({{ '/learning/data-plane/ngfw/ipsec-vpn/' | relative_url }}) | The control/data split: StrongSwan IKE negotiates keys, a bridge installs SAs into VPP, and the data plane encrypts at line rate. |
| **07** | [**Management Plane**]({{ '/learning/data-plane/ngfw/management-plane/' | relative_url }}) | Turning per-packet counters into dashboards: JNI, the stats segment vs the binary API, per-feature reporters, and alarms. |
| **08** | [**Contributor's Guide**]({{ '/learning/data-plane/ngfw/contributor-guide/' | relative_url }}) | Repo layout, the build systems, running & config, the add-a-node recipe, the debugging toolkit, and the gotchas. |

---

## Prerequisite Building Blocks

<div style="display:flex; flex-wrap:wrap; gap:1rem; margin-top:1rem;">
  <a href="{{ '/learning/data-plane/dpdk/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#0a2040;color:white;border-radius:5px;text-decoration:none;">⚡ DPDK Fundamentals</a>
  <a href="{{ '/learning/data-plane/vpp/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#1a7a6e;color:white;border-radius:5px;text-decoration:none;">⚡ VPP Fundamentals</a>
  <a href="{{ '/learning/4g-5g/#ngfw-sase-alignment' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">📡 Where NGFW fits in 5G/SASE</a>
</div>

---

<div style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
  <a href="{{ '/learning/data-plane/' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#667eea;color:white;border-radius:5px;text-decoration:none;margin-right:10px;">← Back to Data Plane</a>
  <a href="{{ '/learning' | relative_url }}" style="display:inline-block;padding:10px 20px;background:#764ba2;color:white;border-radius:5px;text-decoration:none;">Learning Hub 🏠</a>
</div>
