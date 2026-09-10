#!/usr/bin/env python3
"""Compatibility CLI for :mod:`taxonmech.extract`."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from taxonmech.extract import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
