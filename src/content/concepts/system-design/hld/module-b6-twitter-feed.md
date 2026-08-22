---
title: "Module B6: Twitter/X Feed"
description: "Track B · HLD Case Study · Module B6 · Week 16 TWITTER/ X FEED FAN-OUT ON WRITE · FAN-OUT ON READ · HYBRID MODEL SOCIAL GRAPH · TIMELINE CACHE · CELEBRITY PROBLEM 500M…"
domain: system-design
track: system-design-hld
order: 112
chrome: bare
ownHeader: true
url: /learning/system-design/hld/module-b6-twitter-feed/
---

<link rel="stylesheet" href="/assets/css/sd-module-b6.css">
<div class="sd-module-b6">
<div class="signal-bar"></div>
<header>
  <div class="hdr-body">
<div>
<div class="hdr-eye">Track B · HLD Case Study · Module B6 · Week 16</div>
<h1 class="mb6-h1">TWITTER/<span class="acc">X</span><br>FEED</h1>
<div class="hdr-sub">FAN-OUT ON WRITE · FAN-OUT ON READ · HYBRID MODEL<br>SOCIAL GRAPH · TIMELINE CACHE · CELEBRITY PROBLEM</div>
</div>
<div class="hdr-stats">
<div class="hs"><div class="hs-v">500M</div><div class="hs-l">TWEETS/DAY</div></div>
<div class="hs"><div class="hs-v">320K</div><div class="hs-l">TIMELINE RD/SEC</div></div>
<div class="hs"><div class="hs-v">100M</div><div class="hs-l">MAX FOLLOWERS</div></div>
<div class="hs"><div class="hs-v">B6</div><div class="hs-l">MODULE</div></div>
</div>
  </div>
  <div class="tag-row">
<div class="tg" style="border-color:var(--cyan);color:var(--cyan)">Fan-Out Write</div>
<div class="tg" style="border-color:var(--green);color:var(--green)">Fan-Out Read</div>
<div class="tg" style="border-color:var(--amber);color:var(--amber)">Hybrid Model</div>
<div class="tg" style="border-color:var(--pur);color:var(--pur)">Celebrity Problem</div>
<div class="tg" style="border-color:var(--red);color:var(--red)">Write Amplification</div>
<div class="tg">Redis ZSet Timeline</div>
<div class="tg">Async Counts</div>
<div class="tg">CDN Media</div>
  </div>
</header>
<nav class="nav">
  <div class="nt active" onclick="mb6_show('scale',this)">Scale</div>
  <div class="nt" onclick="mb6_show('core',this)">Core Problem</div>
  <div class="nt" onclick="mb6_show('fanout',this)">Fan-Out Models</div>
  <div class="nt" onclick="mb6_show('hybrid',this)">Hybrid ★</div>
  <div class="nt" onclick="mb6_show('schema',this)">Data Model</div>
  <div class="nt" onclick="mb6_show('arch',this)">Architecture</div>
  <div class="nt" onclick="mb6_show('counts',this)">Counts</div>
  <div class="nt" onclick="mb6_show('media',this)">Media & Search</div>
  <div class="nt" onclick="mb6_show('tasks',this)">Tasks</div>
  <div class="nt" onclick="mb6_show('checklist',this)">Checklist</div>
</nav>
<div class="content">
<!-- SCALE -->
<div class="view active" id="view-scale">
  <div class="sh">Twitter at Scale</div>
  <div class="sr">The numbers that drive every architectural decision</div>
  <table class="sc-table">
<thead><tr><th>METRIC</th><th>VALUE</th><th>IMPLICATION</th></tr></thead>
<tbody>
<tr><td>Total users</td><td>300M</td><td>Social graph: 300M × avg 400 follows = 120B follow edges</td></tr>
<tr><td>DAU</td><td>100M</td><td>Only 33% active daily — fanout to inactive users is wasteful</td></tr>
<tr><td>Tweets/day</td><td>500M</td><td>5,800/sec avg, 15,000/sec peak</td></tr>
<tr><td>Timeline reads/day</td><td>28B</td><td>320K reads/sec avg → 800K/sec peak</td></tr>
<tr><td>Read:Write ratio</td><td>~50:1</td><td>System is overwhelmingly read-heavy → cache everything</td></tr>
<tr><td>Avg followers</td><td>200</td><td>Fan-out write cost: 5,800 × 200 = 1.16M Redis writes/sec</td></tr>
<tr><td>Max followers</td><td>100M+</td><td>Celebrities break fan-out-on-write completely</td></tr>
<tr><td>Storage/tweet</td><td>~1 KB</td><td>500M/day × 1KB = 500 GB/day text only</td></tr>
</tbody>
  </table>
  <div class="al cy"><em>The hard constraint:</em> A celebrity with 100M followers tweets once → fan-out on write = 100M Redis writes in seconds. At peak, that's 1.5 TRILLION writes/sec if all celebrities tweet simultaneously. This single fact forces the hybrid approach.</div>
