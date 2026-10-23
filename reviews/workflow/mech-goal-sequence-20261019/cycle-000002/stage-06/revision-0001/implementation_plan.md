# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`, Cycle 2, Stage 6, Revision 1)

- **Repository**: `CultureBotAI/TaxonMech` (`taxonmech`)
- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2`
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1` (`revision-0001`)
- **Source Revision**: `2e13ca650f72b310bf1496bcd72eb399ae160b27`
- **Scope Frozen At**: `2026-10-23T13:45:40Z`
- **Frozen `INFRA_TASKS.md` Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md` (`sha256: 276aa7fa5439a3fac069798ca1b029d8a50b2cbcc47a74f7a3423f9847ba4fa0`)

## 1. Frozen Intake Scope and Dependency Graph

At `2026-10-23T13:45:40Z`, `INFRA_TASKS.md` contained four tracked infrastructure tasks (`taxonmech-infra-0001..0004`), with `taxonmech-infra-0001`, `taxonmech-infra-0002`, and `taxonmech-infra-0003` linked to open umbrella GitHub issue `https://github.com/CultureBotAI/TaxonMech/issues/78` and `taxonmech-infra-0004` linked to open GitHub issue `https://github.com/CultureBotAI/TaxonMech/issues/8`:

| Task ID | Priority | Dependencies | Linked GitHub Issue | Cycle 2 Stage 6 Disposition |
|---|---|---|---|---|
| `taxonmech-infra-0001` | `high` | None | https://github.com/CultureBotAI/TaxonMech/issues/78 | `deferred` (extended `load_causal_graphs()` and `load_inventory()` in `src/taxonmech/seed.py` to enforce offline UniProtKB reference and NCBI Taxonomy vertical lineage consistency across all 15 maintained production overlays; carried forward under open umbrella issue `#78` pending companion task `taxonmech-infra-0002` for corpus-wide raw trait extraction and bulk overlay expansion) |
| `taxonmech-infra-0002` | `medium` | `taxonmech-infra-0001` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `deferred` (`extract_taxon_trait_edges` helper & unit tests implemented in PR `#152`; full `data/raw/taxon_trait_edges.tsv` extraction across 38,357 trait/medium-attested records deferred under open umbrella issue `#78` pending local `kg-microbe` checkout re-extraction) |
| `taxonmech-infra-0003` | `high` | `taxonmech-infra-0001` | https://github.com/CultureBotAI/TaxonMech/issues/78 | `deferred` (added release-pinned `curation/uniprot_proteins.tsv` catalog for UniProt release `2026_02` covering all 13 curated `UniProtKB` accessions across 28 `GENE_OR_PROTEIN` nodes in 15 overlays, and implemented `load_uniprot_proteins()` + `validate_causal_graph_proteins()` in `src/taxonmech/seed.py` with positive and negative-control tests in `tests/test_causal_graph_overlays.py`; full corpus-wide `data/raw/` UniProt Reference Proteomes bulk snapshot deferred under open umbrella issue `#78`) |
| `taxonmech-infra-0004` | `medium` | None | https://github.com/CultureBotAI/TaxonMech/issues/8 | `deferred` (`kg-microbe@30405b70ef762aa46c08278b2b3e06bffb0b34cd` SHA-256 provenance and direct-taxid vs BacDive-subtree contract documented in `docs/HARMONIZATION.md` in PR `#152`; corpus-wide `source_attestations[].notes` re-seeding across 27,118 records deferred under open issue `#8` pending a dedicated 626,048-record YAML + `pages/` regeneration pass) |

## 2. Dependency-Aware Execution Order and Acceptance Criteria

### Wave 1: Release-Pinned Curated UniProtKB Reference Catalog & Offline Accession/Lineage Validator (`taxonmech-infra-0003` & `taxonmech-infra-0001`)

