/**
 * hs_compile.c — Module 15: Hyperscan Pattern Compilation
 *
 * Hyperscan is Intel's high-performance regex library. In the DP application it is
 * used for two distinct purposes:
 *
 *   1. Global threat database (domainsPatternDB):
 *      Regex patterns loaded from patterns.txt / patterns2.txt.
 *      These match TLS SNI extensions, HTTP Host headers, and IP addresses
 *      in URLs. Compiled once at startup with hs_compile_multi().
 *      Pattern IDs defined in domain_scan.h:
 *        HS_PATTERN_ID_TLS=1, HTTP_IPV4=2, HTTP_DOMAIN=3, HTTP_IPV6=4
 *
 *   2. Per-group domain policy database:
 *      Literal domain patterns for each enterprise group.
 *      "google.com", "*.facebook.com", "ads.tracker.io" etc.
 *      Compiled per group with hs_compile_lit_multi().
 *      Used as fallback when rte_hash exact lookup misses (Module 22).
 *
 * This module implements:
 *   - parseFlags()             → maps 'i','s','m','H','8','W' to HS_FLAG_*
 *   - parseFile()              → reads ID:/pattern/flags format (patterns.txt)
 *   - hs_create_db()    → wraps hs_compile_multi/hs_compile_lit_multi
 *   - hs_error_to_string()     → human-readable error codes
 *   - DB info and serialization
 *
 * These are exact reimplementations of the functions in domain_scan.c.
 *
 * Requires: Hyperscan (libhs) installed.
 *   RedHat/Rocky:  dnf install hyperscan hyperscan-devel
 *   Ubuntu:        apt install libhyperscan-dev
 *   From source:   https://github.com/intel/hyperscan
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <assert.h>
#include <ctype.h>

#include <hs.h>   /* Hyperscan main header */

/* ───────────────────────────────────────────────────────────
 * Pattern ID enum — mirrors domain_scan.h exactly
 *
 * These IDs are assigned to each pattern during compilation.
 * When Hyperscan fires a match, the onMatch callback receives
 * the ID of the matching pattern. The callback then uses the ID
 * to determine what to extract (SNI bytes, Host header, etc.)
 * ─────────────────────────────────────────────────────────── */
typedef enum {
    HS_PATTERN_ID_TLS         = 1,  /* TLS SNI extension type 0x00 0x00 */
    HS_PATTERN_ID_HTTP_IPV4   = 2,  /* IPv4 address in URL              */
    HS_PATTERN_ID_HTTP_DOMAIN = 3,  /* HTTP Host: header domain         */
    HS_PATTERN_ID_HTTP_IPV6   = 4,  /* IPv6 address in URL              */
} hs_pattern_id_t;

/* ───────────────────────────────────────────────────────────
 * dp_hyperscan_details — mirrors domain_scan.h
 *
 * Holds the raw pattern data before compilation.
 * Populated by parseFile() or by add_domain_to_group().
 * Passed to hs_create_db().
 * ─────────────────────────────────────────────────────────── */
#define MAX_PATTERNS_PER_DB  200
#define MAX_URL_LEN          256

struct dp_hyperscan_details {
    char    *patterns[MAX_PATTERNS_PER_DB];
    unsigned flags[MAX_PATTERNS_PER_DB];
    unsigned ids[MAX_PATTERNS_PER_DB];
    size_t   len_per_pattern[MAX_PATTERNS_PER_DB]; /* used only for lit_multi */
    unsigned num_pattern;
};

/* ───────────────────────────────────────────────────────────
 * hs_error_to_string — reimplements from domain_scan.c
 *
 * Hyperscan returns typed error codes, not strings. This function
 * converts them for log messages.
 * ─────────────────────────────────────────────────────────── */
