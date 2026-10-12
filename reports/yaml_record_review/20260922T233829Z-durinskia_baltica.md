# YAML Record Review: Durinskia baltica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/durinskia_baltica.yaml
- Started UTC: 2026-09-22T23:38:29Z
- Finished UTC: 2026-09-22T23:38:29Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:59809` |
| Label | `Durinskia baltica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:400754` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/durinskia_baltica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dujonia_santamariae.yaml data/taxa/eukaryota/dujonia_schatavii.yaml data/taxa/eukaryota/dujonia_zeylanoides.yaml data/taxa/eukaryota/durinskia_baltica.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact StrainInfo direct record carrying one matching deposit designation, one NCBI merged-ID side row, no exact native GOLD, NCBI type-material, or BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:59809`, `label: Durinskia baltica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:400754`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:7534`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Durinskia` genus; the bounded scan checked all nine lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39721`, which records one retained direct organism for `NCBITaxon:59809`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:59809`. The YAML carries both exact synonyms and all three related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The single row in `data/raw/ncbi_merged_ids.tsv` retires `NCBITaxon:400756` into this species ID. That old ID is not retained in `data/raw/ncbitaxon_taxa.tsv`, so omitting `replaces` is expected.

The retained GOLD aggregate row supports the generated `GOLD` source attestation. The current local native GOLD organism, project, and analysis catalogs have no exact rows for `NCBITaxon:59809`, so the generated attestation is supported by the aggregate input rather than by a row in `data/gold/organisms.jsonl.gz`.

The exact StrainInfo side inventory has one direct record and one matching `UTEX 1563` deposit designation for `NCBITaxon:59809`, but that record is not present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, three NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/durinskia_baltica.yaml` plus `just validate-strict data/taxa/eukaryota/durinskia_baltica.yaml`.

## Additional Notes

The retained GOLD aggregate reports one organism assertion for this NCBI taxon, while the current local native GOLD catalog contains no exact organism rows. The generated attestation is still supported by the maintained aggregate input that seeded the YAML.
