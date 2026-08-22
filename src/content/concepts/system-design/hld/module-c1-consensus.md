---
title: "Module C1: Consensus Algorithms — Raft & Paxos"
description: "SYSTEM DESIGN MASTERY · TRACK C · MODULE C1 · WEEK 25 RAFT · PAXOS · ETCD · COCKROACHDB · KAFKA KRAFT Advanced Distributed Systems · Consensus Theory · Production Systems…"
domain: system-design
track: system-design-hld
order: 202
url: /learning/system-design/hld/module-c1-consensus/
---

<link rel="stylesheet" href="/assets/css/sd-module-c1.css">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;600&family=DM+Serif+Display&display=swap" rel="stylesheet">

<header>
  <div class="hdr-line"></div>
  <div class="hdr-top">
    <span>SYSTEM DESIGN MASTERY · TRACK C · MODULE C1 · WEEK 25</span>
    <span>RAFT · PAXOS · ETCD · COCKROACHDB · KAFKA KRAFT</span>
  </div>
  <div class="hdr-main">
    <div>
      <div class="hdr-kicker">Advanced Distributed Systems · Consensus Theory · Production Systems</div>
      <h1>Consensus<br><span class="acc">Raft</span><br>& Paxos</h1>
      <div class="hdr-sub">FLP IMPOSSIBILITY · PAXOS PHASES · RAFT LEADER ELECTION<br>LOG REPLICATION · QUORUM MATH · ETCD · COCKROACHDB</div>
    </div>
    <div class="hdr-stats">
      <div class="hs"><div class="hs-v">⌊N/2⌋+1</div><div class="hs-l">QUORUM</div></div>
      <div class="hs"><div class="hs-v">3</div><div class="hs-l">NODE STATES</div></div>
      <div class="hs"><div class="hs-v">4</div><div class="hs-l">PAXOS PHASES</div></div>
      <div class="hs"><div class="hs-v">C1</div><div class="hs-l">MODULE</div></div>
    </div>
  </div>
  <div class="tag-row">
    <div class="tg" style="color:var(--bri)">FLP Impossibility</div>
    <div class="tg" style="color:var(--cya)">Paxos</div>
    <div class="tg" style="color:var(--grn)">Raft ★</div>
    <div class="tg" style="color:var(--yel)">Leader Election</div>
    <div class="tg" style="color:var(--pur)">Log Replication</div>
    <div class="tg" style="color:var(--ora)">Quorum Math</div>
    <div class="tg" style="color:var(--bri)">etcd · CockroachDB · KRaft</div>
  </div>
</header>

<nav class="nav">
  <div class="nt active" onclick="show('problem',this)">Consensus Problem</div>
  <div class="nt" onclick="show('paxos',this)">Paxos</div>
  <div class="nt" onclick="show('raft',this)">Raft Overview</div>
  <div class="nt" onclick="show('election',this)">Leader Election</div>
  <div class="nt" onclick="show('replication',this)">Log Replication</div>
  <div class="nt" onclick="show('quorum',this)">Quorum Math</div>
  <div class="nt" onclick="show('realworld',this)">Real World</div>
  <div class="nt" onclick="show('interview',this)">Interview Q&A</div>
  <div class="nt" onclick="show('tasks',this)">Tasks</div>
  <div class="nt" onclick="show('checklist',this)">Checklist</div>
</nav>

<div class="content">

<!-- PROBLEM -->
<div class="view active" id="view-problem">
  <div class="sh">The Consensus Problem</div>
  <div class="sr">Getting N nodes to agree on a value despite failures</div>
  <div class="cb"><div class="cb-top">What consensus must guarantee<span class="cb-l">DEFINITION</span></div>
<pre class="c"><span class="cm">// Consensus: N nodes must agree on ONE value, even when nodes crash.</span>

<span class="cm">// Three properties required:</span>
<span class="kw">Agreement</span>:   All non-faulty nodes decide on the same value.
<span class="kw">Validity</span>:    The decided value was proposed by some node (not fabricated).
<span class="kw">Termination</span>: All non-faulty nodes eventually decide (make progress).

<span class="cm">// Safety vs Liveness:</span>
<span class="hl">Safety</span>:   "Nothing bad ever happens."  (Agreement + Validity)
           Never return incorrect/conflicting results.
<span class="hl">Liveness</span>: "Something good eventually happens." (Termination)
           System eventually makes progress.

