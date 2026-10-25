# Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019`, Cycle 3, Stage 6, Revision 1)

- **Repository**: `CultureBotAI/TaxonMech` (`taxonmech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1` (`revision-0001`)
- **Source Revision**: `a050e29c140f7ca7e74432e364b10d732e2922f1`
- **Scope Frozen At**: `2026-10-25T05:14:57Z`

## 1. Summary of Implemented Changes and Validation Outcomes

| Task ID | Status | Linked Issue | Implemented Artifacts | Validation Result |
|---|---|---|---|---|
| `taxonmech-infra-0001` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `src/taxonmech/seed.py` (`validate_causal_graph_structure`), `scripts/check_provenance.py`, `curation/causal_graphs/README.md`, `tests/test_causal_graph_overlays.py` | **PASS (Causal-Graph Structural Referential Integrity & Provenance Gate Integrated; Deferred Under Open Umbrella Issue `#78`)** — `load_causal_graphs()` and `scripts/check_provenance.py` enforce `node_id`/`edge_id` uniqueness, edge endpoint referential integrity against `graph.nodes`, non-self-loop edges, and non-empty `evidence[].reference` across all 15 maintained production overlays (110 edges, 38 `GENE_OR_PROTEIN` nodes); task remains `deferred` under open umbrella issue `#78` pending bulk trait extraction (`taxonmech-infra-0002`). |
| `taxonmech-infra-0002` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `src/taxonmech/extract.py` (`TRAIT_EDGE_FIELDS`, `extract_taxon_trait_edges`), `tests/test_causal_graph_overlays.py` | **PASS (Partial / Deferred)** — `test_extract_taxon_trait_edges_preserves_granular_assertions` verifies granular per-taxon predicate/CURIE/publication extraction; full `data/raw/taxon_trait_edges.tsv` extraction deferred to Cycle 4 pending local `kg-microbe` checkout re-extraction. |
| `taxonmech-infra-0003` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `conf/sources.yaml` (`uniprot_proteins`), `src/taxonmech/seed.py` (`BACDIVE_STRAIN_ID_PATTERN`, `_taxa_lineage_compatible`, `validate_causal_graph_proteins`, `load_causal_graphs`, `load_inventory`), `curation/causal_graphs/README.md`, `tests/test_causal_graph_overlays.py` | **PASS (Source Provenance Registration & `GENE_OR_PROTEIN` `strain_id` Lineage Validator Landed; Bulk `data/raw/` Snapshot Deferred Under `#78`)** — `conf/sources.yaml` registers `uniprot_proteins` (`curation/uniprot_proteins.tsv`, UniProt release `2026_02`, 17 accessions across 38 `GENE_OR_PROTEIN` nodes), and `validate_causal_graph_proteins()` verifies `strain_id` format (`^kgmicrobe\.strain:bacdive_[1-9][0-9]*$`), membership in `bacdive_strains.tsv`, and vertical NCBI Taxonomy lineage compatibility with both host `TaxonRecord.identifier` and `organism_taxon_id` (`test_uniprot_proteins_catalog_and_lineage_validator`), while negative controls reject malformed, absent, or cross-species `strain_id` bindings. |
| `taxonmech-infra-0004` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/8 | `docs/HARMONIZATION.md`, `INFRA_TASKS.md` | **PASS (Partial / Deferred)** — `kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` SHA-256 digests and direct-taxid vs BacDive-subtree contract documented in `docs/HARMONIZATION.md`; corpus-wide `source_attestations[].notes` re-seeding deferred under `#8`. |

## 2. Executed Validation Commands

1. **Causal-graph overlay, structural referential integrity, UniProtKB catalog + `strain_id` lineage validator, extractor, and schema unit tests**:
   ```
   .venv/bin/pytest -q -o cache_dir=/tmp/pytest_cache tests/test_causal_graph_overlays.py tests/test_schema.py tests/test_corpus_review_inventory.py
   ```
   - `tests/test_causal_graph_overlays.py`: 6 passed (`test_five_exemplar_causal_graph_overlays_roundtrip_and_render`, `test_load_causal_graphs_rejects_invalid_or_duplicate_overlays`, `test_extract_taxon_trait_edges_preserves_granular_assertions`, `test_committed_curation_causal_graphs_overlays_load_and_validate`, `test_uniprot_proteins_catalog_and_lineage_validator`, `test_validate_causal_graph_structure_and_sources_catalog`).
   - `tests/test_schema.py`: all schema structure, enum, prefix, and `CausalNode` protein scope slot tests passed.
   - `tests/test_corpus_review_inventory.py`: 4 passed.

2. **Ruff linter**:
   ```
   .venv/bin/ruff check --no-cache src/taxonmech/seed.py scripts/check_provenance.py tests/test_causal_graph_overlays.py
   ```
   - 0 errors.

3. **Repository provenance, vendored schema sync, history, and docs checks**:
   - `.venv/bin/python scripts/check_provenance.py`: PASS (`data/raw/MANIFEST.yaml` matches all committed `data/raw/*.tsv` inventories; `curation/uniprot_proteins.tsv` and `curation/causal_graphs/*.yaml` verified).
   - `bash scripts/check_vendored_sync.sh`: PASS (vendored `mech_shared.yaml` and `history.yaml` byte-identical to pinned ref).
   - `.venv/bin/python scripts/validate_history.py`: PASS (29 history records valid).
   - `.venv/bin/python scripts/record_review.py check`: PASS (50 structured review bundles valid).

4. **Workflow evidence and infrastructure ledger validation**:
   ```
   /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --repo-root /Users/marcin/Documents/VIMSS/ontology/Mechs/TaxonMech --evidence reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/evidence.yaml --effective-workflow /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/taxonmech/effective-workflow.json
   ```
   - Verified `valid: true`, `status: ok`, exact match with frozen `infra_snapshot.md` (`sha256: 0ba8eeef1675ee22621b04fa97775dd2d0d34f65868db2d871417bbde7dade3e`) and `INFRA_TASKS.md`.
