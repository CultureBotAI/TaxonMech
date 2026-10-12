# YAML Record Review: Fusarium proliferatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_proliferatum.yaml
- Started UTC: 2026-09-23T03:33:17Z
- Finished UTC: 2026-09-23T03:33:17Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:948311` |
| Label | `Fusarium proliferatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:171627` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_proliferatum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_piperis.yaml data/taxa/eukaryota/fusarium_poae.yaml data/taxa/eukaryota/fusarium_praegraminearum.yaml data/taxa/eukaryota/fusarium_proliferatum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 11 organism assertions, 12 current native GOLD organism rows with 15 linked projects and eight native analysis rows, eight exact NCBI type-material rows, 94 exact StrainInfo records carrying 153 exact deposit rows, three NCBI merged-ID side rows but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:948311`, `label: Fusarium proliferatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:171627`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:203736`, which carries the same label, parent, rank, code, exact synonyms, related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium fujikuroi species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:45051`, which records 11 retained direct organisms for `NCBITaxon:948311`; this agrees with `source_attestations[1].assertion_count: 11` and its organism assertion unit. The current native GOLD catalogs contain 12 exact organisms, 15 linked projects, and eight analyses linked to those exact organism projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:948311`. The YAML preserves all three exact synonyms and all three related synonyms from the NCBI row.

The retained GOLD aggregate supplies 11 organism assertions and intentionally does not gather descendant taxa. The current native GOLD catalogs contain 12 exact organisms, with organism strains `ITEM 2287`, `LF061`, `NRRL62905`, `ET1`, `Fol3`, `Fp_A8`, `312A_c15_2`, `KF3377`, `R16`, `MPVP 328`, `ITEM 2341`, and one unstrained `Fusarium proliferatum` row. Exact native GOLD joins found 15 linked projects and eight project-linked analyses.

The NCBI type-material table has eight exact epitype rows for the target, covering normalized variants of `CBS 480.96` and normalized variants of `NRRL 26427`. StrainInfo has 94 exact target records and 153 exact deposits. These side rows do not create generated child strains by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old IDs `NCBITaxon:165209`, `NCBITaxon:224913`, and `NCBITaxon:42674` into `NCBITaxon:948311`, but no retained rows in `data/raw/ncbitaxon_taxa.tsv` carry those old IDs with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, three exact synonyms, three related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_proliferatum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_proliferatum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_proliferatum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv` and can differ from the current native GOLD exact rows. Native GOLD organism, project, and analysis rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:948311` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