- **Problem Statement**:
  - During Cycle 2 Stage 3 (`add-uniprot-protein-examples`), live UniProt REST API verification exposed multiple accession/locus/strain/checksum mismatches in candidate protein nodes (`UniProtKB:Q9I4X3` `pqsA` vs `UniProtKB:Q9HWH2` `phzM`; `UniProtKB:Q58254` `mcrC` vs `UniProtKB:Q58256` `mcrA`; `UniProtKB:P0A858` `tpiA` vs `UniProtKB:P0A853` `tnaA`; `UniProtKB:Q9I4X2` `pqsB` vs `UniProtKB:Q9HWG9` `phzS`; `UniProtKB:Q58255` `mcrG` vs `UniProtKB:Q58252` `mcrB`; `UniProtKB:Q55P57` belonging to sibling species *Cryptococcus deneoformans* B-3501A `NCBITaxon:283643` rather than *C. deuterogattii* `NCBITaxon:1859096`/`NCBITaxon:294750`).
  - Without a committed offline reference table and seeder validation gate, `load_causal_graphs()` and `load_inventory()` accepted any syntactically valid `UniProtKB:` CURIE and 16-hex `sequence_crc64` without checking whether the accession, entry status, organism taxon ID, reference proteome ID, gene symbol, ordered locus tag, sequence length, CRC64 checksum, sequence version, or EC xrefs match the pinned UniProtKB entry or whether the protein's `organism_taxon_id` lies on the same vertical NCBI Taxonomy lineage as the host `TaxonRecord.identifier`.
- **Implementation Steps**:
  1. Create `curation/uniprot_proteins.tsv` (14 columns: `uniprot_id`, `entry_name`, `entry_status`, `protein_name`, `organism_taxon_id`, `organism_label`, `proteome_id`, `gene_symbol`, `locus_tag`, `ec_numbers`, `sequence_length`, `sequence_crc64`, `sequence_version`, `release_version`) pinning UniProt release `2026_02` metadata for all 13 curated `UniProtKB` accessions across the 15 maintained overlays (`UniProtKB:O26796`, `UniProtKB:P00722`, `UniProtKB:P02920`, `UniProtKB:P0A853`, `UniProtKB:P21332`, `UniProtKB:P27876`, `UniProtKB:P39116`, `UniProtKB:Q55P57`, `UniProtKB:Q58252`, `UniProtKB:Q58256`, `UniProtKB:Q5KGF0`, `UniProtKB:Q9HWG9`, `UniProtKB:Q9HWH2`).
  2. Add `UNIPROT_PROTEINS_PATH`, `UNIPROT_PROTEIN_FIELDS`, `load_uniprot_proteins()`, and `validate_causal_graph_proteins()` in `src/taxonmech/seed.py`:
     - Verify every `GENE_OR_PROTEIN` node in `curation/causal_graphs/*.yaml` against `curation/uniprot_proteins.tsv` (`entry_status`, `organism_taxon_id`, `proteome_id`, `locus_tag`, `gene_symbol`, `sequence_length`, `sequence_crc64`, `sequence_version`, and `EC:` xrefs).
     - Enforce NCBI Taxonomy vertical lineage consistency when `taxa` is loaded in `load_inventory()`: `org_tid == tid or tid in org_lineage or (org_tid in tid_lineage and _taxon_is_species_or_below(taxa, org_tid))`, permitting exact strain matches (`NCBITaxon:83333 -> NCBITaxon:83333`), species-level reference-proteome exemplar projections (`NCBITaxon:83333 -> NCBITaxon:562`), and substrain-to-parent-strain reference-proteome bindings (`NCBITaxon:83333 -> NCBITaxon:511145`), while rejecting cross-species or sibling-strain assignments (`NCBITaxon:283643 -> NCBITaxon:1859096`).
  3. Document `curation/uniprot_proteins.tsv` and the offline validation contract in `curation/causal_graphs/README.md`.
  4. Add positive and negative-control unit tests (`test_uniprot_proteins_catalog_and_lineage_validator`) in `tests/test_causal_graph_overlays.py`.
- **Carry-Forward Scope (`deferred` under open umbrella issue `#78`)**:
  - Umbrella issue `#78` remains open for corpus-wide bulk `data/raw/` UniProt Reference Proteomes ingestion and `data/raw/taxon_trait_edges.tsv` extraction across the remaining 626,033 records.

### Wave 2: Granular Trait Edge Re-Extraction & Corpus-Wide Attestation Note Re-Seeding (`taxonmech-infra-0002` & `taxonmech-infra-0004`)

- **Carry-Forward Scope (`deferred` under open issues `#78` and `#8`)**:
  - `taxonmech-infra-0002` (`data/raw/taxon_trait_edges.tsv` generation via `extract_taxon_trait_edges()`) requires an upstream local `kg-microbe` checkout not mounted in this workspace and remains `deferred` under `#78`.
  - `taxonmech-infra-0004` (corpus-wide `source_attestations[].notes` regeneration across 27,118 multi-edge records) requires a coordinated 626,048-record YAML and `pages/` shard regeneration pass and remains `deferred` under `#8`.
