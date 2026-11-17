# YAML Record Review: Dryadomyces sulphureus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dryadomyces_sulphureus.yaml
- Started UTC: 2026-09-22T23:36:08Z
- Finished UTC: 2026-09-22T23:36:08Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:490887` |
| Label | `Dryadomyces sulphureus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:308908` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dryadomyces_sulphureus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dryadomyces_sulphureus.yaml data/taxa/eukaryota/dujonia_boleticola.yaml data/taxa/eukaryota/dujonia_oleophila.yaml data/taxa/eukaryota/dujonia_railenensis.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with six organism assertions, six exact native GOLD organisms, one native GOLD project and analysis, eight NCBI type-material rows, one exact StrainInfo direct record carrying two matching deposit designations, two NCBI merged-ID side rows, no BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:490887`, `label: Dryadomyces sulphureus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:308908`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:110655`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dryadomyces` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37092`, which records six retained direct organisms for `NCBITaxon:490887`; this agrees with `source_attestations[1].assertion_count: 6` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:490887`. The YAML carries both exact synonyms and all four related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The two rows in `data/raw/ncbi_merged_ids.tsv` retire `NCBITaxon:268495` and `NCBITaxon:44382` into this species ID, but neither old ID is retained in `data/raw/ncbitaxon_taxa.tsv`, so omitting `replaces` is expected.

The eight NCBI type-material rows preserve `ATCC 18095`, `CBS 380.68`, `DSM 1501`, and `MUCL 14524` plus colon-delimited spellings as type material for `Ambrosiella sulphurea`. The exact StrainInfo side inventory has one direct record, carrying `ATCC 18095` and `DSM 1501` type-strain deposit designations, but no rows are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`.

The native GOLD catalogs contain six exact organism rows: `Go0448975` for `Raffaelea sulphurea CBS 380.68`, plus `Go0600550`-`Go0600554` for five `Ambrosiella sulphurea` strains. Only `Go0448975` joins to a native project and analysis in the local GOLD catalogs. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, four NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dryadomyces_sulphureus.yaml` plus `just validate-strict data/taxa/eukaryota/dryadomyces_sulphureus.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the six current native GOLD organism rows. The native GOLD rows use `Ambrosiella` and `Raffaelea` spellings that NCBI records as synonyms of the current `Dryadomyces sulphureus` name.
