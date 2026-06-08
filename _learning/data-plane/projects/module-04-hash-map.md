---
layout: default
title: "Module 04 — Hash Map"
permalink: /learning/data-plane/projects/module-04-hash-map/
---

# Module 04 — Hash Map

## What you learn

How to implement an open-addressing hash map in C with arbitrary-length
keys — the manual equivalent of DPDK's `rte_hash`.

In the DP application, `rte_hash` tables are the backbone of every O(1) policy
decision at packet rate. Understanding this module makes every
`rte_hash_add_key_data()` / `rte_hash_lookup_data()` call in the real
codebase immediately clear.

---

## Where this fits in the real application

```text
Kafka consumer receives policy update
  │
  ├─► add_domain_to_group(group, domain, filter_details)
  │       hashmap_add_str(group->domain_details_table, domain, &fd)
  │       rte_hash_add_key_data(...)   ← real app
  │
Worker lcore receives DNS packet
  │
  ├─► process_dns_for_group()
  │       hashmap_lookup_str(group->domain_details_table, domain, &fd)
  │       rte_hash_lookup_data(...)    ← real app
  │
  │   ret >= 0  → exact match → apply filter_details policy
  │   ret < 0   → no exact match → fall through to Hyperscan regex scan
```

Every `group_struct` in the DP application has its own `domain_details_table` —
one `rte_hash` per enterprise group, sized to that group's domain count.

---

## Files

| File | Purpose |
|---|---|
| `hashmap.h` | Struct, API, inline string-key helpers |
| `hashmap.c` | Implementation + 5 tests including policy lookup simulation |
| `Makefile` | Build rules (no external deps) |

---

## Build and run

```bash
make
./hashmap
```

Expected output:
```
=== Module 04: Hash Map ===
hashmap_entry_t size: 264 bytes
hashmap_t size:       48 bytes

--- Test 1: basic insert/lookup ---
  PASS: insert/lookup correct
  [hashmap:domain_details_table] capacity=64  count=3  load=4.7%  ...

--- Test 2: delete + tombstone ---
  PASS: tombstone preserves probe chain

--- Test 3: upsert ---
  PASS: upsert replaces value, count stays at 1

--- Test 4: load factor (ENOSPC at 75%) ---
  PASS: ENOSPC returned at 75% load

--- Test 5: DNS policy lookup simulation ---
  Inserting 512 domain policies...
  Running 100K lookups (mix of hits and misses)...
  hits=50000  misses=50000
  100K lookups in X.XX ms  (XX.X ns/lookup)
```

---

## Key concepts in the code

### 1. Power-of-2 + bitmask (same as Module 03)

```c
idx = (hash + i) & map->mask;   // instead of % capacity
```

All DPDK data structures use this pattern. The mask is set once at
creation: `mask = capacity - 1`.

### 2. Tombstone (SLOT_DELETED)

```text
Before delete:   [a.com][b.com][c.com][EMPTY]
                  ^hash=0  ^collision  ^collision

Delete b.com:    [a.com][DELETED][c.com][EMPTY]

Lookup c.com:    hash=0 → probe slot 0 (a.com, skip)
                         → probe slot 1 (DELETED, keep probing!)
                         → probe slot 2 (c.com, FOUND)
```

If we marked the deleted slot `EMPTY`, the lookup for `c.com` would
stop at slot 1 and return `ENOENT` — a **false miss**. The tombstone
tells the probe chain "keep going, something was here once".

### 3. Load factor: why 75%?

At 75% occupancy, average probe length ≈ 2.5 for linear probing.
At 90% occupancy, average probe length ≈ 5.5. Worse: it can spike to
dozens for unlucky hash distributions (clustering).

Rule of thumb for the real app:
```c
// if you expect at most 10,000 domains per group:
.entries = 16384   // next power of 2 above 10000/0.75
```

### 4. FNV-1a vs CRC32

| | FNV-1a (this module) | CRC32 HW (rte_hash) |
|---|---|---|
| Speed | ~5 ns per byte | ~1 cycle per 8 bytes |
| Distribution | Good | Excellent |
| Dependency | None | x86 `crc32` instruction |
| Use | Learning, reference | Production at 25+ Gbps |

`rte_hash_crc()` calls the hardware `CRCQ` instruction, processing
8 bytes per clock — that's why rte_hash lookup stays under 100 ns
even for 256-byte domain keys.

### 5. Open addressing vs cuckoo hashing (rte_hash)

**This module (linear probing):**
- Collision → scan forward until empty slot
- Worst case: O(n) probe length at high load
- Simple, cache-friendly

**rte_hash (cuckoo hashing):**
- Two hash functions → two candidate slots
- Collision → "kick out" existing entry, rehash it to its alternate slot
- Worst case lookup: always 2 probes (one per hash function)
- SIMD key comparison: 4 keys checked per cycle using SSE/AVX

For a learner: understand linear probing first (this module), then read
`lib/hash/rte_cuckoo_hash.c` in the DPDK source — the data structure
is the same, only the collision resolution differs.

---

## rte_hash reference (what you'll use in the real app)

```c
/* Create a table (in port_init or group init) */
struct rte_hash_parameters params = {
    .name       = "domain_details_g0",
    .entries    = 16384,
    .key_len    = MAX_URL_LEN,
    .hash_func  = rte_hash_crc,
    .socket_id  = rte_socket_id(),   /* NUMA-local memory */
};
struct rte_hash *tbl = rte_hash_create(&params);

/* Insert (during Kafka policy sync) */
rte_hash_add_key_data(tbl, domain, (void *)&filter);

/* Lookup (hot path — every DNS packet) */
struct filter_details *fd;
int ret = rte_hash_lookup_data(tbl, domain, (void **)&fd);
if (ret >= 0) {
    /* exact match: apply fd->is_blacklisted / is_whitelisted */
} else {
    /* fall through to Hyperscan regex scan */
}

/* Delete (during policy revoke) */
rte_hash_del_key(tbl, domain);
```

---

## Next module

**Module 05 — Packet Structs**: Define Ethernet, IPv4, IPv6, UDP, TCP header
structs in C and parse raw bytes into them — the same structs used in
`pkt_proc.h` for every packet that enters the pipeline.

---

## Source files

| File | Download |
|---|---|
| `hashmap.h` | [hashmap.h](https://github.com/Ajay3007/dataplane-learning/blob/main/04-hash-map/hashmap.h){:target="_blank" rel="noopener noreferrer"} |
| `hashmap.c` | [hashmap.c](https://github.com/Ajay3007/dataplane-learning/blob/main/04-hash-map/hashmap.c){:target="_blank" rel="noopener noreferrer"} |
| `Makefile` | [Makefile](https://github.com/Ajay3007/dataplane-learning/blob/main/04-hash-map/Makefile){:target="_blank" rel="noopener noreferrer"} |
