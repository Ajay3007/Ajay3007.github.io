/**
 * policy_lookup.c — Module 17: Two-tier Policy Lookup
 *
 * The policy engine is the core of the DP application. For every DNS query, it must
 * decide: ALLOW / DROP / SINKHOLE — in under 1 microsecond.
 *
 * Two-tier design:
 *
 *   Tier 1 — rte_hash exact match (O(1), ~10–50 ns):
 *     rte_hash_lookup_data(group->domain_details_table, domain, &fd)
 *     Handles: exact domain entries loaded from Kafka policy sync.
 *     Example: "google.com" → whitelisted; "malware.ru" → blacklisted.
 *
 *   Tier 2 — Hyperscan regex/literal scan (~1–10 µs):
 *     hs_scan_dp_process_group(domain, group->database, scratch, &ctx)
 *     Fallback when hash lookup misses.
 *     Handles: wildcard domains ("*.tracker.io"), pattern rules.
 *     Example: domain ending in ".phishing.tk" matches ".*\\.phishing\\.tk$".
 *
 * Why two tiers?
 *   - 80–90% of DNS queries hit exact-match domains (CDNs, popular sites)
 *   - Hash lookup is ~10 ns: 2M/sec × 10 ns = 20 ms/sec overhead (trivial)
 *   - Hyperscan is ~3–5 µs: if every query needed it, 2M/sec × 5 µs = 10 sec/sec (impossible!)
 *   - The two-tier approach means Hyperscan only runs for the ~10–20% miss cases
 *
 * In the real the DP application project (policy_cache.c):
 *   url_policy_for_dns()  → entry point per DNS packet
 *   fetch_url_policy_for_domain()   → per-group exact match + HS fallback
 *   check_malicious_domain() → malicious domain table check
 *
 * This module is compilable with Hyperscan only (no DPDK).
 * For the rte_hash equivalents, see Module 12.
 * Makefile: gcc ... -lhs -lpthread
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <assert.h>
#include <time.h>
#include <ctype.h>

#include <hs.h>

/* ───────────────────────────────────────────────────────────
 * Policy decision codes — mirrors policy_cache.h exactly
 * ─────────────────────────────────────────────────────────── */
#define ALLOW_PACKET      0    /* forward packet unchanged       */
#define DROP_PACKET       1    /* drop: blacklist / category     */
#define PROCESS_WORKFLOW  2    /* sinkhole (DNS) / RST (TCP/TLS) */

/* ───────────────────────────────────────────────────────────
 * filter_details — mirrors policy_cache.h exactly
 *
 * Stored as the data pointer in domain_details_table.
 * Retrieved via hash lookup or set in Hyperscan callback.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    int      is_whitelisted;      /* 1 → always ALLOW, skip category check */
    int      is_blacklisted;      /* 1 → always DROP                       */
    int      is_domain_based;     /* 1 → domain-level rule                 */
    int      is_port_based;       /* 1 → also enforce port_mask            */
    uint32_t port_mask;           /* bitmask: bit N = block port N         */
    uint32_t category_bitmask;    /* which content categories apply        */
    char     matched_domain[256]; /* which domain triggered this rule      */
} filter_details_t;

/* ───────────────────────────────────────────────────────────
 * Simple hash map (from Module 04 pattern — no DPDK required)
 * Used as a stand-in for rte_hash. In the real app, replace
 * hashmap_t with struct rte_hash * and:
 *   hashmap_add_str()    → rte_hash_add_key_data()
 *   hashmap_lookup_str() → rte_hash_lookup_data()
 * ─────────────────────────────────────────────────────────── */
#define HASHMAP_SIZE     1024
#define HASHMAP_KEY_LEN  256

typedef struct hm_entry {
    char             key[HASHMAP_KEY_LEN];
    void            *data;
    struct hm_entry *next;
} hm_entry_t;

typedef struct {
    hm_entry_t *buckets[HASHMAP_SIZE];
    int          count;
} hashmap_t;

static uint32_t hm_hash(const char *key)
{
    uint32_t h = 2166136261u;
    while (*key) { h ^= (uint8_t)*key++; h *= 16777619u; }
    return h;
}

