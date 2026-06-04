/**
 * hashmap.h — Module 04: Hash Map (open addressing, linear probing)
 *
 * A hash map is the core data structure for all O(1) policy lookups in
 * a dataplane application. In the DP application, rte_hash tables are used for:
 *
 *   domain_details_table    — domain string → filter_details (whitelist/blacklist)
 *   ip_vs_subscriber_table  — subscriber IP → subscriber ID mapping (500K entries)
 *   connection_track_table  — active TCP connection state  (2M entries)
 *   domain_sig_table        — domain → Hyperscan signature ID
 *   malicious_domain_table  — malicious domain → block context
 *
 * All of these use rte_hash, which is DPDK's production hash table backed
 * by cuckoo hashing and a CRC32 hardware hash function.
 *
 * This module implements the simpler open-addressing variant with linear
 * probing. Same API shape as rte_hash — same concepts, no DPDK dependency.
 * Once you understand this, rte_hash_add_key_data() / rte_hash_lookup_data()
 * are immediately clear.
 *
 * Open addressing vs. chaining:
 *   - Open addressing: collision → probe next slot in the same array
 *     (cache-friendly, everything in one allocation)
 *   - Chaining: collision → linked list off the bucket
 *     (pointer chasing → cache misses at line rate)
 *   DPDK chose cuckoo hashing (a form of open addressing with two hash
 *   functions) for the same cache-friendliness reason.
 */

#ifndef HASHMAP_H
#define HASHMAP_H

#include <stdint.h>
#include <stddef.h>

/* ───────────────────────────────────────────────────────────
 * Limits
 * ─────────────────────────────────────────────────────────── */

/*
 * Maximum key length in bytes.
 * rte_hash supports keys up to RTE_HASH_KEY_LENGTH_MAX (64 bytes by default,
 * configurable). We use 256 to accommodate full domain names (max 253 bytes).
 */
#define HASHMAP_MAX_KEY_LEN   256

/*
 * Load factor threshold: 75%.
 * Once the table is 75% full, probe chains get long and lookup degrades.
 * rte_hash uses a similar internal threshold before it starts returning
 * -ENOSPC. In practice, size your table at 2× the expected entry count.
 */
#define HASHMAP_LOAD_FACTOR_PCT  75

/* ───────────────────────────────────────────────────────────
 * Return codes — mirror rte_hash error codes
 * ─────────────────────────────────────────────────────────── */
#define HASHMAP_OK        0
#define HASHMAP_ENOENT   -1   /* key not found              */
#define HASHMAP_ENOSPC   -2   /* table full (> load factor) */
#define HASHMAP_EINVAL   -3   /* bad argument               */
#define HASHMAP_EEXIST   -4   /* key already exists         */

/* ───────────────────────────────────────────────────────────
 * Slot states
 *
 * DELETED (tombstone) is needed for correctness:
 * If we mark a deleted slot as EMPTY, a later lookup for a key
 * that had collided with the deleted slot would stop early and
 * falsely report ENOENT. The tombstone tells the probe to keep
 * scanning past this slot.
 * ─────────────────────────────────────────────────────────── */
typedef enum {
    SLOT_EMPTY    = 0,
    SLOT_OCCUPIED = 1,
    SLOT_DELETED  = 2    /* tombstone — deleted but probe must pass through */
} slot_state_t;

/* ───────────────────────────────────────────────────────────
 * hashmap_entry_t — one bucket slot
 *
 * key[] is stored inline (no pointer) so lookups touch fewer
 * cache lines. rte_hash stores keys in a separate key table
 * alongside a compact signature array for fast SIMD comparison.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    slot_state_t state;
    uint16_t     key_len;
    uint8_t      key[HASHMAP_MAX_KEY_LEN];
    void        *data;       /* user data pointer — same as rte_hash data */
} hashmap_entry_t;

