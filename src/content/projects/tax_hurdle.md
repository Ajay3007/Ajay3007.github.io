---
title: "tax_hurdle"
description: "STCG, LTCG, and speculation tax calculator for Indian equity traders. Parses broker Excel exports, auto-detects column mapping, and produces quarterly breakdowns."
year: 2022
tech: ["Java", "Spring Boot", "Apache POI", "JavaFX", "Swagger"]
github: https://github.com/Ajay3007/tax_hurdle
url: /projects/tax_hurdle/
---

## The Problem

Indian equity traders must calculate STCG, LTCG, and speculation (intraday) P&L separately for ITR filing, across hundreds or thousands of transactions from broker exports. Manual spreadsheet work takes hours and drifts easily. tax_hurdle automates the entire pipeline from raw broker XLSX to a clean quarterly summary.

## How It Works

Upload a broker export (Upstox, Zerodha, or similar). The system auto-detects the column layout, classifies each trade as STCG/LTCG/speculation, and produces:

- Per-quarter STCG and LTCG breakdowns (standard Indian Q1–Q4 + Q5 scheme)
- Speculation P&L and turnover (intraday trades, abs P&L basis)
- Downloadable Excel summary report

Two interfaces ship in the same repo: a Spring Boot REST API (with Swagger UI) and a JavaFX desktop GUI.

## Features

<div class="c-feat-grid">
  <div class="c-feat-card">
    <div class="c-feat-title">Auto-detect Broker Mapping</div>
    <div class="c-feat-desc">Identifies column layout from the XLSX header row. Supports Upstox, Zerodha, and configurable mappings. Shows a preview so you can diagnose mismatches before processing.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">Trade Classification</div>
    <div class="c-feat-desc">Separates STCG (held &gt;24h), LTCG (held &gt;1y), and intraday speculation automatically. Handles the FIFO queue required by Indian tax law for STCG matching.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">Spring Boot REST API</div>
    <div class="c-feat-desc">POST broker XLSX → receive JSON breakdown or download a formatted Excel summary. Swagger UI included for manual testing without a frontend.</div>
  </div>
  <div class="c-feat-card">
    <div class="c-feat-title">JavaFX Desktop GUI</div>
    <div class="c-feat-desc">File picker, live results table, and export button — runs fully offline. Built for traders who prefer not to upload financial data to a server.</div>
  </div>
</div>

## Stack

<div class="c-stack-grid">
  <div><div class="c-stack-key">language</div><div class="c-stack-val">Java 17+</div></div>
  <div><div class="c-stack-key">api</div><div class="c-stack-val">Spring Boot</div></div>
  <div><div class="c-stack-key">excel</div><div class="c-stack-val">Apache POI 5.x</div></div>
  <div><div class="c-stack-key">desktop</div><div class="c-stack-val">JavaFX</div></div>
  <div><div class="c-stack-key">docs</div><div class="c-stack-val">Swagger / OpenAPI</div></div>
  <div><div class="c-stack-key">logging</div><div class="c-stack-val">Apache Log4j2</div></div>
</div>

## Sample Output

```text
[INFO] Parsed 2,401 transactions from broker export.

STCG Summary (FY 2021-22):
  Q1 Apr–Jun  ₹ 45,000
  Q2 Jul–Sep  ₹ 67,500
  Q3 Oct–Dec  ₹ 32,100
  Q4 Jan–Mar  ₹ 58,900
  Q5 Mar-end  ₹ 12,500
  ─────────────────────
  Total STCG  ₹ 2,16,000

Intraday Speculation P&L  ₹ 8,50,000
```
