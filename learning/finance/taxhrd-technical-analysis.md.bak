# TaxHrd — Technical Architecture & Code Analysis

**Deep dive into design patterns, implementation details, and code quality assessment.**

---

## 📐 System Architecture

### Component Diagram

```
┌─────────────────────────────────────────────────────┐
│       InvestingHurdleBootstrapper (Singleton)        │
│         • main() - entry point                       │
│         • getInstance() - singleton instance         │
│         • reporterTesting() - output generation      │
└─────────────┬───────────────────────────┬───────────┘
              │                           │
              ├──────────────┐            ├─────────────────┐
              │              │            │                 │
        ┌─────▼──────┐  ┌───▼────────┐  ┌─▼──────────┐  ┌──▼──────────┐
        │WorkbookLoader│  │EquityLoader│  │HurdleLogger│  │HurdleConstant│
        │  • loadBuys() │  │•calculateSTC│  │•getLogger()│  │•PATHS       │
        │  • loadSells()│  │•returnQtr() │  │•setupLog() │  │•FILE_NAMES  │
        └─────┬────────┘  └───┬────────┘  └────────────┘  └─────────────┘
              │                │
              └────────┬───────┘
                       │
              ┌────────▼────────┐
              │  Security DAO   │
              │  • getter/setter│
              │  • P&L compute  │
              └─────────────────┘
              
       ConcurrentHashMap<String, Queue<Security>>
       (Thread-safe security storage)
```

---

## 🏛️ Design Patterns

### 1. **Singleton Pattern** — InvestingHurdleBootstrapper

**Purpose:** Ensure single instance of bootstrap throughout application lifecycle.

**Implementation:**
```java
public class InvestingHurdleBootstrapper {
    private static InvestingHurdleBootstrapper instance;
    private static final Object lock = new Object();
    
    public static InvestingHurdleBootstrapper getInstance() {
        if (instance == null) {
            synchronized(lock) {
                if (instance == null) {
                    instance = new InvestingHurdleBootstrapper();
                }
            }
        }
        return instance;
    }
}
```

**Benefits:**
✅ Single application state  
✅ Centralized loader initialization  
✅ Global access point  
✅ Thread-safe with double-checked locking  

**Drawbacks:**
⚠️ Hard to test (static methods)  
⚠️ Global mutable state  
⚠️ Difficult to mock dependencies  

---

### 2. **Factory Pattern** — Security Object Creation

**Purpose:** Encapsulate creation of trade record objects.

**Implementation:**
```java
// In WorkbookLoader
Security security = new Security();
security.setSecurityName(row.getCell(0).getStringCellValue());
security.setBuyDate(row.getCell(1).getDateCellValue());
security.setBuyPrice(row.getCell(2).getNumericCellValue());
// ... returns fully initialized Security object
```

**Benefits:**
✅ Centralized object creation  
✅ Validation logic in one place  
✅ Easy to add computed fields  

**Recommendation:** Use builder pattern for complex objects.

---

### 3. **Queue Pattern** — FIFO Trade Processing

**Purpose:** Process buy/sell transactions in chronological order.

**Implementation:**
```java
// ConcurrentHashMap of queues per company
private ConcurrentHashMap<String, Queue<Security>> securityMap = 
    new ConcurrentHashMap<>();

// Add to queue
securityMap.computeIfAbsent(securityName, k -> new ConcurrentLinkedQueue<>())
           .offer(security);

// Retrieve in FIFO order
Queue<Security> trades = securityMap.get("TCS");
Security nextTrade = trades.poll(); // FIFO
```

**Benefits:**
✅ Chronological order preserved  
✅ Natural match logic (FIFO)  
✅ Thread-safe with ConcurrentLinkedQueue  

---

### 4. **Strategy Pattern** — Tax Calculation

**Purpose:** Different calculation strategies for STCG vs. intraday.

**Current Implementation (Implicit):**
```java
if (holdingPeriod > 1 day) {
    // STCG strategy
    calculateSTCG(security);
} else {
    // Intraday strategy
    calculateIntraday(security);
}
```

