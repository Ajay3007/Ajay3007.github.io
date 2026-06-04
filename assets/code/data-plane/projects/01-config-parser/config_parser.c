/**
 * config_parser.c — Module 01: Config Parser
 *
 * In a real dataplane application (like the DP application), the very first thing
 * that runs at startup is config parsing — before DPDK EAL init, before
 * any memory pools, before any threads start.
 *
 * The config drives everything:
 *   - Which CPU cores to hand to DPDK (EAL --lcores, --socket-mem)
 *   - How many RX/TX queues per NIC port
 *   - Where the Hyperscan pattern files live
 *   - Kafka broker address, topic names
 *   - Log level, log file path
 *   - Worker core assignments (which lcore does RX, which does TX, etc.)
 *
 * In the real DP project this logic lives in app_main.c. Parsed values
 * are used to build the argv[] array passed to rte_eal_init() and to
 * populate global config structs used by all subsystems.
 *
 * This module is pure C — no external dependencies.
 * Compile and run it on any Linux box to understand the pattern.
 *
 * Config file format supported:
 *
 *   [section_name]
 *   key = value          # inline comment
 *   # full-line comment
 *   ; also a comment
 *
 * Usage:
 *   ./config_parser [path_to_config_file]
 *   (defaults to sample.conf in current directory)
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <errno.h>

/* ───────────────────────────────────────────────────────────
 * Constants
 *
 * In a real app these would be tuned to the actual config file
 * size. 256 entries is sufficient for a typical dataplane config.
 * ─────────────────────────────────────────────────────────── */
#define MAX_CONFIG_ENTRIES  256
#define MAX_SECTION_LEN      64
#define MAX_KEY_LEN          64
#define MAX_VALUE_LEN       256
#define MAX_LINE_LEN        512

/* ───────────────────────────────────────────────────────────
 * Data Structures
 * ─────────────────────────────────────────────────────────── */

/* One parsed key=value entry, tagged with its section */
typedef struct {
    char section[MAX_SECTION_LEN];
    char key[MAX_KEY_LEN];
    char value[MAX_VALUE_LEN];
} config_entry_t;

/*
 * The full parsed config.
 * Static array — no heap allocation needed for config of this size.
 * In the real app this is a global struct initialized once at startup.
 */
typedef struct {
    config_entry_t entries[MAX_CONFIG_ENTRIES];
    int            count;
} config_t;

/* ───────────────────────────────────────────────────────────
 * Internal helpers
 * ─────────────────────────────────────────────────────────── */

/*
 * trim — strip leading and trailing whitespace in-place.
 * Returns pointer to the first non-space character.
 * This is called on every key and value after splitting on '='.
 */
static char *trim(char *s)
{
    char *end;

    /* skip leading spaces */
    while (isspace((unsigned char)*s))
        s++;

    if (*s == '\0')
        return s;

    /* strip trailing spaces */
    end = s + strlen(s) - 1;
    while (end > s && isspace((unsigned char)*end))
        end--;
    *(end + 1) = '\0';

    return s;
}

/*
 * strip_inline_comment — truncate the string at the first '#' or ';'
 * that is not inside double quotes.
 *
 * Example: "broker.example.com:9092  # primary broker" → "broker.example.com:9092  "
 * The trailing space is removed by a subsequent trim() call.
 */
static void strip_inline_comment(char *s)
{
    char *p      = s;
    int in_quote = 0;

    while (*p) {
        if (*p == '"')
            in_quote = !in_quote;

        if (!in_quote && (*p == '#' || *p == ';')) {
            *p = '\0';
            return;
        }
        p++;
    }
}

/* ───────────────────────────────────────────────────────────
 * Public API
 * ─────────────────────────────────────────────────────────── */

/**
 * config_load — parse an INI config file into a config_t.
 *
 * Call this first, before any other subsystem initializes.
 * In the real DP application:
 *
 *   config_t app_cfg;
 *   if (config_load(&app_cfg, "/etc/dp_app/dp_app.conf") != 0)
 *       rte_exit(EXIT_FAILURE, "Config load failed\n");
 *
 * Returns 0 on success, -1 on error (file not found, parse error, overflow).
 */
