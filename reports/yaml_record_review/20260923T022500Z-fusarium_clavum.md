# YAML Record Review: Fusarium clavum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_clavum.yaml
- Started UTC: 2026-09-23T02:25:00Z
- Finished UTC: 2026-09-23T02:25:00Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2594811` |
| Label | `Fusarium clavum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:450425` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_clavum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_camptoceras.yaml data/taxa/eukaryota/fusarium_cicatricum.yaml data/taxa/eukaryota/fusarium_circinatum.yaml data/taxa/eukaryota/fusarium_clavum.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one current native GOLD organism row with one linked project, one native GOLD analysis row linked by project ID, thirteen NCBI merged-ID side rows, one exact direct StrainInfo row, one StrainInfo deposit row, four NCBI holotype-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2594811`, `label: Fusarium clavum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:450425`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:535037`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium incarnatum-equiseti species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:23815`, which records one retained direct organism for `NCBITaxon:2594811`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2594811`. The YAML preserves four exact synonyms and seventeen related synonyms from NCBI, spanning the `Fusarium clavum` combination, CS3069/FIESC 5 names, and several provisional NRRL names.

The `data/raw/ncbi_merged_ids.tsv` side inventory has thirteen old IDs merged into `NCBITaxon:2594811`: `NCBITaxon:1318460`, `NCBITaxon:1385656`, `NCBITaxon:2506211`, `NCBITaxon:2518147`, `NCBITaxon:453789`, `NCBITaxon:453792`, `NCBITaxon:679418`, `NCBITaxon:679419`, `NCBITaxon:679420`, `NCBITaxon:679421`, `NCBITaxon:679422`, `NCBITaxon:679423`, and `NCBITaxon:875417`. None are retained in `data/raw/ncbitaxon_taxa.tsv` for generated replacement provenance, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies one organism assertion; the current native GOLD catalogs still contain one exact organism row, one linked project row, and one linked analysis row for the target NCBI taxon.

StrainInfo contains one exact direct row and one exact deposit row for the target. Those rows do not produce BacDive-derived local strain children for this taxon. NCBI has four holotype aliases for the target in `typematerial.dmp`: `CBS 126202`, `CBS:126202`, `CBS H-24054`, and `CBS:H-24054`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI related and exact synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_clavum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_clavum.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