static void hm_put(hashmap_t *m, const char *key, void *data)
{
    uint32_t idx = hm_hash(key) & (HASHMAP_SIZE - 1);
    hm_entry_t *e = calloc(1, sizeof(*e));
    strncpy(e->key, key, HASHMAP_KEY_LEN - 1);
    e->data = data;
    e->next = m->buckets[idx];
    m->buckets[idx] = e;
    m->count++;
}

static void *hm_get(hashmap_t *m, const char *key)
{
    uint32_t idx = hm_hash(key) & (HASHMAP_SIZE - 1);
    for (hm_entry_t *e = m->buckets[idx]; e; e = e->next)
        if (strcmp(e->key, key) == 0)
            return e->data;
    return NULL;
}

static void hm_free(hashmap_t *m)
{
    for (int i = 0; i < HASHMAP_SIZE; i++) {
        hm_entry_t *e = m->buckets[i];
        while (e) { hm_entry_t *n = e->next; free(e); e = n; }
    }
}

/* ───────────────────────────────────────────────────────────
 * group_struct — simplified version of group_struct in policy_cache.h
 *
 * In the real app:
 *   struct group_struct {
 *       char group_id[GROUPID_LEN];
 *       struct rte_hash *domain_details_table;  ← exact match
 *       hs_database_t   *database;              ← Hyperscan fallback
 *       struct dp_hyperscan_details *hyperscan_details;
 *       int default_policy;
 *       uint32_t blocked_categories;
 *   };
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    char              group_id[32];
    hashmap_t         domain_table;     /* replaces rte_hash *domain_details_table */
    hs_database_t    *hs_database;      /* Hyperscan fallback DB */
    hs_scratch_t     *hs_scratch;       /* per-worker scratch */
    int               default_policy;   /* ALLOW_PACKET or DROP_PACKET */
    uint32_t          blocked_categories; /* category bitmask for this group */
} group_t;

/* ───────────────────────────────────────────────────────────
 * malicious_context_struct — mirrors policy_cache.h
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    char     domain[256];
    uint32_t category;      /* e.g. MALWARE=1, PHISHING=2, C2=4 */
    int      confidence;    /* 0–100 */
} malicious_ctx_t;

/* Malicious domain table (shared across all groups) */
static hashmap_t g_malicious_table;

/* ───────────────────────────────────────────────────────────
 * Hyperscan match context for group scan
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    unsigned int id;
    int          matched;
    char         matched_pattern[256];
} group_match_ctx_t;

static int onMatchGroup(unsigned int id,
                         unsigned long long from,
                         unsigned long long to,
                         unsigned int flags, void *ctx)
{
    (void)from; (void)to; (void)flags;
    group_match_ctx_t *c = (group_match_ctx_t *)ctx;
    c->id      = id;
    c->matched = 1;
    return 0;  /* continue — find all matches */
}

/* ───────────────────────────────────────────────────────────
 * apply_filter_details — decide action from a filter_details entry
 *
 * This is the core policy logic. Called after BOTH hash lookup
 * and Hyperscan scan — both paths feed the same decision function.
 *
 * Mirrors the decision logic in fetch_url_policy_for_domain()
 * and process_hyperscan_dns_for_group() in the real project.
 * ─────────────────────────────────────────────────────────── */
