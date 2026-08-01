#!/usr/bin/env python3
"""
Release Packaging & Checksum Generator Script for TodoListDemo.

This script:
1. Categorizes project submodules into 4 target category zip archives:
   - todolist-web-apps.zip
   - todolist-backend-apis.zip
   - todolist-mobile-desktop.zip
   - todolist-blockchain-games.zip
2. Packages the clean full repository into todolist-full-repo.tar.gz.
3. Excludes .git, .agents, build artifacts, temporary caches, and node_modules.
4. Generates SHA256SUMS file containing checksums of all 5 release artifacts.
"""

import os
import sys
import argparse
import hashlib
import zipfile
import tarfile
from pathlib import Path
from typing import List, Dict

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent

EXCLUDE_DIRS = {
    '.git',
    '.agents',
    '.vscode',
    '.idea',
    'node_modules',
    'dist',
    'build',
    'target',
    'bin',
    'obj',
    'out',
    '.next',
    '.nuxt',
    '.svelte-kit',
    'coverage',
    '.venv',
    'venv',
    '__pycache__',
    '.pytest_cache',
    '.mypy_cache',
    '.dart_tool',
    '.pub-cache',
    '.flutter-plugins',
    '.flutter-plugins-dependencies',
}

EXCLUDE_FILES = {
    '.DS_Store',
    'Thumbs.db',
}

EXCLUDE_EXTENSIONS = {
    '.pyc',
    '.pyo',
    '.suo',
    '.user',
}

CATEGORY_MAP: Dict[str, List[str]] = {
    "todolist-web-apps.zip": [
        "01-vanilla",
        "03-modern-frameworks",
        "04-metaframeworks",
        "05-ui-libraries",
        "10-pwa",
        "11-blazor",
        "14-state-management",
    ],
    "todolist-backend-apis.zip": [
        "10-backend-apis",
    ],
    "todolist-mobile-desktop.zip": [
        "06-mobile-crossplatform",
        "07-mobile-native",
        "08-desktop",
    ],
    "todolist-blockchain-games.zip": [
        "09-game-engines",
        "12-blockchain",
    ],
}


def should_exclude(path: Path, output_dir: Path) -> bool:
    """Check if a path or any of its parents should be excluded."""
    try:
        path.relative_to(output_dir)
        return True
    except ValueError:
        pass

    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True
        if part.startswith('.git'):
            return True

    if path.is_file():
        if path.name in EXCLUDE_FILES or path.suffix.lower() in EXCLUDE_EXTENSIONS:
            return True

    return False


def compute_sha256(file_path: Path) -> str:
    """Compute SHA256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


def build_zip_archive(archive_path: Path, source_dirs: List[str], repo_root: Path, output_dir: Path):
    """Build a zip archive containing the specified source directories."""
    print(f"📦 Packaging {archive_path.name}...")
    file_count = 0
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for src_dir_name in source_dirs:
            src_dir = repo_root / src_dir_name
            if not src_dir.exists():
                print(f"   ⚠️ Directory {src_dir_name} not found, skipping...")
                continue
            for root, dirs, files in os.walk(src_dir):
                root_path = Path(root)
                dirs[:] = [
                    d for d in dirs
                    if not should_exclude(root_path / d, output_dir)
                ]
                for file in files:
                    file_path = root_path / file
                    if should_exclude(file_path, output_dir):
                        continue
                    arcname = file_path.relative_to(repo_root)
                    zipf.write(file_path, arcname)
                    file_count += 1
    size_mb = archive_path.stat().st_size / (1024 * 1024)
    print(f"   ✅ Created {archive_path.name}: {file_count} files ({size_mb:.2f} MB)")


def build_full_repo_tar(archive_path: Path, repo_root: Path, output_dir: Path):
    """Build tar.gz archive of the full repository ignoring build artifacts and metadata."""
    print(f"📦 Packaging {archive_path.name}...")
    file_count = 0
    with tarfile.open(archive_path, 'w:gz') as tarf:
        for root, dirs, files in os.walk(repo_root):
            root_path = Path(root)
            dirs[:] = [
                d for d in dirs
                if not should_exclude(root_path / d, output_dir)
            ]
            for file in files:
                file_path = root_path / file
                if should_exclude(file_path, output_dir):
                    continue
                arcname = file_path.relative_to(repo_root)
                tarf.add(file_path, arcname=str(arcname))
                file_count += 1
    size_mb = archive_path.stat().st_size / (1024 * 1024)
    print(f"   ✅ Created {archive_path.name}: {file_count} files ({size_mb:.2f} MB)")


def main():
    parser = argparse.ArgumentParser(description="Package TodoListDemo release artifacts and generate SHA256SUMS.")
    parser.add_argument("--output-dir", type=str, default="release_assets", help="Output directory for archives and checksums.")
    args = parser.parse_args()

    output_dir = (REPO_ROOT / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("🚀 TodoListDemo Automated Release Packaging")
    print(f"📁 Repository Root: {REPO_ROOT}")
    print(f"📁 Output Directory: {output_dir}")
    print("=" * 60)

    generated_artifacts = []

    # 1. Build category zip archives
    for zip_name, source_dirs in CATEGORY_MAP.items():
        zip_path = output_dir / zip_name
        build_zip_archive(zip_path, source_dirs, REPO_ROOT, output_dir)
        generated_artifacts.append(zip_path)

    # 2. Build full repo tar.gz archive
    tar_name = "todolist-full-repo.tar.gz"
    tar_path = output_dir / tar_name
    build_full_repo_tar(tar_path, REPO_ROOT, output_dir)
    generated_artifacts.append(tar_path)

    # 3. Generate SHA256SUMS
    checksum_file = output_dir / "SHA256SUMS"
    print(f"\n🔑 Generating {checksum_file.name}...")
    checksum_lines = []
    for artifact in generated_artifacts:
        sha256 = compute_sha256(artifact)
        line = f"{sha256}  {artifact.name}"
        checksum_lines.append(line)
        print(f"   - {artifact.name}: {sha256}")

    checksum_file.write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")
    print(f"✅ Checksum file created at: {checksum_file}")

    print("\n" + "=" * 60)
    print("🎉 All 5 release archives and SHA256SUMS generated successfully!")
    print("=" * 60)


if __name__ == '__main__':
    main()