const char *hs_error_to_string(hs_error_t err)
{
    switch (err) {
    case HS_SUCCESS:           return "HS_SUCCESS";
    case HS_INVALID:           return "HS_INVALID (invalid parameter)";
    case HS_NOMEM:             return "HS_NOMEM (out of memory)";
    case HS_SCAN_TERMINATED:   return "HS_SCAN_TERMINATED (callback returned non-zero)";
    case HS_COMPILER_ERROR:    return "HS_COMPILER_ERROR (pattern syntax error)";
    case HS_DB_VERSION_ERROR:  return "HS_DB_VERSION_ERROR (DB version mismatch)";
    case HS_DB_PLATFORM_ERROR: return "HS_DB_PLATFORM_ERROR (wrong CPU features)";
    case HS_DB_MODE_ERROR:     return "HS_DB_MODE_ERROR (wrong scan mode)";
    case HS_BAD_ALIGN:         return "HS_BAD_ALIGN (pointer alignment error)";
    case HS_BAD_ALLOC:         return "HS_BAD_ALLOC (allocator failure)";
    case HS_SCRATCH_IN_USE:    return "HS_SCRATCH_IN_USE (scratch re-entered)";
    default:                   return "unknown error";
    }
}

/* ───────────────────────────────────────────────────────────
 * parseFlags — reimplements from domain_scan.c
 *
 * Maps a flags string like "i", "is", "8" to HS_FLAG_* bitmask.
 * Used when reading patterns.txt where each line is:
 *   ID:/pattern/flags
 *
 * Flag characters:
 *   i → HS_FLAG_CASELESS    (case-insensitive)
 *   s → HS_FLAG_DOTALL      (. matches \n)
 *   m → HS_FLAG_MULTILINE   (^ and $ match line boundaries)
 *   H → HS_FLAG_SINGLEMATCH (stop after first match — performance opt)
 *   8 → HS_FLAG_UTF8        (UTF-8 mode)
 *   W → HS_FLAG_UCP         (Unicode property support)
 *   f → HS_FLAG_ALLOWEMPTY  (allow patterns that can match empty string)
 * ─────────────────────────────────────────────────────────── */
unsigned parseFlags(const char *flagsStr)
{
    unsigned flags = 0;
    for (const char *p = flagsStr; *p; p++) {
        switch (*p) {
        case 'i': flags |= HS_FLAG_CASELESS;    break;
        case 's': flags |= HS_FLAG_DOTALL;      break;
        case 'm': flags |= HS_FLAG_MULTILINE;   break;
        case 'H': flags |= HS_FLAG_SINGLEMATCH; break;
        case '8': flags |= HS_FLAG_UTF8;        break;
        case 'W': flags |= HS_FLAG_UCP;         break;
        case 'f': flags |= HS_FLAG_ALLOWEMPTY;  break;
        default:
            fprintf(stderr, "[parseFlags] Unknown flag '%c'\n", *p);
            break;
        }
    }
    return flags;
}

/* ───────────────────────────────────────────────────────────
 * parseFile — reimplements from domain_scan.c
 *
 * Reads Hyperscan patterns from a file in the format:
 *
 *   ID:/regex_or_literal/flags
 *
 * Examples from the real patterns.txt:
 *   4:/\x00\x00[\x00-\x09]\x00\x00/
 *   6:/Host: /i
 *   5:/[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/
 *   7:/\[([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}\]/i
 *
 * Lines starting with # are comments.
 * The extracted pattern (between slashes) is heap-allocated;
 * caller is responsible for freeing via free_parsed_patterns().
 * ─────────────────────────────────────────────────────────── */
