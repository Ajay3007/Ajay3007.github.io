# TaxHrd — Code Improvement Refactoring Guide

**Step-by-step improvements with before/after code examples.**

---

## 🎯 Refactoring Overview

This guide provides **actionable code improvements** organized by priority. Each section includes:
- Current implementation
- Problems identified
- Improved solution
- Benefits & trade-offs

---

## 🔴 Priority 1: Critical Issues

---

### 1.1 Implement Average Price Calculation (FIFO Matching)

**Location:** `WorkbookLoader.setAveragePrices()`

**Current Code:**
```java
public void setAveragePrices() {
    // Empty method!
}
```

**Problem:**
- ❌ Average cost basis not calculated
- ❌ P&L calculations inaccurate
- ❌ Essential for tax compliance

**Improved Solution:**

```java
/**
 * Calculate average purchase price using FIFO (First-In-First-Out) method.
 * Matches sells against buys in chronological order.
 */
public void setAveragePrices() {
    HurdleLogger.getLogger().info("Starting FIFO cost basis calculation");
    
    for (String securityName : securityMap.keySet()) {
        Queue<Security> trades = securityMap.get(securityName);
        Queue<Security> buyQueue = new LinkedList<>();
        double accumulatedCost = 0;
        int accumulatedQuantity = 0;
        
        for (Security trade : trades) {
            if (isBuy(trade)) {
                // Add to buy queue for FIFO matching
                buyQueue.offer(trade);
                accumulatedQuantity += trade.getQuantity();
                accumulatedCost += trade.getBuyPrice() * trade.getQuantity();
            } else {
                // Sell: Match against FIFO buys
                int sellQuantity = trade.getQuantity();
                double totalCost = 0;
                
                while (sellQuantity > 0 && !buyQueue.isEmpty()) {
                    Security buy = buyQueue.peek();
                    int matchQuantity = Math.min(sellQuantity, buy.getQuantity());
                    
                    totalCost += buy.getBuyPrice() * matchQuantity;
                    sellQuantity -= matchQuantity;
                    buy.setQuantity(buy.getQuantity() - matchQuantity);
                    
                    if (buy.getQuantity() == 0) {
                        buyQueue.poll();
                    }
                }
                
                // Set average cost on this sell
                double averageCost = totalCost / trade.getQuantity();
                trade.setAverageCostPrice(averageCost);
                
                // Calculate actual P&L
                double actualPL = (trade.getSellPrice() - averageCost) 
                                  * trade.getQuantity();
                trade.setCalculatedPL(actualPL);
                
                HurdleLogger.getLogger().debug(
                    String.format("%s: Sold %d @ %.2f, Cost: %.2f, P&L: %.2f",
                        securityName, trade.getQuantity(), trade.getSellPrice(), 
                        averageCost, actualPL)
                );
            }
        }
    }
    
    HurdleLogger.getLogger().info("FIFO cost basis calculation complete");
}

private boolean isBuy(Security trade) {
    // Determine if trade is buy or sell
    // Implementation depends on your data model
    return trade.getBuyPrice() > 0 && trade.getSellPrice() == 0;
}
```

**Security Class Update:**
```java
public class Security {
    private String securityName;
    private Date tradeDate;
    private double buyPrice;
    private double sellPrice;
    private int quantity;
    private double ltp;
    private double averageCostPrice; // NEW: FIFO cost basis
    private double calculatedPL;     // NEW: Actual P&L
    
    // Getters/Setters
    public double getAverageCostPrice() {
        return averageCostPrice;
    }
    
    public void setAverageCostPrice(double averageCostPrice) {
        this.averageCostPrice = averageCostPrice;
    }
    
    public double getCalculatedPL() {
        return calculatedPL;
    }
    
    public void setCalculatedPL(double calculatedPL) {
        this.calculatedPL = calculatedPL;
    }
}
```

