# YAML Record Review: Cystobasidium psychroaquaticum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cystobasidium_psychroaquaticum.yaml
- Started UTC: 2026-09-22T21:28:25Z
- Finished UTC: 2026-09-22T21:28:25Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1583029` |
| Label | `Cystobasidium psychroaquaticum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:203525` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cystobasidium_psychroaquaticum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cystobasidium_psychroaquaticum.yaml data/taxa/eukaryota/cystobasidium_ritchiei.yaml data/taxa/eukaryota/cystobasidium_slooffiae.yaml data/taxa/eukaryota/cystobasidium_sp_2nf920.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with five retained organisms, five exact native GOLD organism rows with no exact project or analysis rows, ten exact NCBI type-material rows, one StrainInfo deposit hit but no direct exact StrainInfo row, no exact BacDive rows, no final raw strain rows, two NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1583029`, `label: Cystobasidium psychroaquaticum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:203525`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:408461`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cystobasidium` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:12791`, which records five retained organisms for `NCBITaxon:1583029`; this agrees with `source_attestations[1].assertion_count: 5`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1583029`. The YAML carries all three related synonyms filed for this row, including `Rhodotorula sp. CBS 11769` and `Rhodotorula sp. D88R`; NCBI supplies no exact or broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. Exact native GOLD organism rows are keyed to `VKPM Y-3653`, `MUCL 52875`, `K-833`, `DSM 27713`, and `CBS 11769`; none currently join to exact native GOLD project or analysis rows.

The NCBI type-material inventory contributes ten exact rows for culture-from-holotype variants of `CBS 11769`, `KBP 3881`, and `VKPM Y-3653`, holotype variants of `K-833`, and isotype variants of `DSM 27713`.

A StrainInfo deposit hit for `DSM 27713` is associated with this target, but no direct exact StrainInfo row is keyed to `NCBITaxon:1583029`; nothing has been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`, and no `STRAININFO` source attestation is generated. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cystobasidium_psychroaquaticum.yaml` plus `just validate-strict data/taxa/eukaryota/cystobasidium_psychroaquaticum.yaml`.

## Additional Notes

The bounded scan found side-inventory `data/raw/ncbi_merged_ids.tsv` mappings from `NCBITaxon:1094161` and `NCBITaxon:766785` into `NCBITaxon:1583029`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