</div>
<!-- CORE PROBLEM -->
<div class="view" id="view-core">
  <div class="sh">The Core Problem: Home Timeline</div>
  <div class="sr">Why the naive approach fails — and what "fan-out" means</div>
  <div class="cb"><div class="cb-top">Why you can't just query at read time<span class="cb-l">MATH</span></div>


```python
// User U follows 500 people. Naive read-time approach:
SELECT tweet_id FROM tweets WHERE user_id IN (followee_1, followee_2, ... followee_500)
ORDER BY created_at DESC LIMIT 200;

// Cost: 500 DB queries (or 1 massive IN query) per timeline load
// 320,000 timeline reads/sec × 500 queries = 160,000,000 queries/sec
// A well-tuned MySQL handles ~100,000 QPS → need 1,600 DB nodes
// Merge latency: 500 streams × network roundtrip → 200–500ms → SLA violation

// Conclusion: pure read-time fan-out is IMPOSSIBLE at Twitter scale
// We must pre-compute (at least partially) the home timeline
```


  <div class="al am"><em>Fan-out</em> = distributing one event (a new tweet) to N destinations (follower timelines). The question is: do you fan-out at write time (push) or at read time (pull)?</div>
</div>
<!-- FAN-OUT MODELS -->
<div class="view" id="view-fanout">
  <div class="sh">Fan-Out on Write vs Fan-Out on Read</div>
  <div class="sr">The fundamental trade-off — write amplification vs read amplification</div>
  <div class="fo-grid">
<div class="fo-card" style="border-top-color:var(--cyan)">
<div class="fo-name" style="color:var(--cyan)">Fan-Out on Write</div>
<div style="font-family:'Fira Code',monospace;font-size:8px;color:var(--muted);margin-bottom:10px;letter-spacing:1px">PUSH MODEL — pre-compute timeline at write time</div>
<div class="fo-body">User A tweets → fanout service pushes tweet ID into every follower's Redis timeline immediately. Timeline read = instant O(1) sorted set lookup.</div>
<div class="fo-pros">✓ Timeline read: O(1) Redis → instant<br>✓ Scales reads to millions/sec easily<br>✓ No per-user read complexity</div>
<div class="fo-cons">✗ Write amplification: 1 tweet × 100M followers<br>✗ Celebrities break this model entirely<br>✗ Wastes writes for inactive users<br>✗ Redis storage: 300M timelines</div>
</div>
<div class="fo-card" style="border-top-color:var(--green)">
<div class="fo-name" style="color:var(--green)">Fan-Out on Read</div>
<div style="font-family:'Fira Code',monospace;font-size:8px;color:var(--muted);margin-bottom:10px;letter-spacing:1px">PULL MODEL — compute timeline at read time</div>
<div class="fo-body">No pre-computation. At read time, fetch recent tweets from all followees, merge by timestamp. Works perfectly for celebrities — their tweet is one DB write.</div>
<div class="fo-pros">✓ No write amplification — 1 tweet = 1 write<br>✓ Celebrities work fine<br>✓ No wasted storage for inactive users</div>
<div class="fo-cons">✗ 500 DB queries per timeline read<br>✗ 320K reads/sec × 500 = 160M QPS → impossible<br>✗ Merge latency: 200–500ms<br>✗ Hot followee tables under load</div>
</div>
  </div>
  <div class="al cy"><em>Interview insight:</em> Neither model works alone at Twitter's scale. The question "fan-out on write or read?" is a trap — the correct answer is always "it depends on follower count, and we use a hybrid."</div>
</div>
<!-- HYBRID -->
<div class="view" id="view-hybrid">
  <div class="sh">Hybrid Approach ★</div>
  <div class="sr">Fan-out on write for normal users · Fan-out on read for celebrities</div>
  <div class="hyb-box">
