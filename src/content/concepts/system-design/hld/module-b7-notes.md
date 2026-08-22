---
title: "Module B7 Notes: WhatsApp"
description: "Module B7 — Design WhatsApp (Real-Time Messaging) System Design Mastery Course Track B: HLD Week 17 --- 🎯 Module Overview Duration: 1 Week Track: B — HLD Case Studies…"
domain: system-design
track: system-design-hld
order: 115
url: /learning/system-design/hld/module-b7-notes/
---

# Module B7 — Design WhatsApp (Real-Time Messaging)
## System Design Mastery Course | Track B: HLD | Week 17

---

## 🎯 Module Overview

**Duration:** 1 Week | **Track:** B — HLD Case Studies | **Prerequisites:** B1–B6
**Goal:** WhatsApp is the canonical real-time messaging question. It tests WebSockets, message delivery guarantees, presence systems, group messaging fan-out, and storage at scale. Appears at every FAANG.

---

## 1. Requirements

### Functional
```
Core:
  1. 1-on-1 messaging — send/receive text, media, emoji
  2. Group messaging — up to 1,024 members
  3. Message delivery receipts — sent ✓, delivered ✓✓, read ✓✓ (blue)
  4. Online presence — "Online" / "Last seen at 3:42 PM"
  5. Media sharing — images, video, audio, documents

Out of scope: calls, disappearing messages, payments, status stories
```

### Non-Functional
```
Scale:
  2 billion users, 100M DAU
  100 billion messages/day → ~1.16M messages/sec
  Average message: 100 bytes (text) to 10 MB (video)
  Group message fan-out: 1 sender → up to 1,024 recipients

Performance:
  Message delivery latency: p99 < 500ms (sender to recipient)
  Presence update propagation: p99 < 1 second

Availability: 99.99%
Message durability: zero message loss
Ordering: messages in a conversation must be in order
```

---

## 2. The Core Protocol: WebSockets

### Why Not HTTP Polling?
```
Short polling (every 1s):
  100M users × 1 req/sec = 100M req/sec → server overloaded
  Wasteful: most polls return empty response
  Latency: up to 1s delay

Long polling:
  Better: client holds connection open, server responds when message arrives
  Problems: connection drops, reconnect storms, proxy timeouts
  Still stateless — server must find messages for each reconnect

WebSockets (chosen):
  Persistent TCP connection between client and server
  Bidirectional: server pushes messages to client instantly
  Full-duplex: client and server send simultaneously
  Latency: milliseconds (no polling delay)
  Efficient: one connection per user (not per message)
```

### WebSocket Lifecycle
```
1. Client sends HTTP UPGRADE request
2. Server responds 101 Switching Protocols
3. TCP connection remains open — WebSocket frames flow bidirectionally
4. Heartbeat (ping/pong every 30s) keeps connection alive through NAT
5. On disconnect: client reconnects, fetches offline messages via REST
```

---

## 3. High-Level Architecture

```
SEND MESSAGE PATH:
[Alice's Phone]
    │ WebSocket frame: {to: Bob, content: "Hey!"}
    ↓
[Chat Server A]  ← Alice is connected here
    ├── Write message to Cassandra (durable, message_id = Snowflake)
    ├── Publish to Kafka topic: "messages" (async fanout)
    └── Return ACK to Alice: message received by server ✓

[Message Routing Service] (Kafka consumer)
    ├── Look up: which Chat Server is Bob connected to? (Session Store → Redis)
    │     → Bob is connected to Chat Server C
    └── Route message to Chat Server C

[Chat Server C]
    └── Push message to Bob via Bob's WebSocket connection ✓✓ (delivered)

[Bob reads message]
    └── Bob's client sends "read receipt" back via WebSocket
        → Chat Server C routes to Chat Server A → pushed to Alice ✓✓ (blue)

OFFLINE USER PATH:
[Bob is offline]
    Message stored in Cassandra "inbox" for Bob
    When Bob reconnects: REST API fetches all offline messages since last_seen_msg_id
```

---

## 4. Key Components