**Recommendation:** Explicit strategy interface:
```java
interface TaxCalculationStrategy {
    double calculate(Security security);
}

class STCGStrategy implements TaxCalculationStrategy {
    @Override
    public double calculate(Security security) {
        return security.getSellValue() - security.getBuyValue();
    }
}

class IntradayStrategy implements TaxCalculationStrategy {
    @Override
    public double calculate(Security security) {
        return security.getTurnover();
    }
}
```

---

## 📊 Data Flow & Processing Pipeline

### Step 1: Excel Parsing (WorkbookLoader)

```
configuration_stock.xlsx
    ↓ [Read "Buy" sheet]
    ├─ Extract: Security, Date, Price, Quantity, LTP
    ├─ Validate: Non-null fields, numeric types
    ├─ Create Security objects
    └─ Store in securityMap["TCS"] → Queue
    
    ↓ [Read "Sell" sheet]
    ├─ Match with existing buys (FIFO)
    ├─ Calculate holding period
    ├─ Update P&L
    └─ Store in securityMap["TCS"] → Queue
```

### Step 2: Tax Calculation (EquityLoader)

```
tax_2122_.xlsx (Equities sheet, rows 25-297)
    ↓ [Per row]
    ├─ Extract transaction date
    ├─ Call returnQuarter(date)
    ├─ Categorize as STCG or intraday
    ├─ Aggregate to quarter buckets
    └─ Sum totals
    
    ↓ [Results]
    └─ Map<Integer, Double> stcgByQuarter
       {1: 5000, 2: 15000, 3: 8000, 4: 12000, 5: 3000}
```

### Step 3: Report Generation

```
consolidatedResults()
    ├─ Print STCG Summary
    │  ├─ Full consideration value
    │  ├─ Cost of acquisition
    │  └─ STCG = difference
    │
    ├─ Print Quarter Breakdown
    │  ├─ Q1, Q2, Q3, Q4, Q5
    │  └─ Total STCG
    │
    └─ Print Intraday Summary
       ├─ Buy value
       ├─ Sell value
       └─ Total turnover
```

---

## 🔍 Code Quality Analysis

### Strengths ✅

| Aspect | Evidence |
|--------|----------|
| **Error Handling** | Custom `InvalidSecurityException` for validation failures |
| **Logging** | Comprehensive Log4j2 setup with file rotation |
| **Thread Safety** | `ConcurrentHashMap` + `ConcurrentLinkedQueue` for shared state |
| **Encapsulation** | Private members, public getters/setters in `Security` class |
| **Separation of Concerns** | Distinct packages for bootstrap, params, logging, util |
| **Constants Management** | `HurdleConstant` class for file paths |
| **Code Organization** | Logical package structure following domain model |

### Weaknesses ⚠️

| Issue | Impact | Location | Severity |
|-------|--------|----------|----------|
| **Hardcoded Quarter Dates** | Only works for FY 2021-22 | `EquityLoader.returnQuarter()` | 🔴 HIGH |
| **Empty `setAveragePrices()`** | Average cost basis not calculated | `WorkbookLoader` | 🔴 HIGH |
| **No Unit Tests** | No test coverage | Entire project | 🔴 HIGH |
| **Exception Swallowing** | Errors lost in `catch(Exception e)` blocks | `WorkbookLoader`, `EquityLoader` | 🟡 MEDIUM |
| **Static File Paths** | No configuration flexibility | `HurdleConstant` | 🟡 MEDIUM |
| **Console-Only Output** | No CSV/JSON export | `consolidatedResults()` | 🟠 LOW |
| **Limited Validation** | No range checks on prices | `WorkbookLoader` | 🟡 MEDIUM |
| **Tight Coupling** | Loaders depend on specific sheet names | `WorkbookLoader` | 🟡 MEDIUM |

---

## 📋 Detailed Code Walkthrough

### WorkbookLoader — Excel Parser

**Responsibility:** Read Excel files, create Security objects

**Key Methods:**

