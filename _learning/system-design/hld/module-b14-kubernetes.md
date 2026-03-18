---
layout: default
title: "Module B14: Kubernetes & Container Orchestration"
permalink: /learning/system-design/hld/module-b14-kubernetes/
---

<link rel="stylesheet" href="{{ "/assets/css/sd-module-b14.css" | relative_url }}">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<div class="sd-module-b14">

<header>
  <div class="hdr-stamp">
    <span>SYSTEM DESIGN MASTERY · TRACK B · MODULE B14 · WEEK 16</span>
    <span>CONTAINER ORCHESTRATION · MICROSERVICES · ISTIO</span>
  </div>
  <div class="hdr-main">
    <div>
      <div class="hdr-kicker">THE DE FACTO OPERATING SYSTEM OF THE CLOUD</div>
      <h1>KUBERNETES <span class="hl">&amp;</span><br>CONTAINERS</h1>
      <div class="hdr-sub">Moving from single servers to distributed clusters. Learn how Kubernetes automates deployment, scaling, healing, and operations of application containers across clusters of hosts.</div>
    </div>
    <div class="hdr-stats">
      <div class="hs"><div class="hs-v">1</div><div class="hs-l">CONTROL PLANE</div></div>
      <div class="hs"><div class="hs-v">N</div><div class="hs-l">WORKER NODES</div></div>
      <div class="hs"><div class="hs-v">OOTB</div><div class="hs-l">AUTO-HEALING</div></div>
    </div>
  </div>
</header>

<nav class="nav">
  <div class="nt active" onclick="mb14_show('arch', this)">Architecture</div>
  <div class="nt" onclick="mb14_show('primitives', this)">K8s Primitives</div>
  <div class="nt" onclick="mb14_show('scaling', this)">Autoscaling</div>
  <div class="nt" onclick="mb14_show('mesh', this)">Service Mesh</div>
  <div class="nt" onclick="mb14_show('qa', this)">Quick Answers</div>
  <div class="nt" onclick="mb14_show('checklist', this)">Checklist</div>
</nav>

<div class="content">

<!-- ARCHITECTURE -->
<div class="view active" id="view-arch">
  <div class="sh">Cluster Architecture</div>
  <div class="sr">How Kubernetes manages state across thousands of independent machines.</div>
  
  <div class="al"><em>The Goal:</em> Abstract away individual machines. Instead of saying "Deploy this Node.js app to Server A, Server B, and Server C," you tell Kubernetes, "Ensure there are always 3 copies of this Node.js app running somewhere in the cluster, evenly distributed."</div>

  <div class="k8s-grid">
    <div class="k8s-node cp">
      <div class="kn-title">Control Plane <span class="kn-badge">BRAIN</span></div>
      <div class="kn-desc">The master node(s) that manage the cluster state. It makes global decisions (scheduling, responding to cluster events). Contains:
      <br><br><strong>API Server:</strong> The front door. All commands (`kubectl`) go here.
      <br><strong>etcd:</strong> Highly-available Key-Value store holding cluster state.
      <br><strong>Scheduler:</strong> Assigns newly created Pods to Worker Nodes based on CPU/RAM.
      <br><strong>Controller Manager:</strong> Runs background loops to constantly match current state to desired state.</div>
    </div>
    <div class="k8s-node">
      <div class="kn-title">Worker Node <span class="kn-badge">MUSCLE</span></div>
      <div class="kn-desc">The VMs or physical servers where your application containers actually run. Contains:
      <br><br><strong>Kubelet:</strong> The agent running on each node. Ensures containers are healthy and running in their Pods.
      <br><strong>Kube-Proxy:</strong> Maintains network rules on the node, allowing network communication to your Pods.
      <br><strong>Container Runtime:</strong> The software that actually runs containers (e.g., containerd, CRI-O).</div>
    </div>
  </div>
</div>

