# External Links Batch Conversion Guide

## Summary
- **Total markdown files:** 87
- **Total external HTTP/HTTPS links found:** 134
- **Links already with target="_blank":** 8
- **Links needing conversion:** 126

---

## Conversion Patterns & Commands

### Pattern Overview
**Current format (to replace):**
```
[link text](https://example.com)
[link text](http://example.com)
```

**Target format (new):**
```
[link text](https://example.com){:target="_blank" rel="noopener noreferrer"}
[link text](http://example.com){:target="_blank" rel="noopener noreferrer"}
```

### IMPORTANT: Exclude Pattern
Do NOT replace links that already have this pattern:
```
{:target="_blank" rel="noopener noreferrer"}
```

---

## Method 1: PowerShell (Recommended for Windows)

### PowerShell Script (Batch Convert All Files)
This is the most reliable method for your Windows environment:

```powershell
$basePath = "c:\Users\Ajay.Gupt\OneDrive - Reliance Corporate IT Park Limited\Documents\csp\Ajay3007.github.io\learning"

# Get all markdown files
$files = Get-ChildItem -Path $basePath -Filter "*.md" -Recurse

$fileCount = 0
$linkCount = 0

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $originalContent = $content
    
    # Pattern: Match external links NOT already containing {:target="_blank"
    # This regex finds [text](url) where url starts with http/https
    # and the closing ) is not followed by {:target="_blank"
    
    $pattern = '\[([^\]]+)\]\((https?://[^)]+)\)(?!\{:target)'
    
    $content = [regex]::Replace(
        $content,
        $pattern,
        {
            param($match)
            $linkText = $match.Groups[1].Value
            $url = $match.Groups[2].Value
            return "[${linkText}](${url}){:target=`"_blank`" rel=`"noopener noreferrer`"}"
        }
    )
    
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        $newLinkCount = ([regex]::Matches($content, '\{:target="_blank"').Count)
        $oldLinkCount = ([regex]::Matches($originalContent, '\{:target="_blank"').Count)
        $converted = $newLinkCount - $oldLinkCount
        
        if ($converted -gt 0) {
            $fileCount++
            $linkCount += $converted
            Write-Host "✓ $($file.Name) - Converted $converted links"
        }
    }
}

Write-Host "`nConversion Complete!"
Write-Host "Files modified: $fileCount"
Write-Host "Total links converted: $linkCount"
```

**How to run:**
1. Open PowerShell
2. Copy the script above
3. Paste and execute in PowerShell
4. Monitor the output for success

---

## Method 2: sed Commands (for Git Bash / WSL)

If you prefer Unix-style tools, use these sed commands:

### Single sed Command for Batch Replace
```bash
cd "c:/Users/Ajay.Gupt/OneDrive - Reliance Corporate IT Park Limited/Documents/csp/Ajay3007.github.io/learning"

# Convert all .md files in place
find . -type f -name "*.md" -exec sed -i \
  's/\(\[[^]]*\]\)(https\?:\/\/[^)]*)\([^{]*\)$/\1\2{:target="_blank" rel="noopener noreferrer"}/g' \
  {} +
```

### Alternative sed Pattern (More Precise)
```bash
# This pattern is more careful about not double-converting
find . -type f -name "*.md" -exec sed -i \
  -E 's/(\[[^\]]+\]\(https?:\/\/[^)]+\))(?!\{:target)/${1}{:target="_blank" rel="noopener noreferrer"}/g' \
  {} +
