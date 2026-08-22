---
title: "Module B7: WhatsApp"
description: "SYSTEM DESIGN MASTERY · TRACK B · MODULE B7 · WEEK 17 REAL-TIME MESSAGING · WEBSOCKETS · E2E ENCRYPTION Case Study No."
domain: system-design
track: system-design-hld
order: 114
chrome: bare
ownHeader: true
url: /learning/system-design/hld/module-b7-whatsapp/
---

<link rel="stylesheet" href="/assets/css/sd-module-b7.css">
<div class="sd-module-b7">
<header>
  <div class="hdr-bar"></div>
  <div class="hdr-top">
<span>SYSTEM DESIGN MASTERY · TRACK B · MODULE B7 · WEEK 17</span>
<span>REAL-TIME MESSAGING · WEBSOCKETS · E2E ENCRYPTION</span>
  </div>
  <div class="hdr-inner">
<div>
<div class="hdr-kicker">Case Study No. 3 · Real-Time Messaging · Delivery Receipts</div>
<h1 class="mb7-h1">Design<br><span class="acc">WhatsApp</span></h1>
<div class="hdr-sub">WEBSOCKETS · CASSANDRA · PRESENCE SYSTEM<br>GROUP MESSAGING · MEDIA PIPELINE · S3 + CDN</div>
</div>
<div class="hdr-stats">
<div class="hs"><div class="hs-v">2B</div><div class="hs-l">USERS</div></div>
<div class="hs"><div class="hs-v">100B</div><div class="hs-l">MSG/DAY</div></div>
<div class="hs"><div class="hs-v">1K</div><div class="hs-l">CHAT SERVERS</div></div>
<div class="hs"><div class="hs-v">B7</div><div class="hs-l">MODULE</div></div>
</div>
  </div>
  <div class="proto-row">
<div class="pt" style="color:var(--grn)">WebSocket</div>
<div class="pt" style="color:var(--cyan)">Cassandra</div>
<div class="pt" style="color:var(--amber)">Session Store</div>
<div class="pt" style="color:var(--grn)">Delivery Receipts</div>
<div class="pt" style="color:var(--cyan)">Presence</div>
<div class="pt" style="color:var(--amber)">Group Fan-Out</div>
<div class="pt" style="color:var(--grn)">S3 Media</div>
  </div>
</header>
<nav class="nav">
  <div class="nt active" onclick="mb7_show('req',this)">Requirements</div>
  <div class="nt" onclick="mb7_show('ws',this)">WebSockets</div>
  <div class="nt" onclick="mb7_show('arch',this)">Architecture</div>
  <div class="nt" onclick="mb7_show('receipts',this)">Delivery Receipts</div>
  <div class="nt" onclick="mb7_show('presence',this)">Presence</div>
  <div class="nt" onclick="mb7_show('groups',this)">Group Messaging</div>
  <div class="nt" onclick="mb7_show('schema',this)">Data Models</div>
  <div class="nt" onclick="mb7_show('scale',this)">Scale & Estimation</div>
  <div class="nt" onclick="mb7_show('tasks',this)">Tasks</div>
  <div class="nt" onclick="mb7_show('checklist',this)">Checklist</div>
</nav>
<div class="content">
<!-- REQUIREMENTS -->
<div class="view active" id="view-req">
  <div class="sh">Requirements</div>
  <div class="sr">Establish scope — then everything follows from the constraints</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0">
<div style="background:var(--panel);border:1px solid var(--bord2);border-left:2px solid var(--grn);padding:16px">
<div style="font-family:'Exo 2',sans-serif;font-size:14px;font-weight:700;color:var(--white);margin-bottom:10px">Functional</div>
<div style="font-family:'Share Tech Mono',monospace;font-size:10px;color:var(--muted);line-height:2.2">
        1-on-1 messaging (text, media, emoji)<br>
        Group messaging (up to 1,024 members)<br>
        Delivery receipts (sent / delivered / read)<br>
        Online presence + "last seen"<br>
        Media sharing (images, video, audio)<br><br>
