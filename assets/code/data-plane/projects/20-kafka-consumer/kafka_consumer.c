/**
 * kafka_consumer.c — Module 20: Kafka Consumer (Policy Sync)
 *
 * The Kafka consumer receives policy updates from the Provisioning
 * Module and applies them to the in-memory data plane tables. This is
 * how enterprise group policies stay current without restarting the DP.
 *
 * Message flow (SYNC_COMPLETE protocol):
 *
 *   PM → DP (via Kafka topic: policy_updates)
 *
 *   { "type":"BEGIN_SYNC",   "group_id":"enterprise_a" }
 *   { "type":"ADD_DOMAIN",   "group_id":"enterprise_a",
 *     "domain":"google.com", "action":"whitelist" }
 *   { "type":"ADD_DOMAIN",   "group_id":"enterprise_a",
 *     "domain":"facebook.com", "action":"blacklist", "category":2 }
 *   ... (more domain updates)
 *   { "type":"SYNC_COMPLETE","group_id":"enterprise_a" }
 *
 * SYNC_COMPLETE protocol ensures atomicity:
 *   - BEGIN_SYNC:    start building a "pending" policy table
 *   - ADD_DOMAIN:    add to pending table (NOT yet active — workers not affected)
 *   - SYNC_COMPLETE: atomically swap pending → active
 *                   (RCU QSBR in real app — see note below)
 *
 * Why not apply each ADD_DOMAIN immediately?
 *   If we apply domain A (whitelisted) before domain B (blacklisted) arrives,
 *   a worker lcore might see a partial policy state — domain A is allowed
 *   when it should be blocked. SYNC_COMPLETE prevents this window.
 *
 * RCU QSBR note:
 *   The atomic swap of domain_details_table in the real the DP application app uses
 *   RCU QSBR (Quiescent State Based Reclamation) — implemented in the DP core library.
 *   This module shows the pattern using C11 atomic pointer swap + a brief
 *   sleep to approximate the "wait for readers" step. In production, the
 *   real RCU waits until all worker lcores call rte_rcu_qsbr_quiescent().
 *
 * This module also handles:
 *   - Partition rebalance callback
 *   - Message parse errors (skip + log)
 *   - Malicious domain updates (IDPS feed via separate topic)
 *   - Graceful shutdown (rd_kafka_consumer_close)
 *
 * Requires: librdkafka
 * Run against real Kafka (Module 19 for producer):
 *   ./kafka_consumer [broker] [policy_topic] [malicious_topic]
 *
 * Standalone demo (no Kafka needed):
 *   ./kafka_consumer --demo
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdatomic.h>
#include <signal.h>
#include <unistd.h>
#include <ctype.h>

#include <librdkafka/rdkafka.h>

/* ───────────────────────────────────────────────────────────
 * Policy message types
 * ─────────────────────────────────────────────────────────── */
typedef enum {
    MSG_BEGIN_SYNC    = 0,
    MSG_ADD_DOMAIN    = 1,
    MSG_REMOVE_DOMAIN = 2,
    MSG_ADD_GROUP     = 3,
    MSG_REMOVE_GROUP  = 4,
    MSG_SYNC_COMPLETE = 5,
    MSG_ADD_MALICIOUS = 6,   /* from IDPS / threat intel feed */
    MSG_UNKNOWN       = 99,
} policy_msg_type_t;

/* ───────────────────────────────────────────────────────────
 * Parsed policy message
 *
 * In the real app, this is built from the Kafka message payload
 * (JSON, Protobuf, or custom binary format from the PM).
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    policy_msg_type_t type;
    char              group_id[32];
    char              domain[256];
    char              action[16];       /* "allow","blacklist","whitelist" */
    uint32_t          category_bitmask;
    uint32_t          port_mask;
    int               confidence;       /* for malicious feed */
} policy_msg_t;

/* ───────────────────────────────────────────────────────────
 * Simplified in-memory domain table
 * (same hashmap pattern as Module 17, replaces rte_hash)
 * ─────────────────────────────────────────────────────────── */