<span class="cm">// FLP Impossibility (1985): In an ASYNC network with ≥1 possible crash,</span>
<span class="cm">// no algorithm can guarantee BOTH safety AND liveness.</span>
<span class="cm">//</span>
<span class="cm">// Raft and Paxos choose SAFETY over liveness:</span>
<span class="cm">// They may stall (no progress) during certain failure scenarios,</span>
<span class="cm">// but they will NEVER return incorrect results.</span>
<span class="cm">// This is the correct choice for databases and coordination services.</span></pre>
  </div>
  <div class="al blu"><em>Why FLP matters in interviews:</em> When asked "can your system guarantee both consistency and availability?", the correct answer is no — CAP theorem. FLP is the theoretical underpinning. Raft/Paxos are CP systems: they choose consistency (safety) over availability (liveness) during partitions.</div>
</div>

<!-- PAXOS -->
<div class="view" id="view-paxos">
  <div class="sh">Paxos — The Original</div>
  <div class="sr">Four phases to agree on one value — elegant but notoriously hard to implement</div>
  <div class="paxos-phases">
    <div class="pp">
      <div class="pp-phase" style="background:rgba(64,128,255,.1);color:var(--bri)">PHASE 1</div>
      <div class="pp-label"><div class="pp-name">PREPARE</div><div class="pp-sub">PROPOSER → ACCEPTORS</div></div>
      <div class="pp-body">Proposer chooses unique proposal number N (higher than any previously seen).<br>Sends <span style="color:var(--bri)">PREPARE(N)</span> to majority of Acceptors.<br><br>Goal: "I want to propose a value. Will you listen to me (number N) and ignore lower numbers?"</div>
    </div>
    <div class="pp">
      <div class="pp-phase" style="background:rgba(64,128,255,.1);color:var(--bri)">PHASE 1</div>
      <div class="pp-label"><div class="pp-name">PROMISE</div><div class="pp-sub">ACCEPTORS → PROPOSER</div></div>
      <div class="pp-body">Each Acceptor: if N &gt; previously promised number:<br>→ Responds <span style="color:var(--grn)">PROMISE(N, accepted_value, accepted_number)</span><br>→ Promises never to accept proposals &lt; N<br>→ Returns any value it already accepted (crucial for safety!)<br><br>If N ≤ promised: ignores or sends NACK.</div>
    </div>
    <div class="pp">
      <div class="pp-phase" style="background:rgba(32,192,96,.08);color:var(--grn)">PHASE 2</div>
      <div class="pp-label"><div class="pp-name">ACCEPT</div><div class="pp-sub">PROPOSER → ACCEPTORS</div></div>
      <div class="pp-body">Proposer receives PROMISE from majority:<br>→ If any PROMISE included an already-accepted value: <span style="color:var(--red)">MUST use that value</span> (not its own)<br>→ Else: use its own proposed value<br>Sends <span style="color:var(--grn)">ACCEPT(N, value)</span> to majority.<br><br><span style="color:var(--yel)">Safety invariant:</span> using a previously-accepted value preserves agreement already reached.</div>
    </div>
    <div class="pp">
      <div class="pp-phase" style="background:rgba(32,192,96,.08);color:var(--grn)">PHASE 2</div>
      <div class="pp-label"><div class="pp-name">ACCEPTED</div><div class="pp-sub">ACCEPTORS → LEARNERS</div></div>
      <div class="pp-body">Each Acceptor: if N ≥ promised number:<br>→ Accepts value, sends <span style="color:var(--grn)">ACCEPTED(N, value)</span> to Learners<br><br>Learner receives ACCEPTED from majority → <span style="color:var(--grn)">consensus reached!</span><br><br>Value is chosen. All future proposals will discover and preserve this value.</div>
    </div>
  </div>
  <div class="al yel"><em>Why the "must use already-accepted value" rule?</em> Imagine two proposers A and B racing. A gets value "X" accepted by nodes 1 and 2. B comes along and sees node 2's accepted value "X" in its PROMISE response. B must continue with "X" — not its own value. This prevents two different values from being chosen by different majorities. Safety preserved.</div>
</div>

