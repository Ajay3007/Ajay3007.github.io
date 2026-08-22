---
title: "Module B6 Notes: Twitter/X Feed"
description: "Module B6 — Design Twitter/X Feed System Design Mastery Course Track B: HLD Week 16 --- 🎯 Module Overview Duration: 1 Week Track: B — HLD Case Studies Prerequisites: B1–B5…"
domain: system-design
track: system-design-hld
order: 113
url: /learning/system-design/hld/module-b6-notes/
---

# Module B6 — Design Twitter/X Feed
## System Design Mastery Course | Track B: HLD | Week 16

---

## 🎯 Module Overview

**Duration:** 1 Week | **Track:** B — HLD Case Studies
**Prerequisites:** B1–B5 (all fundamentals + URL Shortener)
**Goal:** Twitter/X Feed is the canonical FAANG interview question for social systems. It forces you to make the single hardest trade-off in feed design: fan-out on write vs fan-out on read. Master both models and the hybrid.

---

## 1. Requirements

### Functional
```
1. Post a tweet (text ≤ 280 chars, optional media)
2. Follow / unfollow users
3. Home timeline: latest ~200 tweets from people I follow
4. User timeline: all tweets from a specific user
5. Search tweets (full-text)
6. Trending topics / hashtags
7. Likes, retweets, replies (counts)
```

### Non-Functional (Scale)
```
Users:           300M total, 100M DAU
Tweets/day:      500M (5,800/sec avg, 15,000/sec peak)
Timeline reads:  28B/day → 320K reads/sec avg, 800K/sec peak
Read:Write ratio ~50:1 (timeline reads vs tweet posts)
Follows:         avg 200 followers, some celebrities have 100M+
Storage/tweet:   ~280 bytes text + metadata ≈ 1 KB total
Storage/day:     500M × 1 KB = 500 GB/day
5yr total:       ~900 TB (text only), multi-PB with media

Latency targets:
  Home timeline load: p99 < 200ms
  Post tweet:         p99 < 500ms
  Search results:     p99 < 1s
```

---

## 2. The Core Problem: Home Timeline

The home timeline is the hard part. Given user U who follows 500 people, each of whom tweets ~3×/day:

```
Naive approach: at read time, fetch tweets from all 500 followees, merge, sort.
  500 followees × DB query each = 500 queries per timeline load
  At 320K timeline reads/sec: 160M DB queries/sec → IMPOSSIBLE

Better approach: pre-compute the timeline. But HOW?
```

---

## 3. Fan-Out on Write (Push Model)

When user A tweets, **push** the tweet ID to the inbox of every follower.

```
User A (200 followers) posts tweet T:
  For each follower F in A.followers:
    timeline:F.prepend(T.id)   ← Redis sorted set, score = timestamp

Timeline read for user U:
  ZREVRANGE timeline:U 0 199   ← O(1) read from Redis
  Batch fetch tweet content: MGET tweet:id1 tweet:id2 ...
```

### Data Flow
```
[POST /tweet] → Kafka topic "tweet-created"
                     │
                     ↓
          [Fanout Worker Service]
            reads user A's followers from social graph DB
            for each follower F: ZADD timeline:F timestamp tweetId
                     │
                     ↓
           [Redis timeline cache]
           timeline:userId → sorted set of tweet IDs (latest 1000)
```

### Trade-offs
```
✅ Timeline read is instant — O(1) Redis lookup
✅ Scales reads to millions/sec easily
✅ Consistent experience — all followers see tweet immediately after fanout

❌ Write amplification: 1 tweet × 100M followers = 100M Redis writes
❌ Celebrities (Lady Gaga, 100M followers) cause massive write spikes
❌ Wasted writes: pushed to timelines of inactive users who never open app
❌ Timeline storage: 300M users × 1000 tweet IDs × 8 bytes = 2.4 TB in Redis
```

---

## 4. Fan-Out on Read (Pull Model)

At read time, **pull** tweets from all followees and merge.

```
Timeline read for user U (follows 500 people):
  1. Fetch U's follow list: SELECT followee_id FROM follows WHERE follower_id = U
  2. For each followee F: fetch recent tweets (last 200)
  3. Merge all tweet streams by timestamp, take top 200
  4. Return to user
```

### Trade-offs
```
✅ No write amplification — 1 tweet = 1 DB write
✅ Works perfectly for celebrities (no 100M-follower write spike)
✅ No wasted storage for inactive user timelines

❌ Read is expensive: 500 DB queries per timeline load
❌ 320K reads/sec × 500 queries = 160M queries/sec → impossible at scale
❌ Latency is high: merging 500 streams takes 100–500ms
❌ Hot users' tweet tables are hotspots for reads
```

---

## 5. Hybrid Approach (What Twitter Actually Uses)