### Chat Server (Stateful)
```
Each Chat Server maintains WebSocket connections for N users.
The server IS stateful — knows which users are connected locally.

At scale: 100M concurrent connections ÷ 65K connections/server = ~1,500 servers
(Modern servers with event-loop (Node.js/Netty) handle 100K+ concurrent WS connections)

So: 100M / 100K = 1,000 Chat Servers

Challenge: message must reach the EXACT server Alice is connected to.
Solution: Session Store (Redis) maps user_id → chat_server_id
```

### Session Store (Redis)
```
On user connect:    SET session:{userId} serverIP EX 86400
On user disconnect: DEL session:{userId}
On heartbeat:       EXPIRE session:{userId} 86400  (refresh TTL)

Routing lookup:
  GET session:{bobId} → "chat-server-47:8080"
  Route message to that server via internal HTTP or message queue
```

### Message Store (Cassandra)
```
Why Cassandra:
  ✅ High write throughput (1.16M msg/sec — Cassandra's strength)
  ✅ Partition by conversation_id → all messages in conversation on same node
  ✅ Clustering by message_id DESC → newest first, efficient pagination
  ✅ Multi-datacenter replication built-in

Schema:
CREATE TABLE messages (
    conversation_id UUID,
    message_id      BIGINT,   -- Snowflake ID (embeds timestamp)
    sender_id       BIGINT,
    content         TEXT,
    media_url       TEXT,     -- NULL if text-only
    message_type    VARCHAR,  -- 'text', 'image', 'video', 'audio'
    status          VARCHAR,  -- 'sent', 'delivered', 'read'
    created_at      TIMESTAMP,
    PRIMARY KEY (conversation_id, message_id)
) WITH CLUSTERING ORDER BY (message_id DESC);

Read: SELECT * FROM messages WHERE conversation_id = X LIMIT 50
      → single partition, newest first ✓
```

### Inbox (Offline Messages)
```
When Bob is offline:
  Message is stored in messages table (durable, already done)
  Also stored in inbox:{bobId} sorted set: ZADD inbox:{bobId} {msgId} {msgId}

On Bob reconnects:
  1. Fetch last_read_message_id from Bob's profile
  2. REST call: GET /messages?since={last_read_message_id}
  3. Server queries: SELECT * FROM messages WHERE conversation_id IN (...) AND message_id > last_read
  4. Push all missed messages to Bob
  5. Update last_read_message_id = latest received
```

---

## 5. Message Delivery Receipts

```
Three-state receipt system:
  ✓  (single gray)  = message saved to server
  ✓✓ (double gray)  = message delivered to recipient's device
  ✓✓ (double blue)  = message read by recipient

Implementation:

1. Sender → Server: message sent → Server ACKs → sender shows ✓
2. Server → Recipient online:
     WebSocket push → recipient's device ACKs → server marks delivered → sender gets ✓✓
3. Recipient opens conversation:
     Client sends READ receipt → server routes to sender → shows ✓✓ blue

Storage:
   UPDATE messages SET status = 'delivered' WHERE message_id = X
   (Or: separate receipts table for read-scaling)

Group messages:
   ✓✓ shown when ALL members delivered (not just one)
   Blue ✓✓ shown when ALL members read
   Implementation: delivery_count and read_count columns per group message
   Alternatively: separate message_receipts table (sender_id, message_id, recipient_id, status, timestamp)
```

---

## 6. Presence System

```
"Online" / "Last seen at 3:42 PM"

Challenge: 100M active users — each updating presence every 30s = 3.3M updates/sec

Solution: heartbeat + Redis
  Every 30s: client sends heartbeat via WebSocket
  Server updates: SET presence:{userId} "online" EX 45
  TTL slightly longer than heartbeat → expires if heartbeat stops

Read presence:
  GET presence:{userId}
  → value exists: "Online"
  → missing (expired): "Last seen at {last_heartbeat_time}"

Scaling the presence writes:
  3.3M SETEX/sec is heavy for a single Redis cluster
  Solution: shard presence by userId hash across N Redis clusters
  Or: use Redis Cluster with consistent hashing across 16,384 slots

Privacy:
  Users can disable "last seen" → store preference, return NULL regardless
  Read receipts can also be disabled (WhatsApp privacy settings)

Fanout of presence to contacts:
  When Alice comes online → notify all of Alice's contacts who are currently online
  Expensive: Alice has 300 contacts → 300 WebSocket pushes
  In practice: subscribe-based presence
    Bob subscribes to Alice's presence only when Bob opens a chat with Alice
    Presence only pushed to subscribers (not all contacts)
```