<div class="hyb-title">// HYBRID RULE — threshold-based routing</div>
<div class="hyb-rule" style="border-color:var(--cyan)">
<div class="hr-cond" style="color:var(--cyan)">followers &lt; 10,000</div>
<div class="hr-arrow">→</div>
<div class="hr-action"><span style="color:var(--white)">Fan-out on WRITE</span> — push tweet ID to all follower timelines in Redis immediately</div>
</div>
<div class="hyb-rule" style="border-color:var(--amber)">
<div class="hr-cond" style="color:var(--amber)">followers ≥ 10,000</div>
<div class="hr-arrow">→</div>
<div class="hr-action"><span style="color:var(--white)">Fan-out on READ</span> — tweet stored in DB only; injected at timeline read time</div>
</div>
  </div>
  <div class="sh">Timeline Read — Hybrid Merge</div>
  <div class="cb"><div class="cb-top">How timeline service assembles the feed<span class="cb-l">PSEUDOCODE</span></div>


```python
function getHomeTimeline(userId, limit=200):

    // 1. Pre-computed portion (fan-out-on-write tweets)
    precomputed = redis.ZREVRANGE("timeline:" + userId, 0, limit * 2, WITHSCORES)
    //    O(log N) — fast, covers all normal users the person follows

    // 2. Celebrity injection (fan-out-on-read portion)
    celebrities = socialGraph.getCelebrityFollowees(userId)
    //    Typically <50 celebrities per user (manageable)

    celeb_tweets = []
    for celeb in celebrities:
        recent = tweetCache.getRecentTweets(celeb.userId, n=50)
        celeb_tweets.extend(recent)
    //    50 celebrities × 50 tweets = 2,500 tweet fetches (cached in Redis)

    // 3. Merge by timestamp + deduplicate retweets
    merged = mergeSortedByTimestamp(precomputed, celeb_tweets)
    return merged[:limit]

    // Total latency: ~5–20ms (all Redis operations)
```



  <div class="sh">Fanout Worker Service</div>
  <div class="cb"><div class="cb-top">What happens when @normalUser (800 followers) tweets<span class="cb-l">FLOW</span></div>


```python
POST /tweet → [Tweet Service]
  → INSERT INTO tweets (tweet_id=snowflake(), user_id, content, ...) ✓ durable
  → HSET tweet:{id} userId content likeCount ...                    ✓ cached
  → Kafka.publish("tweet-created", {tweetId, userId, followerCount})

[Fanout Worker] consumes from Kafka:
  if followerCount < 10_000:
      followers = socialGraph.getFollowers(userId)    // read from graph DB
      for followerId in followers:
          redis.ZADD("timeline:"+followerId, timestamp, tweetId)
          redis.ZREMRANGEBYRANK("timeline:"+followerId, 0, -1001)  // keep top 1000
  else:
      // Celebrity: just ensure tweet is in tweet cache, no fanout
      // Timeline reads will inject this lazily
      redis.HSET("tweet:"+tweetId, ...)
```


  <div class="al gn"><em>The elegance:</em> Normal users (99.9% of accounts) get instant fan-out with manageable write cost. Celebrities get lazy injection with zero write amplification. The merge at read time costs ~50 celebrity fetches — all from Redis — adding only 1–2ms to timeline load.</div>
</div>
<!-- SCHEMA -->
<div class="view" id="view-schema">
  <div class="sh">Data Model</div>
  <div class="sr">Tweets table · Follows table · Redis timeline cache</div>
  <div class="schema-box">
