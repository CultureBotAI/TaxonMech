# YAML Record Review: Fusarium sporotrichioides

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_sporotrichioides.yaml
- Started UTC: 2026-09-23T03:44:34Z
- Finished UTC: 2026-09-23T03:44:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5514` |
| Label | `Fusarium sporotrichioides` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:569360` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_sporotrichioides.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/fusarium_sporotrichioides.yaml data/taxa/eukaryota/fusarium_stilboides.yaml data/taxa/eukaryota/fusarium_subglutinans.yaml data/taxa/eukaryota/fusarium_sublunatum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two organism assertions, three current native GOLD organism rows with five linked projects and one native analysis row, 59 exact StrainInfo records carrying 67 exact deposit rows, one NCBI merged-ID side row but no retained retired old IDs, no NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5514`, `label: Fusarium sporotrichioides`, `rank: SPECIES`, `parent_taxon: NCBITaxon:569360`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2448`, which carries the same label, parent, rank, code, exact synonyms, related synonym, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium sambucinum species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38554`, which records two retained direct organisms for `NCBITaxon:5514`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain three exact organisms, five linked projects, and one analysis linked to those exact organism projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5514`. The YAML preserves both exact synonyms and the related synonym from the NCBI row.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs contain three exact organisms, including strain `7-200`, strain `NRRL 3299`, and one unstrained `Fusarium sporotrichioides` row; exact native GOLD joins found five linked projects and one project-linked analysis.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old ID `NCBITaxon:2203386` into `NCBITaxon:5514`, but no retained row in `data/raw/ncbitaxon_taxa.tsv` carries that old ID with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact NCBI type-material, exact BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

StrainInfo has 59 exact target records and 67 exact deposits. These side rows do not create generated child strains by themselves.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, two exact synonyms, one related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_sporotrichioides.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_sporotrichioides.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_sporotrichioides` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv` and can differ from the current native GOLD exact rows. Native GOLD organism, project, and analysis rows are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:5514` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
