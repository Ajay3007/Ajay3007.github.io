/**
 * hs_scan.c — Module 16: Hyperscan Scratch Management + Scanning
 *
 * This module implements the complete scan pipeline from domain_scan.c:
 *
 *   hs_alloc_db_scratch()         → allocate scratch for a database
 *   hs_clone_scratch_for_lcore()      → clone per-lcore scratch from global
 *   hs_scan_payload()        → scan packet payload, extract TLS SNI / HTTP domain
 *   hs_scan_domain_group()  → scan domain string against per-group policy DB
 *   on_hs_match                   → callback for global DB (TLS=1, HTTP=2,3,4)
 *   on_hs_match_group              → callback for group DB (domain extraction)
 *
 * These are exact reimplementations of the functions in domain_scan.c.
 *
 * Why scratch matters:
 *   hs_scan() is NOT thread-safe with respect to the scratch space.
 *   A scratch space is a temporary working buffer that Hyperscan writes
 *   into during a scan. If two threads call hs_scan() with the same scratch
 *   simultaneously, the scan is corrupted and Hyperscan returns
 *   HS_SCRATCH_IN_USE (-9).
 *
 *   Solution: one scratch per lcore (cloned from global_scratch).
 *   In the DP application, each worker lcore gets its own scratch via
 *   hs_clone_scratch_for_lcore() during startup, stored in worker_lcore_info.
 *
 * Requires: Hyperscan (libhs) installed.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <assert.h>
#include <pthread.h>

#include <hs.h>

/* ───────────────────────────────────────────────────────────
 * Pattern ID enum — mirrors domain_scan.h
 * ─────────────────────────────────────────────────────────── */
typedef enum {
    HS_PATTERN_ID_TLS         = 1,
    HS_PATTERN_ID_HTTP_IPV4   = 2,
    HS_PATTERN_ID_HTTP_DOMAIN = 3,
    HS_PATTERN_ID_HTTP_IPV6   = 4,
} hs_pattern_id_t;

/* ───────────────────────────────────────────────────────────
 * Match context structs — mirrors domain_scan.h exactly
 *
 * These are passed as the 'ctx' pointer to hs_scan().
 * The onMatch callback fills them in.
 * After hs_scan() returns, the caller reads the extracted domain.
 * ─────────────────────────────────────────────────────────── */
#define MAX_URL_LEN  256

struct dp_match_context {
    unsigned int       id;               /* ID of matched pattern          */
    unsigned long long from;             /* match start offset in payload  */
    unsigned long long to;               /* match end offset in payload    */
    const uint8_t     *payload;          /* pointer to scanned buffer      */
    uint8_t            matchedPayload[MAX_URL_LEN];
    uint8_t            extractedDomain[MAX_URL_LEN];
    unsigned int       extractedDomainLength;
    unsigned int       onMatch_count;    /* total times callback fired     */
} __attribute__((aligned(64)));

struct dp_match_context_group {
    unsigned int       id;
    unsigned long long from;
    unsigned long long to;
    uint8_t            extractedDomain[MAX_URL_LEN];
    uint8_t            matchedDomain[MAX_URL_LEN];
    unsigned int       matchedDomainLength;
    unsigned int       onMatch_count;
} __attribute__((aligned(64)));

/* ───────────────────────────────────────────────────────────
 * Global state — mirrors globals in domain_scan.c
 * ─────────────────────────────────────────────────────────── */
static hs_database_t *domainsPatternDB   = NULL;  /* global threat DB */
static hs_scratch_t  *global_scratch     = NULL;  /* global scratch   */

/* ───────────────────────────────────────────────────────────
 * read_u16_be — unaligned big-endian 16-bit read
 * Mirrors the helper used throughout pkt_proc.h and domain_scan.c.
 * ─────────────────────────────────────────────────────────── */
static inline uint16_t read_u16_be(const uint8_t *p)
{
    return (uint16_t)((p[0] << 8) | p[1]);
}