<div class="sb-hdr"><span>TABLE: tweets — sharded by user_id</span><span style="color:var(--cyan)">MySQL</span></div>
<div class="sb-body">
<div class="col-row" style="border-bottom:1px solid var(--bord2);margin-bottom:4px">
<div style="font-family:'Fira Code',monospace;font-size:8px;color:var(--muted)">COLUMN</div>
<div style="font-family:'Fira Code',monospace;font-size:8px;color:var(--muted)">TYPE</div>
<div style="font-family:'Fira Code',monospace;font-size:8px;color:var(--muted)">NOTES</div>
</div>
<div class="col-row"><div class="c-n">tweet_id</div><div class="c-t">BIGINT</div><div class="c-d">Snowflake ID — encodes timestamp, no separate created_at needed</div></div>
<div class="col-row"><div class="c-n">user_id</div><div class="c-t">BIGINT</div><div class="c-d">Author — shard key</div></div>
<div class="col-row"><div class="c-n">content</div><div class="c-t">VARCHAR(280)</div><div class="c-d">Tweet text</div></div>
<div class="col-row"><div class="c-n">media_ids</div><div class="c-t">JSON</div><div class="c-d">Array of S3 keys for images/video</div></div>
<div class="col-row"><div class="c-n">reply_to_id</div><div class="c-t">BIGINT</div><div class="c-d">NULL if original tweet; FK to parent tweet</div></div>
<div class="col-row"><div class="c-n">retweet_of</div><div class="c-t">BIGINT</div><div class="c-d">NULL if original; FK to retweeted tweet</div></div>
<div class="col-row"><div class="c-n">like_count</div><div class="c-t">BIGINT</div><div class="c-d">Approximate — updated async via counter service</div></div>
<div style="margin-top:10px;font-family:'Fira Code',monospace;font-size:9px;color:var(--cyan)">INDEX (user_id, tweet_id DESC) — user timeline query</div>
</div>
  </div>
  <div class="schema-box" style="margin-top:8px">
<div class="sb-hdr"><span>TABLE: follows — social graph service</span><span style="color:var(--green)">MySQL / Graph DB</span></div>
<div class="sb-body">
<div class="col-row"><div class="c-n">follower_id</div><div class="c-t">BIGINT</div><div class="c-d">Who is following (part of composite PK)</div></div>
<div class="col-row"><div class="c-n">followee_id</div><div class="c-t">BIGINT</div><div class="c-d">Who is being followed</div></div>
<div class="col-row"><div class="c-n">created_at</div><div class="c-t">TIMESTAMP</div><div class="c-d">When the follow happened</div></div>
<div style="margin-top:10px;font-family:'Fira Code',monospace;font-size:9px;color:var(--cyan)">PRIMARY KEY (follower_id, followee_id)<br>INDEX (followee_id) — "who follows @ladygaga?" for fanout</div>
</div>
  </div>
  <div class="cb" style="margin-top:10px"><div class="cb-top">Redis timeline cache design<span class="cb-l">REDIS</span></div>


```python
// Key pattern: timeline:{userId}
// Type: Sorted Set — score = tweet timestamp (epoch ms)
// Members: tweet_id strings

redis.ZADD("timeline:123", 1700000500000, "tweet_abc")
redis.ZADD("timeline:123", 1700000400000, "tweet_def")

// Read top 200:
tweetIds = redis.ZREVRANGE("timeline:123", 0, 199)   // O(log N + 200)

// Batch hydrate (pipeline, single roundtrip):
tweets = redis.PIPELINE { tweetIds.map(id => HGETALL("tweet:"+id)) }

// Trim timeline to 1000 entries (memory bound):
redis.ZREMRANGEBYRANK("timeline:123", 0, -1001)  // keep newest 1000

// Memory: 300M users × 1000 IDs × 8 bytes = 2.4 TB → Redis cluster
```


</div>
<!-- ARCHITECTURE -->
<div class="view" id="view-arch">
  <div class="sh">Full Architecture</div>
  <div class="sr">Six services — each with a distinct responsibility</div>
  <div class="arch-diagram">