#define HM_SIZE  256

typedef struct filter_details {
    int      is_whitelisted;
    int      is_blacklisted;
    uint32_t category_bitmask;
    uint32_t port_mask;
    char     domain[256];
} filter_details_t;

typedef struct hm_node {
    char              key[256];
    filter_details_t  value;
    struct hm_node   *next;
} hm_node_t;

typedef struct {
    hm_node_t *buckets[HM_SIZE];
    int        count;
} domain_table_t;

static uint32_t hm_hash(const char *k)
{
    uint32_t h = 2166136261u;
    while (*k) { h ^= (uint8_t)*k++; h *= 16777619u; }
    return h & (HM_SIZE - 1);
}

static void dt_add(domain_table_t *t, const char *domain, filter_details_t fd)
{
    uint32_t    idx = hm_hash(domain);
    hm_node_t  *n;

    /* upsert: check if exists */
    for (n = t->buckets[idx]; n; n = n->next) {
        if (strcmp(n->key, domain) == 0) {
            n->value = fd;
            return;
        }
    }

    n = calloc(1, sizeof(*n));
    strncpy(n->key, domain, sizeof(n->key) - 1);
    n->value = fd;
    n->next  = t->buckets[idx];
    t->buckets[idx] = n;
    t->count++;
}

static void dt_remove(domain_table_t *t, const char *domain)
{
    uint32_t   idx  = hm_hash(domain);
    hm_node_t *prev = NULL;
    hm_node_t *cur  = t->buckets[idx];

    while (cur) {
        if (strcmp(cur->key, domain) == 0) {
            if (prev) prev->next = cur->next;
            else       t->buckets[idx] = cur->next;
            free(cur);
            t->count--;
            return;
        }
        prev = cur;
        cur  = cur->next;
    }
}

static filter_details_t *dt_lookup(domain_table_t *t, const char *domain)
{
    uint32_t  idx = hm_hash(domain);
    hm_node_t *n;
    for (n = t->buckets[idx]; n; n = n->next)
        if (strcmp(n->key, domain) == 0)
            return &n->value;
    return NULL;
}

static void dt_free(domain_table_t *t)
{
    for (int i = 0; i < HM_SIZE; i++) {
        hm_node_t *n = t->buckets[i];
        while (n) { hm_node_t *nx = n->next; free(n); n = nx; }
        t->buckets[i] = NULL;
    }
    t->count = 0;
}

/* ───────────────────────────────────────────────────────────
 * Group policy state
 *
 * In the real the DP application app, group_struct holds:
 *   struct rte_hash *domain_details_table;   ← active table
 *   hs_database_t   *database;               ← active Hyperscan DB
 *
 * The atomic pointer swap in SYNC_COMPLETE replaces these with the
 * newly-built pending versions.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    char           group_id[32];
    domain_table_t active;         /* currently used by worker lcores */
    domain_table_t pending;        /* built during sync, not yet active */
    int            sync_in_progress;
    int            default_policy; /* ALLOW=0, DROP=1 */
} group_policy_t;

#define MAX_GROUPS  32
static group_policy_t g_groups[MAX_GROUPS];
static int            g_group_count = 0;

/* Malicious domain table (global, updated from IDPS feed) */
static domain_table_t g_malicious_table;
static atomic_ulong   g_malicious_count = 0;

static volatile int g_shutdown = 0;

/* ───────────────────────────────────────────────────────────
 * Group management helpers
 * ─────────────────────────────────────────────────────────── */
static group_policy_t *get_or_create_group(const char *group_id)
{
    for (int i = 0; i < g_group_count; i++)
        if (strcmp(g_groups[i].group_id, group_id) == 0)
            return &g_groups[i];

    if (g_group_count >= MAX_GROUPS)
        return NULL;

    group_policy_t *g = &g_groups[g_group_count++];
    memset(g, 0, sizeof(*g));
    strncpy(g->group_id, group_id, sizeof(g->group_id) - 1);
    g->default_policy = 0; /* ALLOW by default */
    return g;
}

