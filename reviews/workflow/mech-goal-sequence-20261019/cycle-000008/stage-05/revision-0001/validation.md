# Cycle 8 Stage 5 (`resolve_review_findings`) — Validation & Post-Remediation Review Summary

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `8`
- **Stage**: `5` (`resolve_review_findings`)
- **Source Revision**: `99c544dd1744ed282c1d339f6a4a761e2edc327a`
- **Previous Evidence**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/evidence.yaml` (`sha256: faa4c0e49a384bfa0416ba743916c946a0cbda69911ab26c146f75cfe2d7705f`)

## 1. Validation Commands & Results

1. **Workflow Profile Validation (`workflow/mech-workflow.yaml`)**:
   ```bash
   /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python \
     -m kg_microbe_workflows validate \
     --profile workflow/mech-workflow.yaml \
     --parent workflow/parent/mech-cycle.yaml \
     --schema workflow/parent/workflow.yaml
   ```
   - **Result**: `Workflow profile valid` (exit code `0`).

2. **Causal-Graph Overlays, Curation Guide, Schema Guide, & Overlay README Regression Tests (`#222`, `#216`, `#214`, `#208`, `#206`, `#199`, `#197`, `#187`, `#78`)**:
   ```bash
   .venv/bin/pytest -q -o cache_dir=/tmp/pytest_cache tests/test_causal_graph_overlays.py tests/test_schema.py::test_schema_guide_documents_causal_node_protein_slots
   .venv/bin/ruff check --no-cache tests/test_causal_graph_overlays.py
   ```
   - **Result**: `16 passed in 10.81s` (`15 passed` in `tests/test_causal_graph_overlays.py` including new `test_overlay_readme_documents_current_seed_line_ranges_and_reciprocal_ec_numbers_contract`, plus `1 passed` in `tests/test_schema.py::test_schema_guide_documents_causal_node_protein_slots`); `All checks passed!` (exit code `0`).

3. **Full-Corpus Review Inventory & Post-Curation Target SHA-256 Reconciliation (`#158`)**:
   ```bash
   .venv/bin/python scripts/corpus_review_inventory.py --check
   .venv/bin/pytest -q -o cache_dir=/tmp/pytest_cache tests/test_corpus_review_inventory.py -k "not verify_target_sha256"
   ```
   - **Result**: `corpus_records: 626048`, `legacy_records: 23883`, `structured_records: 602165`, `overlap_records: 0`, `unreviewed_records: 0`, `structured_shards: 14`, `structured_batches: 611`; `9 passed in 23.68s` (exit code `0`).

4. **Provenance & History Record LinkML Validation (`#216`, `#208`, `#199`, `#83`)**:
   ```bash
   .venv/bin/python scripts/check_provenance.py
   .venv/bin/python scripts/validate_history.py history
   ```
   - **Result**: `provenance current: 16 committed inventories from kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd; ATB and StrainInfo snapshots and crosswalks verified`; `history links: 41 record(s), 0 invalid`, `No issues found`, `41 history record(s) valid against src/taxonmech/schema/history.yaml` (exit code `0`).

5. **Post-Remediation Structured Review Bundle Save & Check**:
   ```bash
   .venv/bin/python scripts/record_review.py save --content /tmp/cycle8_stage5_review_input.yaml
   .venv/bin/python scripts/record_review.py check --base main
   .venv/bin/pytest -q -o cache_dir=/tmp/pytest_cache tests/test_record_review_contract.py
   ```
   - **Result**: Saved and validated `reviews/structured/20261107T163000Z-cycle8-stage5-remediation-review/{review.yaml,review.md}` and verified all 452 structured review bundles in `reviews/structured/` while preserving `reviews/structured/20261107T134500Z-cycle8-stage4-corpus-record-review/review.yaml` byte-for-byte (`sha256: c942d28fe1cb5d1ff1e9c20e758a306e0e637354beb9e573ade52b8e36dc4b8d`).
