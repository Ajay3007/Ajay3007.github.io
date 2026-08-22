---
title: "Module 12 — rte_hash CRUD"
description: "Module 12 — rte hash CRUD Reference code — requires DPDK installed."
domain: data-plane
track: dataplane-projects
order: 99
url: /learning/data-plane/projects/module-12-rte-hash/
---

# Module 12 — rte_hash CRUD

> **Reference code** — requires DPDK installed.

## What you learn

The complete `rte_hash` API — DPDK's production hash table used for every
O(1) policy lookup in the DP application. This module covers create, insert, single
lookup, bulk lookup, delete, iterate, and integer key tables, with a
performance comparison showing why bulk lookup is critical at 2M packets/sec.

---

## Hash tables in the real DP application project

| Table | Key type | Value type | Used in |
|---|---|---|---|
| `domain_details_table` | domain string (256B) | `filter_details*` | DNS/TLS policy hot path |
| `ip4_vs_subscriber_table` | `uint32_t` IPv4 | subscriber struct | subscriber resolution |
| `connection_track_table` | connection tuple | connection state | TCP tracking |
| `malicious_domain_table` | domain string | block context | malicious lookup |

All created with `rte_hash_crc` (CRC32 hardware instruction) and
`socket_id = rte_socket_id()` for NUMA-local allocation.

---

## Where this fits in the real application

```text
Kafka policy update received (main lcore):
  add_domain_to_group(group, domain, &filter_details)
    → rte_hash_add_key_data(group->domain_details_table, key, fd)

Worker lcore — DNS packet arrives:
  dns_parse_message() → domain = "blocked-malware.example.com"
  │
  ├─► rte_hash_lookup_data(domain_details_table, domain, &fd)
  │     HIT  → apply fd policy (ALLOW/DROP/SINKHOLE)
  │     MISS → hs_scan_domain_group()   (Module 16)
  │
  └─► if SINKHOLE → dns_build_sinkhole_v4()  (Module 18)

Kafka policy revoke (main lcore):
  rte_hash_del_key(group->domain_details_table, domain)
```

---

## Files

| File | Purpose |
|---|---|
| `rte_hash_crud.c` | 4 demos: CRUD, bulk vs single perf, iterate, integer key |
| `Makefile` | DPDK build |

---

## Key concepts in the code

### 1. `key_len` — the most common rte_hash bug

```c
params.key_len = MAX_URL_LEN;  /* 256 bytes */

/* WRONG: only the string bytes are valid; tail is garbage */
char key[MAX_URL_LEN];
strcpy(key, "google.com");
rte_hash_add_key_data(tbl, key, data);   /* compares all 256 bytes! */

/* CORRECT: zero the entire key buffer first */
char key[MAX_URL_LEN];
memset(key, 0, MAX_URL_LEN);
strncpy(key, "google.com", MAX_URL_LEN - 1);
rte_hash_add_key_data(tbl, key, data);
```

`rte_hash` compares exactly `key_len` bytes using CRC32. If the buffer
beyond the string content contains random stack garbage, `add` and
`lookup` will hash different values — the lookup always misses. This is
silent and extremely hard to debug.

### 2. Bulk lookup — why it matters at line rate

```text
Single lookup at 2M DNS/sec:
  Each domain is a cache miss (~100 ns for DRAM access)
  2M × 100 ns = 200 ms of CPU stall per second

Bulk lookup (LOOKUP_BURST=32):
  CPU issues all 32 DRAM prefetches simultaneously
  Total time ≈ 1 DRAM access for all 32 → 32× reduction
```

```c
/* Hot path — bulk lookup instead of single in the worker loop: */
const void *keys[BURST];
void       *data[BURST];
uint64_t    hit_mask;

rte_hash_lookup_bulk_data(tbl, keys, BURST, &hit_mask, data);

for (int i = 0; i < BURST; i++) {
    if (hit_mask & (1ULL << i)) {
        filter_details_t *fd = data[i];
        /* apply policy */
    }
}
```

### 3. `rte_hash_crc` — why always use this

```c
/* Always specify this as hash_func: */
.hash_func = rte_hash_crc,

/* NOT: */
.hash_func = rte_jhash,    /* slower: software Jenkin's hash */
.hash_func = NULL,         /* uses rte_jhash by default — still slower */
```

`rte_hash_crc` calls the x86 `CRC32` hardware instruction, processing
8 bytes per clock cycle. For a 256-byte domain key: ~32 cycles.
`rte_jhash` processes ~1 byte per cycle for 256 bytes.

### 4. NUMA socket placement

```c
.socket_id = (int)rte_socket_id(),
```

A hash table on socket 0 queried from a lcore on socket 1:
- Each lookup crosses the QPI/UPI interconnect (~100 ns extra)
- At 2M lookups/sec: 200 ms/sec wasted on NUMA penalty

### 5. Thread safety

```c
/* Option A: DPDK built-in RW concurrency (simpler): */
params.extra_flag = RTE_HASH_EXTRA_FLAGS_RW_CONCURRENCY;

/* Option B: RCU QSBR (what the DP application uses): */
/* Reader calls rte_rcu_qsbr_quiescent() in its loop */
/* Writer calls rte_rcu_qsbr_synchronize() before freeing old data */
```

---

## rte_hash API quick-reference

```c
/* Create */
struct rte_hash_parameters p = {
    .name      = "my_table",
    .entries   = 65536,
    .key_len   = MAX_URL_LEN,
    .hash_func = rte_hash_crc,
    .socket_id = rte_socket_id(),
};
struct rte_hash *tbl = rte_hash_create(&p);

/* Insert/update */
int pos = rte_hash_add_key_data(tbl, key, data_ptr);

/* Single lookup */
void *data;
int pos = rte_hash_lookup_data(tbl, key, &data);

/* Bulk lookup */
uint64_t hit_mask;
void *data_out[N];
rte_hash_lookup_bulk_data(tbl, keys, N, &hit_mask, data_out);

/* Delete */
int pos = rte_hash_del_key(tbl, key);

/* Iterate */
uint32_t iter = 0;
const void *k; void *d;
while (rte_hash_iterate(tbl, &k, &d, &iter) >= 0) { ... }

/* Count / destroy */
uint32_t n = rte_hash_count(tbl);
rte_hash_free(tbl);
```

---

## Next module

**Module 13 — Atomic Counters + Per-lcore Stats**: Per-lcore statistics
with `_Atomic` / `atomic_fetch_add` — the pattern used for all DPDK
performance counters.

---

## Source files

| File | Download |
|---|---|
| `rte_hash_crud.c` | [rte_hash_crud.c](https://github.com/Ajay3007/dataplane-learning/blob/main/12-rte-hash/rte_hash_crud.c){:target="_blank" rel="noopener noreferrer"} |
| `Makefile` | [Makefile](https://github.com/Ajay3007/dataplane-learning/blob/main/12-rte-hash/Makefile){:target="_blank" rel="noopener noreferrer"} |