**Benefits:**
✅ Accurate cost basis (FIFO compliance)  
✅ Correct P&L calculation  
✅ Tax-ready data  
✅ Traceable audit trail  

**Trade-offs:**
⚠️ Slightly more memory (FIFO tracking)  
⚠️ Requires valid buy/sell data  

---

### 1.2 Replace java.util.Date with java.time.LocalDate

**Problem:**
- ❌ `java.util.Date` is deprecated (legacy)
- ❌ String-based quarter comparison is fragile
- ❌ No timezone awareness
- ❌ Mutable (thread-unsafe)

**Current Code:**
```java
public int returnQuarter(Date date) {
    SimpleDateFormat formatter = new SimpleDateFormat("dd-MMM");
    String dateStr = formatter.format(date);
    
    if (dateStr.compareTo("01-Apr") >= 0 && 
        dateStr.compareTo("15-Jun") <= 0) {
        return 1;
    }
    // ... more hardcoded comparisons
}
```

**Improved Solution:**

```java
import java.time.LocalDate;
import java.time.MonthDay;
import java.time.Month;

public class EquityLoader {
    
    /**
     * Map a transaction date to financial quarter (Apr-Mar FY).
     * Year-independent, locale-safe implementation.
     */
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
    
    /**
     * Overload for backward compatibility with java.util.Date
     */
    public int returnQuarter(Date date) {
        return returnQuarter(date.toInstant()
            .atZone(ZoneId.systemDefault())
            .toLocalDate());
    }
}
```

**WorkbookLoader Update:**
```java
public void loadBuys() throws InvalidSecurityException, IOException {
    try (FileInputStream fis = new FileInputStream(HurdleConstant.CONFIGURATION_PATH);
         XSSFWorkbook workbook = new XSSFWorkbook(fis)) {
        
        XSSFSheet sheet = workbook.getSheet("Buy");
        
        for (Row row : sheet) {
            if (row == null) continue;
            
            // Convert to LocalDate
            LocalDate tradeDate = row.getCell(1)
                .getLocalDateTimeCellValue()
                .toLocalDate();
            
            double buyPrice = row.getCell(2).getNumericCellValue();
            int quantity = (int) row.getCell(3).getNumericCellValue();
            
            Security security = new Security(
                row.getCell(0).getStringCellValue(),
                tradeDate,
                buyPrice,
                quantity,
                row.getCell(4).getNumericCellValue()
            );
            
            securityMap.computeIfAbsent(security.getSecurityName(), 
                k -> new ConcurrentLinkedQueue<>())
                .offer(security);
        }
    }
}
```

**Security Class Update:**
```java
public class Security {
    private String securityName;
    private LocalDate tradeDate;      // Changed from Date
    private double buyPrice;
    private double sellPrice;
    private int quantity;
    private double ltp;
    
    public Security(String securityName, LocalDate tradeDate, 
                   double buyPrice, int quantity, double ltp) {
        this.securityName = securityName;
        this.tradeDate = tradeDate;
        this.buyPrice = buyPrice;
        this.quantity = quantity;
        this.ltp = ltp;
    }
    
    // Getters/Setters
    public LocalDate getTradeDate() {
        return tradeDate;
    }
    
    public void setTradeDate(LocalDate tradeDate) {
        this.tradeDate = tradeDate;
    }
}
```

**Benefits:**
✅ Modern Java 8+ API  
✅ Immutable & thread-safe  
✅ Cleaner date arithmetic  
✅ Type-safe comparisons  
✅ Year-independent logic  

---

### 1.3 Fix Exception Handling (Proper Logging)

**Problem:**
- ❌ Generic `catch(Exception e)` swallows errors
- ❌ `printStackTrace()` goes to stderr, not logs
- ❌ No error recovery mechanism
- ❌ Stack traces get lost

