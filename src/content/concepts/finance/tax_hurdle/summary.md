---
title: "Summary"
description: "Tax Hurdle Project — Complete Summary & Documentation A consolidated reference guide for the Tax Hurdle investment tax calculation system."
domain: finance
order: 99
ownHeader: true
url: /learning/finance/tax_hurdle/summary/
---

# Tax Hurdle Project — Complete Summary & Documentation

**A consolidated reference guide for the Tax Hurdle investment tax calculation system.**

---

## 📑 Quick Navigation

- **[Executive Summary](#-executive-summary)**
- **[Project Overview](#-project-overview)**
- **[Key Documents](#-key-documents)**
- **[Quick Start](#-quick-start)**
- **[Project Structure](#-project-structure)**
- **[Core Concepts](#-core-concepts)**
- **[Implementation Status](#-implementation-status)**
- **[Next Steps](#-next-steps)**

---

## 🎯 Executive Summary

**Tax Hurdle** is a specialized **Java application for automating tax calculations** in equity trading. It reads Excel files with buy/sell transaction data and produces **quarter-wise Short-Term Capital Gains (STCG) reports** for Indian tax filing.

### Key Facts

| Aspect | Details |
|--------|---------|
| **Language** | Java 8+ |
| **Purpose** | STCG calculation automation |
| **Input** | Excel files (.xlsx) |
| **Output** | Console reports + Log files |
| **Primary User** | Individual equity traders, CAs |
| **Geographic Focus** | India (April-March financial year) |
| **Repository** | [Ajay3007/tax_hurdle](https://github.com/Ajay3007/tax_hurdle) |
| **Status** | Production-ready (v1.0) with improvement opportunities |

### Current Capabilities

✅ Parses Excel buy/sell transactions  
✅ Categorizes trades as STCG or intraday  
✅ Calculates quarter-wise STCG breakdown  
✅ Tracks profit/loss per security  
✅ Logs all operations with Apache Log4j2  
✅ Thread-safe data processing  

### Known Limitations

⚠️ Hardcoded quarter dates (single FY only)  
⚠️ Empty `setAveragePrices()` method  
⚠️ Console output only (no export)  
⚠️ Static file paths  
⚠️ Limited input validation  
⚠️ No unit tests  

---

## 📊 Project Overview

### What is STCG?

**Short-Term Capital Gains** = Profit on shares held **>24 hours** before selling

For Indian tax:
- Taxed as **ordinary income** (added to salary for bracket calculation)
- Must be reported in **Schedule CG of ITR-2**
- Separate from long-term gains (held >1 year, indexed)

**Financial Year:** April 1 – March 31

**Quarter Breakdown:**
- Q1: Apr 1 – Jun 15
- Q2: Jun 16 – Sep 15
- Q3: Sep 16 – Dec 15
- Q4: Dec 16 – Mar 15
- Q5: Mar 16 – Mar 31 (closing period)

---

## 📚 Key Documents

### 1. **Project Summary** (This Document)
One-page comprehensive reference with all key information.

### 2. **Technical Architecture Guide**
[technical-analysis.md](/learning/finance/tax_hurdle/technical-analysis) — Deep dive into:
- System architecture
- Design patterns (4 patterns analyzed)
- Code quality assessment
- Line-by-line walkthroughs
- Testing strategy

### 3. **Refactoring Guide**
[refactoring-guide.md](/learning/finance/tax_hurdle/refactoring-guide) — Step-by-step improvements:
- Priority 1: Critical issues
- Priority 2: Important improvements
- Priority 3: Enhancements
- Before/after code examples

### 4. **Quick Reference**
[quickref.md](/learning/finance/tax_hurdle/quickref) — One-page cheat sheet with key commands and concepts

### 5. **Implementation Checklist**
[checklist.md](/learning/finance/tax_hurdle/checklist) — Track progress on improvements

---

## 🚀 Quick Start

### Prerequisites
- Java 8 or higher
- Apache POI (Excel library)
- Log4j2 (Logging)
- Excel files with trading data

### Installation

```bash
# Clone repository
git clone https://github.com/Ajay3007/tax_hurdle.git
cd tax_hurdle

# Build (if Maven/Gradle configured)
mvn clean package
# OR
gradle build

# Prepare Excel files
mkdir -p configuration
# Place configuration_stock.xlsx and tax_2122_.xlsx in configuration/
```

### Running

```bash
# Compile
javac -cp lib/*:src src/**/*.java

# Run
java -cp lib/*:src bootstrap.InvestingHurdleBootstrapper
```

---

## 📁 Project Structure

```
Tax Hurdle/
│
├── src/
│   ├── bootstrap/
│   │   └── InvestingHurdleBootstrapper.java
│   ├── params/
│   │   ├── WorkbookLoader.java
│   │   └── EquityLoader.java
│   ├── security/
│   │   └── Security.java
│   ├── logging/
│   │   └── HurdleLogger.java
│   ├── util/
│   │   └── HurdleConstant.java
│   └── exception/
│       └── InvalidSecurityException.java
│
├── configuration/
│   ├── configuration_stock.xlsx
│   └── tax_2122_.xlsx
│
├── logs/
│   └── InvestingHurdle.log
│
└── lib/
    ├── poi-4.1.2.jar
    └── log4j2-2.13.3.jar
```

---

## 💡 Core Concepts

### 1. Financial Year (FY)
Indian FY: **April 1 – March 31**

### 2. STCG vs. Intraday

| Aspect | STCG | Intraday |
|--------|------|----------|
| **Holding** | >24 hours | Same day |
| **Tax Type** | Capital gains | Ordinary income |
| **ITR Schedule** | CG | Business Income |

### 3. Quarter Allocation
Transactions segregated by quarter based on **sale date**

### 4. FIFO (First-In-First-Out)
Cost basis matching method that matches oldest buys against newer sells

### 5. P&L Calculation
**Profit/Loss = (Sell Price – Average Cost) × Quantity**

---

## 📈 Implementation Status

### Completed Features ✅
- ✅ Excel parsing (buy/sell)
- ✅ STCG aggregation
- ✅ Intraday tracking
- ✅ Logging setup
- ✅ Thread safety
- ✅ P&L tracking

### In-Progress / TODO 🔄
- ⏳ FIFO cost matching
- ⏳ Unit tests
- ⏳ Exception refactoring
- ⏳ LocalDate migration
- ⏳ Config externalization

---

## 🎓 Learning Resources

### Included Documentation
1. Project summary
2. Technical analysis
3. Refactoring guide
4. Quick reference
5. Implementation checklist

### External Resources
- **Apache POI:** https://poi.apache.org/
- **Log4j2:** https://logging.apache.org/log4j/2.x/
- **Indian Tax System:** https://www.incometaxindia.gov.in/
- **NSE India:** https://www.nseindia.com/

---

## 🏁 Conclusion

**Tax Hurdle** is a well-structured, production-ready Java application with strong fundamentals demonstrating:

✅ Solid design patterns  
✅ Good separation of concerns  
✅ Proper logging & error handling  
✅ Thread-safe data structures  

**Opportunities for improvement** are documented for future enhancement. Excellent portfolio piece for financial software development.

---

**Document Version:** 1.0  
**Last Updated:** December 31, 2025  
**Status:** Complete  

← [Back to Hub]()  |  [Next: Technical Analysis →](/learning/finance/tax_hurdle/technical-analysis)