```

### Per-File sed Command
If you want to process files individually:
```bash
sed -i 's/\(\[[^]]*\]\)(https\?:\/\/[^)]*)\([^{]*\)$/\1\2{:target="_blank" rel="noopener noreferrer"}/g' filename.md
```

---

## Method 3: VS Code Find and Replace

### Using VS Code Regex Find & Replace

**Step 1: Open Find and Replace**
- Press `Ctrl+H` in VS Code

**Step 2: Enable Regex Mode**
- Click the `.*` button (right side of search box) to enable regex

**Step 3: Use This Pattern**

**Find pattern:**
```regex
\[([^\]]+)\]\((https?://[^)]+)\)(?!\{:target)
```

**Replace pattern:**
```regex
[$1]($2){:target="_blank" rel="noopener noreferrer"}
```

**Step 4: Replace All**
- Click "Replace All" button in the learning directory scope

---

## Method 4: Notepad++ (If Using on Windows)

### Using Find and Replace in Notepad++

**Step 1: Open Find > Replace** (`Ctrl+H`)

**Step 2: Settings**
- Enable "Regular expressions"
- Set "Search mode" to "Regular expression"

**Step 3: Patterns**

**Find:**
```regex
\[([^\]]+)\]\((https?://[^)]+)\)(?!\{:target)
```

**Replace:**
```regex
[$1]($2){:target="_blank" rel="noopener noreferrer"}
```

**Step 4: Replace All**

---

## Method 5: Node.js Script (Alternative)

If you prefer Node.js:

```javascript
const fs = require('fs');
const path = require('path');

const basePath = 'c:\\Users\\Ajay.Gupt\\OneDrive - Reliance Corporate IT Park Limited\\Documents\\csp\\Ajay3007.github.io\\learning';

function processMarkdownFiles(dir) {
    const files = fs.readdirSync(dir, { withFileTypes: true });
    let totalConverted = 0;
    let filesModified = 0;

    for (const file of files) {
        const fullPath = path.join(dir, file.name);
        
        if (file.isDirectory()) {
            const result = processMarkdownFiles(fullPath);
            totalConverted += result.count;
            filesModified += result.files;
        } else if (file.name.endsWith('.md')) {
            const content = fs.readFileSync(fullPath, 'utf-8');
            const originalContent = content;
            
            // Pattern: [text](http://... or https://...) not followed by {:target="_blank"
            const pattern = /\[([^\]]+)\]\((https?:\/\/[^)]+)\)(?!\{:target)/g;
            const newContent = content.replace(pattern, 
                '[$1]($2){:target="_blank" rel="noopener noreferrer"}');
            
            if (newContent !== originalContent) {
                const converted = (newContent.match(/\{:target="_blank"/g) || []).length - 
                                (originalContent.match(/\{:target="_blank"/g) || []).length;
                fs.writeFileSync(fullPath, newContent, 'utf-8');
                console.log(`✓ ${file.name} - Converted ${converted} links`);
                filesModified++;
                totalConverted += converted;
            }
        }
    }

    return { count: totalConverted, files: filesModified };
}

const result = processMarkdownFiles(basePath);
console.log(`\nConversion Complete!`);
console.log(`Files modified: ${result.files}`);
console.log(`Total links converted: ${result.count}`);
```

**How to run:**
```bash
node convert-links.js
```

---

## Method 6: Plain Regex for Manual Use

If you're using Find & Replace in any text editor, here are the core patterns:

### Regex Pattern (for most tools)
```
Pattern to find:    \[([^\]]+)\]\((https?:\/\/[^)]+)\)(?!\{:target)
Pattern to replace: [$1]($2){:target="_blank" rel="noopener noreferrer"}
```

### What Each Part Means
- `\[` - Literal opening bracket
- `([^\]]+)` - Capture Group 1: Any characters except closing bracket (the link text)
- `\]` - Literal closing bracket
- `\(` - Literal opening parenthesis
- `(https?:\/\/[^)]+)` - Capture Group 2: URL starting with http:// or https://
- `\)` - Literal closing parenthesis
- `(?!\{:target)` - Negative lookahead: NOT followed by `{:target` (excludes already converted links)

---

## Verification Steps

### After Conversion, Verify Results

**Count converted links:**
```powershell
$basePath = "c:\Users\Ajay.Gupt\OneDrive - Reliance Corporate IT Park Limited\Documents\csp\Ajay3007.github.io\learning"
Get-ChildItem -Path $basePath -Filter "*.md" -Recurse | 
  Select-String -Pattern '\{:target="_blank"' | 
  Measure-Object | 
  Select-Object -ExpandProperty Count
```

**Expected result:** Should be around 142 (134 original + 8 already present)

### Check for Any Remaining Unconverted Links
```powershell
$basePath = "c:\Users\Ajay.Gupt\OneDrive - Reliance Corporate IT Park Limited\Documents\csp\Ajay3007.github.io\learning"
Get-ChildItem -Path $basePath -Filter "*.md" -Recurse | 
  ForEach-Object {
    Select-String -Path $_.FullName -Pattern '\[([^\]]+)\]\((https?://[^)]+)\)(?!\{:target)' | 
    ForEach-Object { $_ }
  }
```

**Expected result:** No matches (or very few if there are edge cases)

---

## Quick Start (Copy-Paste Ready)

### For PowerShell (Recommended):
```powershell
$basePath = "c:\Users\Ajay.Gupt\OneDrive - Reliance Corporate IT Park Limited\Documents\csp\Ajay3007.github.io\learning"; $files = Get-ChildItem -Path $basePath -Filter "*.md" -Recurse; $fileCount = 0; $linkCount = 0; foreach ($file in $files) { $content = Get-Content -Path $file.FullName -Raw; $originalContent = $content; $pattern = '\[([^\]]+)\]\((https?://[^)]+)\)(?!\{:target)'; $content = [regex]::Replace($content, $pattern, { param($match); $linkText = $match.Groups[1].Value; $url = $match.Groups[2].Value; return "[${linkText}](${url}){:target=`"_blank`" rel=`"noopener noreferrer`"}" }); if ($content -ne $originalContent) { Set-Content -Path $file.FullName -Value $content -Encoding UTF8; $newLinkCount = ([regex]::Matches($content, '\{:target="_blank"').Count); $oldLinkCount = ([regex]::Matches($originalContent, '\{:target="_blank"').Count); $converted = $newLinkCount - $oldLinkCount; if ($converted -gt 0) { $fileCount++; $linkCount += $converted; Write-Host "✓ Converted $converted links" } } }; Write-Host "Done! Files: $fileCount, Links: $linkCount"
```

---

## Edge Cases to Consider

### 1. Links Already Converted
- The regex patterns use `(?!\{:target)` negative lookahead to skip these
- Safe to run multiple times

### 2. Markdown Links with Parentheses in URL
- The pattern `[^)]+` handles most cases
- If your URLs contain `)`, they may not match (rare for external links)

### 3. Line Breaks in Links
- Standard markdown doesn't support line breaks in links
- Regex patterns assume single-line links

### 4. Special Characters in Link Text
- Handled by `[^\]]+` which matches anything except `]`
- Should work for Unicode and special characters

---

## Summary

| Method | Tool | Complexity | Speed | Recommended |
|--------|------|-----------|-------|-------------|
| PowerShell | PowerShell | Low | Fast | ✅ YES |
| sed | Git Bash / WSL | Medium | Very Fast | Good |
| VS Code | Text Editor | Very Low | Medium | Good for small sets |
| Notepad++ | Text Editor | Low | Medium | Alternative |
| Node.js | Node.js | Medium | Fast | If JS familiar |

**Recommendation:** Use **Method 1 (PowerShell)** - it's native to Windows, safest, and provides good feedback.

---

## Support

If you encounter any issues:
1. Verify the base path is correct
2. Ensure you have backup of files
3. Test on a single file first
4. Check file encoding (should be UTF-8)
5. Verify regex engine supports lookahead (`(?!...`)