<!-- PRIMITIVES -->
<div class="view" id="view-primitives">
  <div class="sh">The Hierarchy of K8s Primitives</div>
  <div class="sr">The abstractions you use to define your infrastructure as code.</div>

  <div class="hier">
    <div class="hier-item">
      <div class="hi-icon">1</div>
      <div class="hi-body">
        <div class="hi-title">Pod</div>
        <div class="hi-desc">The smallest deployable unit. Usually contains one container (e.g., your Spring Boot app), but can contain sidecars. Pods are ephemeral — if a node dies, the Pod dies and is not revived. A new one takes its place elsewhere.</div>
      </div>
    </div>
    <div class="hier-item">
      <div class="hi-icon">2</div>
      <div class="hi-body">
        <div class="hi-title">ReplicaSet</div>
        <div class="hi-desc">Ensures a specified number of identical Pod replicas are running at any given time. Usually not managed directly by humans, but by Deployments.</div>
      </div>
    </div>
    <div class="hier-item">
      <div class="hi-icon">3</div>
      <div class="hi-body">
        <div class="hi-title">Deployment</div>
        <div class="hi-title" style="font-family: monospace; font-size: 11px; margin-top: 4px; font-weight:normal; color:var(--prim)">State: Stateless Apps</div>
        <div class="hi-desc">Manages ReplicaSets to provide declarative updates. You define the <em>desired state</em> ("I want v2 of my app with 3 replicas"), and the Deployment handles the rolling update from v1 to v2 with zero downtime.</div>
      </div>
    </div>
    <div class="hier-item">
      <div class="hi-icon">4</div>
      <div class="hi-body">
        <div class="hi-title">Service</div>
        <div class="hi-desc">An abstract way to expose an application running on a set of Pods as a network service. Because Pod IPs constantly change, the Service provides a single stable IP and DNS name that load-balances across the healthy Pods.</div>
      </div>
    </div>
    <div class="hier-item">
      <div class="hi-icon">5</div>
      <div class="hi-body">
        <div class="hi-title">StatefulSet</div>
        <div class="hi-title" style="font-family: monospace; font-size: 11px; margin-top: 4px; font-weight:normal; color:var(--acc)">State: Stateful Apps (DBs)</div>
        <div class="hi-desc">Like a Deployment, but provides guarantees about the ordering and uniqueness of Pods. Pods get sticky, persistent identities (e.g., `mysql-0`, `mysql-1`) and persistent storage volumes that survive Pod restarts. Essential for running databases in K8s.</div>
      </div>
    </div>
  </div>
</div>

<!-- SCALING -->
<div class="view" id="view-scaling">
  <div class="sh">Autoscaling Dimensions</div>
  <div class="sr">Reacting to traffic spikes automatically without human intervention.</div>

  <div class="k8s-grid">
    <div class="k8s-node">
      <div class="kn-title">HPA (Horizontal Pod Autoscaler)</div>
      <div class="kn-desc"><strong>Scales: Up & Out (More Pods)</strong><br><br>Watches metrics like CPU or memory utilization. If CPU > 75%, it automatically increases the `# of replicas` in the Deployment. Essential tool for handling variable daily traffic.</div>
    </div>
    <div class="k8s-node">
      <div class="kn-title">VPA (Vertical Pod Autoscaler)</div>
      <div class="kn-desc"><strong>Scales: Up (Bigger Pods)</strong><br><br>Automatically adjusts the CPU and memory reservations for your Pods over time. If your Java app keeps OOM-killing, VPA will restart it with a higher memory limit automatically.</div>
    </div>
    <div class="k8s-node">
      <div class="kn-title">Cluster Autoscaler</div>
      <div class="kn-desc"><strong>Scales: Worker Nodes (Infrastructure)</strong><br><br>When HPA creates new Pods, but all Worker Nodes are full, those Pods stay in a "Pending" state. Cluster Autoscaler notices this and talks to AWS/GCP to provision completely new underlying VMs, joining them to the cluster.</div>
    </div>
  </div>

  <div class="al warn"><em>Interview Tip:</em> When asked "How does the system handle a massive spike?" configuring HPA + Cluster Autoscaler allows the system to seamlessly burst without manual ops intervention.</div>
</div>

<!-- MESH -->
<div class="view" id="view-mesh">
  <div class="sh">Service Mesh & Ingress</div>
  <div class="sr">Managing complex L7 network routing, security, and observability.</div>

  <div class="hier-item" style="margin-bottom: 24px;">
    <div class="hi-body">
      <div class="hi-title">Ingress Controller (e.g., NGINX Ingress)</div>
      <div class="hi-desc">An API object that manages external access to the services in a cluster. It provides HTTP/HTTPS routing based on URLs. E.g., `api.example.com/billing` goes to the Billing Service, while `api.example.com/users` goes to the Users Service. It typically handles SSL termination.</div>
    </div>
  </div>

  <div class="sh">Service Mesh (Istio / Linkerd)</div>
  <div class="sr">The Sidecar Pattern</div>
  
  <div class="al">As your microservices grow to 50+, managing retries, timeouts, circuit breakers, and mutual TLS between every service inside the application code becomes an unmaintainable nightmare.</div>
  
  <p style="font-size: 14px; line-height: 1.6; color: var(--text); margin-bottom: 16px;">A Service Mesh solves this by injecting a <strong>Sidecar Proxy</strong> (like Envoy) into every single Pod. Your application code only talks to `localhost`. The sidecar intercepts all traffic and handles:</p>
  
  <ul style="font-size: 14px; line-height: 1.6; color: var(--text); margin-left: 20px; margin-bottom: 24px;">
    <li>Transparent mTLS encryption between all services.</li>
    <li>L7 Load Balancing (e.g., canary routing 10% traffic to v2).</li>
    <li>Automatic retries, timeouts, and circuit breaking.</li>
    <li>Distributed tracing and metrics collection (Prometheus/Jaeger integration).</li>
  </ul>
