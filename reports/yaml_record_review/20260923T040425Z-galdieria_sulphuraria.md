# YAML Record Review: Galdieria sulphuraria

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/galdieria_sulphuraria.yaml
- Started UTC: 2026-09-23T04:04:25Z
- Finished UTC: 2026-09-23T04:04:25Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:130081` |
| Label | `Galdieria sulphuraria` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:83373` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/galdieria_sulphuraria.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/galdieria_daedala.yaml data/taxa/eukaryota/galdieria_partita.yaml data/taxa/eukaryota/galdieria_phlegrea.yaml data/taxa/eukaryota/galdieria_sulphuraria.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with 14 organism assertions, 11 exact current native GOLD organisms with 275 linked native GOLD projects and nine linked native analysis rows, two exact NCBI type-material rows, four exact StrainInfo records carrying five exact deposit rows, no exact BacDive or NCBI merged-ID rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:130081`, `label: Galdieria sulphuraria`, `rank: SPECIES`, `parent_taxon: NCBITaxon:83373`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:24996`, which carries the same label, parent, rank, code, one exact synonym, two related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Galdieria`; the bounded scan checked all 8 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:7381`, which records 14 retained direct organisms for `NCBITaxon:130081`; this agrees with `source_attestations[1].assertion_count: 14` and its organism assertion unit. A complete current native GOLD sweep found 11 exact organisms, 275 linked projects, and nine linked analyses for the same NCBI taxon ID.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:130081`. The YAML preserves exact synonym `Pleurococcus sulphurarius` and the two related synonyms from the NCBI row.

The retained GOLD aggregate supplies 14 organism assertions. The current native GOLD catalogs have 11 exact organisms filed directly under `NCBITaxon:130081`, including strains `107.79`, `YNP5578.1`, `SAG21`, `MtSh`, `Az2`, `RT22`, `5572`, `MS1`, `SAG 21.92`, and `CCMEE 5587.1`; the complete exact sweep found 275 linked projects and nine native GOLD analysis rows.

The NCBI type-material table has two exact rows for the target, the `SAG 17.91` and `SAG:17.91` type-material spellings under `Pleurococcus sulphurarius`. StrainInfo has four exact target records and five exact deposits. These side rows do not create generated local strain entries by themselves.

No side `data/raw/ncbi_merged_ids.tsv` row maps an old ID into `NCBITaxon:130081`, and no retained row in `data/raw/ncbitaxon_taxa.tsv` carries a retired ID for this target, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, one exact synonym, two related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/galdieria_sulphuraria.yaml` plus `just validate-strict data/taxa/eukaryota/galdieria_sulphuraria.yaml`.

## Additional Notes

No prior exact ignored review report existed for `galdieria_sulphuraria` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:130081` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