/* ───────────────────────────────────────────────────────────
 * on_hs_match — callback for global threat DB scans
 *
 * Called by Hyperscan for EVERY match found in the payload.
 * Returns 0 to continue scanning, non-zero to stop after first match.
 *
 * This is the exact logic from domain_scan.c on_hs_match:
 *
 *  id=1 (TLS): SNI extension type 0x0000 matched.
 *              Read SNI name length at from+7, copy name from from+9.
 *
 *  id=2 (HTTP_IPV4): IPv4 address in URL matched.
 *              Copy the matched bytes (from..to) as the domain.
 *
 *  id=3 (HTTP_DOMAIN): "Host: domain" matched.
 *              Extract the domain part (after "Host: ").
 *
 *  id=4 (HTTP_IPV6): IPv6 in URL — extract bracketed address.
 * ─────────────────────────────────────────────────────────── */
static int on_hs_match(unsigned int id,
                      unsigned long long from,
                      unsigned long long to,
                      unsigned int flags,
                      void *ctx)
{
    (void)flags;

    struct dp_match_context *matchCtx = (struct dp_match_context *)ctx;
    matchCtx->id           = id;
    matchCtx->from         = from;
    matchCtx->to           = to;
    matchCtx->onMatch_count++;

    const uint8_t *payload = matchCtx->payload;

    switch (id) {

    case HS_PATTERN_ID_TLS: /* 1 */
        /*
         * Hyperscan matched the TLS SNI extension type bytes (0x0000...).
         * The SNI extension layout starting at 'from':
         *
         *   from+0, from+1 : extension type = 0x00 0x00
         *   from+2, from+3 : extension data length
         *   from+4, from+5 : server name list length
         *   from+6         : server name type = 0x00 (host_name)
         *   from+7, from+8 : SERVER NAME LENGTH  ← read_u16_be here
         *   from+9 ...     : SERVER NAME BYTES   ← copy from here
         *
         * This is exactly the code in domain_scan.c on_hs_match case 1.
         * See also Module 07 (tls_extract_sni_from_match) for the
         * full explanation of this layout.
         */
        {
            uint16_t name_len = read_u16_be(payload + from + 7);
            if (name_len > 0 && name_len < MAX_URL_LEN) {
                memcpy(matchCtx->extractedDomain,
                       payload + from + 9,
                       name_len);
                matchCtx->extractedDomain[name_len] = '\0';
                matchCtx->extractedDomainLength      = name_len;
            }
        }
        break;

    case HS_PATTERN_ID_HTTP_IPV4: /* 2 */
    case HS_PATTERN_ID_HTTP_IPV6: /* 4 */
        /*
         * IPv4/IPv6 address matched in URL.
         * Copy the matched bytes (from..to range in payload).
         */
        {
            unsigned int match_len = (unsigned int)(to - from);
            if (match_len < MAX_URL_LEN) {
                memcpy(matchCtx->matchedPayload, payload + from, match_len);
                matchCtx->matchedPayload[match_len] = '\0';
                memcpy(matchCtx->extractedDomain,
                       matchCtx->matchedPayload, match_len);
                matchCtx->extractedDomain[match_len] = '\0';
                matchCtx->extractedDomainLength = match_len;
            }
        }
        break;

    case HS_PATTERN_ID_HTTP_DOMAIN: /* 3 */
        /*
         * "Host: example.com" matched.
         * Skip "Host: " prefix (6 bytes) to get the bare domain.
         */
        {
            unsigned int match_len = (unsigned int)(to - from);
            const char  *host_prefix = "Host: ";
            unsigned int prefix_len  = (unsigned int)strlen(host_prefix);
            if (match_len > prefix_len && match_len - prefix_len < MAX_URL_LEN) {
                unsigned int domain_len = match_len - prefix_len;
                memcpy(matchCtx->extractedDomain,
                       payload + from + prefix_len,
                       domain_len);
                matchCtx->extractedDomain[domain_len] = '\0';
                matchCtx->extractedDomainLength        = domain_len;
            }
        }
        break;
    }

    /*
     * Return 0: continue scanning (find all matching patterns).
     * Return non-zero (e.g. 1): HS_SCAN_TERMINATED — stop now.
     *
     * In the DP application, HS_FLAG_SINGLEMATCH is set on all patterns so
     * Hyperscan calls on_hs_match at most once per pattern per scan.
     * We still return 0 to allow other patterns (different IDs) to fire.
     */
    return 0;
}

