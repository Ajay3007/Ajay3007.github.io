---
layout: default
title: "Module B8 Notes: YouTube"
permalink: /learning/system-design/hld/module-b8-notes/
---


# Module B8 — Design YouTube
## System Design Mastery Course | Track B: HLD | Week 18

---

## 🎯 Module Overview

**Duration:** 1 Week | **Track:** B — HLD Fundamentals Deep Dive  
**Prerequisites:** B1–B7  
**Goal:** YouTube is the canonical video platform design. It introduces upload pipelines, transcoding (the most compute-intensive step in consumer tech), HLS adaptive streaming, 3-tier CDN architecture, and the view counter problem. Master this module and you can answer any media platform question.

---

## 1. Requirements & Scale

```
Functional (in scope):
  Upload video (raw file → processed multi-quality variants)
  Stream video (adaptive bitrate, instant start, no buffering)
  Search by title, description, tags, transcript
  View counter (real-time, approximate)
  Like/dislike/comment/subscribe/notify

Non-Functional:
  2B users/month, 800M DAU
  Upload: 500 hours of video per minute
  Watch: 1 billion hours per day
  Read:Write ≈ 200:1

Scale estimations:
  Upload rate:    8.3 hrs of video per second (500 hrs/min ÷ 60)
  Storage growth: 90 TB/day of processed video
  Storage total:  ~1 exabyte accumulated over 15+ years
  CDN bandwidth:  58 Tbps (1B hrs/day × ~5 Mbps per stream)
  
The CDN bandwidth number is the key: 58 Tbps.
No single datacenter can serve this → CDN IS the product.
```

---

## 2. Upload Pipeline

```
Multi-step protocol — resilient to network failure:

Step 1: POST /upload/initiate
  Body: {filename, size, sha256_hash}
  Response: {uploadId, chunkSize: 5MB}

Step 2: SHA-256 deduplication check
  POST /upload/check?hash=abc123
  If exists → return existing videoId (NO upload needed!)
  → Saves bandwidth AND prevents duplicate transcoding

Step 3: Upload chunks (parallelisable)
  PUT /upload/{uploadId}/chunk/{n}  Body: [5MB bytes]
  On failure: GET /upload/{uploadId}/status → {lastChunk: N}
  Resume from chunk N+1

Step 4: POST /upload/{uploadId}/complete
  Triggers transcoding pipeline
  Returns: {videoId, status: "processing"}

Why chunked? 
  Network dropout at chunk 42 of 100 → resume from chunk 42
  Without chunking: restart entire 2GB upload from zero
```

---

## 3. Transcoding Pipeline

```
The problem: raw 10-min 1080p video = ~2GB. Must produce 6 quality levels:
  360p, 480p, 720p, 1080p, 1440p, 4K

Naive approach: one worker, sequential
  10-min video × 6 qualities × 1× realtime = 60 min to process ← too slow

YouTube's approach: temporal parallelism
  1. Split raw video into 1-minute segments
     10-min video → 10 × 1-minute segments
  2. Dispatch ALL segments to workers simultaneously
     10 workers × 1-min segment each → done in ~1 minute (10× speedup)
  3. Each worker also produces all quality levels in parallel
  4. Concatenate results → complete HLS playlist

60-minute video:
  60 workers × 6 quality encoders = 360 parallel processes
  Wallclock time: ~1 minute regardless of video length ✓

What changes first?
  360p segments available in ~5s → serve immediately
  720p available ~15s → upgrade users who have good bandwidth
  1080p, 4K → follow as they complete
```

### Codec Selection
```
H.264 (AVC): universal support, larger files
  Use: default fallback, smart TVs, older clients

VP9: 30-50% smaller than H.264, Chrome native
  Use: YouTube default on web, Android
  → YouTube already encodes it, serving it saves massive CDN bandwidth

AV1: 50% smaller than H.264, CPU-intensive to decode
  Use: flagship devices, 4K content, low-bandwidth markets

In practice: YouTube encodes both H.264 AND VP9 for every video
  Client sends Accept: video/webm → gets VP9
  Client doesn't → gets H.264
  Double storage cost, but saves 30-50% on CDN bandwidth (worth it at scale)
```

---

## 4. HLS Adaptive Bitrate Streaming