<span style="color:var(--faint)">OUT OF SCOPE: calls, disappearing msgs, payments</span>
</div>
</div>
<div style="background:var(--panel);border:1px solid var(--bord2);border-left:2px solid var(--cyan);padding:16px">
<div style="font-family:'Exo 2',sans-serif;font-size:14px;font-weight:700;color:var(--white);margin-bottom:10px">Non-Functional</div>
<div style="font-family:'Share Tech Mono',monospace;font-size:10px;color:var(--muted);line-height:2.2">
        2B users, 100M DAU<br>
        100B messages/day → 1.16M msg/sec<br>
        Group fan-out: 1 → up to 1,024 recipients<br>
        Delivery latency p99 &lt; 500ms<br>
        Presence propagation p99 &lt; 1 second<br>
        Availability: 99.99%<br>
        Durability: zero message loss
</div>
</div>
  </div>
  <div class="al grn"><em>The core insight:</em> 100M concurrent users × persistent WebSocket connection = 1,000 Chat Servers. Each server is stateful — it owns those connections. Routing a message means finding the exact server the recipient is connected to. That's the central routing problem.</div>
</div>
<!-- WEBSOCKETS -->
<div class="view" id="view-ws">
  <div class="sh">Why WebSockets?</div>
  <div class="sr">Comparing polling vs long-polling vs WebSockets</div>
  <div class="comp-grid">
<div class="cc" style="border-top-color:var(--red)">
<div class="cc-name">Short Polling</div>
<div class="cc-sub">CLIENT ASKS EVERY 1 SECOND</div>
<div class="cc-body">100M users × 1 req/sec = 100M req/sec. Server overloaded. Most responses are empty. 1-second worst-case latency. Unacceptable.</div>
</div>
<div class="cc" style="border-top-color:var(--amber)">
<div class="cc-name">Long Polling</div>
<div class="cc-sub">HOLD CONNECTION UNTIL MESSAGE</div>
<div class="cc-body">Better than polling. Still stateless. Proxy timeouts force reconnects. Each reconnect requires re-authentication. Reconnect storms on server restart.</div>
</div>
<div class="cc" style="border-top-color:var(--grn)">
<div class="cc-name">WebSockets ★</div>
<div class="cc-sub">PERSISTENT BIDIRECTIONAL TCP</div>
<div class="cc-body">One connection per user. Server pushes instantly. Sub-10ms delivery. Heartbeat ping/pong keeps alive through NAT. Full-duplex — both sides send simultaneously.</div>
</div>
  </div>
  <div class="cb"><div class="cb-top">WebSocket lifecycle<span class="cb-l">PROTOCOL</span></div>


```python
// 1. HTTP Upgrade handshake
GET /ws HTTP/1.1
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==

// Server responds:
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade

// 2. TCP connection stays open — frames flow bidirectionally
Client → Server: {"type":"message","to":456,"content":"Hey!"}
Server → Client: {"type":"message","from":123,"content":"What's up?"}
Server → Client: {"type":"ack","msgId":7890,"status":"delivered"}

// 3. Heartbeat every 30s — keeps connection alive through NAT
Server → Client: PING
Client → Server: PONG

// 4. On disconnect: client reconnects, fetches offline messages via REST
GET /messages/offline?since="last_message_id"
```


</div>
<!-- ARCHITECTURE -->
<div class="view" id="view-arch">
  <div class="sh">Message Send / Receive Path</div>
  <div class="sr">End-to-end: Alice sends "Hey!" → Bob receives in &lt;500ms</div>
  <div class="msg-flow">