<!-- RAFT OVERVIEW -->
<div class="view" id="view-raft">
  <div class="sh">Raft — Designed for Understandability</div>
  <div class="sr">Three sub-problems, one strong leader, no concurrent proposals</div>
  <div class="state-machine">
    <div class="state-node" style="border-color:var(--muted)">
      <div class="sn-name">Follower</div>
      <div class="sn-desc">Passive.<br>Responds to<br>Leader/Candidate</div>
    </div>
    <div class="state-arrow">
      <div class="sa-label">Election timeout (no heartbeat)</div>
      <div class="sa-line">→</div>
    </div>
    <div class="state-node" style="border-color:var(--yel)">
      <div class="sn-name" style="color:var(--yel)">Candidate</div>
      <div class="sn-desc">Running for<br>leader.<br>Sends votes.</div>
    </div>
    <div class="state-arrow">
      <div class="sa-label">Majority votes received</div>
      <div class="sa-line">→</div>
    </div>
    <div class="state-node" style="border-color:var(--grn)">
      <div class="sn-name" style="color:var(--grn)">Leader</div>
      <div class="sn-desc">All writes.<br>Heartbeats.<br>Log sync.</div>
    </div>
  </div>
  <div style="display:flex;gap:6px;margin:0 0 12px;flex-wrap:wrap">
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--muted);padding:12px;flex:1;min-width:200px">
      <div style="font-family:'DM Serif Display',serif;font-size:14px;color:var(--white);margin-bottom:6px">Follower</div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);line-height:1.8">Passive. Responds to AppendEntries and RequestVote RPCs. If no heartbeat within timeout (150–300ms, random): becomes Candidate.</div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--yel);padding:12px;flex:1;min-width:200px">
      <div style="font-family:'DM Serif Display',serif;font-size:14px;color:var(--white);margin-bottom:6px">Candidate</div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);line-height:1.8">Increments term. Votes for self. Sends RequestVote to all. Gets majority → Leader. Hears from valid Leader → Follower. Timeout → new election.</div>
    </div>
    <div style="background:var(--panel);border:1px solid var(--bord2);border-top:2px solid var(--grn);padding:12px;flex:1;min-width:200px">
      <div style="font-family:'DM Serif Display',serif;font-size:14px;color:var(--white);margin-bottom:6px">Leader</div>
      <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);line-height:1.8">Handles ALL client writes. Sends periodic heartbeats (AppendEntries with no entries). Replicates log. Steps down if higher term discovered.</div>
    </div>
  </div>
  <div class="al blu"><em>Terms — Raft's logical clock:</em> Every RPC includes the sender's term. If a node receives an RPC with a higher term, it immediately updates its term and reverts to Follower. This means a stale leader that reconnects after a network partition instantly steps down — it will always see a higher term from the new leader. No split-brain from reconnected old leaders.</div>
</div>

<!-- ELECTION -->
<div class="view" id="view-election">
  <div class="sh">Leader Election</div>
  <div class="sr">Randomized timeouts prevent simultaneous elections — log completeness prevents stale winners</div>
  <div class="cb"><div class="cb-top">RequestVote RPC — the two critical checks<span class="cb-l">ELECTION PROTOCOL</span></div>
<pre class="c"><span class="cm">// Follower starts election when election timeout expires (150–300ms, RANDOM per node)</span>
<span class="cm">// Randomization prevents all nodes timing out simultaneously</span>

<span class="kw">function</span> <span class="fn">startElection</span>(node) {
  node.currentTerm += <span class="bl">1</span>           <span class="cm">// increment term</span>
  node.state = <span class="str">'CANDIDATE'</span>
  node.votedFor = node.id           <span class="cm">// vote for self</span>
  votes = <span class="bl">1</span>

  <span class="kw">for each</span> peer <span class="kw">in</span> cluster:
    response = peer.<span class="fn">requestVote</span>({
      term:         node.currentTerm,
      candidateId:  node.id,
      lastLogIndex: node.log.<span class="fn">lastIndex</span>(),
      lastLogTerm:  node.log.<span class="fn">lastTerm</span>()
    })

    <span class="kw">if</span> (response.voteGranted) votes++
    <span class="kw">if</span> (votes > cluster.size / <span class="bl">2</span>) {
      node.state = <span class="str">'LEADER'</span>
      node.<span class="fn">sendHeartbeats</span>()  <span class="cm">// immediately prevent new elections</span>
      <span class="kw">return</span>
    }
}

<span class="cm">// Voter grants vote ONLY IF both conditions hold:</span>
<span class="kw">function</span> <span class="fn">handleRequestVote</span>(req) {
  <span class="cm">// Condition 1: haven't voted this term yet</span>
  <span class="kw">if</span> (votedFor != null && votedFor != req.candidateId) <span class="kw">return</span> {voteGranted: <span class="er">false</span>}

  <span class="cm">// Condition 2: candidate's log is AT LEAST as up-to-date as ours</span>
  <span class="cm">// (log completeness check — prevents stale node from winning)</span>
  candidateUpToDate = req.lastLogTerm > myLastLogTerm ||
    (req.lastLogTerm == myLastLogTerm && req.lastLogIndex >= myLastLogIndex)

  <span class="kw">if</span> (!candidateUpToDate) <span class="kw">return</span> {voteGranted: <span class="er">false</span>}

  votedFor = req.candidateId
  <span class="kw">return</span> {voteGranted: <span class="ok">true</span>}
}</pre>
  </div>
  <div class="al grn"><em>Log completeness guarantee:</em> A Candidate can only win if its log is as up-to-date as a majority of nodes. Since committed entries are on a majority of nodes, the winner is guaranteed to have all committed entries. This is why committed entries are never lost — any future leader will have them.</div>
