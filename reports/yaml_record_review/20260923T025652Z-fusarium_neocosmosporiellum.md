# YAML Record Review: Fusarium neocosmosporiellum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_neocosmosporiellum.yaml
- Started UTC: 2026-09-23T02:56:52Z
- Finished UTC: 2026-09-23T02:56:52Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1325723` |
| Label | `Fusarium neocosmosporiellum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:232080` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_neocosmosporiellum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_mori.yaml data/taxa/eukaryota/fusarium_neocosmosporiellum.yaml data/taxa/eukaryota/fusarium_newnesense.yaml data/taxa/eukaryota/fusarium_nisikadoi.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three organism assertions, two current native GOLD organism rows with two linked projects, two native GOLD analysis rows linked by project ID, seven NCBI merged-ID side rows, 63 exact direct StrainInfo rows, 97 StrainInfo deposit rows, 12 NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1325723`, `label: Fusarium neocosmosporiellum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:232080`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:316278`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium solani species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:7935`, which records three retained direct organisms for `NCBITaxon:1325723`; this agrees with `source_attestations[1].assertion_count: 3` and its organism assertion unit. The current native GOLD catalogs contain two exact organism rows, two linked project rows, and two linked analyses.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1325723`. The YAML preserves five exact synonyms, including `Neocosmospora africana`, `Neocosmospora vasinfecta`, and both varieties of `Neocosmospora vasinfecta`, plus nine related NCBI synonyms.

The retained GOLD aggregate supplies three organism assertions. The current native GOLD catalogs still contain exact organism, project, and analysis chains for strains `NRRL 22166` and `NRRL 22436`; the one-row difference between the retained aggregate table and the current native organism catalog is side-evidence drift and does not contradict the generated assertion count.

The `data/raw/ncbi_merged_ids.tsv` side inventory has seven old IDs merged into `NCBITaxon:1325723`: `NCBITaxon:1237070`, `NCBITaxon:131367`, `NCBITaxon:231477`, `NCBITaxon:40622`, `NCBITaxon:453762`, `NCBITaxon:487226`, and `NCBITaxon:875440`. None are retained in `data/raw/ncbitaxon_taxa.tsv` for generated replacement provenance, so the YAML correctly has no generated `replaces` entry.

StrainInfo contains 63 exact direct rows and 97 exact deposit rows for the target. Those rows do not produce BacDive-derived local strain children for this taxon. NCBI has 12 type-material or epitype aliases for the target in `typematerial.dmp`: `ATCC 16238`, `ATCC:16238`, `CBS 325.54`, `CBS:325.54`, `IFO 7591`, `IFO:7591`, `ATCC 62199`, `ATCC:62199`, `NRRL 22166`, `NRRL:22166`, `BPI 910920`, and `BPI:910920`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_neocosmosporiellum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_neocosmosporiellum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_neocosmosporiellum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
