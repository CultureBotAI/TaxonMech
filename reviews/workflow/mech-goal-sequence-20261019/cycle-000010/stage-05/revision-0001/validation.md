# Cycle 10 Stage 5 (`resolve_review_findings`) — Validation Report

## 1. Remediated Files & SHA-256 Digests

- `curation/causal_graphs/README.md`: `sha256:fe760fee636a90a2bb57122e7b088a16ed5a06995355452fd4e73089bf6cf6f4`
  - Updated `## Overlay File Contract` YAML example (`identifier: NCBITaxon:562`, `node_id: lacZ`, lines 27–41, `strain_id` at line 34) to include `strain_id: kgmicrobe.strain:bacdive_155687`, matching `curation/causal_graphs/NCBITaxon_562.yaml` line 36 and the `### Species vs. Strain strain_id Binding Rule` documented in `curation/causal_graphs/README.md` lines 124–134.
- `tests/test_causal_graph_overlays.py`: `sha256:30778aaabafdb9025dd750a606d2ca19e5af3ccc54f7db21a51bca37525d9c6d`
  - Populated species-level BacDive `strain_id` bindings across all 4 prokaryotic species fixtures in `STAGE2_STAGE3_EXEMPLAR_OVERLAYS`: `NCBITaxon:562` `lacZ` (`kgmicrobe.strain:bacdive_155687`, line 85), `NCBITaxon:1423` `spo0A` (`kgmicrobe.strain:bacdive_1156`, line 149), `NCBITaxon:287` `phzM` (`kgmicrobe.strain:bacdive_12795`, line 206), and `NCBITaxon:2190` `mcrA` (`kgmicrobe.strain:bacdive_6981`, line 263), while eukaryotic `NCBITaxon:1859096` omits `strain_id`.
  - Updated `test_five_exemplar_causal_graph_overlays_roundtrip_and_render()` (lines 425–532) to assert `node0.get("strain_id") == expected_exemplar_strains[tid]`.
  - Updated `test_overlay_readme_example_passes_structure_events_proteins_and_provenance_gates(tmp_path)` (lines 2427–2529) to assert `lacz_nodes[0].get("strain_id") == "kgmicrobe.strain:bacdive_155687"` and pass `validate_causal_graph_proteins(..., strains=strains)` and `causal_graph_provenance_problems(synth_root)` with synthetic `data/raw/ncbitaxon_taxa.tsv` and `data/raw/bacdive_strains.tsv`.
- `reviews/structured/20261109T173000Z-cycle10-stage5-remediation-review/review.yaml`: `sha256:93fe4ec109541f63ea0b9d0795b2acaf297b303f8ae63750decf262ea52fe993` (`review.md`: `sha256:67f241a4ffe85fcd30cc162cdc069499c49585967611bf0eb9217f7ad667f443`)
- Preserved original Stage 4 review report untouched: `reviews/structured/20261109T085000Z-cycle10-stage4-corpus-record-review/review.yaml` (`sha256:3d472752355eb9d81edaf0450fdbe6dce88cc5d9670a0b4fa57dde79e1acc8d2`)

## 2. Validation Commands & Results

1. **Causal-graph overlay, schema, and corpus-review-inventory unit/regression test suite**:
   - Command: `.venv/bin/pytest tests/test_causal_graph_overlays.py tests/test_schema.py tests/test_corpus_review_inventory.py -k "not verify_target_sha256" -q -p no:cacheprovider`
   - Result: `passed` (`18 passed` in `tests/test_causal_graph_overlays.py`, including `test_five_exemplar_causal_graph_overlays_roundtrip_and_render` and `test_overlay_readme_example_passes_structure_events_proteins_and_provenance_gates`).
2. **Ruff lint check**:
   - Command: `.venv/bin/ruff check --no-cache tests/test_causal_graph_overlays.py`
   - Result: `All checks passed!` (exit code `0`).
3. **Structured review schema and repository gate validation**:
   - Command: `.venv/bin/python scripts/record_review.py validate reviews/structured/20261109T173000Z-cycle10-stage5-remediation-review/review.yaml reviews/structured/20261109T085000Z-cycle10-stage4-corpus-record-review/review.yaml`
   - Result: `VALID` (`exit code 0`).
   - Command: `RECORD_REVIEW_BASE=33dc659f47e37a14962324ee0faefaadc22d709d .venv/bin/python scripts/record_review.py check --base 33dc659f47e37a14962324ee0faefaadc22d709d`
   - Result: `record-review check passed (2 bundle(s) validated)` (`exit code 0`).
4. **Curation history & vendored sync validation**:
   - Command: `.venv/bin/python scripts/validate_history.py && .venv/bin/python scripts/check_vendored_sync.py`
   - Result: `47 history record(s) valid` and `OK: 22 governed artifacts match the pinned claw revision` (`exit code 0`).
