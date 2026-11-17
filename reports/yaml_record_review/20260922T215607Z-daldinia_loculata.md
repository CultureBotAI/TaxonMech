# YAML Record Review: Daldinia loculata

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/daldinia_loculata.yaml
- Started UTC: 2026-09-22T21:56:07Z
- Finished UTC: 2026-09-22T21:56:07Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:103429` |
| Label | `Daldinia loculata` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:42360` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/daldinia_loculata.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/daldinia_grandis.yaml data/taxa/eukaryota/daldinia_loculata.yaml data/taxa/eukaryota/daldinia_loculatoides.yaml data/taxa/eukaryota/daldinia_vernicosa.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, two exact native GOLD organisms linked to four projects and no analyses, 2 exact NCBI type-material rows, 5 exact StrainInfo direct records carrying 5 matching deposit designations that were not retained in the final StrainInfo overlay, no exact BacDive rows, no final raw strain rows, 11 NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:103429`, `label: Daldinia loculata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:42360`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:18466`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Daldinia` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:463`, which records two retained organisms for `NCBITaxon:103429`; this agrees with `source_attestations[1].assertion_count: 2`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:103429`. The YAML carries the one exact synonym and all 13 related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The exact native GOLD chain contains organisms `Go0498772` and `Go0498774` and projects `Gp0383004`, `Gp0383005`, `Gp0383006`, and `Gp0383008`; the local native GOLD analysis export has no exact row that links through those projects.

The NCBI type-material inventory contributes two exact rows under the synonym taxon name `Sphaeria loculata`, covering `BCRC 34117` and `BCRC:34117` as paratype designations.

Five exact StrainInfo direct records are keyed to `NCBITaxon:103429` and together carry five matching deposit designations, including `CBS 113971` for a retained native GOLD strain, but none have been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no `STRAININFO` source attestation is generated. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/daldinia_loculata.yaml` plus `just validate-strict data/taxa/eukaryota/daldinia_loculata.yaml`.

## Additional Notes

The bounded scan found side-inventory `data/raw/ncbi_merged_ids.tsv` mappings from `NCBITaxon:1180824`, `NCBITaxon:1180826`, `NCBITaxon:1180835`, `NCBITaxon:1180858`, `NCBITaxon:1180929`, `NCBITaxon:1180947`, `NCBITaxon:1180949`, `NCBITaxon:1180994`, `NCBITaxon:1181073`, `NCBITaxon:1181134`, and `NCBITaxon:757968` into `NCBITaxon:103429`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
