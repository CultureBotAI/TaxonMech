"""Verify exact optional shared contract source for CLAW #767 (2026-11-07).

Inputs: explicit CLAW checkout; outputs: checked Git pin and import origin.
"""

import argparse
import subprocess
from pathlib import Path

from kg_microbe_curation import native

from taxonmech.edge_curation import CLAW_COMMIT


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--claw-root", type=Path, required=True)
    root = parser.parse_args().claw_root.resolve()
    if Path(native.__file__).resolve().parent != root / "src/kg_microbe_curation":
        raise ValueError("Shared contract imported from an unexpected checkout")
    head = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    if head != CLAW_COMMIT or native.NATIVE_CONTRACT != "kg-microbe-native-assertion/v1":
        raise ValueError("Shared contract pin/version mismatch")
    if subprocess.check_output(
        ["git", "-C", str(root), "status", "--porcelain", "--", "src/kg_microbe_curation"], text=True
    ):
        raise ValueError("Shared source differs from the exact pinned commit")
    print(f"Verified shared contract source {head}")


if __name__ == "__main__":
    main()