</div>

<!-- LOG REPLICATION -->
<div class="view" id="view-replication">
  <div class="sh">Log Replication & Healing</div>
  <div class="sr">AppendEntries — the workhorse RPC that replicates and heals divergent logs</div>
  <div class="log-diagram">
    <div class="ld-label">// LOG STATE — 5-node cluster after some entries (quorum = 3)</div>
    <div class="ld-row">
      <div class="ld-name" style="color:var(--grn)">Leader L</div>
      <div class="ld-entry le-committed">t1:a=1</div>
      <div class="ld-entry le-committed">t1:b=2</div>
      <div class="ld-entry le-committed">t2:c=3</div>
      <div class="ld-entry le-uncommitted">t2:d=4</div>
      <div class="ld-status" style="color:var(--grn)">← idx 1–3 committed (majority); idx 4 uncommitted</div>
    </div>
    <div class="ld-row">
      <div class="ld-name">F1</div>
      <div class="ld-entry le-committed">t1:a=1</div>
      <div class="ld-entry le-committed">t1:b=2</div>
      <div class="ld-entry le-committed">t2:c=3</div>
      <div class="ld-entry le-uncommitted">t2:d=4</div>
      <div class="ld-status" style="color:var(--muted)">up to date</div>
    </div>
    <div class="ld-row">
      <div class="ld-name" style="color:var(--yel)">F2</div>
      <div class="ld-entry le-committed">t1:a=1</div>
      <div class="ld-entry le-committed">t1:b=2</div>
      <div class="ld-entry le-committed">t2:c=3</div>
      <div class="ld-entry le-missing">?</div>
      <div class="ld-status" style="color:var(--yel)">missing idx 4 → L sends it</div>
    </div>
    <div class="ld-row">
      <div class="ld-name" style="color:var(--yel)">F3</div>
      <div class="ld-entry le-committed">t1:a=1</div>
      <div class="ld-entry le-committed">t1:b=2</div>
      <div class="ld-entry le-missing">?</div>
      <div class="ld-entry le-missing">?</div>
      <div class="ld-status" style="color:var(--yel)">missing idx 3,4 → L sends both</div>
    </div>
    <div class="ld-row">
      <div class="ld-name" style="color:var(--red)">F4</div>
      <div class="ld-entry le-committed">t1:a=1</div>
      <div class="ld-entry le-committed">t1:b=2</div>
      <div class="ld-entry le-conflict">t1:x=9</div>
      <div class="ld-entry le-missing">?</div>
      <div class="ld-status" style="color:var(--red)">conflict at idx 3! L overwrites with t2:c=3</div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Log healing — how Leader brings divergent followers up to date<span class="cb-l">HEALING</span></div>
<pre class="c"><span class="cm">// Leader tracks nextIndex[i] for each Follower (initially = lastLogIndex + 1)</span>
<span class="cm">// On AppendEntries rejection (consistency check failed):</span>
<span class="cm">//   Decrement nextIndex[i] and retry with older entries</span>
<span class="cm">//   Eventually: follower finds a matching point, then sync forward</span>

<span class="cm">// AppendEntries includes a consistency check:</span>
AppendEntries({
  term:         currentTerm,
  leaderId:     myId,
  prevLogIndex: nextIndex[i] - <span class="bl">1</span>,   <span class="cm">// index of entry BEFORE new ones</span>
  prevLogTerm:  log[prevLogIndex].term, <span class="cm">// term of that entry</span>
  entries:      log[nextIndex[i]...],   <span class="cm">// entries to replicate</span>
  leaderCommit: commitIndex             <span class="cm">// highest committed index</span>
})

<span class="cm">// Follower F4 (conflict at idx 3):</span>
<span class="cm">// L sends AppendEntries with prevLogIndex=2, prevLogTerm=1</span>
<span class="cm">// F4 checks: log[2].term == 1? YES → accepts</span>
<span class="cm">// F4 replaces log[3] (t1:x=9) with (t2:c=3) — the conflict is overwritten</span>
<span class="cm">// F4 appends entries[4] = (t2:d=4)</span>

<span class="cm">// Key: committed entries are NEVER overwritten</span>
<span class="cm">// (idx 1,2 were committed — majority had them — F4's idx 3 conflict was NOT committed)</span></pre>
  </div>
</div>