<div class="arch-title">// TWITTER SYSTEM ARCHITECTURE</div>
<div class="arch-layer">
<div class="al-label">CLIENT</div>
<div class="al-nodes">
<div class="arch-node" style="border-color:var(--cyan);color:var(--cyan)">Mobile / Web</div>
<div class="tl-arr" style="padding-top:10px">──→</div>
<div class="arch-node" style="border-color:var(--muted);color:var(--muted)">CDN Edge<br><div class="tl-lbl">static assets</div></div>
<div class="tl-arr" style="padding-top:10px">──→</div>
<div class="arch-node" style="border-color:var(--muted);color:var(--muted)">Load Balancer<br><div class="tl-lbl">L7 / HTTPS</div></div>
</div>
</div>
<div class="arch-layer">
<div class="al-label">SERVICES</div>
<div class="al-nodes">
<div class="arch-node" style="border-color:var(--pur);color:var(--pur)">Tweet Service<br><div class="tl-lbl">post / user timeline</div></div>
<div class="arch-node" style="border-color:var(--cyan);color:var(--cyan)">Timeline Service<br><div class="tl-lbl">home feed assembly</div></div>
<div class="arch-node" style="border-color:var(--green);color:var(--green)">Fanout Service<br><div class="tl-lbl">push to Redis timelines</div></div>
<div class="arch-node" style="border-color:var(--amber);color:var(--amber)">Social Graph Svc<br><div class="tl-lbl">follow / unfollow</div></div>
<div class="arch-node" style="border-color:var(--red);color:var(--red)">Search Service<br><div class="tl-lbl">Elasticsearch</div></div>
<div class="arch-node" style="border-color:var(--muted);color:var(--muted)">Media Service<br><div class="tl-lbl">upload / transcode</div></div>
</div>
</div>
<div class="arch-layer">
<div class="al-label">ASYNC</div>
<div class="al-nodes">
<div class="arch-node" style="border-color:var(--pur);color:var(--pur)">Kafka<br><div class="tl-lbl">tweet-created<br>tweet-liked<br>user-followed</div></div>
<div class="tl-arr" style="padding-top:10px">──→</div>
<div class="arch-node" style="border-color:var(--green);color:var(--green)">Fanout Workers<br><div class="tl-lbl">consume tweet-created<br>push to timelines</div></div>
<div class="tl-arr" style="padding-top:10px">+</div>
<div class="arch-node" style="border-color:var(--amber);color:var(--amber)">Counter Workers<br><div class="tl-lbl">batch update<br>like/retweet counts</div></div>
<div class="tl-arr" style="padding-top:10px">+</div>
<div class="arch-node" style="border-color:var(--red);color:var(--red)">Search Indexer<br><div class="tl-lbl">Elasticsearch<br>write pipeline</div></div>
</div>
</div>
<div class="arch-layer">
<div class="al-label">STORAGE</div>
<div class="al-nodes">
<div class="arch-node" style="border-color:var(--cyan);color:var(--cyan)">Redis Cluster<br><div class="tl-lbl">timelines, tweet cache<br>counts (approximate)</div></div>
<div class="arch-node" style="border-color:var(--pur);color:var(--pur)">MySQL (sharded)<br><div class="tl-lbl">tweets, users<br>sharded by user_id</div></div>
<div class="arch-node" style="border-color:var(--green);color:var(--green)">Graph DB<br><div class="tl-lbl">follows edges<br>300M×400 = 120B</div></div>
<div class="arch-node" style="border-color:var(--red);color:var(--red)">Elasticsearch<br><div class="tl-lbl">full-text search<br>hashtag index</div></div>
<div class="arch-node" style="border-color:var(--muted);color:var(--muted)">S3 + CDN<br><div class="tl-lbl">photos, videos<br>HLS transcoded</div></div>
</div>
</div>
  </div>
</div>
<!-- COUNTS -->
<div class="view" id="view-counts">
  <div class="sh">Likes, Retweets & Follower Counts</div>
  <div class="sr">Async counter aggregation — why you can't do synchronous increments at scale</div>
  <div class="cb"><div class="cb-top">Why synchronous UPDATE like_count fails<span class="cb-l">MATH</span></div>


```sql
// A viral tweet receives 5M likes in 10 minutes
// = 8,333 likes/sec at peak

// Naive: UPDATE tweets SET like_count = like_count + 1 WHERE tweet_id = ?
// Problem: 8,333 concurrent UPDATE ops on SAME row = row-level lock contention
// MySQL handles ~10K single-row updates/sec → this saturates the primary
// And we have thousands of tweets being liked simultaneously

// Solution: decouple write from increment
```


  <div class="count-flow">
<div class="cf-step" style="border-color:var(--cyan);color:var(--cyan)">User likes<br>tweet</div>
<div class="cf-arr">→</div>
<div class="cf-step" style="border-color:var(--green);color:var(--green)">INSERT likes<br>(user,tweet,ts)<br><div style="font-size:8px;margin-top:2px">immediate — dedup check</div></div>
<div class="cf-arr">+</div>
<div class="cf-step" style="border-color:var(--pur);color:var(--pur)">INCR Redis<br>like:{tweetId}<br><div style="font-size:8px;margin-top:2px">instant display</div></div>
<div class="cf-arr">+</div>
<div class="cf-step" style="border-color:var(--amber);color:var(--amber)">Kafka publish<br>"tweet-liked"<br><div style="font-size:8px;margin-top:2px">async</div></div>
<div class="cf-arr">→</div>
<div class="cf-step" style="border-color:var(--muted);color:var(--muted)">Counter Worker<br>batch UPDATE<br>every 30 sec</div>
  </div>
  <div class="al gn"><em>Key insight:</em> Users are shown the Redis count (approximate, updated in real-time via INCR). The DB count lags by up to 30 seconds. This is acceptable — Twitter shows "1.2M" not "1,234,567". The <em>likes table</em> is the source of truth for "did I like this?", not the count column.</div>
