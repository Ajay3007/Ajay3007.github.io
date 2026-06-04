/**
 * rte_hash_crud.c — Module 12: rte_hash CRUD Operations
 *
 * rte_hash is DPDK's lock-free hash table, used throughout the DP application for
 * every O(1) policy lookup at packet rate. Understanding its API is
 * mandatory before reading any of the policy engine code.
 *
 * Hash tables in the real DP application project:
 *
 *   domain_details_table  — per-group: domain string → filter_details
 *                           Created per enterprise group.
 *                           Populated during Kafka policy sync.
 *                           Queried for EVERY DNS packet at line rate.
 *
 *   ip4_vs_subscriber_table — subscriber IPv4 → subscriber ID (separate IPv4 table)
 *   ip_vs_subscriber_table  — subscriber IPv4 → subscriber ID (500K entries)
 *   connection_track_table  — active TCP connections (2M entries)
 *   tls_session_table       — partial TLS handshakes (2M entries)
 *   domain_sig_table        — URL → Hyperscan signature ID
 *   malicious_domain_table  — malicious domain → block context
 *   category_vs_bitmask   — category string → bitmask
 *
 * All created with rte_hash_crc (CRC32 hardware instruction) as hash function.
 * All socket_id = rte_socket_id() for NUMA-local memory.
 *
 * This module covers:
 *   1. Create / destroy
 *   2. Insert (add_key_data)
 *   3. Lookup single (lookup_data) — used in the hot path
 *   4. Bulk lookup (lookup_bulk_data) — 2–3× faster via prefetching
 *   5. Delete (del_key)
 *   6. Iterate (dump all entries)
 *   7. Thread safety options
 *   8. Performance comparison: single vs bulk
 *
 * REFERENCE CODE: requires DPDK installed.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <assert.h>
#include <time.h>

#include <rte_eal.h>
#include <rte_hash.h>
#include <rte_hash_crc.h>
#include <rte_lcore.h>
#include <rte_errno.h>
#include <rte_cycles.h>
#include <rte_malloc.h>

/* ───────────────────────────────────────────────────────────
 * filter_details — mirrors policy_cache.h in the DP application
 *
 * Stored as the 'data' pointer in domain_details_table.
 * Retrieved via rte_hash_lookup_data() in the worker hot path.
 * ─────────────────────────────────────────────────────────── */
#define MAX_URL_LEN       256
#define MAX_DOMAINS       10000   /* per group */

typedef struct {
    int      is_whitelisted;      /* 1: always allow regardless of category */
    int      is_blacklisted;      /* 1: always block                        */
    int      is_domain_based;     /* 1: domain-level rule                   */
    int      is_port_based;       /* 1: also check port_mask                */
    uint32_t port_mask;           /* bitmask of blocked ports (for TLS)     */
    uint32_t category_bitmask;    /* which content categories apply         */
} filter_details_t;

/* ───────────────────────────────────────────────────────────
 * create_domain_table — mirrors add_domain_to_group() setup
 *
 * In the real app:
 *   struct rte_hash_parameters p = {
 *       .name    = "domain_details_g0",
 *       .entries = MAX_DOMAINS_PER_GROUP,
 *       .key_len = MAX_URL_LEN,
 *       .hash_func = rte_hash_crc,
 *       .socket_id = rte_socket_id(),
 *   };
 *   group->domain_details_table = rte_hash_create(&p);
 * ─────────────────────────────────────────────────────────── */
static struct rte_hash *create_domain_table(const char *name, int entries)
{
    struct rte_hash_parameters params = {
        .name       = name,
        /*
         * entries: rte_hash rounds up to the next power of 2 internally.
         * Size for worst-case load: if you expect 10000 entries, request
         * at least 10000 (DPDK will allocate ~16384 slots at 60% load factor).
         */
        .entries    = (uint32_t)entries,

        /*
         * key_len: ALL keys must be exactly this length (padded with \0 if shorter).
         * For domain strings, use MAX_URL_LEN.
         * For IP addresses, use sizeof(uint32_t) = 4.
         * For connection tuples, use sizeof(struct connection_key).
         *
         * rte_hash does NOT store the key_len in the entry — it uses a fixed
         * stride. Mixing key lengths in one table causes silent mismatches.
         */
        .key_len    = MAX_URL_LEN,