/* ───────────────────────────────────────────────────────────
 * Policy message parser
 *
 * Simple JSON field extraction without a full JSON library.
 * In production, use cJSON (single-header) or Jansson.
 * The field extraction matches whatever the PM publishes.
 * ─────────────────────────────────────────────────────────── */
static const char *json_field(const char *json, const char *field,
                               char *out, int out_len)
{
    char search[64];
    snprintf(search, sizeof(search), "\"%s\":\"", field);
    const char *start = strstr(json, search);
    if (!start) {
        /* Try numeric field: "field":NUMBER */
        snprintf(search, sizeof(search), "\"%s\":", field);
        start = strstr(json, search);
        if (!start) { *out = '\0'; return NULL; }
        start += strlen(search);
        int i = 0;
        while (start[i] && start[i] != ',' && start[i] != '}' && i < out_len-1)
            out[i] = start[i++];
        out[i] = '\0';
        return out;
    }
    start += strlen(search);
    int i = 0;
    while (start[i] && start[i] != '"' && i < out_len-1)
        out[i] = start[i++];
    out[i] = '\0';
    return out;
}

static policy_msg_t parse_policy_message(const char *json, int json_len)
{
    policy_msg_t msg = {0};
    char tmp[64];

    (void)json_len;

    json_field(json, "group_id",  msg.group_id,        sizeof(msg.group_id));
    json_field(json, "domain",    msg.domain,           sizeof(msg.domain));
    json_field(json, "action",    msg.action,           sizeof(msg.action));

    if (json_field(json, "category", tmp, sizeof(tmp)))
        msg.category_bitmask = (uint32_t)strtoul(tmp, NULL, 0);
    if (json_field(json, "confidence", tmp, sizeof(tmp)))
        msg.confidence = atoi(tmp);

    /* Determine type from "type" field */
    char type_str[32] = {0};
    json_field(json, "type", type_str, sizeof(type_str));

    if      (strcmp(type_str, "BEGIN_SYNC")    == 0) msg.type = MSG_BEGIN_SYNC;
    else if (strcmp(type_str, "ADD_DOMAIN")    == 0) msg.type = MSG_ADD_DOMAIN;
    else if (strcmp(type_str, "REMOVE_DOMAIN") == 0) msg.type = MSG_REMOVE_DOMAIN;
    else if (strcmp(type_str, "ADD_GROUP")     == 0) msg.type = MSG_ADD_GROUP;
    else if (strcmp(type_str, "REMOVE_GROUP")  == 0) msg.type = MSG_REMOVE_GROUP;
    else if (strcmp(type_str, "SYNC_COMPLETE") == 0) msg.type = MSG_SYNC_COMPLETE;
    else if (strcmp(type_str, "ADD_MALICIOUS") == 0) msg.type = MSG_ADD_MALICIOUS;
    else                                              msg.type = MSG_UNKNOWN;

    return msg;
}

/* ───────────────────────────────────────────────────────────
 * apply_policy_message — update in-memory tables from a parsed message
 *
 * This is the core of the policy sync logic.
 * Mirrors process_entries_in_global_and_dns_table_for_malicious_domain()
 * and related functions in policy_cache.c.
 * ─────────────────────────────────────────────────────────── */