static int apply_filter_details(const filter_details_t *fd,
                                 const group_t *group,
                                 const char *domain,
                                 uint16_t port)
{
    (void)domain;

    /* 1. Explicit whitelist — overrides everything */
    if (fd->is_whitelisted) {
        printf("    → is_whitelisted=1 → ALLOW\n");
        return ALLOW_PACKET;
    }

    /* 2. Explicit blacklist */
    if (fd->is_blacklisted) {
        printf("    → is_blacklisted=1 → DROP (sinkhole for DNS)\n");
        return PROCESS_WORKFLOW;   /* PROCESS_WORKFLOW = sinkhole for DNS */
    }

    /* 3. Category-based block check
     *    The group has a bitmask of blocked categories.
     *    If this domain's category overlaps, block it. */
    if (group->blocked_categories & fd->category_bitmask) {
        printf("    → category_bitmask=0x%08x & blocked=0x%08x → DROP\n",
               fd->category_bitmask, group->blocked_categories);
        return DROP_PACKET;
    }

    /* 4. Port-based block (for TLS policy — block specific ports) */
    if (fd->is_port_based && port > 0) {
        if (fd->port_mask & (1u << (port & 31u))) {
            printf("    → port %u in port_mask=0x%08x → DROP\n",
                   port, fd->port_mask);
            return DROP_PACKET;
        }
    }

    /* 5. Default group policy (allow or deny-by-default) */
    printf("    → no specific rule matched → group default_policy=%s\n",
           group->default_policy == ALLOW_PACKET ? "ALLOW" : "DROP");
    return group->default_policy;
}

/* ───────────────────────────────────────────────────────────
 * check_malicious — check domain against malicious threat feed
 *
 * Mirrors check_malicious_domain() in policy_cache.c.
 * This check runs BEFORE the group policy check.
 * If the domain is in the malicious table, it's blocked regardless
 * of group policy.
 * ─────────────────────────────────────────────────────────── */
static int check_malicious(const char *domain,
                             malicious_ctx_t **ctx_out)
{
    malicious_ctx_t *ctx = (malicious_ctx_t *)hm_get(&g_malicious_table, domain);
    if (ctx) {
        *ctx_out = ctx;
        return 1;  /* found in malicious table */
    }
    *ctx_out = NULL;
    return 0;
}

/* ───────────────────────────────────────────────────────────
 * fetch_url_policy_for_domain — per-group two-tier lookup
 *
 * Mirrors the real the DP application function exactly:
 *
 *   1. Tier 1: hash table exact match
 *      rte_hash_lookup_data(group->domain_details_table, domain, &fd)
 *
 *   2. Tier 2: Hyperscan scan (only on hash miss)
 *      hs_scan_dp_process_group(domain, group->database, scratch, &ctx)
 *
 * Returns ALLOW_PACKET, DROP_PACKET, or PROCESS_WORKFLOW.
 * ─────────────────────────────────────────────────────────── */
static int fetch_url_policy_for_domain(const char *domain,
                                            group_t *group,
                                            uint16_t port)
{
    printf("  [fetch_url_policy_for_domain]\n");
    printf("    group=%s  domain=%s\n", group->group_id, domain);

    /* ── Tier 1: exact match ── */
    filter_details_t *fd = (filter_details_t *)hm_get(&group->domain_table,
                                                        domain);
    if (fd) {
        printf("    Tier 1 HIT (hash exact match) → applying filter_details\n");
        return apply_filter_details(fd, group, domain, port);
    }

    printf("    Tier 1 MISS → falling through to Hyperscan scan\n");

    /* ── Tier 2: Hyperscan fallback ── */
    if (!group->hs_database) {
        printf("    No Hyperscan DB for this group → group default\n");
        return group->default_policy;
    }

    group_match_ctx_t match_ctx = {0};
    hs_error_t err = hs_scan(
        group->hs_database,
        domain,
        (unsigned int)strlen(domain),
        0,
        group->hs_scratch,
        onMatchGroup,
        &match_ctx
    );

    if (err != HS_SUCCESS && err != HS_SCAN_TERMINATED) {
        printf("    Hyperscan scan error: %d\n", err);
        return group->default_policy;
    }

    if (match_ctx.matched) {
        printf("    Tier 2 HIT (Hyperscan match, pattern_id=%u)\n",
               match_ctx.id);
        /*
         * In the real app, the Hyperscan match ID maps to a filter_details
         * entry via get_or_create_domain_details() or a direct policy table.
         * Here we synthesise a block decision for matched patterns.
         */
        filter_details_t hs_fd = {
            .is_blacklisted   = 1,
            .category_bitmask = 0x00000002,  /* social/blocked category */
        };
        return apply_filter_details(&hs_fd, group, domain, port);
    }

    printf("    Tier 2 MISS → group default_policy=%s\n",
           group->default_policy == ALLOW_PACKET ? "ALLOW" : "DROP");
    return group->default_policy;
}

