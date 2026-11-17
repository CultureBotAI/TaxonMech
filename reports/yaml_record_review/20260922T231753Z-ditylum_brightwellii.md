# YAML Record Review: Ditylum brightwellii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/ditylum_brightwellii.yaml
- Started UTC: 2026-09-22T23:17:53Z
- Finished UTC: 2026-09-22T23:17:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:49249` |
| Label | `Ditylum brightwellii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:49248` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/ditylum_brightwellii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dissophora_decumbens.yaml data/taxa/eukaryota/dissophora_globulifera.yaml data/taxa/eukaryota/dissophora_ornata.yaml data/taxa/eukaryota/ditylum_brightwellii.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with six organism assertions, five exact native GOLD organisms linked to no projects or analyses, 16 exact StrainInfo direct records carrying 16 matching deposit designations, no exact NCBI type-material or BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:49249`, `label: Ditylum brightwellii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:49248`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:6257`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Ditylum` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37144`, which records six retained direct organisms for `NCBITaxon:49249`; this agrees with `source_attestations[1].assertion_count: 6` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:49249`. The YAML carries both exact synonyms and both related synonyms filed for this NCBI row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain five exact organisms, `Go0368643` through `Go0368647`, for `Ditylum brightwellii`; the native GOLD project and analysis tables have no exact linked rows for those organism IDs.

The exact StrainInfo side inventory has 16 direct records and 16 matching deposit designations for `NCBITaxon:49249`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, two NCBI exact synonyms, two NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/ditylum_brightwellii.yaml` plus `just validate-strict data/taxa/eukaryota/ditylum_brightwellii.yaml`.

## Additional Notes

The retained GOLD aggregate reports six organism assertions for this NCBI taxon, while the current local native GOLD catalog contains five exact organism rows. The generated attestation is still supported by the maintained aggregate input that seeded the YAML.
