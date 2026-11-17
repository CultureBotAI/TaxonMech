# YAML Record Review: Geotrichum candidum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/geotrichum_candidum.yaml
- Started UTC: 2026-09-23T04:23:36Z
- Finished UTC: 2026-09-23T04:23:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1173061` |
| Label | `Geotrichum candidum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:43987` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/geotrichum_candidum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/geopyxis_carbonaria.yaml data/taxa/eukaryota/geosiphon_pyriformis.yaml data/taxa/eukaryota/geotrichum_armillariae.yaml data/taxa/eukaryota/geotrichum_candidum.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with 26 organism assertions, 22 exact current native GOLD organisms with 22 linked native GOLD projects and 19 linked native analysis rows, eight exact NCBI type-material rows, 337 exact StrainInfo records carrying 433 exact deposit rows, five NCBI merged-ID side rows but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, two exact StrainInfo related-record overlay rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1173061`, `label: Geotrichum candidum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:43987`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:260061`, which carries the same label, parent, rank, code, five exact synonyms, five related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Geotrichum`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:3719`, which records 26 retained direct organisms for `NCBITaxon:1173061`; this agrees with `source_attestations[1].assertion_count: 26` and its organism assertion unit. The current native GOLD catalogs contain 22 exact organisms, each with a linked project, and 19 native analysis rows that link to those projects through `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1173061`. The YAML preserves five exact synonyms and five related synonyms from the NCBI row.

The retained GOLD aggregate supplies 26 organism assertions. The current native GOLD catalogs have 22 exact organisms spanning strains `3C`, `UCDFST 72-186`, `CLIB 918`, `LMA-1147`, `LMA-40`, `LMA-244`, `LMA-317`, `LMA-70`, `LMA-77`, `LMA-1028`, `Y1111`, `PX1908B`, `M4009`, `M2404`, `M2401`, `M1113A`, `F2203`, `B1112B`, `B1109`, `B1101`, `CBS 178.71`, and `NRRL Y-17569`, with 22 linked projects and 19 linked analyses.

The NCBI type-material table has eight exact rows for the target: `DNA406`, `DNA:406`, `IMI 393237`, `IMI:393237`, `KFL406`, `KFL:406`, `CBS 615.84`, and `CBS:615.84`. StrainInfo has 337 exact target records and 433 exact deposits. These side rows mostly do not create generated local strain entries by themselves; two StrainInfo overlay rows for `ATCC 12784` link to an existing BacDive-derived local strain in `data/straininfo/related_records.tsv.gz`.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old IDs `NCBITaxon:1081645`, `NCBITaxon:2282360`, `NCBITaxon:324016`, `NCBITaxon:426520`, and `NCBITaxon:426521` into `NCBITaxon:1173061`, but no retained row in `data/raw/ncbitaxon_taxa.tsv` carries those old IDs with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries directly under this species.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, five exact synonyms, five related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv` or `data/straininfo/exclusions.tsv`; two exact rows in `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/geotrichum_candidum.yaml` plus `just validate-strict data/taxa/eukaryota/geotrichum_candidum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `geotrichum_candidum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. The exact StrainInfo rows for `NCBITaxon:1173061` produce two overlay rows for `kgmicrobe.strain:bacdive_24` in `data/straininfo/related_records.tsv.gz`, but do not produce `data/straininfo/assemblies.tsv` rows or generated local strain entries under this species.

The NCBI merged-ID hits for `NCBITaxon:1081645`, `NCBITaxon:2282360`, `NCBITaxon:324016`, `NCBITaxon:426520`, and `NCBITaxon:426521` are side-inventory old IDs only. Generated `replaces` values come from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`, not directly from every side row in `data/raw/ncbi_merged_ids.tsv`.