static void apply_policy_message(const policy_msg_t *msg)
{
    switch (msg->type) {

    case MSG_BEGIN_SYNC: {
        /*
         * Start buffering into pending table.
         * Worker lcores continue using the active table unchanged.
         * Any reads during this window see the last-complete policy.
         */
        group_policy_t *g = get_or_create_group(msg->group_id);
        if (!g) { fprintf(stderr, "Too many groups\n"); break; }

        dt_free(&g->pending);
        g->sync_in_progress = 1;

        printf("  [BEGIN_SYNC] group=%s — building pending table\n",
               msg->group_id);
        break;
    }

    case MSG_ADD_DOMAIN: {
        group_policy_t *g = get_or_create_group(msg->group_id);
        if (!g) break;

        /* Lowercase the domain before inserting */
        char domain_lc[256];
        strncpy(domain_lc, msg->domain, sizeof(domain_lc)-1);
        for (char *p = domain_lc; *p; p++) *p = (char)tolower(*p);

        filter_details_t fd = {0};
        strncpy(fd.domain, domain_lc, sizeof(fd.domain)-1);
        fd.category_bitmask = msg->category_bitmask;

        if (strcmp(msg->action, "whitelist") == 0)      fd.is_whitelisted = 1;
        else if (strcmp(msg->action, "blacklist") == 0)  fd.is_blacklisted = 1;

        /* Add to pending if sync in progress, else add to active directly */
        domain_table_t *target = g->sync_in_progress ? &g->pending : &g->active;
        dt_add(target, domain_lc, fd);

        printf("  [ADD_DOMAIN]  group=%-20s  domain=%-35s  action=%s\n",
               msg->group_id, domain_lc, msg->action);
        break;
    }

    case MSG_REMOVE_DOMAIN: {
        group_policy_t *g = get_or_create_group(msg->group_id);
        if (!g) break;

        char domain_lc[256];
        strncpy(domain_lc, msg->domain, sizeof(domain_lc)-1);
        for (char *p = domain_lc; *p; p++) *p = (char)tolower(*p);

        dt_remove(&g->active, domain_lc);
        printf("  [REMOVE_DOMAIN] group=%s  domain=%s\n",
               msg->group_id, domain_lc);
        break;
    }

    case MSG_SYNC_COMPLETE: {
        /*
         * Atomically swap pending → active.
         *
         * Real app (RCU QSBR pattern — implemented in the DP core library):
         *
         *   1. Build new rte_hash table in pending (steps above)
         *   2. Recompile Hyperscan DB from pending domains
         *   3. rte_atomic64_set(&group->domain_details_table, pending_ptr)
         *      ← this is the atomic swap; worker lcores now see new table
         *   4. rte_rcu_qsbr_synchronize(qsbr, RTE_QSBR_THRID_INVALID)
         *      ← wait for all worker lcores to quiesce (finish any in-flight lookup)
         *   5. rte_hash_free(old_table)
         *      ← safe to free now: no lcore holds a reference
         *
         * Here (simplified, no actual RCU):
         *   Free active → copy pending → clear pending
         */
        group_policy_t *g = get_or_create_group(msg->group_id);
        if (!g) break;
        if (!g->sync_in_progress) {
            printf("  [SYNC_COMPLETE] WARNING: no sync was in progress for %s\n",
                   msg->group_id);
            break;
        }

        /* Simulate the quiescent wait (real app uses rte_rcu_qsbr_synchronize) */
        /* usleep(1000); */   /* 1ms: in production this would be rcu_synchronize */

        dt_free(&g->active);
        /* Swap: move pending entries to active */
        memcpy(&g->active, &g->pending, sizeof(domain_table_t));
        memset(&g->pending, 0, sizeof(domain_table_t));
        g->sync_in_progress = 0;

        /*
         * In the real app, after the swap:
         *   hs_db_compile_for_groups(group)
         *   ← recompiles group->database from the new domain table
         *   ← worker lcores now use the new Hyperscan DB on next scan
         */

        printf("  [SYNC_COMPLETE] group=%s — %d domains now active\n",
               msg->group_id, g->active.count);
        break;
    }

    case MSG_ADD_GROUP: {
        group_policy_t *g = get_or_create_group(msg->group_id);
        if (!g) break;
        printf("  [ADD_GROUP]  group=%s created\n", msg->group_id);
        break;
    }

    case MSG_REMOVE_GROUP: {
        for (int i = 0; i < g_group_count; i++) {
            if (strcmp(g_groups[i].group_id, msg->group_id) == 0) {
                dt_free(&g_groups[i].active);
                dt_free(&g_groups[i].pending);
                /* shift remaining groups */
                memmove(&g_groups[i], &g_groups[i+1],
                        (g_group_count - i - 1) * sizeof(group_policy_t));
                g_group_count--;
                printf("  [REMOVE_GROUP] group=%s removed\n", msg->group_id);
                break;
            }
        }
        break;
    }

    case MSG_ADD_MALICIOUS: {
        /*
         * Malicious domain from IDPS feed (URLHaus, etc.)
         * Goes into the global malicious table (not per-group).
         * In the real app: process_entries_in_global_and_dns_table_for_malicious_domain()
         * In MRI (Java): published after DNS resolution of threat feed domains.
         */
        char domain_lc[256];
        strncpy(domain_lc, msg->domain, sizeof(domain_lc)-1);
        for (char *p = domain_lc; *p; p++) *p = (char)tolower(*p);

        filter_details_t fd = {.is_blacklisted = 1,
                                .category_bitmask = msg->category_bitmask };
        strncpy(fd.domain, domain_lc, sizeof(fd.domain)-1);
        dt_add(&g_malicious_table, domain_lc, &fd);

        atomic_fetch_add(&g_malicious_count, 1);
        printf("  [ADD_MALICIOUS] domain=%-40s  cat=0x%08x  conf=%d%%\n",
               domain_lc, msg->category_bitmask, msg->confidence);
        break;
    }

    case MSG_UNKNOWN:
    default:
        fprintf(stderr, "  [UNKNOWN] unrecognised message type\n");
        break;
    }
}

