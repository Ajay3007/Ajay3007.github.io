---
title: "Backend Engineering"
tagline: "HTTP fundamentals to production-hardened systems."
description: "Home / Learning / Backend Engineering Roadmap Backend Engineering Roadmap A structured, hands-on path from web fundamentals to production-grade distributed systems — with C/C++…"
domain: engineering
order: 1
status: active
url: /learning/backend/backend-roadmap/
---

<link rel="stylesheet" href="/assets/css/backend-roadmap.css">

<div class="be-breadcrumb">
  <a href="/">Home</a>
  <span>/</span>
  <a href="/learning/">Learning</a>
  <span>/</span>
  Backend Engineering Roadmap
</div>
<div class="be-hero">
  <h1>Backend Engineering Roadmap</h1>
  <p>A structured, hands-on path from web fundamentals to production-grade distributed systems — with C/C++ examples, concept checklists, and interactive progress tracking.</p>
  <div class="be-hero-stats">
    <div><span class="be-stat-val">8</span><span class="be-stat-lbl">Phases</span></div>
    <div><span class="be-stat-val">80</span><span class="be-stat-lbl">Concepts</span></div>
    <div><span class="be-stat-val">8</span><span class="be-stat-lbl">Code Examples</span></div>
    <div><span class="be-stat-val">∞</span><span class="be-stat-lbl">Depth</span></div>
  </div>
</div>
<div class="be-overall-progress">
  <span class="be-op-label">Overall Progress</span>
  <div class="be-op-bar-wrap"><div class="be-op-bar"></div></div>
  <span class="be-op-pct">0%</span>
  <span class="be-op-count">0 of 80 concepts checked</span>
</div>
<nav class="be-phase-nav">
  <div class="be-phase-pills">
    <a class="ch-pill" href="#ph0">Ph0 — Web Basics <span class="pill-count">0/8</span></a>
    <a class="ch-pill" href="#ph1">Ph1 — API Design <span class="pill-count">0/10</span></a>
    <a class="ch-pill" href="#ph2">Ph2 — Databases <span class="pill-count">0/12</span></a>
    <a class="ch-pill" href="#ph3">Ph3 — Auth &amp; Authz <span class="pill-count">0/8</span></a>
    <a class="ch-pill" href="#ph4">Ph4 — Concurrency <span class="pill-count">0/10</span></a>
    <a class="ch-pill" href="#ph5">Ph5 — Event-Driven <span class="pill-count">0/10</span></a>
    <a class="ch-pill" href="#ph6">Ph6 — Microservices <span class="pill-count">0/10</span></a>
    <a class="ch-pill" href="#ph7">Ph7 — Observability <span class="pill-count">0/12</span></a>
  </div>
</nav>
<div class="be-phases">
<!-- ═══════════════════════════════════════════════════════════
     Ph0 — How the Web Works
     ═══════════════════════════════════════════════════════════ -->
<div class="ch-card" id="ph0" data-ch="ph0" style="--ch-accent: linear-gradient(90deg,#00c9a7,#00b4d8);">
  <div class="ch-header">
    <div class="ch-num">Ph0</div>
    <div class="ch-title-wrap">
      <div class="ch-title">How the Web Works</div>
      <div class="ch-meta">
        <span class="ch-badge">Prerequisite</span>
        <span class="ch-badge">No Prereqs</span>
        <a href="/learning/backend/m01-dns-tcp-tls/" class="ch-badge notes-live">📄 M01 Notes</a>
        <a href="/learning/backend/m02-http-servers/" class="ch-badge notes-live">📄 M02 Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/8 checked</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Concepts</div>
    <div class="be-concept-box">
      <ul>
        <li><strong>DNS resolution:</strong> recursive vs iterative queries, TTL, caching chain (browser → OS → recursive resolver → root nameserver → TLD → authoritative)</li>
        <li><strong>TCP three-way handshake:</strong> SYN → SYN-ACK → ACK; connection teardown FIN/FIN-ACK/ACK; RST for abrupt close</li>
        <li><strong>TLS 1.3 handshake:</strong> ClientHello (supported ciphers + key_share), ServerHello + Certificate + CertificateVerify, Finished; ECDHE forward secrecy</li>
        <li><strong>HTTP/1.1:</strong> persistent connections (Keep-Alive), pipelining, head-of-line blocking at TCP layer</li>
        <li><strong>HTTP/2:</strong> binary framing, multiplexing (multiple streams over single TCP), HPACK header compression, server push; still has TCP HOL blocking</li>
        <li><strong>HTTP/3 + QUIC:</strong> runs over UDP, built-in TLS 1.3, independent streams (no HOL blocking), 0-RTT resumption</li>
        <li><strong>Web server accept loop:</strong> listen socket + <code>SO_REUSEADDR</code>/<code>SO_REUSEPORT</code>, <code>accept()</code> blocks until client connects; thread-per-request (Apache) vs event loop (Nginx/epoll)</li>
        <li><strong>Backend request lifecycle:</strong> accept → parse HTTP → route to handler → middleware chain → business logic → DB query → serialize response → send</li>
      </ul>
    </div>
    <div class="ch-section-label">Technologies &amp; Tools</div>
    <div class="be-tools">
      <span class="be-tool-badge">TCP/IP</span>
      <span class="be-tool-badge">TLS 1.3</span>
      <span class="be-tool-badge">HTTP/1.1</span>
      <span class="be-tool-badge">HTTP/2</span>
      <span class="be-tool-badge">HTTP/3</span>
      <span class="be-tool-badge">QUIC</span>
      <span class="be-tool-badge">DNS</span>
      <span class="be-tool-badge">Wireshark</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C Example</button>
    <div class="code-block-wrap">
```c
/* Minimal TCP server skeleton — illustrates accept loop */
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <string.h>

int main(void) {
    int srv = socket(AF_INET, SOCK_STREAM, 0);

    int opt = 1;
    setsockopt(srv, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family      = AF_INET;
    addr.sin_port        = htons(8080);
    addr.sin_addr.s_addr = INADDR_ANY;

    bind(srv, (struct sockaddr *)&addr, sizeof(addr));
    listen(srv, SOMAXCONN);   /* SOMAXCONN = OS backlog limit */

    while (1) {
        int client = accept(srv, NULL, NULL);  /* blocks until client connects */
        /* hand off: thread-per-request -> pthread_create()  */
        /*           event loop          -> epoll_ctl(ADD)   */
        close(client);
    }
}
```
    </div>
    <div class="ch-section-label">Concept Checklist</div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Concept</th><th>Category</th></tr></thead>
      <tbody>
        <tr data-key="ph0-c1"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td>DNS resolution and caching chain (resolver → root → TLD → authoritative)</td><td><span class="cat-badge">Network</span></td></tr>
        <tr data-key="ph0-c2"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td>TCP 3-way handshake and connection teardown (FIN/RST)</td><td><span class="cat-badge">Network</span></td></tr>
        <tr data-key="ph0-c3"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td>TLS 1.3 handshake: ECDHE key exchange and forward secrecy</td><td><span class="cat-badge">Security</span></td></tr>
        <tr data-key="ph0-c4"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td>HTTP/1.1: persistent connections, pipelining, HOL blocking</td><td><span class="cat-badge">HTTP</span></td></tr>
        <tr data-key="ph0-c5"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td>HTTP/2: multiplexing, binary framing, HPACK compression</td><td><span class="cat-badge">HTTP</span></td></tr>
        <tr data-key="ph0-c6"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td>HTTP/3 + QUIC: UDP-based, independent streams, 0-RTT</td><td><span class="cat-badge">HTTP</span></td></tr>
        <tr data-key="ph0-c7"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td>Web server accept loop: thread-per-request vs event loop</td><td><span class="cat-badge">Server</span></td></tr>
        <tr data-key="ph0-c8"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td>Backend request lifecycle: accept → route → middleware → handler → DB → respond</td><td><span class="cat-badge">Server</span></td></tr>
      </tbody>
    </table>
  </div>