/* ───────────────────────────────────────────────────────────
 * on_hs_match_group — callback for per-group domain DB scans
 *
 * Simpler than on_hs_match: just captures the matched domain string.
 * The ID is the domain's policy ID assigned during compilation.
 * The real app uses matchCtx->id as the signature ID.
 * ─────────────────────────────────────────────────────────── */
static int on_hs_match_group(unsigned int id,
                           unsigned long long from,
                           unsigned long long to,
                           unsigned int flags,
                           void *ctx)
{
    (void)flags;

    struct dp_match_context_group *matchCtx =
        (struct dp_match_context_group *)ctx;

    matchCtx->id           = id;
    matchCtx->from         = from;
    matchCtx->to           = to;
    matchCtx->onMatch_count++;

    /* The matched "domain" is the payload string itself (we scanned it) */
    unsigned int match_len = (unsigned int)(to - from);
    if (match_len < MAX_URL_LEN) {
        /* matchedDomain = the portion of the input that matched */
        /* In the real app, the full payload (the domain string) is copied */
        matchCtx->matchedDomainLength = match_len;
    }

    return 0;
}

/* ───────────────────────────────────────────────────────────
 * hs_alloc_db_scratch — reimplements from domain_scan.c hs_alloc_db_scratch()
 *
 * Allocates scratch space for a given database.
 * Scratch is a temporary working buffer Hyperscan uses during hs_scan().
 * It is NOT thread-safe — each lcore needs its own scratch.
 *
 * One scratch can be re-used for multiple scans from the SAME lcore
 * as long as scans are not concurrent (sequential is fine).
 *
 * @db      : the database to allocate scratch for
 * @scratch : pointer to scratch pointer (in/out — can grow existing scratch)
 *
 * Note the signature: hs_alloc_scratch(db, &scratch) can GROW an existing
 * scratch if db requires more space than what scratch currently has.
 * Pass &existing_scratch to reuse, or pass a pointer to NULL to create new.
 * ─────────────────────────────────────────────────────────── */
int hs_alloc_db_scratch(const hs_database_t *db, hs_scratch_t **scratch)
{
    hs_error_t err = hs_alloc_scratch(db, scratch);
    if (err != HS_SUCCESS) {
        fprintf(stderr, "[hs_alloc_db_scratch] hs_alloc_scratch failed: err=%d\n",
                err);
        return -1;
    }

    size_t scratch_sz = 0;
    hs_scratch_size(*scratch, &scratch_sz);
    printf("  Scratch allocated: %zu bytes (%.1f KB)\n",
           scratch_sz, (double)scratch_sz / 1024.0);
    return 0;
}

/* ───────────────────────────────────────────────────────────
 * hs_clone_scratch_for_lcore — reimplements from domain_scan.c hs_clone_scratch_for_lcore()
 *
 * Called once per worker lcore during startup.
 * Creates a per-lcore copy of global_scratch that can be used
 * concurrently with other lcores' scratches.
 *
 * This is more efficient than calling hs_alloc_scratch() per lcore
 * because cloning copies the already-sized scratch without recalculating
 * the required size for each database.
 * ─────────────────────────────────────────────────────────── */
int hs_clone_scratch_for_lcore(hs_scratch_t **dest, int worker_lcore)
{
    if (!global_scratch) {
        fprintf(stderr, "[hs_clone_scratch_for_lcore] global_scratch is NULL — "
                "call hs_init_global_scratch() first\n");
        return -1;
    }

    hs_error_t err = hs_clone_scratch(global_scratch, dest);
    if (err != HS_SUCCESS) {
        fprintf(stderr,
                "[hs_clone_scratch_for_lcore] hs_clone_scratch failed for lcore %d: "
                "err=%d\n", worker_lcore, err);
        return -1;
    }

    printf("  Cloned scratch for worker lcore %d\n", worker_lcore);
    return 0;
}