<!-- QUORUM -->
<div class="view" id="view-quorum">
  <div class="sh">Quorum Math & Failure Tolerance</div>
  <div class="sr">Quorum = ⌊N/2⌋ + 1 — always use odd-sized clusters</div>
  <div class="quorum-grid">
    <div class="qc" style="border-top-color:var(--muted)">
      <div class="qc-n">3</div>
      <div class="qc-sub">nodes</div>
      <div class="qc-q" style="color:var(--bri)">Q = 2</div>
      <div class="qc-f" style="color:var(--grn)">F = 1</div>
      <div class="qc-sub" style="margin-top:4px">dev / small</div>
    </div>
    <div class="qc" style="border-top-color:var(--bri)">
      <div class="qc-n" style="color:var(--bri)">5</div>
      <div class="qc-sub">nodes</div>
      <div class="qc-q" style="color:var(--bri)">Q = 3</div>
      <div class="qc-f" style="color:var(--grn)">F = 2</div>
      <div class="qc-sub" style="margin-top:4px;color:var(--bri)">★ production</div>
    </div>
    <div class="qc" style="border-top-color:var(--muted)">
      <div class="qc-n">7</div>
      <div class="qc-sub">nodes</div>
      <div class="qc-q" style="color:var(--bri)">Q = 4</div>
      <div class="qc-f" style="color:var(--grn)">F = 3</div>
      <div class="qc-sub" style="margin-top:4px">high durability</div>
    </div>
    <div class="qc" style="border-top-color:var(--red)">
      <div class="qc-n">4</div>
      <div class="qc-sub">nodes</div>
      <div class="qc-q" style="color:var(--yel)">Q = 3</div>
      <div class="qc-f" style="color:var(--red)">F = 1</div>
      <div class="qc-sub" style="margin-top:4px;color:var(--red)">✗ avoid: same F=1 as N=3, more overhead</div>
    </div>
    <div class="qc" style="border-top-color:var(--red)">
      <div class="qc-n">6</div>
      <div class="qc-sub">nodes</div>
      <div class="qc-q" style="color:var(--yel)">Q = 4</div>
      <div class="qc-f" style="color:var(--red)">F = 2</div>
      <div class="qc-sub" style="margin-top:4px;color:var(--red)">✗ avoid: same F=2 as N=5, more overhead</div>
    </div>
  </div>
  <div class="cb"><div class="cb-top">Split-brain prevention via quorum<span class="cb-l">PARTITION SAFETY</span></div>
<pre class="c"><span class="cm">// 5-node cluster partitioned into two groups:</span>

Partition A: [Node 1, Node 2, Node 3]  ← has quorum (3 of 5) ✓
Partition B: [Node 4, Node 5]           ← no quorum (2 of 5) ✗

<span class="cm">// Partition A: can elect leader, process writes → active</span>
<span class="cm">// Partition B: cannot reach quorum → cannot elect leader → rejects all writes</span>

<span class="cm">// Two active leaders simultaneously is IMPOSSIBLE:</span>
<span class="cm">// They would each need a majority of N nodes.</span>
<span class="cm">// Two separate majorities of N nodes requires 2 × (⌊N/2⌋ + 1) > N nodes.</span>
<span class="cm">// For N=5: 2 × 3 = 6 > 5. Impossible with only 5 nodes.</span>
<span class="cm">// ∴ At most ONE partition can ever have quorum. No split-brain. ∎</span></pre>
  </div>
</div>

