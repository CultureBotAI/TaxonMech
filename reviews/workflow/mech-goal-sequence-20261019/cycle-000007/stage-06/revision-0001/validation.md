# Cycle 7 Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `7`
- **Stage**: `6` (`infrastructure`)
- **Source Revision**: `c6c16699bb346b4ae2a31b786295ad1fae7c8ca5`
- **Addressed Issue**: `#216` (under open umbrella `#78` for `taxonmech-infra-0001` and `taxonmech-infra-0003`)

## 1. Implemented Changes Validated

1. **`src/taxonmech/seed.py` (`validate_causal_graph_structure`, `validate_causal_graph_events`, `validate_causal_graph_proteins`, `load_causal_graphs`)**:
   - Defined `CAUSAL_GRAPH_KEYS`, `CAUSAL_NODE_KEYS`, `CAUSAL_EDGE_KEYS`, `EVIDENCE_ITEM_KEYS`, `CURATION_EVENT_KEYS`, and `ISO_UTC_TIMESTAMP_PATTERN` (`^20[0-9]{2}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$`), verified against `SchemaView` induced slots in `src/taxonmech/schema/taxonmech.yaml`.
   - `validate_causal_graph_structure()` rejects unexpected keys on `CausalGraph`, `CausalNode`, `CausalEdge`, and `EvidenceItem` mappings so unknown keys cannot be silently dropped during `build_document()`.
   - `validate_causal_graph_events()` (invoked by `load_causal_graphs()`) enforces closed-key `CurationEvent` dictionaries (`CURATION_EVENT_KEYS`), ISO-8601 UTC `timestamp` syntax (`ISO_UTC_TIMESTAMP_PATTERN`), non-decreasing chronological order across `curation_history`, non-empty `curator`/`action`/`changes`, and boolean `llm_assisted`.
   - `validate_causal_graph_proteins()` enforces per-graph `GENE_OR_PROTEIN` `grounding` (`UniProtKB:<accession>`) uniqueness (`seen_protein_groundings`).
2. **`scripts/check_provenance.py` (`causal_graph_provenance_problems`)**:
   - Enforces that every committed `CausalGraph` in `curation/causal_graphs/*.yaml` contains at least one `TAXON` node grounded to the host `TaxonRecord.identifier` (`tid`), every `GENE_OR_PROTEIN` node includes all full 4-part (non-wildcard) `EC:` numbers from `curation/uniprot_proteins.tsv` in `xrefs`, and every `CausalEdge.evidence[]` item carries non-empty `notes` or `snippet` (all 15 committed overlays, 290 edges, 86 `GENE_OR_PROTEIN` nodes, and 39 `curation/uniprot_proteins.tsv` rows pass with zero provenance errors).
3. **`curation/causal_graphs/README.md`, `docs/SCHEMA.md`, `docs/CURATION.md`, `INFRA_TASKS.md`, and `tests/test_causal_graph_overlays.py`**:
   - Updated the `curation/causal_graphs/README.md` YAML example to include a host `TAXON` node (`NCBITaxon:562`) and canonical `CurationEvent` slots (`timestamp`, `curator`, `action`, `changes`, `llm_assisted`), and updated `STAGE2_STAGE3_EXEMPLAR_OVERLAYS` in `tests/test_causal_graph_overlays.py` to use `curator` and `changes`.
   - Added `test_cycle7_stage6_closed_keys_curation_events_and_provenance_invariants` to `tests/test_causal_graph_overlays.py` (14/14 tests passing in `tests/test_causal_graph_overlays.py`, 1,135/1,135 across the full test suite).
   - Synchronized `curation/causal_graphs/README.md`, `docs/SCHEMA.md`, `docs/CURATION.md`, and `INFRA_TASKS.md` with `#216` and carried forward unfinished bulk/upstream work under `#78` and `#8` to Cycle 8.

## 2. Verification Commands and Outcomes

| Gate | Command | Outcome |
|---|---|---|
| Workflow profile validation | `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate --profile workflow/mech-workflow.yaml --parent workflow/parent/mech-cycle.yaml --schema workflow/parent/workflow.yaml` | `PASSED` (`Workflow profile valid`) |
| Causal-graph & UniProt overlay tests | `.venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_causal_graph_overlays.py` | `PASSED` (`14 passed`) |
| Full pytest suite | `.venv/bin/pytest -o cache_dir=/tmp/pytest_cache` | `PASSED` (`1135 passed`) |
| Ruff lint | `.venv/bin/ruff check --no-cache src/ tests/ scripts/` | `PASSED` (`All checks passed!`) |
| Provenance & cross-table check | `.venv/bin/python scripts/check_provenance.py` | `PASSED` (`provenance current: 16 committed inventories from kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd; ATB and StrainInfo snapshots and crosswalks verified`) |
| Vendored claw sync check | `bash scripts/check_vendored_sync.sh` | `PASSED` (`OK: 22 governed artifacts match the pinned claw revision`) |
| Curation history validation | `.venv/bin/python scripts/validate_history.py` | `PASSED` (`38 history record(s) valid against src/taxonmech/schema/history.yaml`) |
| README generated stats check | `.venv/bin/python scripts/check_docs.py --check` | `PASSED` (`README.md stats block is current.`) |
| Record review inventory check | `.venv/bin/python scripts/record_review.py check` | `PASSED` (`valid_reviews: 448, coverage: declared_scopes_only`) |
| Stage 6 workflow evidence manifest validation | `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --root /Users/marcin/Documents/VIMSS/ontology/Mechs/TaxonMech --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-05/revision-0001/evidence.yaml --required-output infra_snapshot --required-output implementation_plan --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-06/revision-0001/evidence.yaml` | `PASSED` (`Base contract and supplied output requirements valid`) |