---

## 7. Group Messaging

```
Groups: up to 1,024 members
6K group messages/sec × 1,024 avg members = 6.1M WS pushes/sec

Architecture:
  Option A: Fan-out at write time
    For each group message: push to all N member WebSocket connections
    At 1,024 members: acceptable (similar to celebrity tweet problem)
    Implementation: maintain group_members table → look up all connections → push

  Option B: Group message queue per user (WhatsApp's approach)
    Group message stored once in messages table (conversation_id = group_id)
    Each member's inbox just stores a pointer (message_id reference)
    On member request: fetch full message from messages table

Storage model:
CREATE TABLE group_members (
    group_id  UUID,
    user_id   BIGINT,
    role      VARCHAR,   -- 'admin', 'member'
    joined_at TIMESTAMP,
    PRIMARY KEY (group_id, user_id)
);

Fan-out service:
  On group message received:
    1. Store message once in messages (conversation_id = group_id)
    2. Look up all online group members from group_members table
    3. Route via Session Store to correct Chat Servers
    4. Push message to online members' WebSocket connections
    5. Store in offline inbox for offline members
```

---

## 8. Media Sharing

```
Challenge: Large files (videos up to 100MB) should not go through chat servers.
           Chat servers handle tiny text messages, not video blobs.

Protocol:
  1. Sender selects media → client uploads DIRECTLY to S3 via pre-signed URL
     Client calls: POST /media/upload → server returns S3 pre-signed PUT URL
     Client uploads: PUT https://s3.../media/{uuid}.mp4 (directly to S3)
     Media service confirms receipt

  2. Media service:
     - Stores original in S3
     - Triggers thumbnail generation (image) or transcoding (video)
     - Stores processed variants in S3
     - CDN caches frequently accessed media

  3. Message contains media_url, not the binary data
     { type: "image", media_url: "https://cdn.wa.me/media/{uuid}.jpg", thumbnail: "..." }

  4. Recipient downloads media directly from CDN — chat server not involved

End-to-end encryption note:
  WhatsApp uses Signal Protocol: media encrypted on client before upload
  Server stores encrypted blob — cannot decrypt content
  Key exchange uses Diffie-Hellman through WhatsApp's key server
  (Out of scope for HLD interview — mention it, don't deep-dive)
```

---

## 9. Message Ordering

```
Challenge: messages must arrive in order within a conversation.

Approach: Snowflake ID as message_id
  Snowflake: [41-bit timestamp][10-bit machine][12-bit sequence]
  Generated at Chat Server when message received
  Globally unique + monotonically increasing per millisecond per server

Ordering guarantee:
  Messages stored in Cassandra: CLUSTERING ORDER BY message_id DESC
  Clients render messages sorted by message_id → timestamp order

Edge case: two messages sent within same millisecond
  Snowflake sequence counter handles this: up to 4096 per ms per machine
  If same machine, sequence guaranteed ordered
  If different machines: timestamp + machine_id → deterministic tie-break

Out-of-order delivery (network reordering):
  Client buffers and re-sorts by message_id before rendering
  Server-assigned Snowflake ID is canonical order — not client-assigned time
```

---

## 10. Estimating Scale

