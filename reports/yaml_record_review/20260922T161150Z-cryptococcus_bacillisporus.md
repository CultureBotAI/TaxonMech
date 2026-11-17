# YAML Record Review: Cryptococcus bacillisporus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryptococcus_bacillisporus.yaml
- Started UTC: 2026-09-22T16:11:50Z
- Finished UTC: 2026-09-22T16:11:50Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:552467` |
| Label | `Cryptococcus bacillisporus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1884637` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryptococcus_bacillisporus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryptococcus_bacillisporus.yaml` | Passed; the strict validator reported 0 total ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with two retained organisms, one exact native GOLD organism row, one exact native GOLD project row, no exact native GOLD analysis rows, 11 exact NCBI type-material side rows, 34 exact StrainInfo direct side rows and 48 exact StrainInfo deposit side rows without joined final StrainInfo rows, no final raw strain rows, one NCBI merged-ID side row, no retained retired rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:552467`, `label: Cryptococcus bacillisporus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1884637`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:129356`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Cryptococcus gattii species complex`; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:38601`, which records two retained organisms for `NCBITaxon:552467`; this agrees with `source_attestations[1].assertion_count: 2` and with the direct-filing note in the YAML.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:552467`. NCBI supplies exact synonyms `Cryptococcus bacillisporus VGIII`, `Cryptococcus gattii VGIII`, `Filobasidiella bacillispora`, and `Filobasidiella neoformans var. bacillispora`, plus three related synonyms for the current and basionym names; these match the YAML synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot has exact organism `Go0093647` and project `Gp0093647` for `Cryptococcus gattii`; no native analysis rows are filed under that project.

The NCBI type-material side inventory has 11 exact rows for this taxon: two `CBS 6955` culture-from-holotype spellings, five `NIH 191` culture-from-holotype spellings, and four `ATCC 32608` holotype spellings. The StrainInfo side inventory has 34 exact direct rows and 48 deposit rows, but none joined into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; no maintained final strain-table rows are present, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryptococcus_bacillisporus.yaml` plus `just validate-strict data/taxa/eukaryota/cryptococcus_bacillisporus.yaml`.

## Additional Notes

The bounded scan found one row in `data/raw/ncbi_merged_ids.tsv` that maps old `NCBITaxon:1450542` into `NCBITaxon:552467`; the old ID is only present in the side inventory, and there are no retained retired rows that would generate `replaces` entries.

The retained GOLD aggregate count for this taxon is larger than the exact native rows currently present in `data/gold/organisms.jsonl.gz`; the generated record follows the retained aggregate TSV for its source attestation count.