</div>
<!-- ═══════════════════════════════════════════════════════════
     Ph1 — API Design & Contracts
     ═══════════════════════════════════════════════════════════ -->
<div class="ch-card" id="ph1" data-ch="ph1" style="--ch-accent: linear-gradient(90deg,#3b82f6,#6366f1);">
  <div class="ch-header">
    <div class="ch-num">Ph1</div>
    <div class="ch-title-wrap">
      <div class="ch-title">API Design &amp; Contracts</div>
      <div class="ch-meta">
        <span class="ch-badge">Foundational</span>
        <span class="ch-badge">Requires Ph0</span>
        <a href="/learning/backend/m03-rest/" class="ch-badge notes-live">📄 M03 Notes</a>
        <a href="/learning/backend/m04-grpc/" class="ch-badge notes-live">📄 M04 Notes</a>
        <a href="/learning/backend/m05-graphql/" class="ch-badge notes-live">📄 M05 Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/10 checked</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Concepts</div>
    <div class="be-concept-box">
      <ul>
        <li><strong>REST principles:</strong> resources as nouns (not verbs), stateless client-server, uniform interface, cacheable responses, layered system, optional HATEOAS</li>
        <li><strong>URL &amp; versioning:</strong> plural nouns (<code>/users</code> not <code>/user</code>), nested resources (<code>/users/42/orders</code>), versioning strategies — URI prefix (<code>/v1/</code>), Accept header (<code>application/vnd.api+json;version=1</code>), query param (<code>?version=1</code>)</li>
        <li><strong>HTTP method semantics:</strong> GET/HEAD (safe + idempotent), PUT/DELETE (idempotent, not safe), POST (neither), PATCH (partial update, should be idempotent in practice)</li>
        <li><strong>Status codes:</strong> 200 OK, 201 Created, 204 No Content, 301/302/304 redirects, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 409 Conflict, 422 Unprocessable Entity, 429 Too Many Requests, 500/502/503/504</li>
        <li><strong>Request/response shaping:</strong> direct payload vs envelope (<code>{data, meta, links}</code>), consistent error objects, snake_case vs camelCase field naming</li>
        <li><strong>Pagination:</strong> offset+limit (simple, but skips/duplicates on concurrent writes), cursor-based (stable, no skips), keyset pagination (most scalable); include <code>total_count</code>, <code>next_cursor</code> in response</li>
        <li><strong>Error standard:</strong> RFC 7807 Problem Details — <code>type</code> (URI), <code>title</code>, <code>status</code>, <code>detail</code>, <code>instance</code> fields; consistent error envelope across all endpoints</li>
        <li><strong>OpenAPI/Swagger:</strong> spec-first design philosophy, YAML schema, <code>$ref</code> for reusable components, code generation for servers (stub) and clients (SDK)</li>
        <li><strong>gRPC:</strong> Protocol Buffers IDL (<code>syntax = "proto3"</code>), service + rpc definitions, unary vs client-streaming vs server-streaming vs bidirectional-streaming; when to prefer (internal services, streaming, strong typing)</li>
        <li><strong>GraphQL:</strong> schema-first (SDL), resolvers, queries (read) vs mutations (write) vs subscriptions (realtime), N+1 problem (DataLoader batching solution)</li>
      </ul>
    </div>
    <div class="ch-section-label">Technologies &amp; Tools</div>
    <div class="be-tools">
      <span class="be-tool-badge">REST</span>
      <span class="be-tool-badge">gRPC</span>
      <span class="be-tool-badge">GraphQL</span>
      <span class="be-tool-badge">OpenAPI</span>
      <span class="be-tool-badge">Protobuf</span>
      <span class="be-tool-badge">Swagger</span>
      <span class="be-tool-badge">RFC 7807</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C Example</button>
    <div class="code-block-wrap">
```c
/* user.proto — gRPC service definition */
// syntax = "proto3";
//
// service UserService {
//   rpc GetUser (GetUserRequest)  returns (UserResponse);          // unary
//   rpc WatchUser (GetUserRequest) returns (stream UserResponse);  // server-streaming
// }
//
// message GetUserRequest { string user_id = 1; }
//
// message UserResponse {
//   string user_id    = 1;
//   string username   = 2;
//   string email      = 3;
//   int64  created_at = 4;   // Unix timestamp
// }

/* Minimal HTTP/1.1 response builder in C */
#include <stdio.h>
#include <string.h>
#include <unistd.h>

void send_json(int fd, int status, const char *body) {
    char header[512];
    int  body_len = (int)strlen(body);
    snprintf(header, sizeof(header),
        "HTTP/1.1 %d OK\r\n"
        "Content-Type: application/json\r\n"
        "Content-Length: %d\r\n"
        "Connection: close\r\n"
        "\r\n",
        status, body_len);
    write(fd, header, strlen(header));
    write(fd, body,   body_len);
}
```
    </div>
    <div class="ch-section-label">Concept Checklist</div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Concept</th><th>Category</th></tr></thead>
      <tbody>
        <tr data-key="ph1-c1"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td>REST constraints: statelessness, uniform interface, resource naming</td><td><span class="cat-badge">REST</span></td></tr>
        <tr data-key="ph1-c2"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td>URL design: plural nouns, nesting, versioning strategies (/v1/, header, query)</td><td><span class="cat-badge">REST</span></td></tr>
        <tr data-key="ph1-c3"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td>HTTP method idempotency: GET/PUT/DELETE vs POST/PATCH semantics</td><td><span class="cat-badge">REST</span></td></tr>
        <tr data-key="ph1-c4"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td>HTTP status code families and when to use each (2xx/3xx/4xx/5xx)</td><td><span class="cat-badge">REST</span></td></tr>
        <tr data-key="ph1-c5"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td>Pagination: offset vs cursor vs keyset — tradeoffs for each</td><td><span class="cat-badge">REST</span></td></tr>
        <tr data-key="ph1-c6"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td>RFC 7807 Problem Details: type, title, status, detail, instance</td><td><span class="cat-badge">API Design</span></td></tr>
        <tr data-key="ph1-c7"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td>OpenAPI spec-first design and code generation workflow</td><td><span class="cat-badge">API Design</span></td></tr>
        <tr data-key="ph1-c8"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td>gRPC: Protobuf IDL, service definition, 4 streaming modes</td><td><span class="cat-badge">gRPC</span></td></tr>
        <tr data-key="ph1-c9"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td>When to choose gRPC over REST (internal, streaming, strong typing)</td><td><span class="cat-badge">gRPC</span></td></tr>
        <tr data-key="ph1-c10"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td>GraphQL: schema, resolvers, N+1 problem and DataLoader solution</td><td><span class="cat-badge">GraphQL</span></td></tr>
      </tbody>
    </table>
  </div>
</div>
<!-- ═══════════════════════════════════════════════════════════
     Ph2 — Databases & Storage
     ═══════════════════════════════════════════════════════════ -->