```
Storage:
  100B messages/day × 100 bytes avg = 10 TB/day (text only)
  With 3× replication (Cassandra): 30 TB/day
  After 5 years: ~55 PB — Cassandra cluster of ~500 nodes at 100 TB/node

Media:
  Assume 20% of messages include media, avg 500 KB
  100B × 20% × 500 KB = 10 PB/day (too large without TTL)
  WhatsApp in practice: media deleted from servers after download
                        (stored on device, not cloud — unlike iCloud)
  With TTL (30 days): rolling 300 PB of media on S3

WebSocket servers:
  100M concurrent users ÷ 100K connections/server = 1,000 Chat Servers
  Each server: 8 core, 64 GB RAM, persistent socket connections (Netty/Vert.x)

Redis (Session + Presence):
  100M active sessions × 50 bytes/entry = 5 GB — fits one Redis node
  100M presence entries × 50 bytes = 5 GB — fits one Redis node
  But 3.3M writes/sec for presence → Redis Cluster (10+ nodes)

Kafka (message routing):
  1.16M messages/sec × 1 KB avg = ~1.16 GB/sec
  With 3× replication: 3.5 GB/sec → 35+ Kafka nodes
  Partitions: hash(conversation_id) → ordering within conversation guaranteed
```

---

## 📝 Tasks

### Task 1 — WebSocket Connection Management
Design the connection management system:
1. Alice opens WhatsApp. How does the app choose which Chat Server to connect to?
2. Chat Server 47 crashes. 100K users lose their connections. What happens?
3. Bob's phone loses network for 60 seconds. What messages are queued? How are they delivered when reconnected?
4. A user has WhatsApp open on phone AND web (2 devices). How does the system manage 2 WebSocket connections for one user?

### Task 2 — Delivery Receipt Implementation
Design the full 3-state delivery receipt system:
1. Write the state machine for message status (sent → delivered → read)
2. For a group of 500 members: when do ✓✓ (delivered) and blue ✓✓ (read) show?
3. Handle the failure case: message delivered, but "delivered" receipt lost in transit
4. What if the sender is offline when the receipt arrives?

### Task 3 — Presence at Scale
Design a presence system for 100M concurrent users with these constraints:
- Presence updates (heartbeat) every 30 seconds
- "Last seen" accurate to within 1 minute
- Privacy: some users hide last seen
- Scale: must handle 3.3M presence writes/sec
- Presence notification: when Alice comes online, notify her contacts

### ⭐ Task 4 — Full WhatsApp Design
End-to-end 45-minute interview simulation. Cover: requirements, estimations, architecture, WebSocket management, message routing, delivery receipts, group messaging fan-out, presence, media sharing. Estimate: Chat Server count, Cassandra nodes, Redis cluster size, Kafka throughput.

---

## ✅ Completion Checklist

- [ ] WebSockets vs polling — why WS for real-time messaging
- [ ] Chat server statefulness — each server owns connections, Session Store maps user→server
- [ ] Message send/receive path end-to-end
- [ ] Cassandra schema: (conversation_id, message_id DESC) primary key
- [ ] Offline message delivery: REST fetch on reconnect using last_read_message_id
- [ ] 3-state delivery receipts: sent ✓, delivered ✓✓, read ✓✓ blue
- [ ] Group messaging: store once, fan-out to online members, inbox for offline
- [ ] Presence system: heartbeat + Redis SETEX with 45s TTL + subscribe-based push
- [ ] Media: S3 pre-signed URL upload + CDN delivery + encrypted blob
- [ ] Snowflake ID for message ordering (timestamp embedded → sortable)
- [ ] Scale math: 1,000 Chat Servers, 30 TB/day Cassandra, 3.3M presence writes/sec
- [ ] Completed Task 1 — WebSocket connection management
- [ ] Completed Task 2 — delivery receipt state machine
- [ ] Completed Task 3 — presence at scale design
- [ ] Completed Task 4 — full WhatsApp design (45-min simulation)

<br>
<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid #ddd;padding-top:20px;">
  <a href="/learning/system-design/hld/module-b6-notes/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">← B6 Twitter Feed Notes</a>
  <a href="/learning/system-design/hld/module-b7-whatsapp/" style="padding:12px 24px;border:1px solid #00d4aa;color:#00d4aa;border-radius:4px;text-decoration:none;font-weight:600;">⚡ Interactive Module</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b8-notes/" style="padding:12px 24px;background:#00d4aa;color:#1a1f36;border-radius:4px;text-decoration:none;font-weight:600;">NEXT: B8 YouTube →</a>
</div>
