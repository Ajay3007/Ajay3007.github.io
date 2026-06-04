---
layout: default
title: "Module 16 — Hyperscan: Scratch Management + Scanning"
permalink: /learning/data-plane/projects/module-16-hyperscan-scan/
---

# Module 16 — Hyperscan: Scratch Management + Scanning

> Requires **Hyperscan (libhs)** installed (see Module 15 setup).

## What you learn

Scratch space allocation, per-lcore cloning, the `hs_scan()` call, and
the `onMatch` callback — the complete scan pipeline from `domain_scan.c`.
Includes exact reimplementations of `hs_alloc_db_scratch()`,
`hs_clone_scratch_for_lcore()`, `hs_scan_payload()`, `hs_scan_domain_group()`,
`on_hs_match`, and `on_hs_match_group`.

---

## The scan pipeline in the DP application

```text
Startup:
  domainsPatternDB compiled (Module 15)
  global_scratch = hs_alloc_scratch(domainsPatternDB)
  for each worker lcore:
      worker_scratch[i] = hs_clone_scratch(global_scratch)
      hs_alloc_scratch(group->database, &worker_scratch[i])  ← grow for group DB

Runtime — per DNS packet:
  dns_parse_message() → domain extracted
  ├─► rte_hash_lookup_data(domain_details_table, domain, &fd)
  │     HIT → apply policy (Module 12)
  │     MISS ↓
  └─► hs_scan_domain_group(domain, group->database, worker_scratch, &matchCtx)
        on_hs_match_group fires → matchCtx.id set

Runtime — per TLS/HTTP packet:
  hs_scan_payload(payload, len, worker_scratch, &matchCtx)
    on_hs_match fires:
      id=1 → read SNI at matchCtx.payload + from + 7 / +9
      id=3 → extract domain from "Host: " match
```

---

## Files

| File | Purpose |
|---|---|
| `hs_scan.c` | Full scan pipeline: scratch, cloning, `hs_scan`, callbacks, 4 demos |
| `Makefile` | Links with `-lhs -lpthread` |

---

## Build and run

```bash
make
./hs_scan
```

Expected output:
```
=== Module 16: Hyperscan Scratch + Scan ===

Demo 1: TLS SNI extraction
  matched_id = 1 (HS_PATTERN_ID_TLS=1)
  extractedDomain = "www.secure-corp.example"
  PASS

Demo 2: HTTP Host header extraction
  matched_id = 3 (HS_PATTERN_ID_HTTP_DOMAIN=3)
  extractedDomain = "blocked-shopping.example.com"
  PASS

Demo 3: Per-group domain scan
  domain="ads.doubleclick.net"  hit=1  PASS → BLOCKED
  domain="google.com"           hit=0  PASS → ALLOW
  domain="TRACKER.ADNXS.COM"    hit=1  PASS → BLOCKED (CASELESS)

Demo 4: Thread safety
  4 threads × 1000 scans = 4000 total
  Successful scans: 4000
  PASS
```

---

## Key concepts

### 1. Scratch is not thread-safe — the most critical rule

```c
/* WRONG: two lcores sharing one scratch */
hs_scan(db, data1, len1, 0, global_scratch, cb, &ctx1);  /* lcore 3 */
hs_scan(db, data2, len2, 0, global_scratch, cb, &ctx2);  /* lcore 4 — CRASH */
/* Returns: HS_SCRATCH_IN_USE (-9) */

/* CORRECT: each lcore has its own clone */
hs_clone_scratch(global_scratch, &lcore3_scratch);
hs_clone_scratch(global_scratch, &lcore4_scratch);

hs_scan(db, data1, len1, 0, lcore3_scratch, cb, &ctx1);  /* safe */
hs_scan(db, data2, len2, 0, lcore4_scratch, cb, &ctx2);  /* safe */
```

In the DP application, each `worker_lcore_info` has its own `worker_scratch` field.
The scratch is cloned during startup by `hs_clone_scratch_for_lcore()` and never
shared between lcores.

### 2. `hs_alloc_scratch` can grow an existing scratch