<div class="mf-label">// ALICE SENDS MESSAGE TO BOB — FULL PATH</div>
<div class="mf-row"><div class="mf-num">1.</div><div class="mf-node">[Alice]</div><div class="mf-arrow">──WS──→</div><div class="mf-desc">[Chat Server A] &nbsp; <span class="mf-note">Alice's persistent connection</span></div></div>
<div class="mf-row"><div class="mf-num">2.</div><div class="mf-node">[Server A]</div><div class="mf-arrow">writes to</div><div class="mf-desc">[Cassandra: messages table] &nbsp; <span class="mf-note">durable, message_id = Snowflake</span></div></div>
<div class="mf-row"><div class="mf-num">3.</div><div class="mf-node">[Server A]</div><div class="mf-arrow">──WS──→</div><div class="mf-desc">[Alice] &nbsp; <span class="mf-note">ACK: message saved ✓ (single grey tick)</span></div></div>
<div class="mf-row"><div class="mf-num">4.</div><div class="mf-node">[Server A]</div><div class="mf-arrow">publishes</div><div class="mf-desc">[Kafka: "messages"] &nbsp; <span class="mf-note">async routing</span></div></div>
<div class="mf-row"><div class="mf-num">5.</div><div class="mf-node">[Router]</div><div class="mf-arrow">GET session:{bobId}</div><div class="mf-desc">[Redis Session Store] &nbsp; <span class="mf-note">→ "chat-server-C:8080"</span></div></div>
<div class="mf-row"><div class="mf-num">6.</div><div class="mf-node">[Router]</div><div class="mf-arrow">HTTP POST</div><div class="mf-desc">[Chat Server C] &nbsp; <span class="mf-note">forward message to Bob's server</span></div></div>
<div class="mf-row"><div class="mf-num">7.</div><div class="mf-node">[Server C]</div><div class="mf-arrow">──WS──→</div><div class="mf-desc">[Bob] &nbsp; <span class="mf-note">message delivered ✓✓ (double grey)</span></div></div>
<div class="mf-row"><div class="mf-num">8.</div><div class="mf-node">[Bob]</div><div class="mf-arrow">opens chat →</div><div class="mf-desc">sends READ receipt → Server C → Server A → Alice &nbsp; <span class="mf-note">✓✓ blue</span></div></div>
  </div>
  <div class="sh">Offline Message Delivery</div>
  <div class="cb"><div class="cb-top">Bob is offline when message sent — then reconnects<span class="cb-l">FLOW</span></div>


```python
// Bob is offline: message stored in Cassandra (already done — Step 2 above)
// Also: store message_id in inbox:{bobId} sorted set
ZADD inbox:bob {message_id} {message_id}

// Bob reconnects (WebSocket upgrade):
// 1. REST call to fetch missed messages
GET /messages/offline?userId=bob&since={lastReadMessageId}

// 2. Server queries Cassandra for all conversations Bob participates in
// 3. Returns all messages with message_id > lastReadMessageId
// 4. Push to Bob's new WebSocket connection
// 5. Update last_read_message_id = latest received
// 6. Mark each message as delivered → route receipts back to senders
```


</div>
<!-- RECEIPTS -->
<div class="view" id="view-receipts">
  <div class="sh">Message Delivery Receipts</div>
  <div class="sr">Three-state system — the detail that separates good answers from great ones</div>
  <div class="receipt-row">
<div class="rr" style="background:rgba(0,232,122,.03)">
<div class="rr-sym">✓</div>
<div class="rr-name">SENT</div>
<div class="rr-desc">Single grey tick.<br>Message saved to Chat Server &amp; Cassandra.<br>Server ACKs to sender immediately.<br>Guarantee: message will not be lost.</div>
</div>
<div class="rr" style="background:rgba(0,232,122,.05)">
<div class="rr-sym">✓✓</div>
<div class="rr-name">DELIVERED</div>
<div class="rr-desc">Double grey tick.<br>Message reached recipient's device.<br>Recipient's client ACKs via WebSocket.<br>Server updates status, notifies sender.</div>
</div>
<div class="rr" style="background:rgba(0,212,255,.05);border-left:2px solid var(--cyan)">
<div class="rr-sym" style="color:var(--cyan)">✓✓</div>
<div class="rr-name" style="color:var(--cyan)">READ</div>
<div class="rr-desc">Double blue tick.<br>Recipient opened the conversation.<br>Client sends READ event via WebSocket.<br>Routed back to sender. Privacy: can be disabled.</div>
</div>
  </div>
  <div class="cb"><div class="cb-top">Group message receipt tracking<span class="cb-l">SQL / CASSANDRA</span></div>


```sql
-- Option A: counters on message row
ALTER TABLE messages ADD delivered_count INT DEFAULT 0;
ALTER TABLE messages ADD read_count INT DEFAULT 0;
-- ✓✓ shown when delivered_count = group_size
-- ✓✓ blue when read_count = group_size

-- Option B: per-recipient receipts table (more granular, scales better)
CREATE TABLE message_receipts (
    message_id    BIGINT,
    recipient_id  BIGINT,
    status        VARCHAR,  -- 'delivered' | 'read'
    updated_at    TIMESTAMP,
    PRIMARY KEY (message_id, recipient_id)
);
-- Query: SELECT COUNT(*) FROM message_receipts
--        WHERE message_id = X AND status = 'read'
-- Compare to group size → determine if all have read
```


  <div class="al amb"><em>Failure case:</em> What if delivered-ACK is lost in transit? The sender doesn't get ✓✓ but the message was delivered. The recipient should re-send the ACK on next heartbeat or reconnect. Delivered status is idempotent — sending it twice is harmless.</div>