```
HLS = HTTP Live Streaming. Works over plain HTTP (CDN-cacheable).

File structure:
  master.m3u8         ← first thing player downloads
    └── 360p.m3u8     ← list of 2-second .ts segments
    └── 720p.m3u8
    └── 1080p.m3u8
         └── seg_001.ts  (2 seconds of video)
         └── seg_002.ts
         └── seg_003.ts  ...

master.m3u8 contents:
  #EXT-X-STREAM-INF:BANDWIDTH=500000,RESOLUTION=640x360
  https://cdn.youtube.com/v/abc123/360p.m3u8

  #EXT-X-STREAM-INF:BANDWIDTH=5000000,RESOLUTION=1920x1080
  https://cdn.youtube.com/v/abc123/1080p.m3u8

Player algorithm (every 2 seconds):
  Measure current download bandwidth
  Compare to BANDWIDTH values in master.m3u8
  Select best quality that bandwidth supports
  Next segment request goes to new quality level
  → Seamless quality switch, no rebuffering

The critical insight: each .ts segment is independent.
Switching quality means switching to a different .m3u8 playlist.
The switch happens between segments → no disruption.
```

---

## 5. 3-Tier CDN Architecture

```
The 58 Tbps problem requires 3 tiers:

Tier 1: Edge PoPs (Points of Presence)
  Count:    1,000+ globally
  Latency:  5–20ms from user
  Content:  Hot content (top 10% of videos = 90% of views)
  Storage:  10–100 TB per PoP
  Hit rate: ~80%

Tier 2: Regional Cache
  Count:    ~100 nodes
  Latency:  30–60ms
  Content:  Warm content (missed at edge)
  Storage:  ~1 PB per node
  Hit rate: ~15% (of remaining traffic)

Tier 3: Origin (GCS/S3)
  Latency:  100–200ms
  Content:  Cold / long-tail videos
  Serves:   ~5% of total requests

CDN Pre-warming:
  Big channel upload → don't wait for cache misses
  if (subscriberCount > 1M) → prefetch to ALL edge PoPs
  if (viewVelocity > 10K/min) → prefetch to all edges (virality detection)
  Pre-warm only first 5 segments (10-30s) → covers most users' "quick skip" behaviour
```

---

## 6. View Counter Design

```
Scale: 11,600 views/sec globally. Viral video: 2,778 views/sec on ONE video.
Naive approach: UPDATE videos SET views = views + 1 → shuts down MySQL.

Production solution (3 layers):

Layer 1: Redis Sharded Counter (display, ~immediate)
  INCR view_count:{videoId}:shard_{random(10)}
  Read: SUM all 10 shards
  Pre-warm on Redis cluster restart (durability concern)

Layer 2: Kafka event stream (durability + analytics)
  kafka.publish("view-events", {videoId, userId, ip, timestamp, country})
  Durable — survives Redis failure
  Async — doesn't add latency to view response

Layer 3: ClickHouse (analytics, creator dashboard)
  ClickHouse consumer reads Kafka
  Supports: views per hour, per country, per device type
  SQL: SELECT COUNT(*) FROM view_events WHERE video_id=X AND hour=Y

Spam prevention:
  SETNX view-dedup:{videoId}:{ip}:{hour} 1  EX 3600
  If key already exists → view not counted (same IP, same hour)
  Stateless dedup — no DB lookup, just Redis atomic check
```

---

## 7. Storage Strategy

```
Object storage layout:
  raw/{videoId}/original.mp4           ← DELETED after transcoding
  processed/{videoId}/master.m3u8
  processed/{videoId}/360p/seg_001.ts
  processed/{videoId}/1080p/seg_001.ts
  thumbnails/{videoId}/thumb_1.jpg

Cost tiering by popularity:
  > 100 views/month:   Standard storage (fast, expensive)
  10–100 views/month:  Nearline (slightly slower, 50% cheaper)
  < 10 views/month:    Coldline (80% cheaper)
  < 1 view/month:      Archive (95% cheaper, hours to retrieve)

Key insight: ~80% of YouTube videos have < 1,000 total views
  Tiering the long tail to cold storage saves enormous cost

Replication: GCS multi-region = automatic 3× AZ replication
Cross-region: popular videos replicated to US, EU, APAC buckets
```

---

## 8. Search Architecture

