/**
 * kafka_producer.c — Module 19: Kafka Producer (CDR Export)
 *
 * Every policy decision in the DP application generates a Charging Data Record (CDR):
 *   - Which subscriber (IP, subscriber ID) made a DNS query
 *   - To which domain (with category and group)
 *   - What the policy decision was (ALLOW / DROP / SINKHOLE)
 *   - When (millisecond timestamp)
 *
 * CDRs are published to a Kafka topic by each worker lcore.
 * Downstream microservices (billing, analytics, SIEM) consume the topic.
 *
 * In the real the DP application project:
 *   - One Kafka producer instance per application (shared, thread-safe)
 *   - Worker lcores batch CDRs locally (e.g., 1000 records)
 *   - On batch full or timeout: rd_kafka_produce() for each record
 *   - Main lcore calls rd_kafka_poll() in its control loop
 *   - At shutdown: rd_kafka_flush() then rd_kafka_destroy()
 *
 * This module also covers:
 *   - Producer config (broker, acks, retries, batch size)
 *   - Delivery report callback (confirm message delivered to broker)
 *   - Back-pressure handling (RD_KAFKA_RESP_ERR__QUEUE_FULL)
 *   - JSON CDR record format
 *   - Graceful shutdown with flush
 *
 * Requires: librdkafka
 *   RedHat/Rocky: dnf install librdkafka librdkafka-devel
 *   Ubuntu:       apt-get install librdkafka-dev
 *   From source:  https://github.com/confluentinc/librdkafka
 *
 * Run against a real Kafka broker:
 *   docker run -p 9092:9092 apache/kafka:3.7.0
 *   ./kafka_producer localhost:9092
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdatomic.h>
#include <time.h>
#include <signal.h>
#include <unistd.h>

#include <librdkafka/rdkafka.h>

/* ───────────────────────────────────────────────────────────
 * Policy decision codes — mirrors policy_cache.h
 * ─────────────────────────────────────────────────────────── */
#define ALLOW_PACKET      0
#define DROP_PACKET       1
#define PROCESS_WORKFLOW  2

/* ───────────────────────────────────────────────────────────
 * CDR record — one entry per policy decision
 *
 * In the real the DP application project, cdr fields are populated at the
 * point of policy decision in process_hyperscan_dns_for_group()
 * or fetch_group_url_details_for_dns(), then queued for batch export.
 * ─────────────────────────────────────────────────────────── */
typedef struct {
    uint64_t timestamp_ms;        /* Unix time in milliseconds           */
    uint32_t subscriber_ip;       /* subscriber IPv4, host byte order    */
    char     subscriber_id[32];   /* subscriber identifier               */
    char     domain[256];         /* queried domain name                 */
    uint16_t qtype;               /* DNS_TYPE_A=1 or DNS_TYPE_AAAA=28    */
    int      action;              /* ALLOW_PACKET / DROP / SINKHOLE      */
    uint32_t group_id;            /* enterprise group                    */
    uint32_t category_bitmask;    /* content category flags              */
} cdr_record_t;

/* ───────────────────────────────────────────────────────────
 * CDR batch — per-worker accumulator before Kafka publish
 *
 * In the DP application, each worker lcore accumulates CDRs locally to avoid
 * calling rd_kafka_produce() on every packet (syscall overhead).
 * When the batch fills or the flush timer fires, all pending CDRs
 * are submitted to the Kafka queue in one burst.
 * ─────────────────────────────────────────────────────────── */
#define CDR_BATCH_MAX     256   /* flush when this many CDRs pending */
#define CDR_FLUSH_MS      100   /* or flush every 100ms whichever first */

typedef struct {
    cdr_record_t records[CDR_BATCH_MAX];
    int          count;
    uint64_t     last_flush_ms;
} cdr_batch_t;

/* ───────────────────────────────────────────────────────────
 * Global Kafka state
 * ─────────────────────────────────────────────────────────── */