```c
/* After compiling domainsPatternDB: */
hs_alloc_scratch(domainsPatternDB, &scratch);    /* allocates new scratch */

/* After compiling group->database: */
hs_alloc_scratch(group->database, &scratch);     /* GROWS scratch if needed */
/* The same scratch can now be used with BOTH databases */
```

In the DP application, `hs_scratch_compile_for_group()` calls `hs_alloc_scratch`
with each group's database on the existing per-lcore scratch to grow it.

### 3. The `onMatch` callback — return value semantics

```c
static int on_hs_match(unsigned int id, unsigned long long from,
                      unsigned long long to, unsigned int flags, void *ctx)
{
    /* Process the match... */
    return 0;    /* 0: continue scanning */
    /* return 1; → HS_SCAN_TERMINATED: stop now */
}
```

Always treat `HS_SCAN_TERMINATED` the same as `HS_SUCCESS` in the caller:

```c
hs_error_t err = hs_scan(...);
if (err != HS_SUCCESS && err != HS_SCAN_TERMINATED)
    return -1;  /* actual error */
```

### 4. The `from`/`to` offsets and SNI extraction

```text
Hyperscan match for pattern 1 (TLS SNI ext type 0x00 0x00...):
  from = offset of 0x00 0x00 bytes in the payload

SNI extension layout at 'from':
  from+0, from+1 : 0x00 0x00 (extension type = server_name)
  from+2, from+3 : extension data length
  from+4, from+5 : server name list length
  from+6         : name type (0x00 = host_name)
  from+7, from+8 : name length  ← read_u16_be(payload + from + 7)
  from+9 ...     : name bytes   ← copy payload + from + 9
```

### 5. `onMatch_count` — detect multiple pattern fires

```c
struct dp_match_context ctx;
hs_scan_payload(payload, len, scratch, &ctx);

if (ctx.onMatch_count == 0)
    /* no patterns matched */
else if (ctx.onMatch_count == 1)
    /* exactly one match — typical with HS_FLAG_SINGLEMATCH */
else
    /* multiple patterns matched (different IDs) */
```

With `HS_FLAG_SINGLEMATCH` set on every pattern, each pattern fires at
most once per scan. The DP application checks this to handle the case where both
a TLS match (id=1) and an HTTP match (id=3) fire on the same payload.

### 6. `hs_scan_domain_group` return value

```c
int ret = hs_scan_domain_group(domain, group->database, scratch, &matchCtx);
/* ret = matchCtx.id / 10  (DP application convention) */
/* ret = 0: no match → ALLOW */
/* ret > 0: matched → domain ID / 10 */
```

The `/10` convention exists in the real codebase to convert pattern IDs
(which are multiples of 10 in the group DB: `ids[i] = (i+1) * 10`) back
to a simpler 0-based signature index used in the policy decision.

---

## Module 15 + 16 together: the full Hyperscan pipeline

```text
Module 15 (compile):
  hs_create_db() → hs_database_t *db
  parseFile() + hs_compile_multi() → domainsPatternDB
  hs_compile_lit_multi() → group->database

Module 16 (scratch + scan):
  hs_init_global_scratch() → global_scratch
  hs_clone_scratch_for_lcore() → per-lcore worker_scratch
  hs_scan_payload() → on_hs_match → SNI / Host extracted
  hs_scan_domain_group() → on_hs_match_group → domain match
```

---

## Next module

**Module 17 — Two-tier Policy Lookup**: The complete policy engine that
combines `rte_hash` exact match (Module 12) with Hyperscan fallback
(Modules 15–16) into the single `url_policy_for_dns()` function — the
hot path called for every DNS packet in the DP application.

---

## Source files

| File | Download |
|---|---|
| `hs_scan.c` | [hs_scan.c]({{ '/assets/code/data-plane/projects/16-hyperscan-scan/hs_scan.c' | relative_url }}) |
| `Makefile` | [Makefile]({{ '/assets/code/data-plane/projects/16-hyperscan-scan/Makefile' | relative_url }}) |