```
Search system:
  Primary DB: MySQL (structured video metadata)
  Search index: Elasticsearch (full-text search)
  Sync: MySQL → Debezium CDC → Kafka → Elasticsearch consumer

Elasticsearch document:
  {
    videoId:            "abc123",
    title:              "How to make pasta"     ← full-text, heavily weighted
    description:        "Step by step guide..."  ← full-text
    tags:               ["cooking", "pasta"]      ← exact match
    transcript:         "Today we're making..."   ← auto-generated captions
    viewCount:          1500000                   ← signal for ranking
    uploadDate:         "2024-01-15"              ← recency signal
    channelSubscribers: 5000000                   ← authority signal
  }

Autocomplete: ES "search_as_you_type" field type on title
  Returns suggestions after 2 characters
  Cached for top 1000 queries → sub-ms response

Sync lag: CDC-based sync may lag MySQL by seconds → acceptable
  Users don't expect search results for a video in first 10 seconds after upload
```

---

## 📝 Tasks

### Task 1 — Transcoding Pipeline Design
1. How many transcoding workers are needed for 8.3 hrs/sec input? Show the math.
2. Design the Kafka topic + partition key for transcoding job queue
3. A 4-hour video, temporal parallelism, 240 segments. How do you coordinate concatenation?
4. Worker crashes at segment 42 of 240. How do you resume?
5. Priority queue: paid creators get priority. Design the mechanism.

### Task 2 — CDN Caching Strategy
1. Mr. Beast uploads (230M subs) — what happens in the first 10 minutes?
2. Steady video: 500K views/day for 5 years. What tier is it cached at?
3. Long-tail: 2 views/month — should it be on CDN at all?
4. 50M people watch live event simultaneously — thundering herd on CDN?
5. Creator updates thumbnail after 1M views — how to purge 1,000+ edge nodes?

### Task 3 — View Counter at Scale
1. Viral video: 10M views in 1 hour (2,778/sec on single video)
2. Must display count with &lt; 30 second lag
3. Redis crash should NOT lose counts (durability)
4. Spam prevention: same IP same hour counts once only
5. Analytics: views-per-hour for last 30 days in creator dashboard

### ⭐ Task 4 — Full YouTube Design (45-min simulation)
Cover all 8 components: requirements, estimation, upload pipeline, transcoding, HLS, CDN, view counter, failure modes.

---

## ✅ Completion Checklist

- [ ] Requirements: upload, stream, search, view count, 200:1 read:write ratio
- [ ] Estimation: 90 TB/day storage, 58 Tbps CDN bandwidth
- [ ] Chunked upload: uploadId, 5 MB chunks, SHA-256 dedup, resume
- [ ] Transcoding: temporal parallelism, 60× speedup for 60-min video
- [ ] Codec trade-offs: H.264 (universal), VP9 (30-50% smaller), AV1 (future)
- [ ] HLS: master.m3u8 → quality .m3u8 → 2s .ts segments
- [ ] Adaptive bitrate: bandwidth measured every 2s, switch at segment boundary
- [ ] CDN 3-tier: edge (80% hit) → regional (15%) → origin (5%)
- [ ] CDN pre-warming: subscriber count + view velocity triggers
- [ ] View counter: sharded Redis + Kafka durability + ClickHouse analytics
- [ ] Spam: SETNX dedup per IP per hour
- [ ] Storage lifecycle: hot → nearline → coldline → archive by popularity
- [ ] Search: Elasticsearch + CDC sync from MySQL
- [ ] Completed Task 1 — transcoding pipeline design
- [ ] Completed Task 2 — CDN strategy
- [ ] Completed Task 3 — view counter at scale
- [ ] Completed Task 4 — full YouTube design simulation

**→ Next: Module B9 — Rate Limiter**

<br>

<div style="display: flex; justify-content: space-between; align-items: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1);">
  <a href="/learning/system-design/hld/module-b8-youtube/" style="display: inline-flex; align-items: center; gap: 8px; padding: 12px 20px; background: rgba(0, 232, 122, 0.1); color: #00e87a; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 0.9rem; transition: background 0.2s;">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    BACK TO VISUAL PAGE
  </a>
  <a href="/learning/system-design/hld/" style="display: inline-flex; align-items: center; gap: 8px; padding: 12px 20px; background: rgba(0, 212, 170, 0.1); color: #00d4aa; text-decoration: none; border-radius: 6px; font-weight: 600; font-size: 0.9rem; transition: background 0.2s;">
    BACK TO HLD TRACK
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
  </a>
</div>
