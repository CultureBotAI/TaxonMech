# YAML Record Review: Cytospora chrysosperma

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cytospora_chrysosperma.yaml
- Started UTC: 2026-09-22T21:38:04Z
- Finished UTC: 2026-09-22T21:38:04Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:252740` |
| Label | `Cytospora chrysosperma` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:117544` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cytospora_chrysosperma.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cystostereum_murrayi.yaml data/taxa/eukaryota/cytidia_salicina.yaml data/taxa/eukaryota/cytidiella_melzeri.yaml data/taxa/eukaryota/cytospora_chrysosperma.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three retained organisms, three exact native GOLD organism/project rows joined to two exact native GOLD analysis rows, six exact NCBI type-material rows, 15 exact StrainInfo records with 15 deposit designations not retained in the final StrainInfo overlay, no exact BacDive rows, no final raw strain rows, two NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:252740`, `label: Cytospora chrysosperma`, `rank: SPECIES`, `parent_taxon: NCBITaxon:117544`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:51254`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cytospora` genus; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:22955`, which records three retained organisms for `NCBITaxon:252740`; this agrees with `source_attestations[1].assertion_count: 3`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:252740`. The YAML carries all four exact synonyms and all three related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. Exact native GOLD rows form three organism/project chains for two `Valsa sordida` strains, `CFL2056` and `YSFL`, and one `Cytospora chrysosperma` transcriptome project for `CFL2056`; two of the three projects have analysis rows linked through `AP PROJECT GOLD IDS`.

The NCBI type-material inventory contributes holotype variants of `BPI 910662` under synonym taxon name `Cytospora populicola` and epitype variants of `CBS 197.50` under synonym taxon name `Sphaeria chrysosperma`.

Fifteen exact StrainInfo records are keyed directly to `NCBITaxon:252740`, covering 15 deposit designations, but they have not been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no `STRAININFO` source attestation is generated. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cytospora_chrysosperma.yaml` plus `just validate-strict data/taxa/eukaryota/cytospora_chrysosperma.yaml`.

## Additional Notes

The bounded scan found side-inventory `data/raw/ncbi_merged_ids.tsv` mappings from `NCBITaxon:2421473` and `NCBITaxon:509221` into `NCBITaxon:252740`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
