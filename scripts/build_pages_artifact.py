#!/usr/bin/env python3
"""Stage only the generated site and root redirect, preserving published URLs."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Leave headroom below GitHub Pages' documented 1 GB published-site limit.
MAX_SITE_BYTES = 950_000_000


def stage(out: Path | None, *, root: Path = ROOT, limit: int = MAX_SITE_BYTES) -> int:
    if out is not None and out.resolve().is_relative_to(root.resolve()):
        raise ValueError("stage the site outside the repository to avoid recursive copies")
    if out is not None and out.exists():
        raise ValueError(f"output already exists: {out}")
    sources = [root / "index.html", root / ".nojekyll", root / "pages"]
    files = []
    for source in sources:
        if not source.exists():
            raise ValueError(f"missing site input: {source}")
        candidates = [source, *source.rglob("*")] if source.is_dir() else [source]
        if any(path.is_symlink() for path in candidates):
            raise ValueError(f"site input contains a symbolic link: {source}")
        files.extend(path for path in candidates if path.is_file())
    total = sum(path.stat().st_size for path in files)
    if total > limit:
        raise ValueError(f"site is {total:,} bytes; publication budget is {limit:,} bytes")
    if out is None:
        return total
    out.mkdir(parents=True)
    for source in sources:
        if source.is_dir():
            shutil.copytree(source, out / source.name)
        else:
            shutil.copy2(source, out / source.name)
    return total


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--out", type=Path)
    mode.add_argument("--check", action="store_true", help="Check the budget without writing an artifact.")
    args = parser.parse_args()
    total = stage(args.out)
    print(f"Site publication: {total:,} bytes (budget {MAX_SITE_BYTES:,})")


if __name__ == "__main__":
    main()
