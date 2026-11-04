# Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019`, Cycle 5, Stage 6, Revision 1)

- **Repository**: `CultureBotAI/TaxonMech` (`taxonmech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `5`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1` (`revision-0001`)
- **Source Revision**: `e0cc7c86ac2107242ab499db610737f5fcad1c9b`
- **Scope Frozen At**: `2026-11-04T11:34:48Z`

## 1. Summary of Implemented Changes and Validation Outcomes

| Task ID | Status | Linked Issue | Implemented Artifacts | Validation Result |
|---|---|---|---|---|
| `taxonmech-infra-0001` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 (`#199`) | `src/taxonmech/seed.py` (`NCBITAXON_ID_PATTERN`, `validate_causal_graph_structure`, `validate_causal_graph_proteins`), `scripts/check_provenance.py` (`causal_graph_provenance_problems`), `curation/causal_graphs/README.md`, `tests/test_causal_graph_overlays.py` | **PASS (`CausalGraph` Node Connectivity, `graph_id`/`node_id`/`NCBITaxon` Regex Syntax, Species-or-Below Scope, and Full `check_provenance.py` Cross-Table Validation Integrated Under `#199`; Deferred Under Open Umbrella Issue `#78`)** — `validate_causal_graph_structure()`, `validate_causal_graph_proteins()`, and `causal_graph_provenance_problems()` enforce full node connectivity (no disconnected nodes), `EDGE_ID_PATTERN` on `graph_id` and `node_id`, `NCBITAXON_ID_PATTERN` and `_taxon_is_species_or_below` on host `identifier`, and filename-stem + `curation/seed_scope.tsv` membership across all 15 maintained production overlays (204 edges, 64 `GENE_OR_PROTEIN` nodes); task remains `deferred` to Cycle 6 under open umbrella issue `#78` pending bulk trait extraction (`taxonmech-infra-0002`). |
| `taxonmech-infra-0002` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `src/taxonmech/extract.py` (`TRAIT_EDGE_FIELDS`, `extract_taxon_trait_edges`), `tests/test_causal_graph_overlays.py` | **PASS (Partial / Deferred)** — `test_extract_taxon_trait_edges_preserves_granular_assertions` verifies granular per-taxon predicate/CURIE/publication extraction; full `data/raw/taxon_trait_edges.tsv` extraction deferred to Cycle 6 pending local `kg-microbe` checkout re-extraction. |
| `taxonmech-infra-0003` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 (`#199`) | `src/taxonmech/seed.py` (`UNIPROT_ID_PATTERN`, `NCBITAXON_ID_PATTERN`, `PROTEOME_ID_PATTERN`, `load_uniprot_proteins`, `validate_causal_graph_proteins`), `scripts/check_provenance.py` (`causal_graph_provenance_problems`), `curation/causal_graphs/README.md`, `tests/test_causal_graph_overlays.py` | **PASS (`UNIPROT_ID_PATTERN`, `NCBITAXON_ID_PATTERN`, `PROTEOME_ID_PATTERN`, Species-or-Below `organism_taxon_id`, and Cross-Table Provenance Validation Landed Under `#199`; Bulk `data/raw/` Snapshot Deferred Under `#78`)** — `load_uniprot_proteins()`, `validate_causal_graph_proteins()`, and `causal_graph_provenance_problems()` enforce strict regex patterns and `_taxon_is_species_or_below` across all 29 pinned UniProtKB accessions in `curation/uniprot_proteins.tsv` and 64 `GENE_OR_PROTEIN` nodes across 15 maintained overlays (`test_causal_graph_node_connectivity_and_id_patterns_enforced` and `test_causal_graph_provenance_problems_gate`). |
| `taxonmech-infra-0004` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/8 | `docs/HARMONIZATION.md`, `scripts/audit_review_remediation_groups.py`, `INFRA_TASKS.md` | **PASS (Partial / Deferred)** — `kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` SHA-256 digests and direct-taxid vs BacDive-subtree contract documented in `docs/HARMONIZATION.md` and audited by `scripts/audit_review_remediation_groups.py` (PR `#198`, `#196`, `#197`); corpus-wide `source_attestations[].notes` re-seeding deferred to Cycle 6 under `#8`. |

## 2. Executed Validation Commands

1. **Causal-graph overlay, node connectivity, regex invariant, species-or-below scope, provenance cross-table gate, and remediation group audit unit tests**:
   ```
   .venv/bin/pytest -q -o cache_dir=/tmp/pytest-cache tests/test_causal_graph_overlays.py tests/test_review_remediation_groups.py tests/test_schema.py tests/test_corpus_review_inventory.py
   ```
   - `tests/test_causal_graph_overlays.py`: 10 passed (including `test_causal_graph_node_connectivity_and_id_patterns_enforced` and `test_causal_graph_provenance_problems_gate`).
   - `tests/test_review_remediation_groups.py`: 5 passed.
   - `tests/test_schema.py`: 9 passed.
   - `tests/test_corpus_review_inventory.py`: 4 passed.

2. **Ruff linter**:
   ```
   .venv/bin/ruff check --no-cache src/taxonmech/seed.py scripts/check_provenance.py tests/test_causal_graph_overlays.py
   ```
   - 0 errors (`All checks passed!`).

3. **Repository provenance, vendored schema sync, history, and docs checks**:
   - `.venv/bin/python scripts/check_provenance.py`: PASS (`data/raw/MANIFEST.yaml` matches all committed `data/raw/*.tsv` inventories; `curation/uniprot_proteins.tsv`, `curation/causal_graphs/*.yaml`, `data/raw/ncbitaxon_taxa.tsv`, `data/raw/bacdive_strains.tsv`, and `curation/seed_scope.tsv` verified).
   - `bash scripts/check_vendored_sync.sh`: PASS (`OK: 22 governed artifacts match the pinned claw revision`).
   - `.venv/bin/python scripts/validate_history.py`: PASS (`31 history record(s) valid against src/taxonmech/schema/history.yaml`).
   - `.venv/bin/python scripts/record_review.py check`: PASS (all structured review bundles valid).

4. **Workflow evidence and infrastructure ledger validation**:
   ```
   /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --file reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/evidence.yaml --repo-root /Users/marcin/Documents/VIMSS/ontology/Mechs/TaxonMech --run-id mech-goal-sequence-20261019 --cycle 5 --stage 6 --source-revision e0cc7c86ac2107242ab499db610737f5fcad1c9b --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-05/revision-0001/evidence.yaml --required-output infra_snapshot --required-output implementation_plan --required-output validation
   ```
   - Verified `valid: true`, exact match with frozen `infra_snapshot.md` (`sha256: b64bec8e5962706b6df2c6537556d0a228bd638c85343e026bc55fc05b2cec1e`) and `INFRA_TASKS.md`.