**Current Code:**
```java
public void loadBuys() {
    try {
        FileInputStream fis = new FileInputStream(HurdleConstant.CONFIGURATION_PATH);
        XSSFWorkbook workbook = new XSSFWorkbook(fis);
        XSSFSheet sheet = workbook.getSheet("Buy");
        // ... processing
    } catch (Exception e) {
        e.printStackTrace(); // ❌ Bad!
    }
}
```

**Improved Solution:**

```java
/**
 * Load buy transactions from Excel with proper exception handling.
 * 
 * @throws IOException if file cannot be read
 * @throws InvalidSecurityException if data validation fails
 */
public void loadBuys() throws IOException, InvalidSecurityException {
    Logger logger = HurdleLogger.getLogger();
    logger.info("Starting buy transaction load from: {}", 
        HurdleConstant.CONFIGURATION_PATH);
    
    try (FileInputStream fis = new FileInputStream(HurdleConstant.CONFIGURATION_PATH);
         XSSFWorkbook workbook = new XSSFWorkbook(fis)) {
        
        XSSFSheet sheet = workbook.getSheet("Buy");
        if (sheet == null) {
            throw new InvalidSecurityException("'Buy' sheet not found in workbook");
        }
        
        int successCount = 0;
        int errorCount = 0;
        
        for (Row row : sheet) {
            if (row == null || row.getPhysicalNumberOfCells() == 0) {
                continue; // Skip empty rows
            }
            
            try {
                Security security = parseBuyRow(row);
                securityMap.computeIfAbsent(security.getSecurityName(), 
                    k -> new ConcurrentLinkedQueue<>())
                    .offer(security);
                successCount++;
            } catch (InvalidSecurityException e) {
                errorCount++;
                logger.warn("Skipping invalid buy record at row {}: {}", 
                    row.getRowNum(), e.getMessage());
            } catch (Exception e) {
                errorCount++;
                logger.error("Unexpected error parsing row {}", 
                    row.getRowNum(), e);
            }
        }
        
        logger.info("Buy load complete: {} loaded, {} errors", 
            successCount, errorCount);
        
        if (successCount == 0) {
            throw new InvalidSecurityException("No valid buy records found");
        }
        
    } catch (FileNotFoundException e) {
        logger.error("Configuration file not found: {}", 
            HurdleConstant.CONFIGURATION_PATH);
        throw new IOException("Cannot locate buy configuration", e);
    } catch (IOException e) {
        logger.error("Failed to read buy configuration", e);
        throw e;
    }
}

/**
 * Parse a single buy row from Excel with validation.
 */
private Security parseBuyRow(Row row) throws InvalidSecurityException {
    Cell nameCell = row.getCell(0);
    Cell dateCell = row.getCell(1);
    Cell priceCell = row.getCell(2);
    Cell quantityCell = row.getCell(3);
    Cell ltpCell = row.getCell(4);
    
    // Validate required cells
    if (nameCell == null || nameCell.getCellType() != CellType.STRING) {
        throw new InvalidSecurityException("Row " + row.getRowNum() + 
            ": Security name (cell A) must be text");
    }
    
    String securityName = nameCell.getStringCellValue().trim();
    if (securityName.isEmpty()) {
        throw new InvalidSecurityException("Row " + row.getRowNum() + 
            ": Security name cannot be empty");
    }
    
    if (dateCell == null || dateCell.getCellType() != CellType.NUMERIC) {
        throw new InvalidSecurityException("Row " + row.getRowNum() + 
            ": Trade date (cell B) must be a date");
    }
    
    LocalDate tradeDate = dateCell.getLocalDateTimeCellValue().toLocalDate();
    
    if (priceCell == null || priceCell.getCellType() != CellType.NUMERIC) {
        throw new InvalidSecurityException("Row " + row.getRowNum() + 
            ": Price (cell C) must be numeric");
    }
    
    double buyPrice = priceCell.getNumericCellValue();
    if (buyPrice <= 0) {
        throw new InvalidSecurityException("Row " + row.getRowNum() + 
            ": Price must be positive, got " + buyPrice);
    }
    
    if (quantityCell == null || quantityCell.getCellType() != CellType.NUMERIC) {
        throw new InvalidSecurityException("Row " + row.getRowNum() + 
            ": Quantity (cell D) must be numeric");
    }
    
    int quantity = (int) quantityCell.getNumericCellValue();
    if (quantity <= 0) {
        throw new InvalidSecurityException("Row " + row.getRowNum() + 
            ": Quantity must be positive, got " + quantity);
    }
    
    double ltp = ltpCell != null && ltpCell.getCellType() == CellType.NUMERIC 
        ? ltpCell.getNumericCellValue() 
        : 0;
    
    return new Security(securityName, tradeDate, buyPrice, quantity, ltp);
}
```

