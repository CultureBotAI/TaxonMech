# YAML Record Review: Ganoderma boninense

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/ganoderma_boninense.yaml
- Started UTC: 2026-09-23T04:10:00Z
- Finished UTC: 2026-09-23T04:10:00Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:34458` |
| Label | `Ganoderma boninense` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5314` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/ganoderma_boninense.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/ganoderma_boninense.yaml data/taxa/eukaryota/ganoderma_leucocontextum.yaml data/taxa/eukaryota/ganoderma_lucidum.yaml data/taxa/eukaryota/ganoderma_multipileum_bcrc_37180.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with two organism assertions, one exact current native GOLD organism with one linked native GOLD project and one linked native analysis row, six exact StrainInfo records carrying 12 exact deposit rows, no exact NCBI type-material, BacDive, or NCBI merged-ID rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:34458`, `label: Ganoderma boninense`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5314`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:3865`, which carries the same label, parent, rank, code, one related synonym, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Ganoderma`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:32873`, which records two retained direct organisms for `NCBITaxon:34458`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit. The current native GOLD catalogs contain one exact organism, `Go0384519` for strain `NJ3`, with one linked project, `Gp0235626`, and one analysis row linked through `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:34458`. The YAML preserves the related synonym from the NCBI row and correctly has no exact-synonym entries because the exact-synonym field is empty upstream.

The retained GOLD aggregate supplies two organism assertions. The current native GOLD catalogs have the exact organism `Ganoderma boninense NJ3`, one matching project, and one native GOLD analysis for `Ganoderma boninense NJ3`.

The NCBI type-material table has no exact rows for the target. StrainInfo has six exact target records and 12 exact deposits. These side rows do not create generated local strain entries by themselves.

No side `data/raw/ncbi_merged_ids.tsv` row maps an old ID into `NCBITaxon:34458`, and no retained row in `data/raw/ncbitaxon_taxa.tsv` carries a retired ID for this target, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, one related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/ganoderma_boninense.yaml` plus `just validate-strict data/taxa/eukaryota/ganoderma_boninense.yaml`.

## Additional Notes

No prior exact ignored review report existed for `ganoderma_boninense` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:34458` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
