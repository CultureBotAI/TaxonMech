# YAML Record Review: Dioszegia hungarica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/dioszegia_hungarica.yaml
- Started UTC: 2026-09-22T23:02:34Z
- Finished UTC: 2026-09-22T23:02:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:4972` |
| Label | `Dioszegia hungarica` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:165440` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/dioszegia_hungarica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/dioszegia_fristingensis.yaml data/taxa/eukaryota/dioszegia_hungarica.yaml data/taxa/eukaryota/diplocarpon_coronariae.yaml data/taxa/eukaryota/diplocarpon_rosae.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with ten retained direct organisms, nine exact native GOLD organisms with no linked local native projects or analyses, 22 exact NCBI type-material rows, 29 exact StrainInfo direct records carrying 56 matching deposit designations, no exact BacDive rows, no final raw strain rows, two NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:4972`, `label: Dioszegia hungarica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:165440`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2169`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Dioszegia` genus; the bounded scan checked all 12 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37233`, which records ten retained direct organisms for `NCBITaxon:4972`; this agrees with `source_attestations[1].assertion_count: 10` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:4972`. The YAML carries both exact synonyms and both related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain nine exact organisms for strains `UCD 68-187`, `NRRL Y-6667`, `NBRC 1052`, `JCM 9046`, `IFO 1052`, `DSM 6903`, `CCRC 21600`, `CBS 4214`, and `ATCC 24921`; the local native GOLD project and analysis tables have no exact rows linked through those organisms.

The NCBI type-material inventory contributes 22 exact rows under `Dioszegia hungarica`, covering the `CBS 4214` culture from type material and type-material designations for `ATCC 24291`, `BCRC 21600`, `CCRC 21600`, `DBVPG 7152`, `IFO 1052`, `IGC 3954`, `JCM 9046`, `MUCL 30660`, `NRRL Y-6667`, and `UCD 68-187`.

The exact StrainInfo side inventory has 29 direct records and 56 matching deposit designations for `NCBITaxon:4972`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/dioszegia_hungarica.yaml` plus `just validate-strict data/taxa/eukaryota/dioszegia_hungarica.yaml`.

## Additional Notes

The retained GOLD aggregate row reports ten organisms for this taxon, while the current local native GOLD scan found nine exact organism rows by `ORGANISM NCBI TAX ID`. The generated `source_attestations` entry follows the aggregate row.

The bounded scan also found side-inventory `data/raw/ncbi_merged_ids.tsv` mappings from `NCBITaxon:763780` and `NCBITaxon:89925` into `NCBITaxon:4972`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