/* ───────────────────────────────────────────────────────────
 * url_policy_for_dns — main entry point
 *
 * Mirrors the real the DP application function.
 *
 * Called for EVERY DNS query after domain extraction.
 * Steps:
 *   1. Check malicious domain table (IDPS threat feed)
 *   2. For each group the subscriber belongs to: fetch_group_url_details
 *   3. If any group blocks: DROP or SINKHOLE
 *   4. If all groups allow: ALLOW
 * ─────────────────────────────────────────────────────────── */
static int url_policy_for_dns(const char *domain,
                                             int qtype,  /* DNS_TYPE_A=1 or AAAA=28 */
                                             group_t **groups,
                                             int n_groups,
                                             uint16_t port)
{
    printf("\n[url_policy_for_dns]\n");
    printf("  domain=%s  qtype=%s  groups=%d\n",
           domain, qtype == 1 ? "A" : "AAAA", n_groups);

    /* ── Step 1: malicious domain check (runs before group policy) ── */
    malicious_ctx_t *mal_ctx = NULL;
    if (check_malicious(domain, &mal_ctx)) {
        printf("  MALICIOUS domain: category=0x%08x  confidence=%d%%\n",
               mal_ctx->category, mal_ctx->confidence);
        printf("  Decision: PROCESS_WORKFLOW (sinkhole DNS → walled garden IP)\n");
        return PROCESS_WORKFLOW;
    }

    /* ── Step 2: per-group policy lookup ── */
    int final_decision = ALLOW_PACKET;

    for (int g = 0; g < n_groups; g++) {
        int decision = fetch_url_policy_for_domain(domain,
                                                        groups[g], port);
        printf("  Group [%s] decision: %s\n",
               groups[g]->group_id,
               decision == ALLOW_PACKET     ? "ALLOW"    :
               decision == DROP_PACKET      ? "DROP"     :
               decision == PROCESS_WORKFLOW ? "SINKHOLE" : "?");

        /* Most restrictive wins: DROP/SINKHOLE overrides ALLOW */
        if (decision != ALLOW_PACKET)
            final_decision = decision;
    }

    printf("  Final decision: %s\n",
           final_decision == ALLOW_PACKET     ? "ALLOW"    :
           final_decision == DROP_PACKET      ? "DROP"     :
           final_decision == PROCESS_WORKFLOW ? "SINKHOLE (DNS redirect)" : "?");
    return final_decision;
}

/* ───────────────────────────────────────────────────────────
 * Setup helpers
 * ─────────────────────────────────────────────────────────── */
static group_t *create_group(const char *id, int default_policy,
                               uint32_t blocked_categories)
{
    group_t *g = calloc(1, sizeof(*g));
    strncpy(g->group_id, id, sizeof(g->group_id) - 1);
    g->default_policy      = default_policy;
    g->blocked_categories  = blocked_categories;
    return g;
}

/* Add a domain policy entry to a group's hash table */
static void add_domain_policy(group_t *g, const char *domain,
                               int is_white, int is_black,
                               uint32_t category)
{
    filter_details_t *fd = calloc(1, sizeof(*fd));
    fd->is_whitelisted   = is_white;
    fd->is_blacklisted   = is_black;
    fd->is_domain_based  = 1;
    fd->category_bitmask = category;
    strncpy(fd->matched_domain, domain, sizeof(fd->matched_domain) - 1);

    /* Lowercase the key (mirrors dns_normalize_name in Module 06) */
    char key[256];
    strncpy(key, domain, sizeof(key) - 1);
    for (char *p = key; *p; p++) *p = (char)tolower(*p);

    hm_put(&g->domain_table, key, fd);
}