        /*
         * hash_func: rte_hash_crc uses the x86 CRC32 hardware instruction.
         * Processes 8 bytes per clock — roughly 10× faster than FNV-1a.
         * This is why all tables in the DP application use rte_hash_crc.
         */
        .hash_func  = rte_hash_crc,

        /*
         * socket_id: allocate table memory on this NUMA socket.
         * A table on socket 0 queried from a lcore on socket 1 causes
         * cross-NUMA memory accesses — ~100 ns penalty per lookup.
         * Always use rte_socket_id() or the same socket as the NIC.
         */
        .socket_id  = (int)rte_socket_id(),

        /*
         * extra_flag: HASH_EXTRA_FLAGS_RW_CONCURRENCY enables safe
         * concurrent reads and writes without RCU.
         * the DP application uses its own RCU QSBR instead (implemented in the DP core library).
         * For simpler cases, this flag is sufficient.
         */
        /* .extra_flag = RTE_HASH_EXTRA_FLAGS_RW_CONCURRENCY, */
    };

    struct rte_hash *tbl = rte_hash_create(&params);
    if (!tbl)
        fprintf(stderr, "rte_hash_create(%s) failed: %s\n",
                name, rte_strerror(rte_errno));
    return tbl;
}

/* ───────────────────────────────────────────────────────────
 * make_key — produce a fixed-length key from a domain string
 *
 * rte_hash compares exactly key_len bytes. If the real domain name
 * is shorter than MAX_URL_LEN, the trailing bytes must be zeroed —
 * otherwise the comparison sees garbage and the lookup fails.
 *
 * In the real app, domain names from DNS packets are already in a
 * stack buffer; zeroing the rest before lookup is done inline.
 * ─────────────────────────────────────────────────────────── */
static void make_key(char key[MAX_URL_LEN], const char *domain)
{
    memset(key, 0, MAX_URL_LEN);
    strncpy(key, domain, MAX_URL_LEN - 1);
}

/* ───────────────────────────────────────────────────────────
 * Demo 1: CRUD — mirrors domain policy table operations
 * ─────────────────────────────────────────────────────────── */
