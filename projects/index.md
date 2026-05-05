---
layout: default
title: Projects
---

<section class="c-section" style="margin-top: 0; padding-top: 56px;">
  <div class="c-section-head">
    <div>
      <div class="c-kicker">// SHIPPED</div>
      <h1 class="c-section-title">Projects.</h1>
    </div>
  </div>

  <div class="c-card-grid c-cols-2">

    <div class="c-card c-proj-card">
      <div class="c-card-meta">
        <span>№ 01</span>
        <span>2024</span>
      </div>
      <div class="c-proj-viz">
        <div class="c-viz-pipeline">
          <span class="c-viz-node">UPLOAD</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node">PARSE</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node c-viz-node--hi">EDIT · GEN · MERGE</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node">EXPORT</span>
        </div>
        <div class="c-viz-label">Flask + Vue.js · PCAP &amp; binary analysis</div>
      </div>
      <h2 class="c-card-title"><span class="c-card-slash">~/</span>devtoolbox</h2>
      <p class="c-card-desc">Web suite for network packet analysis. Edit, generate, and merge PCAP captures; inspect binary files in hex from a browser — no local tooling required.</p>
      <div class="c-tag-row">
        <span class="c-tag">Python</span>
        <span class="c-tag">Flask</span>
        <span class="c-tag">Vue.js 3</span>
        <span class="c-tag">Scapy</span>
        <span class="c-tag">Docker</span>
      </div>
      <div class="c-proj-links">
        <a href="{{ '/projects/devtoolbox/' | relative_url }}" class="c-proj-link-case">Case study →</a>
        <a href="https://github.com/Ajay3007/devtoolbox" target="_blank" rel="noopener noreferrer" class="c-proj-link-gh">GitHub ↗</a>
      </div>
    </div>

    <div class="c-card c-proj-card">
      <div class="c-card-meta">
        <span>№ 02</span>
        <span>2024</span>
      </div>
      <div class="c-proj-viz">
        <div class="c-viz-kanban">
          <div>
            <div class="c-viz-col-head">TODO</div>
            <div class="c-viz-chip">New module</div>
            <div class="c-viz-chip">Write docs</div>
          </div>
          <div>
            <div class="c-viz-col-head">IN PROGRESS</div>
            <div class="c-viz-chip c-viz-chip--active">AI agent loop</div>
          </div>
          <div>
            <div class="c-viz-col-head">DONE</div>
            <div class="c-viz-chip c-viz-chip--done">CLI v2</div>
            <div class="c-viz-chip c-viz-chip--done">GUI release</div>
          </div>
        </div>
      </div>
      <h2 class="c-card-title"><span class="c-card-slash">~/</span>workctl</h2>
      <p class="c-card-desc">Java CLI + GUI workspace manager. Kanban board, work logs, command library, and Claude AI agent — all stored as plain Markdown. No database.</p>
      <div class="c-tag-row">
        <span class="c-tag">Java</span>
        <span class="c-tag">JavaFX</span>
        <span class="c-tag">Gradle</span>
        <span class="c-tag">Claude API</span>
        <span class="c-tag">Picocli</span>
      </div>
      <div class="c-proj-links">
        <a href="{{ '/projects/workctl/' | relative_url }}" class="c-proj-link-case">Case study →</a>
        <a href="https://github.com/Ajay3007/workctl" target="_blank" rel="noopener noreferrer" class="c-proj-link-gh">GitHub ↗</a>
      </div>
    </div>

    <div class="c-card c-proj-card">
      <div class="c-card-meta">
        <span>№ 03</span>
        <span>2024</span>
      </div>
      <div class="c-proj-viz">
        <div class="c-viz-pipeline">
          <span class="c-viz-node">PCAP</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node">LINK LAYER</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node">TCP REASSEMBLY</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node">FTP PARSER</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node c-viz-node--hi">FILE OUT</span>
        </div>
        <div class="c-viz-label">C++ · libpcap · offline file reconstruction</div>
      </div>
      <h2 class="c-card-title"><span class="c-card-slash">~/</span>ftp-analyzer</h2>
      <p class="c-card-desc">C++ utility that reconstructs FTP-transferred files from raw PCAP captures. Performs TCP reassembly and FTP control-channel parsing entirely offline — no server access needed.</p>
      <div class="c-tag-row">
        <span class="c-tag">C++</span>
        <span class="c-tag">libpcap</span>
        <span class="c-tag">TCP/IP</span>
        <span class="c-tag">CMake</span>
      </div>
      <div class="c-proj-links">
        <a href="{{ '/projects/ftp-analyzer/' | relative_url }}" class="c-proj-link-case">Case study →</a>
        <a href="https://github.com/Ajay3007/ftp-analyzer" target="_blank" rel="noopener noreferrer" class="c-proj-link-gh">GitHub ↗</a>
      </div>
    </div>

    <div class="c-card c-proj-card">
      <div class="c-card-meta">
        <span>№ 04</span>
        <span>2025</span>
      </div>
      <div class="c-proj-viz">
        <div class="c-viz-pipeline">
          <span class="c-viz-node">INPUT</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node c-viz-node--hi">CLAUDE</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node">REDIS TOOL</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node">RESULT</span>
        </div>
        <div class="c-viz-loop-note">↑ result feeds back to Claude ↑</div>
      </div>
      <h2 class="c-card-title"><span class="c-card-slash">~/</span>redis-ai-agent</h2>
      <p class="c-card-desc">Claude-powered AI agent that translates plain English to Redis operations. Demonstrates the agent loop pattern: Claude decides which tool to call, reads the result, then explains what happened.</p>
      <div class="c-tag-row">
        <span class="c-tag">Java</span>
        <span class="c-tag">Maven</span>
        <span class="c-tag">Claude API</span>
        <span class="c-tag">Redis</span>
        <span class="c-tag">Docker</span>
      </div>
      <div class="c-proj-links">
        <a href="{{ '/projects/redis-ai-agent/' | relative_url }}" class="c-proj-link-case">Case study →</a>
        <a href="https://github.com/Ajay3007/redis-ai-agent" target="_blank" rel="noopener noreferrer" class="c-proj-link-gh">GitHub ↗</a>
      </div>
    </div>

    <div class="c-card c-proj-card c-card-full">
      <div class="c-card-meta">
        <span>№ 05</span>
        <span>2022</span>
      </div>
      <div class="c-proj-viz">
        <div class="c-viz-pipeline">
          <span class="c-viz-node">BROKER XLSX</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node">AUTO-DETECT MAP</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node">CALCULATE</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node c-viz-node--hi">STCG · LTCG · SPECULATION</span>
          <span class="c-viz-arrow">→</span>
          <span class="c-viz-node">EXPORT</span>
        </div>
        <div class="c-viz-label">Java · Spring Boot · Apache POI · JavaFX</div>
      </div>
      <h2 class="c-card-title"><span class="c-card-slash">~/</span>tax_hurdle</h2>
      <p class="c-card-desc">STCG, LTCG, and speculation tax calculator for Indian equity traders. Upload broker Excel exports (Upstox, Zerodha), auto-detect column mapping, compute quarterly breakdowns, and export a full summary — via Spring Boot REST API or JavaFX desktop GUI.</p>
      <div class="c-tag-row">
        <span class="c-tag">Java</span>
        <span class="c-tag">Spring Boot</span>
        <span class="c-tag">Apache POI</span>
        <span class="c-tag">JavaFX</span>
        <span class="c-tag">Swagger</span>
      </div>
      <div class="c-proj-links">
        <a href="{{ '/projects/tax_hurdle/' | relative_url }}" class="c-proj-link-case">Case study →</a>
        <a href="https://github.com/Ajay3007/tax_hurdle" target="_blank" rel="noopener noreferrer" class="c-proj-link-gh">GitHub ↗</a>
      </div>
    </div>

  </div>
</section>
