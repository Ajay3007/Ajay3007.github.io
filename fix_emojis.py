#!/usr/bin/env python3
from pathlib import Path
from ftfy import fix_text

def repair_file(path: Path) -> bool:
    # Read with replacement to avoid decode errors, then fix text.
    raw = path.read_text(encoding='utf-8', errors='replace')
    fixed = fix_text(raw)
    if fixed != raw:
        # Write back atomically when possible.
        tmp = path.with_suffix(path.suffix + '.tmp')
        tmp.write_text(fixed, encoding='utf-8')
        try:
            tmp.replace(path)
        except Exception:
            path.write_text(fixed, encoding='utf-8')
        return True
    return False

def main():
    learning_dir = Path('learning')
    fixed = []
    errors = []
    for md in learning_dir.rglob('*.md'):
        try:
            if repair_file(md):
                fixed.append(str(md))
        except Exception as e:
            errors.append((str(md), str(e)))

    print(f"📊 Total files fixed: {len(fixed)}")
    for f in fixed[:50]:
        print(f"  ✅ {f}")
    if len(fixed) > 50:
        print(f"  ... {len(fixed) - 50} more")
    if errors:
        print(f"\n⚠️ Errors: {len(errors)}")
        for p, e in errors[:10]:
            print(f"  - {p} -> {e}")

if __name__ == '__main__':
    main()