</div>
<!-- PRESENCE -->
<div class="view" id="view-presence">
  <div class="sh">Presence System</div>
  <div class="sr">100M concurrent users sending heartbeats every 30s = 3.3M writes/sec</div>
  <div class="pres-box">
<div class="pb-label">// PRESENCE LIFECYCLE — ALICE'S SESSION</div>
<div class="pb-row"><div class="pb-time">T=0:00</div><div class="pb-event" style="border-color:var(--grn);color:var(--grn)">CONNECT</div><div class="pb-note">SET presence:alice "online" EX 45 &nbsp;|&nbsp; Chat Server registers session</div></div>
<div class="pb-row"><div class="pb-time">T=0:30</div><div class="pb-event" style="border-color:var(--cyan);color:var(--cyan)">HEARTBEAT</div><div class="pb-note">EXPIRE presence:alice 45 &nbsp;|&nbsp; Refreshes TTL — keeps "online"</div></div>
<div class="pb-row"><div class="pb-time">T=1:00</div><div class="pb-event" style="border-color:var(--cyan);color:var(--cyan)">HEARTBEAT</div><div class="pb-note">EXPIRE presence:alice 45 &nbsp;|&nbsp; Continuous 30s cadence</div></div>
<div class="pb-row"><div class="pb-time">T=1:05</div><div class="pb-event" style="border-color:var(--amber);color:var(--amber)">DISCONNECT</div><div class="pb-note">No explicit DEL — key expires in 45 - 5 = 40s</div></div>
<div class="pb-row"><div class="pb-time">T=1:45</div><div class="pb-event" style="border-color:var(--red);color:var(--red)">EXPIRED</div><div class="pb-note">Key gone → GET presence:alice returns NULL → "Last seen 1:05"</div></div>
  </div>
  <div class="cb"><div class="cb-top">Presence read + subscriber-based push<span class="cb-l">REDIS</span></div>


```python
// Write: every 30s heartbeat via WebSocket
SETEX presence:{userId} 45 "online"   // 45s TTL > 30s heartbeat interval

// Read: check if user is online
String val = redis.get("presence:" + userId);
if (val != null) return "Online";
else return "Last seen at " + db.getLastSeen(userId);

// Scaling the writes:
// 100M active users × 1 write/30s = 3.3M writes/sec
// Redis Cluster: shard by hash(userId) across 10+ nodes
// Each node handles ~330K writes/sec → achievable

// Subscriber-based presence notifications (avoids fan-out to all contacts):
// Bob opens chat with Alice → subscribe to presence:{aliceId}
// Alice comes online → notify only active subscribers (open chat windows)
// NOT: notify all 300 of Alice's contacts (expensive, most don't care)
```


</div>
<!-- GROUPS -->
<div class="view" id="view-groups">
  <div class="sh">Group Messaging</div>
  <div class="sr">1 sender → up to 1,024 recipients — fan-out at delivery time</div>
  <div class="fo-boxes">
<div class="fb" style="border-left-color:var(--grn)">
<div class="fb-t">Store Once, Route Many</div>
<div class="fb-b">Group message stored ONE TIME in Cassandra (conversation_id = group_id). Each member's inbox stores only the message_id (pointer). No data duplication.</div>
<div class="fb-code" style="color:var(--grn)">
        messages table: 1 row<br>
        group_member inboxes: 1,024 message_id pointers<br>
        Storage: 1× message + 1,024× 8-byte pointers
</div>
</div>
<div class="fb" style="border-left-color:var(--cyan)">
<div class="fb-t">Fan-Out at Delivery</div>
<div class="fb-b">Fan-out service (Kafka consumer) looks up online group members, finds their Chat Servers via Session Store, routes message to each. Offline members get message in inbox on reconnect.</div>
<div class="fb-code" style="color:var(--cyan)">
        Online (500 of 1,024): WS push immediately<br>
        Offline (524 of 1,024): inbox entry → REST on reconnect<br>
        Throughput: 1,000 groups × 1 msg/group/sec × 512 = 512K pushes/sec
</div>
</div>
  </div>
  <div class="cb"><div class="cb-top">Group message fan-out service<span class="cb-l">JAVA</span></div>


