# YAML Record Review: Dactylodendron pinicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dactylodendron_pinicola.yaml
- Started UTC: 2026-09-22T21:49:42Z
- Finished UTC: 2026-09-22T21:49:42Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:329262` |
| Label | `Dactylodendron pinicola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2824174` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dactylodendron_pinicola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dactylellina_cionopaga.yaml data/taxa/eukaryota/dactylodendron_pinicola.yaml data/taxa/eukaryota/dactylonectria_estremocensis.yaml data/taxa/eukaryota/dactylonectria_macrodidyma.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, no exact native GOLD rows in the local JSONL exports, 10 exact NCBI type-material rows, 11 exact StrainInfo direct records carrying 13 matching deposit designations that were not retained in the final StrainInfo overlay, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:329262`, `label: Dactylodendron pinicola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2824174`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:67223`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dactylodendron` genus; the bounded scan checked all 15 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:32219`, which records one retained organism for `NCBITaxon:329262`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:329262`. The YAML carries the one exact synonym and both related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL exports contain no exact organism, project, or analysis rows for `NCBITaxon:329262`, but the generated record relies on the retained aggregate row.

The NCBI type-material inventory contributes 10 exact rows under the synonym taxon name `Arthrographis pinicola`, covering designation variants of `ATCC 66466`, `CBS 653.89`, `DAOM 210573`, `IFM 52651`, and `UAMH 6402`.

Eleven exact StrainInfo direct records are keyed to `NCBITaxon:329262` and together carry 13 matching deposit designations, including a direct record for type deposit `ATCC 66466`, but none have been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no `STRAININFO` source attestation is generated. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dactylodendron_pinicola.yaml` plus `just validate-strict data/taxa/eukaryota/dactylodendron_pinicola.yaml`.

## Additional Notes

None.
