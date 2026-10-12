# YAML Record Review: Entelexis geochares

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/entelexis_geochares.yaml
- Started UTC: 2026-09-23T00:10:59Z
- Finished UTC: 2026-09-23T00:10:59Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:46361` |
| Label | `Entelexis geochares` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3712600` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/entelexis_geochares.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/entelexis_apis.yaml data/taxa/eukaryota/entelexis_geochares.yaml data/taxa/eukaryota/entelexis_gropengiesseri.yaml data/taxa/eukaryota/entelexis_paramagnoliae.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project row, no native GOLD analyses, 16 NCBI type-material rows, eight exact StrainInfo direct records carrying 18 matching deposit designations, no NCBI merged-ID or exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:46361`, `label: Entelexis geochares`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3712600`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5834`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Entelexis` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36289`, which records one retained direct organism for `NCBITaxon:46361`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:46361`. The YAML preserves NCBI's exact synonyms `Candida geochares`, `Starmerella geochares`, and `Torulopsis geochares`, plus all four related synonyms filed for this row; NCBI supplies no broad synonyms or old-ID side rows.

The 16 NCBI type-material rows preserve culture-from-holotype aliases for `ATCC 36852`, `CCRC 22394`, `IFO 10278`, `JCM 9851`, and `NRRL Y-17073` under `Torulopsis geochares`, plus holotype aliases for `CBS 6870`. The native GOLD catalogs contain one exact organism row, `Go0705258` for `Starmerella geochares NRRL Y-17073`, with one matching project, `Gp0831293`, and no matching native GOLD analysis rows.

The exact StrainInfo side inventory has eight direct records carrying 18 matching deposit designations, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, three NCBI exact synonyms, four NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/entelexis_geochares.yaml` plus `just validate-strict data/taxa/eukaryota/entelexis_geochares.yaml`.

## Additional Notes

The NCBI type-material sample was expanded with an exact `NCBITaxon:46361` lookup in `data/raw/ncbi_type_material.tsv` to account for all 16 designations. The retained GOLD aggregate count matches the one current native GOLD organism row.
