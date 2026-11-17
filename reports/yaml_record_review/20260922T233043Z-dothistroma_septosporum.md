# YAML Record Review: Dothistroma septosporum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dothistroma_septosporum.yaml
- Started UTC: 2026-09-22T23:30:43Z
- Finished UTC: 2026-09-22T23:30:43Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:64363` |
| Label | `Dothistroma septosporum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:242508` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dothistroma_septosporum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dothiorella_sarmentorum.yaml data/taxa/eukaryota/dothistroma_septosporum.yaml data/taxa/eukaryota/drechmeria_coniospora.yaml data/taxa/eukaryota/drechslerella_stenobrocha.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, the retained GOLD aggregate row, 20 exact native GOLD organisms, 22 native GOLD projects, 20 native GOLD analyses, eight exact StrainInfo direct records carrying eight matching deposit designations, one NCBI merged-ID side row, no NCBI type-material rows, no lineage mismatches, no BacDive rows, and no final raw strain rows. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:64363`, `label: Dothistroma septosporum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:242508`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:8155`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dothistroma` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40252`, which records 19 retained direct organisms for `NCBITaxon:64363`; this agrees with `source_attestations[1].assertion_count: 19` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:64363`. The YAML carries all three exact synonyms and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The single row in `data/raw/ncbi_merged_ids.tsv` retires `NCBITaxon:317917` into this species ID. That old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`, so omitting `replaces` is expected.

The native GOLD catalogs currently contain 20 exact organism rows for `NCBITaxon:64363`, 22 projects joined through those organism IDs, and 20 analyses joined through the native project IDs. The project rows include `Gp0017021` for `Dothistroma septosporum NZE10`, `Gp0039755` for the unstrained `Dothistroma septosporum` organism, 18 rows for the `Go0384355`-`Go0384372` CMW/NZFS/MU_NZE8 organism block, and two additional `Go0009597` EST projects.

The exact StrainInfo side inventory has eight direct records and eight matching deposit designations for `NCBITaxon:64363`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, three NCBI exact synonyms, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dothistroma_septosporum.yaml` plus `just validate-strict data/taxa/eukaryota/dothistroma_septosporum.yaml`.

## Additional Notes

The retained GOLD aggregate count of 19 differs from the 20 current exact rows in the local native GOLD organism catalog. The generated YAML follows the retained aggregate input that seeded the record.