static rd_kafka_t       *g_producer  = NULL;
static rd_kafka_topic_t *g_topic_cdr = NULL;

/* Delivery report counters */
static atomic_ulong g_delivered   = 0;
static atomic_ulong g_failed      = 0;
static volatile int g_shutdown    = 0;

/* ───────────────────────────────────────────────────────────
 * get_timestamp_ms — millisecond-resolution Unix timestamp
 * ─────────────────────────────────────────────────────────── */
static uint64_t get_timestamp_ms(void)
{
    struct timespec ts;
    clock_gettime(CLOCK_REALTIME, &ts);
    return (uint64_t)ts.tv_sec * 1000ULL + (uint64_t)ts.tv_nsec / 1000000ULL;
}

/* ───────────────────────────────────────────────────────────
 * cdr_to_json — serialise a CDR record to a JSON string
 *
 * In production, Protobuf or Avro gives better efficiency.
 * JSON is used here for readability — easy to inspect with
 * kafka-console-consumer.
 * ─────────────────────────────────────────────────────────── */
static int cdr_to_json(const cdr_record_t *rec, char *buf, int buf_len)
{
    const char *action_str =
        rec->action == ALLOW_PACKET     ? "allow"    :
        rec->action == DROP_PACKET      ? "drop"     :
        rec->action == PROCESS_WORKFLOW ? "sinkhole" : "unknown";

    return snprintf(buf, buf_len,
        "{"
        "\"ts\":%"PRIu64","
        "\"ip\":\"%u.%u.%u.%u\","
        "\"subscriber_id\":\"%s\","
        "\"domain\":\"%s\","
        "\"qtype\":%u,"
        "\"action\":\"%s\","
        "\"group\":%u,"
        "\"category\":\"0x%08x\""
        "}",
        rec->timestamp_ms,
        (rec->subscriber_ip >> 24) & 0xFF,
        (rec->subscriber_ip >> 16) & 0xFF,
        (rec->subscriber_ip >>  8) & 0xFF,
         rec->subscriber_ip        & 0xFF,
        rec->subscriber_id,
        rec->domain,
        rec->qtype,
        action_str,
        rec->group_id,
        rec->category_bitmask);
}

/* ───────────────────────────────────────────────────────────
 * Delivery report callback
 *
 * Called by librdkafka (from rd_kafka_poll()) for every message
 * that has been acknowledged by the broker (or failed).
 *
 * This is the only place you know a message is truly delivered.
 * "rd_kafka_produce returned 0" only means the message entered
 * the local queue — it doesn't mean the broker received it.
 *
 * In the real the DP application app, delivery failures trigger a LOG_WARN
 * and a counter increment. CDRs are considered best-effort —
 * re-transmission is not implemented (acceptable for CDR loss < 0.01%).
 *
 * The callback runs in the rd_kafka_poll() thread context —
 * which in the DP application is the main lcore's control loop.
 * DO NOT call heavy work here; just update counters and log.
 * ─────────────────────────────────────────────────────────── */
static void delivery_report_cb(rd_kafka_t *rk,
                                 const rd_kafka_message_t *msg,
                                 void *opaque)
{
    (void)rk;
    (void)opaque;

    if (msg->err) {
        fprintf(stderr,
                "[Kafka] Delivery FAILED: topic=%s  err=%s\n",
                rd_kafka_topic_name(msg->rkt),
                rd_kafka_err2str(msg->err));
        atomic_fetch_add(&g_failed, 1);
    } else {
        /*
         * msg->offset: the offset this message was assigned in the topic partition.
         * msg->partition: which partition it landed on.
         * In production logs, include these for end-to-end message tracing.
         */
        atomic_fetch_add(&g_delivered, 1);
    }
}

