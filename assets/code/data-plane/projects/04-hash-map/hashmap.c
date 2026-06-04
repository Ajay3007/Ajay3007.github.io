/**
 * hashmap.c — Module 04: Hash Map (open addressing, linear probing)
 *
 * Implements an open-addressing hash map with:
 *   - FNV-1a hash function   (rte_hash uses CRC32 hardware instruction)
 *   - Linear probing         (rte_hash uses cuckoo hashing)
 *   - Tombstone deletion     (rte_hash uses a free-list approach)
 *   - Power-of-2 capacity    (same as rte_hash)
 *   - Arbitrary-length keys  (same as rte_hash)
 *
 * The demo at the bottom mirrors the real DP application policy lookup:
 *   domain string → filter_details (whitelist / blacklist / port mask)
 *
 * This is exactly what domain_details_table does in every group_struct —
 * populated during policy sync from Kafka, queried for every DNS packet.
 */

#include "hashmap.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <time.h>
#include <stdint.h>
#include <inttypes.h>

/* ───────────────────────────────────────────────────────────
 * FNV-1a hash function
 *
 * Fast, simple, good distribution for string keys.
 * FNV-1a is the "good enough" choice for non-performance-critical paths.
 *
 * rte_hash uses CRC32 via the x86 hardware instruction:
 *   rte_hash_crc(key, key_len, init_val)
 * which runs in ~1 cycle per 8 bytes — roughly 10× faster than FNV-1a.
 * On a real NIC at 25 Gbps the hash is in the critical path, so the
 * hardware instruction matters. Here FNV-1a is fine for learning.
 * ─────────────────────────────────────────────────────────── */
static uint32_t fnv1a(const void *key, uint16_t len)
{
    const uint8_t *data = (const uint8_t *)key;
    uint32_t       hash = 2166136261U;   /* FNV offset basis */
    uint16_t       i;

    for (i = 0; i < len; i++) {
        hash ^= data[i];
        hash *= 16777619U;               /* FNV prime */
    }
    return hash;
}

/* ───────────────────────────────────────────────────────────
 * Internal helper — is n a power of 2?
 * ─────────────────────────────────────────────────────────── */
static int is_pow2(uint32_t n)
{
    return (n != 0) && ((n & (n - 1)) == 0);
}

/* ───────────────────────────────────────────────────────────
 * hashmap_create
 * ─────────────────────────────────────────────────────────── */
hashmap_t *hashmap_create(uint32_t capacity)
{
    hashmap_t *map;

    if (!is_pow2(capacity)) {
        fprintf(stderr, "[hashmap] capacity %u must be a power of 2\n",
                capacity);
        return NULL;
    }

    map = calloc(1, sizeof(hashmap_t));
    if (!map)
        return NULL;

    map->buckets = calloc(capacity, sizeof(hashmap_entry_t));
    if (!map->buckets) {
        free(map);
        return NULL;
    }

    map->capacity    = capacity;
    map->mask        = capacity - 1;
    map->count       = 0;
    map->max_entries = (capacity * HASHMAP_LOAD_FACTOR_PCT) / 100;

    return map;
}

/* ───────────────────────────────────────────────────────────
 * hashmap_destroy
 * ─────────────────────────────────────────────────────────── */
void hashmap_destroy(hashmap_t *map)
{
    if (!map)
        return;
    free(map->buckets);
    free(map);
}

/* ───────────────────────────────────────────────────────────
 * hashmap_add_key_data
 *
 * Probe sequence: slot = (hash + i) & mask  (linear probing)
 *
 * Linear probing has better cache behaviour than quadratic probing
 * because probe steps are sequential memory addresses. At high load
 * factors it forms "clusters" — cuckoo hashing avoids this while
 * keeping worst-case lookup at 2 probes (two hash functions).
 * ─────────────────────────────────────────────────────────── */
