# YAML Record Review: Cryptococcus gattii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryptococcus_gattii.yaml
- Started UTC: 2026-09-22T16:42:43Z
- Finished UTC: 2026-09-22T16:42:43Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:37769` |
| Label | `Cryptococcus gattii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1884637` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryptococcus_gattii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryptococcus_deuterogattii_r265.yaml data/taxa/eukaryota/cryptococcus_deuterogattii_ram5.yaml data/taxa/eukaryota/cryptococcus_floricola.yaml data/taxa/eukaryota/cryptococcus_gattii.yaml` | Passed; the strict batch reported 0 total ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, no exact native GOLD organism rows, 17 NCBI type-material rows, 45 exact StrainInfo rows, no final raw strain rows, four NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:37769`, `label: Cryptococcus gattii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1884637`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:4284`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cryptococcus gattii species complex`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:33793`, which records one retained organism filed directly under `NCBITaxon:37769`; this agrees with `source_attestations[1].assertion_count: 1` and the YAML note that descendant taxa are not gathered.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:37769`. The YAML carries all five exact synonyms and four related synonyms from the 2026-09-13 NCBI taxonomy snapshot, preserving `Cryptococcus neoformans var. gattii` as an exact synonym and the serotype labels as related synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot has no exact organism, project, or analysis rows for `NCBITaxon:37769`, which is consistent with the generated record relying on the retained aggregate row for its direct GOLD count.

NCBI type-material rows record neotype and culture-from-neotype labels for `Cryptococcus neoformans var. gattii`, including ATCC 32269, BCCM/IHEM 11796, CBS 6289, CBS 8273, IHEM 11796, MUCL 30449, NIH 3233, RV 20186, and CBS H-21966 forms. StrainInfo has 45 exact direct and deposit rows for this NCBI ID, but no BacDive-derived local strain row exists for this taxon, so no StrainInfo overlay is expected in the final strain tables and `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryptococcus_gattii.yaml` plus `just validate-strict data/taxa/eukaryota/cryptococcus_gattii.yaml`.

## Additional Notes

The bounded scan found four side-inventory rows in `data/raw/ncbi_merged_ids.tsv` that map old IDs `NCBITaxon:1608282`, `NCBITaxon:292817`, `NCBITaxon:37768`, and `NCBITaxon:413065` into active ID `NCBITaxon:37769`; it found no retained retired rows that would generate `replaces` entries.