/* ───────────────────────────────────────────────────────────
 * kafka_producer_init — create producer with full config
 *
 * Mirrors the Kafka init in the DP application app_main.c:
 *
 *   const char *broker = config_get_string(&cfg, "kafka", "broker", "...");
 *   kafka_producer_init(broker, topic_cdr);
 *
 * Key config properties explained:
 *
 *   bootstrap.servers  : broker address(es)
 *   acks               : "all" = wait for all replicas (durability)
 *                        "1"   = wait for leader only (faster, less durable)
 *                        "0"   = fire-and-forget (fastest, data loss risk)
 *                        the DP application uses "1" for CDR — acceptable small loss
 *   retries            : retry on transient network errors
 *   retry.backoff.ms   : wait between retries
 *   batch.size         : max bytes to batch before sending (throughput)
 *   linger.ms          : wait up to N ms to accumulate more messages
 *                        (batch efficiency vs latency trade-off)
 *   compression.type   : snappy/lz4 reduces Kafka network/storage load
 *   queue.buffering.max.messages : max messages in local queue before
 *                        rd_kafka_produce returns QUEUE_FULL
 * ─────────────────────────────────────────────────────────── */
int kafka_producer_init(const char *broker, const char *topic_name)
{
    char errstr[512];

    /* ── Step 1: create config object ── */
    rd_kafka_conf_t *conf = rd_kafka_conf_new();

    /* Register delivery report callback */
    rd_kafka_conf_set_dr_msg_cb(conf, delivery_report_cb);

    /* ── Step 2: set config properties ── */
    struct {
        const char *key;
        const char *val;
    } props[] = {
        { "bootstrap.servers",              broker           },
        { "acks",                           "1"              },
        { "retries",                        "3"              },
        { "retry.backoff.ms",               "100"            },
        { "batch.size",                     "65536"          }, /* 64KB */
        { "linger.ms",                      "5"              }, /* 5ms batching */
        { "compression.type",               "snappy"         },
        { "queue.buffering.max.messages",   "100000"         },
        { "queue.buffering.max.kbytes",     "102400"         }, /* 100MB */
        { "socket.keepalive.enable",        "true"           },
        /* Log level: 0=emerg..7=debug. Use 3 (err) in production. */
        { "log_level",                      "3"              },
    };

    for (size_t i = 0; i < sizeof(props)/sizeof(props[0]); i++) {
        rd_kafka_conf_res_t res = rd_kafka_conf_set(conf,
                                                     props[i].key, props[i].val,
                                                     errstr, sizeof(errstr));
        if (res != RD_KAFKA_CONF_OK) {
            fprintf(stderr, "[Kafka] conf_set(%s=%s) failed: %s\n",
                    props[i].key, props[i].val, errstr);
            rd_kafka_conf_destroy(conf);
            return -1;
        }
    }

    /* ── Step 3: create producer instance ── */
    g_producer = rd_kafka_new(RD_KAFKA_PRODUCER, conf, errstr, sizeof(errstr));
    if (!g_producer) {
        fprintf(stderr, "[Kafka] rd_kafka_new failed: %s\n", errstr);
        /* conf is freed by rd_kafka_new on success; on failure, free it */
        rd_kafka_conf_destroy(conf);
        return -1;
    }
    /* NOTE: conf is now owned by g_producer, do NOT call rd_kafka_conf_destroy */

    printf("[Kafka] Producer created, connecting to %s\n", broker);

    /* ── Step 4: create topic handle ── */
    rd_kafka_topic_conf_t *topic_conf = rd_kafka_topic_conf_new();

    g_topic_cdr = rd_kafka_topic_new(g_producer, topic_name, topic_conf);
    if (!g_topic_cdr) {
        fprintf(stderr, "[Kafka] rd_kafka_topic_new(%s) failed: %s\n",
                topic_name, rd_kafka_err2str(rd_kafka_last_error()));
        rd_kafka_destroy(g_producer);
        g_producer = NULL;
        return -1;
    }
    /* NOTE: topic_conf owned by g_topic_cdr after this */

    printf("[Kafka] Topic handle created: %s\n", topic_name);
    return 0;
}