void parseFile(const char *filename,
               char ***patterns_out,
               unsigned **flags_out,
               unsigned **ids_out,
               int *count_out)
{
    FILE *fp;
    char  line[1024];
    int   capacity = 64;
    int   count    = 0;

    char    **patterns = malloc(capacity * sizeof(char *));
    unsigned *flags    = malloc(capacity * sizeof(unsigned));
    unsigned *ids      = malloc(capacity * sizeof(unsigned));
    assert(patterns && flags && ids);

    fp = fopen(filename, "r");
    if (!fp) {
        fprintf(stderr, "[parseFile] Cannot open '%s'\n", filename);
        *count_out = 0;
        free(patterns); free(flags); free(ids);
        *patterns_out = NULL; *flags_out = NULL; *ids_out = NULL;
        return;
    }

    while (fgets(line, sizeof(line), fp)) {
        /* strip newline */
        char *nl = strchr(line, '\n');
        if (nl) *nl = '\0';

        /* skip comments and empty lines */
        if (line[0] == '#' || line[0] == '\0') continue;

        /* parse: ID:/pattern/flags */
        char *colon = strchr(line, ':');
        if (!colon) continue;
        *colon = '\0';
        unsigned id = (unsigned)atoi(line);
        char *rest = colon + 1;

        /* pattern is between the two '/' delimiters */
        if (*rest != '/') continue;
        rest++;
        char *end_slash = strrchr(rest, '/');
        if (!end_slash || end_slash == rest - 1) continue;
        *end_slash = '\0';

        /* flags string after the closing '/' */
        const char *flags_str = end_slash + 1;

        if (count >= capacity) {
            capacity *= 2;
            patterns = realloc(patterns, capacity * sizeof(char *));
            flags    = realloc(flags,    capacity * sizeof(unsigned));
            ids      = realloc(ids,      capacity * sizeof(unsigned));
            assert(patterns && flags && ids);
        }

        patterns[count] = strdup(rest);
        flags[count]    = parseFlags(flags_str);
        ids[count]      = id;
        count++;
    }
    fclose(fp);

    *patterns_out = patterns;
    *flags_out    = flags;
    *ids_out      = ids;
    *count_out    = count;
}

/* ───────────────────────────────────────────────────────────
 * hs_create_db — reimplements from domain_scan.c
 *
 * Compiles patterns into an hs_database_t.
 * @compile_mode_lit = 1 (HS_COMPILE_MULTI_FLAG): use hs_compile_lit_multi
 *                     (for domain literals — faster, no regex engine)
 * @compile_mode_lit = 0: use hs_compile_multi
 *                     (for regex patterns like the TLS/HTTP patterns)
 *
 * Returns 0 on success, -1 on error.
 * Increments hs_db_compile_count (in the real app).
 * ─────────────────────────────────────────────────────────── */
#define HS_COMPILE_MULTI_FLAG  1

int hs_create_db(struct dp_hyperscan_details *hs_details,
                         int compile_mode_lit,
                         hs_database_t **database)
{
    hs_compile_error_t *compile_error = NULL;
    hs_error_t          err;

    if (hs_details->num_pattern == 0) {
        fprintf(stderr, "[hs_create_db] No patterns to compile\n");
        return -1;
    }

    if (compile_mode_lit == HS_COMPILE_MULTI_FLAG) {
        /*
         * hs_compile_lit_multi — for LITERAL (non-regex) patterns.
         *
         * Used for per-group domain tables: "google.com", "facebook.com", etc.
         * Much faster to compile than regex. Matching is also faster because
         * no NFA/DFA is constructed — Hyperscan uses SIMD string search.
         *
         * @len_per_pattern: length of each literal string (no NUL terminator
         * needed — Hyperscan treats them as byte arrays, not C strings).
         */
        err = hs_compile_lit_multi(
            (const char *const *)hs_details->patterns,
            hs_details->flags,
            hs_details->ids,
            hs_details->len_per_pattern,
            hs_details->num_pattern,
            HS_MODE_BLOCK,      /* block scan mode: whole buffer scanned at once */
            NULL,               /* platform info: NULL = current CPU */
            database,
            &compile_error
        );
    } else {
        /*
         * hs_compile_multi — for REGEX patterns.
         *
         * Used for the global threat DB: patterns that match TLS SNI headers,
         * HTTP Host fields, IP addresses in URLs.
         * Takes longer to compile (NFA/DFA construction) but is very fast
         * at scan time — all patterns scanned in one pass over the data.
         */
        err = hs_compile_multi(
            (const char *const *)hs_details->patterns,
            hs_details->flags,
            hs_details->ids,
            hs_details->num_pattern,
            HS_MODE_BLOCK,
            NULL,
            database,
            &compile_error
        );
    }

    if (err != HS_SUCCESS) {
        if (compile_error) {
            fprintf(stderr,
                    "[hs_create_db] Compile error (pattern %d): %s\n",
                    compile_error->expression,
                    compile_error->message);
            hs_free_compile_error(compile_error);
        } else {
            fprintf(stderr, "[hs_create_db] Error: %s\n",
                    hs_error_to_string(err));
        }
        return -1;
    }

    return 0;
}

