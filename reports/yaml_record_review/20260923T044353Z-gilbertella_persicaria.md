# YAML Record Review: Gilbertella persicaria

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gilbertella_persicaria.yaml
- Started UTC: 2026-09-23T04:43:53Z
- Finished UTC: 2026-09-23T04:43:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:101096` |
| Label | `Gilbertella persicaria` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:101095` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gilbertella_persicaria.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/gigaspora_margarita.yaml data/taxa/eukaryota/gigaspora_rosea.yaml data/taxa/eukaryota/gilbertella_persicaria.yaml data/taxa/eukaryota/gilbertella_persicaria_var_indica.yaml` | Passed; the strict batch scanned 4 files with 0 error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with five organism assertions, five exact current native GOLD organisms with six linked native GOLD projects, no linked native analyses, 11 exact NCBI type-material rows, 26 exact StrainInfo rows, 40 exact StrainInfo deposit rows, one side NCBI merged-ID row, no retained retired NCBI rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:101096`, `label: Gilbertella persicaria`, `rank: SPECIES`, `parent_taxon: NCBITaxon:101095`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:17416`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Gilbertella`; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:242`, which records five retained direct organisms for `NCBITaxon:101096`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit. The current native GOLD catalogs contain exact organisms `Go0302618`, `Go0470756`, `Go0470783`, `Go0470784`, and `Go0470845`, with six exact linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:101096`. `Choanephora persicaria` is present in `data/raw/ncbitaxon_taxa.tsv:17416` as an exact synonym, and `Choanephora persicaria E.D. Eddy, 1925`, `Gilbertella persicaria (E.D. Eddy) Hesselt., 1960`, and `Gilbertella sp. CBS 403.51` are present as related synonyms.

The retained GOLD aggregate supplies five organism assertions. The current native GOLD catalogs have exact organism rows for `CBS 190.32`, `CBS 442.64-`, `CBS 246.59+`, `CBS 190.32-`, and `NRRL A-13613`; those rows link to six projects, including the second `Go0302618` transcriptome project that was outside the bounded project sample.

NCBI type material rows list `CBS 190.32`, `ATCC 24413`, `IMI 101697`, `NRRL 2700`, and `VKM F-1042` plus colonized variants under `NCBITaxon:101096`. Exact StrainInfo rows are present as side inventory rows, but there are no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; StrainInfo only overlays BacDive-derived local strains, and this taxon has no generated local strain rows.

The side `data/raw/ncbi_merged_ids.tsv` inventory has one old ID, `NCBITaxon:1195487`, merged into `NCBITaxon:101096`, but the retained retired NCBI table contributes no old ID rows for this target. Omitting `replaces` is therefore consistent with the generated source state.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gilbertella_persicaria.yaml` plus `just validate-strict data/taxa/eukaryota/gilbertella_persicaria.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gilbertella_persicaria` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or organism GOLD ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