static void demo_crud(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 1: CRUD — domain_details_table operations\n");
    printf("══════════════════════════════════════════════\n\n");

    struct rte_hash *tbl = create_domain_table("domain_details_g0", MAX_DOMAINS);
    assert(tbl != NULL);

    /*
     * Allocate filter_details from NUMA-local hugepage memory.
     * In the real app, these live in per-group memory allocated once
     * during group initialization.
     * rte_zmalloc_socket() → zeroed allocation on the given socket.
     */
    filter_details_t *fd_blocked  = rte_zmalloc_socket("fd", sizeof(*fd_blocked),
                                                         0, rte_socket_id());
    filter_details_t *fd_allowed  = rte_zmalloc_socket("fd", sizeof(*fd_allowed),
                                                         0, rte_socket_id());
    filter_details_t *fd_port     = rte_zmalloc_socket("fd", sizeof(*fd_port),
                                                         0, rte_socket_id());
    assert(fd_blocked && fd_allowed && fd_port);

    fd_blocked->is_blacklisted   = 1;
    fd_blocked->category_bitmask = 0x00000001; /* malware category */

    fd_allowed->is_whitelisted   = 1;

    fd_port->is_port_based       = 1;
    fd_port->port_mask           = (1 << 443) | (1 << 80); /* block HTTP/HTTPS */

    /* ── INSERT ──
     *
     * rte_hash_add_key_data(tbl, key, data)
     * Returns: position (>= 0) on success
     *          -EINVAL  if key is NULL
     *          -ENOSPC  if table is full
     *
     * In the real app this is called from add_domain_to_group()
     * during Kafka policy sync (SYNC_COMPLETE message received).
     */
    char key[MAX_URL_LEN];
    int  ret;

    make_key(key, "blocked-malware.example.com");
    ret = rte_hash_add_key_data(tbl, key, fd_blocked);
    printf("[INSERT] blocked-malware.example.com → ret=%d\n", ret);
    assert(ret >= 0);

    make_key(key, "trusted-partner.corp.internal");
    ret = rte_hash_add_key_data(tbl, key, fd_allowed);
    printf("[INSERT] trusted-partner.corp.internal → ret=%d\n", ret);
    assert(ret >= 0);

    make_key(key, "restricted-site.io");
    ret = rte_hash_add_key_data(tbl, key, fd_port);
    printf("[INSERT] restricted-site.io → ret=%d\n", ret);
    assert(ret >= 0);

    printf("        table count: %u entries\n\n", rte_hash_count(tbl));

    /* ── LOOKUP ──
     *
     * rte_hash_lookup_data(tbl, key, &data)
     * Returns: position (>= 0) on HIT — data is valid
     *          -ENOENT         on MISS — data is untouched
     *
     * This is the HOT PATH — called for every DNS/TLS packet.
     * In the real app (process_hyperscan_dns_for_group):
     *
     *   struct filter_details *fd;
     *   int pos = rte_hash_lookup_data(group->domain_details_table,
     *                                   domain_key, (void **)&fd);
     *   if (pos >= 0) {
     *       // exact match: apply fd policy
     *   } else {
     *       // no exact match: fall through to Hyperscan regex scan
     *   }
     */
    filter_details_t *out = NULL;

    make_key(key, "blocked-malware.example.com");
    ret = rte_hash_lookup_data(tbl, key, (void **)&out);
    printf("[LOOKUP] blocked-malware.example.com → %s (pos=%d)\n",
           ret >= 0 ? "HIT" : "MISS", ret);
    if (ret >= 0)
        printf("         is_blacklisted=%d  category=0x%08x\n",
               out->is_blacklisted, out->category_bitmask);

    make_key(key, "google.com");  /* not in table */
    ret = rte_hash_lookup_data(tbl, key, (void **)&out);
    printf("[LOOKUP] google.com → %s (pos=%d) → fall through to Hyperscan\n",
           ret >= 0 ? "HIT" : "MISS", ret);
    assert(ret == -ENOENT);

    /* ── UPSERT — update existing entry ──
     *
     * Calling add_key_data on a key that already exists REPLACES the data.
     * Used when a Kafka policy update revises an existing domain's category.
     */
    filter_details_t *fd_updated = rte_zmalloc_socket("fd", sizeof(*fd_updated),
                                                        0, rte_socket_id());
    fd_updated->is_blacklisted   = 1;
    fd_updated->category_bitmask = 0x00000003; /* malware + phishing */

    make_key(key, "blocked-malware.example.com");
    ret = rte_hash_add_key_data(tbl, key, fd_updated);
    printf("\n[UPSERT] blocked-malware.example.com with new bitmask → ret=%d\n", ret);
    assert(ret >= 0);

    ret = rte_hash_lookup_data(tbl, key, (void **)&out);
    printf("         after upsert: category=0x%08x (was 0x1, now 0x3)\n",
           out->category_bitmask);
    assert(out->category_bitmask == 0x3);
    assert(rte_hash_count(tbl) == 3);  /* count unchanged */

    /* ── DELETE ──
     *
     * Used when a domain is removed from policy (policy revoke message).
     * Returns position >= 0 on success, -ENOENT if not found.
     * Note: rte_hash_del_key does NOT free the data pointer — the app
     * must track and free it separately.
     */
    make_key(key, "restricted-site.io");
    ret = rte_hash_del_key(tbl, key);
    printf("\n[DELETE] restricted-site.io → ret=%d\n", ret);
    assert(ret >= 0);

    ret = rte_hash_lookup_data(tbl, key, (void **)&out);
    printf("[LOOKUP] restricted-site.io after delete → %s\n",
           ret >= 0 ? "HIT (bug!)" : "MISS (correct)");
    assert(ret == -ENOENT);
    printf("         table count after delete: %u\n\n", rte_hash_count(tbl));

    rte_hash_free(tbl);
    rte_free(fd_blocked);
    rte_free(fd_allowed);
    rte_free(fd_port);
    rte_free(fd_updated);
}