/* ───────────────────────────────────────────────────────────
 * print_db_info — inspect a compiled database
 * ─────────────────────────────────────────────────────────── */
static void print_db_info(const hs_database_t *db, const char *label)
{
    char *info_str = NULL;
    if (hs_database_info(db, &info_str) == HS_SUCCESS) {
        printf("  [DB: %s]\n", label);
        printf("    info      : %s\n", info_str);
        free(info_str);
    }

    size_t db_size = 0;
    if (hs_database_size(db, &db_size) == HS_SUCCESS)
        printf("    size      : %zu bytes (%.1f KB)\n",
               db_size, (double)db_size / 1024.0);
    printf("\n");
}

/* ═══════════════════════════════════════════════════════════
 * Demo 1: Global threat DB (hs_compile_multi with regex)
 *
 * Mirrors hs_init_global_scratch() in domain_scan.c.
 * Patterns match TLS ClientHello SNI extension, HTTP Host headers,
 * and IP addresses in URLs.
 * ═══════════════════════════════════════════════════════════ */
static void demo_global_threat_db(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 1: Global threat DB (hs_compile_multi, regex)\n");
    printf("══════════════════════════════════════════════\n\n");

    struct dp_hyperscan_details hs = {0};

    /*
     * These patterns mirror what the DP application loads from patterns.txt.
     * In production the patterns are tuned for:
     *   - Maximum coverage (catch all TLS/HTTP variants)
     *   - Minimal false positives
     *   - Compatible with HS_FLAG_SINGLEMATCH for performance
     */

    /* Pattern 4: TLS ClientHello SNI extension type (0x0000) prefix
     * Matches the server_name extension type bytes in a TLS ClientHello.
     * When this fires, on_hs_match reads SNI name at from+7 / from+9. */
    hs.patterns[0] = "\x00\x00\x00\x00\x00";  /* simplified: 5 null bytes */
    hs.flags[0]    = HS_FLAG_SINGLEMATCH;
    hs.ids[0]      = HS_PATTERN_ID_TLS;        /* 1 */

    /* Pattern 5: IPv4 address in URL
     * e.g. "http://1.2.3.4/path" — policy checks the raw IP directly */
    hs.patterns[1] = "[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}";
    hs.flags[1]    = HS_FLAG_CASELESS | HS_FLAG_SINGLEMATCH;
    hs.ids[1]      = HS_PATTERN_ID_HTTP_IPV4;  /* 2 */

    /* Pattern 6: HTTP Host header domain
     * e.g. "Host: www.example.com\r\n" */
    hs.patterns[2] = "Host: [a-zA-Z0-9._-]+";
    hs.flags[2]    = HS_FLAG_CASELESS | HS_FLAG_SINGLEMATCH;
    hs.ids[2]      = HS_PATTERN_ID_HTTP_DOMAIN; /* 3 */

    /* Pattern 7: IPv6 address in URL
     * e.g. "http://[2001:db8::1]/path" */
    hs.patterns[3] = "\\[([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}\\]";
    hs.flags[3]    = HS_FLAG_CASELESS | HS_FLAG_SINGLEMATCH;
    hs.ids[3]      = HS_PATTERN_ID_HTTP_IPV6;  /* 4 */

    hs.num_pattern = 4;

    printf("  Compiling %u regex patterns (hs_compile_multi)...\n",
           hs.num_pattern);
    for (unsigned i = 0; i < hs.num_pattern; i++) {
        printf("    id=%-3u  flags=0x%04x  pattern=\"%s\"\n",
               hs.ids[i], hs.flags[i], hs.patterns[i]);
    }
    printf("\n");

    hs_database_t *db = NULL;
    int ret = hs_create_db(&hs, 0 /* regex mode */, &db);

    if (ret == 0) {
        printf("  Compilation SUCCESS\n");
        print_db_info(db, "global_threat_db (domainsPatternDB)");
        hs_free_database(db);
    } else {
        printf("  Compilation FAILED (see error above)\n\n");
    }
}