/* Compile Hyperscan DB for wildcard/regex patterns in a group */
static void compile_group_hs(group_t *g,
                               const char **patterns,
                               const unsigned *ids,
                               unsigned n)
{
    char   **pats  = malloc(n * sizeof(char *));
    unsigned *flags = malloc(n * sizeof(unsigned));
    size_t   *lens  = malloc(n * sizeof(size_t));

    for (unsigned i = 0; i < n; i++) {
        pats[i]  = (char *)patterns[i];
        flags[i] = HS_FLAG_CASELESS | HS_FLAG_SINGLEMATCH;
        lens[i]  = strlen(patterns[i]);
    }

    hs_compile_error_t *err = NULL;
    hs_error_t r = hs_compile_lit_multi(
        (const char *const *)pats, flags, ids, lens, n,
        HS_MODE_BLOCK, NULL, &g->hs_database, &err);

    if (r != HS_SUCCESS) {
        if (err) { fprintf(stderr, "HS compile error: %s\n", err->message);
                   hs_free_compile_error(err); }
    } else {
        hs_alloc_scratch(g->hs_database, &g->hs_scratch);
    }

    free(pats); free(flags); free(lens);
}

static void destroy_group(group_t *g)
{
    /* Free all filter_details in the hash table */
    for (int i = 0; i < HASHMAP_SIZE; i++) {
        for (hm_entry_t *e = g->domain_table.buckets[i]; e; e = e->next)
            free(e->data);
    }
    hm_free(&g->domain_table);
    if (g->hs_scratch)  hs_free_scratch(g->hs_scratch);
    if (g->hs_database) hs_free_database(g->hs_database);
    free(g);
}

/* ═══════════════════════════════════════════════════════════
 * Demo: full policy scenario
 * ═══════════════════════════════════════════════════════════ */
