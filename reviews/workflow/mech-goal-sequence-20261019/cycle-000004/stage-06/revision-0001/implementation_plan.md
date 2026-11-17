# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`, Cycle 4, Stage 6, Revision 1)

- **Repository**: `CultureBotAI/TaxonMech` (`taxonmech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `4`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1` (`revision-0001`)
- **Source Revision**: `11bf38c5f683ad2b21039b41771e64f35930c81c`
- **Scope Frozen At**: `2026-10-31T14:45:23Z`
- **Frozen `INFRA_TASKS.md` Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md` (`sha256: 8521a0f783afd2fc432ed972b2399c72acef2187a9cf615e303f28b9f0a12714`)

## 1. Frozen Intake Scope and Dependency Graph

At `2026-10-31T14:45:23Z`, `INFRA_TASKS.md` contained four tracked infrastructure tasks (`taxonmech-infra-0001..0004`), with `taxonmech-infra-0001`, `taxonmech-infra-0002`, and `taxonmech-infra-0003` linked to open umbrella GitHub issue `https://github.com/CultureBotAI/TaxonMech/issues/78` (with Cycle 4 Stage 6 grouped repository-local invariant enforcement tracked in dedicated sub-issue `https://github.com/CultureBotAI/TaxonMech/issues/189`) and `taxonmech-infra-0004` linked to open GitHub issue `https://github.com/CultureBotAI/TaxonMech/issues/8`:

| Task ID | Priority | Dependencies | Linked GitHub Issue | Cycle 4 Stage 6 Disposition |
|---|---|---|---|---|
| `taxonmech-infra-0001` | `high` | None | https://github.com/CultureBotAI/TaxonMech/issues/78 (`#189`) | `deferred` (extended `validate_causal_graph_structure()` and `validate_causal_graph_proteins()` in `src/taxonmech/seed.py` under `#189` to enforce `CausalNodeTypeEnum` membership (`CAUSAL_NODE_TYPES`), isolation of all 9 protein-only slots (`PROTEIN_ONLY_NODE_SLOTS`) to `GENE_OR_PROTEIN` nodes, `CURIE_PATTERN` and `EDGE_ID_PATTERN` syntax, `NCBITaxon:` grounding and `ncbitaxon_taxa.tsv` lineage consistency on `TAXON` nodes, duplicate `xrefs`/parallel-edge/evidence-reference rejection, and `EVIDENCE_REFERENCE_PATTERN` (`PMID:`, `PMC:PMC`, `DOI:10.`, `http(s)://`) on edge evidence across all 15 maintained overlays [161 edges, 51 `GENE_OR_PROTEIN` nodes]; carried forward under open umbrella issue `#78` pending companion task `taxonmech-infra-0002` for corpus-wide raw trait extraction and bulk overlay expansion) |
| `taxonmech-infra-0002` | `medium` | `taxonmech-infra-0001` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `deferred` (`extract_taxon_trait_edges` helper & unit tests implemented in PR `#152`; full `data/raw/taxon_trait_edges.tsv` extraction across 38,357 trait/medium-attested records deferred to Cycle 5 under open umbrella issue `#78` pending local `kg-microbe` checkout re-extraction) |
| `taxonmech-infra-0003` | `high` | `taxonmech-infra-0001` | https://github.com/CultureBotAI/TaxonMech/issues/78 (`#189`) | `deferred` (extended `load_uniprot_proteins()` and `validate_causal_graph_proteins()` in `src/taxonmech/seed.py` under `#189` to enforce required descriptive metadata (`entry_name`, `protein_name`, `organism_label`, `release_version`), `gene_symbol` or `locus_tag` presence, and `EC_NUMBER_PATTERN` (`^EC:[1-7]\.(?:[0-9]+|-)\.(?:[0-9]+|-)\.(?:n?[0-9]+|-)$`) syntax and non-duplication on all 23 pinned UniProtKB rows in `curation/uniprot_proteins.tsv` and 51 `GENE_OR_PROTEIN` nodes across 15 overlays; full corpus-wide `data/raw/` UniProt Reference Proteomes bulk snapshot deferred to Cycle 5 under open umbrella issue `#78`) |
| `taxonmech-infra-0004` | `medium` | None | https://github.com/CultureBotAI/TaxonMech/issues/8 | `deferred` (`kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` SHA-256 provenance and direct-taxid vs BacDive-subtree contract documented in `docs/HARMONIZATION.md` in PR `#152`; corpus-wide `source_attestations[].notes` re-seeding across 27,118 records deferred to Cycle 5 under open issue `#8` pending a dedicated 626,048-record YAML + `pages/` regeneration pass) |

## 2. Dependency-Aware Execution Order and Acceptance Criteria

### Wave 1: `CausalNode`/`CausalEdge` Schema Invariant Enforcement, Protein-Only Slot Isolation, `TAXON` Node Lineage Validation, and UniProtKB EC/Metadata Completeness (`taxonmech-infra-0001` & `taxonmech-infra-0003`; Issue `#189` under `#78`)

- **Problem Statement**:
  1. `validate_causal_graph_structure()` in `src/taxonmech/seed.py` checked `node_id` and `edge_id` uniqueness, endpoint membership in `graph.nodes`, `subject != object`, and non-empty `evidence[].reference`, but did not enforce `CausalNodeTypeEnum` membership (`CAUSAL_NODE_TYPES`), allowing invalid node types (such as `"PHENOTYPE"` in an earlier test fixture) to pass `validate_causal_graph_structure()` before LinkML validation.
  2. `validate_causal_graph_structure()` did not prohibit the 9 `GENE_OR_PROTEIN`-specific UniProtKB protein-grounding slots (`organism_taxon_id`, `strain_id`, `proteome_id`, `gene_symbol`, `locus_tag`, `sequence_length`, `sequence_crc64`, `sequence_version`, `entry_status`) on non-`GENE_OR_PROTEIN` nodes (`PATHWAY`, `CHEMICAL`, `BIOLOGICAL_PROCESS`, `TAXON`, `TRAIT`, etc.), nor did it enforce `CURIE_PATTERN` on `grounding`, `xrefs`, and `predicate_id`, `EDGE_ID_PATTERN` on `edge_id`, `EVIDENCE_REFERENCE_PATTERN` on `evidence[].reference`, or uniqueness of `xrefs`, edge `evidence[].reference` citations, and parallel `(subject, predicate_id or predicate, object)` edges.
  3. `load_uniprot_proteins()` validated `uniprot_id`, `entry_status`, `organism_taxon_id`, `proteome_id`, `sequence_length`, `sequence_version`, and `sequence_crc64`, but did not enforce non-empty descriptive columns (`entry_name`, `protein_name`, `organism_label`, `release_version`), presence of `gene_symbol` or `locus_tag`, or `EC_NUMBER_PATTERN` (`EC:<digits>`) syntax and uniqueness on `ec_numbers` (and `validate_causal_graph_proteins()` did not validate `EC:` xref syntax on `GENE_OR_PROTEIN` nodes or `ncbitaxon_taxa.tsv` lineage consistency on `TAXON` nodes).
- **Implementation Steps**:
  1. Define `CURIE_PATTERN`, `EDGE_ID_PATTERN`, `EC_NUMBER_PATTERN`, `EVIDENCE_REFERENCE_PATTERN`, `CAUSAL_NODE_TYPES`, and `PROTEIN_ONLY_NODE_SLOTS` in `src/taxonmech/seed.py`.
  2. Extend `load_uniprot_proteins()` in `src/taxonmech/seed.py` to enforce non-empty `entry_name`, `protein_name`, `organism_label`, and `release_version`, presence of `gene_symbol` or `locus_tag`, and `EC_NUMBER_PATTERN` syntax and uniqueness on `ec_numbers`.
  3. Extend `validate_causal_graph_structure()` in `src/taxonmech/seed.py` to enforce `CAUSAL_NODE_TYPES` membership, `PROTEIN_ONLY_NODE_SLOTS` isolation to `GENE_OR_PROTEIN` nodes, `CURIE_PATTERN` on `grounding`, `xrefs`, and `predicate_id`, `NCBITaxon:` prefix on `TAXON` node `grounding`, `EDGE_ID_PATTERN` on `edge_id`, `EVIDENCE_REFERENCE_PATTERN` on `evidence[].reference`, and non-duplication of `xrefs` (including against `grounding`), `evidence[].reference`, and parallel `(subject, predicate_id or predicate, object)` edges.
  4. Extend `validate_causal_graph_proteins()` in `src/taxonmech/seed.py` to verify `EC_NUMBER_PATTERN` on `GENE_OR_PROTEIN` `EC:` xrefs and verify that any `TAXON` node `grounding` exists in `ncbitaxon_taxa.tsv` and is vertically lineage-compatible (`_taxa_lineage_compatible`) with the host `TaxonRecord.identifier`.
  5. Document the expanded Gate 3 and Gate 4 contracts in `curation/causal_graphs/README.md` and add comprehensive unit and negative-control tests (`test_validate_causal_graph_node_edge_and_protein_ec_invariants`) in `tests/test_causal_graph_overlays.py`.
- **Carry-Forward Scope (`deferred` under open umbrella issue `#78`)**:
  - Issue `#189` is closed by this PR; umbrella issue `#78` remains open for corpus-wide bulk `data/raw/` UniProt Reference Proteomes ingestion and `data/raw/taxon_trait_edges.tsv` extraction across the remaining 626,033 records.

### Wave 2: Granular Trait Edge Re-Extraction & Corpus-Wide Attestation Note Re-Seeding (`taxonmech-infra-0002` & `taxonmech-infra-0004`)

- **Carry-Forward Scope (`deferred` to Cycle 5 under open issues `#78` and `#8`)**:
  - `taxonmech-infra-0002` (`data/raw/taxon_trait_edges.tsv` generation via `extract_taxon_trait_edges()`) requires an upstream local `kg-microbe` checkout not mounted in this workspace and remains `deferred` to Cycle 5 under `#78`.
  - `taxonmech-infra-0004` (corpus-wide `source_attestations[].notes` regeneration across 27,118 multi-edge records) requires a coordinated 626,048-record YAML and `pages/` shard regeneration pass and remains `deferred` to Cycle 5 under `#8`.