/* ═══════════════════════════════════════════════════════════
 * Demo 2: Per-group domain DB (hs_compile_lit_multi with literals)
 *
 * Mirrors hyperscan_db_compile_for_groups() / hs_create_db()
 * called with compile_mode_lit = HS_COMPILE_MULTI_FLAG.
 *
 * Domain literals from the enterprise policy:
 *   "google.com", "facebook.com", "youtube.com" → whitelisted
 *   "malware-site.ru", "phishing.tk"             → blacklisted
 *
 * These are exact byte matches — no regex engine needed.
 * Hyperscan uses SIMD acceleration (SSSE3/AVX2) for literal search.
 * ═══════════════════════════════════════════════════════════ */
static void demo_per_group_domain_db(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 2: Per-group domain DB (hs_compile_lit_multi, literals)\n");
    printf("══════════════════════════════════════════════\n\n");

    const char *domains[] = {
        "google.com",
        "facebook.com",
        "youtube.com",
        "malware-download.ru",
        "phishing-bank.tk",
        "ads.doubleclick.net",
        "tracker.adnxs.com",
    };
    unsigned n = sizeof(domains) / sizeof(domains[0]);

    struct dp_hyperscan_details hs = {0};

    for (unsigned i = 0; i < n; i++) {
        hs.patterns[i]        = (char *)domains[i];
        hs.flags[i]           = HS_FLAG_CASELESS | HS_FLAG_SINGLEMATCH;
        hs.ids[i]             = i + 1;            /* arbitrary ID per domain */
        hs.len_per_pattern[i] = strlen(domains[i]);
    }
    hs.num_pattern = n;

    printf("  Compiling %u literal domains (hs_compile_lit_multi)...\n", n);
    for (unsigned i = 0; i < n; i++) {
        printf("    id=%-3u  len=%-4zu  \"%s\"\n",
               hs.ids[i], hs.len_per_pattern[i], hs.patterns[i]);
    }
    printf("\n");

    hs_database_t *db = NULL;
    int ret = hs_create_db(&hs, HS_COMPILE_MULTI_FLAG /* literal */, &db);

    if (ret == 0) {
        printf("  Compilation SUCCESS\n");
        print_db_info(db, "per_group_domain_db");

        /*
         * In the real app, this db is stored in group->database.
         * Module 16 (Hyperscan scan) will use it.
         * Module 21 (scratch management) allocates a scratch for it.
         */
        printf("  db stored as group->database\n");
        printf("  next: allocate scratch with hs_alloc_scratch(db, &scratch)\n\n");

        hs_free_database(db);
    } else {
        printf("  Compilation FAILED\n\n");
    }
}

/* ═══════════════════════════════════════════════════════════
 * Demo 3: parseFlags + parseFile (reimplements from domain_scan.c)
 * ═══════════════════════════════════════════════════════════ */
static void demo_parse_flags(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 3: parseFlags() — flag string to HS_FLAG_*\n");
    printf("══════════════════════════════════════════════\n\n");

    struct { const char *str; unsigned expected; } tests[] = {
        { "",    0 },
        { "i",   HS_FLAG_CASELESS },
        { "is",  HS_FLAG_CASELESS | HS_FLAG_DOTALL },
        { "iH",  HS_FLAG_CASELESS | HS_FLAG_SINGLEMATCH },
        { "isH", HS_FLAG_CASELESS | HS_FLAG_DOTALL | HS_FLAG_SINGLEMATCH },
        { "8",   HS_FLAG_UTF8 },
    };

    for (size_t i = 0; i < sizeof(tests)/sizeof(tests[0]); i++) {
        unsigned got = parseFlags(tests[i].str);
        printf("  parseFlags(\"%-4s\") = 0x%04x  %s\n",
               tests[i].str, got,
               got == tests[i].expected ? "OK" : "MISMATCH");
        assert(got == tests[i].expected);
    }
    printf("\n");
}

