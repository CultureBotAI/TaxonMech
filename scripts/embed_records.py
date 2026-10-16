#!/usr/bin/env python3
"""Embed representative and multi-source TaxonMech records with BAAI/bge-small-en-v1.5.

Reads the published search index (`pages/index.json.gz`) or falls back to
`load_records()` when rendering a small fixture corpus, selects all 4-source
harmonized taxa (`NCBITAXON`, `GTDB`, `LPSN`, `BACDIVE`) plus representative
Archaea, Eukaryota, and Other-domain taxa, and writes L2-normalized embeddings
to `data/embeddings/corpus_embeddings.npz`.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_GZ = REPO_ROOT / "pages" / "index.json.gz"
OUT_DIR = REPO_ROOT / "data" / "embeddings"
DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"


def select_records(rows: list[dict], max_per_domain_extra: int = 300) -> list[dict]:
    """Select all 4-source harmonized taxa plus representative non-bacterial taxa."""
    if len(rows) <= 10000:
        return rows
    selected_ids: set[str] = set()
    selected: list[dict] = []

    def add(row: dict) -> None:
        ident = row["identifier"]
        if ident not in selected_ids:
            selected_ids.add(ident)
            selected.append(row)

    for row in rows:
        sources = row.get("sources") or []
        if len(sources) >= 4 or row.get("status") != "SEEDED" or row.get("domain") == "OTHER":
            add(row)

    for domain in ("ARCHAEA", "EUKARYOTA"):
        candidates = [r for r in rows if r.get("domain") == domain and r["identifier"] not in selected_ids]
        candidates.sort(
            key=lambda r: (
                len(r.get("sources") or []),
                int(bool(r.get("has_type_strain"))),
                r.get("strain_count") or 0,
                r.get("gtdb_mapping_count") or 0,
            ),
            reverse=True,
        )
        for row in candidates[:max_per_domain_extra]:
            add(row)

    return selected


def record_text(row: dict) -> str:
    """Construct a descriptive text passage for semantic embedding."""
    label = row.get("label") or row["identifier"]
    parts = label.split()
    genus = parts[0] if parts else ""
    domain = row.get("domain") or "OTHER"
    rank = row.get("rank") or "NO_RANK"
    sources = ", ".join(row.get("sources") or [])
    strains = row.get("strain_count") or 0
    typed = "with LPSN/BacDive type strain" if row.get("has_type_strain") else "without type strain"
    gtdb = row.get("gtdb_mapping_count") or 0
    status = row.get("status") or "SEEDED"
    return (
        f"Taxon: {label} ({row['identifier']}). "
        f"Genus/clade: {genus}. Domain: {domain}. Rank: {rank}. "
        f"Attested sources: {sources}. "
        f"Strain status: {typed}, {strains} BacDive strains, {gtdb} GTDB species mappings. "
        f"Curation status: {status}."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--out", type=Path, default=OUT_DIR / "corpus_embeddings.npz")
    args = parser.parse_args()

    rows = json.loads(gzip.decompress(INDEX_GZ.read_bytes()))
    selected = select_records(rows)
    texts = [record_text(r) for r in selected]
    text_hashes = [hashlib.sha256(t.encode("utf-8")).hexdigest()[:16] for t in texts]

    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(args.model)
    vectors = model.encode(
        texts,
        batch_size=args.batch_size,
        show_progress_bar=False,
        normalize_embeddings=True,
    )
    vectors = np.asarray(vectors, dtype=np.float32)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    metadata = [
        {
            "id": r["identifier"],
            "label": r.get("label") or r["identifier"],
            "domain": r.get("domain") or "OTHER",
            "rank": r.get("rank") or "NO_RANK",
            "status": r.get("status") or "SEEDED",
            "sources": r.get("sources") or [],
            "source_count": len(r.get("sources") or []),
            "strain_count": r.get("strain_count") or 0,
            "has_type_strain": bool(r.get("has_type_strain")),
            "gtdb_mapping_count": r.get("gtdb_mapping_count") or 0,
            "page": r.get("page") or f"taxon.html?id={r['identifier']}",
            "text_hash": h,
        }
        for r, h in zip(selected, text_hashes, strict=True)
    ]
    np.savez_compressed(
        args.out,
        embeddings=vectors,
        metadata_json=np.array(json.dumps(metadata, ensure_ascii=False)),
        model=np.array(args.model),
    )
    print(f"Embedded {len(selected)} TaxonMech records ({vectors.shape[1]}d) -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