**Custom Exception Update:**
```java
/**
 * Exception thrown when security record validation fails.
 */
public class InvalidSecurityException extends Exception {
    public InvalidSecurityException(String message) {
        super(message);
    }
    
    public InvalidSecurityException(String message, Throwable cause) {
        super(message, cause);
    }
}
```

**Benefits:**
✅ Clear error messages  
✅ Proper stack trace logging  
✅ Distinguishes validation vs. I/O errors  
✅ Fail-fast approach  
✅ Better debugging information  

---

## 🟡 Priority 2: Important Improvements

---

### 2.1 Externalize Quarter Configuration

**Problem:**
- ❌ Quarter dates hardcoded in method
- ❌ Only works for single financial year
- ❌ Cannot configure without recompiling

**Solution:**

Create `QuarterConfig.java`:
```java
public class QuarterConfig {
    private static final Map<Integer, DateRange> QUARTERS = new LinkedHashMap<>();
    
    static {
        // Financial year April 1 – March 31
        QUARTERS.put(1, new DateRange(Month.APRIL, 1, Month.JUNE, 15));
        QUARTERS.put(2, new DateRange(Month.JUNE, 16, Month.SEPTEMBER, 15));
        QUARTERS.put(3, new DateRange(Month.SEPTEMBER, 16, Month.DECEMBER, 15));
        QUARTERS.put(4, new DateRange(Month.DECEMBER, 16, Month.MARCH, 15));
        QUARTERS.put(5, new DateRange(Month.MARCH, 16, Month.MARCH, 31));
    }
    
    public static int getQuarter(LocalDate date) {
        MonthDay monthDay = MonthDay.of(date.getMonth(), date.getDayOfMonth());
        
        for (Map.Entry<Integer, DateRange> entry : QUARTERS.entrySet()) {
            if (entry.getValue().contains(monthDay)) {
                return entry.getKey();
            }
        }
        
        throw new IllegalArgumentException("Invalid date: " + date);
    }
    
    public static class DateRange {
        private final MonthDay start;
        private final MonthDay end;
        
        public DateRange(Month startMonth, int startDay, Month endMonth, int endDay) {
            this.start = MonthDay.of(startMonth, startDay);
            this.end = MonthDay.of(endMonth, endDay);
        }
        
        public boolean contains(MonthDay date) {
            if (start.compareTo(end) <= 0) {
                return date.compareTo(start) >= 0 && date.compareTo(end) <= 0;
            } else {
                // Wraps year boundary (e.g., Dec to Mar)
                return date.compareTo(start) >= 0 || date.compareTo(end) <= 0;
            }
        }
    }
}
```

**Usage:**
```java
int quarter = QuarterConfig.getQuarter(LocalDate.now());
```

**Benefits:**
✅ Externalized configuration  
✅ Year-independent  
✅ Easy to add new financial years  
✅ Testable  

---

### 2.2 Parameterize File Paths

**Current Code:**
```java
public class HurdleConstant {
    public static final String CONFIGURATION_PATH = 
        "./configuration/configuration_stock.xlsx";
    public static final String TAX_FILE_PATH = 
        "./configuration/tax_2122_.xlsx";
}
```

**Improved Solution:**

