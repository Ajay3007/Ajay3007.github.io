#!/usr/bin/env python3
import argparse
from datetime import datetime
from pathlib import Path
import sys

def insert_changelog_entry(log_path: Path, date_str: str, items: list[str], dry_run: bool=False) -> str:
    if not log_path.exists():
        raise FileNotFoundError(f"Log file not found: {log_path}")
    content = log_path.read_text(encoding='utf-8')

    header = "**Changelog**"
    idx = content.find(header)
    if idx == -1:
        raise RuntimeError("Changelog header '**Changelog**' not found in log file.")

    # Find insertion point: after the header line
    lines = content.splitlines()
    try:
        header_line_index = next(i for i, l in enumerate(lines) if l.strip() == header)
    except StopIteration:
        raise RuntimeError("Exact Changelog header line not found.")

    # Build new entry block
    entry_lines = []
    entry_lines.append(f"- {date_str}:")
    for it in items:
        entry_lines.append(f"  - {it}")
    entry_lines.append("")  # trailing blank line for readability

    # Insert after header line and any existing blank line that follows
    insert_at = header_line_index + 1
    # If next line is blank, keep insert_at after it to visually separate
    if insert_at < len(lines) and lines[insert_at].strip() == "":
        insert_at += 1

    updated_lines = lines[:insert_at] + entry_lines + lines[insert_at:]
    updated = "\n".join(updated_lines) + ("\n" if not updated_lines[-1].endswith("\n") else "")

    if not dry_run:
        tmp = log_path.with_suffix(log_path.suffix + '.tmp')
        tmp.write_text(updated, encoding='utf-8')
        try:
            tmp.replace(log_path)
        except Exception:
            log_path.write_text(updated, encoding='utf-8')
    return updated


def main():
    parser = argparse.ArgumentParser(description="Append a dated changelog entry to SITE_MAINTENANCE_LOG.md.")
    parser.add_argument('--date', help="Date in YYYY-MM-DD (defaults to today)")
    parser.add_argument('--item', dest='items', action='append', required=True,
                        help="Bullet item to add (can specify multiple --item)")
    parser.add_argument('--dry-run', action='store_true', help="Print updated content to stdout without writing")
    parser.add_argument('--log', default='SITE_MAINTENANCE_LOG.md', help="Path to maintenance log file")
    args = parser.parse_args()

    date_str = args.date or datetime.now().date().isoformat()
    log_path = Path(args.log)

    try:
        updated = insert_changelog_entry(log_path, date_str, args.items, dry_run=args.dry_run)
        if args.dry_run:
            sys.stdout.write(updated)
        else:
            print(f"✅ Appended changelog entry for {date_str} to {log_path}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
