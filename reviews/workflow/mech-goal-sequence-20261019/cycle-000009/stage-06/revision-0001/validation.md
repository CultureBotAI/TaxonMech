# Cycle 9 Stage 6 (`infrastructure`) — Validation & Adversarial Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle `9`, Stage `6` (`infrastructure`)
- **Repository**: `CultureBotAI/TaxonMech`
- **GitHub Issue Addressed**: [#236](https://github.com/CultureBotAI/TaxonMech/issues/236) (under open umbrella issue [#78](https://github.com/CultureBotAI/TaxonMech/issues/78); [#8](https://github.com/CultureBotAI/TaxonMech/issues/8) carried forward)
- **Frozen `infra_scope` SHA-256**: `0df9141042e64ab44338bb6e8beec7933b770847a8f3deb5fc0cb77de1cd77fa` (`frozen_at: 2026-11-08T17:17:06Z`)

---

## 1. Implemented Changes (`#236`)

1. **`src/taxonmech/seed.py`**:
   - Added `UNIPROT_RELEASE_PATTERN = re.compile(r"^20[0-9]{2}_(?:0[1-9]|1[0-2])$")` (line 84) and enforced `release_version` syntax, catalog-wide `organism_taxon_id`→`(organism_label, proteome_id)` consistency (`seen_org_meta`), 1:1 `proteome_id`→`organism_taxon_id` mapping (`seen_proteome_org`), and `organism_label` correspondence with `ncbitaxon_taxa.tsv` in `load_uniprot_proteins()` (lines 339–447).
   - Enforced per-graph `CausalNode.label` uniqueness (`seen_node_labels`), rejection of edges targeting a `TAXON` node as `object`, and `RO:0002292` (`expresses`) object `GENE_OR_PROTEIN` typing (`node_types_by_id`) in `validate_causal_graph_structure()` (lines 479–670).
2. **`scripts/check_provenance.py`**:
   - Extended `causal_graph_provenance_problems()` (lines 154–265) to require every `CausalNode` in `curation/causal_graphs/*.yaml` to declare a non-empty `grounding` CURIE, every `TAXON` node's `label` to match `taxa[n_grounding]["label"]` in `data/raw/ncbitaxon_taxa.tsv`, and every `RO:0002292` (`expresses`) edge to originate from a host `TAXON` node (`subject in host_taxon_nids`).
3. **`curation/causal_graphs/README.md`, `docs/SCHEMA.md`, `docs/CURATION.md`, and `INFRA_TASKS.md`**:
   - Documented the new `#236` validation and provenance invariants, updated `src/taxonmech/seed.py` (`lines 339–447`, `lines 743–748, 843–860`) and `scripts/check_provenance.py` (`lines 218–230`) line ranges, and updated `INFRA_TASKS.md` to record Cycle 9 Stage 2 (`PR #231`), Stage 3 (`PR #232`), Stage 5 (`#234`, `PR #235`), and Stage 6 (`#236`) progress while carrying `taxonmech-infra-0001..0004` forward as `deferred` to Cycle 10 under `#78` and `#8`.
4. **`tests/test_causal_graph_overlays.py`**:
   - Updated `test_overlay_readme_documents_current_seed_line_ranges_and_reciprocal_ec_numbers_contract` for the `lines 743–748, 843–860` locator and added `test_cycle9_stage6_uniprot_release_org_proteome_consistency_and_causal_graph_node_label_edge_typing_gates` (18/18 tests passing in `tests/test_causal_graph_overlays.py`).

---

## 2. Verification & Quality Gate Results

| Gate / Command | Outcome | Details |
|---|---|---|
| `.venv/bin/pytest -q -p no:cacheprovider tests/test_causal_graph_overlays.py tests/test_schema.py` | **PASSED (`0`)** | `24 passed` (`18 passed` in `tests/test_causal_graph_overlays.py` including `test_cycle9_stage6_uniprot_release_org_proteome_consistency_and_causal_graph_node_label_edge_typing_gates`, and `6 passed` in `tests/test_schema.py`) |
| `.venv/bin/python scripts/check_provenance.py` | **PASSED (`0`)** | `provenance current: 16 committed inventories from kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd; ATB and StrainInfo snapshots and crosswalks verified` |
| `.venv/bin/ruff check --no-cache src/ tests/ scripts/` | **PASSED (`0`)** | `All checks passed!` |
| `bash scripts/check_vendored_sync.sh` | **PASSED (`0`)** | `OK: 22 governed artifacts match the pinned claw revision` |
| `.venv/bin/python scripts/validate_history.py` | **PASSED (`0`)** | `history links: 44 record(s), 0 invalid; 44 history record(s) valid against src/taxonmech/schema/history.yaml` |
| `.venv/bin/python scripts/check_docs.py --check` | **PASSED (`0`)** | `README.md corpus block is current` |
| `.venv/bin/python scripts/record_review.py check --base main` | **PASSED (`0`)** | `record-review check passed (no record changes against main)` |
| `kg_microbe_workflows validate-evidence` | **PASSED (`0`)** | Stage 6 `evidence.yaml` validated against `reviews/workflow/mech-goal-sequence-20261019/cycle-000009/stage-05/revision-0001/evidence.yaml` with required outputs `infra_snapshot`, `implementation_plan`, and `validation` |

---

## 3. Independent Adversarial Review Summary

- **Review Scope**: Full diff against `main` (`f99b34604cac3c67e875b1d869592f072e2a95bc`) across `src/taxonmech/seed.py`, `scripts/check_provenance.py`, `tests/test_causal_graph_overlays.py`, `curation/causal_graphs/README.md`, `docs/SCHEMA.md`, `docs/CURATION.md`, `INFRA_TASKS.md`, `reviews/workflow/latest.yaml`, and `reviews/workflow/mech-goal-sequence-20261019/cycle-000009/stage-06/revision-0001/{infra_snapshot.md,implementation_plan.md,validation.md,evidence.yaml}`.
- **Findings**: `0` blocking or non-blocking findings (`remaining_findings: 0`, `status: complete`).
