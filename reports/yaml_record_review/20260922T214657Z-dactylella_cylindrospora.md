# YAML Record Review: Dactylella cylindrospora

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dactylella_cylindrospora.yaml
- Started UTC: 2026-09-22T21:46:57Z
- Finished UTC: 2026-09-22T21:46:57Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1814901` |
| Label | `Dactylella cylindrospora` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:47025` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dactylella_cylindrospora.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dacrymyces_stillatus.yaml data/taxa/eukaryota/dacryonaema_rufum.yaml data/taxa/eukaryota/dacryopinax_primogenitus.yaml data/taxa/eukaryota/dactylella_cylindrospora.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism/project/analysis chain, six exact NCBI type-material rows, one exact StrainInfo record with five deposit designations not retained in the final StrainInfo overlay, no exact BacDive rows, no final raw strain rows, two NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1814901`, `label: Dactylella cylindrospora`, `rank: SPECIES`, `parent_taxon: NCBITaxon:47025`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:474610`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dactylella` genus; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:16076`, which records one retained organism for `NCBITaxon:1814901`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1814901`. The YAML carries both exact synonyms and both related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The exact native GOLD chain contains organism `Go0631232`, project `Gp0644535`, and an analysis row named `Dactylella cylindrospora CBS325.70` that links back through `AP PROJECT GOLD IDS`.

The NCBI type-material inventory contributes six exact rows under the synonym taxon name `Candelabrella cylindrospora`, covering designation variants of `ATCC 44854`, `CBS 325.70`, and `IMI 140015`.

One exact StrainInfo record is keyed directly to `NCBITaxon:1814901` and carries five deposit designations, but it has not been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no `STRAININFO` source attestation is generated. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dactylella_cylindrospora.yaml` plus `just validate-strict data/taxa/eukaryota/dactylella_cylindrospora.yaml`.

## Additional Notes

The bounded scan found side-inventory `data/raw/ncbi_merged_ids.tsv` mappings from `NCBITaxon:47240` and `NCBITaxon:97334` into `NCBITaxon:1814901`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