```java
public void handleGroupMessage(GroupMessageEvent e) {
    // 1. Message already stored in Cassandra by Chat Server
    UUID groupId = e.groupId;
    long messageId = e.messageId;

    // 2. Fetch all group members (paginated from Cassandra/Redis)
    List<Long> members = groupService.getMembers(groupId);

    for (long memberId : members) {
        if (memberId == e.senderId) continue;  // skip sender

        String serverAddr = redis.get("session:" + memberId);

        if (serverAddr != null) {
            // Online: route to their Chat Server
            chatRouter.deliver(serverAddr, memberId, messageId);
        } else {
            // Offline: store in inbox for later delivery
            redis.zadd("inbox:" + memberId, messageId, messageId);
        }
    }
}
```


</div>
<!-- DATA MODELS -->
<div class="view" id="view-schema">
  <div class="sh">Data Models</div>
  <div class="sr">Messages (Cassandra), Social Graph, Sessions (Redis)</div>
  <div class="schema">
<div class="schema-hdr"><span>TABLE: messages — Cassandra</span><span style="color:var(--grn)">PRIMARY KEY (conversation_id, message_id DESC)</span></div>
<div class="schema-body">
<div class="col-row" style="border-bottom:1px solid var(--bord2);margin-bottom:4px;padding-bottom:6px">
<span style="font-family:'Share Tech Mono',monospace;font-size:8px;color:var(--muted)">COLUMN</span>
<span style="font-family:'Share Tech Mono',monospace;font-size:8px;color:var(--muted)">TYPE</span>
<span style="font-family:'Share Tech Mono',monospace;font-size:8px;color:var(--muted)">NOTES</span>
</div>
<div class="col-row"><div class="col-n">conversation_id</div><div class="col-t">UUID</div><div class="col-d">Partition key — all messages in chat on same node</div></div>
<div class="col-row"><div class="col-n">message_id</div><div class="col-t">BIGINT</div><div class="col-d">Clustering key DESC — Snowflake ID, newest first, embeds timestamp</div></div>
<div class="col-row"><div class="col-n">sender_id</div><div class="col-t">BIGINT</div><div class="col-d">Who sent it</div></div>
<div class="col-row"><div class="col-n">content</div><div class="col-t">TEXT</div><div class="col-d">Encrypted text (E2E: only decryptable on device)</div></div>
<div class="col-row"><div class="col-n">media_url</div><div class="col-t">TEXT</div><div class="col-d">S3/CDN URL, NULL for text messages</div></div>
<div class="col-row"><div class="col-n">message_type</div><div class="col-t">VARCHAR</div><div class="col-d">'text' | 'image' | 'video' | 'audio' | 'document'</div></div>
<div class="col-row"><div class="col-n">status</div><div class="col-t">VARCHAR</div><div class="col-d">'sent' | 'delivered' | 'read' — updated by receipt events</div></div>
<div style="font-family:'Share Tech Mono',monospace;font-size:9px;color:var(--grn);margin-top:10px;line-height:1.8">
        QUERY "last 50 msgs": SELECT * FROM messages WHERE conversation_id = X LIMIT 50 → single partition ✓<br>
        ORDERING: message_id DESC → newest first, no sort needed ✓<br>
        PAGINATION: WHERE message_id &lt; {cursor} LIMIT 50 → keyset pagination ✓
</div>
</div>
  </div>
  <div class="sh">Media Upload Protocol</div>
  <div class="cb"><div class="cb-top">Client uploads directly to S3 — Chat Server never touches media bytes<span class="cb-l">FLOW</span></div>


```python
// Step 1: Client requests pre-signed upload URL
POST /media/upload/presign
Response: {uploadUrl: "https://s3.../media/uuid.jpg?X-Amz-Signature=...", mediaId: "uuid"}

// Step 2: Client uploads directly to S3 (NOT through Chat Server)
PUT https://s3.amazonaws.com/wa-media/uuid.jpg
Content-Type: image/jpeg
Body: [encrypted image bytes]

// Step 3: Client sends message with media reference
WS: {type:"message", to:456, mediaId:"uuid", mediaType:"image", thumbnail:"base64..."}

// Step 4: Recipient downloads from CDN (not Chat Server)
GET https://cdn.wa.me/media/uuid.jpg  ← edge-cached, fast

// Benefits:
// Chat servers handle only ~200 byte WS frames (never MB of media)
// S3 + CDN handle bandwidth independently
// E2E encryption: client encrypts before upload, only recipient can decrypt
```