int hashmap_add_key_data(hashmap_t  *map,
                          const void *key,
                          uint16_t    key_len,
                          void       *data)
{
    uint32_t hash, idx, i;
    int      tombstone_idx = -1;

    if (!map || !key || key_len == 0 || key_len > HASHMAP_MAX_KEY_LEN)
        return HASHMAP_EINVAL;

    if (map->count >= map->max_entries)
        return HASHMAP_ENOSPC;

    hash = fnv1a(key, key_len);

    for (i = 0; i < map->capacity; i++) {
        idx = (hash + i) & map->mask;
        hashmap_entry_t *e = &map->buckets[idx];

        if (e->state == SLOT_EMPTY) {
            /*
             * Prefer inserting at the first tombstone we passed —
             * reusing a tombstone slot keeps probe chains shorter.
             */
            if (tombstone_idx >= 0)
                idx = (uint32_t)tombstone_idx;

            map->buckets[idx].state   = SLOT_OCCUPIED;
            map->buckets[idx].key_len = key_len;
            memcpy(map->buckets[idx].key, key, key_len);
            map->buckets[idx].data    = data;
            map->count++;
            return HASHMAP_OK;
        }

        if (e->state == SLOT_DELETED) {
            if (tombstone_idx < 0)
                tombstone_idx = (int)idx;  /* remember first tombstone */
            continue;
        }

        /* SLOT_OCCUPIED: check if this is the same key (upsert) */
        if (e->key_len == key_len && memcmp(e->key, key, key_len) == 0) {
            e->data = data;   /* update existing */
            return HASHMAP_OK;
        }

        map->n_collisions++;
    }

    return HASHMAP_ENOSPC;
}

/* ───────────────────────────────────────────────────────────
 * hashmap_lookup_data — the hot path
 *
 * Called for every packet in the policy engine. Keep it tight.
 * In the real app, this is replaced by rte_hash_lookup_data()
 * which uses CRC32 + SIMD key comparison and averages < 100 ns
 * per lookup at 500K entries.
 * ─────────────────────────────────────────────────────────── */
int hashmap_lookup_data(hashmap_t  *map,
                         const void *key,
                         uint16_t    key_len,
                         void      **data_out)
{
    uint32_t hash, idx, i;

    if (!map || !key || key_len == 0 || !data_out)
        return HASHMAP_EINVAL;

    map->n_lookups++;
    hash = fnv1a(key, key_len);

    for (i = 0; i < map->capacity; i++) {
        idx = (hash + i) & map->mask;
        hashmap_entry_t *e = &map->buckets[idx];

        if (e->state == SLOT_EMPTY)
            return HASHMAP_ENOENT;   /* probe chain ended: key not here */

        if (e->state == SLOT_DELETED)
            continue;               /* tombstone: keep probing */

        if (e->key_len == key_len && memcmp(e->key, key, key_len) == 0) {
            *data_out = e->data;
            return HASHMAP_OK;
        }

        map->n_collisions++;
    }

    return HASHMAP_ENOENT;
}

/* ───────────────────────────────────────────────────────────
 * hashmap_del_key
 *
 * Marks slot as SLOT_DELETED (tombstone) rather than SLOT_EMPTY.
 * This preserves the probe chain for other keys that hashed to
 * the same initial bucket and stepped over this slot on insert.
 *
 * Without tombstones: deleting slot A would cause lookups for
 * keys that collided with A to stop early → false ENOENT.
 * ─────────────────────────────────────────────────────────── */
int hashmap_del_key(hashmap_t  *map,
                     const void *key,
                     uint16_t    key_len)
{
    uint32_t hash, idx, i;

    if (!map || !key || key_len == 0)
        return HASHMAP_EINVAL;

    hash = fnv1a(key, key_len);

    for (i = 0; i < map->capacity; i++) {
        idx = (hash + i) & map->mask;
        hashmap_entry_t *e = &map->buckets[idx];

        if (e->state == SLOT_EMPTY)
            return HASHMAP_ENOENT;

        if (e->state == SLOT_DELETED)
            continue;

        if (e->key_len == key_len && memcmp(e->key, key, key_len) == 0) {
            e->state = SLOT_DELETED;
            map->count--;
            return HASHMAP_OK;
        }
    }

    return HASHMAP_ENOENT;
}

/* ───────────────────────────────────────────────────────────
 * hashmap_dump_stats
 * ─────────────────────────────────────────────────────────── */
void hashmap_dump_stats(const hashmap_t *map, const char *name)
{
    printf("[hashmap:%s] capacity=%u  count=%u  load=%.1f%%  "
           "lookups=%" PRIu64 "  collisions=%" PRIu64 "\n",
           name ? name : "?",
           map->capacity,
           map->count,
           (double)map->count * 100.0 / map->capacity,
           map->n_lookups,
           map->n_collisions);
}

/* ═══════════════════════════════════════════════════════════
 * Demo — mirrors the domain_details_table in the DP application
 *
 * In the real app:
 *   - group_struct has a rte_hash *domain_details_table
 *   - Populated by add_domain_to_group() during Kafka policy sync
 *   - Queried by process_dns_for_group() for every DNS packet
 *
 * Here we simulate the same flow with our hashmap_t.
 * ═══════════════════════════════════════════════════════════ */