<!-- REAL WORLD -->
<div class="view" id="view-realworld">
  <div class="sh">Real-World Systems</div>
  <div class="sr">Where Raft and Paxos run in production — and how</div>
  <div class="rw-grid">
    <div class="rw" style="border-left-color:var(--bri)">
      <div class="rw-name">etcd</div>
      <div class="rw-sub">KUBERNETES CONTROL PLANE · RAFT</div>
      <div class="rw-body">Every Kubernetes object (Pod, Service, ConfigMap) lives in etcd. kubectl apply → API Server → etcd Raft leader → committed to majority → response.</div>
      <div class="rw-detail">3 nodes: F=1 · 5 nodes: F=2 ★ production<br>Linearizable reads: go through leader (fresh)<br>Serializable reads: any node (may be stale)<br>Rolling upgrade: 5-node cluster → 4 available while 1 restarts → quorum maintained</div>
    </div>
    <div class="rw" style="border-left-color:var(--grn)">
      <div class="rw-name">CockroachDB</div>
      <div class="rw-sub">DISTRIBUTED SQL · RAFT PER RANGE</div>
      <div class="rw-body">Table data split into 64MB ranges. Each range has 3 replicas forming its own Raft group. A node is simultaneously Leader for some ranges, Follower for others.</div>
      <div class="rw-detail">Thousands of Raft groups on a 3-node cluster<br>Leaseholder (Raft leader) handles reads for range<br>Range splits when &gt;64MB → two Raft groups<br>Writes: Raft committed → SQL response</div>
    </div>
    <div class="rw" style="border-left-color:var(--yel)">
      <div class="rw-name">Kafka KRaft</div>
      <div class="rw-sub">REPLACING ZOOKEEPER · KAFKA 3.x+</div>
      <div class="rw-body">Kafka's own Raft implementation for broker metadata. Controller quorum (3–5 nodes) uses KRaft. Eliminates separate ZooKeeper cluster.</div>
      <div class="rw-detail">Pre-3.x: ZooKeeper for controller election<br>KRaft: metadata stored in __cluster_metadata topic<br>Failover: ~30s (ZK) → milliseconds (KRaft)<br>Simpler ops: one system instead of two</div>
    </div>
    <div class="rw" style="border-left-color:var(--pur)">
      <div class="rw-name">ZooKeeper / ZAB</div>
      <div class="rw-sub">PAXOS VARIANT · COORDINATION SERVICE</div>
      <div class="rw-body">ZAB (ZooKeeper Atomic Broadcast) = Paxos variant. Still widely used for distributed locks, leader election, service discovery, config management.</div>
      <div class="rw-detail">ZAB vs Raft: new ZAB leader re-proposes all uncommitted entries from previous epoch; Raft leader commits new entries and old entries commit implicitly<br>Ephemeral znodes auto-deleted on session expire<br>Hadoop, HBase, older Kafka all depend on ZooKeeper</div>
    </div>
  </div>
  <table class="cmp-table" style="margin-top:14px">
    <thead><tr><th>PROPERTY</th><th>PAXOS</th><th>RAFT</th></tr></thead>
    <tbody>
      <tr><td>Leadership model</td><td>Any node can propose (no designated leader)</td><td>Strong single leader — only leader proposes</td></tr>
      <tr><td>Log ordering</td><td>Complex — gaps allowed, holes possible</td><td>Sequential — no gaps, simple ordering</td></tr>
      <tr><td>Understandability</td><td>Notoriously hard — vague on many details</td><td>Explicitly designed to be understandable</td></tr>
      <tr><td>Livelock risk</td><td>Yes — two proposers can keep pre-empting each other</td><td>No — randomized timeouts prevent simultaneous elections</td></tr>
      <tr><td>Reconfiguration</td><td>Not specified in original paper</td><td>Joint consensus specified and safe</td></tr>
      <tr><td>Real implementations</td><td>Chubby (Google), ZAB (ZooKeeper)</td><td>etcd, CockroachDB, TiKV, Consul, KRaft</td></tr>
    </tbody>
  </table>
</div>

