---
title: "Quickref"
description: "Tax Hurdle — Quick Reference Guide Fast lookup guide for key concepts, commands, and resources."
domain: finance
order: 99
ownHeader: true
url: /learning/finance/tax_hurdle/quickref/
---

# Tax Hurdle — Quick Reference Guide

**Fast lookup guide for key concepts, commands, and resources.**

---

## 🎯 Quick Navigation

- **[Project Facts](#-project-facts)**
- **[Financial Concepts](#-financial-concepts)**
- **[File Structure](#-file-structure)**
- **[Design Patterns](#-design-patterns)**
- **[Commands](#-commands)**
- **[Resources](#-resources)**

---

## 📊 Project Facts

**Language:** Java 8+  
**Purpose:** STCG calculation automation  
**Input:** Excel files (.xlsx)  
**Output:** Console reports + Log files  
**Repository:** [Ajay3007/tax_hurdle](https://github.com/Ajay3007/tax_hurdle)  
**Status:** Production-ready (v1.0)  

---

## 💰 Financial Concepts

### STCG (Short-Term Capital Gains)
- Profit on shares held **>24 hours but <1 year**
- Taxed as **ordinary income** in India
- Reported in **Schedule CG of ITR-2**

### Indian Financial Year
- **Period:** April 1 – March 31
- **Q1:** Apr 1 – Jun 15
- **Q2:** Jun 16 – Sep 15
- **Q3:** Sep 16 – Dec 15
- **Q4:** Dec 16 – Mar 15
- **Q5:** Mar 16 – Mar 31

### FIFO Method
**First-In-First-Out** cost basis matching:
- Match oldest buys against newer sells
- Standard method for P&L calculation
- Essential for tax compliance

---

## 📁 File Structure

```
src/
├── bootstrap/        # InvestingHurdleBootstrapper (Singleton)
├── params/          # WorkbookLoader, EquityLoader
├── security/        # Security DAO
├── logging/         # HurdleLogger (Log4j2)
├── util/            # HurdleConstant
└── exception/       # InvalidSecurityException

configuration/      # Input Excel files
logs/              # Output log files
lib/               # Dependencies (POI, Log4j2)
```

---

## 🏛️ Design Patterns

| Pattern | Class | Purpose |
|---------|-------|---------|
| **Singleton** | InvestingHurdleBootstrapper | Single app instance |
| **Factory** | WorkbookLoader | Create Security objects |
| **Queue** | ConcurrentLinkedQueue | FIFO trade processing |
| **Strategy** | Tax calculation logic | STCG vs Intraday |

---

## 🔴 Critical Issues

| Issue | Location | Severity |
|-------|----------|----------|
| Empty `setAveragePrices()` | WorkbookLoader | 🔴 HIGH |
| Hardcoded quarter dates | EquityLoader | 🔴 HIGH |
| No unit tests | Entire project | 🔴 HIGH |
| Exception swallowing | All loaders | 🟡 MEDIUM |
| Static file paths | HurdleConstant | 🟡 MEDIUM |

---

## ⚡ Commands

### Clone Repository
```bash
git clone https://github.com/Ajay3007/tax_hurdle.git
cd tax_hurdle
```

### Build
```bash
mvn clean package
# OR
gradle build
```

### Run
```bash
java -cp lib/*:src bootstrap.InvestingHurdleBootstrapper
```

### Compile
```bash
javac -cp lib/*:src src/**/*.java
```

---

## 🔗 Resources

**Documentation:**
- [Project Summary](/learning/finance/tax_hurdle/summary)
- [Technical Analysis](/learning/finance/tax_hurdle/technical-analysis)
- [Refactoring Guide](/learning/finance/tax_hurdle/refactoring-guide)

**External:**
- [Apache POI](https://poi.apache.org/)
- [Log4j2](https://logging.apache.org/log4j/2.x/)
- [Indian Tax System](https://www.incometaxindia.gov.in/)
- [GitHub Repository](https://github.com/Ajay3007/tax_hurdle)

---

**Quick Ref Version:** 1.0  
**Last Updated:** December 31, 2025

← [Back to Hub]()