int config_load(config_t *cfg, const char *filename)
{
    FILE *fp;
    char  line[MAX_LINE_LEN];
    char  current_section[MAX_SECTION_LEN] = "";
    int   lineno = 0;

    if (!cfg || !filename)
        return -1;

    memset(cfg, 0, sizeof(*cfg));

    fp = fopen(filename, "r");
    if (!fp) {
        fprintf(stderr, "[config] Cannot open '%s': %s\n",
                filename, strerror(errno));
        return -1;
    }

    while (fgets(line, sizeof(line), fp)) {
        char *p;
        lineno++;

        /* strip newline characters (handles \n and \r\n) */
        p = strchr(line, '\n'); if (p) *p = '\0';
        p = strchr(line, '\r'); if (p) *p = '\0';

        p = trim(line);

        /* skip blank lines and full-line comments */
        if (*p == '\0' || *p == '#' || *p == ';')
            continue;

        /* ── Section header: [section_name] ── */
        if (*p == '[') {
            char *end = strchr(p, ']');
            if (!end) {
                fprintf(stderr, "[config] Line %d: malformed section "
                        "header (no closing ']')\n", lineno);
                fclose(fp);
                return -1;
            }
            *end = '\0';
            strncpy(current_section, trim(p + 1), MAX_SECTION_LEN - 1);
            current_section[MAX_SECTION_LEN - 1] = '\0';
            continue;
        }

        /* ── key = value ── */
        char *eq = strchr(p, '=');
        if (!eq) {
            /* warn but continue — tolerant of stray lines */
            fprintf(stderr, "[config] Line %d: no '=' found, skipping: %s\n",
                    lineno, p);
            continue;
        }

        if (cfg->count >= MAX_CONFIG_ENTRIES) {
            fprintf(stderr, "[config] Too many entries (max %d). "
                    "Increase MAX_CONFIG_ENTRIES.\n", MAX_CONFIG_ENTRIES);
            fclose(fp);
            return -1;
        }

        *eq = '\0';
        char *key   = trim(p);
        char *value = trim(eq + 1);

        strip_inline_comment(value);
        value = trim(value);   /* re-trim after comment stripped */

        config_entry_t *entry = &cfg->entries[cfg->count++];
        strncpy(entry->section, current_section, MAX_SECTION_LEN - 1);
        strncpy(entry->key,     key,             MAX_KEY_LEN     - 1);
        strncpy(entry->value,   value,           MAX_VALUE_LEN   - 1);
    }

    fclose(fp);
    return 0;
}

/**
 * config_get_string — fetch a value by section + key.
 *
 * Returns default_val if the key is not found.
 * The returned pointer points into the config_t's internal storage —
 * do not free it. In the real app values are copied into dedicated
 * config structs (e.g., app_cfg.kafka_broker[]).
 *
 * Example:
 *   const char *broker = config_get_string(&cfg, "kafka", "broker",
 *                                           "localhost:9092");
 *   rd_kafka_conf_set(rk_conf, "bootstrap.servers", broker, ...);
 */
const char *config_get_string(const config_t *cfg,
                               const char     *section,
                               const char     *key,
                               const char     *default_val)
{
    int i;
    for (i = 0; i < cfg->count; i++) {
        if (strcmp(cfg->entries[i].section, section) == 0 &&
            strcmp(cfg->entries[i].key,     key)     == 0)
            return cfg->entries[i].value;
    }
    return default_val;
}

/**
 * config_get_int — fetch a value as integer.
 *
 * Returns default_val if key is missing or value is not a valid integer.
 *
 * Example:
 *   int num_queues = config_get_int(&cfg, "port", "num_rx_queues", 1);
 *   rte_eth_dev_configure(port_id, num_queues, num_queues, &port_conf);
 */
int config_get_int(const config_t *cfg,
                   const char     *section,
                   const char     *key,
                   int             default_val)
{
    const char *val = config_get_string(cfg, section, key, NULL);
    char       *endptr;
    long        v;

    if (!val)
        return default_val;

    errno = 0;
    v = strtol(val, &endptr, 10);

    if (errno != 0 || endptr == val || *endptr != '\0') {
        fprintf(stderr, "[config] '%s.%s' = '%s' is not a valid integer, "
                "using default %d\n", section, key, val, default_val);
        return default_val;
    }
    return (int)v;
}

/**
 * config_get_bool — fetch a value as boolean (0 or 1).
 *
 * Accepts: true/false, yes/no, 1/0 (case-insensitive).
 * Returns default_val if key is missing or value is unrecognized.
 *
 * Example:
 *   int hs_enabled = config_get_bool(&cfg, "policy", "enable_hyperscan", 1);
 *   if (hs_enabled)
 *       initialize_hyperscan_engine();
 */
int config_get_bool(const config_t *cfg,
                    const char     *section,
                    const char     *key,
                    int             default_val)
{
    const char *val = config_get_string(cfg, section, key, NULL);

    if (!val)
        return default_val;

    if (strcasecmp(val, "true")  == 0 ||
        strcasecmp(val, "yes")   == 0 ||
        strcmp(val, "1")         == 0)
        return 1;

    if (strcasecmp(val, "false") == 0 ||
        strcasecmp(val, "no")    == 0 ||
        strcmp(val, "0")         == 0)
        return 0;

    fprintf(stderr, "[config] '%s.%s' = '%s' is not a valid boolean, "
            "using default %d\n", section, key, val, default_val);
    return default_val;
}

/**
 * config_dump — print all parsed entries to stdout.
 *
 * Call this right after config_load() during startup so operators
 * can confirm what the application loaded before any subsystem starts.
 * In the real app this prints at LOG_LEVEL_INFO.
 */