static void demo_parse_file(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 4: parseFile() — read patterns.txt format\n");
    printf("══════════════════════════════════════════════\n\n");

    /* Write a sample patterns.txt for the demo */
    const char *sample_patterns_txt =
        "# Global Hyperscan patterns\n"
        "# Format: ID:/pattern/flags\n"
        "4:/\\x00\\x00\\x00\\x00\\x00/H\n"
        "5:/[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}/iH\n"
        "6:/Host: [a-zA-Z0-9._-]+/iH\n"
        "7:/\\[([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}\\]/iH\n";

    FILE *fp = fopen("/tmp/sase_patterns.txt", "w");
    assert(fp != NULL);
    fputs(sample_patterns_txt, fp);
    fclose(fp);

    char    **patterns = NULL;
    unsigned *flags    = NULL;
    unsigned *ids      = NULL;
    int       count    = 0;

    parseFile("/tmp/sase_patterns.txt", &patterns, &flags, &ids, &count);

    printf("  Loaded %d patterns from /tmp/sase_patterns.txt:\n", count);
    for (int i = 0; i < count; i++) {
        printf("    id=%-3u  flags=0x%04x  pattern=\"%s\"\n",
               ids[i], flags[i], patterns[i]);
    }
    printf("\n");

    /* Compile the loaded patterns into a DB */
    if (count > 0) {
        struct dp_hyperscan_details hs = {0};
        for (int i = 0; i < count && i < MAX_PATTERNS_PER_DB; i++) {
            hs.patterns[i] = patterns[i];
            hs.flags[i]    = flags[i];
            hs.ids[i]      = ids[i];
        }
        hs.num_pattern = (unsigned)count;

        hs_database_t *db = NULL;
        if (hs_create_db(&hs, 0, &db) == 0) {
            printf("  DB compiled from file  ✓\n");
            print_db_info(db, "from_file");
            hs_free_database(db);
        }

        for (int i = 0; i < count; i++) free(patterns[i]);
        free(patterns); free(flags); free(ids);
    }
}

/* ═══════════════════════════════════════════════════════════
 * Demo 5: Serialization — persist DB to disk / shared memory
 *
 * Serializing the database avoids recompiling on every restart.
 * Useful for:
 *   - Large global DBs that take seconds to compile
 *   - Sharing a compiled DB between DPDK processes
 *   - Precompiling on a build server, shipping to production
 * ═══════════════════════════════════════════════════════════ */
static void demo_serialization(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 5: DB serialization / deserialization\n");
    printf("══════════════════════════════════════════════\n\n");

    /* Compile a small DB to serialize */
    hs_compile_error_t *err = NULL;
    hs_database_t      *db  = NULL;
    const char *pat = "malware\\.[a-z]{2,6}";
    unsigned flags  = HS_FLAG_CASELESS | HS_FLAG_SINGLEMATCH;
    unsigned id     = 100;

    hs_error_t r = hs_compile_multi(&pat, &flags, &id, 1,
                                     HS_MODE_BLOCK, NULL, &db, &err);
    assert(r == HS_SUCCESS);

    /* ── Serialize ── */
    size_t   serial_sz = 0;
    char    *serial_buf = NULL;

    assert(hs_serialized_database_size(db, &serial_sz) == HS_SUCCESS);
    serial_buf = malloc(serial_sz);
    assert(serial_buf != NULL);
    assert(hs_serialize_database(db, serial_buf, serial_sz) == HS_SUCCESS);

    printf("  Original DB size   : ");
    size_t db_sz = 0;
    hs_database_size(db, &db_sz);
    printf("%zu bytes\n", db_sz);
    printf("  Serialized size    : %zu bytes (can be written to disk)\n", serial_sz);

    hs_free_database(db);
    db = NULL;

    /* Write to a temp file (simulates disk persistence) */
    fp: {
        FILE *f = fopen("/tmp/dp_app_hs_db.bin", "wb");
        if (f) {
            fwrite(serial_buf, 1, serial_sz, f);
            fclose(f);
            printf("  Written to         : /tmp/dp_app_hs_db.bin\n");
        }
    }

    /* ── Deserialize ── */
    /*
     * In the real app, this is called on restart to avoid recompiling.
     * hs_deserialize_database() allocates a new db — no need to recompile.
     *
     * Note: the deserialized DB must be used on the same CPU features
     * as the serialized one (same Hyperscan platform). Use
     * hs_deserialize_database_at() for a pre-allocated buffer (useful
     * with rte_malloc_socket to ensure NUMA locality).
     */
    hs_database_t *db2 = NULL;
    r = hs_deserialize_database(serial_buf, serial_sz, &db2);

    if (r == HS_SUCCESS) {
        printf("  Deserialized OK\n");
        print_db_info(db2, "deserialized_db");
        hs_free_database(db2);
    } else {
        printf("  Deserialization failed: %s\n", hs_error_to_string(r));
    }

    free(serial_buf);
}