/* ───────────────────────────────────────────────────────────
 * hs_scan_payload — scan packet payload with global threat DB
 *
 * Reimplements from domain_scan.c hs_scan_payload().
 *
 * Scans payload against domainsPatternDB looking for:
 *   - TLS ClientHello SNI extension (id=1)
 *   - HTTP Host header domain (id=3)
 *   - IP address in URL (id=2,4)
 *
 * Returns the matched pattern ID (1,2,3,4) on match, 0 on no match,
 * -1 on error. The extracted domain is in matchCtx->extractedDomain.
 * ─────────────────────────────────────────────────────────── */
int hs_scan_payload(const uint8_t *payload, uint16_t payload_len,
                        hs_scratch_t *worker_scratch,
                        struct dp_match_context *matchCtx)
{
    memset(matchCtx, 0, sizeof(*matchCtx));
    matchCtx->payload = payload;

    /*
     * Use per-lcore worker_scratch if available, fall back to global.
     * In a real multi-lcore app, always use worker_scratch — it is the
     * scratch cloned for this lcore. Falling back to global_scratch in
     * a multi-threaded context causes HS_SCRATCH_IN_USE corruption.
     */
    hs_scratch_t *scratch = worker_scratch ? worker_scratch : global_scratch;

    hs_error_t err = hs_scan(
        domainsPatternDB,
        (const char *)payload,
        payload_len,
        0,           /* flags: unused in BLOCK mode, always pass 0 */
        scratch,
        on_hs_match,   /* callback fired for each match */
        matchCtx     /* passed as 'ctx' to callback */
    );

    /*
     * HS_SCAN_TERMINATED: the onMatch callback returned non-zero,
     * requesting early termination. This is not an error — it means
     * the application deliberately stopped the scan (e.g., after
     * finding one match is enough). Treat it as success.
     */
    if (err != HS_SUCCESS && err != HS_SCAN_TERMINATED)
        return -1;

    return (int)matchCtx->id;   /* 0 if no match, else the matched ID */
}

/* ───────────────────────────────────────────────────────────
 * hs_scan_domain_group — scan domain string against group policy DB
 *
 * Reimplements from domain_scan.c hs_scan_domain_group().
 *
 * This is called when:
 *   1. rte_hash exact match misses for this domain (Module 12)
 *   2. Fall through to Hyperscan regex/literal scan
 *
 * The domain string is scanned against the per-group literal database.
 * If a match fires, matchCtx->id is set to the matched domain's ID.
 *
 * Returns matchCtx->id (the signature ID) on match, -1 on error.
 * ─────────────────────────────────────────────────────────── */
int hs_scan_domain_group(const char *domain,
                               hs_database_t *group_db,
                               hs_scratch_t *worker_scratch,
                               struct dp_match_context_group *matchCtx)
{
    if (!group_db) {
        return -1;  /* group has no Hyperscan DB (no domain patterns) */
    }

    memset(matchCtx, 0, sizeof(*matchCtx));

    hs_scratch_t *scratch = worker_scratch ? worker_scratch : global_scratch;

    /* The scratch must have been allocated/grown for group_db too.
     * In the real app, hyperscan_scratch_compile_for_group() calls
     * hs_alloc_scratch(group->database, &worker_scratch) to grow it. */

    hs_error_t err = hs_scan(
        group_db,
        domain,
        (unsigned int)strlen(domain),
        0,
        scratch,
        on_hs_match_group,
        matchCtx
    );

    if (err != HS_SUCCESS && err != HS_SCAN_TERMINATED)
        return -1;

    /* Return sig_id / 10 convention from the real app */
    return matchCtx->onMatch_count > 0 ? (int)(matchCtx->id) : 0;
}

