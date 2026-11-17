# YAML Record Review: Danielia oregonensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/danielia_oregonensis.yaml
- Started UTC: 2026-09-22T21:58:01Z
- Finished UTC: 2026-09-22T21:58:01Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:46584` |
| Label | `Danielia oregonensis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:3312681` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/danielia_oregonensis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/danielia_oregonensis.yaml data/taxa/eukaryota/danielia_reshetovae.yaml data/taxa/eukaryota/danielozyma_ontarioensis.yaml data/taxa/eukaryota/darkera_picea.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism/project/analysis chain, 18 exact NCBI type-material rows, 7 exact StrainInfo direct records carrying 23 matching deposit designations that were not retained in the final StrainInfo overlay, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:46584`, `label: Danielia oregonensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3312681`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:5857`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Danielia` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36325`, which records one retained organism for `NCBITaxon:46584`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:46584`. The YAML carries the one exact synonym and both related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The exact native GOLD chain contains organism `Go0517103`, project `Gp0441141`, and an analysis row named `Clavispora oregonensis NRRL Y-5850` that links back through `AP PROJECT GOLD IDS`.

The NCBI type-material inventory contributes 18 exact rows under the synonym taxon name `Candida oregonensis`, covering designation variants of `ATCC 42268`, `BCRC 21575`, `CBS 5036`, `CCRC 21575`, `DBVPG 6149`, `IFO 1980`, `JCM 1811`, `NRRL Y-5850`, and `UCD 60-73`.

Seven exact StrainInfo direct records are keyed to `NCBITaxon:46584` and together carry 23 matching deposit designations, including retained GOLD strain `NRRL Y-5850`, but none have been retained into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no `STRAININFO` source attestation is generated. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/danielia_oregonensis.yaml` plus `just validate-strict data/taxa/eukaryota/danielia_oregonensis.yaml`.

## Additional Notes

None.
