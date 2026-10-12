# YAML Record Review: Diaporthe ampelina

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/diaporthe_ampelina.yaml
- Started UTC: 2026-09-22T22:26:04Z
- Finished UTC: 2026-09-22T22:26:04Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1214573` |
| Label | `Diaporthe ampelina` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:36922` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/diaporthe_ampelina.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/diacronema_lutheri.yaml data/taxa/eukaryota/diaporthe_ampelina.yaml data/taxa/eukaryota/diaporthe_aspalathi.yaml data/taxa/eukaryota/diaporthe_caulivora.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained direct organisms, two exact native GOLD organisms linked to two projects and two analyses, four exact NCBI type-material rows, 25 exact StrainInfo direct records carrying 35 matching deposit designations, no exact BacDive rows, no final raw strain rows, 14 NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1214573`, `label: Diaporthe ampelina`, `rank: SPECIES`, `parent_taxon: NCBITaxon:36922`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:274828`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Diaporthe` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:5100`, which records two retained direct organisms for `NCBITaxon:1214573`; this agrees with `source_attestations[1].assertion_count: 2` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1214573`. The YAML carries all six exact synonyms and all 18 related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain two exact organisms, `Go0114000` for `Diaporthe ampelina UCDDA912` and `Go0144199` for `Diaporthe ampelina S3MP`; two projects, `Gp0117694` and `Gp0149794`; and two analyses that link back through `AP PROJECT GOLD IDS`.

The NCBI type-material inventory contributes four exact rows under the synonym taxon name `Phoma ampelina`, covering culture-from-neotype variants of `CBS 114016` and `STEU 2660`.

The exact StrainInfo side inventory has 25 direct records and 35 matching deposit designations for `NCBITaxon:1214573`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/diaporthe_ampelina.yaml` plus `just validate-strict data/taxa/eukaryota/diaporthe_ampelina.yaml`.

## Additional Notes

The bounded scan found 14 side-inventory `data/raw/ncbi_merged_ids.tsv` mappings into `NCBITaxon:1214573`, including `NCBITaxon:127590`, `NCBITaxon:1304142`, `NCBITaxon:83180`, and 11 `NCBITaxon:9840xx` IDs; no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