/* ───────────────────────────────────────────────────────────
 * hs_init_global_scratch — reimplements from domain_scan.c
 *
 * Called once at startup AFTER compiling domainsPatternDB.
 * This scratch is then cloned for each worker lcore.
 * ─────────────────────────────────────────────────────────── */
static int hs_init_global_scratch(void)
{
    if (!domainsPatternDB) {
        fprintf(stderr, "[init_scratch] domainsPatternDB is NULL\n");
        return -1;
    }
    return hs_alloc_db_scratch(domainsPatternDB, &global_scratch);
}

/* ═══════════════════════════════════════════════════════════
 * Compile helper — compile global DB + group DB for demos
 * ═══════════════════════════════════════════════════════════ */
static hs_database_t *compile_global_db(void)
{
    const char *patterns[] = {
        "\x00\x00\x00\x00\x00",             /* id=1: TLS SNI ext */
        "Host: [a-zA-Z0-9._-]+",            /* id=3: HTTP Host   */
        "[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}", /* id=2: IPv4 */
    };
    unsigned flags[] = {
        HS_FLAG_SINGLEMATCH,
        HS_FLAG_CASELESS | HS_FLAG_SINGLEMATCH,
        HS_FLAG_SINGLEMATCH,
    };
    unsigned ids[] = {1, 3, 2};

    hs_compile_error_t *err = NULL;
    hs_database_t      *db  = NULL;
    hs_error_t r = hs_compile_multi(patterns, flags, ids, 3,
                                     HS_MODE_BLOCK, NULL, &db, &err);
    if (r != HS_SUCCESS) {
        if (err) { fprintf(stderr, "Compile error: %s\n", err->message);
                   hs_free_compile_error(err); }
        return NULL;
    }
    return db;
}

static hs_database_t *compile_group_db(const char **domains, size_t n,
                                        unsigned *ids_out)
{
    char     **pats  = malloc(n * sizeof(char *));
    unsigned  *flags = malloc(n * sizeof(unsigned));
    unsigned  *ids   = malloc(n * sizeof(unsigned));
    size_t    *lens  = malloc(n * sizeof(size_t));
    assert(pats && flags && ids && lens);

    for (size_t i = 0; i < n; i++) {
        pats[i]  = (char *)domains[i];
        flags[i] = HS_FLAG_CASELESS | HS_FLAG_SINGLEMATCH;
        ids[i]   = (unsigned)(i + 1);
        lens[i]  = strlen(domains[i]);
        ids_out[i] = ids[i];
    }

    hs_compile_error_t *err = NULL;
    hs_database_t      *db  = NULL;
    hs_error_t r = hs_compile_lit_multi(
        (const char *const *)pats, flags, ids, lens, (unsigned)n,
        HS_MODE_BLOCK, NULL, &db, &err);

    free(pats); free(flags); free(ids); free(lens);

    if (r != HS_SUCCESS) {
        if (err) { fprintf(stderr, "Group compile error: %s\n", err->message);
                   hs_free_compile_error(err); }
        return NULL;
    }
    return db;
}

/* ═══════════════════════════════════════════════════════════
 * Demo 1: TLS SNI extraction (hs_scan_payload, id=4)
 * ═══════════════════════════════════════════════════════════ */