/* ═══════════════════════════════════════════════════════════
 * Demo 6: Error handling — invalid pattern
 * ═══════════════════════════════════════════════════════════ */
static void demo_error_handling(void)
{
    printf("══════════════════════════════════════════════\n");
    printf("Demo 6: Compile error handling (invalid pattern)\n");
    printf("══════════════════════════════════════════════\n\n");

    hs_compile_error_t *compile_error = NULL;
    hs_database_t      *db            = NULL;

    /* Deliberately broken patterns */
    const char *bad_patterns[] = {
        "good_pattern[0-9]+",   /* pattern 0: valid */
        "bad_pattern[0-9",      /* pattern 1: unclosed bracket — INVALID */
        "another_good.*",       /* pattern 2: valid */
    };
    unsigned flags[] = {HS_FLAG_CASELESS, HS_FLAG_CASELESS, HS_FLAG_CASELESS};
    unsigned ids[]   = {1, 2, 3};

    hs_error_t err = hs_compile_multi(bad_patterns, flags, ids, 3,
                                       HS_MODE_BLOCK, NULL, &db, &compile_error);

    if (err != HS_SUCCESS) {
        printf("  hs_compile_multi returned: %s\n", hs_error_to_string(err));
        if (compile_error) {
            printf("  compile_error->expression : %d  (0-indexed pattern)\n",
                   compile_error->expression);
            printf("  compile_error->message    : %s\n\n",
                   compile_error->message);
            printf("  In the real app:\n");
            printf("    LOG_ERROR(\"Hyperscan compile error (expr %%d): %%s\",\n");
            printf("              compile_error->expression, compile_error->message);\n");
            printf("    hs_free_compile_error(compile_error);\n\n");
            hs_free_compile_error(compile_error);
        }
    }

    /* Show that hs_free_compile_error is REQUIRED (memory leak otherwise) */
    printf("  Rule: ALWAYS call hs_free_compile_error() after an error.\n");
    printf("        Forgetting it leaks memory on every bad pattern reload.\n\n");
}

/* ─── main ──────────────────────────────────────────────── */
int main(void)
{
    /* Verify Hyperscan version */
    printf("=== Module 15: Hyperscan Pattern Compilation ===\n\n");
    printf("Hyperscan version: %s\n\n", hs_version());

    demo_global_threat_db();
    demo_per_group_domain_db();
    demo_parse_flags();
    demo_parse_file();
    demo_serialization();
    demo_error_handling();

    printf("=== All demos complete ===\n\n");
    printf("API summary:\n");
    printf("  hs_compile_multi(pats,flags,ids,n,mode,plt,&db,&err)\n");
    printf("  hs_compile_lit_multi(pats,flags,ids,lens,n,mode,plt,&db,&err)\n");
    printf("  hs_free_database(db)\n");
    printf("  hs_free_compile_error(err)\n");
    printf("  hs_database_info(db, &info_str)    → version, mode, features\n");
    printf("  hs_database_size(db, &size)        → bytes in DB\n");
    printf("  hs_serialize_database(db, buf, sz) → disk persistence\n");
    printf("  hs_deserialize_database(buf,sz,&db)→ reload from disk\n");
    printf("\n");
    printf("Mode choices:\n");
    printf("  HS_MODE_BLOCK    → whole buffer scanned at once (the DP application uses this)\n");
    printf("  HS_MODE_STREAM   → streaming: data arrives in chunks\n");
    printf("  HS_MODE_VECTORED → multiple non-contiguous buffers in one call\n");
    return 0;
}