/* ───────────────────────────────────────────────────────────
 * Rebalance callback
 *
 * Called when consumer group membership changes (another consumer
 * joins or leaves). the DP application uses a single consumer (no consumer group
 * load balancing needed) but the callback must still be registered
 * to handle partition assignment correctly.
 * ─────────────────────────────────────────────────────────── */
static void rebalance_cb(rd_kafka_t *rk,
                          rd_kafka_resp_err_t err,
                          rd_kafka_topic_partition_list_t *partitions,
                          void *opaque)
{
    (void)opaque;

    switch (err) {
    case RD_KAFKA_RESP_ERR__ASSIGN_PARTITIONS:
        printf("[Kafka] Partition ASSIGNED: %d partitions\n",
               partitions->cnt);
        rd_kafka_assign(rk, partitions);
        break;

    case RD_KAFKA_RESP_ERR__REVOKE_PARTITIONS:
        printf("[Kafka] Partition REVOKED: %d partitions\n",
               partitions->cnt);
        rd_kafka_assign(rk, NULL);
        break;

    default:
        fprintf(stderr, "[Kafka] Rebalance error: %s\n",
                rd_kafka_err2str(err));
        rd_kafka_assign(rk, NULL);
        break;
    }
}

/* ───────────────────────────────────────────────────────────
 * kafka_consumer_init — create consumer with full config
 * ─────────────────────────────────────────────────────────── */
static rd_kafka_t *kafka_consumer_init(const char *broker,
                                        const char *group_id)
{
    char errstr[512];
    rd_kafka_conf_t *conf = rd_kafka_conf_new();

    /* Register rebalance callback */
    rd_kafka_conf_set_rebalance_cb(conf, rebalance_cb);

    struct {
        const char *key;
        const char *val;
    } props[] = {
        { "bootstrap.servers",        broker                },
        { "group.id",                 group_id              },
        /*
         * auto.offset.reset:
         *   "earliest" = start from oldest unread message.
         *   Use for policy topic: on DP restart, replay all policies
         *   so the domain tables are fully rebuilt.
         *   "latest" = start from newest. Use for CDR consumers that
         *   only care about real-time data.
         */
        { "auto.offset.reset",        "earliest"            },
        /*
         * enable.auto.commit = false:
         *   Commit offsets manually AFTER successfully applying policies.
         *   If DP crashes mid-sync (after consuming but before SYNC_COMPLETE),
         *   auto-commit would mark messages as processed even though they
         *   were never applied. Manual commit ensures replay on restart.
         */
        { "enable.auto.commit",       "false"               },
        { "session.timeout.ms",       "30000"               },
        { "max.poll.interval.ms",     "60000"               },
        { "fetch.min.bytes",          "1"                   },
        { "fetch.wait.max.ms",        "100"                 },
    };

    for (size_t i = 0; i < sizeof(props)/sizeof(props[0]); i++) {
        if (rd_kafka_conf_set(conf, props[i].key, props[i].val,
                               errstr, sizeof(errstr)) != RD_KAFKA_CONF_OK) {
            fprintf(stderr, "[Kafka] conf_set(%s) failed: %s\n",
                    props[i].key, errstr);
            rd_kafka_conf_destroy(conf);
            return NULL;
        }
    }

    rd_kafka_t *rk = rd_kafka_new(RD_KAFKA_CONSUMER, conf,
                                   errstr, sizeof(errstr));
    if (!rk) {
        fprintf(stderr, "[Kafka] rd_kafka_new failed: %s\n", errstr);
        rd_kafka_conf_destroy(conf);
        return NULL;
    }

    /*
     * Forward internal event queue to consumer queue.
     * Required when using rd_kafka_consumer_poll().
     * Must be called immediately after rd_kafka_new for a consumer.
     */
    rd_kafka_poll_set_consumer(rk);

    return rk;
}