static void demo_tls_sni_scan(hs_scratch_t *scratch)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 1: TLS SNI extraction (hs_scan_payload, id=4)\n");
    printf("══════════════════════════════════════════════\n\n");

    /*
     * Realistic TLS ClientHello payload (TCP data after TCP header).
     * SNI = "www.secure-corp.example" (23 bytes) at offset 54.
     *
     * Layout at offset 54 (the SNI extension type 0x0000):
     *   54:  00 00  → extension type = server_name
     *   56:  00 1c  → ext data length = 28
     *   58:  00 1a  → server name list length = 26
     *   60:  00     → name type = host_name
     *   61:  00 17  → name length = 23   ← from+7 = 61
     *   63:  "www.secure-corp.example"   ← from+9 = 63
     */
    static const uint8_t tls_clienthello[] = {
        /* TLS Record */
        0x16, 0x03, 0x01, 0x00, 0x6a,
        /* Handshake: ClientHello */
        0x01, 0x00, 0x00, 0x66,
        /* ClientHello: version + random */
        0x03, 0x03,
        0xaa,0xbb,0xcc,0xdd,0xee,0xff,0x00,0x11,
        0x22,0x33,0x44,0x55,0x66,0x77,0x88,0x99,
        0xaa,0xbb,0xcc,0xdd,0xee,0xff,0x00,0x11,
        0x22,0x33,0x44,0x55,0x66,0x77,0x88,0x99,
        /* session_id: none */
        0x00,
        /* cipher suites */
        0x00,0x04, 0x13,0x01, 0x13,0x02,
        /* compression */
        0x01, 0x00,
        /* extensions total length */
        0x00,0x39,
        /* SNI extension: type 0x0000 at offset 54 */
        0x00,0x00,              /* type: server_name  ← Hyperscan matches here */
        0x00,0x1c,              /* ext data length: 28 */
        0x00,0x1a,              /* server name list length: 26 */
        0x00,                   /* name type: host_name */
        0x00,0x17,              /* name length: 23    ← from+7 */
        /* "www.secure-corp.example"    ← from+9 */
        0x77,0x77,0x77,0x2e,
        0x73,0x65,0x63,0x75,0x72,0x65,0x2d,
        0x63,0x6f,0x72,0x70,0x2e,
        0x65,0x78,0x61,0x6d,0x70,0x6c,0x65,
        /* supported_versions ext */
        0x00,0x2b, 0x00,0x03, 0x02, 0x03,0x04,
        /* ALPN ext */
        0x00,0x10, 0x00,0x0e, 0x00,0x0c,
        0x02, 0x68,0x32,
        0x08, 0x68,0x74,0x74,0x70,0x2f,0x31,0x2e,0x31,
    };

    struct dp_match_context matchCtx;
    int matched_id = hs_scan_payload(tls_clienthello,
                                         sizeof(tls_clienthello),
                                         scratch, &matchCtx);

    printf("  Scanned %zu-byte TLS ClientHello payload\n",
           sizeof(tls_clienthello));
    printf("  matched_id          = %d (%s)\n", matched_id,
           matched_id == HS_PATTERN_ID_TLS ? "HS_PATTERN_ID_TLS=1" : "?");
    printf("  from                = %llu  (SNI ext type offset)\n", matchCtx.from);
    printf("  extractedDomain     = \"%s\"\n", matchCtx.extractedDomain);
    printf("  extractedDomainLength = %u\n\n",
           matchCtx.extractedDomainLength);

    assert(matched_id == HS_PATTERN_ID_TLS);
    assert(strcmp((char *)matchCtx.extractedDomain, "www.secure-corp.example") == 0);
    printf("  PASS: SNI extracted correctly\n\n");
}

/* ═══════════════════════════════════════════════════════════
 * Demo 2: HTTP Host header extraction (id=6)
 * ═══════════════════════════════════════════════════════════ */
static void demo_http_host_scan(hs_scratch_t *scratch)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 2: HTTP Host header extraction (id=6)\n");
    printf("══════════════════════════════════════════════\n\n");

    const char *http_request =
        "GET /path?q=1 HTTP/1.1\r\n"
        "Host: blocked-shopping.example.com\r\n"
        "User-Agent: Mozilla/5.0\r\n"
        "Accept: */*\r\n\r\n";

    struct dp_match_context matchCtx;
    int matched_id = hs_scan_payload(
        (const uint8_t *)http_request,
        (uint16_t)strlen(http_request),
        scratch, &matchCtx);

    printf("  HTTP payload (first 60 bytes): \"%.60s...\"\n", http_request);
    printf("  matched_id      = %d (%s)\n", matched_id,
           matched_id == HS_PATTERN_ID_HTTP_DOMAIN
               ? "HS_PATTERN_ID_HTTP_DOMAIN=3" : "?");
    printf("  extractedDomain = \"%s\"\n\n", matchCtx.extractedDomain);
    assert(matched_id == HS_PATTERN_ID_HTTP_DOMAIN);
    printf("  PASS\n\n");
}

