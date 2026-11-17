#!/usr/bin/env python3
"""Project TaxonMech text embeddings to 2D with PaCMAP (`data/embeddings/corpus_map.json`)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IN = REPO_ROOT / "data" / "embeddings" / "corpus_embeddings.npz"
DEFAULT_OUT = REPO_ROOT / "data" / "embeddings" / "corpus_map.json"


def project_2d(vectors: np.ndarray) -> np.ndarray:
    centered = vectors - vectors.mean(axis=0, keepdims=True)
    norms = np.linalg.norm(centered, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    normed = centered / norms

    import pacmap

    n_neighbors = max(2, min(10, len(normed) - 1))
    reducer = pacmap.PaCMAP(
        n_components=2,
        n_neighbors=n_neighbors,
        MN_ratio=0.5,
        FP_ratio=2.0,
        apply_pca=False,
        random_state=42,
    )
    coords = reducer.fit_transform(normed, init="pca")
    mins = coords.min(axis=0)
    maxs = coords.max(axis=0)
    span = np.where((maxs - mins) == 0, 1.0, maxs - mins)
    scaled = (coords - mins) / span
    return scaled


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_IN)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    data = np.load(args.input, allow_pickle=False)
    vectors = data["embeddings"].astype(np.float32)
    metadata = json.loads(str(data["metadata_json"]))
    model_name = str(data["model"])

    coords = project_2d(vectors)
    points = []
    for meta, (x, y) in zip(metadata, coords, strict=True):
        points.append(
            {
                "id": meta["id"],
                "label": meta["label"],
                "domain": meta["domain"],
                "rank": meta["rank"],
                "status": meta["status"],
                "sources": meta["sources"],
                "source_count": meta["source_count"],
                "strain_count": meta["strain_count"],
                "has_type_strain": meta["has_type_strain"],
                "gtdb_mapping_count": meta["gtdb_mapping_count"],
                "page": meta["page"],
                "x": round(float(x), 4),
                "y": round(float(y), 4),
            }
        )

    payload = {
        "model": model_name,
        "dim": int(vectors.shape[1]),
        "method": (
            "PaCMAP (n_neighbors=10, MN_ratio=0.5, FP_ratio=2.0, init=pca) "
            "on mean-centered L2-normalized vectors"
        ),
        "count": len(points),
        "points": points,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    out_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n"
    args.out.write_text(out_json, encoding="utf-8")
    print(f"Wrote 2D embedding map ({len(points)} points) -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
