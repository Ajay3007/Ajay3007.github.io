# TaxHrd — Investment Tax Calculator

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Java Version](https://img.shields.io/badge/Java-8%2B-orange.svg)](https://java.com)

**Automated Short-Term Capital Gains (STCG) calculation system for Indian equity traders**

## 📋 What is TaxHrd?

TaxHrd is a **Java-based financial application** that automates tax calculations for equity trading. It reads Excel files containing buy/sell transactions and:

- ✅ Calculates **STCG (Short-Term Capital Gains)** for shares held >24 hours
- ✅ Segregates **intraday trades** separately 
- ✅ Breaks down STCG by **financial quarters** (Apr-Mar financial year)
- ✅ Generates **profit/loss summaries** per security
- ✅ Logs all operations with **Apache Log4j2**

**Use Case:** Prepare accurate tax reports for CA (Chartered Accountant) filing during Indian Income Tax Return (ITR) submission.

---

## 🎯 Quick Start

### Prerequisites
- **Java 8+** installed
- **Excel files** (`.xlsx`) with trading data in `./configuration/` folder

### Usage

```bash
java -cp .:./lib/* bootstrap.InvestingHurdleBootstrapper
```

### Input Files Required

1. **`configuration_stock.xlsx`**
   - Sheets: "Buy", "Sell"
   - Columns: Security Name, Date, Price, Quantity, LTP (Last Traded Price)

2. **`tax_2122_.xlsx`**
   - Sheet: "Equities"
   - Rows 25–297 with transaction details

### Output

Console report:
```
$$$$  STCG Summary  $$$$
Full Value of consideration: ₹X,XXX
Cost of acquisition: ₹X,XXX
STCG = ₹X,XXX

STCG by Quarter:
Q1: ₹X,XXX | Q2: ₹X,XXX | Q3: ₹X,XXX | Q4: ₹X,XXX | Q5: ₹X,XXX
```

Log file: `./logs/InvestingHurdle.log`

---

## 📊 Financial Concepts

### What is STCG?

**Short-Term Capital Gains** = Profit/Loss on shares held >24 hours before selling

For Indian tax purposes:
- **STCG = Sale Price – Purchase Price**
- Taxed as **ordinary income** (added to salary for tax bracket calculation)
- Must be reported in **ITR-2 (Capital Gains Schedule)**
- Different from long-term capital gains (held >365 days)

### Financial Year Quarters

TaxHrd segments STCG by Indian financial quarters:

| Quarter | Period           | Typical Reporting |
|---------|-----------------|-------------------|
| Q1      | Apr 1 – Jun 15  | First estimate    |
| Q2      | Jun 16 – Sep 15 | Mid-year review   |
| Q3      | Sep 16 – Dec 15 | December deadline |
| Q4      | Dec 16 – Mar 15 | Pre-close review  |
| Q5      | Mar 16 – Mar 31 | Year-end closure  |

### Intraday vs STCG

| Category    | Holding Period | Tax Classification |
|-------------|----------------|--------------------|
| **Intraday**| Same day       | Business income    |
| **STCG**    | >24 hours      | Capital gains      |
| **LTCG**    | >1 year        | Long-term capital gains (indexed) |

---

## 🏗️ Architecture

### Package Structure

```
src/
├── bootstrap/
│   └── InvestingHurdleBootstrapper      # Entry point (Singleton)
├── params/
│   ├── WorkbookLoader                   # Excel parser
│   └── EquityLoader                     # STCG calculator
├── security/
│   └── Security                         # Trade record model
├── logging/
│   └── HurdleLogger                     # Log4j2 wrapper
├── util/
│   └── HurdleConstant                   # File path constants
└── exception/
    └── InvalidSecurityException          # Custom validation exception
```

### Key Components

| Class | Responsibility | Key Methods |
|-------|-----------------|-------------|
| **InvestingHurdleBootstrapper** | Orchestrates entire flow | `main()`, `getInstance()` |
| **WorkbookLoader** | Parses Excel files | `loadBuys()`, `loadSells()` |
| **EquityLoader** | Calculates tax metrics | `calculateSTCG()`, `returnQuarter()` |
| **Security** | Trade record DAO | Getters/setters for trade details |
| **HurdleLogger** | Logging setup | `getLogger()`, `setupLogger()` |

### Data Flow

```
Excel Files (Buy/Sell)
    ↓
WorkbookLoader (Parse)
    ↓
Security Objects (Model)
    ↓
EquityLoader (Calculate)
    ↓
Report Output + Log4j2
```

---

## 💡 Core Features

### 1. **Multi-File Processing**
- Reads both configuration and tax Excel files
- Handles multiple sheets (Buy, Sell, Equities)
- Robust null checking and type casting

### 2. **Trade Categorization**
- Automatically classifies trades as STCG or intraday
- Tracks buy/sell value per security
- Calculates P&L per transaction

### 3. **Quarter-Wise Aggregation**
- Maps transaction dates to quarters automatically
- Sums STCG across all securities per quarter
- Tracks total turnover for speculation trades

### 4. **Thread-Safe Storage**
- `ConcurrentHashMap<String, Queue<Security>>` for security data
- Supports multi-threaded access
- No race conditions on shared state

### 5. **Comprehensive Logging**
```properties
# Log4j2 Configuration
- Console output (INFO level)
- File output (DEBUG level)
- Rolling appender (10KB per file, 5 backups)
- Timestamp + thread info
```

---

## 🔧 Code Examples

### Load Buy Transactions

```java
WorkbookLoader loader = new WorkbookLoader();
loader.loadBuys(); // Reads "Buy" sheet from configuration_stock.xlsx
// Populates: securityMap.put("TCS", Queue<Security with buy details>)
```

### Calculate STCG by Quarter

```java
EquityLoader equityLoader = new EquityLoader();
Map<Integer, Double> stcgByQuarter = equityLoader.calculateSTCG();
// Returns: {1: 5000, 2: 15000, 3: 8000, 4: 12000, 5: 3000}
```

### Determine Quarter from Date

```java
Date tradeDate = new SimpleDateFormat("dd-MMM-yy").parse("25-Jun-2021");
int quarter = equityLoader.returnQuarter(tradeDate);
// Returns: 2 (Jun 16 – Sep 15)
```

---

## ⚠️ Known Limitations & Improvements

| Issue | Severity | Suggestion |
|-------|----------|-----------|
| Hardcoded quarter dates | 🟡 Medium | Externalize to config file |
| `setAveragePrices()` empty | 🟡 Medium | Implement FIFO/LIFO matching |
| Console output only | 🟠 Low | Add CSV/PDF export |
| Static file paths | 🟡 Medium | Accept CLI arguments |
| No unit tests | 🔴 High | Add JUnit tests |
| Exception swallowing | 🟡 Medium | Log and propagate exceptions |
| Limited validation | 🟡 Medium | Validate price ranges, date formats |

### Future Enhancements

- [ ] Spring Boot REST API
- [ ] Database persistence (PostgreSQL)
- [ ] Multi-year tax reports
- [ ] Dividend tracking
- [ ] Mutual fund support
- [ ] ITR schedule auto-generation
- [ ] CSV import/export

---

## 📦 Dependencies

```xml
<!-- Excel Parsing -->
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>4.1.2</version>
</dependency>

<!-- Logging -->
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-core</artifactId>
    <version>2.13.3</version>
</dependency>
```

---

## 📄 Configuration

### File Structure

```
TaxHrd/
├── src/
│   ├── bootstrap/
│   ├── params/
│   ├── security/
│   ├── logging/
│   ├── util/
│   └── exception/
├── configuration/
│   ├── configuration_stock.xlsx     ← Input: Buy/Sell trades
│   └── tax_2122_.xlsx               ← Input: Equity data
├── logs/
│   └── InvestingHurdle.log          ← Output: Log file
└── lib/
    ├── poi-*.jar
    └── log4j2-*.jar
```

### Environment Setup

```bash
# Set classpath
export CLASSPATH=.:./lib/poi-4.1.2.jar:./lib/log4j2-core-2.13.3.jar:./lib/log4j2-api-2.13.3.jar

# Run application
java bootstrap.InvestingHurdleBootstrapper
```

---

## 🧪 Testing

Currently, the project lacks unit tests. Recommended additions:

```java
@Test
public void testReturnQuarter() {
    Date q1Date = new SimpleDateFormat("dd-MMM-yy").parse("15-May-2021");
    assertEquals(1, equityLoader.returnQuarter(q1Date));
}

@Test
public void testInvalidSecurityException() {
    assertThrows(InvalidSecurityException.class, () -> {
        loader.validateSecurity(null);
    });
}
```

---

## 📚 Learning Resources

- **Apache POI Docs:** https://poi.apache.org/
- **Log4j2 Guide:** https://logging.apache.org/log4j/2.x/
- **Indian Tax (ITR):** https://www.incometaxindia.gov.in/
- **Stock Market Basics:** https://www.nseindia.com/ (NSE India)

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m "Add feature"`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ajay Gupta**  
GitHub: [@Ajay3007](https://github.com/Ajay3007)  
Portfolio: [ajay3007.github.io](https://ajay3007.github.io)

---

## 📞 Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/Ajay3007/TaxHrd/issues)
- Contact via GitHub

---

**Last Updated:** January 2025  
**Version:** 1.0.0