static void demo_policy_scenarios(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Setting up enterprise group policies...\n");
    printf("══════════════════════════════════════════════\n\n");

    /* ── Group 1: "enterprise_a" — strict policy ──
     * default: DROP everything not explicitly allowed
     * Categories blocked: 0x00000006 (social=2, entertainment=4) */
    group_t *g1 = create_group("enterprise_a", DROP_PACKET, 0x00000006);
    add_domain_policy(g1, "google.com",     1, 0, 0);         /* whitelist */
    add_domain_policy(g1, "github.com",     1, 0, 0);         /* whitelist */
    add_domain_policy(g1, "facebook.com",   0, 1, 0x00000002);/* blacklist+social */
    add_domain_policy(g1, "youtube.com",    0, 0, 0x00000004);/* category: entertainment */
    add_domain_policy(g1, "malware-site.ru",0, 1, 0);        /* explicit blacklist */

    /* Wildcard patterns in Hyperscan DB: block all .social, .gaming TLDs */
    const char *g1_patterns[] = {
        "*.social",
        "*.games",
        "ads.tracker.io",
    };
    unsigned g1_ids[] = {10, 20, 30};
    compile_group_hs(g1, g1_patterns, g1_ids, 3);

    printf("Group [enterprise_a]:\n");
    printf("  default_policy     = DROP\n");
    printf("  blocked_categories = 0x06 (social|entertainment)\n");
    printf("  whitelisted: google.com, github.com\n");
    printf("  blacklisted: facebook.com, malware-site.ru\n");
    printf("  by category: youtube.com\n");
    printf("  by Hyperscan: *.social, *.games, ads.tracker.io\n\n");

    /* ── Group 2: "enterprise_b" — permissive policy ──
     * default: ALLOW, only specific domains blocked */
    group_t *g2 = create_group("enterprise_b", ALLOW_PACKET, 0x00000001);
    add_domain_policy(g2, "malware-site.ru", 0, 1, 0);
    add_domain_policy(g2, "phishing.com",    0, 1, 0);

    printf("Group [enterprise_b]:\n");
    printf("  default_policy = ALLOW\n");
    printf("  blacklisted: malware-site.ru, phishing.com\n\n");

    /* ── Global malicious domain table ──
     * Populated from threat intelligence feeds (URLHaus, etc.) */
    malicious_ctx_t *mal1 = calloc(1, sizeof(*mal1));
    strncpy(mal1->domain, "c2-server.badactor.net", sizeof(mal1->domain)-1);
    mal1->category   = 0x00000004;  /* C2 */
    mal1->confidence = 98;
    hm_put(&g_malicious_table, "c2-server.badactor.net", mal1);

    printf("Malicious table: c2-server.badactor.net (C2, 98%% confidence)\n\n");

    /* ── Test scenarios ── */
    group_t *groups1[] = {g1};      /* subscriber in enterprise_a only */
    group_t *groups2[] = {g2};      /* subscriber in enterprise_b only */
    group_t *groups_both[] = {g1, g2}; /* subscriber in both groups */

    struct {
        const char *domain;
        int         qtype;
        group_t   **groups;
        int         n_groups;
        int         expected;
        const char *description;
    } tests[] = {
        /* Tier 1 hits */
        {"google.com",           1, groups1,    1, ALLOW_PACKET,    "whitelisted in g1"},
        {"facebook.com",         1, groups1,    1, PROCESS_WORKFLOW,"blacklisted in g1"},
        {"youtube.com",          1, groups1,    1, DROP_PACKET,     "category blocked in g1"},
        {"malware-site.ru",      1, groups1,    1, PROCESS_WORKFLOW,"blacklisted in g1"},
        /* Default policy */
        {"unknown-site.com",     1, groups1,    1, DROP_PACKET,     "not in g1, default=DROP"},
        {"unknown-site.com",     1, groups2,    1, ALLOW_PACKET,    "not in g2, default=ALLOW"},
        /* Tier 2: Hyperscan fallback */
        {"ads.tracker.io",       1, groups1,    1, PROCESS_WORKFLOW,"Hyperscan literal match in g1"},
        /* Malicious table check (pre-group) */
        {"c2-server.badactor.net",1, groups1,   1, PROCESS_WORKFLOW,"malicious table hit"},
        /* Multi-group: most restrictive wins */
        {"facebook.com",         1, groups_both,2, PROCESS_WORKFLOW,"blacklisted in g1, allowed in g2 → g1 wins"},
    };

    int passed = 0, failed = 0;
    for (size_t i = 0; i < sizeof(tests)/sizeof(tests[0]); i++) {
        printf("────────────────────────────────────────\n");
        printf("Test %zu: %s\n  Scenario: %s\n",
               i+1, tests[i].domain, tests[i].description);

        int result = url_policy_for_dns(
            tests[i].domain, tests[i].qtype,
            tests[i].groups, tests[i].n_groups, 0);

        const char *result_str =
            result == ALLOW_PACKET     ? "ALLOW"    :
            result == DROP_PACKET      ? "DROP"     :
            result == PROCESS_WORKFLOW ? "SINKHOLE" : "?";
        const char *expected_str =
            tests[i].expected == ALLOW_PACKET     ? "ALLOW"    :
            tests[i].expected == DROP_PACKET      ? "DROP"     :
            tests[i].expected == PROCESS_WORKFLOW ? "SINKHOLE" : "?";

        int ok = (result == tests[i].expected);
        printf("\n  Result: %-10s  Expected: %-10s  %s\n",
               result_str, expected_str, ok ? "PASS ✓" : "FAIL ✗");

        if (ok) passed++; else failed++;
    }

    printf("\n════════════════════════════════════════\n");
    printf("Results: %d passed, %d failed\n\n", passed, failed);

    /* Cleanup */
    destroy_group(g1);
    destroy_group(g2);
    free(mal1);
}

/* ═══════════════════════════════════════════════════════════
 * Performance demo: exact match vs Hyperscan fallback
 * ═══════════════════════════════════════════════════════════ */
#define PERF_ITERS  500000

