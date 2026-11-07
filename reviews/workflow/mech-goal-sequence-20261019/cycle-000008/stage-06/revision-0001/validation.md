# Cycle 8 Stage 6 (`infrastructure`) — Validation & Adversarial Review Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle `8`, Stage `6` (`infrastructure`)
- **Repository**: `CultureBotAI/TaxonMech`
- **GitHub Issue Addressed**: [#224](https://github.com/CultureBotAI/TaxonMech/issues/224) (under open umbrella issue [#78](https://github.com/CultureBotAI/TaxonMech/issues/78); [#8](https://github.com/CultureBotAI/TaxonMech/issues/8) carried forward)
- **Frozen `infra_scope` SHA-256**: `52d673554dbe32f05a8deb95fa673b274e86934b82dfba9df124cc395dcb0a76` (`frozen_at: 2026-11-07T19:37:19Z`)

---

## 1. Implemented Changes (`#224`)

1. **`src/taxonmech/seed.py`**:
   - Added `UNIPROT_ENTRY_NAME_PATTERN = re.compile(r"^[A-Z0-9]{1,11}_[A-Z0-9]{2,5}$")` (line 83) and enforced `entry_name` syntax, catalog-wide `entry_name` uniqueness (`seen_entry_names`), and catalog-wide `(organism_taxon_id, locus_tag)` uniqueness (`seen_org_loci`) in `load_uniprot_proteins()` (lines 338–416).
   - Enforced per-graph `CausalNode.grounding` uniqueness across all grounded nodes (`seen_node_groundings`) and per-graph `predicate`↔`predicate_id` pairing consistency (`seen_pred_by_id`, `seen_id_by_pred`) in `validate_causal_graph_structure()` (lines 429–614).
2. **`scripts/check_provenance.py`**:
   - Extended `causal_graph_provenance_problems()` (lines 154–235) to require every `CausalEdge` in `curation/causal_graphs/*.yaml` to declare a non-empty `predicate_id` CURIE and every `GENE_OR_PROTEIN` node to be linked from a host `TAXON` node (`grounding == tid`) via `RO:0002292` (`expresses`) and to have at least one outgoing functional/regulatory/causal edge (`edge.subject == node_id`).
3. **`curation/causal_graphs/README.md`, `docs/SCHEMA.md`, `docs/CURATION.md`, and `INFRA_TASKS.md`**:
   - Documented the new `#224` validation and provenance invariants, updated `src/taxonmech/seed.py` (`lines 338–416`, `lines 697–702, 797–814`) and `scripts/check_provenance.py` (`lines 197–209`) line ranges, and updated `INFRA_TASKS.md` to record Cycle 8 Stage 2 (`PR #219`), Stage 3 (`PR #220`), Stage 5 (`#222`, `PR #223`), and Stage 6 (`#224`) progress while carrying `taxonmech-infra-0001..0004` forward as `deferred` to Cycle 9 under `#78` and `#8`.
4. **`tests/test_causal_graph_overlays.py`**:
   - Updated `test_overlay_readme_documents_current_seed_line_ranges_and_reciprocal_ec_numbers_contract` for the `lines 697–702, 797–814` locator and added `test_cycle8_stage6_uniprot_catalog_node_grounding_and_protein_edge_topology_gates` (16/16 tests passing in `tests/test_causal_graph_overlays.py`).

---

## 2. Verification & Quality Gate Results

| Gate / Command | Outcome | Details |
|---|---|---|
| `.venv/bin/pytest tests/test_causal_graph_overlays.py` | **PASSED (`0`)** | `16 passed` (including `test_cycle8_stage6_uniprot_catalog_node_grounding_and_protein_edge_topology_gates` and `test_overlay_readme_documents_current_seed_line_ranges_and_reciprocal_ec_numbers_contract`) |
| `.venv/bin/python scripts/check_provenance.py` | **PASSED (`0`)** | `provenance current: 16 committed inventories from kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd; ATB and StrainInfo snapshots and crosswalks verified` |
| `.venv/bin/ruff check --no-cache src/ tests/ scripts/` | **PASSED (`0`)** | `All checks passed!` |
| `bash scripts/check_vendored_sync.sh` | **PASSED (`0`)** | `OK: 22 governed artifacts match the pinned claw revision` |
| `.venv/bin/python scripts/validate_history.py` | **PASSED (`0`)** | `history links: 41 record(s), 0 invalid; 41 history record(s) valid against src/taxonmech/schema/history.yaml` |
| `.venv/bin/python scripts/check_docs.py --check` | **PASSED (`0`)** | `README.md corpus block is current` |
| `.venv/bin/python scripts/record_review.py check --base main` | **PASSED (`0`)** | `record-review check passed (no record changes against main)` |
| `kg_microbe_workflows validate-evidence` | **PASSED (`0`)** | Stage 6 `evidence.yaml` validated against `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-05/revision-0001/evidence.yaml` with required outputs `infra_snapshot`, `implementation_plan`, and `validation` |

---

## 3. Independent Adversarial Review Summary

- **Review Scope**: Full diff against `main` (`ab35a0d0a0a2b47d250145db0c15b414fccbfdb8`) across `src/taxonmech/seed.py`, `scripts/check_provenance.py`, `tests/test_causal_graph_overlays.py`, `curation/causal_graphs/README.md`, `docs/SCHEMA.md`, `docs/CURATION.md`, `INFRA_TASKS.md`, `reviews/workflow/latest.yaml`, and `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-06/revision-0001/{infra_snapshot.md,implementation_plan.md,validation.md,evidence.yaml}`.
- **Findings**: `0` blocking or non-blocking findings (`remaining_findings: 0`, `status: complete`).
