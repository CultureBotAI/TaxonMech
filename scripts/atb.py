#!/usr/bin/env python3
"""Build the full AllTheBacteria catalogue and the TaxonMech crosswalks."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from taxonmech.atb import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
