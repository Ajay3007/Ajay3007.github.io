---
layout: project
title: workctl
description: "CLI + GUI workspace manager. Kanban board, work logs, command library, and Claude AI agent — all stored as plain Markdown files. No database, fully Git-versionable."
github: https://github.com/Ajay3007/workctl
tags: [Java, JavaFX 21, Gradle, Claude API, Picocli, Markdown]
year: 2024
permalink: /projects/workctl/
---

## Design Philosophy

Developer task tracking is fragmented across browser tabs, sticky notes, and half-finished Notion pages. workctl consolidates it into a single tool with one key constraint: **filesystem as database**. Every task, log, and command lives in `.md` files — human-readable, Git-versionable, and zero-migration-forever.

## Features

<div class="c-feat-grid">
  <div class="c-feat-card">
    <div class="c-feat-title">Task Kanban</div>
    <div class="c-feat-desc">Open → In Progress → Done board with drag-and-drop in the GUI. Priority sorting, subtask tracking, and stagnation detection built in.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">Work Logging</div>
    <div class="c-feat-desc">Structured daily logs with sections for assigned work, completed items, notes, and commands run. Auto-generate weekly summaries across a date range.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">Claude AI Agent</div>
    <div class="c-feat-desc">Embedded agent in both CLI and GUI. Read mode queries your workspace for insights; write mode decomposes goals into subtasks via the Anthropic API tool-use loop.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">Command Library</div>
    <div class="c-feat-desc">Personal searchable reference for Linux, Docker, Git, and any CLI commands. Reusable workflow templates with per-run execution tracking.</div>
  </div>
</div>

## Stack

<div class="c-stack-grid">
  <div><div class="c-stack-key">language</div><div class="c-stack-val">Java 17+</div></div>
  <div><div class="c-stack-key">build</div><div class="c-stack-val">Gradle (multi-module)</div></div>
  <div><div class="c-stack-key">gui</div><div class="c-stack-val">JavaFX 21</div></div>
  <div><div class="c-stack-key">cli</div><div class="c-stack-val">Picocli</div></div>
  <div><div class="c-stack-key">markdown</div><div class="c-stack-val">CommonMark</div></div>
  <div><div class="c-stack-key">ai</div><div class="c-stack-val">Claude API</div></div>
</div>

## Quick Start

```bash
# Download release binary (no Java needed)
# https://github.com/Ajay3007/workctl/releases/tag/v2.0.0

workctl init --workspace ~/work
workctl add-task -t "Prepare System Design Board" -p 1
workctl mark 1          # move to Done
workctl gui             # launch JavaFX desktop app
```

## Modules

The repo is a Gradle multi-module monorepo:

- `core/` — parsing engine, task models, logs, configs
- `cli/` — Picocli command-line interface bound to core
- `gui/` — JavaFX presentation layer
- `agent/` — Claude API interaction and context builder