/* ───────────────────────────────────────────────────────────
 * Demo 2: bulk lookup — the critical performance optimization
 *
 * At 2M DNS packets/sec, each domain lookup is a cache miss
 * (the hash table is too large to fit in L3 cache).
 * A cache miss on x86 stalls the CPU for ~100 ns waiting for DRAM.
 *
 * Bulk lookup with prefetching:
 *   - Issue N lookups at once
 *   - The CPU can pipeline N DRAM fetches simultaneously
 *   - Total time: ~100 ns (one DRAM fetch) instead of N × 100 ns
 *
 * rte_hash_lookup_bulk_data() implements this automatically.
 * In the DP application, this is used in fetch_group_url_details_for_dns().
 * ─────────────────────────────────────────────────────────── */
#define LOOKUP_BURST     32
#define PERF_ITERATIONS  1000000

static void demo_bulk_lookup(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 2: bulk lookup vs single lookup (perf)\n");
    printf("══════════════════════════════════════════════\n\n");

    struct rte_hash *tbl = create_domain_table("bulk_test", 65536);
    assert(tbl != NULL);

    /* Populate with 10000 domains */
    filter_details_t *fd_store = rte_zmalloc_socket("fds",
        sizeof(filter_details_t) * 10000, 0, rte_socket_id());
    assert(fd_store != NULL);

    char key[MAX_URL_LEN];
    for (int i = 0; i < 10000; i++) {
        snprintf(key, MAX_URL_LEN, "enterprise-domain-%d.corp.internal", i);
        /* zero-pad the rest of the key buffer */
        memset(key + strlen(key), 0, MAX_URL_LEN - strlen(key));
        fd_store[i].is_blacklisted = (i % 7 == 0) ? 1 : 0;
        rte_hash_add_key_data(tbl, key, &fd_store[i]);
    }
    printf("Populated table: %u entries\n\n", rte_hash_count(tbl));

    /* ── Single lookup benchmark ── */
    uint64_t t0 = rte_rdtsc();
    int hits_single = 0;

    for (int i = 0; i < PERF_ITERATIONS; i++) {
        snprintf(key, MAX_URL_LEN, "enterprise-domain-%d.corp.internal",
                 i % 10000);
        memset(key + strlen(key), 0, MAX_URL_LEN - strlen(key));

        filter_details_t *out = NULL;
        if (rte_hash_lookup_data(tbl, key, (void **)&out) >= 0)
            hits_single++;
    }

    uint64_t t1 = rte_rdtsc();
    double hz = rte_get_tsc_hz();
    double single_ns = ((double)(t1 - t0) / hz * 1e9) / PERF_ITERATIONS;

    printf("Single lookup: %d hits / %d  →  %.1f ns/lookup\n",
           hits_single, PERF_ITERATIONS, single_ns);

    /* ── Bulk lookup benchmark ──
     *
     * rte_hash_lookup_bulk_data(tbl, keys, n, &hit_mask, data_out):
     *   keys[]:     array of n key pointers
     *   n:          number of keys to look up
     *   hit_mask:   uint64_t bitmask, bit i set if keys[i] was found
     *   data_out[]: data pointer for each found key
     *
     * The function internally prefetches hash buckets before comparing,
     * so N DRAM fetches can overlap. This is the same technique used in
     * the Linux kernel's bulk lookup for routing tables.
     */
    uint64_t t2 = rte_rdtsc();
    int hits_bulk = 0;
    int iter_bulk = PERF_ITERATIONS / LOOKUP_BURST;

    static char key_bufs[LOOKUP_BURST][MAX_URL_LEN];
    const void *keys_ptr[LOOKUP_BURST];
    void       *data_out[LOOKUP_BURST];
    uint64_t    hit_mask;

    for (int b = 0; b < iter_bulk; b++) {
        /* Prepare a burst of keys */
        for (int j = 0; j < LOOKUP_BURST; j++) {
            int idx = (b * LOOKUP_BURST + j) % 10000;
            snprintf(key_bufs[j], MAX_URL_LEN,
                     "enterprise-domain-%d.corp.internal", idx);
            memset(key_bufs[j] + strlen(key_bufs[j]), 0,
                   MAX_URL_LEN - strlen(key_bufs[j]));
            keys_ptr[j] = key_bufs[j];
        }

        /*
         * Single call looks up all LOOKUP_BURST keys.
         * Internally prefetches bucket N+1 while comparing bucket N.
         * Result: roughly the same time as 1 single lookup for the whole burst.
         */
        rte_hash_lookup_bulk_data(tbl, keys_ptr, LOOKUP_BURST,
                                   &hit_mask, data_out);

        /* Count hits from bitmask */
        for (int j = 0; j < LOOKUP_BURST; j++)
            if (hit_mask & (1ULL << j))
                hits_bulk++;
    }

    uint64_t t3 = rte_rdtsc();
    int total_bulk = iter_bulk * LOOKUP_BURST;
    double bulk_ns = ((double)(t3 - t2) / hz * 1e9) / total_bulk;

    printf("Bulk   lookup: %d hits / %d  →  %.1f ns/lookup  (burst=%d)\n",
           hits_bulk, total_bulk, bulk_ns, LOOKUP_BURST);
    printf("Speedup: %.1fx\n\n", single_ns / bulk_ns);
    printf("At 2M DNS/sec: single=%.0f ms/sec overhead, bulk=%.0f ms/sec\n\n",
           single_ns * 2e6 / 1e6,
           bulk_ns   * 2e6 / 1e6);

    rte_hash_free(tbl);
    rte_free(fd_store);
}

