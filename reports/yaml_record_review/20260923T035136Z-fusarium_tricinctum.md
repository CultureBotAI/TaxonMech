# YAML Record Review: Fusarium tricinctum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_tricinctum.yaml
- Started UTC: 2026-09-23T03:51:36Z
- Finished UTC: 2026-09-23T03:51:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:61284` |
| Label | `Fusarium tricinctum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:679429` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_tricinctum.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/fusarium_torreyae.yaml data/taxa/eukaryota/fusarium_torulosum.yaml data/taxa/eukaryota/fusarium_tricinctum.yaml data/taxa/eukaryota/fusarium_tucumaniae.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, two exact current native GOLD organisms with three linked native GOLD projects and two linked native analysis rows, six exact NCBI type-material rows, 90 exact StrainInfo records carrying 102 exact deposit rows, eight NCBI merged-ID side rows but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:61284`, `label: Fusarium tricinctum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:679429`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:7771`, which carries the same label, parent, rank, code, two exact synonyms, 10 related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium tricinctum species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39857`, which records two retained direct organisms for `NCBITaxon:61284`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs also contain two exact organisms, `Go0136931` for strain `MPI-SDFR-AT-0068` and `Go0681028` for strain `NRRL 25481`, with three linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:61284`. The YAML preserves exact synonyms `Gibberella tricincta` and `Selenosporium tricinctum`, and it preserves the 10 related synonyms from the NCBI row.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have exact organisms for `Fusarium tricinctum MPI-SDFR-AT-0068` and `Fusarium tricinctum NRRL 25481`; `MPI-SDFR-AT-0068` has one standard-draft and one transcriptome project, `NRRL 25481` has one linked project, and native analyses link to project IDs `Gp0141911` and `Gp0783066`.

The NCBI type-material table has six exact rows for the target, the `BBA 64485`, `BBA:64485`, `CBS 393.93`, `CBS:393.93`, `NRRL 25481`, and `NRRL:25481` culture-from-epitype spellings under `Selenosporium tricinctum`. StrainInfo has 90 exact target records and 102 exact deposits. These side rows do not create generated child strains by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps eight old IDs into `NCBITaxon:61284`, but no retained row in `data/raw/ncbitaxon_taxa.tsv` carries those old IDs with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, two exact synonyms, 10 related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_tricinctum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_tricinctum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_tricinctum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:61284` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
