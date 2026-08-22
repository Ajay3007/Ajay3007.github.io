#!/usr/bin/env python3
"""
Validation script to check for common site maintenance issues before commit.
Scans for:
- Mojibake/corrupted emoji sequences
- External links missing new-tab attributes
- Icon paths with /ajdevhub/ prefix
- Image src without relative_url
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

def check_mojibake(files: List[Path]) -> List[Tuple[Path, int, str]]:
    """Check for mojibake/corrupted emoji patterns."""
    issues = []
    pattern = re.compile(r'ðŸ|ï¸')
    for fpath in files:
        try:
            content = fpath.read_text(encoding='utf-8', errors='replace')
            for i, line in enumerate(content.splitlines(), 1):
                if pattern.search(line):
                    issues.append((fpath, i, f"Mojibake detected: {line[:80]}"))
        except Exception as e:
            pass
    return issues

def check_external_links_no_newtab(files: List[Path]) -> List[Tuple[Path, int, str]]:
    """Check for external links missing target=_blank attribute."""
    issues = []
    # Match markdown links to http/https without the new-tab attribute following
    pattern = re.compile(r'\[([^\]]+)\]\((https?://[^)]+)\)(?!\{:target)')
    for fpath in files:
        try:
            content = fpath.read_text(encoding='utf-8', errors='replace')
            for i, line in enumerate(content.splitlines(), 1):
                if pattern.search(line):
                    issues.append((fpath, i, f"External link missing target=_blank: {line[:80]}"))
        except Exception as e:
            pass
    return issues

def check_ajdevhub_paths(files: List[Path]) -> List[Tuple[Path, int, str]]:
    """Check for stale /ajdevhub/ asset paths."""
    issues = []
    pattern = re.compile(r'/ajdevhub/')
    for fpath in files:
        try:
            content = fpath.read_text(encoding='utf-8', errors='replace')
            for i, line in enumerate(content.splitlines(), 1):
                if pattern.search(line):
                    issues.append((fpath, i, f"Stale /ajdevhub/ path: {line[:80]}"))
        except Exception as e:
            pass
    return issues

def check_absolute_internal_links(files: List[Path]) -> List[Tuple[Path, int, str]]:
    """Check for absolute internal markdown links not using relative_url."""
    issues = []
    # Match markdown links to /... that don't already use relative_url
    pattern = re.compile(r'\]\(/(learning|projects|blogs|blog|about|assets|images)(?!.*relative_url)')
    for fpath in files:
        try:
            content = fpath.read_text(encoding='utf-8', errors='replace')
            for i, line in enumerate(content.splitlines(), 1):
                if pattern.search(line) and 'relative_url' not in line:
                    issues.append((fpath, i, f"Absolute internal link: {line[:80]}"))
        except Exception as e:
            pass
    return issues

def check_image_src_no_relative_url(files: List[Path]) -> List[Tuple[Path, int, str]]:
    """Check for image src with absolute paths not using relative_url."""
    issues = []
    # Match img src="/assets/..." that don't use relative_url filter
    pattern = re.compile(r'src=["\']/(assets|images)/[^"\']*["\'](?!.*relative_url)')
    for fpath in files:
        try:
            content = fpath.read_text(encoding='utf-8', errors='replace')
            for i, line in enumerate(content.splitlines(), 1):
                if pattern.search(line) and 'relative_url' not in line:
                    issues.append((fpath, i, f"Image src missing relative_url: {line[:80]}"))
        except Exception as e:
            pass
    return issues

def main():
    # Scan the learning collection. This was `learning/` until the content moved
    # into the Jekyll collection at `_learning/`, after which the script silently
    # exited 0 on every run without checking anything.
    learning_dir = Path('_learning')
    if not learning_dir.exists():
        print("❌ _learning/ directory not found. Run this from the repository root.")
        return 1

    # manim-scripts is video tooling, excluded from the site build.
    md_files = [p for p in learning_dir.rglob('*.md') if 'manim-scripts' not in p.parts]
    layout_files = list(Path('_layouts').rglob('*.html')) if Path('_layouts').exists() else []
    all_files = md_files + layout_files

    if not all_files:
        print("⚠️ No markdown or layout files found.")
        return 1

    # Run checks
    checks = [
        ("Mojibake/corrupted emojis", check_mojibake),
        ("External links without new-tab", check_external_links_no_newtab),
        ("Stale /ajdevhub/ paths", check_ajdevhub_paths),
        ("Absolute internal links", check_absolute_internal_links),
        ("Image src without relative_url", check_image_src_no_relative_url),
    ]

    total_issues = 0
    for check_name, check_fn in checks:
        issues = check_fn(all_files)
        if issues:
            print(f"\n⚠️ {check_name} ({len(issues)} found):")
            for fpath, line_no, msg in issues[:10]:  # Show first 10
                print(f"  {fpath}:{line_no} - {msg}")
            if len(issues) > 10:
                print(f"  ... and {len(issues) - 10} more")
            total_issues += len(issues)
        else:
            print(f"✅ {check_name}: OK")

    print(f"\n{'='*60}")
    if total_issues == 0:
        print(f"✅ All checks passed! ({len(all_files)} files scanned)")
    else:
        print(f"❌ {total_issues} issue(s) found. Fix before committing.")
    print(f"{'='*60}")
    return 1 if total_issues else 0

if __name__ == '__main__':
    sys.exit(main())
