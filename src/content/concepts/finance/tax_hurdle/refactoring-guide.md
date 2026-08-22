---
title: "Refactoring Guide"
description: "Tax Hurdle — Code Improvement Refactoring Guide Step-by-step improvements with before/after code examples."
domain: finance
order: 99
ownHeader: true
url: /learning/finance/tax_hurdle/refactoring-guide/
---

# Tax Hurdle — Code Improvement Refactoring Guide

**Step-by-step improvements with before/after code examples.**

---

## 📑 Quick Navigation

- **[Refactoring Overview](#-refactoring-overview)**
- **[Priority 1: Critical Issues](#-priority-1-critical-issues)**
- **[Priority 2: Important Improvements](#-priority-2-important-improvements)**
- **[Priority 3: Enhancements](#-priority-3-enhancements)**
- **[Implementation Roadmap](#-implementation-roadmap)**

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

### 1.1 Implement FIFO Cost Basis Matching

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
public void setAveragePrices() {
    HurdleLogger.getLogger().info("Starting FIFO cost basis calculation");
    
    for (String securityName : securityMap.keySet()) {
        Queue<Security> trades = securityMap.get(securityName);
        Queue<Security> buyQueue = new LinkedList<>();
        
        for (Security trade : trades) {
            if (isBuy(trade)) {
                buyQueue.offer(trade);
            } else {
                // Match sell against FIFO buys
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
                
                double averageCost = totalCost / trade.getQuantity();
                trade.setAveragePrice(averageCost);
            }
        }
    }
}
```

**Benefits:**
✅ Accurate P&L calculation  
✅ Tax-compliant FIFO matching  
✅ Essential for tax filing  

---

### 1.2 Migrate from `java.util.Date` to `LocalDate`

**Current Code:**
```java
Date date = row.getCell(1).getDateCellValue();

if (dateStr.compareTo("01-Apr") >= 0) { // String comparison!
    // ...
}
```

**Problems:**
- ❌ `java.util.Date` is mutable and error-prone
- ❌ String comparison is locale-dependent
- ❌ Year-specific hardcoding

**Improved Solution:**
```java
LocalDate date = row.getCell(1).getDateCellValue().toInstant()
    .atZone(ZoneId.systemDefault()).toLocalDate();

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
✅ Immutable, thread-safe dates  
✅ Year-independent  
✅ Locale-safe  
✅ Type-safe comparisons  

---

### 1.3 Fix Exception Handling

**Current Code:**
```java
try {
    // ... code ...
} catch (Exception e) {
    e.printStackTrace();
}
```

**Problems:**
- ❌ Catches generic `Exception` (too broad)
- ❌ `printStackTrace()` instead of proper logging
- ❌ Errors silently swallowed
- ❌ Difficult debugging

**Improved Solution:**
```java
public void loadBuys() throws InvalidSecurityException {
    try (FileInputStream fis = new FileInputStream(HurdleConstant.CONFIGURATION_PATH);
         XSSFWorkbook workbook = new XSSFWorkbook(fis)) {
        
        XSSFSheet sheet = workbook.getSheet("Buy");
        if (sheet == null) {
            throw new InvalidSecurityException("'Buy' sheet not found");
        }
        
        for (Row row : sheet) {
            try {
                Security security = parseAndValidate(row);
                securityMap.computeIfAbsent(security.getSecurityName(),
                    k -> new ConcurrentLinkedQueue<>()).offer(security);
                    
            } catch (InvalidSecurityException e) {
                HurdleLogger.getLogger().warn("Skipping invalid row: " + e.getMessage());
            } catch (ClassCastException e) {
                HurdleLogger.getLogger().warn("Type conversion failed", e);
            }
        }
    } catch (IOException e) {
        HurdleLogger.getLogger().error("Failed to load buy sheet", e);
        throw new InvalidSecurityException("Excel file read error", e);
    }
}

private Security parseAndValidate(Row row) throws InvalidSecurityException {
    Cell nameCell = row.getCell(0);
    if (nameCell == null || nameCell.getStringCellValue().trim().isEmpty()) {
        throw new InvalidSecurityException("Security name is empty at row " + row.getRowNum());
    }
    
    // Validate other cells similarly
    
    return new Security(/* ... */);
}
```

**Benefits:**
✅ Specific exceptions caught
✅ Proper error logging  
✅ Stack traces preserved
✅ Errors not silently ignored

---

## 🟡 Priority 2: Important Improvements

---

### 2.1 Externalize Quarter Configuration

**Current Code:**
```java
public int returnQuarter(LocalDate date) {
    if (monthDay.isBefore(MonthDay.of(Month.JUNE, 16))) {
        return 1;
    } else if (monthDay.isBefore(MonthDay.of(Month.SEPTEMBER, 16))) {
        return 2;
    // ... hardcoded dates
}
```

**Improved Solution:**
```java
// Create QuarterConfig enum or class
public enum QuarterDefinition {
    Q1(Month.APRIL, 1, Month.JUNE, 15),
    Q2(Month.JUNE, 16, Month.SEPTEMBER, 15),
    Q3(Month.SEPTEMBER, 16, Month.DECEMBER, 15),
    Q4(Month.DECEMBER, 16, Month.MARCH, 15),
    Q5(Month.MARCH, 16, Month.MARCH, 31);
    
    private final MonthDay startDate;
    private final MonthDay endDate;
    
    QuarterDefinition(Month startMonth, int startDay, Month endMonth, int endDay) {
        this.startDate = MonthDay.of(startMonth, startDay);
        this.endDate = MonthDay.of(endMonth, endDay);
    }
    
    public boolean contains(LocalDate date) {
        MonthDay monthDay = MonthDay.from(date);
        return monthDay.isBefore(endDate.plusDays(1));
    }
}

public int returnQuarter(LocalDate date) {
    for (QuarterDefinition q : QuarterDefinition.values()) {
        if (q.contains(date)) {
            return q.ordinal() + 1;
        }
    }
    throw new InvalidSecurityException("Date " + date + " not in any quarter");
}
```

**Benefits:**
✅ Configuration externalized  
✅ Easy to support multiple FYs  
✅ Type-safe  
✅ Reusable  

---

### 2.2 Parameterize File Paths

**Current Code:**
```java
public static final String CONFIGURATION_PATH = 
    "C:\\Users\\...\\configuration\\";
```

**Improved Solution:**
```java
// Load from properties file
public class AppConfig {
    private static final Properties props = new Properties();
    
    static {
        try (InputStream input = 
             AppConfig.class.getClassLoader()
                      .getResourceAsStream("application.properties")) {
            props.load(input);
        } catch (IOException e) {
            throw new RuntimeException("Failed to load config", e);
        }
    }
    
    public static String getConfigurationPath() {
        return props.getProperty("tax.configuration.path", 
            "./configuration");
    }
}

// application.properties
tax.configuration.path=/home/user/tax_data/configuration
tax.log.path=/home/user/tax_data/logs
```

**Or via command-line:**
```java
public static void main(String[] args) {
    String configPath = args.length > 0 ? args[0] : "./configuration";
    // Use configPath
}
```

**Benefits:**
✅ Environment-specific configs  
✅ No code changes needed  
✅ Docker/cloud friendly  
✅ Easy CI/CD integration  

---

### 2.3 Add Input Validation Layer

**Current Code:**
```java
double buyPrice = row.getCell(2).getNumericCellValue();
// No validation!
```

**Improved Solution:**
```java
public class ValidationUtils {
    public static void validatePrice(double price, String fieldName) 
            throws InvalidSecurityException {
        if (price <= 0) {
            throw new InvalidSecurityException(
                fieldName + " must be positive, got: " + price);
        }
        if (price > 1_000_000_000) {
            throw new InvalidSecurityException(
                fieldName + " exceeds maximum limit: " + price);
        }
    }
    
    public static void validateQuantity(int quantity, String fieldName)
            throws InvalidSecurityException {
        if (quantity <= 0) {
            throw new InvalidSecurityException(
                fieldName + " must be positive, got: " + quantity);
        }
        if (quantity > 10_000_000) {
            throw new InvalidSecurityException(
                fieldName + " exceeds maximum: " + quantity);
        }
    }
    
    public static String validateSecurityName(String name)
            throws InvalidSecurityException {
        if (name == null || name.trim().isEmpty()) {
            throw new InvalidSecurityException("Security name cannot be empty");
        }
        if (name.length() > 50) {
            throw new InvalidSecurityException(
                "Security name too long: " + name.length());
        }
        return name.trim();
    }
}

// Usage
double buyPrice = row.getCell(2).getNumericCellValue();
ValidationUtils.validatePrice(buyPrice, "Buy Price");
```

**Benefits:**
✅ Data integrity  
✅ Early error detection  
✅ Consistent validation  
✅ Better error messages  

---

## 🟢 Priority 3: Enhancements

---

### 3.1 Add Report Export (CSV)

```java
public void exportToCSV(String filename) throws IOException {
    try (FileWriter writer = new FileWriter(filename);
         CSVPrinter csvPrinter = new CSVPrinter(writer, 
             CSVFormat.DEFAULT.withHeader("Quarter", "STCG", "Status"))) {
        
        for (int q = 1; q <= 5; q++) {
            double stcg = stcgByQuarter.getOrDefault(q, 0.0);
            csvPrinter.printRecord(q, stcg, "COMPLETE");
        }
    }
}
```

---

### 3.2 Migrate to Java 8+ Stream API

```java
// Calculate total STCG using streams
double totalSTCG = stcgByQuarter.values().stream()
    .mapToDouble(Double::doubleValue)
    .sum();

// Group securities by quarter
Map<Integer, List<Security>> byQuarter = allSecurities.stream()
    .collect(Collectors.groupingBy(s -> returnQuarter(s.getSaleDate())));
```

---

## 📋 Implementation Roadmap

### Phase 1 (Weeks 1-2): Critical Fixes

- [ ] Implement FIFO cost basis
- [ ] Fix hardcoded quarters
- [ ] Migrate to `LocalDate`
- [ ] Improve exception handling

### Phase 2 (Weeks 3-4): Important Improvements

- [ ] Externalize quarter config
- [ ] Parameterize file paths
- [ ] Add input validation

### Phase 3 (Weeks 5-6): Enhancements

- [ ] Add CSV export
- [ ] Add unit tests (80%+ coverage)
- [ ] Stream API migration

### Phase 4 (Weeks 7+): Future

- [ ] Database persistence
- [ ] Spring Boot REST API
- [ ] Web UI (React/Vue)

---

**Document Version:** 1.0  
**Last Updated:** December 31, 2025

← [Back to Hub]()  |  [Previous: Technical Analysis](/learning/finance/tax_hurdle/technical-analysis)
