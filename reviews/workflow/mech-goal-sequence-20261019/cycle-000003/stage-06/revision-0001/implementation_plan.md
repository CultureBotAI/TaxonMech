# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`, Cycle 3, Stage 6, Revision 1)

- **Repository**: `CultureBotAI/TaxonMech` (`taxonmech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1` (`revision-0001`)
- **Source Revision**: `a050e29c140f7ca7e74432e364b10d732e2922f1`
- **Scope Frozen At**: `2026-10-25T05:14:57Z`
- **Frozen `INFRA_TASKS.md` Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md` (`sha256: 0ba8eeef1675ee22621b04fa97775dd2d0d34f65868db2d871417bbde7dade3e`)

## 1. Frozen Intake Scope and Dependency Graph

At `2026-10-25T05:14:57Z`, `INFRA_TASKS.md` contained four tracked infrastructure tasks (`taxonmech-infra-0001..0004`), with `taxonmech-infra-0001`, `taxonmech-infra-0002`, and `taxonmech-infra-0003` linked to open umbrella GitHub issue `https://github.com/CultureBotAI/TaxonMech/issues/78` and `taxonmech-infra-0004` linked to open GitHub issue `https://github.com/CultureBotAI/TaxonMech/issues/8`:

| Task ID | Priority | Dependencies | Linked GitHub Issue | Cycle 3 Stage 6 Disposition |
|---|---|---|---|---|
| `taxonmech-infra-0001` | `high` | None | https://github.com/CultureBotAI/TaxonMech/issues/78 | `deferred` (implemented `validate_causal_graph_structure()` in `src/taxonmech/seed.py` enforcing `node_id`/`edge_id` uniqueness, edge endpoint referential integrity against `graph.nodes`, non-self-loop edges, and non-empty `evidence[].reference`, and wired `load_uniprot_proteins()` + `load_causal_graphs()` into `scripts/check_provenance.py`; carried forward under open umbrella issue `#78` pending companion task `taxonmech-infra-0002` for corpus-wide raw trait extraction and bulk overlay expansion) |
| `taxonmech-infra-0002` | `medium` | `taxonmech-infra-0001` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `deferred` (`extract_taxon_trait_edges` helper & unit tests implemented in PR `#152`; full `data/raw/taxon_trait_edges.tsv` extraction across 38,357 trait/medium-attested records deferred under open umbrella issue `#78` pending local `kg-microbe` checkout re-extraction) |
| `taxonmech-infra-0003` | `high` | `taxonmech-infra-0001` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `deferred` (registered `uniprot_proteins` in `conf/sources.yaml` pointing to release-pinned `curation/uniprot_proteins.tsv` [UniProt release `2026_02`, 17 accessions across 38 `GENE_OR_PROTEIN` nodes in 15 overlays], and extended `validate_causal_graph_proteins()` + `load_inventory()` in `src/taxonmech/seed.py` to enforce `strain_id` format, `bacdive_strains.tsv` inventory membership, and vertical NCBI Taxonomy lineage consistency against both record `identifier` and `organism_taxon_id`; full corpus-wide `data/raw/` UniProt Reference Proteomes bulk snapshot deferred under open umbrella issue `#78`) |
| `taxonmech-infra-0004` | `medium` | None | https://github.com/CultureBotAI/TaxonMech/issues/8 | `deferred` (`kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` SHA-256 provenance and direct-taxid vs BacDive-subtree contract documented in `docs/HARMONIZATION.md` in PR `#152`; corpus-wide `source_attestations[].notes` re-seeding across 27,118 records deferred under open issue `#8` pending a dedicated 626,048-record YAML + `pages/` regeneration pass) |

## 2. Dependency-Aware Execution Order and Acceptance Criteria

### Wave 1: Causal-Graph Structural Referential Integrity Gate, Provenance Catalog Registration, and `GENE_OR_PROTEIN` `strain_id` Lineage Validation (`taxonmech-infra-0001` & `taxonmech-infra-0003`)

- **Problem Statement**:
  1. `load_causal_graphs()` in `src/taxonmech/seed.py` verified `graph_id` uniqueness per overlay but did not enforce graph-internal referential integrity (uniqueness of `node_id` and `edge_id` within a graph, `edge.subject` and `edge.object` referencing declared `node_id`s in `graph.nodes`, prohibition of self-loop edges `subject == object`, and presence of non-empty `evidence[].reference` on every edge). Because `CausalGraph.nodes` and `CausalGraph.edges` are YAML lists, LinkML's JSON Schema validator (`scripts/validate_strict.py`) cannot detect dangling edge endpoints or duplicate `node_id`/`edge_id` values.
  2. `validate_causal_graph_proteins()` in `src/taxonmech/seed.py` validated `organism_taxon_id` against `ncbitaxon_taxa.tsv` and `curation/uniprot_proteins.tsv`, but did not validate `strain_id` (`kgmicrobe.strain:bacdive_*`, present on 16 `GENE_OR_PROTEIN` nodes across 5 maintained overlays) against `data/raw/bacdive_strains.tsv` or verify that the linked BacDive strain's taxon IDs are lineage-consistent with both the host `TaxonRecord.identifier` and the protein's `organism_taxon_id`.
  3. `conf/sources.yaml` omitted an entry for `uniprot_proteins` (`curation/uniprot_proteins.tsv`), and `scripts/check_provenance.py` did not invoke `load_uniprot_proteins()` and `load_causal_graphs()`.
- **Implementation Steps**:
  1. Register `uniprot_proteins` under `sources:` in `conf/sources.yaml` documenting the release-pinned UniProtKB (`2026_02`) / UniProt Reference Proteomes catalog at `curation/uniprot_proteins.tsv`.
  2. Add `validate_causal_graph_structure()` in `src/taxonmech/seed.py` and invoke it in `load_causal_graphs()` to enforce `node_id` and `edge_id` uniqueness, `edge.subject`/`edge.object` membership in `graph.nodes`, `subject != object`, and non-empty `evidence[].reference`.
  3. Add `BACDIVE_STRAIN_ID_PATTERN` and `_taxa_lineage_compatible()` in `src/taxonmech/seed.py`, and extend `validate_causal_graph_proteins()` (and `load_causal_graphs()` / `load_inventory()`) with `strains: dict[str, list[dict[str, str]]] | None = None` to verify that every `GENE_OR_PROTEIN` `strain_id` matches `^kgmicrobe\.strain:bacdive_[1-9][0-9]*$`, exists in `data/raw/bacdive_strains.tsv`, and links to at least one taxon ID that is vertically lineage-compatible with both the host `TaxonRecord.identifier` and `organism_taxon_id`.
  4. Wire `load_uniprot_proteins()` and `load_causal_graphs()` into `scripts/check_provenance.py`.
  5. Add positive and negative-control unit tests (`test_validate_causal_graph_structure_and_sources_catalog` and extended `test_uniprot_proteins_catalog_and_lineage_validator`) in `tests/test_causal_graph_overlays.py`.
- **Carry-Forward Scope (`deferred` under open umbrella issue `#78`)**:
  - Umbrella issue `#78` remains open for corpus-wide bulk `data/raw/` UniProt Reference Proteomes ingestion and `data/raw/taxon_trait_edges.tsv` extraction across the remaining 626,033 records.

### Wave 2: Granular Trait Edge Re-Extraction & Corpus-Wide Attestation Note Re-Seeding (`taxonmech-infra-0002` & `taxonmech-infra-0004`)

- **Carry-Forward Scope (`deferred` under open issues `#78` and `#8`)**:
  - `taxonmech-infra-0002` (`data/raw/taxon_trait_edges.tsv` generation via `extract_taxon_trait_edges()`) requires an upstream local `kg-microbe` checkout not mounted in this workspace and remains `deferred` under `#78`.
  - `taxonmech-infra-0004` (corpus-wide `source_attestations[].notes` regeneration across 27,118 multi-edge records) requires a coordinated 626,048-record YAML and `pages/` shard regeneration pass and remains `deferred` under `#8`.
