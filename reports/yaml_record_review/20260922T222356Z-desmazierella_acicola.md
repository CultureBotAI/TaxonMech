# YAML Record Review: Desmazierella acicola

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/desmazierella_acicola.yaml
- Started UTC: 2026-09-22T22:23:56Z
- Finished UTC: 2026-09-22T22:23:56Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:47194` |
| Label | `Desmazierella acicola` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:47193` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/desmazierella_acicola.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/descolea_maculata.yaml data/taxa/eukaryota/desmazierella_acicola.yaml data/taxa/eukaryota/detonula_confervacea.yaml data/taxa/eukaryota/devriesia_sp.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained direct organism, no exact current native GOLD organism/project/analysis rows, no exact NCBI type-material rows, three exact StrainInfo direct records carrying four matching deposit designations, no exact BacDive rows, no final raw strain rows, 27 NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:47194`, `label: Desmazierella acicola`, `rank: SPECIES`, `parent_taxon: NCBITaxon:47193`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5935`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Desmazierella` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36461`, which records one retained direct organism for `NCBITaxon:47194`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:47194`. The YAML carries the exact synonym `Desmazierella aicola` and all 27 related synonyms filed for this row; NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD exact scan did not find a current native organism, project, or analysis row for `NCBITaxon:47194`; the generated retained GOLD aggregate row is still sufficient for the one-organism source attestation in this record.

The exact StrainInfo side inventory has three direct records and four matching deposit designations for `NCBITaxon:47194`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact NCBI type-material, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/desmazierella_acicola.yaml` plus `just validate-strict data/taxa/eukaryota/desmazierella_acicola.yaml`.

## Additional Notes

The bounded scan found 27 side-inventory `data/raw/ncbi_merged_ids.tsv` mappings into `NCBITaxon:47194`, covering `NCBITaxon:1543717`, `NCBITaxon:1548944`, `NCBITaxon:1550247` through `NCBITaxon:1550265`, and `NCBITaxon:1604359` through `NCBITaxon:1604364`; no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` would generate `replaces` entries.
