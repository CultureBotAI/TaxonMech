# YAML Record Review: Cutaneotrichosporon curvatum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cutaneotrichosporon_curvatum.yaml
- Started UTC: 2026-09-22T20:50:37Z
- Finished UTC: 2026-09-22T20:50:37Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:57679` |
| Label | `Cutaneotrichosporon curvatum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1838142` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cutaneotrichosporon_curvatum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cutaneotrichosporon_curvatum.yaml data/taxa/eukaryota/cutaneotrichosporon_cutaneum.yaml data/taxa/eukaryota/cutaneotrichosporon_cyanovorans.yaml data/taxa/eukaryota/cutaneotrichosporon_daszewskae.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with nine retained organisms, nine exact native GOLD organism rows, five exact native GOLD project rows, three exact native GOLD analysis rows, 22 exact NCBI type-material rows, 26 exact StrainInfo direct side rows covering 61 deposits, no exact BacDive rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:57679`, `label: Cutaneotrichosporon curvatum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1838142`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:7324`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cutaneotrichosporon` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39300`, which records nine retained organisms for `NCBITaxon:57679`; this agrees with `source_attestations[1].assertion_count: 9`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:57679`. NCBI supplies seven exact synonyms and one related synonym on the same row, matching the YAML `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The complete local native GOLD JSONL snapshot has nine exact organism rows for `ATCC 20509`, `SBUG-Y 855`, `JCM 1532`, `PYCC 2565`, `NBRC 1159`, `MUCL 29819`, `DSM 101032`, `CBS 570`, and `ATCC 100567`; five exact native projects and three exact native analyses are tied to those organism IDs.

NCBI lists 22 exact type-material side rows under `Candida heveanensis var. curvata`, all with `type material` status and alternate plain or colonized designations. Exact StrainInfo side rows are also present, covering 61 deposits across 26 direct StrainInfo records; none are joined into the maintained final StrainInfo or raw strain tables for this target.

No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cutaneotrichosporon_curvatum.yaml` plus `just validate-strict data/taxa/eukaryota/cutaneotrichosporon_curvatum.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:57679`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
