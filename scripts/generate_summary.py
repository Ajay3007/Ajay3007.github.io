#!/usr/bin/env python3
"""
Automated Summary Generator for Markdown Files
===============================================

This script analyzes markdown files and generates comprehensive executive summaries
similar to the TaxHrd documentation style.

Usage:
    python generate_summary.py <file_path>
    python generate_summary.py --batch learning/dsa/
    python generate_summary.py --all

Author: Ajay Gupta
Date: December 2025
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from datetime import datetime


class MarkdownSummaryGenerator:
    """Generates executive summaries for markdown documentation files."""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.content = ""
        self.lines = []
        self.has_frontmatter = False
        self.frontmatter_end = 0
        
    def read_file(self) -> bool:
        """Read the markdown file content."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
                self.lines = self.content.split('\n')
            return True
        except Exception as e:
            print(f"❌ Error reading {self.file_path}: {e}")
            return False
    
    def detect_frontmatter(self) -> None:
        """Detect YAML frontmatter if present."""
        if self.lines and self.lines[0].strip() == '---':
            for i, line in enumerate(self.lines[1:], 1):
                if line.strip() == '---':
                    self.has_frontmatter = True
                    self.frontmatter_end = i + 1
                    break
    
    def extract_headings(self) -> List[Tuple[int, str, str]]:
        """Extract all headings with their levels and text."""
        headings = []
        for i, line in enumerate(self.lines):
            if line.strip().startswith('#'):
                match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
                if match:
                    level = len(match.group(1))
                    text = match.group(2).strip()
                    headings.append((level, text, i))
        return headings
    
    def extract_code_blocks(self) -> int:
        """Count code blocks in the document."""
        return len(re.findall(r'```[\s\S]*?```', self.content))
    
    def extract_lists(self) -> int:
        """Count bullet/numbered lists."""
        list_count = 0
        for line in self.lines:
            if re.match(r'^\s*[-*+]\s+', line) or re.match(r'^\s*\d+\.\s+', line):
                list_count += 1
        return list_count
    
    def extract_links(self) -> List[str]:
        """Extract all markdown links."""
        return re.findall(r'\[([^\]]+)\]\(([^)]+)\)', self.content)
    
    def estimate_reading_time(self) -> int:
        """Estimate reading time in minutes (250 words/min)."""
        words = len(re.findall(r'\b\w+\b', self.content))
        return max(1, words // 250)
    
    def analyze_content(self) -> Dict[str, any]:
        """Analyze document structure and content."""
        headings = self.extract_headings()
        code_blocks = self.extract_code_blocks()
        lists = self.extract_lists()
        links = self.extract_links()
        reading_time = self.estimate_reading_time()
        
        # Categorize headings by level
        h1_count = sum(1 for h in headings if h[0] == 1)
        h2_count = sum(1 for h in headings if h[0] == 2)
        h3_count = sum(1 for h in headings if h[0] == 3)
        
        # Extract main topics (H2 headings)
        main_topics = [h[1] for h in headings if h[0] == 2]
        
        return {
            'total_lines': len(self.lines),
            'headings': headings,
            'h1_count': h1_count,
            'h2_count': h2_count,
            'h3_count': h3_count,
            'main_topics': main_topics,
            'code_blocks': code_blocks,
            'lists': lists,
            'links': links,
            'reading_time': reading_time,
        }
    
    def generate_toc(self, headings: List[Tuple[int, str, int]]) -> str:
        """Generate hierarchical Table of Contents from all headings (H1-H6)."""
        if not headings:
            return ""
        
        toc = []
        toc.append("## 📑 Table of Contents")
        toc.append("")
        
        # Track numbering for each level
        counters = [0, 0, 0, 0, 0, 0]  # For H1-H6
        
        for level, heading, _ in headings:
            if level > 6:  # Skip any heading deeper than H6
                continue
            
            # Create anchor link matching Jekyll/Kramdown behavior exactly
            # Check if heading starts with non-ASCII character (emoji)
            starts_with_emoji = heading and ord(heading[0]) > 127
            
            anchor = heading
            # Remove all emojis and special unicode (anything above ASCII 127)
            anchor = ''.join(char if ord(char) < 128 else ' ' for char in anchor)
            # Convert to lowercase
            anchor = anchor.lower()
            # Replace common punctuation with spaces first
            for char in '()[]{}:;,.!?"\'/\\|':
                anchor = anchor.replace(char, ' ')
            # Replace whitespace with single hyphens
            anchor = re.sub(r'\s+', '-', anchor)
            # Remove any remaining non-alphanumeric except hyphens
            anchor = re.sub(r'[^a-z0-9-]', '', anchor)
            # Remove multiple consecutive hyphens
            anchor = re.sub(r'-+', '-', anchor)
            # Remove leading/trailing hyphens
            anchor = anchor.strip('-')
            
            # If heading started with emoji, Jekyll adds leading hyphen
            if starts_with_emoji and anchor:
                anchor = '-' + anchor
            
            # Update counters
            counters[level - 1] += 1
            # Reset deeper level counters
            for i in range(level, 6):
                counters[i] = 0
            
            # Create numbering (e.g., 1, 1.1, 1.1.1)
            number_parts = [str(counters[i]) for i in range(level) if counters[i] > 0]
            number = '.'.join(number_parts)
            
            # Create indentation based on level
            indent = '  ' * (level - 1)
            
            # Format TOC entry
            if level == 1:
                toc.append(f"{number}. **[{heading}](#{anchor})**")
            else:
                toc.append(f"{indent}{number}. [{heading}](#{anchor})")
        
        toc.append("")
        toc.append("---")
        toc.append("")
        
        return '\n'.join(toc)
    
    def generate_summary(self) -> str:
        """Generate comprehensive executive summary."""
        analysis = self.analyze_content()
        
        summary = []
        
        # Add Table of Contents first
        toc = self.generate_toc(analysis['headings'])
        if toc:
            summary.append(toc)
        
        # Main Topics
        if analysis['main_topics']:
            summary.append("### 🎯 Main Topics Covered")
            summary.append("")
            for i, topic in enumerate(analysis['main_topics'][:8], 1):
                # Clean emojis and special chars from topic
                clean_topic = re.sub(r'[^\w\s-]', '', topic).strip()
                summary.append(f"{i}. **{clean_topic}**")
            if len(analysis['main_topics']) > 8:
                summary.append(f"... and {len(analysis['main_topics']) - 8} more")
            summary.append("")
        
        summary.append("---")
        summary.append("")
        
        return '\n'.join(summary)
    
    def insert_summary(self) -> str:
        """Insert summary after frontmatter or at the beginning."""
        summary = self.generate_summary()
        
        if self.has_frontmatter:
            # Insert after frontmatter
            before = self.lines[:self.frontmatter_end]
            after = self.lines[self.frontmatter_end:]
            
            # Check if summary/TOC already exists
            if any('Table of Contents' in line or 'Main Topics Covered' in line for line in after[:30]):
                print("⚠️  Summary/TOC section already exists. Skipping...")
                return None
            
            return '\n'.join(before) + '\n\n' + summary + '\n'.join(after)
        else:
            # Check if summary/TOC already exists
            if any('Table of Contents' in line or 'Main Topics Covered' in line for line in self.lines[:30]):
                print("⚠️  Summary/TOC section already exists. Skipping...")
                return None
            
            # Insert at the beginning
            return summary + '\n'.join(self.lines)
    
    def write_file(self, content: str) -> bool:
        """Write updated content back to file."""
        try:
            # Backup original file
            backup_path = self.file_path.with_suffix('.md.bak')
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(self.lines))
            
            # Write new content
            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Summary added to {self.file_path}")
            print(f"   Backup saved: {backup_path}")
            return True
        except Exception as e:
            print(f"❌ Error writing {self.file_path}: {e}")
            return False
    
    def process(self) -> bool:
        """Main processing pipeline."""
        if not self.read_file():
            return False
        
        self.detect_frontmatter()
        new_content = self.insert_summary()
        
        if new_content is None:
            return False
        
        return self.write_file(new_content)