void config_dump(const config_t *cfg)
{
    int i;
    printf("[config] Loaded %d entries:\n", cfg->count);
    for (i = 0; i < cfg->count; i++) {
        printf("  [%-20s]  %-24s = %s\n",
               cfg->entries[i].section,
               cfg->entries[i].key,
               cfg->entries[i].value);
    }
}

/* ───────────────────────────────────────────────────────────
 * Demo main()
 *
 * Shows how the real application reads config at startup.
 * In app_main.c, these parsed values are used to:
 *   1. Build the eal_argv[] array for rte_eal_init()
 *   2. Configure NIC ports (rte_eth_dev_configure)
 *   3. Set up Kafka producer/consumer (rd_kafka_conf_set)
 *   4. Decide which lcores run RX, TX, and worker roles
 *   5. Load Hyperscan pattern files
 * ─────────────────────────────────────────────────────────── */
int main(int argc, char *argv[])
{
    config_t    cfg;
    const char *config_file = "sample.conf";

    if (argc > 1)
        config_file = argv[1];

    printf("=== Module 01: Config Parser ===\n\n");

    if (config_load(&cfg, config_file) != 0) {
        fprintf(stderr, "Failed to load config file: %s\n", config_file);
        return 1;
    }

    config_dump(&cfg);
    printf("\n--- Values a real dataplane app reads at startup ---\n\n");

    /* ── EAL params (used to build rte_eal_init argv) ── */
    printf("[EAL]\n");
    printf("  cores         = %s\n",
           config_get_string(&cfg, "eal", "cores", "0-3"));
    printf("  socket_mem    = %d MB\n",
           config_get_int(&cfg, "eal", "socket_mem", 1024));
    printf("  hugepage_sz   = %d KB\n",
           config_get_int(&cfg, "eal", "hugepage_sz", 2048));

    /* ── Port config (used in rte_eth_dev_configure) ── */
    printf("\n[PORT]\n");
    printf("  port_id       = %d\n",
           config_get_int(&cfg, "port", "port_id", 0));
    printf("  num_rx_queues = %d\n",
           config_get_int(&cfg, "port", "num_rx_queues", 1));
    printf("  num_tx_queues = %d\n",
           config_get_int(&cfg, "port", "num_tx_queues", 1));
    printf("  rx_desc       = %d\n",
           config_get_int(&cfg, "port", "rx_desc", 1024));
    printf("  tx_desc       = %d\n",
           config_get_int(&cfg, "port", "tx_desc", 1024));

    /* ── Worker lcore assignments ── */
    printf("\n[WORKER]\n");
    printf("  rx_lcore      = %d\n",
           config_get_int(&cfg, "worker", "rx_lcore", 1));
    printf("  tx_lcore      = %d\n",
           config_get_int(&cfg, "worker", "tx_lcore", 2));
    printf("  worker_lcores = %s\n",
           config_get_string(&cfg, "worker", "worker_lcores", "3,4,5"));

    /* ── Kafka (passed to rd_kafka_conf_set) ── */
    printf("\n[KAFKA]\n");
    printf("  broker        = %s\n",
           config_get_string(&cfg, "kafka", "broker", "localhost:9092"));
    printf("  topic_policy  = %s\n",
           config_get_string(&cfg, "kafka", "topic_policy", "dp_policy"));
    printf("  topic_cdr     = %s\n",
           config_get_string(&cfg, "kafka", "topic_cdr", "dp_cdr"));
    printf("  group_id      = %s\n",
           config_get_string(&cfg, "kafka", "group_id", "dp_consumer"));

    /* ── Policy / Hyperscan ── */
    printf("\n[POLICY]\n");
    printf("  pattern_file  = %s\n",
           config_get_string(&cfg, "policy", "pattern_file",
                             "/etc/dp_app/patterns.txt"));
    printf("  max_groups    = %d\n",
           config_get_int(&cfg, "policy", "max_groups", 1000));
    printf("  enable_hs     = %s\n",
           config_get_bool(&cfg, "policy", "enable_hyperscan", 1)
               ? "true" : "false");

    /* ── Logging ── */
    printf("\n[LOGGING]\n");
    printf("  level         = %s\n",
           config_get_string(&cfg, "logging", "level", "INFO"));
    printf("  file          = %s\n",
           config_get_string(&cfg, "logging", "file",
                             "/var/log/dp_app/dp_app.log"));

    /* ── Missing key falls back gracefully ── */
    printf("\n[MISSING KEY DEMO]\n");
    printf("  eal.missing   = %d  (default, key not in file)\n",
           config_get_int(&cfg, "eal", "missing_key", 42));
    printf("  port.missing  = %s  (default, key not in file)\n",
           config_get_string(&cfg, "port", "missing_str", "fallback_value"));

    return 0;
}