</div>

<!-- QA -->
<div class="view" id="view-qa">
  <div class="sh">Quick Answers</div>
  <div class="sr">K8s concepts commonly tested in system design interviews.</div>

  <div class="qa-list">
    <div class="qa">
      <div class="qa-hd" onclick="mb14_qa(this)">
        <div class="qa-q">Should you run a relational database (PostgreSQL/MySQL) in Kubernetes?</div>
        <div class="qa-arr">+</div>
      </div>
      <div class="qa-bd">Technically possible using StatefulSets and PVs (Persistent Volumes). However, in most enterprise environments, it is far safer and less operationally burdensome to use managed databases (like AWS RDS or Aurora). Use K8s for stateless compute, use Cloud Providers for stateful storage. If you MUST run it in K8s, use an Operator (like Patroni) to manage failover.</div>
    </div>
    
    <div class="qa">
      <div class="qa-hd" onclick="mb14_qa(this)">
        <div class="qa-q">What is the difference between a Liveness Probe and a Readiness Probe?</div>
        <div class="qa-arr">+</div>
      </div>
      <div class="qa-bd"><strong>Readiness Probe:</strong> Does this container have established DB connections and is ready to receive traffic? If it fails, K8s stops sending traffic to the Pod via Services, but doesn't kill it.<br><br><strong>Liveness Probe:</strong> Is this container deadlocked or crashed? If it fails, K8s restarts the container.</div>
    </div>

    <div class="qa">
      <div class="qa-hd" onclick="mb14_qa(this)">
        <div class="qa-q">What is the "Split-Brain" problem in etcd?</div>
        <div class="qa-arr">+</div>
      </div>
      <div class="qa-bd">etcd uses the Raft consensus algorithm, which strictly requires a majority quorum `(N/2)+1` to write state. Running a 2-node etcd cluster is dangerous because if the network partitions, neither node has a majority, and the cluster becomes read-only. Always run etcd (Control Plane) in odd numbers: 3, 5, or 7.</div>
    </div>
  </div>
</div>

<!-- CHECKLIST -->
<div class="view" id="view-checklist">
  <div class="prog-row"><span id="prog-lbl">0 / 6 completed</span><span>MODULE B14 PROGRESS</span></div>
  <div class="prog-track"><div class="prog-fill" id="prog-fill"></div></div>

  <div class="chk-grid">
    <div class="chk" onclick="mb14_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Understand the separation of Control Plane and Worker Nodes.</div></div>
    <div class="chk" onclick="mb14_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can differentiate Pods, Deployments, Services, and StatefulSets.</div></div>
    <div class="chk" onclick="mb14_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Know the three dimensions of autoscaling (HPA, VPA, Cluster Autoscaler).</div></div>
    <div class="chk" onclick="mb14_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Understand what Ingress is and how it routes L7 HTTP traffic.</div></div>
    <div class="chk" onclick="mb14_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Can explain the Sidecar pattern and the primary uses for a Service Mesh.</div></div>
    <div class="chk" onclick="mb14_tick(this)"><div class="chk-box"></div><div class="chk-lbl">Completed HLD Track and ready for full System Design mock interviews.</div></div>
  </div>
</div>

</div>

<div class="mb-nav">
  <a href="/learning/system-design/hld/module-b13-ml-systems/" class="btn">← B13 ML SYSTEMS</a>
  <a href="/learning/system-design/system-design-roadmap/" class="btn">↑ ROADMAP</a>
  <a href="/learning/system-design/hld/module-c1-consensus/" class="btn">NEXT: C1 CONSENSUS →</a>
</div>

</div>
<script src="{{ "/assets/js/sd-module-b14.js" | relative_url }}"></script>
