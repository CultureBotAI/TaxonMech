# YAML Record Review: Fusarium caatingaense

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_caatingaense.yaml
- Started UTC: 2026-09-23T02:21:39Z
- Finished UTC: 2026-09-23T02:21:39Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2562764` |
| Label | `Fusarium caatingaense` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:450425` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_caatingaense.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_buharicum.yaml data/taxa/eukaryota/fusarium_bulbicola.yaml data/taxa/eukaryota/fusarium_burgessii.yaml data/taxa/eukaryota/fusarium_caatingaense.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one current native GOLD organism row with one linked project, one native GOLD analysis row linked by project ID, six NCBI merged-ID side rows, six NCBI type-material rows, no StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2562764`, `label: Fusarium caatingaense`, `rank: SPECIES`, `parent_taxon: NCBITaxon:450425`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:530462`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium incarnatum-equiseti species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:23290`, which records one retained direct organism for `NCBITaxon:2562764`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2562764`. The YAML preserves all eight NCBI related synonyms, including `Fusarium caatingaense A.C.S. Santos, C.S. Lima, P.V. Tiago & N.T. Oliveira, 2019` and the `Fusarium sp. FIESC`/`Fusarium sp. NRRL 34003` provisional names.

The `data/raw/ncbi_merged_ids.tsv` side inventory has six old IDs merged into `NCBITaxon:2562764`: `NCBITaxon:1353780`, `NCBITaxon:2219976`, `NCBITaxon:2544926`, `NCBITaxon:2736615`, `NCBITaxon:679400`, and `NCBITaxon:875410`. None are retained in `data/raw/ncbitaxon_taxa.tsv` for generated replacement provenance, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies one organism assertion; the current native GOLD catalogs still contain one exact organism row, one linked project row, and one linked analysis row for the target NCBI taxon.

No exact StrainInfo or BacDive rows are present for the target. NCBI has six type-material aliases for the target in `typematerial.dmp`: `MUM 1859`, `MUM:1859`, `URM<BRA> 6779`, `URM<BRA>:6779`, `URM<BRA> 91192`, and `URM<BRA>:91192`. No maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, eight NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact direct SI-ID or deposit rows; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_caatingaense.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_caatingaense.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
