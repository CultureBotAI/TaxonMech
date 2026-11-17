# YAML Record Review: Debaryomyces psychrophilus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/debaryomyces_psychrophilus.yaml
- Started UTC: 2026-09-22T22:07:36Z
- Finished UTC: 2026-09-22T22:07:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:45577` |
| Label | `Debaryomyces psychrophilus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:4958` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/debaryomyces_psychrophilus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/debaryomyces_maramus.yaml data/taxa/eukaryota/debaryomyces_nepalensis.yaml data/taxa/eukaryota/debaryomyces_prosopidis.yaml data/taxa/eukaryota/debaryomyces_psychrophilus.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained direct organism, one exact native GOLD organism linked to one project and one analysis, 15 exact NCBI type-material rows, one exact StrainInfo direct record carrying 10 matching deposit designations, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:45577`, `label: Debaryomyces psychrophilus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:4958`, and `genetic_code: 12` match `data/raw/ncbitaxon_taxa.tsv:5623`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Debaryomyces` genus; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36078`, which records one retained direct organism for `NCBITaxon:45577`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:45577`. The YAML carries both exact synonyms filed for this row, `Candida psychrophila` and `Torulopsis psychrophila`, plus all three related synonyms, and NCBI supplies no broad synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD rows contain one exact organism, `Go0384527` for `Candida psychrophila NRRL Y-17665`; one project under that organism, `Gp0235634`; and one analysis named `Candida psychrophila NRRL Y-17665` that links back through `AP PROJECT GOLD IDS`.

The NCBI type-material inventory contributes 15 exact rows under the synonym taxon name `Torulopsis psychrophila`, covering culture-from-holotype variants of `ATCC 22163`, `ATCC 60199`, `BCRC 22405`, `CCRC 22405`, `IFO 10418`, and `JCM 2388`, plus holotype variants of `CBS 5956`.

The exact StrainInfo side inventory has one direct record and 10 matching deposit designations for `NCBITaxon:45577`, but none are present in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, NCBI exact and related synonyms, genetic code `12`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/debaryomyces_psychrophilus.yaml` plus `just validate-strict data/taxa/eukaryota/debaryomyces_psychrophilus.yaml`.

## Additional Notes

None.