</div>
<!-- MEDIA & SEARCH -->
<div class="view" id="view-media">
  <div class="sh">Media Storage</div>
  <div class="sr">S3 + CDN + transcoding pipeline — serving petabytes of images and video</div>
  <div class="cb"><div class="cb-top">Image and video pipeline<span class="cb-l">FLOW</span></div>


```python
// IMAGE UPLOAD:
Client → CDN upload endpoint → S3 (raw bucket)
Tweet stores: media_ids: ["s3://tweets-raw/2024/01/img_abc.jpg"]
CDN serves: https://pbs.twimg.com/media/img_abc.jpg
// CDN cache hit rate: 99%+ for viral content
// Without CDN: 100M impressions × 500KB = 50TB bandwidth from S3 → $$$

// VIDEO UPLOAD (async transcoding):
Client → S3 raw → Lambda trigger → Transcoding worker
  Transcodes to HLS (HTTP Live Streaming) at multiple bitrates:
    240p, 480p, 720p, 1080p
  Output → S3 transcoded bucket → CDN
// HLS: browser fetches small segments (2-10sec), adapts bitrate to bandwidth
```



  <div class="sh" style="margin-top:22px">Trending Topics</div>
  <div class="cb"><div class="cb-top">Sliding window hashtag counting<span class="cb-l">STREAM PROCESSING</span></div>


```python
// Kafka stream: every tweet → extract hashtags
Tweet: "Just watched #Oppenheimer, amazing! #movies"
Extract: ["#Oppenheimer", "#movies"]

// Flink/Storm: count per hashtag in 1-hour sliding window
// Min-heap: maintain top-30 hashtags globally + per-region

// Store in Redis sorted set:
redis.ZINCRBY("trending:global", 1, "#Oppenheimer")
redis.ZINCRBY("trending:US", 1, "#Oppenheimer")

// Read top 10:
redis.ZREVRANGE("trending:global", 0, 9, WITHSCORES)

// Refresh: recalculate every 5 minutes
// Geographic trending: separate sorted set per region
```


</div>
<!-- TASKS -->
<div class="view" id="view-tasks">
  <div class="task-list">
<div class="task-card">
<div class="task-hd" onclick="mb6_tt(this)"><div class="t-num">01</div><div class="t-lbl">Fan-Out Cost Analysis</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
<div class="task-bd">
<p>Calculate the write cost for each scenario:</p>
<ol>
<li>@ladygaga (100M followers) tweets once. Pure fan-out on write: how many Redis writes? At what rate (assuming 10s to fanout)?</li>
<li>100K users each follow @ladygaga. Timeline load for each. Pure fan-out on read: how many extra tweet fetches? Total QPS added?</li>
<li>Hybrid model (10K follower threshold): what % of Twitter accounts qualify as "celebrity"? What % of total write cost does this save?</li>
<li>Redis storage: 300M active users × 1000 timeline entries × 8 bytes. Compare to fan-out-on-read (no timeline storage).</li>
</ol>
</div>
</div>
<div class="task-card">
<div class="task-hd" onclick="mb6_tt(this)"><div class="t-num">02</div><div class="t-lbl">Extended Data Model</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
<div class="task-bd">
<p>Extend the schema and describe the fanout/read changes for:</p>
<ol>
<li><strong>Twitter Lists</strong> — user creates a curated list of accounts; list has its own timeline</li>
<li><strong>Tweet threads</strong> — reply chain, show conversation in order</li>
<li><strong>Quote tweets</strong> — retweet with added comment (references original)</li>
<li><strong>Pinned tweet</strong> — always shown first on user profile page</li>
</ol>
</div>
</div>
<div class="task-card">
<div class="task-hd" onclick="mb6_tt(this)"><div class="t-num">03</div><div class="t-lbl">Failure Scenario Design</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
<div class="task-bd">
<ol>
<li>Fanout service crashes mid-fanout: 10M of 100M followers got the tweet, then crash. How do you ensure eventual consistency?</li>
<li>Redis timeline cache completely wiped (OOM, cluster failure). 300M users with empty timelines hit the timeline service simultaneously.</li>
<li>Social graph DB is down. Fanout service can't resolve followers. What happens to new tweets posted during the outage?</li>
<li>Elasticsearch is unavailable. Users submit search queries. Design graceful degradation.</li>
</ol>
</div>
</div>
<div class="task-card" style="border-top:2px solid var(--cyan)">
<div class="task-hd" onclick="mb6_tt(this)"><div class="t-num" style="color:var(--cyan)">★</div><div class="t-lbl">Full 45-Minute Design Simulation</div><div class="t-meta">45 min timed</div><div class="t-arr">›</div></div>
<div class="task-bd">
<p>Set a timer. On paper or whiteboard, design Twitter's home timeline from scratch using the 7-step framework. Must include:</p>
<ul>
<li>Requirements + NFRs with all key numbers</li>
<li>Capacity estimation (tweets/day, QPS, storage)</li>
<li>Full architecture diagram (all 6 services + storage layers)</li>
<li>Fan-out model decision with hybrid threshold justification</li>
<li>DB schema (tweets + follows + Redis timeline cache design)</li>
<li>At least 2 edge cases (celebrity problem + one other)</li>
<li>Scale evolution: what changes if Twitter 10× in size?</li>
</ul>
<p style="margin-top:8px">After completing, review against this module's content. What did you miss? What would you add?</p>
</div>
</div>
  </div>
