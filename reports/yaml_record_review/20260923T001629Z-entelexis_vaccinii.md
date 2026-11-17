# YAML Record Review: Entelexis vaccinii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/entelexis_vaccinii.yaml
- Started UTC: 2026-09-23T00:16:29Z
- Finished UTC: 2026-09-23T00:16:29Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:45600` |
| Label | `Entelexis vaccinii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3712600` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/entelexis_vaccinii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/entelexis_vaccinii.yaml data/taxa/eukaryota/enterospora_canceri.yaml data/taxa/eukaryota/entodinium_caudatum.yaml data/taxa/eukaryota/entoleuca_mammata.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project row, no native GOLD analyses, 22 NCBI type-material rows, one exact StrainInfo row with 10 deposits, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:45600`, `label: Entelexis vaccinii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3712600`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5635`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Entelexis` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36091`, which records one retained direct organism for `NCBITaxon:45600`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:45600`. The YAML preserves NCBI's exact synonyms `Candida vaccinii` and `Starmerella vaccinii`, plus all three related synonyms filed for this row; NCBI supplies no broad synonyms or old-ID side rows.

The 22 NCBI type-material rows preserve culture-from-holotype aliases for `BCRC 22417`, `CCRC 22417`, `IAM 13117`, `JCM 9446`, and `NRRL Y-17684` under `Candida vaccinii`, plus holotype aliases for `CBS 7318`. The native GOLD catalogs contain one exact organism row, `Go0704942` for `Starmerella vaccinii NRRL Y-17684`, with one matching project, `Gp0830957`, and no matching native GOLD analysis rows.

StrainInfo contains one exact target row, `siID 65831`, with 10 deposit designations for `Candida vaccinii`; those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, three NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/entelexis_vaccinii.yaml` plus `just validate-strict data/taxa/eukaryota/entelexis_vaccinii.yaml`.

## Additional Notes

The NCBI type-material sample was expanded with an exact `NCBITaxon:45600` lookup in `data/raw/ncbi_type_material.tsv` to account for all 22 designations. The retained GOLD aggregate count matches the one current native GOLD organism row.