/* ───────────────────────────────────────────────────────────
 * kafka_produce_cdr — publish one CDR record
 *
 * Called from cdr_flush_batch() with each buffered CDR.
 * Mirrors the rd_kafka_produce() call in the real the DP application app.
 *
 * The subscriber IP is used as the message KEY.
 * Kafka partitions messages by key hash — all CDRs for the same
 * subscriber land in the same partition, preserving per-subscriber order.
 * ─────────────────────────────────────────────────────────── */
static int kafka_produce_cdr(const cdr_record_t *rec)
{
    char json_buf[512];
    int  json_len = cdr_to_json(rec, json_buf, sizeof(json_buf));
    if (json_len <= 0) return -1;

    /* Message key: subscriber IP (4 bytes, network byte order) */
    uint32_t key_ip = htonl(rec->subscriber_ip);

    int err = rd_kafka_produce(
        g_topic_cdr,
        RD_KAFKA_PARTITION_UA,      /* UA = let Kafka choose partition by key */
        RD_KAFKA_MSG_F_COPY,        /* copy payload: buffer can be reused after return */
        json_buf, (size_t)json_len, /* payload + len */
        &key_ip, sizeof(key_ip),   /* key + key_len: subscriber IP */
        NULL                        /* opaque: passed to delivery callback */
    );

    if (err == -1) {
        rd_kafka_resp_err_t kafka_err = rd_kafka_last_error();

        if (kafka_err == RD_KAFKA_RESP_ERR__QUEUE_FULL) {
            /*
             * Local message queue is full — broker is unreachable or
             * too slow to consume. Back-pressure: call poll() to trigger
             * delivery callbacks and free queue space, then retry.
             *
             * In the DP application, the CDR batch is simply dropped if the queue
             * stays full (CDR loss is acceptable; packet processing is not).
             */
            fprintf(stderr, "[Kafka] Queue full — retrying after poll\n");
            rd_kafka_poll(g_producer, 100);  /* 100ms */
            /* retry once */
            err = rd_kafka_produce(g_topic_cdr, RD_KAFKA_PARTITION_UA,
                                    RD_KAFKA_MSG_F_COPY,
                                    json_buf, (size_t)json_len,
                                    &key_ip, sizeof(key_ip), NULL);
        }

        if (err == -1) {
            fprintf(stderr, "[Kafka] produce failed: %s\n",
                    rd_kafka_err2str(rd_kafka_last_error()));
            return -1;
        }
    }

    /*
     * rd_kafka_poll(rk, 0) — non-blocking poll.
     * Triggers delivery callbacks for any messages that have been
     * acknowledged since last poll. Must be called regularly.
     * In the DP application main lcore control loop: rd_kafka_poll(producer, 0).
     * Passing 0 means "return immediately, process any pending callbacks".
     */
    rd_kafka_poll(g_producer, 0);
    return 0;
}

/* ───────────────────────────────────────────────────────────
 * cdr_batch_add — add a record to the per-worker batch
 *
 * In the real the DP application worker lcore:
 *   cdr_batch_add(&worker_info->cdr_batch, &rec);
 * called at every policy decision point in the hot path.
 * ─────────────────────────────────────────────────────────── */
static void cdr_batch_add(cdr_batch_t *batch, const cdr_record_t *rec)
{
    batch->records[batch->count++] = *rec;

    /* Flush when batch is full */
    if (batch->count >= CDR_BATCH_MAX) {
        for (int i = 0; i < batch->count; i++)
            kafka_produce_cdr(&batch->records[i]);
        printf("[CDR] Batch flushed: %d records\n", batch->count);
        batch->count         = 0;
        batch->last_flush_ms = get_timestamp_ms();
    }
}