</div>
<!-- SCALE -->
<div class="view" id="view-scale">
  <div class="sh">Scale & Estimation</div>
  <div class="sr">Numbers that anchor every architectural decision</div>
  <table class="est-t">
<thead><tr><th>COMPONENT</th><th>VALUE</th><th>CALCULATION</th></tr></thead>
<tbody>
<tr><td>Chat Servers</td><td>~1,000</td><td>100M concurrent users ÷ 100K WS connections/server</td></tr>
<tr><td>Message throughput</td><td>1.16M msg/sec</td><td>100B msg/day ÷ 86,400</td></tr>
<tr><td>Text storage/day</td><td>10 TB/day</td><td>1.16M/sec × 100 bytes × 86,400</td></tr>
<tr><td>With Cassandra replication (3×)</td><td>30 TB/day</td><td>10 TB × 3 replicas</td></tr>
<tr><td>Cassandra nodes (5yr)</td><td>~500 nodes</td><td>30 TB/day × 365 × 5 = 55 PB ÷ 100 TB/node</td></tr>
<tr><td>Session Store (Redis)</td><td>5 GB</td><td>100M sessions × 50 bytes = 5 GB — fits 1 node</td></tr>
<tr><td>Presence writes/sec</td><td>3.3M/sec</td><td>100M users ÷ 30s heartbeat</td></tr>
<tr><td>Presence Redis nodes</td><td>10+ nodes</td><td>3.3M ops/sec ÷ 300K ops/node</td></tr>
<tr><td>Kafka throughput</td><td>~1.2 GB/sec</td><td>1.16M msg/sec × 1 KB avg × 3 replicas</td></tr>
</tbody>
  </table>
  <div class="al grn"><em>Key numbers to say aloud:</em> "1,000 Chat Servers for 100M concurrent WebSocket connections." · "Cassandra (conversation_id, message_id DESC) — single partition read for chat history." · "Presence writes at 3.3M/sec require a Redis Cluster, not a single node." · "Media never touches Chat Servers — S3 pre-signed URL + CDN."</div>
</div>
<!-- TASKS -->
<div class="view" id="view-tasks">
  <div class="task-list">
<div class="task-card">
<div class="task-hd" onclick="mb7_tt(this)"><div class="t-num">01</div><div class="t-lbl">WebSocket Connection Management</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
<div class="task-bd">
<ol>
<li>Alice opens WhatsApp. How does the app choose which Chat Server to connect to? (hint: load balancer with sticky sessions? consistent hashing?)</li>
<li>Chat Server 47 crashes. 100K users lose their connections. What happens step-by-step? How long until they're reconnected?</li>
<li>Bob's phone loses network for 60 seconds. What is queued where? Walk through the exact delivery sequence when he reconnects.</li>
<li>WhatsApp Web: same account open on phone AND laptop. Design the multi-device connection model. How does a message reach both devices?</li>
</ol>
</div>
</div>
<div class="task-card">
<div class="task-hd" onclick="mb7_tt(this)"><div class="t-num">02</div><div class="t-lbl">Delivery Receipt State Machine</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
<div class="task-bd">
<ol>
<li>Draw the state machine for message status: valid states, valid transitions, triggering events</li>
<li>Group of 500 members: when exactly do ✓✓ (delivered) and ✓✓ blue (read) show? All 500? First? Majority?</li>
<li>Failure: message delivered to Bob, but "delivered" ACK lost in transit. How does the system eventually become consistent?</li>
<li>Alice is offline when Bob's read receipt arrives. Where is it stored? When does Alice see the blue tick?</li>
</ol>
</div>
</div>
<div class="task-card">
<div class="task-hd" onclick="mb7_tt(this)"><div class="t-num">03</div><div class="t-lbl">Presence System at 100M Users</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
<div class="task-bd">
<p>Design a presence system with these constraints:</p>
<ul>
<li>Presence heartbeat every 30s from each online user</li>
<li>"Last seen" accurate to within 1 minute</li>
<li>Privacy: some users hide last seen entirely</li>
<li>Must handle 3.3M presence writes/sec</li>
<li>When Alice comes online, notify Bob (who has a chat open with Alice)</li>
</ul>
<p style="margin-top:8px">Design the Redis schema, write path, read path, and subscriber notification mechanism.</p>
</div>
</div>
<div class="task-card" style="border-top:2px solid var(--grn)">
<div class="task-hd" onclick="mb7_tt(this)"><div class="t-num" style="color:var(--grn)">★</div><div class="t-lbl">Full WhatsApp Design — 45-min Simulation</div><div class="t-meta">~3 hrs</div><div class="t-arr">›</div></div>
<div class="task-bd">
<p>Apply all 7 framework steps. Time to 45 minutes:</p>
<ol>
<li>Requirements + estimations: Chat Server count, Cassandra nodes, Redis cluster, Kafka throughput</li>
<li>Full architecture diagram: all components, data flows</li>
<li>Deep dive: WebSocket routing (Session Store lookup, Chat Server statefulness)</li>
<li>Deep dive: group messaging fan-out at 1,024 members</li>
<li>Deep dive: presence at 100M users (heartbeat + Redis TTL + subscriber push)</li>
<li>Failure modes: Chat Server crash, Redis down, Cassandra shard failure</li>
<li>Media pipeline: S3 pre-signed URL → CDN → E2E encryption mention</li>
</ol>
</div>
</div>
  </div>
