# YAML Record Review: Extremus antarcticus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/extremus_antarcticus.yaml
- Started UTC: 2026-09-23T01:22:18Z
- Finished UTC: 2026-09-23T01:22:18Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:702011` |
| Label | `Extremus antarcticus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1670431` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/extremus_antarcticus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/exophiala_xenobiotica.yaml data/taxa/eukaryota/exserohilum_turcicum.yaml data/taxa/eukaryota/extremus_antarcticus.yaml data/taxa/eukaryota/extremus_sp.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with four organism assertions, one current native GOLD organism with two linked projects, four NCBI merged-ID side rows, four NCBI type-material rows, no current exact native GOLD analyses, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:702011`, `label: Extremus antarcticus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1670431`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:164847`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Extremus` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:41639`, which records four retained direct organisms for `NCBITaxon:702011`; this agrees with `source_attestations[1].assertion_count: 4` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:702011`. The YAML preserves NCBI's exact synonym `Devriesia antarctica` plus seven related synonyms.

`data/raw/ncbi_merged_ids.tsv:18239`, `data/raw/ncbi_merged_ids.tsv:18240`, `data/raw/ncbi_merged_ids.tsv:18241`, and `data/raw/ncbi_merged_ids.tsv:18256` map four old side-inventory IDs to `NCBITaxon:702011`; none are retained as rows with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies four organism assertions; the current native GOLD catalogs contain one exact organism row and two linked project rows for the target NCBI taxon.

NCBI type-material rows 258798-258801 list four holotype or isotype designations for `Extremus antarcticus`. No exact StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI exact synonym, seven NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/extremus_antarcticus.yaml` plus `just validate-strict data/taxa/eukaryota/extremus_antarcticus.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD exact row count is lower than the retained aggregate count but remains side evidence only. The NCBI merged-ID rows are side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