#### `loadBuys()`
```java
public void loadBuys() {
    try {
        FileInputStream fis = new FileInputStream(HurdleConstant.CONFIGURATION_PATH);
        XSSFWorkbook workbook = new XSSFWorkbook(fis);
        XSSFSheet sheet = workbook.getSheet("Buy");
        
        for (Row row : sheet) {
            String security = row.getCell(0).getStringCellValue();
            Date date = row.getCell(1).getDateCellValue();
            double buyPrice = row.getCell(2).getNumericCellValue();
            int quantity = (int) row.getCell(3).getNumericCellValue();
            double ltp = row.getCell(4).getNumericCellValue();
            
            Security obj = new Security(security, date, buyPrice, quantity, ltp);
            securityMap.computeIfAbsent(security, k -> new ConcurrentLinkedQueue<>())
                       .offer(obj);
        }
    } catch (Exception e) {
        e.printStackTrace(); // ⚠️ Better: log and throw
    }
}
```

**Issues:**
- ❌ Catches generic `Exception` (too broad)
- ❌ `printStackTrace()` instead of proper logging
- ❌ No null checks on cell values
- ❌ Assumes fixed column order (fragile)

**Improvement:**
```java
public void loadBuys() throws InvalidSecurityException, IOException {
    try (FileInputStream fis = new FileInputStream(HurdleConstant.CONFIGURATION_PATH);
         XSSFWorkbook workbook = new XSSFWorkbook(fis)) {
        
        XSSFSheet sheet = workbook.getSheet("Buy");
        if (sheet == null) {
            throw new InvalidSecurityException("'Buy' sheet not found");
        }
        
        for (Row row : sheet) {
            try {
                Security security = parseSecurityRow(row);
                securityMap.computeIfAbsent(security.getSecurityName(), 
                    k -> new ConcurrentLinkedQueue<>()).offer(security);
            } catch (InvalidSecurityException e) {
                HurdleLogger.getLogger().warn("Skipping invalid row: " + e.getMessage());
            }
        }
    } catch (IOException e) {
        HurdleLogger.getLogger().error("Failed to load buy sheet", e);
        throw e;
    }
}

private Security parseSecurityRow(Row row) throws InvalidSecurityException {
    Cell nameCell = row.getCell(0);
    if (nameCell == null || nameCell.getStringCellValue().isEmpty()) {
        throw new InvalidSecurityException("Security name is empty");
    }
    
    // ... validate other cells
    
    return new Security(...);
}
```

---

### EquityLoader — Tax Calculator

**Responsibility:** Calculate STCG by quarter

**Key Method:** `calculateSTCG()`

```java
public Map<Integer, Double> calculateSTCG() {
    Map<Integer, Double> stcgMap = new HashMap<>();
    // Initialize quarters 1-5
    for (int i = 1; i <= 5; i++) {
        stcgMap.put(i, 0.0);
    }
    
    // Read "Equities" sheet from tax file
    FileInputStream fis = new FileInputStream(HurdleConstant.TAX_FILE_PATH);
    XSSFWorkbook workbook = new XSSFWorkbook(fis);
    XSSFSheet sheet = workbook.getSheet("Equities");
    
    // Rows 25-297 contain equity data
    for (int rowNum = 25; rowNum <= 297; rowNum++) {
        Row row = sheet.getRow(rowNum);
        Date saleDate = row.getCell(1).getDateCellValue();
        double stcg = row.getCell(8).getNumericCellValue(); // STCG column
        
        int quarter = returnQuarter(saleDate);
        double currentValue = stcgMap.get(quarter);
        stcgMap.put(quarter, currentValue + stcg);
    }
    
    return stcgMap;
}
```

**Issues:**
- ❌ Hardcoded row numbers (25-297) — fragile
- ❌ Hardcoded column indices — magic numbers
- ❌ No validation of numeric cells
- ❌ Doesn't close resources properly (no try-with-resources)

---

### returnQuarter() — Date to Quarter Mapping

**Purpose:** Map a transaction date to financial quarter