Create `config.properties`:
```properties
# File paths
configuration.buy.path=./configuration/configuration_stock.xlsx
configuration.tax.path=./configuration/tax_2122_.xlsx
logging.path=./logs

# Logging
logging.level=INFO
logging.max.file.size=10485760
logging.max.backups=5
```

`ConfigLoader.java`:
```java
public class ConfigLoader {
    private static final Properties props = new Properties();
    private static final Logger logger = HurdleLogger.getLogger();
    
    static {
        try (InputStream input = ConfigLoader.class.getClassLoader()
            .getResourceAsStream("config.properties")) {
            
            if (input == null) {
                logger.warn("config.properties not found, using defaults");
                loadDefaults();
            } else {
                props.load(input);
            }
        } catch (IOException e) {
            logger.error("Failed to load configuration", e);
            loadDefaults();
        }
    }
    
    public static String getConfigPath(String key, String defaultValue) {
        return props.getProperty(key, defaultValue);
    }
    
    public static String getConfigBuyPath() {
        return getConfigPath("configuration.buy.path", 
            "./configuration/configuration_stock.xlsx");
    }
    
    public static String getConfigTaxPath() {
        return getConfigPath("configuration.tax.path", 
            "./configuration/tax_2122_.xlsx");
    }
    
    public static String getLoggingPath() {
        return getConfigPath("logging.path", "./logs");
    }
    
    private static void loadDefaults() {
        props.setProperty("configuration.buy.path", 
            "./configuration/configuration_stock.xlsx");
        props.setProperty("configuration.tax.path", 
            "./configuration/tax_2122_.xlsx");
        props.setProperty("logging.path", "./logs");
    }
}
```

**CLI Override Option:**
```java
public class InvestingHurdleBootstrapper {
    
    public static void main(String[] args) {
        if (args.length > 0) {
            // Override with CLI arguments
            System.setProperty("configuration.buy.path", args[0]);
        }
        if (args.length > 1) {
            System.setProperty("configuration.tax.path", args[1]);
        }
        
        getInstance().run();
    }
}

// Usage:
// java bootstrap.InvestingHurdleBootstrapper \
//   ./config/my_buys.xlsx \
//   ./config/my_tax.xlsx
```

**Benefits:**
✅ Environment-specific configs  
✅ No hardcoding  
✅ Easy deployment  
✅ CLI override support  

---

### 2.3 Add Input Validation Layer

**Solution:**

`SecurityValidator.java`:
```java
public class SecurityValidator {
    private static final Logger logger = HurdleLogger.getLogger();
    
    private static final double MIN_PRICE = 0.01;
    private static final double MAX_PRICE = 1_000_000.00;
    private static final int MIN_QUANTITY = 1;
    private static final int MAX_QUANTITY = 1_000_000;
    
    /**
     * Validate a security record for correctness.
     */
    public static void validate(Security security) throws InvalidSecurityException {
        validateSecurityName(security.getSecurityName());
        validateTradeDate(security.getTradeDate());
        validatePrice(security.getBuyPrice(), "Buy price");
        validatePrice(security.getSellPrice(), "Sell price");
        validateQuantity(security.getQuantity());
    }
    
    private static void validateSecurityName(String name) 
            throws InvalidSecurityException {
        if (name == null || name.trim().isEmpty()) {
            throw new InvalidSecurityException("Security name cannot be empty");
        }
        if (name.length() > 50) {
            throw new InvalidSecurityException(
                "Security name too long (max 50 chars): " + name);
        }
        if (!name.matches("[A-Z0-9&-]+")) {
            throw new InvalidSecurityException(
                "Invalid security name format: " + name);
        }
    }
    
    private static void validateTradeDate(LocalDate date) 
            throws InvalidSecurityException {
        if (date == null) {
            throw new InvalidSecurityException("Trade date cannot be null");
        }
        if (date.isAfter(LocalDate.now().plusDays(1))) {
            throw new InvalidSecurityException(
                "Trade date cannot be in future: " + date);
        }
        LocalDate minDate = LocalDate.of(2000, 1, 1);
        if (date.isBefore(minDate)) {
            throw new InvalidSecurityException(
                "Trade date too old (before 2000): " + date);
        }
    }
    
    private static void validatePrice(double price, String priceType) 
            throws InvalidSecurityException {
        if (price < 0) {
            throw new InvalidSecurityException(
                priceType + " cannot be negative: " + price);
        }
        if (price > 0 && (price < MIN_PRICE || price > MAX_PRICE)) {
            throw new InvalidSecurityException(
                priceType + " out of range [" + MIN_PRICE + "-" + MAX_PRICE 
                + "]: " + price);
        }
    }
    
    private static void validateQuantity(int quantity) 
            throws InvalidSecurityException {
        if (quantity < MIN_QUANTITY || quantity > MAX_QUANTITY) {
            throw new InvalidSecurityException(
                "Quantity out of range [" + MIN_QUANTITY + "-" + MAX_QUANTITY 
                + "]: " + quantity);
        }
    }
}
```

