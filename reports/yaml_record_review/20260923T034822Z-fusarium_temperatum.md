# YAML Record Review: Fusarium temperatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_temperatum.yaml
- Started UTC: 2026-09-23T03:48:22Z
- Finished UTC: 2026-09-23T03:48:22Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:767483` |
| Label | `Fusarium temperatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:171627` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_temperatum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_sulawesiense.yaml data/taxa/eukaryota/fusarium_tanahbumbuense.yaml data/taxa/eukaryota/fusarium_temperatum.yaml data/taxa/eukaryota/fusarium_tenuicristatum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and one linked native analysis row, eight exact NCBI type-material rows, 37 exact StrainInfo records carrying 37 exact deposit rows, one NCBI merged-ID side row but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:767483`, `label: Fusarium temperatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:171627`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:178504`, which carries the same label, parent, rank, code, two related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium fujikuroi species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:42589`, which records one retained direct organism for `NCBITaxon:767483`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism, `Go0093049` for strain `CMWF389`, with one linked project, `Gp0093049`, and one analysis row linked through `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:767483`. The YAML preserves related synonyms `Fusarium sp. JS-2010` and `Fusarium sp. MW-2020k` from the NCBI row and correctly has no exact-synonym entries because the exact-synonym field is empty upstream.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have the exact organism `Fusarium temperatum CMWF389`, one matching project, and one native GOLD analysis for `Fusarium temperatum CMWF389`.

The NCBI type-material table has eight exact rows for the target, covering `MUCL 52463`, `MUCL:52463`, `MUCL 53011-H`, `MUCL:53011-H`, `MUCL 52463-H`, `MUCL:52463-H`, `MUCL 52438`, and `MUCL:52438`. StrainInfo has 37 exact target records and 37 exact deposits. These side rows do not create generated child strains by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old ID `NCBITaxon:2773089` into `NCBITaxon:767483`, but no retained row in `data/raw/ncbitaxon_taxa.tsv` carries that old ID with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, two related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_temperatum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_temperatum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_temperatum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:767483` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
