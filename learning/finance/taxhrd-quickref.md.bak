# TaxHrd Quick Reference Card

**One-page cheat sheet for TaxHrd project.**

---

## 🎯 What is TaxHrd?

**Java app** → Reads Excel trading data → **Calculates STCG taxes** (quarterly breakdown)

**Use:** Indian equity traders filing income tax returns (ITR)

---

## 📂 Core Components

| Class | Role |
|-------|------|
| `InvestingHurdleBootstrapper` | Entry point (Singleton) |
| `WorkbookLoader` | Parse Excel files |
| `EquityLoader` | Calculate STCG by quarter |
| `Security` | Trade record model |
| `HurdleLogger` | Logging setup (Log4j2) |
| `HurdleConstant` | File paths |
| `InvalidSecurityException` | Custom validation error |

---

## 📊 Financial Quarters (Apr-Mar FY)

```
Q1: Apr 1 — Jun 15    (Opening)
Q2: Jun 16 — Sep 15   (Mid-year)
Q3: Sep 16 — Dec 15   (December deadline)
Q4: Dec 16 — Mar 15   (Pre-close)
Q5: Mar 16 — Mar 31   (Year-end)
```

---

## 💰 Key Formulas

**STCG = Sell Value - Buy Value** (for holdings >24 hours)

**Total STCG = Sum(Q1 + Q2 + Q3 + Q4 + Q5)**

**Intraday Turnover = Sum(Buy Value + Sell Value)**

---

## 🔴 Top 3 Issues to Fix

| Priority | Issue | Fix | Impact |
|----------|-------|-----|--------|
| P1 | Empty `setAveragePrices()` | Implement FIFO | P&L accuracy |
| P1 | Hardcoded quarters | Externalize config | Multi-year support |
| P1 | Exception swallowing | Proper logging | Debugging |

---

## 🚀 Quick Implementation Path

```
Week 1: Critical fixes
  ├─ FIFO cost basis (4h)
  ├─ LocalDate migration (3h)
  └─ Exception handling (4h)

Week 2: Configuration
  ├─ Quarter externalization (2h)
  ├─ File path parameters (2h)
  └─ Input validation (3h)

Week 3: Testing
  ├─ Unit tests (6h)
  ├─ Export functionality (3h)
  └─ Code review (2h)
```

---

## 💻 Running the App

```bash
# Build
javac -cp lib/*:src src/**/*.java

# Run
java -cp lib/*:src bootstrap.InvestingHurdleBootstrapper

# Output
# → Console report with STCG by quarter
# → logs/InvestingHurdle.log file
```

---

## 📁 Input Files Needed

```
configuration/
├── configuration_stock.xlsx
│   ├── Buy sheet (columns: Security, Date, Price, Qty, LTP)
│   └── Sell sheet (same columns)
└── tax_2122_.xlsx
    └── Equities sheet (rows 25-297)
```

---

## 📊 Design Patterns Used

1. **Singleton** → Single app instance
2. **Factory** → Create Security objects
3. **Queue** → FIFO trade processing
4. **Logging** → Log4j2 wrapper

---

## 🧪 Testing Essentials

**Must test:**
- Quarter mapping (boundary dates)
- FIFO matching (cost basis)
- Exception handling (invalid data)
- P&L calculations

**Target:** 80%+ coverage

---

## 🔑 Key Classes (Methods)

```java
// Bootstrap
getInstance()           // Singleton access
main(args)             // Entry point

// Loaders
loadBuys()             // Parse buy sheet
loadSells()            // Parse sell sheet
calculateSTCG()        // Aggregate STCG

// Utilities
returnQuarter(date)    // Date to quarter (1-5)
getLogger()            // Get Log4j2 logger
validate(security)     // Input validation
```

---

## 📚 Documentation Files

| Document | Purpose | Time |
|----------|---------|------|
| **Summary** | Quick overview | 5-10 min |
| **Technical** | Architecture deep-dive | 20-30 min |
| **Refactoring** | Improvement guide | 15-20 min |
| **Portfolio** | Showcase | 8-12 min |
| **Hub** | Navigation guide | 5 min |

---

## ⚠️ Known Limitations

