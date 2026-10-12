# YAML Record Review: Diaporthe cotoneastri

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/diaporthe_cotoneastri.yaml
- Started UTC: 2026-09-22T22:29:06Z
- Finished UTC: 2026-09-22T22:29:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1214570` |
| Label | `Diaporthe cotoneastri` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2972384` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/diaporthe_cotoneastri.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/diaporthe_cf_hevae.yaml data/taxa/eukaryota/diaporthe_citriasiana.yaml data/taxa/eukaryota/diaporthe_cotoneastri.yaml data/taxa/eukaryota/diaporthe_eres.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with five retained direct organisms, five exact native GOLD organisms with no linked projects or analyses, four exact NCBI type-material rows, two exact StrainInfo direct records carrying four matching deposit designations, no exact BacDive rows, no final raw strain rows, four NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1214570`, `label: Diaporthe cotoneastri`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2972384`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:274827`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Diaporthe eres species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:5099`, which records five retained direct organisms for `NCBITaxon:1214570`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1214570`. The YAML carries the single exact synonym and all six related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain five exact organisms: `Go0622726` for `Phomopsis cotoneastri P 407`, `Go0622727` for `Phomopsis cotoneastri IMI 162181a`, `Go0622728` for `Phomopsis cotoneastri DSM 5135`, `Go0622729` for `Phomopsis cotoneastri CMI 162181a`, and `Go0622730` for `Phomopsis cotoneastri CBS 439.82`. No native GOLD projects or analyses link to those organisms in the local snapshot.

The NCBI type-material inventory contributes four exact rows, covering culture-from-isotype variants of `CBS 439.82` and isotype variants of `CBS H-7633`.

The exact StrainInfo side inventory has two direct records and four matching deposit designations for `NCBITaxon:1214570`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/diaporthe_cotoneastri.yaml` plus `just validate-strict data/taxa/eukaryota/diaporthe_cotoneastri.yaml`.

## Additional Notes

The bounded scan found side-inventory `data/raw/ncbi_merged_ids.tsv` mappings from `NCBITaxon:1203521`, `NCBITaxon:1203522`, `NCBITaxon:1203524`, and `NCBITaxon:699521` into `NCBITaxon:1214570`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