/* ───────────────────────────────────────────────────────────
 * cdr_batch_flush_if_timeout — time-based flush
 *
 * Called from the main lcore control loop every 100ms.
 * Ensures CDRs are exported even when traffic is low (batch never fills).
 * ─────────────────────────────────────────────────────────── */
static void cdr_batch_flush_if_timeout(cdr_batch_t *batch)
{
    uint64_t now = get_timestamp_ms();
    if (batch->count > 0 &&
        (now - batch->last_flush_ms) >= CDR_FLUSH_MS) {
        for (int i = 0; i < batch->count; i++)
            kafka_produce_cdr(&batch->records[i]);
        printf("[CDR] Timer flush: %d records\n", batch->count);
        batch->count         = 0;
        batch->last_flush_ms = now;
    }
}

/* ───────────────────────────────────────────────────────────
 * kafka_producer_shutdown — graceful flush + destroy
 *
 * CRITICAL: must be called before process exit.
 * Messages in the local queue that haven't been sent yet will be
 * lost if rd_kafka_destroy() is called without flushing first.
 *
 * rd_kafka_flush() blocks until all queued messages are sent
 * (or timeout expires). In the real app: timeout = 10000ms (10s).
 * ─────────────────────────────────────────────────────────── */
void kafka_producer_shutdown(void)
{
    if (!g_producer) return;

    printf("[Kafka] Flushing pending messages (timeout 5s)...\n");

    /*
     * rd_kafka_flush() blocks the calling thread until:
     *   - All queued messages are delivered (or failed)
     *   - OR timeout expires
     * Returns RD_KAFKA_RESP_ERR__TIMED_OUT if timeout was reached.
     */
    rd_kafka_resp_err_t err = rd_kafka_flush(g_producer, 5000);
    if (err == RD_KAFKA_RESP_ERR__TIMED_OUT)
        fprintf(stderr, "[Kafka] Flush timed out — some CDRs may be lost\n");
    else
        printf("[Kafka] Flush complete\n");

    printf("[Kafka] delivered=%" PRIu64 "  failed=%" PRIu64 "\n",
           atomic_load(&g_delivered), atomic_load(&g_failed));

    if (g_topic_cdr) {
        rd_kafka_topic_destroy(g_topic_cdr);
        g_topic_cdr = NULL;
    }
    rd_kafka_destroy(g_producer);
    g_producer = NULL;
}

/* ─── Signal handler ────────────────────────────────────── */
static void sig_handler(int sig) { (void)sig; g_shutdown = 1; }

/* ═══════════════════════════════════════════════════════════
 * Demo: simulate the DP application CDR export flow
 *
 * Generates 500 simulated CDR records across 3 workers,
 * exports them to Kafka in batches, then does a timer-based flush.
 * ═══════════════════════════════════════════════════════════ */

/* Simulate one DNS packet policy decision → CDR record */
static cdr_record_t make_test_cdr(int seq)
{
    static const char *domains[] = {
        "google.com", "facebook.com", "ads.doubleclick.net",
        "malware.ru", "github.com", "streaming.netflix.com",
        "tracker.adnxs.com", "api.internal.corp", "cdn.akamai.net"
    };
    static const int actions[] = {
        ALLOW_PACKET, PROCESS_WORKFLOW, PROCESS_WORKFLOW,
        PROCESS_WORKFLOW, ALLOW_PACKET, DROP_PACKET,
        DROP_PACKET, ALLOW_PACKET, ALLOW_PACKET
    };

    cdr_record_t rec = {0};
    int idx = seq % 9;

    rec.timestamp_ms    = get_timestamp_ms();
    rec.subscriber_ip   = 0xC0A80100 + (seq % 100);  /* 198.51.100.X */
    snprintf(rec.subscriber_id, sizeof(rec.subscriber_id), "subscriber-%09d", seq % 1000000000);
    strncpy(rec.domain, domains[idx], sizeof(rec.domain) - 1);
    rec.qtype           = (seq % 3 == 0) ? 28 : 1;  /* mix A and AAAA */
    rec.action          = actions[idx];
    rec.group_id        = (uint32_t)(seq % 5 + 1);
    rec.category_bitmask= (idx == 1) ? 0x2 : (idx == 5) ? 0x4 : 0;

    return rec;
}