```java
public int returnQuarter(Date date) {
    SimpleDateFormat formatter = new SimpleDateFormat("dd-MMM");
    String dateStr = formatter.format(date);
    
    if (dateStr.compareTo("01-Apr") >= 0 && dateStr.compareTo("15-Jun") <= 0) {
        return 1;
    } else if (dateStr.compareTo("16-Jun") >= 0 && dateStr.compareTo("15-Sep") <= 0) {
        return 2;
    } else if (dateStr.compareTo("16-Sep") >= 0 && dateStr.compareTo("15-Dec") <= 0) {
        return 3;
    } else if (dateStr.compareTo("16-Dec") >= 0 && dateStr.compareTo("15-Mar") <= 0) {
        return 4;
    } else {
        return 5; // Mar 16-31
    }
}
```

**Issues:**
- ❌ Hardcoded dates only work for one year
- ❌ String comparison is fragile (locale-dependent)
- ❌ No handling of year boundaries
- ❌ Inefficient (format + compare every time)

**Improvement:**
```java
public int returnQuarter(LocalDate date) {
    MonthDay monthDay = MonthDay.of(date.getMonth(), date.getDayOfMonth());
    
    if (monthDay.isBefore(MonthDay.of(Month.JUNE, 16))) {
        return 1; // Apr 1 – Jun 15
    } else if (monthDay.isBefore(MonthDay.of(Month.SEPTEMBER, 16))) {
        return 2; // Jun 16 – Sep 15
    } else if (monthDay.isBefore(MonthDay.of(Month.DECEMBER, 16))) {
        return 3; // Sep 16 – Dec 15
    } else if (monthDay.isBefore(MonthDay.of(Month.MARCH, 16))) {
        return 4; // Dec 16 – Mar 15
    } else {
        return 5; // Mar 16 – Mar 31
    }
}
```

**Benefits:**
✅ Year-independent  
✅ Uses `LocalDate` (Java 8+, better than `java.util.Date`)  
✅ Clear comparison logic  
✅ Locale-safe  

---

## 🔐 Thread Safety Analysis

### Current Implementation

```java
private ConcurrentHashMap<String, Queue<Security>> securityMap = 
    new ConcurrentHashMap<>();
```

**Thread-Safe Operations:**
✅ `securityMap.computeIfAbsent()` — atomic operation  
✅ `ConcurrentLinkedQueue.offer()` — thread-safe insertion  
✅ Multiple threads can add to different queues simultaneously  

**Potential Issues:**
⚠️ If reading/writing same queue concurrently:
```java
// Thread 1: Reading
Queue<Security> trades = securityMap.get("TCS");
Security trade = trades.poll(); // Removed from queue

// Thread 2: Checking size
if (trades.size() > 0) { // ← Race condition!
    Security trade2 = trades.poll();
}
```

**Recommendation:** Use atomic references or synchronized blocks for complex operations.

---

## 📈 Performance Considerations

### Time Complexity

| Operation | Complexity | Notes |
|-----------|-----------|-------|
| Load buys | O(n) | n = number of buy rows |
| Load sells | O(n) | n = number of sell rows |
| Calculate STCG | O(m) | m = number of equity rows (273) |
| Find quarter | O(1) | Fixed number of comparisons (5 max) |
| **Overall** | **O(n + m)** | Linear with input size |

### Space Complexity

| Data Structure | Space | Notes |
|---|---|---|
| `securityMap` | O(n) | n = total number of transactions |
| Quarter buckets | O(5) | Fixed 5 quarters |
| **Overall** | **O(n)** | Linear with transactions |

**Optimization Opportunities:**
- Cache formatted dates in `returnQuarter()` (avoid repeated formatting)
- Use `HashMap` instead of `ConcurrentHashMap` if single-threaded
- Stream API for functional aggregation of STCG values

---

## 🧪 Testing Strategy

### Unit Tests Needed

