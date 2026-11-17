# YAML Record Review: Daia tannicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/daia_tannicola.yaml
- Started UTC: 2026-09-22T21:52:00Z
- Finished UTC: 2026-09-22T21:52:00Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:45514` |
| Label | `Daia tannicola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3712545` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/daia_tannicola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dactylonectria_torresensis.yaml data/taxa/eukaryota/daedaleopsis_nitida.yaml data/taxa/eukaryota/daia_ofunaensis.yaml data/taxa/eukaryota/daia_tannicola.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism/project chain with no exact native GOLD analysis rows, 9 exact NCBI type-material rows, 3 exact StrainInfo direct records carrying 22 matching deposit designations that were not retained in the final StrainInfo overlay, no exact BacDive rows, no final raw strain rows, one NCBI merged-ID side row, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:45514`, `label: Daia tannicola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3712545`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5582`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Daia` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36026`, which records one retained organism for `NCBITaxon:45514`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:45514`. The YAML carries all three exact synonyms and all three related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The exact native GOLD chain contains organism `Go0705287` and project `Gp0831322`; the local native GOLD analysis export has no exact row that links through that project.

The NCBI type-material inventory contributes nine exact rows under the synonym taxon name `Pichia tannicola`, covering culture-from-holotype variants of `NRRL Y-17392` and holotype variants of `CBS 6065`.

Three exact StrainInfo direct records are keyed to `NCBITaxon:45514` and together carry 22 matching deposit designations, but none have been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no `STRAININFO` source attestation is generated. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/daia_tannicola.yaml` plus `just validate-strict data/taxa/eukaryota/daia_tannicola.yaml`.

## Additional Notes

The bounded scan found a side-inventory `data/raw/ncbi_merged_ids.tsv` mapping from `NCBITaxon:45499` into `NCBITaxon:45514`, but no retained retired row in `data/raw/ncbitaxon_taxa.tsv` would generate a `replaces` entry.