Combine both models based on follower count:

```
Rule:
  Normal users (< 10K followers): fan-out on WRITE
  Celebrities   (≥ 10K followers): fan-out on READ (lazy inject at read time)

POST tweet by @normalUser (800 followers):
  → Fanout service pushes tweet ID to 800 followers' Redis timelines immediately
  → Fast fanout, manageable write cost

POST tweet by @ladygaga (100M followers):
  → Tweet stored in DB + tweet cache only
  → NO immediate fanout (would require 100M Redis writes)

READ timeline for user U:
  1. Fetch pre-computed timeline from Redis (fan-out-on-write tweets)
  2. Check follow list for celebrities U follows
  3. Fetch recent tweets from each celebrity (fan-out-on-read component)
  4. Merge the two sets by timestamp
  5. Return top 200

This limits celebrity fanout reads to ~number of celebrities U follows (~few dozen max)
```

---

## 6. Data Model

### Tweets Table (MySQL sharded by user_id)
```sql
CREATE TABLE tweets (
    tweet_id     BIGINT PRIMARY KEY,    -- Snowflake ID (encodes timestamp)
    user_id      BIGINT NOT NULL,       -- author
    content      VARCHAR(280),
    media_ids    JSON,                  -- array of S3 keys
    reply_to_id  BIGINT,               -- NULL if not a reply
    retweet_of   BIGINT,               -- NULL if not a retweet
    like_count   BIGINT DEFAULT 0,     -- approximate, updated async
    retweet_count BIGINT DEFAULT 0,
    created_at   TIMESTAMP,
    INDEX (user_id, created_at DESC)   -- user timeline query
);
```

### Follows Table (separate social graph service)
```sql
CREATE TABLE follows (
    follower_id  BIGINT NOT NULL,
    followee_id  BIGINT NOT NULL,
    created_at   TIMESTAMP,
    PRIMARY KEY (follower_id, followee_id),
    INDEX (followee_id)                -- "who follows @ladygaga?"
);
```

### Redis Timeline Cache
```
Key: timeline:{userId}
Type: Sorted Set (ZSet)
Score: tweet timestamp (Unix epoch ms)
Member: tweet_id

ZADD timeline:123 1700000000 tweet_id_abc
ZREVRANGE timeline:123 0 199  ← top 200 most recent tweet IDs
Max size: 1000 entries per user (ZREMRANGEBYRANK to trim)
```

### Tweet Content Cache (Redis)
```
Key: tweet:{tweetId}
Type: Hash
Fields: userId, content, likeCount, retweetCount, createdAt
TTL: 24 hours
HGETALL tweet:{id}  ← hydrate tweet for display
```

---

## 7. Architecture

```
[Client]
    │
    ├─ POST /tweet ──→ [Tweet Service] ──→ [MySQL: tweets shard]
    │                        └──────────→ [Kafka: tweet-created]
    │                                              │
    │                                   [Fanout Service]
    │                                    reads social graph
    │                                    pushes to Redis timelines
    │                                    (skips celebrities)
    │
    ├─ GET /home-timeline ──→ [Timeline Service]
    │                               ├─ ZREVRANGE timeline:{userId} from Redis
    │                               ├─ inject celebrity tweets (fan-out-on-read)
    │                               ├─ merge by timestamp
    │                               └─ MGET tweet:{id} for each (batch hydrate)
    │
    ├─ GET /user-timeline ──→ [Tweet Service]
    │                          SELECT * FROM tweets WHERE user_id=? ORDER BY created_at DESC
    │
    ├─ POST /follow ──→ [Social Graph Service] ──→ [Graph DB / MySQL: follows]
    │
    └─ GET /search ──→ [Search Service] ──→ [Elasticsearch index]
```

---

## 8. Media Storage

```
Tweets with images/videos:
  Upload:  Client → CDN upload endpoint → S3 (origin)
  Serve:   Client → CDN edge (cached) → S3 (on miss)

Tweet stores: media_ids: ["s3://tweets/2024/01/img_abc.jpg"]
CDN URL:      https://pbs.twimg.com/media/img_abc.jpg

Video transcoding:
  Raw upload → S3 raw bucket → Lambda/Worker → transcode to HLS (multiple bitrates)
  → S3 transcoded bucket → CDN

Why CDN is essential:
  Viral tweet with 100M impressions × 500KB image = 50 TB transferred
  Without CDN: origin S3 + bandwidth bill is astronomical
  With CDN: 99%+ cache hit rate for popular media
```

---

## 9. Search & Trending

### Search (Elasticsearch)
```
On tweet creation → Kafka → Search indexer consumer → Elasticsearch index
  Index fields: content (full-text), userId, timestamp, likeCount

Query: GET /search?q=ukraine+war
  Elasticsearch: full-text match + rank by (recency + engagement)
  Response: top 50 tweet IDs → hydrate from tweet cache
```