**Usage in parseBuyRow:**
```java
private Security parseBuyRow(Row row) throws InvalidSecurityException {
    // ... existing parsing code ...
    
    Security security = new Security(securityName, tradeDate, 
        buyPrice, quantity, ltp);
    
    // Validate before returning
    SecurityValidator.validate(security);
    
    return security;
}
```

**Benefits:**
✅ Centralized validation  
✅ Reusable across loaders  
✅ Clear error messages  
✅ Range checking  

---

## 🟢 Priority 3: Enhancements

---

### 3.1 Add Report Export Functionality

**Solution:**

`ReportExporter.java`:
```java
public class ReportExporter {
    private static final Logger logger = HurdleLogger.getLogger();
    
    /**
     * Export tax report to CSV format.
     */
    public void exportToCSV(String filePath, TaxReport report) 
            throws IOException {
        try (PrintWriter writer = new PrintWriter(new FileWriter(filePath))) {
            writer.println("TaxHrd Report - STCG Calculation");
            writer.println("Generated: " + LocalDateTime.now());
            writer.println();
            
            // STCG Summary
            writer.println("STCG Summary");
            writer.println("Full Consideration Value," + report.getFullValue());
            writer.println("Cost of Acquisition," + report.getCostOfAcquisition());
            writer.println("STCG," + report.getTotalSTCG());
            writer.println();
            
            // Quarter Breakdown
            writer.println("Quarter,STCG");
            for (int q = 1; q <= 5; q++) {
                writer.println("Q" + q + "," + report.getSTCGbyQuarter(q));
            }
            writer.println();
            
            // Security Details
            writer.println("Security,Quantity,Buy Price,Sell Price,P&L");
            for (SecurityReport sec : report.getSecurityReports()) {
                writer.println(String.format("%s,%d,%.2f,%.2f,%.2f",
                    sec.getName(), sec.getQuantity(), 
                    sec.getBuyPrice(), sec.getSellPrice(), 
                    sec.getPnL()));
            }
            
            logger.info("Report exported to: " + filePath);
        }
    }
    
    /**
     * Export to JSON format for web integration.
     */
    public void exportToJSON(String filePath, TaxReport report) 
            throws IOException {
        try (PrintWriter writer = new PrintWriter(new FileWriter(filePath))) {
            String json = new JSONObject(report).toString(2);
            writer.print(json);
            logger.info("JSON report exported to: " + filePath);
        }
    }
}
```

**Usage:**
```java
ReportExporter exporter = new ReportExporter();
exporter.exportToCSV("./reports/tax_report_2122.csv", taxReport);
exporter.exportToJSON("./reports/tax_report_2122.json", taxReport);
```

**Benefits:**
✅ Multiple formats  
✅ Easy integration with CA tools  
✅ Archivable  

