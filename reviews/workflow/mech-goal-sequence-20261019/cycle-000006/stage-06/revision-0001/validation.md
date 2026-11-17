# Cycle 6 Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `6`
- **Stage**: `6` (`infrastructure`)
- **Source Revision**: `0415ba3062aee129825160f6f6dae5d0748eddb3`
- **Addressed Issue**: `#208` (under open umbrella `#78` for `taxonmech-infra-0001` and `taxonmech-infra-0003`)

## 1. Implemented Changes Validated

1. **`src/taxonmech/seed.py` (`validate_causal_graph_structure`, `validate_causal_graph_proteins`, `load_causal_graphs`)**:
   - `validate_causal_graph_structure()` enforces per-taxon `graph_id` uniqueness (`seen_graph_ids`) and requires every `TAXON` node (`node_type == "TAXON"`) to carry a non-empty `grounding` matching `NCBITAXON_ID_PATTERN` (`^NCBITaxon:[1-9][0-9]*$`).
   - `load_causal_graphs()` requires every `CausalGraph` entry loaded from `curation/causal_graphs/*.yaml` to have a non-empty string `title`, a non-empty `nodes` list, and a non-empty `edges` list before invoking `validate_causal_graph_structure()`.
   - `validate_causal_graph_proteins()` enforces the host-subtree `strain_id` binding rule (`s_tid == tid or tid in _taxon_lineage(taxa, s_tid)` in addition to `_taxa_lineage_compatible(taxa, s_tid, org_tid)`), ensuring any `strain_id` declared on a `GENE_OR_PROTEIN` node appears on the host `TaxonRecord.strains[]` list and rejecting ancestor-species `strain_id` bindings on infraspecific strain overlays whose `strains` list is `[]`.
2. **`scripts/check_provenance.py` (`causal_graph_provenance_problems`)**:
   - Verifies that every `uniprot_id` in `curation/uniprot_proteins.tsv` is referenced by at least one `GENE_OR_PROTEIN` node across `curation/causal_graphs/*.yaml` (34/34 accessions referenced across 75 `GENE_OR_PROTEIN` nodes in the 15 committed overlays) and that every committed overlay in `curation/causal_graphs/*.yaml` carries a non-empty `curation_history` list.
3. **`curation/causal_graphs/README.md`, `docs/SCHEMA.md`, `INFRA_TASKS.md`, and `tests/test_causal_graph_overlays.py`**:
   - Added `test_cycle6_stage6_causal_graph_and_uniprot_provenance_invariants` to `tests/test_causal_graph_overlays.py` (12/12 tests passing in `tests/test_causal_graph_overlays.py`, 1,134/1,134 across the full test suite).
   - Synchronized `curation/causal_graphs/README.md`, `docs/SCHEMA.md`, and `INFRA_TASKS.md` with `#208` and carried forward unfinished bulk/upstream work under `#78` and `#8` to Cycle 7.

## 2. Verification Commands and Outcomes

| Gate | Command | Outcome |
|---|---|---|
| Workflow profile validation | `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate --profile workflow/mech-workflow.yaml --parent workflow/parent/mech-cycle.yaml --schema workflow/parent/workflow.yaml` | `PASSED` (`Workflow profile valid`) |
| Causal-graph & UniProt overlay tests | `.venv/bin/pytest tests/test_causal_graph_overlays.py` | `PASSED` (`12 passed`) |
| Full pytest suite | `.venv/bin/pytest -o cache_dir=/tmp/pytest_cache` | `PASSED` (`1134 passed`) |
| Ruff lint | `.venv/bin/ruff check --no-cache src/ tests/ scripts/` | `PASSED` (`All checks passed!`) |
| Provenance & cross-table check | `.venv/bin/python scripts/check_provenance.py` | `PASSED` (`provenance current: 16 committed inventories from kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd; ATB and StrainInfo snapshots and crosswalks verified`) |
| Vendored claw sync check | `bash scripts/check_vendored_sync.sh` | `PASSED` (`OK: 22 governed artifacts match the pinned claw revision`) |
| Curation history validation | `.venv/bin/python scripts/validate_history.py` | `PASSED` (`35 history record(s) valid against src/taxonmech/schema/history.yaml`) |
| README generated stats check | `.venv/bin/python scripts/check_docs.py --check` | `PASSED` (`README.md stats block is current.`) |
| Record review inventory check | `.venv/bin/python scripts/record_review.py check` | `PASSED` (`OK: 1 structured review(s), 602165 structured-inventory record(s), 23883 legacy-inventory record(s)`) |
| Stage 6 workflow evidence manifest validation | `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --file reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-06/revision-0001/evidence.yaml --repo-root /Users/marcin/Documents/VIMSS/ontology/Mechs/TaxonMech --run-id mech-goal-sequence-20261019 --cycle 6 --stage 6 --source-revision 0415ba3062aee129825160f6f6dae5d0748eddb3 --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-05/revision-0001/evidence.yaml --required-output infra_snapshot --required-output implementation_plan --required-output validation` | `PASSED` (`Evidence manifest valid`) |
