# Scripts Documentation

**Automation tools for portfolio maintenance and content generation**

---

## 📁 Contents

| Script | Purpose | Status |
|--------|---------|--------|
| `generate_summary.py` | Auto-generate executive summaries for markdown files | ✅ Production |
| `add_changelog_entry.py` | Add entries to site maintenance log | ✅ Production |
| `validate_site.py` | Validate Jekyll site structure and links | ✅ Production |
| `SUMMARY_GENERATION_GUIDE.md` | Complete guide for summary generation | 📖 Documentation |
| `SUMMARY_TEMPLATE.md` | Manual template for executive summaries | 📋 Template |
| `SUMMARY_IMPLEMENTATION_REPORT.md` | Implementation completion report | 📊 Report |

---

## 🚀 Quick Start

### Generate Executive Summaries

```bash
# Single file
python scripts/generate_summary.py learning/dsa/Arrays/index.md

# Entire directory
python scripts/generate_summary.py --batch learning/dsa/

# All learning sections
python scripts/generate_summary.py --all
```

### Add Changelog Entry

```bash
python scripts/add_changelog_entry.py "Added executive summaries to DSA docs"
```

### Validate Site

```bash
python scripts/validate_site.py
```

---

## 📖 Documentation

### Summary Generation

**Full Guide:** [SUMMARY_GENERATION_GUIDE.md](SUMMARY_GENERATION_GUIDE.md)

**Quick Reference:**
- Analyzes markdown content automatically
- Generates executive summaries with stats
- Inserts after frontmatter
- Creates backups (.md.bak)
- Prevents duplicates

**Manual Template:** [SUMMARY_TEMPLATE.md](SUMMARY_TEMPLATE.md)

---

## 🛠️ Requirements

### Python Version
- Python 3.6 or higher
- No external dependencies (uses only standard library)

### Environment
- Windows PowerShell ✅
- Linux/Mac Terminal ✅
- Git Bash ✅

---

## 📋 Examples

### Example 1: Process DSA Files

```bash
cd "c:\Users\Ajay.Gupt\OneDrive - Reliance Corporate IT Park Limited\Documents\csp\Ajay3007.github.io"
python scripts\generate_summary.py --batch learning\dsa\
```

**Output:**
```
📁 Found 15 markdown files in learning/dsa/
============================================================
📄 Processing: learning/dsa/Arrays/index.md
✅ Summary added to learning/dsa/Arrays/index.md
   Backup saved: learning/dsa/Arrays/index.md.bak
...
============================================================
✅ Successfully processed: 12
⏭️  Skipped: 2
❌ Failed: 1
```

### Example 2: Use Manual Template

```bash
# Copy template
cp scripts/SUMMARY_TEMPLATE.md learning/networking/new-topic.md

# Edit placeholders
# [Document Title] → TCP/IP Networking
# [X min] → 10
# etc.
```

---

## 🎯 Best Practices

### When to Use Automation

✅ Processing multiple files  
✅ Standardizing structure across docs  
✅ Initial summary generation  
✅ Batch updates for new sections  

### When to Use Manual Template

✅ Single new document  
✅ Custom summary requirements  
✅ Fine-grained control  
✅ Learning the structure  

---

## 🔧 Customization

### Modify Summary Structure

Edit `generate_summary.py`:

```python
# Line 125-200: Summary generation logic
def generate_summary(self) -> str:
    # Customize sections here
    summary.append("## 📋 Executive Summary")
    # Add/remove/modify sections
```

### Change Reading Speed

```python
# Line 150
reading_time = max(1, words // 250)  # Change 250 to your preferred WPM
```

### Skip Certain Files

```python
# Line 225
if md_file.name.lower() == 'index.md':  # Add more conditions
    skip_count += 1
    continue
```

---

## 📊 Summary Statistics

### Files Enhanced (December 2025)

| Category | Files | Status |
|----------|-------|--------|
| **DSA** | 3 main topics | ✅ Complete |
| **OOP** | 2 main topics | ✅ Complete |
| **System Design** | 3 main topics | ✅ Complete |
| **Total** | 8 critical files | ✅ Complete |

### Lines of Code

| Script | Lines | Language |
|--------|-------|----------|
| `generate_summary.py` | 400+ | Python |
| `add_changelog_entry.py` | 150+ | Python |
| `validate_site.py` | 300+ | Python |

---

## 🐛 Troubleshooting

### Common Issues

**Issue:** `'python' is not recognized`

**Solution:**
```bash
# Try python3
python3 scripts/generate_summary.py <file>

# Or use full path
"C:\Python39\python.exe" scripts/generate_summary.py <file>
```

**Issue:** Permission denied

**Solution:**
- Close file in editor
- Check if file is read-only
- Run with admin privileges (if needed)

**Issue:** Summary already exists

**Solution:**
- This is intentional (prevents duplicates)
- Manually remove existing summary to regenerate
- Or edit script to force overwrite (line 170)

---

## 📚 Resources

### Documentation Files

- **[SUMMARY_GENERATION_GUIDE.md](SUMMARY_GENERATION_GUIDE.md)** — Complete usage guide
- **[SUMMARY_TEMPLATE.md](SUMMARY_TEMPLATE.md)** — Manual template
- **[SUMMARY_IMPLEMENTATION_REPORT.md](SUMMARY_IMPLEMENTATION_REPORT.md)** — Implementation report

### Example References

- **learning/finance/taxhrd-summary.md** — Gold standard comprehensive summary
- **learning/dsa/Arrays/index.md** — DSA topic summary
- **learning/oop/design-patterns.md** — Design patterns summary
- **learning/system-design/high-level.md** — System design summary

---

## 🤝 Contributing

### Adding New Scripts

1. Create script in `scripts/` folder
2. Add entry to this README
3. Document usage and examples
4. Test on sample files

### Improving Existing Scripts

1. Edit script file
2. Test changes thoroughly
3. Update documentation
4. Commit with clear message

---

## 📞 Support

### Questions?

- **Script usage:** Check [SUMMARY_GENERATION_GUIDE.md](SUMMARY_GENERATION_GUIDE.md)
- **Template help:** See [SUMMARY_TEMPLATE.md](SUMMARY_TEMPLATE.md)
- **Examples:** View [SUMMARY_IMPLEMENTATION_REPORT.md](SUMMARY_IMPLEMENTATION_REPORT.md)

---

## 🎉 Success Stories

### What's Been Automated

✅ **8 documentation files** enhanced with executive summaries  
✅ **1,200+ lines** of structured content added  
✅ **Consistent format** across all summaries  
✅ **Automatic backups** created for safety  
✅ **Zero manual formatting** errors  

### Time Saved

- **Manual creation:** ~30 min per summary × 8 files = 4 hours
- **Automated creation:** 5 min setup + 2 min execution = 7 minutes
- **Time saved:** 3 hours 53 minutes (97% reduction!)

---

## 🔮 Future Enhancements

### Potential Additions

- [ ] Auto-detect difficulty level (Beginner/Intermediate/Advanced)
- [ ] Generate table of contents from headings
- [ ] Extract code language stats (Java/Python/C++ percentage)
- [ ] Link validation (check all internal links work)
- [ ] Generate summary comparison report
- [ ] AI-powered content recommendations

---

## 📖 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Dec 2025 | Initial release with summary generation |
| - | - | Future updates will be documented here |

---

**Maintained by:** Ajay Gupta  
**Last Updated:** December 2025  
**Status:** Active Development 🚀