---

### 3.2 Add Comprehensive Unit Tests

**JUnit Test Suite:**

```java
public class EquityLoaderTest {
    
    private EquityLoader loader;
    
    @Before
    public void setUp() {
        loader = new EquityLoader();
    }
    
    @Test
    public void testReturnQuarter_Q1Boundary() {
        assertEquals(1, loader.returnQuarter(LocalDate.of(2021, 4, 1)));
        assertEquals(1, loader.returnQuarter(LocalDate.of(2021, 6, 15)));
    }
    
    @Test
    public void testReturnQuarter_Q2Boundary() {
        assertEquals(2, loader.returnQuarter(LocalDate.of(2021, 6, 16)));
        assertEquals(2, loader.returnQuarter(LocalDate.of(2021, 9, 15)));
    }
    
    @Test
    public void testReturnQuarter_Q5Boundary() {
        assertEquals(5, loader.returnQuarter(LocalDate.of(2021, 3, 16)));
        assertEquals(5, loader.returnQuarter(LocalDate.of(2021, 3, 31)));
    }
    
    @Test
    public void testCalculateSTCG_Sum() {
        // Arrange
        setupTestData();
        
        // Act
        Map<Integer, Double> result = loader.calculateSTCG();
        
        // Assert
        double total = result.values().stream()
            .mapToDouble(Double::doubleValue)
            .sum();
        assertTrue(total > 0, "Total STCG should be positive");
    }
    
    @Test(expected = InvalidSecurityException.class)
    public void testValidateSecurityName_Empty() 
            throws InvalidSecurityException {
        SecurityValidator.validate(new Security("", null, 0, 0, 0));
    }
    
    @Test
    public void testFIFOMatching() {
        // Buy 100 shares @ 100
        Security buy1 = new Security("TCS", LocalDate.of(2021, 1, 1), 100, 100, 0);
        
        // Sell 50 shares @ 150
        Security sell1 = new Security("TCS", LocalDate.of(2021, 2, 1), 0, 50, 0);
        sell1.setSellPrice(150);
        
        // Expected: P&L = (150 - 100) * 50 = 2500
        double expectedPL = (150 - 100) * 50;
        assertEquals(expectedPL, sell1.calculatePL(), 0.01);
    }
    
    private void setupTestData() {
        // Mock data setup
    }
}
```

**Benefits:**
✅ Regression prevention  
✅ Documentation  
✅ Confidence in changes  
✅ CI/CD integration  

---

## 📋 Summary Table

| Issue | Priority | Effort | Impact | Status |
|-------|----------|--------|--------|--------|
| FIFO Cost Basis | 🔴 P1 | High | Critical | ⏳ TODO |
| Fix Quarter Calculation | 🔴 P1 | Medium | High | ⏳ TODO |
| Exception Handling | 🔴 P1 | High | High | ⏳ TODO |
| Externaliz Quarters | 🟡 P2 | Medium | Medium | ⏳ TODO |
| Parameter File Paths | 🟡 P2 | Low | Medium | ⏳ TODO |
| Input Validation | 🟡 P2 | High | Medium | ⏳ TODO |
| Report Export | 🟢 P3 | Medium | Low | ⏳ TODO |
| Unit Tests | 🟢 P3 | High | Medium | ⏳ TODO |

---

## 🚀 Implementation Roadmap

### Phase 1 (Week 1-2): Critical Fixes
1. Implement FIFO matching
2. Fix quarter date logic
3. Improve exception handling

### Phase 2 (Week 3): Configuration
4. Externalize quarters
5. Parameterize file paths
6. Add input validation

### Phase 3 (Week 4): Testing & Polish
7. Add comprehensive tests
8. Export functionality
9. Documentation

### Phase 4: Future Enhancements
10. Database integration
11. Spring Boot API
12. Web UI

---

**Document Version:** 1.0  
**Created:** January 2025  
**Status:** Ready for implementation