int main(int argc, char *argv[])
{
    const char *broker     = (argc > 1) ? argv[1] : "localhost:9092";
    const char *topic_name = (argc > 2) ? argv[2] : "dp_cdr";

    signal(SIGINT,  sig_handler);
    signal(SIGTERM, sig_handler);

    printf("=== Module 19: Kafka Producer (CDR Export) ===\n\n");
    printf("Broker     : %s\n", broker);
    printf("Topic      : %s\n", topic_name);
    printf("Batch size : %d records\n", CDR_BATCH_MAX);
    printf("Flush timer: %d ms\n\n", CDR_FLUSH_MS);

    /* ── Init Kafka producer ── */
    if (kafka_producer_init(broker, topic_name) < 0) {
        fprintf(stderr, "Failed to initialise Kafka producer\n");
        return 1;
    }

    /* ── Simulate 3 worker lcores with their own CDR batches ── */
    cdr_batch_t worker_batches[3];
    for (int w = 0; w < 3; w++) {
        memset(&worker_batches[w], 0, sizeof(cdr_batch_t));
        worker_batches[w].last_flush_ms = get_timestamp_ms();
    }

    printf("\n[Simulation] Generating CDR records across 3 workers...\n\n");

    int total_records = 500;
    for (int i = 0; i < total_records && !g_shutdown; i++) {
        int worker_id = i % 3;
        cdr_record_t rec = make_test_cdr(i);

        if (i < 5) {
            /* Show first few records */
            char json[512];
            cdr_to_json(&rec, json, sizeof(json));
            printf("[Worker %d] CDR #%d: %s\n", worker_id, i, json);
        }

        cdr_batch_add(&worker_batches[worker_id], &rec);

        /*
         * Main lcore control loop: every ~100ms, poll for delivery
         * callbacks and flush timed-out batches.
         * In the DP application this is the main lcore's while(running) loop.
         */
        if (i % 100 == 0) {
            rd_kafka_poll(g_producer, 0);   /* process delivery callbacks */
            for (int w = 0; w < 3; w++)
                cdr_batch_flush_if_timeout(&worker_batches[w]);
        }
    }

    /* Flush remaining partial batches */
    printf("\n[Flush] Flushing remaining partial batches...\n");
    for (int w = 0; w < 3; w++) {
        if (worker_batches[w].count > 0) {
            for (int i = 0; i < worker_batches[w].count; i++)
                kafka_produce_cdr(&worker_batches[w].records[i]);
            printf("[Worker %d] Final flush: %d records\n",
                   w, worker_batches[w].count);
            worker_batches[w].count = 0;
        }
    }

    /* Graceful shutdown */
    kafka_producer_shutdown();

    printf("\n=== Summary ===\n");
    printf("  Total CDRs generated : %d\n", total_records);
    printf("  Delivered to broker  : %lu\n", atomic_load(&g_delivered));
    printf("  Failed               : %lu\n", atomic_load(&g_failed));

    if (atomic_load(&g_failed) == 0 && atomic_load(&g_delivered) > 0)
        printf("\nAll CDRs delivered successfully. "
               "Check with kafka-console-consumer:\n"
               "  kafka-console-consumer.sh --topic %s "
               "--from-beginning --bootstrap-server %s\n",
               topic_name, broker);
    else if (atomic_load(&g_delivered) == 0)
        printf("\nNo messages delivered. Is Kafka running at %s?\n"
               "Start with: docker run -p 9092:9092 apache/kafka:3.7.0\n",
               broker);

    return 0;
}
