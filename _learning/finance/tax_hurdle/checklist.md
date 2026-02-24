---
layout: learning
title: Checklist
permalink: /learning/finance/tax_hurdle/checklist/
---

# Tax Hurdle — Implementation Checklist

**Track progress on code improvements and enhancements.**

---

## 🎯 Implementation Roadmap

### Phase 1: Critical Issues (Weeks 1-2)

- [ ] **P1.1** Implement FIFO cost basis in `setAveragePrices()`
  - [ ] Create FIFO matching algorithm
  - [ ] Calculate average costs
  - [ ] Update Security objects
  - **Status:** Not started

- [ ] **P1.2** Fix hardcoded quarter dates
  - [ ] Create `QuarterDefinition` enum
  - [ ] Use `LocalDate` instead of `java.util.Date`
  - [ ] Support multi-year calculations
  - **Status:** Not started

- [ ] **P1.3** Migrate from `java.util.Date` to `java.time`
  - [ ] Replace all `Date` references
  - [ ] Use `LocalDate`, `LocalDateTime`
  - [ ] Update Excel parsing
  - **Status:** Not started

- [ ] **P1.4** Fix exception handling
  - [ ] Replace generic `Exception` catches
  - [ ] Add specific exception types
  - [ ] Proper logging with stack traces
  - **Status:** Not started

---

### Phase 2: Important Improvements (Weeks 3-4)

- [ ] **P2.1** Externalize configuration
  - [ ] Create `application.properties`
  - [ ] Load quarter definitions from config
  - [ ] Support command-line arguments
  - **Status:** Not started

- [ ] **P2.2** Parameterize file paths
  - [ ] Remove hardcoded paths
  - [ ] Load from configuration
  - [ ] Environment-specific configs
  - **Status:** Not started

- [ ] **P2.3** Add input validation
  - [ ] Create `ValidationUtils` class
  - [ ] Validate prices, quantities, dates
  - [ ] Range checks and format validation
  - **Status:** Not started

- [ ] **P2.4** Improve logging
  - [ ] Add meaningful log statements
  - [ ] Use appropriate log levels
  - [ ] Add structured logging
  - **Status:** Not started

---

### Phase 3: Enhancements (Weeks 5-6)

- [ ] **P3.1** Add export functionality
  - [ ] CSV export of results
  - [ ] JSON export option
  - [ ] PDF generation
  - **Status:** Not started

- [ ] **P3.2** Add unit tests
  - [ ] Test `returnQuarter()` with all quarters
  - [ ] Test STCG calculation logic
  - [ ] Test exception handling paths
  - [ ] Test Security P&L calculation
  - [ ] Target: 80%+ code coverage
  - **Status:** Not started

- [ ] **P3.3** Migrate to Java 8+ features
  - [ ] Use Stream API for aggregations
  - [ ] Lambda expressions where applicable
  - [ ] Method references
  - **Status:** Not started

- [ ] **P3.4** Refactor for testability
  - [ ] Dependency injection
  - [ ] Separate concerns
  - [ ] Reduce tight coupling
  - **Status:** Not started

---

### Phase 4: Future Features (Month 2+)

- [ ] **P4.1** Database integration
  - [ ] Persistence layer
  - [ ] Query historical data
  - [ ] Multi-year reports

- [ ] **P4.2** REST API (Spring Boot)
  - [ ] Controller layer
  - [ ] Service layer
  - [ ] Error handling

- [ ] **P4.3** Web UI
  - [ ] React/Vue frontend
  - [ ] File upload interface
  - [ ] Report visualization
  - [ ] Export functionality

- [ ] **P4.4** Multi-year support
  - [ ] Store historical calculations
  - [ ] Compare year-over-year
  - [ ] Cumulative reports

---

## 📊 Progress Summary

| Phase | Total Items | Completed | %Complete |
|-------|------------|-----------|-----------|
| **Phase 1** | 4 | 0 | 0% |
| **Phase 2** | 4 | 0 | 0% |
| **Phase 3** | 4 | 0 | 0% |
| **Phase 4** | 4 | 0 | 0% |
| **TOTAL** | **16** | **0** | **0%** |

---

## 🔄 Dependent Tasks

```
Phase 1 (Critical)
    ↓
Phase 2 (Important)
    ↓
Phase 3 (Enhancements)
    ↓
Phase 4 (Future)
```

### Critical Dependencies

1. **FIFO implementation** must be done before testing P&L accuracy
2. **Quarter configuration** must be externalized before database work
3. **Unit tests** needed before refactoring
4. **Input validation** should be done before export functionality

---

## 📝 Notes

### Phase 1 Priorities
- FIFO is blocking accurate tax compliance
- Hardcoded quarters limit usability
- Exception handling needed for production

### Phase 2 Benefits
- Configuration externalization enables cloud deployment
- Input validation prevents data corruption
- Path parameterization enables Docker/K8s

### Phase 3 Quality Gates
- 80%+ test coverage before API deployment
- Stream API modernizes code style
- Export features enable business reporting

### Phase 4 Vision
- Database enables historical analysis
- REST API enables web/mobile access
- Web UI democratizes tool usage

---

## 🏁 Completion Criteria

**Phase 1:** All critical issues resolved, tested  
**Phase 2:** Important features complete, 50% test coverage  
**Phase 3:** Enhancements done, 80%+ test coverage, refactored  
**Phase 4:** Production-grade API and UI, 90%+ test coverage  

---

**Checklist Version:** 1.0  
**Last Updated:** December 31, 2025  
**Last Reviewed:** December 31, 2025

← [Back to Hub]()
