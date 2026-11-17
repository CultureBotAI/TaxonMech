# Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019`, Cycle 2, Stage 6, Revision 1)

- **Repository**: `CultureBotAI/TaxonMech` (`taxonmech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1` (`revision-0001`)
- **Source Revision**: `2e13ca650f72b310bf1496bcd72eb399ae160b27`
- **Scope Frozen At**: `2026-10-23T13:45:40Z`

## 1. Summary of Implemented Changes and Validation Outcomes

| Task ID | Status | Linked Issue | Implemented Artifacts | Validation Result |
|---|---|---|---|---|
| `taxonmech-infra-0001` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `src/taxonmech/seed.py`, `curation/causal_graphs/README.md`, `tests/test_causal_graph_overlays.py` | **PASS (Offline Protein & Lineage Gate Integrated; Deferred Under Open Umbrella Issue `#78`)** — `load_causal_graphs()` and `load_inventory()` automatically validate all 15 maintained production overlays (83 edges, 28 `GENE_OR_PROTEIN` nodes) against `curation/uniprot_proteins.tsv` and NCBI Taxonomy vertical lineage; task remains `deferred` under open umbrella issue `#78` pending bulk trait extraction (`taxonmech-infra-0002`). |
| `taxonmech-infra-0002` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `src/taxonmech/extract.py` (`TRAIT_EDGE_FIELDS`, `extract_taxon_trait_edges`), `tests/test_causal_graph_overlays.py` | **PASS (Partial / Deferred)** — `test_extract_taxon_trait_edges_preserves_granular_assertions` verifies granular per-taxon predicate/CURIE/publication extraction; full `data/raw/taxon_trait_edges.tsv` extraction deferred to Cycle 3 pending local `kg-microbe` checkout re-extraction. |
| `taxonmech-infra-0003` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `curation/uniprot_proteins.tsv`, `src/taxonmech/seed.py` (`UNIPROT_PROTEINS_PATH`, `UNIPROT_PROTEIN_FIELDS`, `load_uniprot_proteins`, `validate_causal_graph_proteins`), `curation/causal_graphs/README.md`, `tests/test_causal_graph_overlays.py` | **PASS (Curated Catalog & Offline Validator Landed; Bulk `data/raw/` Snapshot Deferred Under `#78`)** — All 13 curated `UniProtKB` accessions across 28 `GENE_OR_PROTEIN` nodes in 15 overlays pass offline metadata, CRC64, EC xref, and vertical NCBI Taxonomy lineage validation (`test_uniprot_proteins_catalog_and_lineage_validator`), while negative controls reject unpinned accessions (`UniProtKB:Q9HWH3`), mismatched `sequence_crc64`, and cross-species bindings (`UniProtKB:Q55P57` on `NCBITaxon:1859096`). |
| `taxonmech-infra-0004` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/8 | `docs/HARMONIZATION.md`, `INFRA_TASKS.md` | **PASS (Partial / Deferred)** — `kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` SHA-256 digests and direct-taxid vs BacDive-subtree contract documented in `docs/HARMONIZATION.md`; corpus-wide `source_attestations[].notes` re-seeding deferred under `#8`. |

## 2. Executed Validation Commands

1. **Causal-graph overlay, UniProtKB catalog/lineage validator, extractor, and schema unit tests**:
   ```
   .venv/bin/pytest -q -o cache_dir=/tmp/pytest_cache tests/test_causal_graph_overlays.py tests/test_schema.py tests/test_corpus_review_inventory.py
   ```
   - `tests/test_causal_graph_overlays.py`: 5 passed (`test_five_exemplar_causal_graph_overlays_roundtrip_and_render`, `test_committed_production_causal_graph_overlays_match_seeded_records`, `test_uniprot_proteins_catalog_and_lineage_validator`, `test_load_causal_graphs_rejects_invalid_or_duplicate_overlays`, `test_extract_taxon_trait_edges_preserves_granular_assertions`).
   - `tests/test_schema.py`: all schema structure, enum, prefix, and `CausalNode` protein scope slot tests passed.
   - `tests/test_corpus_review_inventory.py`: 4 passed.

2. **Ruff linter**:
   ```
   .venv/bin/ruff check --no-cache src/taxonmech/seed.py tests/test_causal_graph_overlays.py
   ```
   - 0 errors.

3. **Repository provenance, vendored schema sync, history, and docs checks**:
   - `.venv/bin/python scripts/check_provenance.py`: PASS (`data/raw/MANIFEST.yaml` matches all committed `data/raw/*.tsv` inventories).
   - `bash scripts/check_vendored_sync.sh`: PASS (vendored `mech_shared.yaml` and `history.yaml` byte-identical to pinned ref).
   - `.venv/bin/python scripts/validate_history.py`: PASS (23 history records valid).
   - `.venv/bin/python scripts/record_review.py check`: PASS (47 structured review bundles valid).

4. **Workflow evidence and infrastructure ledger validation**:
   ```
   /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --repo-root /Users/marcin/Documents/VIMSS/ontology/Mechs/TaxonMech --evidence reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/evidence.yaml --effective-workflow /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/taxonmech/effective-workflow.json
   ```
   - Verified `valid: true`, `status: ok`, exact match with frozen `infra_snapshot.md` (`sha256: 276aa7fa5439a3fac069798ca1b029d8a50b2cbcc47a74f7a3423f9847ba4fa0`) and `INFRA_TASKS.md`.