/* Mirrors filter_details in policy_cache.h */
typedef struct {
    int      is_whitelisted;    /* 1 = allow regardless of category     */
    int      is_blacklisted;    /* 1 = block always                     */
    int      is_port_based;     /* 1 = also check port mask             */
    uint32_t port_mask;         /* bitmask of blocked ports             */
} filter_details_t;

/* ─── Test 1: basic insert + lookup ─────────────────────── */
static void test_basic(void)
{
    printf("\n--- Test 1: basic insert/lookup ---\n");

    hashmap_t *map = hashmap_create(64);
    assert(map != NULL);

    filter_details_t fd_block  = { .is_blacklisted = 1 };
    filter_details_t fd_allow  = { .is_whitelisted = 1 };
    filter_details_t fd_port   = { .is_port_based  = 1, .port_mask = 0x0050 };

    assert(hashmap_add_str(map, "blocked.com",  &fd_block) == HASHMAP_OK);
    assert(hashmap_add_str(map, "allowed.com",  &fd_allow) == HASHMAP_OK);
    assert(hashmap_add_str(map, "port-rule.com",&fd_port)  == HASHMAP_OK);

    void *out;
    assert(hashmap_lookup_str(map, "blocked.com", &out) == HASHMAP_OK);
    assert(((filter_details_t *)out)->is_blacklisted == 1);

    assert(hashmap_lookup_str(map, "allowed.com", &out) == HASHMAP_OK);
    assert(((filter_details_t *)out)->is_whitelisted == 1);

    assert(hashmap_lookup_str(map, "notfound.com", &out) == HASHMAP_ENOENT);

    printf("  PASS: insert/lookup correct\n");
    hashmap_dump_stats(map, "domain_details_table");
    hashmap_destroy(map);
}

/* ─── Test 2: delete + tombstone correctness ────────────── */
static void test_delete(void)
{
    printf("\n--- Test 2: delete + tombstone ---\n");

    hashmap_t *map = hashmap_create(8);
    assert(map != NULL);

    filter_details_t fd = { .is_blacklisted = 1 };

    /* Insert three keys that may collide (small table = high collision rate) */
    assert(hashmap_add_str(map, "a.com", &fd) == HASHMAP_OK);
    assert(hashmap_add_str(map, "b.com", &fd) == HASHMAP_OK);
    assert(hashmap_add_str(map, "c.com", &fd) == HASHMAP_OK);

    /* Delete b.com — its slot becomes a tombstone */
    assert(hashmap_del_str(map, "b.com") == HASHMAP_OK);

    /* c.com must still be findable even though b.com's slot is now
     * a tombstone in c.com's probe chain */
    void *out;
    assert(hashmap_lookup_str(map, "c.com", &out) == HASHMAP_OK);
    assert(hashmap_lookup_str(map, "b.com", &out) == HASHMAP_ENOENT);

    printf("  PASS: tombstone preserves probe chain\n");
    hashmap_destroy(map);
}

/* ─── Test 3: upsert (update existing key) ──────────────── */
static void test_upsert(void)
{
    printf("\n--- Test 3: upsert ---\n");

    hashmap_t *map = hashmap_create(16);
    filter_details_t v1 = { .is_blacklisted = 1 };
    filter_details_t v2 = { .is_whitelisted = 1 };

    /* Insert initial policy */
    assert(hashmap_add_str(map, "example.com", &v1) == HASHMAP_OK);

    void *out;
    assert(hashmap_lookup_str(map, "example.com", &out) == HASHMAP_OK);
    assert(((filter_details_t *)out)->is_blacklisted == 1);

    /* Policy update received from Kafka — overwrite same key */
    assert(hashmap_add_str(map, "example.com", &v2) == HASHMAP_OK);
    assert(hashmap_lookup_str(map, "example.com", &out) == HASHMAP_OK);
    assert(((filter_details_t *)out)->is_whitelisted == 1);
    assert(map->count == 1);   /* no duplicate entry created */

    printf("  PASS: upsert replaces value, count stays at 1\n");
    hashmap_destroy(map);
}

