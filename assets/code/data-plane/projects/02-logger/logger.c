/**
 * logger.c — Module 02: Logger
 *
 * The logger is the second subsystem initialized at startup (right after
 * config parsing). Once it's up, every subsequent startup step —
 * EAL init, port init, mempool creation, Kafka connection, Hyperscan
 * compilation — logs its progress through it.
 *
 * Design requirements for a dataplane logger:
 *
 *  1. Thread-safe  — multiple lcores log concurrently. A mutex is the
 *                    simplest correct solution. In a high-frequency path
 *                    you would use a lock-free ring (like the real app does
 *                    via DPDK's RTE_LOG + rte_log infrastructure), but for
 *                    control-plane and startup paths a mutex is fine.
 *
 *  2. Timestamps   — millisecond precision. Operators correlating logs
 *                    with packet captures need sub-second granularity.
 *
 *  3. Dual output  — stderr for immediate visibility + log file for
 *                    persistence. In the real app the log file is
 *                    rotated by logrotate on RedHat.
 *
 *  4. Level filter — DEBUG floods the log under load. Level is set from
 *                    config at startup and can be changed at runtime via
 *                    log_set_level() (e.g., triggered by a SIGUSR1 handler).
 *
 *  5. ANSI colours — level-coded colours in console output help operators
 *                    spot WARN/ERROR lines at a glance. Stripped from
 *                    file output (log parsers don't handle escape codes).
 */

#include "logger.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdarg.h>
#include <pthread.h>

/* ───────────────────────────────────────────────────────────
 * ANSI colour codes — console output only.
 * File output never includes these (log parsers / grep break on them).
 * ─────────────────────────────────────────────────────────── */
#define ANSI_RESET   "\033[0m"
#define ANSI_GREY    "\033[90m"
#define ANSI_CYAN    "\033[36m"
#define ANSI_YELLOW  "\033[33m"
#define ANSI_RED     "\033[31m"
#define ANSI_BOLDRED "\033[1;31m"

/* ───────────────────────────────────────────────────────────
 * Global logger instance
 * Initialized once by logger_init(), used by all LOG_* macros.
 * ─────────────────────────────────────────────────────────── */
static logger_t g_logger = {
    .level    = LOG_LEVEL_INFO,
    .log_file = NULL,
    .console  = 1,
};

static int g_initialized = 0;

/* ───────────────────────────────────────────────────────────
 * Internal helpers
 * ─────────────────────────────────────────────────────────── */

/* Map log_level_t → short label string */
static const char *level_to_str(log_level_t level)
{
    switch (level) {
    case LOG_LEVEL_DEBUG: return "DEBUG";
    case LOG_LEVEL_INFO:  return "INFO ";
    case LOG_LEVEL_WARN:  return "WARN ";
    case LOG_LEVEL_ERROR: return "ERROR";
    case LOG_LEVEL_FATAL: return "FATAL";
    default:              return "?????";
    }
}

/* Map log_level_t → ANSI colour for console */
static const char *level_to_colour(log_level_t level)
{
    switch (level) {
    case LOG_LEVEL_DEBUG: return ANSI_GREY;
    case LOG_LEVEL_INFO:  return ANSI_CYAN;
    case LOG_LEVEL_WARN:  return ANSI_YELLOW;
    case LOG_LEVEL_ERROR: return ANSI_RED;
    case LOG_LEVEL_FATAL: return ANSI_BOLDRED;
    default:              return ANSI_RESET;
    }
}

/* Map string from config → log_level_t */
static log_level_t str_to_level(const char *s)
{
    if (!s)                        return LOG_LEVEL_INFO;
    if (strcasecmp(s, "DEBUG") == 0) return LOG_LEVEL_DEBUG;
    if (strcasecmp(s, "INFO")  == 0) return LOG_LEVEL_INFO;
    if (strcasecmp(s, "WARN")  == 0) return LOG_LEVEL_WARN;
    if (strcasecmp(s, "ERROR") == 0) return LOG_LEVEL_ERROR;
    if (strcasecmp(s, "FATAL") == 0) return LOG_LEVEL_FATAL;

    fprintf(stderr, "[logger] Unknown log level '%s', defaulting to INFO\n", s);
    return LOG_LEVEL_INFO;
}