def process_file(file_path: str) -> bool:
    """Process a single markdown file."""
    print(f"\n📄 Processing: {file_path}")
    generator = MarkdownSummaryGenerator(file_path)
    return generator.process()


def process_directory(directory: str, recursive: bool = True) -> None:
    """Process all markdown files in a directory."""
    path = Path(directory)
    
    if not path.exists():
        print(f"❌ Directory not found: {directory}")
        return
    
    pattern = "**/*.md" if recursive else "*.md"
    md_files = list(path.glob(pattern))
    
    if not md_files:
        print(f"⚠️  No markdown files found in {directory}")
        return
    
    print(f"\n📁 Found {len(md_files)} markdown files in {directory}")
    print("=" * 60)
    
    success_count = 0
    skip_count = 0
    fail_count = 0
    
    for md_file in md_files:
        # Skip index files (usually don't need summaries)
        if md_file.name.lower() == 'index.md':
            skip_count += 1
            continue
        
        # Skip README files
        if md_file.name.lower() == 'readme.md':
            skip_count += 1
            continue
        
        if process_file(str(md_file)):
            success_count += 1
        else:
            fail_count += 1
    
    print("\n" + "=" * 60)
    print(f"✅ Successfully processed: {success_count}")
    print(f"⏭️  Skipped: {skip_count}")
    print(f"❌ Failed: {fail_count}")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file:  python generate_summary.py <file.md>")
        print("  Directory:    python generate_summary.py --batch <directory>")
        print("  All learning: python generate_summary.py --all")
        print("\nExamples:")
        print("  python generate_summary.py learning/dsa/Arrays/index.md")
        print("  python generate_summary.py --batch learning/dsa/")
        print("  python generate_summary.py --all")
        return
    
    arg = sys.argv[1]
    
    if arg == "--all":
        # Process all learning directories
        base = Path("learning")
        if not base.exists():
            print("❌ learning/ directory not found")
            return
        
        for subdir in ["dsa", "oop", "system-design", "networking", "operating-systems", "finance"]:
            dir_path = base / subdir
            if dir_path.exists():
                process_directory(str(dir_path), recursive=True)
    
    elif arg == "--batch":
        if len(sys.argv) < 3:
            print("❌ Please specify directory: python generate_summary.py --batch <directory>")
            return
        process_directory(sys.argv[2], recursive=True)
    
    else:
        # Single file
        if not os.path.exists(arg):
            print(f"❌ File not found: {arg}")
            return
        process_file(arg)


if __name__ == "__main__":
    main()