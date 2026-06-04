/**
 * logger.h — Module 02: Logger
 *
 * In the real DP project, logger.h is included by every .c file.
 * It is the second thing initialized at startup — right after config parsing
 * and before any DPDK, Kafka, or Hyperscan subsystem starts.
 *
 * Include this header in any module that needs to log:
 *   #include "logger.h"
 *
 * Usage:
 *   LOG_INFO("Port %d initialized with %d RX queues", port_id, num_queues);
 *   LOG_WARN("Kafka poll timeout, retrying...");
 *   LOG_ERROR("Failed to allocate mempool: %s", strerror(errno));
 *   LOG_DEBUG("DNS query: %s  lcore=%u", domain, rte_lcore_id());
 */

#ifndef LOGGER_H
#define LOGGER_H

#include <stdio.h>
#include <stdarg.h>
#include <pthread.h>

/* ───────────────────────────────────────────────────────────
 * Log levels — in increasing order of severity.
 * The configured level acts as a filter: only messages at or
 * above the configured level are printed.
 *
 * In the real app the level is read from config:
 *   const char *lvl = config_get_string(&cfg, "logging", "level", "INFO");
 *   logger_init(lvl, config_get_string(&cfg, "logging", "file", NULL));
 * ─────────────────────────────────────────────────────────── */
typedef enum {
    LOG_LEVEL_DEBUG = 0,
    LOG_LEVEL_INFO,
    LOG_LEVEL_WARN,
    LOG_LEVEL_ERROR,
    LOG_LEVEL_FATAL      /* also calls abort() after logging */
} log_level_t;

/* ───────────────────────────────────────────────────────────
 * Logger state — one global instance for the whole application.
 * In the real app this is a file-scoped static in logger.c, not
 * exposed in the header. Exposed here for educational clarity.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    log_level_t     level;        /* current filter level              */
    FILE           *log_file;     /* NULL = console only               */
    int             console;      /* 1 = also print to stderr          */
    pthread_mutex_t lock;         /* guards concurrent writes          */
} logger_t;

/* ───────────────────────────────────────────────────────────
 * Strip directory path from __FILE__ so log lines show
 * "core_process.c:142" instead of
 * "/home/user/sase-dp/src/dpdk_core/core_process.c:142"
 * ─────────────────────────────────────────────────────────── */
#define __FILENAME__ \
    ((__builtin_strrchr(__FILE__, '/') != NULL) \
        ? __builtin_strrchr(__FILE__, '/') + 1  \
        : __FILE__)

/* ───────────────────────────────────────────────────────────
 * Logging macros — use these everywhere.
 *
 * They automatically capture file, line, and function name.
 * Macro wrapping is important: if the log level is below the
 * configured threshold, the entire call is still evaluated
 * in the function but the mutex + I/O are skipped inside
 * log_write() — in a future optimization you can add a
 * branch before the call here to avoid argument evaluation
 * entirely.
 * ─────────────────────────────────────────────────────────── */
#define LOG_DEBUG(fmt, ...) \
    log_write(LOG_LEVEL_DEBUG, __FILENAME__, __LINE__, fmt, ##__VA_ARGS__)

#define LOG_INFO(fmt, ...) \
    log_write(LOG_LEVEL_INFO,  __FILENAME__, __LINE__, fmt, ##__VA_ARGS__)

#define LOG_WARN(fmt, ...) \
    log_write(LOG_LEVEL_WARN,  __FILENAME__, __LINE__, fmt, ##__VA_ARGS__)

#define LOG_ERROR(fmt, ...) \
    log_write(LOG_LEVEL_ERROR, __FILENAME__, __LINE__, fmt, ##__VA_ARGS__)

/*
 * LOG_FATAL logs the message then calls abort().
 * Use for unrecoverable startup failures (e.g., mempool alloc failed,
 * config file missing in production). In the real app this triggers
 * a core dump that can be analyzed with GDB.
 */
#define LOG_FATAL(fmt, ...) \
    log_write(LOG_LEVEL_FATAL, __FILENAME__, __LINE__, fmt, ##__VA_ARGS__)

/* ─── Public API ─────────────────────────────────────────── */

/**
 * logger_init — initialize the logger.
 *
 * @level_str  : "DEBUG", "INFO", "WARN", "ERROR" (from config)
 * @log_file   : path to log file, or NULL for console-only output
 *
 * Returns 0 on success, -1 if the log file cannot be opened.
 * Call once at startup before any other LOG_* macro is used.
 */
int logger_init(const char *level_str, const char *log_file);

/**
 * logger_close — flush and close the log file.
 * Call at graceful shutdown.
 */
void logger_close(void);

/**
 * log_set_level — change the log level at runtime.
 * Useful for toggling DEBUG level via a signal or OAM command
 * without restarting the application.
 */
void log_set_level(log_level_t level);

/**
 * log_write — internal implementation called by macros.
 * Do not call directly; use LOG_DEBUG / LOG_INFO / etc.
 */
void log_write(log_level_t level, const char *file, int line,
               const char *fmt, ...)
    __attribute__((format(printf, 4, 5)));

#endif /* LOGGER_H */
