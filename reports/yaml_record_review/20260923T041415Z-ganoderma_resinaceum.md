# YAML Record Review: Ganoderma resinaceum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/ganoderma_resinaceum.yaml
- Started UTC: 2026-09-23T04:14:15Z
- Finished UTC: 2026-09-23T04:14:15Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:34465` |
| Label | `Ganoderma resinaceum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5314` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/ganoderma_resinaceum.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/ganoderma_resinaceum.yaml data/taxa/eukaryota/gautieria_morchelliformis.yaml data/taxa/eukaryota/geastrum_triplex.yaml data/taxa/eukaryota/gelasinospora_brevispora.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, no exact current native GOLD organism, project, or analysis rows, no exact NCBI type-material rows, 29 exact StrainInfo records carrying 43 exact deposit rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:34465`, `label: Ganoderma resinaceum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5314`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:3866`, which carries the same label, parent, rank, code, one related synonym, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Ganoderma`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:32880`, which records one retained direct organism for `NCBITaxon:34465`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs have no exact organism, project, or analysis row for this NCBI ID in this checkout.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:34465`. The YAML preserves the related synonym `Ganoderma resinaceum Boud., 1889` from the NCBI row.

The retained GOLD aggregate supplies one organism assertion, but that aggregate has no current exact native GOLD organism counterpart for `NCBITaxon:34465` in the native organism, project, or analysis snapshots scanned in this checkout.

StrainInfo has 29 exact target records and 43 exact deposits. These side rows do not create generated local strain entries by themselves.

No side `data/raw/ncbi_merged_ids.tsv` row, exact NCBI type-material row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, one related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/ganoderma_resinaceum.yaml` plus `just validate-strict data/taxa/eukaryota/ganoderma_resinaceum.yaml`.

## Additional Notes

No prior exact ignored review report existed for `ganoderma_resinaceum` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:34465` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.