</div>
<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 14 completed</span><span style="font-family:'Fira Code',monospace">MODULE B6 · TWITTER FEED</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Twitter scale: 300M users, 500M tweets/day, 320K timeline reads/sec</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Fan-out on write: how it works, write amplification problem, celebrity failure mode</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Fan-out on read: how it works, 160M QPS impossibility, merge latency</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Hybrid model: threshold (10K followers), celebrity inject at read time, merge logic</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can draw full architecture: 6 services + Kafka + Redis + MySQL + Graph DB + S3</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Redis timeline cache: sorted set, score = timestamp, ZREVRANGE, trim to 1000</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">DB schema: tweets (sharded by user_id) + follows (indexed on followee_id)</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Like/retweet counts: async Kafka → counter worker → Redis INCR + periodic DB flush</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Media: S3 + CDN + HLS transcoding pipeline for video</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Trending: sliding window, Flink, Redis sorted set, per-region</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Search: Elasticsearch, async indexing via Kafka, hydrate tweet IDs from cache</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 1: fan-out cost analysis with actual numbers</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 3: failure scenarios — fanout crash, Redis wipe, graph DB down</div></div>
<div class="chk" onclick="mb6_tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 4: 45-min timed full design simulation completed</div></div>
  </div>
  <div style="margin-top:28px;background:var(--panel);border:1px solid var(--bord2);padding:22px;border-top:2px solid var(--cyan)">
<div style="font-family:'Fira Code',monospace;font-size:8px;color:var(--muted);letter-spacing:2px;margin-bottom:8px">// NEXT MODULE</div>
<div style="font-family:'Space Mono',monospace;font-size:26px;font-weight:700;color:var(--white);margin-bottom:6px">B7 — Design WhatsApp</div>
<div style="font-family:'Fira Code',monospace;font-size:9px;color:var(--muted);line-height:2">
      Real-time messaging · WebSocket connection management<br>
      Message delivery guarantees (sent / delivered / read)<br>
      Group chats · Media sharing · End-to-end encryption overview<br>
      Presence (online/offline) · Message ordering · Offline queue
</div>
  </div>
</div>
</div>
</div>
<!-- Bottom Navigation -->
<div class="mb6-bottom-nav">
  <a href="/learning/system-design/hld/module-b5-url-shortener/" class="mb6-nav-footer-btn">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
    B5: URL Shortener
  </a>
  <a href="/learning/system-design/hld/module-b6-notes/" class="mb6-nav-footer-btn">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    READ STUDY NOTES
  </a>
  <a href="/learning/system-design/system-design-roadmap/" class="mb6-nav-footer-btn">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="17 1 21 5 17 9"></polyline><path d="M3 11V9a4 4 0 0 1 4-4h14"></path><polyline points="7 23 3 19 7 15"></polyline><path d="M21 13v2a4 4 0 0 1-4 4H3"></path></svg>
    ROADMAP
  </a>
  <a href="/learning/system-design/hld/module-b7-whatsapp/" class="mb6-nav-footer-btn">
<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
    B7: WhatsApp
  </a>
</div>
<script src="/assets/js/sd-module-b6.js"></script>
