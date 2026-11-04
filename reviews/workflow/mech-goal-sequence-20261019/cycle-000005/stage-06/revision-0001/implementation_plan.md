# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`, Cycle 5, Stage 6, Revision 1)

- **Repository**: `CultureBotAI/TaxonMech` (`taxonmech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `5`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1` (`revision-0001`)
- **Source Revision**: `e0cc7c86ac2107242ab499db610737f5fcad1c9b`
- **Scope Frozen At**: `2026-11-04T11:34:48Z`
- **Frozen `INFRA_TASKS.md` Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/infra_snapshot.md` (`sha256: b64bec8e5962706b6df2c6537556d0a228bd638c85343e026bc55fc05b2cec1e`)

## 1. Frozen Intake Scope and Dependency Graph

At `2026-11-04T11:34:48Z`, `INFRA_TASKS.md` contained four tracked infrastructure tasks (`taxonmech-infra-0001..0004`), with `taxonmech-infra-0001`, `taxonmech-infra-0002`, and `taxonmech-infra-0003` linked to open umbrella GitHub issue `https://github.com/CultureBotAI/TaxonMech/issues/78` (with Cycle 5 Stage 6 grouped repository-local invariant and provenance enforcement tracked in dedicated sub-issue `https://github.com/CultureBotAI/TaxonMech/issues/199`) and `taxonmech-infra-0004` linked to open GitHub issue `https://github.com/CultureBotAI/TaxonMech/issues/8`:

| Task ID | Priority | Dependencies | Linked GitHub Issue | Cycle 5 Stage 6 Disposition |
|---|---|---|---|---|
| `taxonmech-infra-0001` | `high` | None | https://github.com/CultureBotAI/TaxonMech/issues/78 (`#199`) | `deferred` (extended `validate_causal_graph_structure()` and `validate_causal_graph_proteins()` in `src/taxonmech/seed.py` and added `causal_graph_provenance_problems()` in `scripts/check_provenance.py` under `#199` to enforce `CausalGraph` node connectivity [no disconnected nodes unreferenced by any edge], `EDGE_ID_PATTERN` syntax on `graph_id` and `node_id`, `NCBITAXON_ID_PATTERN` syntax on `identifier`, species-or-below scope (`_taxon_is_species_or_below`) on host record taxa, and full cross-table provenance + `curation/seed_scope.tsv` membership + `<identifier>.yaml` filename-stem validation across all 15 maintained overlays [204 edges, 64 `GENE_OR_PROTEIN` nodes]; carried forward to Cycle 6 under open umbrella issue `#78` pending companion task `taxonmech-infra-0002` for corpus-wide raw trait extraction and bulk overlay expansion) |
| `taxonmech-infra-0002` | `medium` | `taxonmech-infra-0001` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `deferred` (`extract_taxon_trait_edges` helper & unit tests implemented in PR `#152`; full `data/raw/taxon_trait_edges.tsv` extraction across 38,357 trait/medium-attested records deferred to Cycle 6 under open umbrella issue `#78` pending local `kg-microbe` checkout re-extraction) |
| `taxonmech-infra-0003` | `high` | `taxonmech-infra-0001` | https://github.com/CultureBotAI/TaxonMech/issues/78 (`#199`) | `deferred` (extended `load_uniprot_proteins()` and `validate_causal_graph_proteins()` in `src/taxonmech/seed.py` and `causal_graph_provenance_problems()` in `scripts/check_provenance.py` under `#199` to enforce `UNIPROT_ID_PATTERN`, `NCBITAXON_ID_PATTERN`, and `PROTEOME_ID_PATTERN` regex syntax, species-or-below scope (`_taxon_is_species_or_below`) on `organism_taxon_id`, and full cross-table lineage/strain verification against `data/raw/ncbitaxon_taxa.tsv` and `data/raw/bacdive_strains.tsv` across all 29 pinned UniProtKB rows in `curation/uniprot_proteins.tsv` and 64 `GENE_OR_PROTEIN` nodes in 15 overlays; full corpus-wide `data/raw/` UniProt Reference Proteomes bulk snapshot deferred to Cycle 6 under open umbrella issue `#78`) |
| `taxonmech-infra-0004` | `medium` | None | https://github.com/CultureBotAI/TaxonMech/issues/8 | `deferred` (`kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` SHA-256 provenance and direct-taxid vs BacDive-subtree contract documented in `docs/HARMONIZATION.md` in PR `#152` and enforced via deterministic audit helpers in `scripts/audit_review_remediation_groups.py` in Cycle 5 Stage 5 PR `#198` (`#196`, `#197`); corpus-wide `source_attestations[].notes` re-seeding across 27,118 records deferred to Cycle 6 under open issue `#8` pending a dedicated 626,048-record YAML + `pages/` regeneration pass) |

## 2. Dependency-Aware Execution Order and Acceptance Criteria

### Wave 1: `CausalGraph` Node Connectivity, `graph_id`/`node_id`/UniProtKB/Proteome/NCBITaxon Regex Enforcement, Species-or-Below Scope Enforcement, and Full Provenance Cross-Table Gate (`taxonmech-infra-0001` & `taxonmech-infra-0003`; Issue `#199` under `#78`)

- **Problem Statement**:
  1. `validate_causal_graph_structure()` in `src/taxonmech/seed.py` verified that every `edge.subject` and `edge.object` existed in `graph.nodes`, but did not check the converse: a `CausalGraph` could include disconnected `CausalNode` entries never referenced by any `CausalEdge`.
  2. `validate_causal_graph_structure()`, `load_uniprot_proteins()`, and `validate_causal_graph_proteins()` checked prefix strings (`startswith("UniProtKB:")`, `startswith("NCBITaxon:")`, `startswith("UP:UP")`) rather than strict canonical regexes (`UNIPROT_ID_PATTERN`, `NCBITAXON_ID_PATTERN`, `PROTEOME_ID_PATTERN`, and `EDGE_ID_PATTERN` on `graph_id`), and did not enforce the repository species-or-below rule (`_taxon_is_species_or_below`) on overlay `identifier` and `GENE_OR_PROTEIN` `organism_taxon_id`.
  3. `scripts/check_provenance.py` invoked `load_uniprot_proteins()` and `load_causal_graphs()` without passing `taxa` (`data/raw/ncbitaxon_taxa.tsv`) or `strains` (`data/raw/bacdive_strains.tsv`) and without verifying that every overlay in `curation/causal_graphs/*.yaml` matches its `identifier` filename stem (`<identifier>.yaml` with `:` replaced by `_`) and is present in `curation/seed_scope.tsv`.
- **Implementation Steps**:
  1. Define `UNIPROT_ID_PATTERN`, `NCBITAXON_ID_PATTERN`, and `PROTEOME_ID_PATTERN` in `src/taxonmech/seed.py`.
  2. Extend `load_uniprot_proteins()` in `src/taxonmech/seed.py` to enforce `UNIPROT_ID_PATTERN`, `NCBITAXON_ID_PATTERN`, `PROTEOME_ID_PATTERN`, and (when `taxa` is provided) `ncbitaxon_taxa.tsv` presence and `_taxon_is_species_or_below(taxa, org_tid)` on every row of `curation/uniprot_proteins.tsv`.
  3. Extend `validate_causal_graph_structure()` in `src/taxonmech/seed.py` to enforce `NCBITAXON_ID_PATTERN` on `tid`, `EDGE_ID_PATTERN` on `graph_id` and `node_id`, and full node connectivity (`disconnected = sorted(seen_node_ids - connected_node_ids)` must be empty).
  4. Extend `validate_causal_graph_proteins()` in `src/taxonmech/seed.py` to enforce `NCBITAXON_ID_PATTERN` and `_taxon_is_species_or_below(taxa, tid)` on every overlay's host `tid` (regardless of whether the graph has `GENE_OR_PROTEIN` nodes), plus `UNIPROT_ID_PATTERN`, `NCBITAXON_ID_PATTERN`, `PROTEOME_ID_PATTERN`, and `_taxon_is_species_or_below(taxa, org_tid)` on `GENE_OR_PROTEIN` nodes.
  5. Add `causal_graph_provenance_problems(repo_root)` in `scripts/check_provenance.py` to load `data/raw/ncbitaxon_taxa.tsv`, `data/raw/bacdive_strains.tsv`, and `curation/seed_scope.tsv`, run full cross-table validation of `curation/uniprot_proteins.tsv` and `curation/causal_graphs/*.yaml`, and verify filename-stem and `seed_scope.tsv` alignment.
  6. Update `curation/causal_graphs/README.md` and add unit and negative-control tests (`test_causal_graph_node_connectivity_and_id_patterns_enforced` and `test_causal_graph_provenance_problems_gate`) in `tests/test_causal_graph_overlays.py`.
- **Carry-Forward Scope (`deferred` under open umbrella issue `#78`)**:
  - Issue `#199` is closed by this PR; umbrella issue `#78` remains open for corpus-wide bulk `data/raw/` UniProt Reference Proteomes ingestion and `data/raw/taxon_trait_edges.tsv` extraction across the remaining 626,033 records.

### Wave 2: Granular Trait Edge Re-Extraction & Corpus-Wide Attestation Note Re-Seeding (`taxonmech-infra-0002` & `taxonmech-infra-0004`)

- **Carry-Forward Scope (`deferred` to Cycle 6 under open issues `#78` and `#8`)**:
  - `taxonmech-infra-0002` (`data/raw/taxon_trait_edges.tsv` generation via `extract_taxon_trait_edges()`) requires an upstream local `kg-microbe` checkout not mounted in this workspace and remains `deferred` to Cycle 6 under `#78`.
  - `taxonmech-infra-0004` (corpus-wide `source_attestations[].notes` regeneration across 27,118 multi-edge records) requires a coordinated 626,048-record YAML and `pages/` shard regeneration pass and remains `deferred` to Cycle 6 under `#8`.
