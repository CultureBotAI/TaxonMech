# Cycle 11 Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019`)

## 1. Summary of Implemented Upgrades ([#259](https://github.com/CultureBotAI/TaxonMech/issues/259), [#78](https://github.com/CultureBotAI/TaxonMech/issues/78))

1. **UniProtKB Catalog Ordering & Single-Release-Pin Validation (`src/taxonmech/seed.py` lines 341–501)**:
   - `load_uniprot_proteins()` now enforces strict ascending `uniprot_id` row ordering (`prev_uid` check) and a single uniform `release_version` catalog pin (`pinned_release_version` check) across all 59 rows in `curation/uniprot_proteins.tsv`.
2. **Causal-Graph `CHEBI:`/`GO:` Grounding & Optional Text-Slot Validation (`src/taxonmech/seed.py` lines 87–88, 533–789)**:
   - Added `CHEBI_ID_PATTERN` (`^CHEBI:[1-9][0-9]*$`) and `GO_ID_PATTERN` (`^GO:[0-9]{7}$`).
   - `validate_causal_graph_structure()` now enforces `CHEMICAL` ↔ `CHEBI:` domain isolation and `CHEBI_ID_PATTERN` validation, `GO_ID_PATTERN` validation on `BIOLOGICAL_PROCESS`, `MOLECULAR_FUNCTION`, `CELLULAR_COMPONENT`, and `GO:`-grounded `CausalNode` entries, and non-empty string validation on optional `CausalGraph.description`, `CausalNode.description`, and `EvidenceItem.snippet`/`notes` when present.
3. **Host-Taxon `TAXON` Exclusivity & Within-Graph `GENE_OR_PROTEIN` Homogeneity (`scripts/check_provenance.py` lines 99–340)**:
   - `causal_graph_provenance_problems()` now rejects any `TAXON` node in `curation/causal_graphs/<slug>.yaml` whose `grounding` does not equal the overlay's host taxon `tid`, and enforces within-graph `organism_taxon_id` and `strain_id` homogeneity across all `GENE_OR_PROTEIN` nodes in a `CausalGraph`.
4. **Documentation, Ledger Dispositions, & Unit Tests**:
   - Updated `curation/causal_graphs/README.md`, `docs/SCHEMA.md`, `docs/CURATION.md`, and `INFRA_TASKS.md` (carrying `taxonmech-infra-0001..0004` forward as `deferred` to Cycle 12 under open `#78` and `#8`).
   - Added `test_cycle11_stage6_uniprot_sort_release_pin_and_causal_graph_chebi_go_homogeneity_gates` in `tests/test_causal_graph_overlays.py` and updated `test_overlay_readme_documents_current_seed_line_ranges_and_reciprocal_ec_numbers_contract`.

## 2. Quality Gate Results

| Check | Command | Result |
|---|---|---|
| Lint | `.venv/bin/ruff check --no-cache src/taxonmech/seed.py scripts/check_provenance.py tests/test_causal_graph_overlays.py` | Passed (`All checks passed!`) |
| Causal-Graph Overlay Unit & Integration Tests | `.venv/bin/pytest tests/test_causal_graph_overlays.py` | Passed (`20 passed`) |
| Provenance Gate | `.venv/bin/python scripts/check_provenance.py` | Passed (`provenance OK`) |
| Vendored Sync | `.venv/bin/python scripts/check_vendored_sync.py` | Passed (`vendored-sync OK`) |
| History Validation | `.venv/bin/python scripts/validate_history.py` | Passed |
| README Statistics Sync | `.venv/bin/python scripts/check_docs.py --check` | Passed (`README statistics block is current`) |
| Native Record Review Gate | `.venv/bin/python scripts/record_review.py check --base main` | Passed (`0 record YAML files touched on branch`) |
| Workflow Evidence Contract | `kg_microbe_workflows validate-evidence --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-05/revision-0001/evidence.yaml --required-output infra_snapshot --required-output implementation_plan --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-06/revision-0001/evidence.yaml` | Passed (`VALID`) |