/* ───────────────────────────────────────────────────────────
 * Demo 3: iterate — dump all entries (OAM / diagnostics)
 *
 * Used in the real app when an operator requests a dump of all
 * active policies for a group, or when logging group state after
 * a Kafka policy sync completes.
 * ─────────────────────────────────────────────────────────── */
static void demo_iterate(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 3: iterate all entries\n");
    printf("══════════════════════════════════════════════\n\n");

    struct rte_hash *tbl = create_domain_table("iter_test", 64);
    assert(tbl != NULL);

    /* Insert a handful of policies */
    const char *domains[] = {
        "news.example.com", "social.example.com",
        "banking.example.com", "games.example.com"
    };
    filter_details_t fds[4] = {
        {0, 0, 0, 0, 0, 0x01}, /* news: category 1 */
        {0, 1, 0, 0, 0, 0x02}, /* social: blocked */
        {1, 0, 0, 0, 0, 0x04}, /* banking: whitelisted */
        {0, 1, 0, 0, 0, 0x08}, /* games: blocked */
    };

    char key[MAX_URL_LEN];
    for (int i = 0; i < 4; i++) {
        make_key(key, domains[i]);
        rte_hash_add_key_data(tbl, key, &fds[i]);
    }

    printf("All policies in group (count=%u):\n", rte_hash_count(tbl));

    /*
     * rte_hash_iterate(tbl, &key, &data, &next):
     *   key:  receives pointer to the stored key bytes
     *   data: receives the stored data pointer
     *   next: iterator position (start with 0, advances each call)
     *   Returns: entry position >= 0 while entries remain, -ENOENT when done
     *
     * NOT safe to call concurrently with add/del without locking.
     * In the real app, iterate is only called from the main lcore
     * during a stats dump (not from worker lcores).
     */
    uint32_t    iter_pos = 0;
    const void *iter_key;
    void       *iter_data;

    while (rte_hash_iterate(tbl, &iter_key, &iter_data, &iter_pos) >= 0) {
        filter_details_t *fd = (filter_details_t *)iter_data;
        printf("  domain=%-30s  blacklisted=%d  whitelisted=%d  cat=0x%02x\n",
               (const char *)iter_key,
               fd->is_blacklisted,
               fd->is_whitelisted,
               fd->category_bitmask);
    }

    printf("\n");
    rte_hash_free(tbl);
}

/* ───────────────────────────────────────────────────────────
 * Demo 4: integer key — mirrors ip_vs_subscriber_table
 *
 * Not all rte_hash tables use string keys. The subscriber IP table
 * maps uint32_t (IPv4 address) → subscriber struct.
 * key_len = sizeof(uint32_t) = 4 bytes.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    char subscriber_id[32];   /* subscriber identifier */
    uint32_t group_id;
} subscriber_t;