<div class="ch-card" id="ph2" data-ch="ph2" style="--ch-accent: linear-gradient(90deg,#8b5cf6,#a855f7);">
  <div class="ch-header">
    <div class="ch-num">Ph2</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Databases &amp; Storage</div>
      <div class="ch-meta">
        <span class="ch-badge">Core</span>
        <span class="ch-badge">Requires Ph1</span>
        <a href="/learning/backend/m06-sql-indexing/" class="ch-badge notes-live">📄 M06 Notes</a>
        <a href="/learning/backend/m07-nosql/" class="ch-badge notes-live">📄 M07 Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/12 checked</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Concepts</div>
    <div class="be-concept-box">
      <ul>
        <li><strong>Relational schema design:</strong> normalization (1NF removes repeating groups, 2NF removes partial dependencies, 3NF removes transitive dependencies), ERD, foreign key constraints, check constraints</li>
        <li><strong>Indexes:</strong> B-tree (default, ordered, range queries), hash (equality only), composite (left-prefix rule), covering (index-only scan), partial/filtered; index selectivity; write amplification tradeoff</li>
        <li><strong>Query plans:</strong> <code>EXPLAIN ANALYZE</code> (actual rows, actual time), sequential scan vs index scan vs index-only scan, join algorithms (nested loop, hash join, merge join), planner statistics</li>
        <li><strong>Transactions &amp; ACID:</strong> Atomicity (all-or-nothing), Consistency (invariants preserved), Isolation (concurrent txns don't interfere), Durability (committed = persisted to WAL/disk)</li>
        <li><strong>Isolation levels:</strong> Read Uncommitted (dirty reads), Read Committed (default PostgreSQL), Repeatable Read (no phantom in MySQL InnoDB via MVCC), Serializable (SSI in PostgreSQL); phenomena: dirty read, non-repeatable read, phantom read</li>
        <li><strong>Deadlocks:</strong> detection (wait-for graph cycle), prevention (lock ordering — always acquire locks in same order), lock timeout (<code>lock_timeout = '2s'</code> in PostgreSQL), <code>SKIP LOCKED</code> for queue patterns</li>
        <li><strong>NoSQL taxonomy:</strong> document (MongoDB — flexible schema, nested objects), key-value (Redis — sub-ms latency), wide-column (Cassandra — write-optimized, partitioned by key), time-series (InfluxDB), graph (Neo4j); choose by access pattern</li>
        <li><strong>Redis data structures:</strong> string (counters, cache), hash (object fields), list (queues, stacks), set (unique members), sorted set (leaderboards, rate limiting), stream (event log); each with O() complexity</li>
        <li><strong>Caching patterns:</strong> cache-aside/lazy loading (app reads cache first, on miss reads DB and populates cache), read-through (cache fetches from DB), write-through (write to cache + DB sync), write-behind (async DB write)</li>
        <li><strong>Redis advanced:</strong> persistence modes (RDB — snapshot at intervals, AOF — append-only log, both for durability), pub/sub (fire-and-forget), Lua scripting (atomic multi-command), rate limiting with <code>INCR+EXPIRE</code></li>
        <li><strong>Connection pooling:</strong> why (TCP + auth handshake cost per connection), Little's Law (avg connections = arrival_rate × avg_latency), pgBouncer modes (session/transaction/statement), pool exhaustion and backpressure</li>
        <li><strong>Database migrations:</strong> versioned sequential scripts (Flyway/Liquibase pattern), forward-only vs rollback scripts, zero-downtime techniques: expand-contract (add column nullable → backfill → add NOT NULL → drop old column)</li>
      </ul>
    </div>
    <div class="ch-section-label">Technologies &amp; Tools</div>
    <div class="be-tools">
      <span class="be-tool-badge">PostgreSQL</span>
      <span class="be-tool-badge">MySQL</span>
      <span class="be-tool-badge">Redis</span>
      <span class="be-tool-badge">MongoDB</span>
      <span class="be-tool-badge">Cassandra</span>
      <span class="be-tool-badge">pgBouncer</span>
      <span class="be-tool-badge">hiredis</span>
      <span class="be-tool-badge">libpq</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C Example</button>
    <div class="code-block-wrap">
```c
/* PostgreSQL via libpq — parameterized query (prevents SQL injection) */
#include <libpq-fe.h>
#include <stdio.h>

void fetch_user(PGconn *conn, const char *user_id) {
    const char *params[1] = { user_id };
    PGresult *res = PQexecParams(conn,
        "SELECT id, name, email FROM users WHERE id = $1",
        1,    /* nParams */
        NULL, /* paramTypes  (let server infer) */
        params, NULL, NULL,
        0     /* result format: text */
    );
    if (PQresultStatus(res) == PGRES_TUPLES_OK && PQntuples(res) > 0) {
        printf("id=%-6s  name=%-20s  email=%s\n",
            PQgetvalue(res, 0, 0),
            PQgetvalue(res, 0, 1),
            PQgetvalue(res, 0, 2));
    }
    PQclear(res);
}

/* Redis cache-aside via hiredis */
#include <hiredis/hiredis.h>
#include <string.h>

/* Returns cached JSON string or NULL (caller must free reply) */
redisReply *get_user_cached(redisContext *rc, PGconn *pg,
                             const char *user_id)
{
    char key[64];
    snprintf(key, sizeof(key), "user:%s", user_id);

    redisReply *r = redisCommand(rc, "GET %s", key);
    if (r && r->type == REDIS_REPLY_STRING)
        return r;   /* cache HIT */

    freeReplyObject(r);

    /* cache MISS — query DB, then SET with 5-min TTL */
    /* fetch_user(pg, user_id) -> serialize to JSON ->  */
    /* redisCommand(rc, "SET %s %s EX 300", key, json_val) */
    return NULL;
}
```
    </div>
    <div class="ch-section-label">Concept Checklist</div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Concept</th><th>Category</th></tr></thead>
      <tbody>
        <tr data-key="ph2-c1"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td>Relational schema normalization: 1NF, 2NF, 3NF and when to denormalize</td><td><span class="cat-badge">SQL</span></td></tr>
        <tr data-key="ph2-c2"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td>Index types: B-tree, hash, composite, covering, partial; left-prefix rule</td><td><span class="cat-badge">SQL</span></td></tr>
        <tr data-key="ph2-c3"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td>Query plans: EXPLAIN ANALYZE, sequential scan vs index scan</td><td><span class="cat-badge">SQL</span></td></tr>
        <tr data-key="ph2-c4"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td>ACID properties and what each guarantees</td><td><span class="cat-badge">Transactions</span></td></tr>
        <tr data-key="ph2-c5"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td>Isolation levels: RC, RR, Serializable; dirty/phantom/non-repeatable reads</td><td><span class="cat-badge">Transactions</span></td></tr>
        <tr data-key="ph2-c6"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td>Deadlocks: detection, lock ordering prevention, SKIP LOCKED</td><td><span class="cat-badge">Transactions</span></td></tr>
        <tr data-key="ph2-c7"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td>NoSQL taxonomy: document, key-value, wide-column, time-series, graph — when to use</td><td><span class="cat-badge">NoSQL</span></td></tr>
        <tr data-key="ph2-c8"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td>Redis data structures and time complexity of each</td><td><span class="cat-badge">Redis</span></td></tr>
        <tr data-key="ph2-c9"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td>Caching patterns: cache-aside, read-through, write-through, write-behind</td><td><span class="cat-badge">Caching</span></td></tr>
        <tr data-key="ph2-c10"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td>Redis persistence: RDB vs AOF; pub/sub; Lua atomicity</td><td><span class="cat-badge">Redis</span></td></tr>
        <tr data-key="ph2-c11"><td class="solved-cell"><div class="solved-check"></div></td><td>11</td><td>Connection pooling: Little's Law, pgBouncer modes, pool exhaustion</td><td><span class="cat-badge">Performance</span></td></tr>
        <tr data-key="ph2-c12"><td class="solved-cell"><div class="solved-check"></div></td><td>12</td><td>Zero-downtime migrations: expand-contract pattern</td><td><span class="cat-badge">Migrations</span></td></tr>
      </tbody>
    </table>
  </div>
</div>
<!-- ═══════════════════════════════════════════════════════════
     Ph3 — Authentication & Authorization
     ═══════════════════════════════════════════════════════════ -->
<div class="ch-card" id="ph3" data-ch="ph3" style="--ch-accent: linear-gradient(90deg,#ef4444,#f97316);">
  <div class="ch-header">
    <div class="ch-num">Ph3</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Authentication &amp; Authorization</div>
      <div class="ch-meta">
        <span class="ch-badge">Core</span>
        <span class="ch-badge">Requires Ph1</span>
        <a href="/learning/backend/m09-auth-jwt/" class="ch-badge notes-live">📄 M09 Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/8 checked</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Concepts</div>
    <div class="be-concept-box">
      <ul>
        <li><strong>Session-based auth:</strong> server stores session state (in-memory or Redis), session ID in HttpOnly+Secure cookie, session fixation attack (regenerate session ID on login), CSRF protection (SameSite=Strict or CSRF token)</li>
        <li><strong>JWT structure:</strong> three base64url-encoded sections — header (alg, typ), payload (claims), signature; standard claims: <code>iss</code> (issuer), <code>sub</code> (subject), <code>aud</code> (audience), <code>exp</code> (expiry), <code>nbf</code> (not before), <code>iat</code> (issued at), <code>jti</code> (JWT ID for revocation)</li>
        <li><strong>JWT signing algorithms:</strong> HS256 (HMAC-SHA256, shared secret — symmetric, all services need secret), RS256 (RSA — private key signs, public key verifies — asymmetric, safe to distribute public key), ES256 (ECDSA, smaller keys than RSA)</li>
        <li><strong>Access + refresh token pattern:</strong> short-lived access token (15min–1hr, stateless validation), long-lived refresh token (7–30 days, stored in DB, one-time-use rotation, allows revocation)</li>
        <li><strong>OAuth2 flows:</strong> Authorization Code + PKCE (for SPAs and mobile — code verifier/challenge prevents interception), Client Credentials (machine-to-machine, no user), Device Code (CLI/TV apps — user visits URL on phone)</li>
        <li><strong>API Keys:</strong> generation (crypto/rand CSPRNG → hex or base62 encoding), never store plaintext (store SHA-256 hash + prefix for lookup), scoping to specific resources/operations, key rotation strategy</li>
        <li><strong>RBAC vs ABAC:</strong> Role-Based (user has role, role has permissions — simple, coarse-grained), Attribute-Based (policy: ALLOW if subject.dept == resource.dept AND action == "read" — flexible, complex); hybrid (RBAC for coarse, ABAC for fine-grained)</li>
        <li><strong>Password storage:</strong> why fast hashes are wrong (MD5/SHA256: billions/sec on GPU), bcrypt (configurable cost factor, ~100ms target), Argon2id (OWASP recommended — memory-hard, time-hard, side-channel resistant), always timing-safe comparison (constant-time memcmp)</li>
      </ul>
    </div>
    <div class="ch-section-label">Technologies &amp; Tools</div>
    <div class="be-tools">
      <span class="be-tool-badge">JWT</span>
      <span class="be-tool-badge">OAuth2</span>
      <span class="be-tool-badge">OpenSSL</span>
      <span class="be-tool-badge">bcrypt</span>
      <span class="be-tool-badge">Argon2</span>
      <span class="be-tool-badge">Redis (sessions)</span>
      <span class="be-tool-badge">PKCE</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C Example</button>
    <div class="code-block-wrap">
```c
/* JWT HMAC-SHA256 signature verification (OpenSSL) */
#include <openssl/hmac.h>
#include <openssl/evp.h>
#include <string.h>
#include <stdio.h>

/* Compare two byte arrays in constant time to prevent timing attacks */
static int const_time_cmp(const unsigned char *a,
                           const unsigned char *b, size_t len) {
    unsigned char diff = 0;
    for (size_t i = 0; i < len; i++)
        diff |= a[i] ^ b[i];
    return diff == 0;
}

/* Verify HS256: header_payload = "base64url(hdr).base64url(payload)" */
int jwt_verify_hs256(const char    *header_payload,
                     const unsigned char *expected_sig, size_t sig_len,
                     const unsigned char *secret,       size_t secret_len)
{
    unsigned char digest[EVP_MAX_MD_SIZE];
    unsigned int  digest_len = 0;

    HMAC(EVP_sha256(),
         secret,   (int)secret_len,
         (const unsigned char *)header_payload, strlen(header_payload),
         digest,  &digest_len);

    if (digest_len != sig_len) return 0;
    return const_time_cmp(digest, expected_sig, digest_len);
}
```
    </div>
    <div class="ch-section-label">Concept Checklist</div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Concept</th><th>Category</th></tr></thead>
      <tbody>
        <tr data-key="ph3-c1"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td>Session-based auth: HttpOnly cookie, Redis-backed sessions, session fixation</td><td><span class="cat-badge">Auth</span></td></tr>
        <tr data-key="ph3-c2"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td>JWT structure: header.payload.signature, standard claims (iss, sub, exp, jti)</td><td><span class="cat-badge">JWT</span></td></tr>
        <tr data-key="ph3-c3"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td>JWT signing: HS256 vs RS256 vs ES256 — symmetric vs asymmetric tradeoffs</td><td><span class="cat-badge">JWT</span></td></tr>
        <tr data-key="ph3-c4"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td>Access + refresh token pattern: rotation, revocation, short-lived access tokens</td><td><span class="cat-badge">JWT</span></td></tr>
        <tr data-key="ph3-c5"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td>OAuth2 flows: Authorization Code + PKCE, Client Credentials, Device Code</td><td><span class="cat-badge">OAuth2</span></td></tr>
        <tr data-key="ph3-c6"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td>API Keys: CSPRNG generation, hashing at rest, scoping, rotation</td><td><span class="cat-badge">API Security</span></td></tr>
        <tr data-key="ph3-c7"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td>RBAC vs ABAC: coarse-grained roles vs attribute-based policy evaluation</td><td><span class="cat-badge">Authorization</span></td></tr>
        <tr data-key="ph3-c8"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td>Password storage: bcrypt cost factor, Argon2id memory-hardness, timing-safe compare</td><td><span class="cat-badge">Security</span></td></tr>
      </tbody>
    </table>
  </div>
</div>
<!-- ═══════════════════════════════════════════════════════════
     Ph4 — Concurrency & Performance
     ═══════════════════════════════════════════════════════════ -->
<div class="ch-card" id="ph4" data-ch="ph4" style="--ch-accent: linear-gradient(90deg,#f59e0b,#f97316);">
  <div class="ch-header">
    <div class="ch-num">Ph4</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Concurrency &amp; Performance</div>
      <div class="ch-meta">
        <span class="ch-badge">Intermediate</span>
        <span class="ch-badge">Requires Ph0, Ph2</span>
        <a href="/learning/backend/m11-concurrency/" class="ch-badge notes-live">📄 M11 Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/10 checked</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Concepts</div>
    <div class="be-concept-box">
      <ul>
        <li><strong>Threading models:</strong> thread-per-request (simple, high memory — 8KB stack × 10K = 80MB+), thread pool with bounded queue (Apache worker MPM), event loop + I/O multiplexing (Nginx, Node.js), green threads/goroutines (M:N userspace scheduling)</li>
        <li><strong>Synchronization primitives:</strong> mutex (exclusive lock, binary), RW lock (multiple concurrent readers OR single writer), semaphore (counting lock, rate limiting), condition variable (wait for predicate — always pair with mutex), spinlock (busy-wait, only for very short critical sections on multi-core)</li>
        <li><strong>Lock-free programming:</strong> compare-and-swap (CAS) — atomically: if (*ptr == expected) { *ptr = desired; return true; }, ABA problem (use versioned pointers), GCC <code>__atomic</code> builtins (<code>__atomic_compare_exchange_n</code>), C11 <code>stdatomic.h</code></li>
        <li><strong>I/O multiplexing evolution:</strong> <code>select</code> (FD_SET bitmap, 1024 fd limit), <code>poll</code> (no fd limit, linear scan), <code>epoll</code> (Linux — O(1) notification, edge-triggered ET vs level-triggered LT, epoll_create1/epoll_ctl/epoll_wait), <code>io_uring</code> (Linux 5.1+ — async submit+complete ring buffers, zero-copy, no syscall per I/O)</li>
        <li><strong>C10K problem:</strong> 10,000 concurrent connections — why thread-per-request fails (OS scheduling overhead, stack memory), how epoll event loop solves it (single thread handles thousands of FDs)</li>
        <li><strong>In-process caching:</strong> LRU eviction (doubly-linked list + hash map = O(1) get/put), LFU (min-heap of frequency buckets), cache capacity planning (hot data &lt;&lt; cold data)</li>
        <li><strong>Distributed caching with Redis:</strong> cache stampede (thundering herd when TTL expires simultaneously — mutex lock, probabilistic early expiry, background refresh), hotspot key sharding, client-side consistent hashing</li>
        <li><strong>Connection pool management:</strong> pool exhaustion (queue vs reject vs timeout), health checks on idle connections (keepalive probe or validation query), backpressure signals upstream</li>
        <li><strong>Load balancing algorithms:</strong> round-robin (uniform distribution), weighted round-robin (heterogeneous backends), least-connections (for variable request durations), IP hash (session stickiness, avoid with horizontal scaling), consistent hashing (minimal key redistribution when nodes added/removed)</li>
        <li><strong>Horizontal scaling design:</strong> stateless services (no server-side session), shared-nothing architecture, externalizing state (Redis, DB), idempotent operations (safe to retry), eventual consistency tradeoffs</li>
      </ul>
    </div>
    <div class="ch-section-label">Technologies &amp; Tools</div>
    <div class="be-tools">
      <span class="be-tool-badge">epoll</span>
      <span class="be-tool-badge">io_uring</span>
      <span class="be-tool-badge">pthreads</span>
      <span class="be-tool-badge">stdatomic.h</span>
      <span class="be-tool-badge">Redis</span>
      <span class="be-tool-badge">pgBouncer</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C Example</button>
    <div class="code-block-wrap">
```c
/* epoll edge-triggered event loop skeleton (Linux) */
#include <sys/epoll.h>
#include <sys/socket.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

#define MAX_EVENTS 128

static void set_nonblocking(int fd) {
    int flags = fcntl(fd, F_GETFL, 0);
    fcntl(fd, F_SETFL, flags | O_NONBLOCK);
}

void run_event_loop(int listen_fd) {
    int epfd = epoll_create1(EPOLL_CLOEXEC);

    struct epoll_event ev;
    ev.events  = EPOLLIN;
    ev.data.fd = listen_fd;
    epoll_ctl(epfd, EPOLL_CTL_ADD, listen_fd, &ev);

    struct epoll_event events[MAX_EVENTS];

    while (1) {
        int n = epoll_wait(epfd, events, MAX_EVENTS, -1 /* block forever */);

        for (int i = 0; i < n; i++) {
            if (events[i].data.fd == listen_fd) {
                /* New connection */
                int client = accept(listen_fd, NULL, NULL);
                set_nonblocking(client);

                ev.events  = EPOLLIN | EPOLLET;  /* edge-triggered */
                ev.data.fd = client;
                epoll_ctl(epfd, EPOLL_CTL_ADD, client, &ev);
            } else {
                /* Data available — handle_client(events[i].data.fd) */
                /* With ET: must read until EAGAIN */
            }
        }
    }
}
```
    </div>
    <div class="ch-section-label">Concept Checklist</div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Concept</th><th>Category</th></tr></thead>
      <tbody>
        <tr data-key="ph4-c1"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td>Threading models: thread-per-request vs thread pool vs event loop vs green threads</td><td><span class="cat-badge">Concurrency</span></td></tr>
        <tr data-key="ph4-c2"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td>Mutex, RW lock, semaphore, condition variable — when to use each</td><td><span class="cat-badge">Concurrency</span></td></tr>
        <tr data-key="ph4-c3"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td>Lock-free CAS: compare-and-swap, ABA problem, GCC __atomic builtins</td><td><span class="cat-badge">Concurrency</span></td></tr>
        <tr data-key="ph4-c4"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td>I/O multiplexing: select → poll → epoll (ET vs LT) → io_uring evolution</td><td><span class="cat-badge">I/O</span></td></tr>
        <tr data-key="ph4-c5"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td>C10K problem: why threads fail at scale, how epoll solves it</td><td><span class="cat-badge">I/O</span></td></tr>
        <tr data-key="ph4-c6"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td>In-process caching: LRU (linked list + hash map), LFU, eviction policies</td><td><span class="cat-badge">Caching</span></td></tr>
        <tr data-key="ph4-c7"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td>Cache stampede: thundering herd, mutex lock, probabilistic early expiry</td><td><span class="cat-badge">Caching</span></td></tr>
        <tr data-key="ph4-c8"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td>Connection pool exhaustion: queue vs reject, backpressure, health checks</td><td><span class="cat-badge">Performance</span></td></tr>
        <tr data-key="ph4-c9"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td>Load balancing algorithms: round-robin, least-conn, consistent hashing</td><td><span class="cat-badge">Scaling</span></td></tr>
        <tr data-key="ph4-c10"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td>Stateless design: externalizing state for horizontal scaling</td><td><span class="cat-badge">Scaling</span></td></tr>
      </tbody>
    </table>
  </div>
</div>
<!-- ═══════════════════════════════════════════════════════════
     Ph5 — Event-Driven Architecture
     ═══════════════════════════════════════════════════════════ -->
<div class="ch-card" id="ph5" data-ch="ph5" style="--ch-accent: linear-gradient(90deg,#06b6d4,#0ea5e9);">
  <div class="ch-header">
    <div class="ch-num">Ph5</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Event-Driven Architecture</div>
      <div class="ch-meta">
        <span class="ch-badge">Intermediate</span>
        <span class="ch-badge">Requires Ph2, Ph4</span>
        <a href="/learning/backend/m13-messaging/" class="ch-badge notes-live">📄 M13 Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/10 checked</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Concepts</div>
    <div class="be-concept-box">
      <ul>
        <li><strong>Why event-driven:</strong> temporal decoupling (producer/consumer run independently), fanout (one event → many consumers), audit log (full history replayable), reduces synchronous blocking chains, enables eventual consistency</li>
        <li><strong>Message queues vs event streams:</strong> RabbitMQ (work queue model — message consumed and deleted, at-most-once or at-least-once via acks, competing consumers, dead-letter exchange) vs Kafka (persistent log — messages retained, consumer groups replay from offset, unlimited retention)</li>
        <li><strong>Kafka internals:</strong> topic partitioned across brokers, each partition is an ordered immutable log; leader partition + replicas (In-Sync Replicas ISR); producer assigns partition (key hash or round-robin); consumer group — each partition consumed by exactly one consumer in group; offset committed by consumer</li>
        <li><strong>Kafka delivery semantics:</strong> at-most-once (<code>acks=0</code>, fire-and-forget), at-least-once (<code>acks=all</code> + retry — may duplicate), exactly-once (idempotent producer + transactions — <code>enable.idempotence=true</code> + <code>transactional.id</code>)</li>
        <li><strong>RabbitMQ patterns:</strong> direct exchange (routing key match), topic exchange (routing key pattern <code>*.error</code>), fanout exchange (broadcast to all bound queues), headers exchange; dead-letter exchange (DLX) for failed messages; message TTL; priority queues</li>
        <li><strong>Saga pattern:</strong> managing distributed transactions without 2PC; orchestration (central Saga Orchestrator sends commands, receives events, handles compensations), choreography (each service reacts to events and emits new events); compensating transactions roll back completed steps</li>
        <li><strong>Outbox pattern:</strong> write event to outbox table in same DB transaction as business data (atomicity), separate Relay/CDC process polls outbox and publishes to broker, mark as published; prevents lost events on crash between DB write and broker publish</li>
        <li><strong>CQRS</strong> (Command Query Responsibility Segregation): write side (commands mutate state, normalized DB optimized for writes), read side (queries return projections, denormalized read model optimized for reads); sync via domain events or CDC; eventual consistency between models</li>
        <li><strong>Event Sourcing:</strong> system state = ordered log of immutable domain events (not current state snapshot); reconstruct any past state by replaying events; snapshots for performance (don't replay full history); projections for derived read models; event schema versioning challenge</li>
        <li><strong>Idempotent consumers:</strong> natural idempotency (PUT/DELETE — repeated calls have same effect), deduplication table (store processed event IDs, reject duplicates), atomic check-and-process with DB transaction; combine with outbox for exactly-once end-to-end</li>
      </ul>
    </div>
    <div class="ch-section-label">Technologies &amp; Tools</div>
    <div class="be-tools">
      <span class="be-tool-badge">Kafka</span>
      <span class="be-tool-badge">RabbitMQ</span>
      <span class="be-tool-badge">librdkafka</span>
      <span class="be-tool-badge">Apache Pulsar</span>
      <span class="be-tool-badge">NATS</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C Example</button>
    <div class="code-block-wrap">
```c
/* Kafka producer using librdkafka (C client) */
#include <librdkafka/rdkafka.h>
#include <string.h>
#include <stdio.h>

static void delivery_cb(rd_kafka_t *rk, const rd_kafka_message_t *msg,
                         void *opaque) {
    (void)rk; (void)opaque;
    if (msg->err)
        fprintf(stderr, "Delivery failed: %s\n",
                rd_kafka_err2str(msg->err));
}

void produce_event(const char *brokers, const char *topic,
                   const char *key,    const char *value) {
    char errstr[512];

    rd_kafka_conf_t *conf = rd_kafka_conf_new();
    rd_kafka_conf_set(conf, "bootstrap.servers", brokers,
                      errstr, sizeof(errstr));
    rd_kafka_conf_set_dr_msg_cb(conf, delivery_cb);

    rd_kafka_t *rk = rd_kafka_new(RD_KAFKA_PRODUCER, conf,
                                  errstr, sizeof(errstr));
    rd_kafka_topic_t *rkt = rd_kafka_topic_new(rk, topic, NULL);

retry:
    if (rd_kafka_produce(rkt,
            RD_KAFKA_PARTITION_UA,    /* auto-select partition by key hash */
            RD_KAFKA_MSG_F_COPY,      /* copy payload into rdkafka */
            (void *)value, strlen(value),
            key, strlen(key),
            NULL) == -1) {
        if (rd_kafka_last_error() == RD_KAFKA_RESP_ERR__QUEUE_FULL) {
            rd_kafka_poll(rk, 100);   /* drain delivery queue */
            goto retry;
        }
    }

    rd_kafka_flush(rk, 10000);        /* wait up to 10s for delivery */
    rd_kafka_topic_destroy(rkt);
    rd_kafka_destroy(rk);
}
```
    </div>
    <div class="ch-section-label">Concept Checklist</div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Concept</th><th>Category</th></tr></thead>
      <tbody>
        <tr data-key="ph5-c1"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td>Why events: temporal decoupling, audit log, fanout, replay capability</td><td><span class="cat-badge">Architecture</span></td></tr>
        <tr data-key="ph5-c2"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td>Message queue vs event stream: RabbitMQ (work queue, delete on consume) vs Kafka (log, retain+replay)</td><td><span class="cat-badge">Architecture</span></td></tr>
        <tr data-key="ph5-c3"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td>Kafka internals: topics, partitions, offsets, ISR, consumer group rebalancing</td><td><span class="cat-badge">Kafka</span></td></tr>
        <tr data-key="ph5-c4"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td>Delivery semantics: at-most-once, at-least-once, exactly-once (idempotent producer)</td><td><span class="cat-badge">Kafka</span></td></tr>
        <tr data-key="ph5-c5"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td>RabbitMQ patterns: exchange types, DLX, message TTL</td><td><span class="cat-badge">Events</span></td></tr>
        <tr data-key="ph5-c6"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td>Saga pattern: orchestration vs choreography, compensating transactions</td><td><span class="cat-badge">Patterns</span></td></tr>
        <tr data-key="ph5-c7"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td>Outbox pattern: atomic write to outbox table, relay publishes to broker</td><td><span class="cat-badge">Patterns</span></td></tr>
        <tr data-key="ph5-c8"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td>CQRS: separate write model (commands) from read model (projections)</td><td><span class="cat-badge">Patterns</span></td></tr>
        <tr data-key="ph5-c9"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td>Event Sourcing: state as event log, snapshots, projections, schema versioning</td><td><span class="cat-badge">Patterns</span></td></tr>
        <tr data-key="ph5-c10"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td>Idempotent consumers: dedup table, atomic check-and-process</td><td><span class="cat-badge">Patterns</span></td></tr>
      </tbody>
    </table>
  </div>
</div>
<!-- ═══════════════════════════════════════════════════════════
     Ph6 — Microservices & Infrastructure
     ═══════════════════════════════════════════════════════════ -->
<div class="ch-card" id="ph6" data-ch="ph6" style="--ch-accent: linear-gradient(90deg,#f59e0b,#10b981);">
  <div class="ch-header">
    <div class="ch-num">Ph6</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Microservices &amp; Infrastructure</div>
      <div class="ch-meta">
        <span class="ch-badge">Advanced</span>
        <span class="ch-badge">Requires Ph3, Ph5</span>
        <a href="/learning/backend/m15-microservices/" class="ch-badge notes-live">📄 M15 Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/10 checked</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Concepts</div>
    <div class="be-concept-box">
      <ul>
        <li><strong>Monolith vs microservices decision:</strong> start with modular monolith, split when team topology demands it (Conway's Law), bounded contexts (DDD) define service boundaries; microservices add operational complexity — don't split prematurely</li>
        <li><strong>Strangler Fig pattern:</strong> incrementally replace monolith — route specific URL paths to new service at API gateway, coexist with monolith during migration, deprecate monolith module by module; avoids big-bang rewrite risk</li>
        <li><strong>Inter-service communication strategy:</strong> sync REST/gRPC (simple, tight coupling, propagates latency) vs async events (loose coupling, eventual consistency, harder to debug); request-reply over async via correlation ID in message header</li>
        <li><strong>API Gateway responsibilities:</strong> single entry point, path-based routing to backend services, authentication/authorization offload (validate JWT before forwarding), rate limiting and throttling, SSL termination, request aggregation (backend for frontend pattern), canary traffic splitting</li>
        <li><strong>Service discovery:</strong> client-side (service queries registry like Consul/Eureka, client chooses instance — more control), server-side (load balancer queries registry — simpler client), DNS-based (Kubernetes Services use kube-dns)</li>
        <li><strong>Circuit breaker:</strong> closed state (normal, count failures), open state (fail fast immediately — no calls to unhealthy service, prevents cascade), half-open state (allow probe requests to test recovery); bulkhead pattern (isolate resource pools per service)</li>
        <li><strong>Docker best practices for C/C++:</strong> multi-stage build (Stage 1: gcc:13 builder compiles binary, Stage 2: debian:slim runtime copies binary — minimal image size), non-root user (<code>useradd -r</code>), <code>.dockerignore</code> (exclude build artifacts), pin base image versions, <code>ENTRYPOINT</code> vs <code>CMD</code></li>
        <li><strong>Kubernetes fundamentals:</strong> Pod (smallest deployable unit, co-located containers), Deployment (manages ReplicaSet, rolling updates, rollback), Service (stable DNS name + ClusterIP load balancing), Ingress (HTTP/S routing + TLS termination), ConfigMap (non-secret config), Secret (base64-encoded credentials), liveness probe (restart if unhealthy), readiness probe (remove from Service endpoints if not ready)</li>
        <li><strong>CI/CD pipeline stages:</strong> lint → unit test → integration test → build OCI image → push to registry → deploy to staging → smoke test → deploy to production; blue-green (two identical environments, instant cutover); canary (route 5% → 20% → 100% traffic to new version)</li>
        <li><strong>12-Factor App:</strong> I-Codebase (one repo, many deploys), II-Dependencies (explicitly declared), III-Config (env vars, not hardcoded), IV-Backing services (attached resources, swap without code change), V-Build/release/run (strict separation), VI-Processes (stateless, share nothing), VII-Port binding, VIII-Concurrency (scale out via process model), IX-Disposability (fast startup, graceful shutdown), X-Dev/prod parity, XI-Logs (stdout, not files), XII-Admin processes</li>
      </ul>
    </div>
    <div class="ch-section-label">Technologies &amp; Tools</div>
    <div class="be-tools">
      <span class="be-tool-badge">Docker</span>
      <span class="be-tool-badge">Kubernetes</span>
      <span class="be-tool-badge">Consul</span>
      <span class="be-tool-badge">Nginx</span>
      <span class="be-tool-badge">Helm</span>
      <span class="be-tool-badge">GitHub Actions</span>
      <span class="be-tool-badge">ArgoCD</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show Dockerfile Example</button>
    <div class="code-block-wrap">
```dockerfile
# -- Stage 1: Build (fat image with full toolchain) --
FROM gcc:13 AS builder
WORKDIR /src

# Copy source and build system first (layer caching)
COPY Makefile ./
COPY src/     ./src/

# Build release binary (strip debug symbols)
RUN make release CFLAGS="-O2 -DNDEBUG" && strip bin/server

# -- Stage 2: Minimal runtime --
FROM debian:bookworm-slim
RUN apt-get update \
 && apt-get install -y --no-install-recommends libpq5 ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Non-root user for security
RUN useradd -r -u 1001 -s /sbin/nologin appuser
WORKDIR /app
COPY --from=builder /src/bin/server .
USER appuser

EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/health || exit 1

ENTRYPOINT ["./server"]
```
    </div>
    <div class="ch-section-label">Concept Checklist</div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Concept</th><th>Category</th></tr></thead>
      <tbody>
        <tr data-key="ph6-c1"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td>Monolith vs microservices: Conway's Law, bounded contexts, modular monolith first</td><td><span class="cat-badge">Architecture</span></td></tr>
        <tr data-key="ph6-c2"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td>Strangler Fig: incremental migration via API gateway routing</td><td><span class="cat-badge">Architecture</span></td></tr>
        <tr data-key="ph6-c3"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td>Sync vs async inter-service communication: tradeoffs, correlation ID pattern</td><td><span class="cat-badge">Communication</span></td></tr>
        <tr data-key="ph6-c4"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td>API Gateway: routing, auth offload, rate limiting, BFF pattern</td><td><span class="cat-badge">Infra</span></td></tr>
        <tr data-key="ph6-c5"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td>Service discovery: client-side (Consul) vs server-side vs DNS-based (K8s)</td><td><span class="cat-badge">Infra</span></td></tr>
        <tr data-key="ph6-c6"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td>Circuit breaker: closed/open/half-open states, bulkhead pattern</td><td><span class="cat-badge">Reliability</span></td></tr>
        <tr data-key="ph6-c7"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td>Docker multi-stage build for C/C++: builder → slim runtime, non-root user</td><td><span class="cat-badge">Docker</span></td></tr>
        <tr data-key="ph6-c8"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td>Kubernetes: Pod, Deployment, Service, Ingress, liveness vs readiness probe</td><td><span class="cat-badge">K8s</span></td></tr>
        <tr data-key="ph6-c9"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td>CI/CD: pipeline stages, blue-green deployment, canary traffic splitting</td><td><span class="cat-badge">CI/CD</span></td></tr>
        <tr data-key="ph6-c10"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td>12-Factor App: config via env, stateless processes, stdout logs</td><td><span class="cat-badge">Best Practices</span></td></tr>
      </tbody>
    </table>
  </div>
</div>
<!-- ═══════════════════════════════════════════════════════════
     Ph7 — Observability & Hardening
     ═══════════════════════════════════════════════════════════ -->
<div class="ch-card" id="ph7" data-ch="ph7" style="--ch-accent: linear-gradient(90deg,#e11d48,#dc2626);">
  <div class="ch-header">
    <div class="ch-num">Ph7</div>
    <div class="ch-title-wrap">
      <div class="ch-title">Observability &amp; Hardening</div>
      <div class="ch-meta">
        <span class="ch-badge">Production</span>
        <span class="ch-badge">Requires Ph6</span>
        <a href="/learning/backend/m17-observability/" class="ch-badge notes-live">📄 M17 Notes</a>
      </div>
    </div>
    <span class="ch-chevron">▼</span>
  </div>
  <div class="ch-progress-row">
    <div class="ch-prog-bar-wrap"><div class="ch-prog-bar"></div></div>
    <span class="ch-prog-text">0/12 checked</span>
    <span class="ch-prog-pct">0%</span>
  </div>
  <div class="ch-body">
    <div class="ch-section-label">Key Concepts</div>
    <div class="be-concept-box">
      <ul>
        <li><strong>3 pillars of observability:</strong> logs (discrete events — what happened), metrics (aggregated numeric data — how many/how fast), traces (causal chains across services — why it was slow); each answers different questions; together give full system visibility</li>
        <li><strong>Structured logging:</strong> JSON lines format (one JSON object per line), mandatory fields (timestamp ISO-8601, level, service, trace_id, span_id, message), log levels (DEBUG verbose, INFO normal, WARN degraded, ERROR unexpected failure, FATAL unrecoverable), never log secrets or PII, use correlation/trace IDs to link logs across services</li>
        <li><strong>Metrics types:</strong> counter (monotonically increasing, e.g., <code>http_requests_total</code> — use <code>rate()</code>), gauge (point-in-time value, e.g., <code>memory_usage_bytes</code>, <code>active_connections</code>), histogram (bucketed distribution, e.g., <code>request_duration_seconds</code> — use <code>histogram_quantile()</code> for p99)</li>
        <li><strong>RED method</strong> (for services): Rate (requests/second), Errors (error rate %), Duration (latency percentiles p50/p95/p99); <strong>USE method</strong> (for resources): Utilization (% time busy), Saturation (queue depth, wait time), Errors (device error rate)</li>
        <li><strong>Prometheus:</strong> pull-based scraping (Prometheus polls <code>/metrics</code> endpoint on services), exposition format (<code># HELP</code>, <code># TYPE</code>, <code>metric_name{labels} value timestamp</code>), PromQL (<code>rate(http_requests_total[5m])</code>, <code>histogram_quantile(0.99, ...)</code>, <code>by(service)</code>), AlertManager for alerting rules and routing</li>
        <li><strong>Distributed tracing:</strong> trace (end-to-end request chain, unique trace_id), span (single operation within trace, span_id + parent_span_id), W3C <code>traceparent</code> header for cross-service propagation, OpenTelemetry SDK (language-agnostic instrumentation, OTLP export to Jaeger/Tempo/Zipkin)</li>
        <li><strong>Health check endpoints:</strong> <code>GET /health/live</code> — liveness probe (is process alive? if fails, Kubernetes restarts container), <code>GET /health/ready</code> — readiness probe (is service ready to serve traffic? if fails, removed from Service endpoints); startup probe for slow-starting containers</li>
        <li><strong>Rate limiting algorithms:</strong> token bucket (bucket refills at rate r, allow bursts up to capacity b — bursty traffic ok), sliding window log (store timestamps of all requests, exact but memory O(requests)), sliding window counter (approximate, memory O(1), compromise); implement at API gateway (global) and per-service (defense in depth)</li>
        <li><strong>OWASP Top 10 for backends:</strong> SQL injection (parameterized queries only — never string concat), command injection (avoid shell=True / system(), use execv), SSRF (Server-Side Request Forgery — allowlist outbound URLs), broken access control (check authorization on every request, not just auth), security misconfiguration (disable debug endpoints in prod, no default credentials), insecure deserialization (validate and sanitize all deserialized input)</li>
        <li><strong>Input validation:</strong> allowlist over denylist (define what is allowed, reject everything else), validate at trust boundaries only (never trust client input), size limits (prevent DoS via large payloads — max body size), type checking, sanitize before SQL/shell/HTML context</li>
        <li><strong>Secrets management:</strong> never in source code or Docker images (scan with truffleHog/gitleaks), environment variables (basic, visible in <code>/proc/PID/environ</code> — acceptable for containers), HashiCorp Vault (dynamic secrets with TTL + auto-rotation, audit log, fine-grained policies), AWS Secrets Manager / GCP Secret Manager; secret rotation strategy</li>
        <li><strong>Graceful shutdown:</strong> catch SIGTERM (Kubernetes sends this before SIGKILL after <code>terminationGracePeriodSeconds</code>), stop accepting new connections (close listen socket or remove from load balancer), drain in-flight requests (atomic counter), close DB connection pool, deregister from service discovery, log completion; target: shutdown in &lt; terminationGracePeriodSeconds (default 30s)</li>
      </ul>
    </div>
    <div class="ch-section-label">Technologies &amp; Tools</div>
    <div class="be-tools">
      <span class="be-tool-badge">Prometheus</span>
      <span class="be-tool-badge">Grafana</span>
      <span class="be-tool-badge">Jaeger</span>
      <span class="be-tool-badge">OpenTelemetry</span>
      <span class="be-tool-badge">HashiCorp Vault</span>
      <span class="be-tool-badge">AlertManager</span>
    </div>
    <button class="code-toggle-btn"><span class="caret">▸</span> Show C Example</button>
    <div class="code-block-wrap">
```c
/* Graceful shutdown via SIGTERM — C implementation */
#include <signal.h>
#include <stdatomic.h>
#include <stdio.h>
#include <unistd.h>

static atomic_int  in_flight        = 0;
static atomic_bool shutdown_req     = false;

static void handle_sigterm(int sig) {
    (void)sig;
    atomic_store(&shutdown_req, true);
}

void register_signals(void) {
    struct sigaction sa = { .sa_handler = handle_sigterm };
    sigemptyset(&sa.sa_mask);
    sigaction(SIGTERM, &sa, NULL);
    sigaction(SIGINT,  &sa, NULL);   /* also handle Ctrl-C */
}

/* Called at start of each request handler */
void request_begin(void) { atomic_fetch_add(&in_flight, 1); }

/* Called at end of each request handler */
void request_end(void)   { atomic_fetch_sub(&in_flight, 1); }

int main(void) {
    register_signals();
    /* ... start server, accept connections ... */

    /* Main loop — stop accepting when shutdown requested */
    while (!atomic_load(&shutdown_req)) {
        /* accept() new connections */
    }

    /* Drain: wait for all in-flight requests to complete */
    fprintf(stderr, "[shutdown] draining %d in-flight requests\n",
            atomic_load(&in_flight));
    while (atomic_load(&in_flight) > 0)
        usleep(5000);   /* poll every 5ms */

    /* Close DB pools, deregister from service discovery */
    fprintf(stderr, "[shutdown] clean exit\n");
    return 0;
}
```
    </div>
    <div class="ch-section-label">Concept Checklist</div>
    <table class="ch-problem-table">
      <thead><tr><th>✓</th><th>#</th><th>Concept</th><th>Category</th></tr></thead>
      <tbody>
        <tr data-key="ph7-c1"><td class="solved-cell"><div class="solved-check"></div></td><td>1</td><td>3 pillars: logs (events), metrics (aggregates), traces (causal chains) — what each answers</td><td><span class="cat-badge">Observability</span></td></tr>
        <tr data-key="ph7-c2"><td class="solved-cell"><div class="solved-check"></div></td><td>2</td><td>Structured logging: JSON lines, mandatory fields, log levels, trace_id correlation</td><td><span class="cat-badge">Observability</span></td></tr>
        <tr data-key="ph7-c3"><td class="solved-cell"><div class="solved-check"></div></td><td>3</td><td>Metric types: counter (rate()), gauge, histogram (histogram_quantile p99)</td><td><span class="cat-badge">Metrics</span></td></tr>
        <tr data-key="ph7-c4"><td class="solved-cell"><div class="solved-check"></div></td><td>4</td><td>RED method (Rate, Errors, Duration) and USE method (Utilization, Saturation, Errors)</td><td><span class="cat-badge">Metrics</span></td></tr>
        <tr data-key="ph7-c5"><td class="solved-cell"><div class="solved-check"></div></td><td>5</td><td>Prometheus: pull-based scraping, exposition format, PromQL, AlertManager</td><td><span class="cat-badge">Metrics</span></td></tr>
        <tr data-key="ph7-c6"><td class="solved-cell"><div class="solved-check"></div></td><td>6</td><td>Distributed tracing: trace/span model, W3C traceparent header, OpenTelemetry</td><td><span class="cat-badge">Tracing</span></td></tr>
        <tr data-key="ph7-c7"><td class="solved-cell"><div class="solved-check"></div></td><td>7</td><td>Health checks: liveness (restart) vs readiness (remove from LB) vs startup probe</td><td><span class="cat-badge">Reliability</span></td></tr>
        <tr data-key="ph7-c8"><td class="solved-cell"><div class="solved-check"></div></td><td>8</td><td>Rate limiting: token bucket, sliding window log, sliding window counter</td><td><span class="cat-badge">Performance</span></td></tr>
        <tr data-key="ph7-c9"><td class="solved-cell"><div class="solved-check"></div></td><td>9</td><td>OWASP Top 10: SQL injection, SSRF, broken access control, security misconfiguration</td><td><span class="cat-badge">Security</span></td></tr>
        <tr data-key="ph7-c10"><td class="solved-cell"><div class="solved-check"></div></td><td>10</td><td>Input validation: allowlist, trust boundaries, size limits, sanitization</td><td><span class="cat-badge">Security</span></td></tr>
        <tr data-key="ph7-c11"><td class="solved-cell"><div class="solved-check"></div></td><td>11</td><td>Secrets management: Vault dynamic secrets, never in code/images, rotation</td><td><span class="cat-badge">Security</span></td></tr>
        <tr data-key="ph7-c12"><td class="solved-cell"><div class="solved-check"></div></td><td>12</td><td>Graceful shutdown: SIGTERM handler, drain in-flight, close pools, deregister</td><td><span class="cat-badge">Reliability</span></td></tr>
      </tbody>
    </table>
  </div>
</div>
</div><!-- /.be-phases -->
<script>
// Inline init — ensure progress is calculated after page load
document.addEventListener('DOMContentLoaded', function() {
  // JS file handles all logic; this is a no-op safety net
});
</script>


<script src="/assets/js/backend-roadmap.js" defer></script>