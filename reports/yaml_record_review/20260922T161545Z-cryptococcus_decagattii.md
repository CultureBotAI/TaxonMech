# YAML Record Review: Cryptococcus decagattii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryptococcus_decagattii.yaml
- Started UTC: 2026-09-22T16:15:45Z
- Finished UTC: 2026-09-22T16:15:45Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1859122` |
| Label | `Cryptococcus decagattii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1884637` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryptococcus_decagattii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryptococcus_decagattii.yaml` | Passed; the strict validator reported 0 total ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, no exact native GOLD organism/project/analysis rows, 16 exact NCBI type-material side rows, one exact StrainInfo direct side row and one exact StrainInfo deposit side row without joined final StrainInfo rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1859122`, `label: Cryptococcus decagattii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1884637`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:485940`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Cryptococcus gattii species complex`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:16590`, which records one retained organism for `NCBITaxon:1859122`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1859122`. NCBI supplies the exact synonyms `Cryptococcus gattii AFLP10`, `Cryptococcus gattii VGIV/VGIIIc`, and `Cryptococcus gattii VGIVj/VGIIIc` and the related synonym `Cryptococcus decagattii Hagen & Boekhout, 2015`, matching the YAML synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The bounded scan did not find any exact native GOLD organism, project, or analysis rows for this taxon in the local `data/gold/*.jsonl.gz` snapshot.

The NCBI type-material side inventory has 16 exact rows for this taxon: twelve culture-from-holotype spellings for the IHEM/CBS/RV identifiers and four `CBS H-21970` holotype spellings. The StrainInfo side inventory has one exact direct row and one exact deposit row, but neither joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no maintained final strain-table rows are present, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryptococcus_decagattii.yaml` plus `just validate-strict data/taxa/eukaryota/cryptococcus_decagattii.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:1859122`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.

The retained GOLD aggregate row has one organism for this species, while the bounded scan found no exact native GOLD JSONL rows under `NCBITaxon:1859122`; the generated record follows the retained aggregate TSV for its source attestation count.