static void demo_performance(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Performance: Tier 1 (hash) vs Tier 2 (Hyperscan)\n");
    printf("══════════════════════════════════════════════\n\n");

    group_t *g = create_group("perf_group", ALLOW_PACKET, 0);

    /* Load 10K domains into hash table */
    char domain[256];
    for (int i = 0; i < 10000; i++) {
        snprintf(domain, sizeof(domain), "domain-%d.corp.internal", i);
        add_domain_policy(g, domain, 0, (i % 100 == 0) ? 1 : 0, 0);
    }

    /* Compile a small Hyperscan DB */
    const char *hs_pats[] = {"blocked-wildcard.example"};
    unsigned    hs_ids[]  = {1};
    compile_group_hs(g, hs_pats, hs_ids, 1);

    struct timespec t0, t1;

    /* ── Tier 1 benchmark: domains that HIT the hash table ── */
    clock_gettime(CLOCK_MONOTONIC, &t0);
    int hits = 0;
    for (int i = 0; i < PERF_ITERS; i++) {
        snprintf(domain, sizeof(domain), "domain-%d.corp.internal", i % 10000);
        if (hm_get(&g->domain_table, domain) != NULL) hits++;
    }
    clock_gettime(CLOCK_MONOTONIC, &t1);
    double hash_ns = ((t1.tv_sec  - t0.tv_sec)  * 1e9 +
                      (t1.tv_nsec - t0.tv_nsec)) / PERF_ITERS;

    /* ── Tier 2 benchmark: domains that MISS hash and hit Hyperscan ── */
    clock_gettime(CLOCK_MONOTONIC, &t0);
    int hs_hits = 0;
    for (int i = 0; i < PERF_ITERS / 10; i++) {
        snprintf(domain, sizeof(domain), "unknown-site-%d.example.com", i);
        if (hm_get(&g->domain_table, domain) == NULL && g->hs_database) {
            group_match_ctx_t ctx = {0};
            hs_scan(g->hs_database, domain, strlen(domain), 0,
                    g->hs_scratch, onMatchGroup, &ctx);
            if (ctx.matched) hs_hits++;
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &t1);
    double hs_ns = ((t1.tv_sec  - t0.tv_sec)  * 1e9 +
                    (t1.tv_nsec - t0.tv_nsec)) / (PERF_ITERS / 10);

    printf("  %d domains in hash table\n", g->domain_table.count);
    printf("\n  Tier 1 (hash exact match):\n");
    printf("    hits=%d  %.1f ns/lookup\n", hits, hash_ns);

    printf("\n  Tier 2 (hash miss + Hyperscan):\n");
    printf("    hs_hits=%d  %.1f ns/lookup\n", hs_hits, hs_ns);

    printf("\n  Tier 1 is %.1fx faster than Tier 2\n\n", hs_ns / hash_ns);
    printf("  At 2M DNS/sec:\n");
    printf("    If 90%% hit Tier 1 (%.0f ns): %.0f ms/sec overhead\n",
           hash_ns, 0.9 * 2e6 * hash_ns / 1e6);
    printf("    If 10%% need Tier 2 (%.0f ns): %.0f ms/sec overhead\n",
           hs_ns,  0.1 * 2e6 * hs_ns   / 1e6);
    printf("    Total: acceptable for 4 worker lcores\n\n");

    destroy_group(g);
}

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    printf("=== Module 17: Two-tier Policy Lookup ===\n\n");
    printf("Hyperscan version: %s\n\n", hs_version());

    memset(&g_malicious_table, 0, sizeof(g_malicious_table));

    demo_policy_scenarios();
    demo_performance();

    printf("=== All demos complete ===\n\n");

    printf("Decision code reference (policy_cache.h):\n");
    printf("  ALLOW_PACKET (0)    → forward DNS response unchanged\n");
    printf("  DROP_PACKET (1)     → silently drop\n");
    printf("  PROCESS_WORKFLOW (2)→ sinkhole (DNS) / RST inject (TLS)\n\n");

    printf("Real app call chain per DNS packet:\n");
    printf("  dns_parse_message() → domain\n");
    printf("  rte_hash_lookup(subscriber_table, src_ip) → subscriber + group_ids\n");
    printf("  url_policy_for_dns(domain, qtype, groups, n)\n");
    printf("    → check_malicious_domain()\n");
    printf("    → fetch_url_policy_for_domain() × n_groups\n");
    printf("         → rte_hash_lookup(domain_details_table)  [Tier 1]\n");
    printf("         → hs_scan_dp_process_group()             [Tier 2]\n");
    printf("         → apply_filter_details()\n");
    printf("    → ALLOW / DROP / PROCESS_WORKFLOW\n");
    printf("  if PROCESS_WORKFLOW:\n");
    printf("    dns_build_sinkhole_v4()   (Module 23)\n");

    return 0;
}