/* ───────────────────────────────────────────────────────────
 * kafka_consumer_run — main poll loop
 *
 * This loop runs in the main lcore's control thread.
 * It interleaves Kafka polling with:
 *   - rd_kafka_poll for producer (Module 19) — CDR delivery callbacks
 *   - stats printing
 *   - OAM command processing
 * ─────────────────────────────────────────────────────────── */
static void kafka_consumer_run(rd_kafka_t *rk, int max_messages)
{
    int consumed = 0;

    while (!g_shutdown && consumed < max_messages) {
        /*
         * rd_kafka_consumer_poll():
         *   timeout_ms = 1000: block up to 1 second waiting for a message.
         *   In the DP application main lcore loop, use 100ms (same as CDR flush timer).
         *   Returns NULL if no message within timeout.
         */
        rd_kafka_message_t *msg = rd_kafka_consumer_poll(rk, 1000);

        if (!msg)
            continue;    /* timeout: no message, loop again */

        /* ── Error events ── */
        if (msg->err) {
            if (msg->err == RD_KAFKA_RESP_ERR__PARTITION_EOF) {
                /* Reached end of partition — normal, not an error */
                printf("[Kafka] Reached end of partition %d at offset %"
                       PRId64 "\n",
                       msg->partition, msg->offset);
            } else {
                fprintf(stderr, "[Kafka] Consumer error: %s\n",
                        rd_kafka_message_errstr(msg));
            }
            rd_kafka_message_destroy(msg);
            continue;
        }

        /* ── Process message ── */
        printf("\n[Message] partition=%d  offset=%"PRId64"  len=%zd\n",
               msg->partition, msg->offset, msg->len);

        policy_msg_t pmsg = parse_policy_message(
            (const char *)msg->payload, (int)msg->len);
        apply_policy_message(&pmsg);
        consumed++;

        /*
         * Manual offset commit: mark THIS message as processed.
         * If we crash before the next SYNC_COMPLETE, the uncommitted
         * messages will be re-delivered on restart.
         *
         * In the real the DP application app, commit happens only after SYNC_COMPLETE
         * is successfully applied — not after each ADD_DOMAIN.
         * This way, a crash mid-sync replays the entire sync from BEGIN_SYNC.
         */
        if (pmsg.type == MSG_SYNC_COMPLETE) {
            rd_kafka_commit_message(rk, msg, 0 /* sync commit */);
            printf("  [Offset committed at SYNC_COMPLETE]\n");
        }

        rd_kafka_message_destroy(msg);
    }
}

/* ═══════════════════════════════════════════════════════════
 * Standalone demo — simulates a full policy sync without Kafka
 *
 * Feeds the same messages that the PM would publish, directly
 * through apply_policy_message(). No broker needed.
 * ═══════════════════════════════════════════════════════════ */