/* ───────────────────────────────────────────────────────────
 * hashmap_t — the table
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    hashmap_entry_t *buckets;
    uint32_t         capacity;    /* total slots, must be power of 2 */
    uint32_t         mask;        /* capacity - 1 for fast modulo     */
    uint32_t         count;       /* current occupied entries         */
    uint32_t         max_entries; /* HASHMAP_LOAD_FACTOR_PCT% of cap  */

    /* stats — useful for sizing decisions */
    uint64_t         n_lookups;
    uint64_t         n_collisions;   /* probe steps beyond first slot */
} hashmap_t;

/* ─── Public API ─────────────────────────────────────────── */

/**
 * hashmap_create — allocate a hash table with 'capacity' slots.
 *
 * 'capacity' must be a power of 2.
 * Rule of thumb: set capacity = 2 × expected_max_entries.
 *
 * Real app equivalent:
 *   struct rte_hash_parameters params = {
 *       .name       = "domain_details",
 *       .entries    = MAX_DOMAINS_PER_GROUP,
 *       .key_len    = MAX_URL_LEN,
 *       .hash_func  = rte_hash_crc,
 *       .socket_id  = rte_socket_id(),
 *   };
 *   group->domain_details_table = rte_hash_create(&params);
 */
hashmap_t *hashmap_create(uint32_t capacity);

/**
 * hashmap_destroy — free the table.
 * Does NOT free the data pointers stored in the table.
 */
void hashmap_destroy(hashmap_t *map);

/**
 * hashmap_add_key_data — insert or update a key→data mapping.
 *
 * If the key already exists, its data pointer is updated (upsert).
 *
 * Real app equivalent:
 *   rte_hash_add_key_data(group->domain_details_table,
 *                          domain, &filter);
 *
 * Returns HASHMAP_OK, HASHMAP_ENOSPC (table full), HASHMAP_EINVAL.
 */
int hashmap_add_key_data(hashmap_t  *map,
                          const void *key,
                          uint16_t    key_len,
                          void       *data);

/**
 * hashmap_lookup_data — find a key and return its data pointer.
 *
 * This is the hot path — called for every packet in the policy engine.
 * rte_hash_lookup_data() is the equivalent, backed by CRC32 hardware
 * instruction and SIMD key comparison for speed.
 *
 * Real app equivalent (in process_hyperscan_dns_for_group):
 *   struct filter_details *fd;
 *   ret = rte_hash_lookup_data(group->domain_details_table,
 *                               domain, (void**)&fd);
 *   if (ret >= 0)  // exact match found
 *       apply_policy(fd);
 *
 * Returns HASHMAP_OK and sets *data_out on success, HASHMAP_ENOENT if missing.
 */
int hashmap_lookup_data(hashmap_t  *map,
                         const void *key,
                         uint16_t    key_len,
                         void      **data_out);

/**
 * hashmap_del_key — remove a key from the table.
 *
 * Sets the slot to SLOT_DELETED (tombstone) so probe chains stay intact.
 *
 * Real app equivalent:
 *   rte_hash_del_key(group->domain_details_table, domain);
 *
 * Returns HASHMAP_OK or HASHMAP_ENOENT.
 */
int hashmap_del_key(hashmap_t  *map,
                     const void *key,
                     uint16_t    key_len);

/**
 * hashmap_dump_stats — print occupancy and collision statistics.
 * Used at startup and in OAM diagnostics to verify table sizing.
 */
void hashmap_dump_stats(const hashmap_t *map, const char *name);

/* Convenience wrapper for NUL-terminated string keys */
static inline int hashmap_add_str(hashmap_t *map, const char *key, void *data)
{
    return hashmap_add_key_data(map, key, (uint16_t)__builtin_strlen(key), data);
}

static inline int hashmap_lookup_str(hashmap_t *map, const char *key,
                                      void **data_out)
{
    return hashmap_lookup_data(map, key, (uint16_t)__builtin_strlen(key),
                                data_out);
}

static inline int hashmap_del_str(hashmap_t *map, const char *key)
{
    return hashmap_del_key(map, key, (uint16_t)__builtin_strlen(key));
}

#endif /* HASHMAP_H */