<!-- INTERVIEW -->
<div class="view" id="view-interview">
  <div class="sh">Interview Q&A</div>
  <div class="sr">The consensus questions that appear in FAANG deep dives</div>
  <div class="iqa-list">
    <div class="iqa"><div class="iqa-hd" onclick="qa(this)"><div class="iqa-q">"How does Raft prevent split-brain?"</div><div class="iqa-arr">›</div></div><div class="iqa-bd">Quorum requirement — a leader can only be elected and can only commit entries with acknowledgements from a majority (⌊N/2⌋+1) of nodes. In a network partition, only one partition can have a majority. Two simultaneous leaders would require two separate majorities, which requires more than N nodes total. For N=5: two majorities of 3 = 6 nodes needed, impossible with 5. At most one partition can ever have quorum — no split-brain.</div></div>
    <div class="iqa"><div class="iqa-hd" onclick="qa(this)"><div class="iqa-q">"What happens if the Raft leader crashes mid-write?"</div><div class="iqa-arr">›</div></div><div class="iqa-bd">Two cases: (1) Entry not yet committed (not replicated to majority) — the new leader may not have it. From the client's perspective the write is lost (timeout); client must retry. (2) Entry was committed (majority had it) — the log completeness check in leader election guarantees only a candidate with all committed entries can win. The new leader will have the entry. Committed entries are never lost.</div></div>
    <div class="iqa"><div class="iqa-hd" onclick="qa(this)"><div class="iqa-q">"Why use 5 nodes instead of 3 for etcd in production?"</div><div class="iqa-arr">›</div></div><div class="iqa-bd">3 nodes tolerates 1 failure. 5 nodes tolerates 2 simultaneous failures. In a 3-AZ cloud deployment: a 5-node cluster can lose an entire AZ (1-2 nodes) AND a second node in another AZ and still maintain quorum. For rolling upgrades: take 1 node offline → 4/5 available, quorum maintained throughout. Write latency cost (waiting for 3 vs 2 ACKs) is acceptable for a coordination service. For most production Kubernetes clusters, 5 etcd nodes is the standard.</div></div>
    <div class="iqa"><div class="iqa-hd" onclick="qa(this)"><div class="iqa-q">"What is the difference between Raft and Paxos?"</div><div class="iqa-arr">›</div></div><div class="iqa-bd">Both solve consensus. Paxos allows any node to propose values — flexible but complex, especially for log replication where gaps and ordering become issues. It's also underspecified: leader election, reconfiguration, and gap handling are left to the implementer. Raft enforces a strong single leader — all writes go through the leader, the leader's log is always authoritative. Raft also explicitly specifies leader election (randomized timeouts), log replication (AppendEntries with consistency check), and cluster membership changes (joint consensus). Raft was designed to be understandable, which is why most modern systems choose it.</div></div>
    <div class="iqa"><div class="iqa-hd" onclick="qa(this)"><div class="iqa-q">"What is the FLP impossibility result and why does it matter?"</div><div class="iqa-arr">›</div></div><div class="iqa-bd">FLP (Fischer, Lynch, Paterson 1985) proves that in a fully asynchronous network where even one node may crash, no consensus algorithm can guarantee both safety (correct results) AND liveness (eventual progress). This means you must choose: Raft and Paxos choose safety — they may stall during certain failure scenarios but will never return incorrect results. This is the correct trade-off for databases. It's also the theoretical foundation of the CAP theorem: CP systems (like etcd) choose consistency over availability during partitions.</div></div>
    <div class="iqa"><div class="iqa-hd" onclick="qa(this)"><div class="iqa-q">"How does CockroachDB use Raft?"</div><div class="iqa-arr">›</div></div><div class="iqa-bd">CockroachDB shards table data into 64MB ranges, each with 3 replicas. Each range's replicas form an independent Raft group. A node simultaneously acts as Raft leader for some ranges and follower for others — load is naturally distributed. Writes to a key go to the Raft leader for that key's range, which replicates to the other two replicas and commits when 2 of 3 acknowledge. This gives CockroachDB serializable SQL transactions across a distributed cluster, with each range providing its own linearizable log.</div></div>
  </div>
</div>