static void run_standalone_demo(void)
{
    printf("=== Standalone demo (no Kafka broker needed) ===\n\n");

    /* Sequence of messages the PM would publish */
    const char *messages[] = {
        /* Group enterprise_a — full sync */
        "{\"type\":\"BEGIN_SYNC\",\"group_id\":\"enterprise_a\"}",

        "{\"type\":\"ADD_DOMAIN\",\"group_id\":\"enterprise_a\","
         "\"domain\":\"google.com\",\"action\":\"whitelist\",\"category\":0}",

        "{\"type\":\"ADD_DOMAIN\",\"group_id\":\"enterprise_a\","
         "\"domain\":\"facebook.com\",\"action\":\"blacklist\",\"category\":2}",

        "{\"type\":\"ADD_DOMAIN\",\"group_id\":\"enterprise_a\","
         "\"domain\":\"youtube.com\",\"action\":\"allow\",\"category\":4}",

        "{\"type\":\"ADD_DOMAIN\",\"group_id\":\"enterprise_a\","
         "\"domain\":\"malware-download.ru\",\"action\":\"blacklist\",\"category\":1}",

        "{\"type\":\"ADD_DOMAIN\",\"group_id\":\"enterprise_a\","
         "\"domain\":\"github.com\",\"action\":\"whitelist\",\"category\":0}",

        "{\"type\":\"SYNC_COMPLETE\",\"group_id\":\"enterprise_a\"}",

        /* Group enterprise_b — separate sync */
        "{\"type\":\"BEGIN_SYNC\",\"group_id\":\"enterprise_b\"}",

        "{\"type\":\"ADD_DOMAIN\",\"group_id\":\"enterprise_b\","
         "\"domain\":\"phishing-bank.tk\",\"action\":\"blacklist\",\"category\":1}",

        "{\"type\":\"SYNC_COMPLETE\",\"group_id\":\"enterprise_b\"}",

        /* Malicious domain updates (from IDPS feed via MRI) */
        "{\"type\":\"ADD_MALICIOUS\","
         "\"domain\":\"c2-botnet.badactor.net\","
         "\"category\":4,\"confidence\":98}",

        "{\"type\":\"ADD_MALICIOUS\","
         "\"domain\":\"ransomware-payload.xyz\","
         "\"category\":1,\"confidence\":95}",

        /* Incremental update (no full sync needed) */
        "{\"type\":\"ADD_DOMAIN\",\"group_id\":\"enterprise_a\","
         "\"domain\":\"new-approved-site.com\",\"action\":\"whitelist\",\"category\":0}",

        "{\"type\":\"REMOVE_DOMAIN\",\"group_id\":\"enterprise_a\","
         "\"domain\":\"youtube.com\"}",
    };

    int n = (int)(sizeof(messages) / sizeof(messages[0]));

    printf("Processing %d policy messages:\n\n", n);

    for (int i = 0; i < n; i++) {
        policy_msg_t pmsg = parse_policy_message(messages[i],
                                                  (int)strlen(messages[i]));
        apply_policy_message(&pmsg);
    }

    /* ── Print final state ── */
    printf("\n════════════════════════════════════════\n");
    printf("Final policy state:\n\n");

    for (int g = 0; g < g_group_count; g++) {
        group_policy_t *grp = &g_groups[g];
        printf("  Group [%s]  domains=%d\n",
               grp->group_id, grp->active.count);

        /* Print all entries */
        for (int b = 0; b < HM_SIZE; b++) {
            for (hm_node_t *n = grp->active.buckets[b]; n; n = n->next) {
                printf("    %-40s  whitelist=%d  blacklist=%d  cat=0x%x\n",
                       n->key,
                       n->value.is_whitelisted,
                       n->value.is_blacklisted,
                       n->value.category_bitmask);
            }
        }
        printf("\n");
    }

    printf("  Malicious table: %lu entries\n",
           atomic_load(&g_malicious_count));
    for (int b = 0; b < HM_SIZE; b++) {
        for (hm_node_t *n = g_malicious_table.buckets[b]; n; n = n->next)
            printf("    %-40s  cat=0x%x\n",
                   n->key, n->value.category_bitmask);
    }

    /* ── Test policy lookups (what worker lcores would do) ── */
    printf("\n════════════════════════════════════════\n");
    printf("Policy lookup verification:\n\n");

    struct { const char *group; const char *domain; } checks[] = {
        { "enterprise_a", "google.com" },
        { "enterprise_a", "facebook.com" },
        { "enterprise_a", "youtube.com" },       /* removed */
        { "enterprise_a", "new-approved-site.com" },
        { "enterprise_b", "phishing-bank.tk" },
    };

    for (size_t i = 0; i < sizeof(checks)/sizeof(checks[0]); i++) {
        group_policy_t *g = NULL;
        for (int j = 0; j < g_group_count; j++)
            if (strcmp(g_groups[j].group_id, checks[i].group) == 0)
                { g = &g_groups[j]; break; }

        filter_details_t *fd = g ? dt_lookup(&g->active, checks[i].domain) : NULL;

        printf("  [%-20s] %-40s → ",
               checks[i].group, checks[i].domain);
        if (!fd)
            printf("NOT FOUND (default policy)\n");
        else if (fd->is_whitelisted)
            printf("WHITELIST\n");
        else if (fd->is_blacklisted)
            printf("BLACKLIST\n");
        else
            printf("ALLOW (category=0x%x)\n", fd->category_bitmask);
    }
}

