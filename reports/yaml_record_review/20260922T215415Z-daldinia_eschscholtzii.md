# YAML Record Review: Daldinia eschscholtzii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/daldinia_eschscholtzii.yaml
- Started UTC: 2026-09-22T21:54:15Z
- Finished UTC: 2026-09-22T21:54:15Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:292717` |
| Label | `Daldinia eschscholtzii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:42360` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/daldinia_eschscholtzii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/daldinia_bambusicola.yaml data/taxa/eukaryota/daldinia_caldariorum.yaml data/taxa/eukaryota/daldinia_decipiens.yaml data/taxa/eukaryota/daldinia_eschscholtzii.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with three retained organisms, 3 exact native GOLD organisms linked to 10 projects and one analysis, no exact NCBI type-material rows, no exact StrainInfo records, no exact BacDive rows, no final raw strain rows, one NCBI merged-ID side row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:292717`, `label: Daldinia eschscholtzii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:42360`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:59680`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Daldinia` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:28798`, which records three retained organisms for `NCBITaxon:292717`; this agrees with `source_attestations[1].assertion_count: 3`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:292717`. The YAML carries both exact synonyms and both related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The exact native GOLD chain contains organisms `Go0039250`, `Go0107307`, and `Go0510331`; projects `Gp0039250`, `Gp0107307`, `Gp0230450`, `Gp0230451`, `Gp0230452`, `Gp0230453`, `Gp0230454`, `Gp0230455`, `Gp0396289`, and `Gp0396290`; and an analysis row named `Daldinia eschscholtzii UM 1400` that links back through `AP PROJECT GOLD IDS`.

The local NCBI type-material inventory has no exact rows for this taxon ID.

The bounded scan found no exact StrainInfo records, no exact BacDive rows, and no maintained final strain-table rows, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/daldinia_eschscholtzii.yaml` plus `just validate-strict data/taxa/eukaryota/daldinia_eschscholtzii.yaml`.

## Additional Notes

The bounded scan found a side-inventory `data/raw/ncbi_merged_ids.tsv` mapping from `NCBITaxon:1180959` into `NCBITaxon:292717`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` would generate a `replaces` entry.
