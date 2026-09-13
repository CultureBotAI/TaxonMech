#!/usr/bin/env python3
"""List source coverage or find exact identifiers in complete native catalogs."""

import argparse
import json

from taxonmech.source_catalog import check, load_manifest, query


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source")
    parser.add_argument("--identifier")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        failures = check()
        if failures:
            raise SystemExit("\n".join(failures))
        print("Complete source catalog hashes, dependencies and census counts verified.")
        return
    manifest = load_manifest()
    if not args.source:
        if args.identifier:
            parser.error("--identifier requires --source")
        print(json.dumps(manifest, indent=2, ensure_ascii=False))
        return
    source = next((item for item in manifest["sources"] if item["id"] == args.source), None)
    if source is None:
        parser.error("unknown source; run without arguments to list source IDs")
    result = query(source, args.identifier, limit=args.limit) if args.identifier else source
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