<!-- TASKS -->
<div class="view" id="view-tasks">
  <div class="task-list">
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">1</div><div class="t-lbl">Raft Election Simulation</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Simulate a 5-node Raft cluster on paper. Nodes: A (leader, term=1), B, C, D, E (all followers).</p>
        <ol>
          <li>Leader A crashes. Election timeouts (random): B=180ms, C=250ms, D=300ms, E=350ms. Walk through exactly what messages B sends, what the others reply, and who wins.</li>
          <li>During B's election, network partition isolates Node E completely. What does E do? What does it see when the partition heals?</li>
          <li>A comes back online. Its term is still 1. The new leader is in term 2. What happens the moment A receives a heartbeat from the new leader?</li>
          <li>Edge case: B and C both time out at exactly the same time (before receiving each other's RequestVote). Walk through the split-vote scenario and the resolution.</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">2</div><div class="t-lbl">Log Replication & Healing</div><div class="t-meta">~1.5 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>5-node cluster. Leader L has log: <code>[t1:a=1][t1:b=2][t2:c=3][t2:d=4]</code>. Quorum = 3.</p>
        <ol>
          <li>Determine which entries are committed. Show your quorum calculation using the follower states shown in the Log Replication tab.</li>
          <li>For F4 (conflicting entry <code>t1:x=9</code> at index 3): What is the AppendEntries message L sends to heal it? What does F4 do with its conflicting entry?</li>
          <li>Where did F4's <code>t1:x=9</code> come from? (Hint: think about a previous leader in term 1 that proposed it but crashed before committing.)</li>
          <li>After healing, L commits entry <code>t2:d=4</code>. Walk through the commit protocol — which AppendEntries message triggers F2 and F3 to apply it to their state machines?</li>
        </ol>
      </div>
    </div>
    <div class="task-card">
      <div class="task-hd" onclick="tt(this)"><div class="t-num">3</div><div class="t-lbl">Quorum & Failure Scenarios</div><div class="t-meta">~1 hr</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>5-node etcd cluster across 3 AZs: AZ1 = nodes 1,2 | AZ2 = nodes 3,4 | AZ3 = node 5.</p>
        <ol>
          <li>AZ2 fails entirely (nodes 3 and 4 go down). Can the remaining 3 nodes elect a leader and process writes? Calculate the quorum.</li>
          <li>Network partition: {1, 3, 5} can reach each other; {2, 4} can reach each other. What happens in each partition? Which can elect a leader?</li>
          <li>You need to restart one node for maintenance. How many can be simultaneously down while maintaining quorum?</li>
          <li>You're expanding from 3 to 5 nodes. During the expansion, there's a brief window where the cluster is in a "joint consensus" state with both old (3) and new (5) configurations active. What are the risks? What would happen if the leader crashed exactly during this window?</li>
        </ol>
      </div>
    </div>
    <div class="task-card" style="border-top:2px solid var(--bri)">
      <div class="task-hd" onclick="tt(this)"><div class="t-num" style="color:var(--bri)">★</div><div class="t-lbl">Design etcd-Backed Leader Election for Microservices</div><div class="t-meta">~2 hrs</div><div class="t-arr">›</div></div>
      <div class="task-bd">
        <p>Design a leader election service for a microservice that must have exactly one active instance at a time (e.g., a Saga Orchestrator from B11).</p>
        <ol>
          <li>Use etcd leases (TTL keys): describe the full election protocol — how does a node acquire leadership? What is the TTL and why?</li>
          <li>The leader's network to etcd becomes slow (200ms latency, not broken). The lease TTL is 5s, heartbeat every 1s. What happens? Does the leader lose leadership?</li>
          <li>The leader process crashes without releasing the lease. How long before a new leader is elected? How do you minimize this window?</li>
          <li>Fencing problem: old leader (slow network) and new leader both think they are leader for a brief window. How do you prevent them from both writing to the same resource? (Hint: fencing tokens)</li>
          <li>Compare to ZooKeeper ephemeral znodes: same pattern, but what happens if the ZooKeeper session times out vs if the etcd lease expires?</li>
        </ol>
      </div>
    </div>
  </div>
</div>

<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 20 completed</span><span style="font-family:'JetBrains Mono',monospace">MODULE C1 · CONSENSUS</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>
  <div class="chk-grid">
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">FLP impossibility: safety vs liveness trade-off, why Raft chooses safety</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Paxos: Prepare → Promise → Accept → Accepted — all four phases and why</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Paxos safety invariant: proposer must use already-accepted value</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Paxos hard to implement: multi-Paxos, gaps, reconfiguration all unspecified</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Raft: three sub-problems (election, log replication, safety)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Raft node states: Follower → Candidate → Leader, and all transitions</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Terms as logical clock: higher-term RPC → immediately revert to Follower</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Leader election: randomized timeouts, RequestVote, log completeness check</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Log completeness guarantee: winner always has all committed entries</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Log replication: AppendEntries, prevLogIndex/prevLogTerm consistency check</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Commitment: entry committed when majority has it — never lost after that</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Log healing: nextIndex, decrement on rejection, follower overwrites conflicts</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Split-brain proof: two majorities require &gt;N nodes — impossible</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Quorum math: N=3→F=1, N=5→F=2; always odd-sized clusters</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">etcd: Raft for k8s control plane, 3 vs 5 nodes, linearizable vs serializable reads</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">CockroachDB: Raft per 64MB range, thousands of Raft groups, leaseholder</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">Kafka KRaft: Raft replacing ZooKeeper, faster failover, simpler ops</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 1: Raft election simulation (5-node, crash, partition, stale leader)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 2: Log replication and healing (conflicting entries, commit protocol)</div></div>
    <div class="chk" onclick="tick(this)"><div class="chk-box"></div><div class="chk-lbl">✏️ Task 4 (capstone): etcd-backed leader election with fencing tokens</div></div>
  </div>
  <div style="margin-top:28px;background:var(--panel);border:1px solid var(--bord2);padding:22px;border-top:2px solid var(--bri)">
    <div style="font-family:'JetBrains Mono',monospace;font-size:8px;color:var(--muted);letter-spacing:2px;margin-bottom:8px">// NEXT MODULE</div>
    <div style="font-family:'DM Serif Display',serif;font-size:26px;color:var(--white);margin-bottom:6px">C2 — Geo-Distribution & Multi-Region Architecture</div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--muted);line-height:2">
      Active-active vs active-passive · CRDTs · Conflict resolution<br>
      DynamoDB Global Tables · CockroachDB multi-region · Latency-based routing<br>
      GDPR & data residency · RPO/RTO design · Cross-region replication lag
    </div>
  </div>
</div>
</div>


<div class="mb-nav">
  <a href="/learning/system-design/hld/module-b14-kubernetes/">← B14 Kubernetes</a>
  <a href="/learning/system-design/hld/module-c1-notes/">📄 Study Notes</a>
  <a href="/learning/system-design/system-design-roadmap/">↑ Roadmap</a>
  <a href="/learning/system-design/hld/module-c2-geo-distribution/" class="primary">C2 Geo-Distribution →</a>
</div>

<script src="/assets/js/sd-module-c1.js"></script>
