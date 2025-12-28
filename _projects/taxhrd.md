---
layout: project
title: TaxHrd - Investment Tax Calculation System
description: "Java-based investment tax calculator for Indian equity traders. Automates STCG calculation with quarter-wise breakdown, Excel integration, and comprehensive logging."
permalink: /projects/taxhrd/
---

# TaxHrd Engine

**A Java-based system to calculate and categorize investment taxes (STCG) from equity trading activity.**

---

## Overview

TaxHrd is a specialized financial application designed to **automate tax calculations for Indian equity traders**. It reads Excel-based trading data and produces **quarter-wise Short-Term Capital Gains (STCG) breakdowns**, separate from intraday speculation profits.

**Use Case:** Prepare accurate tax reports for CA (Chartered Accountant) filing during ITR submission.

---

## Key Features

✅ **Dual-Mode Trade Classification**
- **STCG (Long-Term):** Shares held >24hrs, taxed as capital gains
- **Intraday (Speculation):** Day trades, taxed as regular income

✅ **Quarter-Wise STCG Breakdown**
- Automatically segregates gains by financial quarter (Q1, Q2, Q3, Q4, Q5)
- Aligns with Indian tax year (April–March)

✅ **Excel Integration**
- Reads buy/sell data from `.xlsx` files
- Validates all required fields (security, date, price, quantity)
- Robust error handling with custom exceptions

✅ **Comprehensive Logging**
- Apache Log4j2 integration
- Rolling file appenders with size-based rotation
- Console + file output simultaneously

✅ **Financial Calculations**
- Buy/Sell value aggregation
- P&L (Profit & Loss) computation
- Average price tracking per security

---

## Project Architecture

### Package Structure

```
InvestingHurdle/
├── src/
│   ├── bootstrap/
│   │   └── InvestingHurdleBootstrapper.java    # Singleton entry point
│   ├── params/
│   │   ├── WorkbookLoader.java                 # Excel parser for buy/sell
│   │   └── EquityLoader.java                   # STCG calculator & aggregator
│   ├── security/
│   │   └── Security.java                       # Trade record model
│   ├── logging/
│   │   └── HurdleLogger.java                   # Log4j2 config wrapper
│   ├── util/
│   │   └── HurdleConstant.java                 # File path constants
│   └── exception/
│       └── InvalidSecurityException.java        # Custom validation error
```

### Core Components

**1. InvestingHurdleBootstrapper** (Main Entry)
- Singleton pattern for global state
- Orchestrates loader initialization
- Prints summary reports to console
- Uses `ConcurrentHashMap` for thread-safe security storage

**2. WorkbookLoader**
- Parses "Buy" and "Sell" sheets from Excel
- Extracts: Security name, Date, Price, Quantity, LTP (Last Traded Price)
- Stores all trades in a `Queue<Security>` per company
- Throws `InvalidSecurityException` on missing fields

**3. EquityLoader**
- Reads "Equities" sheet with pre-calculated values
- Maps dates to financial quarters
- Aggregates STCG by quarter (`stcgQ1..Q5`)
- Sums intraday turnover separately
- Returns totals for buy/sell/P&L

**4. Security**
- Immutable trade record (with getters/setters)
- Stores: Company, Date, Buy/Sell Price, Quantity, LTP
- Calculates: Buy/Sell average, Total value, P&L

**5. HurdleLogger**
- Wraps Apache Log4j2
- Configures console + rolling file appenders
- Logs to `./logs/` with 10KB per file, max 5 backups

---

## Financial Concepts

### STCG (Short-Term Capital Gains)

In India, if you **hold shares >24 hours before selling**:
- **STCG = Sell Value – Buy Value**
- Taxed as ordinary income (add to salary for tax bracket)
- **Not eligible** for long-term capital gains indexation

**Financial Year Quarters:**
- **Q1:** Apr 1 — Jun 15
- **Q2:** Jun 16 — Sep 15
- **Q3:** Sep 16 — Dec 15
- **Q4:** Dec 16 — Mar 15
- **Q5:** Mar 16 — Mar 31 (closing period)

### Intraday Turnover

Shares bought and sold within the **same trading day**:
- Profits taxed as "Other Sources" income
- Must report total turnover for disclosure
- Separate from STCG calculation

---

## How It Works

1. **Load Configuration**
   - Read `./configuration/configuration_stock.xlsx` (buy/sell data)
   - Read `./configuration/tax_2122_.xlsx` (equity transaction details)

