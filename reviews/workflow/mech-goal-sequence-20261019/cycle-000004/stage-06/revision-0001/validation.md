# Stage 6 Infrastructure Validation Report (`mech-goal-sequence-20261019`, Cycle 4, Stage 6, Revision 1)

- **Repository**: `CultureBotAI/TaxonMech` (`taxonmech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `4`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1` (`revision-0001`)
- **Source Revision**: `11bf38c5f683ad2b21039b41771e64f35930c81c`
- **Scope Frozen At**: `2026-10-31T14:45:23Z`

## 1. Summary of Implemented Changes and Validation Outcomes

| Task ID | Status | Linked Issue | Implemented Artifacts | Validation Result |
|---|---|---|---|---|
| `taxonmech-infra-0001` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 (`#189`) | `src/taxonmech/seed.py` (`CAUSAL_NODE_TYPES`, `CURIE_PATTERN`, `EDGE_ID_PATTERN`, `EVIDENCE_REFERENCE_PATTERN`, `PROTEIN_ONLY_NODE_SLOTS`, `validate_causal_graph_structure`, `validate_causal_graph_proteins`), `curation/causal_graphs/README.md`, `tests/test_causal_graph_overlays.py` | **PASS (`CausalNode`/`CausalEdge` Schema Invariants, Protein-Only Slot Isolation, and `TAXON` Node Lineage Validation Integrated Under `#189`; Deferred Under Open Umbrella Issue `#78`)** — `validate_causal_graph_structure()` and `validate_causal_graph_proteins()` enforce `CausalNodeTypeEnum` membership, isolation of all 9 protein-only slots (`PROTEIN_ONLY_NODE_SLOTS`) to `GENE_OR_PROTEIN` nodes, `CURIE_PATTERN` and `EDGE_ID_PATTERN` syntax, `NCBITaxon:` grounding and `ncbitaxon_taxa.tsv` vertical lineage consistency on `TAXON` nodes, duplicate `xrefs`/parallel-edge/evidence-reference rejection, and `EVIDENCE_REFERENCE_PATTERN` (`PMID:`, `PMC:PMC`, `DOI:10.`, `http(s)://`) on edge evidence across all 15 maintained production overlays (161 edges, 51 `GENE_OR_PROTEIN` nodes); task remains `deferred` to Cycle 5 under open umbrella issue `#78` pending bulk trait extraction (`taxonmech-infra-0002`). |
| `taxonmech-infra-0002` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `src/taxonmech/extract.py` (`TRAIT_EDGE_FIELDS`, `extract_taxon_trait_edges`), `tests/test_causal_graph_overlays.py` | **PASS (Partial / Deferred)** — `test_extract_taxon_trait_edges_preserves_granular_assertions` verifies granular per-taxon predicate/CURIE/publication extraction; full `data/raw/taxon_trait_edges.tsv` extraction deferred to Cycle 5 pending local `kg-microbe` checkout re-extraction. |
| `taxonmech-infra-0003` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/78 (`#189`) | `src/taxonmech/seed.py` (`EC_NUMBER_PATTERN`, `load_uniprot_proteins`, `validate_causal_graph_proteins`), `curation/causal_graphs/README.md`, `tests/test_causal_graph_overlays.py` | **PASS (UniProtKB Descriptive Metadata, `gene_symbol`/`locus_tag` Presence, and `EC_NUMBER_PATTERN` Validation Landed Under `#189`; Bulk `data/raw/` Snapshot Deferred Under `#78`)** — `load_uniprot_proteins()` and `validate_causal_graph_proteins()` enforce required descriptive metadata (`entry_name`, `protein_name`, `organism_label`, `release_version`), `gene_symbol` or `locus_tag` presence, and `EC_NUMBER_PATTERN` (`^EC:[1-7]\.(?:[0-9]+|-)\.(?:[0-9]+|-)\.(?:n?[0-9]+|-)$`) syntax and non-duplication across all 23 pinned UniProtKB accessions in `curation/uniprot_proteins.tsv` and 51 `GENE_OR_PROTEIN` nodes across 15 maintained overlays (`test_validate_causal_graph_node_edge_and_protein_ec_invariants`), while negative controls reject missing descriptive fields, missing `gene_symbol`+`locus_tag`, and malformed/duplicate `EC:` values. |
| `taxonmech-infra-0004` | `deferred` | https://github.com/CultureBotAI/TaxonMech/issues/8 | `docs/HARMONIZATION.md`, `INFRA_TASKS.md` | **PASS (Partial / Deferred)** — `kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` SHA-256 digests and direct-taxid vs BacDive-subtree contract documented in `docs/HARMONIZATION.md`; corpus-wide `source_attestations[].notes` re-seeding deferred to Cycle 5 under `#8`. |

## 2. Executed Validation Commands

1. **Causal-graph overlay, structural referential integrity, `CausalNode`/`CausalEdge` schema invariants, UniProtKB EC/metadata + `strain_id` lineage validator, extractor, ATB/StrainInfo seeder integration, and schema unit tests**:
   ```
   .venv/bin/pytest -q -o cache_dir=/tmp/pytest_cache tests/test_causal_graph_overlays.py tests/test_atb_schema_seed.py tests/test_straininfo_schema_seed.py tests/test_seed.py tests/test_schema.py tests/test_corpus_review_inventory.py
   ```
   - `tests/test_causal_graph_overlays.py`: 7 passed (`test_five_exemplar_causal_graph_overlays_roundtrip_and_render`, `test_load_causal_graphs_rejects_invalid_or_duplicate_overlays`, `test_extract_taxon_trait_edges_preserves_granular_assertions`, `test_committed_curation_causal_graphs_overlays_load_and_validate`, `test_uniprot_proteins_catalog_and_lineage_validator`, `test_validate_causal_graph_structure_and_sources_catalog`, `test_validate_causal_graph_node_edge_and_protein_ec_invariants`).
   - `tests/test_atb_schema_seed.py`, `tests/test_straininfo_schema_seed.py`, `tests/test_seed.py`: 331 passed.
   - `tests/test_schema.py`: 9 passed (all schema structure, enum, prefix, `CausalNode` protein scope slot, and `docs/SCHEMA.md` coverage tests passed).
   - `tests/test_corpus_review_inventory.py`: 4 passed.

2. **Ruff linter**:
   ```
   .venv/bin/ruff check --no-cache src/taxonmech/seed.py tests/test_causal_graph_overlays.py
   ```
   - 0 errors (`All checks passed!`).

3. **Repository provenance, vendored schema sync, history, and docs checks**:
   - `.venv/bin/python scripts/check_provenance.py`: PASS (`data/raw/MANIFEST.yaml` matches all committed `data/raw/*.tsv` inventories; `curation/uniprot_proteins.tsv` and `curation/causal_graphs/*.yaml` verified).
   - `bash scripts/check_vendored_sync.sh`: PASS (`OK: 22 governed artifacts match the pinned claw revision`).
   - `.venv/bin/python scripts/validate_history.py`: PASS (`29 history record(s) valid against src/taxonmech/schema/history.yaml`).
   - `.venv/bin/python scripts/record_review.py check`: PASS (all structured review bundles valid).

4. **Workflow evidence and infrastructure ledger validation**:
   ```
   /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --repo-root /Users/marcin/Documents/VIMSS/ontology/Mechs/TaxonMech --evidence reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/evidence.yaml --effective-workflow /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/taxonmech/effective-workflow.json
   ```
   - Verified `valid: true`, `status: ok`, exact match with frozen `infra_snapshot.md` (`sha256: 8521a0f783afd2fc432ed972b2399c72acef2187a9cf615e303f28b9f0a12714`) and `INFRA_TASKS.md`.