/* ═══════════════════════════════════════════════════════════
 * Demo 3: Per-group domain scan (hs_scan_domain_group)
 *
 * This is the Hyperscan fallback after rte_hash miss (Module 12).
 * Scans the extracted domain name against the per-group literal DB.
 * ═══════════════════════════════════════════════════════════ */
static void demo_group_domain_scan(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 3: Per-group domain scan (hs_scan_domain_group)\n");
    printf("══════════════════════════════════════════════\n\n");

    /* Simulate group policy: these domains are blocked for this group */
    const char *blocked_domains[] = {
        "ads.doubleclick.net",
        "tracker.adnxs.com",
        "malware-download.ru",
        "phishing.example.tk",
        "streaming-block.io",
    };
    unsigned n = sizeof(blocked_domains) / sizeof(blocked_domains[0]);
    unsigned domain_ids[5] = {0};

    hs_database_t *group_db = compile_group_db(blocked_domains, n, domain_ids);
    assert(group_db != NULL);

    /* Allocate scratch for the group DB.
     * In the real app, hyperscan_scratch_compile_for_group() calls
     * hs_alloc_scratch(group->database, &worker_info->worker_scratch)
     * to GROW the per-lcore scratch to also cover the group DB. */
    hs_scratch_t *group_scratch = NULL;
    assert(hs_alloc_scratch(group_db, &group_scratch) == HS_SUCCESS);

    /* Test domains to scan */
    const char *test_domains[] = {
        "ads.doubleclick.net",     /* in group DB: should match */
        "malware-download.ru",     /* in group DB: should match */
        "google.com",              /* NOT in group DB: should miss */
        "TRACKER.ADNXS.COM",       /* uppercase: should match (CASELESS flag) */
    };
    int expected[] = {1, 1, 0, 1};   /* 1=match, 0=miss */

    printf("  Group has %u blocked domains\n\n", n);

    for (int i = 0; i < 4; i++) {
        struct dp_match_context_group matchCtx;
        int ret = hs_scan_domain_group(test_domains[i], group_db,
                                            group_scratch, &matchCtx);
        int hit = (matchCtx.onMatch_count > 0);

        printf("  domain=\"%s\"\n", test_domains[i]);
        printf("    hit=%d  id=%u  sig_id=%d  expected_hit=%d  %s\n",
               hit, matchCtx.id, ret, expected[i],
               hit == expected[i] ? "PASS" : "FAIL");

        if (hit) {
            printf("    → POLICY: domain is BLOCKED by group policy\n");
            printf("    → next: sinkhole response (Module 23)\n");
        } else {
            printf("    → POLICY: domain not in group DB → ALLOW (default)\n");
        }
        printf("\n");
        assert(hit == expected[i]);
    }

    hs_free_scratch(group_scratch);
    hs_free_database(group_db);
}

/* ═══════════════════════════════════════════════════════════
 * Demo 4: Scratch safety — thread-safety demonstration
 *
 * Shows that each thread needs its own scratch via clone.
 * Using one scratch from two threads simultaneously causes
 * HS_SCRATCH_IN_USE — this demo proves cloning solves it.
 * ═══════════════════════════════════════════════════════════ */
#define NUM_SCAN_THREADS  4

typedef struct {
    int            thread_id;
    hs_scratch_t  *scratch;      /* per-thread cloned scratch */
    int            scan_count;
    int            errors;
} scan_thread_arg_t;

static void *scan_thread_func(void *arg)
{
    scan_thread_arg_t *ta      = (scan_thread_arg_t *)arg;
    const char        *payload = "Host: api.example.com\r\nContent-Type: text/html";

    for (int i = 0; i < 1000; i++) {
        struct dp_match_context ctx;
        int ret = hs_scan_payload((const uint8_t *)payload,
                                      (uint16_t)strlen(payload),
                                      ta->scratch, &ctx);
        if (ret < 0)
            ta->errors++;
        else
            ta->scan_count++;
    }
    return NULL;
}