</div>
<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 15 completed</span><span style="font-family:'Share Tech Mono',monospace">MODULE B7 · WHATSAPP</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">WebSockets vs polling: why WS, lifecycle, heartbeat, reconnect</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Chat Server statefulness: owns connections, Session Store maps user→server</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Full send path: Alice → Server A → Cassandra → Kafka → Router → Server C → Bob</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Session Store: SET session:{userId} serverAddr EX 86400 on connect</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Cassandra schema: (conversation_id, message_id DESC) — single partition chat history</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Offline delivery: inbox sorted set + REST fetch on reconnect with cursor</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">3-state receipts: ✓ sent, ✓✓ delivered, ✓✓ blue read — state machine</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Group receipts: message_receipts table with per-recipient status</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Presence: SETEX 45s TTL + heartbeat 30s + subscribe-based notifications</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Presence scale: 3.3M writes/sec → Redis Cluster (10+ nodes)</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Group messaging: store once, route many, inbox for offline members</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Media: S3 pre-signed URL (client uploads directly) + CDN delivery</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Scale numbers: 1K Chat Servers, 30 TB/day, 3.3M presence writes/sec</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Tasks 1–3: WS management, receipt state machine, presence design</div></div>
<div class="chk" onclick="mb7_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 4 (capstone): full WhatsApp — 45-min interview simulation</div></div>
  </div>
  <div style="margin-top:28px;background:var(--panel);border:1px solid var(--bord2);padding:22px;border-top:2px solid var(--grn)">
<div style="font-family:'Share Tech Mono',monospace;font-size:8px;color:var(--muted);letter-spacing:2px;margin-bottom:8px">// NEXT MODULE</div>
<div style="font-family:'Exo 2',sans-serif;font-size:28px;font-weight:900;color:var(--white);margin-bottom:6px">B8 — Design YouTube</div>
<div style="font-family:'Share Tech Mono',monospace;font-size:9px;color:var(--muted);line-height:2">
      Video upload pipeline · Transcoding (HLS adaptive bitrate)<br>
      CDN video delivery · View counter · Recommendation engine overview<br>
      Search indexing · Comment system · Storage at petabyte scale
</div>
  </div>
  </div>
  <!-- Bottom Navigation -->
  <div class="mb7-bottom-nav">
<a href="/learning/system-design/hld/module-b6-twitter-feed/" class="mb7-nav-footer-btn">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
      B6: Twitter Feed
</a>
<a href="/learning/system-design/hld/module-b7-notes/" class="mb7-nav-footer-btn">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
      READ STUDY NOTES
</a>
<a href="/learning/system-design/system-design-roadmap/" class="mb7-nav-footer-btn">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="17 1 21 5 17 9"></polyline><path d="M3 11V9a4 4 0 0 1 4-4h14"></path><polyline points="7 23 3 19 7 15"></polyline><path d="M21 13v2a4 4 0 0 1-4 4H3"></path></svg>
      ROADMAP
</a>
<a href="/learning/system-design/hld/module-b8-youtube/" class="mb7-nav-footer-btn">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      B8: YouTube
</a>
  </div>
</div>
</div>
<script src="/assets/js/sd-module-b7.js"></script>