static void demo_integer_key(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 4: integer key — ip_vs_subscriber_table pattern\n");
    printf("══════════════════════════════════════════════\n\n");

    struct rte_hash_parameters params = {
        .name      = "ip_vs_subscriber",
        .entries   = 524288,       /* 500K subscribers */
        .key_len   = sizeof(uint32_t),
        .hash_func = rte_hash_crc,
        .socket_id = (int)rte_socket_id(),
    };
    struct rte_hash *tbl = rte_hash_create(&params);
    assert(tbl != NULL);

    subscriber_t sub1 = { .subscriber_id = "subscriber-12345678", .group_id = 42 };
    subscriber_t sub2 = { .subscriber_id = "subscriber-98765432", .group_id = 99 };

    /* Key is the subscriber's IP address (network byte order) */
    uint32_t ip1 = 0xC0A80164;  /* 198.51.100.5 */
    uint32_t ip2 = 0x0A000001;  /* 10.0.0.1 */

    rte_hash_add_key_data(tbl, &ip1, &sub1);
    rte_hash_add_key_data(tbl, &ip2, &sub2);

    /*
     * In the real app, for every incoming packet:
     *   uint32_t src_ip = ip4->src_ip;  (already network byte order)
     *   subscriber_t *sub;
     *   if (rte_hash_lookup_data(subscriber_table, &src_ip, (void **)&sub) >= 0) {
     *       // found subscriber: get group_id for policy lookup
     *       group = get_group(sub->group_id);
     *   }
     */
    subscriber_t *out;
    uint32_t lookup_ip = 0xC0A80164;
    int ret = rte_hash_lookup_data(tbl, &lookup_ip, (void **)&out);
    printf("Lookup 198.51.100.5 → %s  group=%u\n",
           ret >= 0 ? out->subscriber_id : "NOT FOUND",
           ret >= 0 ? out->group_id : 0);
    assert(ret >= 0);
    assert(out->group_id == 42);

    lookup_ip = 0xDEADBEEF;  /* unknown subscriber */
    ret = rte_hash_lookup_data(tbl, &lookup_ip, (void **)&out);
    printf("Lookup 222.173.190.239 → %s\n",
           ret >= 0 ? out->subscriber_id : "NOT FOUND (no group policy)");
    assert(ret == -ENOENT);

    printf("\n");
    rte_hash_free(tbl);
}

/* ─── Minimal EAL args ──────────────────────────────────── */
static const char *eal_args[] = {
    "rte_hash_crud", "-l", "0", "--socket-mem", "256",
    "-n", "4", "--proc-type", "auto", "--no-pci",
};

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    printf("=== Module 12: rte_hash CRUD ===\n\n");

    int ret = rte_eal_init(
        (int)(sizeof(eal_args) / sizeof(eal_args[0])),
        (char **)(uintptr_t)eal_args);
    if (ret < 0)
        rte_exit(EXIT_FAILURE, "rte_eal_init: %s\n", rte_strerror(rte_errno));

    demo_crud();
    demo_bulk_lookup();
    demo_iterate();
    demo_integer_key();

    printf("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n");
    printf("rte_hash API quick-reference:\n\n");
    printf("  rte_hash_create(&params)               → create table\n");
    printf("  rte_hash_free(tbl)                     → destroy table\n");
    printf("  rte_hash_add_key_data(tbl, key, data)  → insert/upsert\n");
    printf("  rte_hash_lookup_data(tbl, key, &data)  → single lookup (hot path)\n");
    printf("  rte_hash_lookup_bulk_data(tbl, keys,   → bulk lookup (2–3× faster)\n");
    printf("       n, &hit_mask, data_out)\n");
    printf("  rte_hash_del_key(tbl, key)             → delete\n");
    printf("  rte_hash_iterate(tbl, &k, &d, &next)   → iterate all\n");
    printf("  rte_hash_count(tbl)                    → entry count\n");
    printf("  rte_hash_crc                           → use as hash_func always\n");
    printf("\n");
    printf("  key_len rule: ALL keys must be exactly params.key_len bytes\n");
    printf("                → memset(key, 0, MAX_URL_LEN) before strncpy()\n");

    rte_eal_cleanup();
    return 0;
}