static void demo_scratch_thread_safety(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 4: Per-thread scratch (thread safety)\n");
    printf("══════════════════════════════════════════════\n\n");

    pthread_t         threads[NUM_SCAN_THREADS];
    scan_thread_arg_t args[NUM_SCAN_THREADS];

    /* Clone global_scratch once per thread */
    for (int i = 0; i < NUM_SCAN_THREADS; i++) {
        args[i].thread_id  = i;
        args[i].scratch    = NULL;
        args[i].scan_count = 0;
        args[i].errors     = 0;
        hs_clone_scratch_for_lcore(&args[i].scratch, i);
    }

    /* Launch all threads simultaneously — each uses its own scratch */
    for (int i = 0; i < NUM_SCAN_THREADS; i++)
        pthread_create(&threads[i], NULL, scan_thread_func, &args[i]);

    for (int i = 0; i < NUM_SCAN_THREADS; i++)
        pthread_join(threads[i], NULL);

    int total_scans = 0, total_errors = 0;
    for (int i = 0; i < NUM_SCAN_THREADS; i++) {
        total_scans  += args[i].scan_count;
        total_errors += args[i].errors;
        hs_free_scratch(args[i].scratch);
    }

    printf("  %d threads × 1000 scans = %d total\n",
           NUM_SCAN_THREADS, NUM_SCAN_THREADS * 1000);
    printf("  Successful scans : %d\n", total_scans);
    printf("  Errors (HS_SCRATCH_IN_USE) : %d\n\n", total_errors);
    assert(total_errors == 0);
    printf("  PASS: per-thread scratch cloning prevents all concurrency errors\n\n");

    printf("  If we had used a single shared scratch:\n");
    printf("    hs_scan() would return HS_SCRATCH_IN_USE (-9) on concurrent access\n");
    printf("    Solution: hs_clone_scratch_for_lcore() for each worker lcore\n\n");
}

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    printf("=== Module 16: Hyperscan Scratch + Scan ===\n\n");
    printf("Hyperscan version: %s\n\n", hs_version());

    /* Compile global DB + initialize scratch (mirrors hs_init_global_scratch) */
    printf("[Init] Compiling global threat DB...\n");
    domainsPatternDB = compile_global_db();
    assert(domainsPatternDB != NULL);
    printf("[Init] Allocating global_scratch...\n");
    assert(hs_init_global_scratch() == 0);

    size_t scratch_sz;
    hs_scratch_size(global_scratch, &scratch_sz);
    printf("[Init] global_scratch size: %zu bytes\n\n", scratch_sz);

    /* Demo 1 + 2 use global_scratch directly (single-threaded) */
    demo_tls_sni_scan(global_scratch);
    demo_http_host_scan(global_scratch);
    demo_group_domain_scan();
    demo_scratch_thread_safety();

    /* Cleanup */
    hs_free_scratch(global_scratch);
    hs_free_database(domainsPatternDB);

    printf("=== All demos complete ===\n\n");
    printf("API summary:\n");
    printf("  hs_alloc_scratch(db, &scratch)         → allocate scratch\n");
    printf("  hs_alloc_scratch(db, &existing)        → GROW existing scratch\n");
    printf("  hs_clone_scratch(src, &dest)            → clone per-lcore copy\n");
    printf("  hs_scratch_size(scratch, &size)         → scratch size in bytes\n");
    printf("  hs_scan(db, data, len, 0, scratch, cb, ctx) → scan buffer\n");
    printf("  hs_free_scratch(scratch)                → cleanup\n");
    printf("\n");
    printf("  hs_scan returns:\n");
    printf("    HS_SUCCESS (0)         → scan complete\n");
    printf("    HS_SCAN_TERMINATED (-4)→ callback returned non-zero (not an error)\n");
    printf("    HS_SCRATCH_IN_USE (-9) → scratch used by another thread (bug!)\n");
    printf("    HS_INVALID (-1)        → NULL db, scratch, or data pointer\n");
    return 0;
}
