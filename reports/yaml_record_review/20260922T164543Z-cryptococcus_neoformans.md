# YAML Record Review: Cryptococcus neoformans

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryptococcus_neoformans.yaml
- Started UTC: 2026-09-22T16:45:43Z
- Finished UTC: 2026-09-22T16:45:43Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5207` |
| Label | `Cryptococcus neoformans` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1897064` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryptococcus_neoformans.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryptococcus_gattii_wm276.yaml data/taxa/eukaryota/cryptococcus_neoformans.yaml data/taxa/eukaryota/cryptococcus_neoformans_102_14.yaml data/taxa/eukaryota/cryptococcus_neoformans_1033.yaml` | Passed; the strict batch reported 0 total ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with 26 retained organisms, two exact native GOLD organism rows, two exact native GOLD project rows, two exact native GOLD analysis rows, five NCBI type-material rows, 857 exact StrainInfo rows, no final raw strain rows, two NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5207`, `label: Cryptococcus neoformans`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1897064`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2288`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cryptococcus neoformans species complex`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:37781`, which records 26 retained organisms filed directly under `NCBITaxon:5207`; this agrees with `source_attestations[1].assertion_count: 26` and the YAML note that descendant taxa are not gathered.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5207`. The YAML carries all nine exact synonyms and eleven related synonyms from the 2026-09-13 NCBI taxonomy snapshot, including the exact `Cryptococcus neoformans var. grubii`, `Filobasidiella neoformans`, and `Torula neoformans` aliases.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organisms `Go0657856` and `Go0657857`, exact projects `Gp0702124` and `Gp0702125`, and two native analysis rows for `Cryptococcus neoformans PH4021C` and `Cryptococcus neoformans PH4008` tied to those projects.

NCBI type-material rows record CBS 8710, H99, and NYSD 1649 labels for `Cryptococcus neoformans var. grubii`. StrainInfo has 857 exact direct rows and 932 exact deposit rows for this NCBI ID, but no BacDive-derived local strain row exists for this taxon, so no StrainInfo overlay is expected in the final strain tables and `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryptococcus_neoformans.yaml` plus `just validate-strict data/taxa/eukaryota/cryptococcus_neoformans.yaml`.

## Additional Notes

The bounded scan found two side-inventory rows in `data/raw/ncbi_merged_ids.tsv` that map old IDs `NCBITaxon:178876` and `NCBITaxon:427679` into active ID `NCBITaxon:5207`; it found no retained retired rows that would generate `replaces` entries.