❌ Quarter dates hardcoded (single FY only)  
❌ No FIFO cost basis calculation  
❌ Console output only (no export)  
❌ Static file paths (no CLI args)  
❌ No unit tests  
❌ Generic exception handling  

---

## 🎯 Success Metrics

✅ FIFO implemented & tested  
✅ 80%+ test coverage  
✅ Exception handling fixed  
✅ Config externalized  
✅ Documentation complete  
✅ Export functionality added  

---

## 📞 Quick Links

- **Refactoring Guide:** [Code improvements](taxhrd-refactoring-guide.md)
- **Technical Analysis:** [Architecture](taxhrd-technical-analysis.md)
- **Documentation Hub:** [All docs](index.md)
- **GitHub:** [Repository](https://github.com/Ajay3007/TaxHrd)

---

## 🚦 Next Steps

1. [ ] Read technical analysis (patterns)
2. [ ] Study refactoring guide (P1 items)
3. [ ] Set up test framework
4. [ ] Implement FIFO matching
5. [ ] Add comprehensive tests

---

## 🎓 Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Java 8+ |
| Excel | Apache POI |
| Logging | Log4j2 |
| Testing | JUnit 4/5 (future) |
| Build | Maven/Gradle (likely) |

---

## 💡 STCG Calculation Steps

```
1. Read Excel (buy/sell transactions)
2. Create Security objects
3. Identify holding period
4. If holding >24h → STCG
5. Map to quarter (sale date)
6. Sum STCG per quarter
7. Generate report
```

---

## 📊 Architecture (90-second version)

```
Excel Files
    ↓ [WorkbookLoader]
Security Objects
    ↓ [EquityLoader]
Quarter Buckets
    ↓ [Report Generator]
Console + Log Output
```

---

## 🎯 Priority Matrix

```
        High Effort
           ↑
           │
H   ├─────────────┤
i   │  3 Long-term│ 2 Quick wins
g   ├─────────────┤
h   │  4 Deferred │ 1 Critical
    │             │
I   └─────────────→ Low Effort
m       P1  P2  P3
p
a
c
t

P1 (Critical): Fix bugs → High impact, varies effort
P2 (Important): Improve → Medium impact, medium effort
P3 (Enhancement): Nice-to-have → Low impact, varies
```

---

## 🔧 Common Tasks

### Add New Validation
```java
// 1. Add check in parseRow()
if (value < 0) {
    throw new InvalidSecurityException("Value must be positive");
}

// 2. Add unit test
@Test(expected = InvalidSecurityException.class)
public void testValidation_Negative() { ... }
```

### Add Export Format
```java
// 1. Add method to ReportExporter
public void exportToXML(String path, TaxReport report) { ... }

// 2. Test the format
@Test public void testExportXML() { ... }
```

### Add Quarter Rule
```java
// 1. Update QuarterConfig
QUARTERS.put(6, new DateRange(...));

// 2. Test new quarter
@Test public void testReturnQuarter_Q6() { ... }
```

---

## ⏰ Time Estimates

| Task | Hours | When |
|------|-------|------|
| FIFO | 4-6 | Week 1 |
| LocalDate | 3-4 | Week 1 |
| Exceptions | 4-5 | Week 1 |
| Config | 2-3 | Week 2 |
| Validation | 3-4 | Week 2 |
| Tests | 6-8 | Week 3 |
| Export | 3-4 | Week 3 |

**Total:** ~28-34 hours (4 weeks @ 8h/week)

---

## 🎓 What You'll Learn

✅ Tax calculation logic  
✅ FIFO matching algorithm  
✅ Excel parsing (POI)  
✅ Design patterns  
✅ Exception handling  
✅ Unit testing  
✅ Logging frameworks  
✅ Java best practices  

---

## 🏁 Ready?

1. **Pick a document:** [Hub](index.md)
2. **Start implementing:** [Refactoring Guide](taxhrd-refactoring-guide.md)
3. **Track progress:** [Checklist](taxhrd-checklist.md)
4. **Ask questions:** [GitHub Issues](https://github.com/Ajay3007/TaxHrd/issues)

---

**Version:** 1.0 | **Last Updated:** Jan 2025 | **Status:** Ready to use

Print this card. 📌 Post it above your desk. 🚀 Start coding!
