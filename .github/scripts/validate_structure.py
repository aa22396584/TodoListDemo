#!/usr/bin/env python3
"""
Structure & Documentation Validator for TodoListDemo.

This script:
1. Identifies all category directories and active submodules.
2. Ensures every submodule contains a README.md file.
3. Validates relative links across all Markdown documentation files.
4. Exits 0 on success, or 1 on validation errors with diagnostic output.
"""

import sys
import os
import re
from pathlib import Path

# Path setup
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent

EXCLUDE_DIRS = {
    '.git',
    '.agents',
    '.github',
    '.vscode',
    'node_modules',
    'dist',
    'build',
    'target',
    '.venv',
    'venv',
    '__pycache__',
}


def strip_code_blocks(text: str) -> str:
    """Strips fenced code blocks (```...```) to prevent false-positive link matches."""
    return re.sub(r'```[\s\S]*?```', '', text)


def scan_submodules(repo_root: Path):
    """Scans category directories and verifies that every submodule contains a README.md."""
    print("🔍 [1/2] Scanning submodules for README.md completeness...")
    
    category_dirs = []
    for entry in sorted(repo_root.iterdir()):
        if entry.is_dir() and entry.name not in EXCLUDE_DIRS and not entry.name.startswith('.'):
            # Category directories typically match patterns like 01-vanilla, 03-modern-frameworks, etc.
            # Or contain sub-directories
            subdirs = [d for d in entry.iterdir() if d.is_dir() and not d.name.startswith('.') and d.name not in EXCLUDE_DIRS]
            if subdirs:
                category_dirs.append((entry, subdirs))
    
    total_submodules = 0
    missing_readmes = []
    
    for category_path, submodules in category_dirs:
        for submodule in sorted(submodules):
            total_submodules += 1
            readme = submodule / "README.md"
            if not readme.is_file():
                rel_path = submodule.relative_to(repo_root)
                missing_readmes.append(str(rel_path))
    
    print(f"   Found {len(category_dirs)} category directories and {total_submodules} submodules.")
    
    if missing_readmes:
        print(f"❌ ERROR: Found {len(missing_readmes)} submodule(s) missing README.md:")
        for missing in missing_readmes:
            print(f"   - {missing}/README.md")
    else:
        print(f"✅ All {total_submodules} submodules have a valid README.md!")
        
    return total_submodules, missing_readmes


def validate_relative_links(repo_root: Path):
    """Scans all Markdown files and verifies relative link targets exist."""
    print("\n🔍 [2/2] Validating relative links in Markdown files...")
    
    md_files = []
    for root, dirs, files in os.walk(repo_root):
        # Prune excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)
    
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    broken_links = []
    total_links_checked = 0
    
    for md_path in md_files:
        rel_file = md_path.relative_to(repo_root)
        try:
            raw_content = md_path.read_text(encoding='utf-8', errors='ignore')
        except Exception as e:
            print(f"⚠️ Warning: Could not read {rel_file}: {e}")
            continue
            
        cleaned_content = strip_code_blocks(raw_content)
        
        for text, url in link_pattern.findall(cleaned_content):
            url = url.strip()
            # Ignore external, mailto, anchor-only links
            if url.startswith(('http://', 'https://', 'mailto:', '#', 'ftp://', 'data:', 'tel:')):
                continue
                
            clean_url = url.split('#')[0].strip()
            if not clean_url:
                continue
                
            total_links_checked += 1
            target_path = (md_path.parent / clean_url).resolve()
            
            if not target_path.exists():
                broken_links.append((str(rel_file), text, url))
                
    print(f"   Scanned {len(md_files)} Markdown files, checked {total_links_checked} relative links.")
    
    if broken_links:
        print(f"❌ ERROR: Found {len(broken_links)} broken relative link(s):")
        for file_path, text, url in broken_links:
            print(f"   - In {file_path}: [{text}]({url}) -> Target file does not exist")
    else:
        print("✅ All relative links are valid!")
        
    return len(md_files), total_links_checked, broken_links


def main():
    print("=" * 60)
    print("🚀 TodoListDemo Project Structure & Documentation Validator")
    print(f"📁 Repository Root: {REPO_ROOT}")
    print("=" * 60)
    
    total_submodules, missing_readmes = scan_submodules(REPO_ROOT)
    total_md_files, total_links_checked, broken_links = validate_relative_links(REPO_ROOT)
    
    print("\n" + "=" * 60)
    print("📊 Validation Summary:")
    print(f"   - Category directories scanned: {total_submodules} submodules validated")
    print(f"   - Missing READMEs: {len(missing_readmes)}")
    print(f"   - Markdown files scanned: {total_md_files}")
    print(f"   - Relative links checked: {total_links_checked}")
    print(f"   - Broken links found: {len(broken_links)}")
    print("=" * 60)
    
    if missing_readmes or broken_links:
        print("❌ RESULT: Structure validation FAILED!")
        sys.exit(1)
    else:
        print("🎉 RESULT: Structure validation PASSED successfully!")
        sys.exit(0)


if __name__ == '__main__':
    main()