### Trending Topics
```
Approach: sliding window count of hashtags

Implementation:
  Kafka stream: extract hashtags from each tweet
  Flink/Storm: count per hashtag in 1-hour sliding window
  Top-K: maintain min-heap of top 30 hashtags
  Store: Redis sorted set "trending" → ZADD trending count #hashtag
  Read: ZREVRANGE trending 0 9 ← top 10

Refresh rate: every 5 minutes
Geographic trending: separate sorted set per region (trending:US, trending:IN)
```

---

## 10. Counts (Likes, Retweets, Followers)

```
Problem: 500M tweets/day × likes/retweets = billions of write ops/day
         Can't UPDATE tweets SET like_count += 1 synchronously at this rate

Solution: Counter service with async aggregation

1. User likes tweet → POST /like
2. Immediately: write to likes table (for "did I like this?" check)
3. Async: Kafka event "tweet-liked" → counter aggregation worker
4. Counter worker: batches 1000 events → UPDATE tweets SET like_count += N
   Or: Redis INCR like_count:{tweetId} → periodic flush to DB

Display: serve from Redis cache (approximate) — exact count in DB
Accuracy: ~1-5 second lag. Acceptable — Twitter shows "1.2M likes" not "1,234,567"
```

---

## 📝 Tasks

### Task 1 — Fan-Out Analysis
Calculate the cost of fan-out on write for these scenarios:
- 100M-follower celebrity tweets once → how many Redis writes?
- 100K users each follow this celebrity → how many extra reads at timeline load?
- What's the storage difference: full fan-out-on-write vs hybrid (threshold 10K followers)?

### Task 2 — Data Model Extension
Extend the schema to support:
1. Twitter Lists (user-created collections of accounts)
2. Tweet thread / conversation chains
3. Quote tweets (retweet with comment)
4. Pinned tweets (shown first on user profile)

### Task 3 — Failure Scenarios
Design failure handling for:
1. Fanout service crashes mid-fanout (10M of 100M followers updated, then crash)
2. Redis timeline cache is wiped (cache miss for all 300M users simultaneously)
3. Social graph DB is down (can't resolve followers for fanout)
4. Elasticsearch is unavailable (search requests fail)

### ⭐ Task 4 — Full Design Interview Simulation
Set a 45-minute timer. On a blank sheet of paper, design Twitter's home timeline from scratch using the 7-step framework. Include:
- Requirements + NFRs with numbers
- Capacity estimation
- Full architecture diagram
- Fan-out decision + hybrid threshold justification
- DB schema (tweets + follows)
- Redis timeline cache design
- At least 2 edge cases
- 1 scaling evolution (what changes at 10× current scale)

---

## ✅ Checklist

- [ ] Can state Twitter's scale: 300M users, 500M tweets/day, 320K timeline reads/sec
- [ ] Explain fan-out on write: what it does, write amplification problem
- [ ] Explain fan-out on read: what it does, read fan-out problem
- [ ] Know the hybrid approach: threshold-based, celebrity inject at read time
- [ ] Can draw the complete architecture with all 6 services
- [ ] Know the Redis timeline cache design (sorted set, score = timestamp)
- [ ] Know the DB schema: tweets table + follows table + indexes
- [ ] Understand the celebrity problem and why it breaks pure fan-out-on-write
- [ ] Know how likes/counts are handled (async Kafka counter service)
- [ ] Know media storage: S3 + CDN + transcoding pipeline
- [ ] Know trending topics: sliding window, Flink, Redis sorted set
- [ ] Know search: Elasticsearch, indexing pipeline, hydration pattern
- [ ] Tasks 1–3 completed
- [ ] Task 4: Full 45-min timed simulation completed

<br>
<div style="margin-top:40px;display:flex;flex-wrap:wrap;gap:12px;font-family:'IBM Plex Mono',monospace;font-size:13px;border-top:1px solid #ddd;padding-top:20px;">
  <a href="/learning/system-design/hld/module-b5-notes/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">← B5 URL Shortener Notes</a>
  <a href="/learning/system-design/hld/module-b6-twitter-feed/" style="padding:12px 24px;border:1px solid #00d4aa;color:#00d4aa;border-radius:4px;text-decoration:none;font-weight:600;">⚡ Interactive Module</a>
  <a href="/learning/system-design/system-design-roadmap/" style="padding:12px 24px;border:1px solid #ccc;border-radius:4px;color:#666;text-decoration:none;">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-b7-notes/" style="padding:12px 24px;background:#00d4aa;color:#1a1f36;border-radius:4px;text-decoration:none;font-weight:600;">NEXT: B7 WhatsApp →</a>
</div>