```java
@Test
public void testReturnQuarter_Q1() {
    LocalDate q1Date = LocalDate.of(2021, 5, 15);
    assertEquals(1, equityLoader.returnQuarter(q1Date));
}

@Test
public void testReturnQuarter_Q2() {
    LocalDate q2Date = LocalDate.of(2021, 8, 20);
    assertEquals(2, equityLoader.returnQuarter(q2Date));
}

@Test
public void testReturnQuarter_Q5() {
    LocalDate q5Date = LocalDate.of(2021, 3, 25);
    assertEquals(5, equityLoader.returnQuarter(q5Date));
}

@Test
public void testCalculateSTCG_Sum() {
    // Arrange
    Map<Integer, Double> result = equityLoader.calculateSTCG();
    
    // Assert
    double totalSTCG = result.values().stream()
        .mapToDouble(Double::doubleValue)
        .sum();
    assertTrue(totalSTCG > 0, "STCG should be positive");
}

@Test(expected = InvalidSecurityException.class)
public void testLoadBuys_NullSecurityName() {
    loader.loadBuys(); // Should throw if name is null
}

@Test
public void testSecurityCalculatesPLCorrectly() {
    Security security = new Security("TCS", new Date(), 100, 10, 110);
    double expectedPL = (110 - 100) * 10; // 100
    assertEquals(expectedPL, security.calculatePL(), 0.01);
}
```

### Integration Tests

```java
@Test
public void testEndToEndTaxCalculation() {
    // Arrange: Create test Excel files
    
    // Act: Run full workflow
    InvestingHurdleBootstrapper app = InvestingHurdleBootstrapper.getInstance();
    app.loadAndCalculate();
    
    // Assert: Verify STCG matches expected values
    assertEquals(expectedTotal, app.getTotalSTCG(), 0.01);
}
```

---

## 🎯 Recommendations Summary

### Priority 1 (Critical)

1. **Add Unit Tests**
   - Test `returnQuarter()` with boundary dates
   - Test STCG calculation logic
   - Test exception handling
   - Target: 80%+ code coverage

2. **Fix Hardcoded Quarter Dates**
   - Move to configuration file or enum
   - Support multi-year calculations
   - Use `LocalDate` instead of `java.util.Date`

3. **Implement `setAveragePrices()`**
   - Critical for accurate cost basis
   - Implement FIFO matching logic
   - Essential for compliance

### Priority 2 (Important)

4. **Improve Exception Handling**
   - Replace `catch(Exception e)` with specific exceptions
   - Log full stack traces
   - Propagate exceptions properly

5. **Parameterize File Paths**
   - Accept command-line arguments
   - Load from properties file
   - Environment-specific configs

6. **Add Input Validation**
   - Check cell data types before casting
   - Validate date formats
   - Range checks on prices/quantities

### Priority 3 (Enhancement)

7. **Export Functionality**
   - CSV export for spreadsheet import
   - JSON for web integration
   - PDF for archival

8. **Migrate to Java 8+ Features**
   - Stream API for aggregations
   - Lambda expressions
   - `java.time` API (replace `Date`)

9. **Database Integration**
   - Persist calculations to database
   - Query historical data
   - Generate multi-year reports

10. **Web UI**
    - Spring Boot REST API
    - React/Vue frontend
    - Real-time calculations

---

## 📚 Related Patterns

This application successfully demonstrates:
- ✅ **Singleton Pattern** for application initialization
- ✅ **Factory Pattern** for object creation
- ✅ **Template Method** in data loading process
- ✅ **Data Transfer Object (DTO)** in `Security` class
- ✅ **Repository Pattern** in `securityMap` storage

Candidates for improvement:
- 🔄 **Strategy Pattern** for tax calculation algorithms
- 🔄 **Builder Pattern** for complex `Security` object creation
- 🔄 **Adapter Pattern** for different Excel formats
- 🔄 **Observer Pattern** for calculation change notifications

---

## 🔗 Cross-References

- [TaxHrd Project Page](../projects/taxhrd.md)
- [GitHub Repository](https://github.com/Ajay3007/TaxHrd)
- [README Documentation](../README.md)

---

**Document Version:** 1.0  
**Last Updated:** January 2025  
**Author:** Code Analysis Assistant