/* ─── Test 4: load factor enforcement ───────────────────── */
static void test_load_factor(void)
{
    printf("\n--- Test 4: load factor (ENOSPC at 75%%) ---\n");

    /* capacity=8 → max_entries = 8*75/100 = 6 */
    hashmap_t *map = hashmap_create(8);
    filter_details_t fd = {0};
    char key[32];
    int i;

    for (i = 0; i < 6; i++) {
        snprintf(key, sizeof(key), "domain%d.com", i);
        assert(hashmap_add_str(map, key, &fd) == HASHMAP_OK);
    }

    /* 7th insert should fail — table is at load limit */
    int ret = hashmap_add_str(map, "overflow.com", &fd);
    assert(ret == HASHMAP_ENOSPC);

    printf("  PASS: ENOSPC returned at %.0f%% load\n",
           (double)HASHMAP_LOAD_FACTOR_PCT);
    printf("  In real app: rte_hash returns -ENOSPC → "
           "log error + drop new domain\n");
    hashmap_dump_stats(map, "small_table");
    hashmap_destroy(map);
}

/* ─── Test 5: simulate DNS policy lookup at packet rate ─── */
static void test_policy_lookup_perf(void)
{
    printf("\n--- Test 5: DNS policy lookup simulation ---\n");

    /* 2048 entries → 1024 domains at 50%% load (comfortable) */
    hashmap_t *map = hashmap_create(2048);
    filter_details_t policies[512];
    char domain[64];
    int i;

    /* Populate: simulate policy sync from Kafka */
    printf("  Inserting 512 domain policies...\n");
    for (i = 0; i < 512; i++) {
        policies[i].is_blacklisted = (i % 3 == 0) ? 1 : 0;
        policies[i].is_whitelisted = (i % 5 == 0) ? 1 : 0;
        snprintf(domain, sizeof(domain), "enterprise-domain-%d.internal", i);
        assert(hashmap_add_str(map, domain, &policies[i]) == HASHMAP_OK);
    }

    /* Simulate: 100K DNS lookups — mix of hits and misses */
    printf("  Running 100K lookups (mix of hits and misses)...\n");
    struct timespec t0, t1;
    int hits = 0, misses = 0;
    void *out;

    clock_gettime(CLOCK_MONOTONIC, &t0);

    for (i = 0; i < 100000; i++) {
        /* alternate between known domains and unknown */
        if (i % 2 == 0)
            snprintf(domain, sizeof(domain),
                     "enterprise-domain-%d.internal", i % 512);
        else
            snprintf(domain, sizeof(domain), "unknown-%d.com", i);

        if (hashmap_lookup_str(map, domain, &out) == HASHMAP_OK)
            hits++;
        else
            misses++;
    }

    clock_gettime(CLOCK_MONOTONIC, &t1);

    double elapsed_ms = (t1.tv_sec  - t0.tv_sec)  * 1000.0 +
                        (t1.tv_nsec - t0.tv_nsec)  / 1e6;
    double ns_per_lookup = (elapsed_ms * 1e6) / 100000.0;

    printf("  hits=%d  misses=%d\n", hits, misses);
    printf("  100K lookups in %.2f ms  (%.1f ns/lookup)\n",
           elapsed_ms, ns_per_lookup);
    printf("  Note: rte_hash_lookup_data with CRC32 HW typically < 100 ns\n");

    hashmap_dump_stats(map, "domain_details_table");
    hashmap_destroy(map);
}

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    printf("=== Module 04: Hash Map ===\n");
    printf("hashmap_entry_t size: %zu bytes\n", sizeof(hashmap_entry_t));
    printf("hashmap_t size:       %zu bytes\n\n", sizeof(hashmap_t));

    test_basic();
    test_delete();
    test_upsert();
    test_load_factor();
    test_policy_lookup_perf();

    printf("\nAll tests passed.\n");

    printf("\n--- How this maps to rte_hash in the DP application ---\n");
    printf("  hashmap_create(cap)              →  rte_hash_create(&params)\n");
    printf("  hashmap_add_key_data(m,k,l,d)    →  rte_hash_add_key_data(h,k,d)\n");
    printf("  hashmap_lookup_data(m,k,l,&d)    →  rte_hash_lookup_data(h,k,&d)\n");
    printf("  hashmap_del_key(m,k,l)           →  rte_hash_del_key(h,k)\n");
    printf("  fnv1a() hash                     →  rte_hash_crc() (CRC32 HW)\n");
    printf("  linear probing                   →  cuckoo hashing (2 hash fns)\n");
    printf("  SLOT_DELETED tombstone           →  rte_hash free-list\n");

    return 0;
}