/*
 * get_timestamp — write "YYYY-MM-DD HH:MM:SS.mmm" into buf.
 *
 * clock_gettime(CLOCK_REALTIME) gives nanosecond precision.
 * We truncate to milliseconds — enough for operator correlation
 * without making log lines too wide.
 */
static void get_timestamp(char *buf, size_t len)
{
    struct timespec ts;
    struct tm       tm_info;

    clock_gettime(CLOCK_REALTIME, &ts);
    localtime_r(&ts.tv_sec, &tm_info);

    /* "2024-06-02 14:32:01.456" */
    strftime(buf, len, "%Y-%m-%d %H:%M:%S", &tm_info);
    snprintf(buf + 19, len - 19, ".%03ld", ts.tv_nsec / 1000000L);
}

/* ───────────────────────────────────────────────────────────
 * Public API implementation
 * ─────────────────────────────────────────────────────────── */

/**
 * logger_init — open the log file and set the filter level.
 *
 * In the real app, called in app_main.c immediately after config_load():
 *
 *   logger_init(
 *       config_get_string(&cfg, "logging", "level",    "INFO"),
 *       config_get_string(&cfg, "logging", "file",     NULL)
 *   );
 *   LOG_INFO("the DP application starting up...");
 */
int logger_init(const char *level_str, const char *log_file_path)
{
    pthread_mutex_init(&g_logger.lock, NULL);

    g_logger.level   = str_to_level(level_str);
    g_logger.console = 1;

    if (log_file_path && *log_file_path) {
        g_logger.log_file = fopen(log_file_path, "a");
        if (!g_logger.log_file) {
            fprintf(stderr, "[logger] Cannot open log file '%s', "
                    "falling back to console only\n", log_file_path);
            /* not fatal — console logging still works */
        }
    }

    g_initialized = 1;
    return 0;
}

/**
 * logger_close — flush and close.
 * In the real app called from the SIGTERM handler before rte_eal_cleanup().
 */
void logger_close(void)
{
    if (g_logger.log_file) {
        fflush(g_logger.log_file);
        fclose(g_logger.log_file);
        g_logger.log_file = NULL;
    }
    pthread_mutex_destroy(&g_logger.lock);
}

/**
 * log_set_level — change the filter level at runtime.
 *
 * In the real app this is triggered by:
 *   - A SIGUSR1 handler that toggles between INFO and DEBUG
 *   - An OAM (Operations, Administration & Management) command
 *     received over the management channel
 *
 * No restart needed — takes effect immediately for all lcores
 * because g_logger.level is a single shared value. The read is
 * not atomic here (fine for a flag that changes rarely), but in a
 * strict implementation you'd use _Atomic or a memory fence.
 */
void log_set_level(log_level_t level)
{
    g_logger.level = level;
}

/**
 * log_write — the function behind all LOG_* macros.
 *
 * Format written to BOTH console and file:
 *   [2024-06-02 14:32:01.456] [INFO ] [config_parser.c:78] EAL ready
 *
 * Console additionally gets ANSI colour around the level label.
 *
 * Thread safety: pthread_mutex_lock ensures that concurrent log calls
 * from different lcores do not interleave partial lines. In DPDK the
 * real rte_log() uses a similar internal spinlock.
 */
void log_write(log_level_t level, const char *file, int line,
               const char *fmt, ...)
{
    char    timestamp[32];
    char    message[1024];
    va_list args;

    /* fast path: skip everything if below configured level */
    if (level < g_logger.level)
        return;

    if (!g_initialized) {
        /* logger not yet initialized — write to stderr directly */
        va_start(args, fmt);
        vfprintf(stderr, fmt, args);
        va_end(args);
        fprintf(stderr, "\n");
        return;
    }

    get_timestamp(timestamp, sizeof(timestamp));

    va_start(args, fmt);
    vsnprintf(message, sizeof(message), fmt, args);
    va_end(args);

    pthread_mutex_lock(&g_logger.lock);

    /* ── Console output (with ANSI colour) ── */
    if (g_logger.console) {
        fprintf(stderr,
                "%s[%s] [%s] [%s:%d] %s%s\n",
                level_to_colour(level),
                timestamp,
                level_to_str(level),
                file, line,
                message,
                ANSI_RESET);
    }

    /* ── File output (no colour codes) ── */
    if (g_logger.log_file) {
        fprintf(g_logger.log_file,
                "[%s] [%s] [%s:%d] %s\n",
                timestamp,
                level_to_str(level),
                file, line,
                message);
        /* flush immediately so log is not lost on crash.
         * In a high-throughput path you would only flush periodically
         * or on WARN/ERROR, but for a DP app crash logs matter more
         * than throughput of log writes. */
        fflush(g_logger.log_file);
    }

    pthread_mutex_unlock(&g_logger.lock);

    /* FATAL: log is written, now abort to generate a core dump */
    if (level == LOG_LEVEL_FATAL)
        abort();
}

