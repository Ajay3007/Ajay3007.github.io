---
layout: default
title: "Module 17 — Two-tier Policy Lookup"
permalink: /learning/data-plane/projects/module-17-policy-lookup/
---

# Module 17 — Two-tier Policy Lookup

> Requires **Hyperscan (libhs)**. No DPDK needed — fully runnable.

## What you learn

The complete policy decision engine: how `rte_hash` exact match (Tier 1)
and Hyperscan fallback (Tier 2) combine into the single function called
for every DNS packet in the DP application. Includes `filter_details` application,
malicious domain pre-check, multi-group evaluation, and a performance
benchmark showing why the two-tier design is essential at 2M packets/sec.

---

## Why two tiers are necessary

```text
Naive approach: scan every domain with Hyperscan
  2M DNS/sec × 5 µs/scan = 10,000 ms/sec of CPU time → bottleneck

Two-tier approach:
  90% of domains hit the hash table (exact match, ~50 ns)
  10% fall through to Hyperscan (~5 µs)

  2M × 0.90 × 50 ns   =  90 ms/sec  (Tier 1)
  2M × 0.10 × 5,000 ns = 1000 ms/sec (Tier 2)
  Total = 1090 ms/sec across 4 cores = 272 ms/core
  → comfortable headroom at 2M DNS/sec
```

---

## Where this fits in the real application

```text
Worker lcore receives DNS packet
  │
  ├─► dns_parse_message()      → domain = "blocked.example.com"
  │
  ├─► rte_hash_lookup(subscriber_table, src_ip) → subscriber_t *sub
  │     sub->group_id → which enterprise group
  │
  └─► url_policy_for_dns(domain, qtype, groups, n)
        │
        ├─► check_malicious_domain(domain)
        │     rte_hash_lookup(malicious_domain_table, domain)
        │     HIT → PROCESS_WORKFLOW (sinkhole) immediately
        │     MISS ↓
        │
        └─► fetch_url_policy_for_domain(domain, group)
              │
              ├─── Tier 1: rte_hash_lookup_data(domain_details_table, domain, &fd)
              │      HIT  → apply_filter_details(fd, group, port)
              │      MISS ↓
              │
              └─── Tier 2: hs_scan_domain_group(domain, group->database, scratch)
                     HIT  → apply_filter_details(synthesised_fd, group, port)
                     MISS → group->default_policy
```

---

## Build and run

```bash
make
./policy_lookup
```

Expected output (abbreviated):
```
=== Module 17: Two-tier Policy Lookup ===

Test 1: google.com
  Tier 1 HIT → is_whitelisted=1 → ALLOW
  Result: ALLOW      Expected: ALLOW      PASS ✓

Test 7: ads.tracker.io
  Tier 1 MISS → falling through to Hyperscan
  Tier 2 HIT (Hyperscan match, pattern_id=30)
  is_blacklisted=1 → SINKHOLE
  Result: SINKHOLE   Expected: SINKHOLE   PASS ✓

Results: 9 passed, 0 failed

Performance:
  Tier 1 (hash): ~45 ns/lookup
  Tier 2 (hash miss + Hyperscan): ~3200 ns/lookup
  Tier 1 is ~71x faster than Tier 2
```

---

## Key concepts

### 1. Decision hierarchy (most restrictive wins)

```c
apply_filter_details(fd, group, domain, port):
  1. is_whitelisted  → ALLOW  (highest priority)
  2. is_blacklisted  → SINKHOLE
  3. category check  → DROP
  4. port check      → DROP
  5. default_policy  → group-level fallback (lowest priority)
```

A whitelisted domain is always allowed even if its category is blocked.
A blacklisted domain is always blocked even if the group's default is ALLOW.

### 2. Multi-group evaluation

```c
/* Subscriber belongs to groups A and B */
for (int g = 0; g < n_groups; g++) {
    int d = fetch_url_policy_for_domain(domain, groups[g], port);
    if (d != ALLOW_PACKET)
        final_decision = d;   /* most restrictive wins */
}
```

### 3. Malicious domain check — runs before group policy

```c
if (check_malicious(domain, &ctx)) {
    /* Blocked regardless of group policy */
    return PROCESS_WORKFLOW;
}
```

The malicious table (`malicious_domain_table`) is populated
from threat intelligence feeds (URLHaus, IDPS feeds) via Kafka. It runs
**before** group policy and cannot be overridden by a whitelist.

### 4. `filter_details` fields and their meaning

| Field | Value | Effect |
|---|---|---|
| `is_whitelisted` | 1 | Always ALLOW, skip all other checks |
| `is_blacklisted` | 1 | Always SINKHOLE (DNS) or RST (TLS) |
| `category_bitmask` | `0x00000002` | Social media category |
| `category_bitmask` | `0x00000004` | Entertainment category |
| `is_port_based` | 1 | Also check `port_mask` for this domain |

### 5. PROCESS_WORKFLOW (2) vs DROP_PACKET (1)

```text
PROCESS_WORKFLOW (2): For DNS → build sinkhole response (Module 18)
                        For TLS → inject TCP RST
                        The packet is "processed" before dropping

DROP_PACKET (1):       Silently discard the packet
                        Used for category-blocked domains where
                        silent drop is preferred over sinkhole
```

The DNS sinkhole redirects the client to a walled garden IP.
Pure drops look like a network timeout to the client — appropriate
for malware/phishing where you don't want to tip off the attacker.

---

## Next module

**Module 18 — DNS Sinkhole**: When `url_policy_for_dns()`
returns `PROCESS_WORKFLOW`, the DNS query packet is rewritten in-place into
a sinkhole response.

---

## Source files

| File | Download |
|---|---|
| `policy_lookup.c` | [policy_lookup.c]({{ '/assets/code/data-plane/projects/17-policy-lookup/policy_lookup.c' | relative_url }}) |
| `Makefile` | [Makefile]({{ '/assets/code/data-plane/projects/17-policy-lookup/Makefile' | relative_url }}) |
