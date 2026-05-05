---
layout: project
title: redis-ai-agent
description: "Claude-powered AI agent that translates plain English to Redis operations. A hands-on implementation of the agent loop pattern for backend engineers."
github: https://github.com/Ajay3007/redis-ai-agent
tags: [Java, Maven, Claude API, Redis, Docker]
year: 2025
permalink: /projects/redis-ai-agent/
---

## What It Is

Most AI demos are chatbots — they respond with text. This project implements a true **agent loop**: Claude doesn't just answer, it decides which Redis operation to run, executes it, reads the result, and then explains what happened. The key distinction is tool use with feedback.

```
You: "Set user:1001 to 'Ajay' and expire it in 300 seconds"
  ↓
AgentLoop → Claude API → Claude calls: set_key tool
  ↓
RedisTools → jedis.setex("user:1001", 300, "Ajay")
  ↓
Tool result fed back to Claude
  ↓
Agent: "Done! Stored 'Ajay' under user:1001 with a 5-minute TTL."
```

## Features

<div class="c-feat-grid">
  <div class="c-feat-card">
    <div class="c-feat-title">Agent Loop</div>
    <div class="c-feat-desc">Full multi-turn loop: user input → Claude API call with tool definitions → tool execution → result back to Claude → final response. Handles multi-step operations in one conversation turn.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">Redis Tool Set</div>
    <div class="c-feat-desc">Four Redis operations exposed as Claude tools: get key, set key (with optional TTL), delete key, and list all keys. Claude decides which to call based on the user's natural language input.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">Clean Architecture</div>
    <div class="c-feat-desc">Four focused classes: Main (REPL loop), AgentLoop (orchestration), ClaudeClient (HTTP + tool schema), RedisTools (Jedis operations). Easy to extend with new tools.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">Zero Framework</div>
    <div class="c-feat-desc">Raw HTTP calls to the Anthropic API — no LangChain, no Spring AI. The agent loop logic is fully visible and easy to study, which is the point of the project.</div>
  </div>
</div>

## Stack

<div class="c-stack-grid">
  <div><div class="c-stack-key">language</div><div class="c-stack-val">Java 17+</div></div>
  <div><div class="c-stack-key">build</div><div class="c-stack-val">Maven</div></div>
  <div><div class="c-stack-key">ai</div><div class="c-stack-val">Claude API (tool use)</div></div>
  <div><div class="c-stack-key">redis client</div><div class="c-stack-val">Jedis</div></div>
  <div><div class="c-stack-key">redis server</div><div class="c-stack-val">Docker (redis:7-alpine)</div></div>
</div>

## Quick Start

```bash
# 1. Start Redis
docker run -d --name redis-agent -p 6379:6379 redis:7-alpine

# 2. Set API key
export ANTHROPIC_API_KEY=sk-ant-...

# 3. Build and run
git clone https://github.com/Ajay3007/redis-ai-agent.git
cd redis-ai-agent
mvn clean package -q
java -jar target/redis-ai-agent-1.0-SNAPSHOT.jar

> Set user:42 to "hello" with 60s TTL
Agent: Done — stored "hello" at user:42, expires in 60 seconds.
```