/* ───────────────────────────────────────────────────────────
 * Demo main()
 *
 * Simulates the startup log sequence of a real dataplane app:
 *   config → logger → EAL → ports → mempools → workers → kafka
 *
 * Compare this to the startup prints you see when running dp_app.
 * ─────────────────────────────────────────────────────────── */
int main(void)
{
    /* Step 1: init logger — in the real app level + file come from config */
    logger_init("DEBUG", NULL);   /* NULL = console only for this demo */

    LOG_INFO("=== the DP application starting ===");
    LOG_INFO("Logger initialized: level=DEBUG, output=console");

    /* Step 2: config (Module 01) */
    LOG_INFO("Loading config file: /etc/dp_app/dp_app.conf");
    LOG_DEBUG("Config: eal.cores=0-7, eal.socket_mem=2048");
    LOG_DEBUG("Config: port.num_rx_queues=4, port.rx_desc=1024");
    LOG_INFO("Config loaded: 23 entries");

    /* Step 3: EAL init (Module 11) */
    LOG_INFO("Initializing DPDK EAL...");
    LOG_DEBUG("EAL args: -l 0-7 --socket-mem 2048 -n 4");
    LOG_INFO("EAL initialized: 8 lcores available, 2 NUMA sockets");

    /* Step 4: port init (Module 13) */
    LOG_INFO("Initializing NIC port 0...");
    LOG_DEBUG("Port 0: configuring 4 RX queues, 4 TX queues");
    LOG_DEBUG("Port 0: RX desc=1024, TX desc=1024, MTU=1500");
    LOG_INFO("Port 0: link UP  speed=25Gbps  duplex=full");

    /* Step 5: mempool (Module 12) */
    LOG_INFO("Creating mbuf mempool: 65536 elements, socket 0");
    LOG_DEBUG("Mempool: element size=%zu, cache_size=256",
              sizeof(void *) + 2048);  /* simplified */

    /* Step 6: Hyperscan (Module 19-21) */
    LOG_INFO("Compiling Hyperscan pattern DB...");
    LOG_DEBUG("Loading pattern file: /etc/dp_app/patterns.txt");
    LOG_DEBUG("Loading pattern file: /etc/dp_app/patterns2.txt");
    LOG_INFO("Hyperscan DB compiled: 128 patterns, scratch allocated");

    /* Step 7: worker lcores (Module 15) */
    LOG_INFO("Launching worker lcores: RX=1  TX=2  workers=3,4,5,6");
    LOG_DEBUG("lcore 1: RX loop started on port 0 queue 0");
    LOG_DEBUG("lcore 3: worker started, scratch cloned from global");

    /* Step 8: Kafka (Module 25-26) */
    LOG_INFO("Connecting to Kafka broker: broker.example.com:9092");
    LOG_WARN("Kafka: initial connection attempt timed out, retrying (1/3)");
    LOG_INFO("Kafka: connected. Subscribed to topic: policy_updates");

    /* Typical warn/error scenarios */
    LOG_WARN("Port 0: RX descriptor ring 80%% full on queue 2 — "
             "worker lcore 4 may be falling behind");
    LOG_ERROR("Hyperscan scratch alloc failed for lcore 7: ENOMEM — "
              "falling back to global scratch (lock contention possible)");

    /* Runtime level change (e.g., toggled by SIGUSR1) */
    LOG_INFO("--- Switching log level to WARN (simulating runtime change) ---");
    log_set_level(LOG_LEVEL_WARN);
    LOG_DEBUG("This DEBUG line is NOT printed (below WARN)");
    LOG_INFO("This INFO line is NOT printed (below WARN)");
    LOG_WARN("This WARN line IS printed");

    log_set_level(LOG_LEVEL_DEBUG);
    LOG_INFO("--- Log level restored to DEBUG ---");

    LOG_INFO("Startup complete. Packet processing active.");

    logger_close();
    return 0;
}