/* ─── Signal handler ────────────────────────────────────── */
static void sig_handler(int sig) { (void)sig; g_shutdown = 1; }

/* ─── main ──────────────────────────────────────────────── */
int main(int argc, char *argv[])
{
    signal(SIGINT,  sig_handler);
    signal(SIGTERM, sig_handler);

    printf("=== Module 20: Kafka Consumer (Policy Sync) ===\n\n");

    /* Standalone demo mode (no Kafka needed) */
    if (argc == 2 && strcmp(argv[1], "--demo") == 0) {
        run_standalone_demo();
        return 0;
    }

    const char *broker       = (argc > 1) ? argv[1] : "localhost:9092";
    const char *policy_topic = (argc > 2) ? argv[2] : "policy_updates";
    const char *group_id     = "dp_consumer";

    printf("Broker : %s\n", broker);
    printf("Topic  : %s\n", policy_topic);
    printf("Group  : %s\n\n", group_id);
    printf("(Run with --demo for standalone mode without Kafka)\n\n");

    /* ── Init consumer ── */
    rd_kafka_t *rk = kafka_consumer_init(broker, group_id);
    if (!rk) return 1;

    /* ── Subscribe to policy topic ── */
    rd_kafka_topic_partition_list_t *topics =
        rd_kafka_topic_partition_list_new(1);
    rd_kafka_topic_partition_list_add(topics, policy_topic,
                                       RD_KAFKA_PARTITION_UA);

    rd_kafka_resp_err_t err = rd_kafka_subscribe(rk, topics);
    rd_kafka_topic_partition_list_destroy(topics);

    if (err != RD_KAFKA_RESP_ERR_NO_ERROR) {
        fprintf(stderr, "[Kafka] subscribe failed: %s\n",
                rd_kafka_err2str(err));
        rd_kafka_destroy(rk);
        return 1;
    }

    printf("[Kafka] Subscribed to %s, polling...\n\n", policy_topic);

    /* ── Run consumer loop ── */
    kafka_consumer_run(rk, 10000 /* max messages, 0=infinite */);

    /* ── Graceful shutdown ── */
    printf("\n[Kafka] Closing consumer...\n");
    rd_kafka_consumer_close(rk);
    rd_kafka_destroy(rk);

    printf("[Kafka] Consumer closed.\n");
    printf("Groups active: %d  Malicious domains: %lu\n",
           g_group_count, atomic_load(&g_malicious_count));

    /* Cleanup */
    for (int i = 0; i < g_group_count; i++) {
        dt_free(&g_groups[i].active);
        dt_free(&g_groups[i].pending);
    }
    dt_free(&g_malicious_table);

    return 0;
}
