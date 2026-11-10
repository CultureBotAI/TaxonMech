# Cycle 10 Stage 6 (`infrastructure`) — Validation & Adversarial Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle `10`, Stage `6` (`infrastructure`)
- **Repository**: `CultureBotAI/TaxonMech`
- **GitHub Issue Addressed**: [#249](https://github.com/CultureBotAI/TaxonMech/issues/249) (under open umbrella issue [#78](https://github.com/CultureBotAI/TaxonMech/issues/78); [#8](https://github.com/CultureBotAI/TaxonMech/issues/8) carried forward)
- **Frozen `infra_scope` SHA-256**: `e0ad8a4e0d70365132924802c3aef51d0101476a45e2c3aafab582f53af3f8ef` (`frozen_at: 2026-11-10T04:43:08Z`)

---

## 1. Implemented Changes (`#249`)

1. **`src/taxonmech/seed.py`**:
   - Extended `load_uniprot_proteins()` (lines 339–484) to enforce per-organism `(organism_taxon_id, gene_symbol)` uniqueness (`seen_org_genes`), per-organism `(organism_taxon_id, sequence_crc64)` uniqueness (`seen_org_crc64`), per-organism `entry_name` `_<org_code>` suffix consistency (`seen_org_mnemonic_suffix`), and `entry_status`↔`entry_name` prefix alignment (`TREMBL` prefix equals bare accession; `SWISS_PROT` prefix differs from bare accession).
   - Extended `validate_causal_graph_structure()` (lines 516–730) to enforce `CausalNode.grounding` prefix-to-`node_type` domain isolation (`NCBITaxon:` exclusively on `TAXON`, `UniProtKB:` matching `UNIPROT_ID_PATTERN` exclusively on `GENE_OR_PROTEIN`) and reject multiple `RO:0002292` (`expresses`) edges targeting the same `GENE_OR_PROTEIN` `object` (`seen_expressed_objects`).
2. **`scripts/check_provenance.py`**:
   - Extended `causal_graph_provenance_problems()` (lines 218–241) to require every `GENE_OR_PROTEIN` node on a host `TaxonRecord.identifier` whose subtree contains a lineage-compatible BacDive strain to declare a non-empty `strain_id` (`#246`, `#197`).
3. **`curation/causal_graphs/README.md`, `docs/SCHEMA.md`, `docs/CURATION.md`, and `INFRA_TASKS.md`**:
   - Documented the new `#249` validation and provenance invariants, updated `src/taxonmech/seed.py` (`lines 339–484`, `lines 803–808, 903–920`) and `scripts/check_provenance.py` (`lines 218–241`, `lines 244–256`) line ranges, and updated `INFRA_TASKS.md` to record Cycle 10 Stage 2 (`PR #240`), Stage 3 (`PR #243`), Stage 5 (`#246`, `PR #247`), and Stage 6 (`#249`) progress while carrying `taxonmech-infra-0001..0004` forward as `deferred` to Cycle 11 under `#78` and `#8`.
4. **`tests/test_causal_graph_overlays.py`**:
   - Updated `test_overlay_readme_documents_current_seed_line_ranges_and_reciprocal_ec_numbers_contract` for the `lines 803–808, 903–920` locator and added `test_cycle10_stage6_uniprot_gene_crc64_mnemonic_and_causal_graph_prefix_strain_id_gates` (19/19 tests passing in `tests/test_causal_graph_overlays.py`).

---

## 2. Verification & Quality Gate Results

| Gate / Command | Outcome | Details |
|---|---|---|
| `.venv/bin/pytest -q -p no:cacheprovider tests/test_causal_graph_overlays.py tests/test_schema.py` | **PASSED (`0`)** | `25 passed` (`19 passed` in `tests/test_causal_graph_overlays.py` including `test_cycle10_stage6_uniprot_gene_crc64_mnemonic_and_causal_graph_prefix_strain_id_gates`, and `6 passed` in `tests/test_schema.py`) |
| `.venv/bin/python scripts/check_provenance.py` | **PASSED (`0`)** | `provenance current: 16 committed inventories from kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd; ATB and StrainInfo snapshots and crosswalks verified` |
| `.venv/bin/ruff check --no-cache src/ tests/ scripts/` | **PASSED (`0`)** | `All checks passed!` |
| `bash scripts/check_vendored_sync.sh` | **PASSED (`0`)** | `OK: 22 governed artifacts match the pinned claw revision` |
| `.venv/bin/python scripts/validate_history.py` | **PASSED (`0`)** | `history links: 44 record(s), 0 invalid; 44 history record(s) valid against src/taxonmech/schema/history.yaml` |
| `.venv/bin/python scripts/check_docs.py --check` | **PASSED (`0`)** | `README.md corpus block is current` |
| `.venv/bin/python scripts/record_review.py check --base main` | **PASSED (`0`)** | `record-review check passed (no record changes against main)` |
| `kg_microbe_workflows validate-evidence` | **PASSED (`0`)** | Stage 6 `evidence.yaml` validated against `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-05/revision-0001/evidence.yaml` with required outputs `infra_snapshot`, `implementation_plan`, and `validation` |

---

## 3. Independent Adversarial Review Summary

- **Review Scope**: Full diff against `main` (`6a86624b7ba126a5982b758431b9804cf0ffb395`) across `src/taxonmech/seed.py`, `scripts/check_provenance.py`, `tests/test_causal_graph_overlays.py`, `curation/causal_graphs/README.md`, `docs/SCHEMA.md`, `docs/CURATION.md`, `INFRA_TASKS.md`, `reviews/workflow/latest.yaml`, and `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-06/revision-0001/{infra_snapshot.md,implementation_plan.md,validation.md,evidence.yaml}`.
- **Findings**: `0` blocking or non-blocking findings (`remaining_findings: 0`, `status: complete`).
