# YAML Record Review: Dichomitus squalens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dichomitus_squalens.yaml
- Started UTC: 2026-09-22T22:36:55Z
- Finished UTC: 2026-09-22T22:36:55Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:114155` |
| Label | `Dichomitus squalens` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:114154` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dichomitus_squalens.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dichomitus_squalens.yaml data/taxa/eukaryota/dichotomocladium_elegans.yaml data/taxa/eukaryota/dichotomocladium_hesseltinei.yaml data/taxa/eukaryota/dichotomocladium_robustum.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 20 retained direct organisms, 20 exact native GOLD organisms linked to 504 projects and two analyses, no exact NCBI type-material rows, 24 exact StrainInfo direct records carrying 25 matching deposit designations, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |
| Exact native GOLD scan | Passed; the exact compressed GOLD scan confirmed 20 organism rows, 504 project rows, and two analysis rows for `NCBITaxon:114155`. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:114155`, `label: Dichomitus squalens`, `rank: SPECIES`, `parent_taxon: NCBITaxon:114154`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:20705`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dichomitus` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:2925`, which records 20 retained direct organisms for `NCBITaxon:114155`; this agrees with `source_attestations[1].assertion_count: 20` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:114155`. The YAML carries the single exact synonym and both related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. An exact native GOLD scan confirmed 20 exact organisms, 504 projects under those organisms, and two analysis rows. The analysis rows both point at `Gp0008772` for `Dichomitus squalens LYAD-421 SS1` through `AP PROJECT GOLD IDS`.

The exact StrainInfo side inventory has 24 direct records and 25 matching deposit designations for `NCBITaxon:114155`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dichomitus_squalens.yaml` plus `just validate-strict data/taxa/eukaryota/dichomitus_squalens.yaml`.

## Additional Notes

The bounded scan found no side-inventory `data/raw/ncbi_merged_ids.tsv` mappings into `NCBITaxon:114155`.
