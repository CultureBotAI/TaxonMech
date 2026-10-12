# YAML Record Review: Hortaea werneckii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hortaea_werneckii.yaml
- Started UTC: 2026-09-23T07:07:47Z
- Finished UTC: 2026-09-23T07:07:47Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:91943` |
| Label | `Hortaea werneckii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:91942` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hortaea_werneckii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hortaea_werneckii.yaml data/taxa/eukaryota/hortiboletus_rubellus.yaml data/taxa/eukaryota/huiozyma_naganishii_cbs_8797.yaml data/taxa/eukaryota/huiozyma_sinensis.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with 11 organism assertions, 11 exact current native GOLD organisms with 11 linked native GOLD projects and 11 linked native GOLD analyses, 20 exact NCBI type-material rows, 10 side NCBI merged-ID rows, 49 direct exact StrainInfo rows with 62 deposit rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:91943`, `label: Hortaea werneckii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:91942`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:14873`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hortaea`; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:44491`, which records 11 retained direct organisms for `NCBITaxon:91943`; this agrees with `source_attestations[1].assertion_count: 11` and its organism assertion unit. Exact native GOLD enumeration also found 11 current organisms, 11 linked projects, and 11 linked analyses for the same NCBI ID.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:91943`. `Cladosporium werneckii` and `Exophiala werneckii` are present in `data/raw/ncbitaxon_taxa.tsv:14873` as exact synonyms, and all 13 generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies 11 organism assertions. The current native GOLD catalogs have exact organisms `Go0631650` through `Go0631660`, linked projects `Gp0645190` through `Gp0645200`, and 11 native analyses linked by those exact project IDs for `EXF-562`, `EXF-120`, `EXF-2788`, `EXF-151`, `EXF-2682`, `EXF-171`, `EXF-10513`, `EXF-6669`, `EXF-6654`, `EXF-6651`, and `EXF-6656`.

NCBI carries 20 exact culture-from-type-material aliases for `Cladosporium werneckii` at `data/raw/ncbi_type_material.tsv:273060` through `data/raw/ncbi_type_material.tsv:273079`, spanning ATCC 36317, CBS 107.67, CDC B1432, EXF 151, and NCMH 75 spelling variants. These aliases do not contradict the generated `strain_count: 0` because no exact BacDive, StrainInfo assembly, or maintained final strain rows are linked to `NCBITaxon:91943`.

NCBI merged-ID side data maps 10 retired IDs, `NCBITaxon:661567` through `NCBITaxon:661576`, into `NCBITaxon:91943`, but no retained retired source rows exist for those old IDs in `data/raw/ncbitaxon_taxa.tsv`, so the absence of generated `replaces` values is consistent with the generator inputs.

StrainInfo has 49 direct exact rows with 62 deposit rows for this taxon, but that side inventory is not joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or a maintained final strain table for this generated record.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hortaea_werneckii.yaml` plus `just validate-strict data/taxa/eukaryota/hortaea_werneckii.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hortaea_werneckii` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