2. **Parse Trades**
   - `WorkbookLoader` extracts buy/sell transactions
   - Creates `Security` objects, stores in `securityMap`

3. **Calculate Tax Metrics**
   - `EquityLoader` processes equity sheet (rows 25–297)
   - Identifies STCG vs. intraday based on holding period
   - Allocates STCG to quarters by sale date

4. **Report Results**
   ```
   STCG Summary:
   - Total STCG: ₹X,XXX
   - Q1: ₹X,XXX | Q2: ₹X,XXX | Q3: ₹X,XXX | Q4: ₹X,XXX | Q5: ₹X,XXX
   
   Speculation Summary:
   - Buy Value: ₹X,XXX | Sell Value: ₹X,XXX
   - Total Turnover: ₹X,XXX
   ```

---

## Code Quality & Design Patterns

### Patterns Used

✅ **Singleton Pattern** — Bootstrap manages single instance of loaders  
✅ **Factory Pattern** — `Security` objects created via constructors  
✅ **Queue Pattern** — `Queue<Security>` per company for FIFO processing  
✅ **ConcurrentHashMap** — Thread-safe multi-threaded access  

### Strengths

- Clear separation of concerns (parsing, calculation, logging)
- Custom exception for validation errors
- Robust Excel error handling (null checks, type casting)
- Comprehensive P&L tracking per security

---

## Potential Improvements

⚠️ **Current Limitations:**

1. **Hardcoded Quarters**  
   - Q dates hardcoded in `returnQuarter()` method
   - **Suggestion:** Externalize to config file for multi-year support

2. **Missing Average Price Logic**  
   - `setAveragePrices()` method is empty
   - **Suggestion:** Implement FIFO/LIFO matching for precise cost basis

3. **No CSV/XML Export**  
   - Currently console-only output
   - **Suggestion:** Add `ReportGenerator` class for ITR-friendly formats

4. **Static File Paths**  
   - Excel paths hardcoded in `HurdleConstant`
   - **Suggestion:** Accept paths as CLI arguments

5. **Minimal Testing**  
   - No unit tests present
   - **Suggestion:** Add JUnit tests for `EquityLoader.returnQuarter()`, P&L calculations

6. **Exception Swallowing**  
   - Catch blocks print to stdout, don't propagate
   - **Suggestion:** Use checked exceptions + proper stack trace logging

7. **Security Validation**  
   - Only checks for empty fields
   - **Suggestion:** Validate date formats, price ranges, quantity boundaries

---

## Technologies

| Component       | Technology           | Version |
|-----------------|----------------------|---------|
| Language        | Java                 | 8+      |
| Excel Parsing   | Apache POI           | 4.x+    |
| Logging         | Apache Log4j2        | 2.x+    |
| Build Tool      | (Likely) Maven/Gradle| —       |

---

## Running the Application

### Prerequisites
- Java 8+
- Excel config files in `./configuration/` folder

### Command

```bash
java -cp .:./lib/* bootstrap.InvestingHurdleBootstrapper
```

### Expected Output
```
WELCOME TO THE INVESTING WORLD...

$$$$$$$$$********  STCG  ********$$$$$$$$$
Full Value of consideration: ₹X,XXX
Cost of acquisition: ₹X,XXX
STCG = ₹X,XXX
STCG total: ₹X,XXX
STCG Q1 = ₹X,XXX
...

END
```

---

## Future Roadmap

🔄 **v2.0 Enhancements**
- [ ] Web interface (Spring Boot + React)
- [ ] Database persistence (PostgreSQL)
- [ ] Multi-year tax reports
- [ ] Dividend tracking integration
- [ ] ITR schedule auto-fill

---

## Repository

**GitHub:** [Ajay3007/TaxHrd](https://github.com/Ajay3007/TaxHrd)

---

## Summary

TaxHrd is a **focused, single-purpose financial tool** that solves a real pain point: automating tax calculations for Indian equity traders. While it has room for refactoring (hardcoded dates, missing exports), its core logic is sound and demonstrates strong understanding of:
- Financial transaction modeling
- Date-based categorization logic
- Java best practices (logging, custom exceptions, thread safety)
- Real-world Excel integration

**Ideal for:** Individual traders, small trading collectives, or as a proof-of-concept for a larger tax automation platform.
