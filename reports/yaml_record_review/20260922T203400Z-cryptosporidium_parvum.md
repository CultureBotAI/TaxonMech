# YAML Record Review: Cryptosporidium parvum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cryptosporidium_parvum.yaml
- Started UTC: 2026-09-22T20:34:00Z
- Finished UTC: 2026-09-22T20:34:00Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:5807` |
| Label | `Cryptosporidium parvum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5806` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cryptosporidium_parvum.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cryptosporidium_parvum.yaml data/taxa/eukaryota/cryptosporidium_ryanae.yaml data/taxa/eukaryota/cryptosporidium_sp_chipmunk_genotype_i.yaml data/taxa/eukaryota/cryptosporidium_tyzzeri.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with sixteen retained organisms, seventeen exact native GOLD organism rows, seventeen exact native GOLD project rows, fifteen exact native GOLD analysis rows, no NCBI type-material rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, NCBI merged-ID side rows but no retained retired rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:5807`, `label: Cryptosporidium parvum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5806`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:2578`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cryptosporidium` genus; the bounded scan checked all 12 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:39370`, which records sixteen retained organisms for `NCBITaxon:5807`; this agrees with `source_attestations[1].assertion_count: 16`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:5807`. NCBI supplies thirteen related synonyms on the same row, from `Cryptosporidium parvum Tyzzer, 1912` through the `Cryptosporidium sp. A1` to `Cryptosporidium sp. A12` names including `Cryptosporidium sp. A7-MAZM`; these match the YAML `synonyms` block.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot has seventeen current exact organisms and seventeen exact projects for `NCBITaxon:5807`, spanning `Go0002365`/`Gp0002365` through `Go0682646`/`Gp0784734`; fifteen exact native analysis rows are tied to the same native project set.

No exact NCBI type-material, StrainInfo, BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, generated NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cryptosporidium_parvum.yaml` plus `just validate-strict data/taxa/eukaryota/cryptosporidium_parvum.yaml`.

## Additional Notes

The bounded scan found side-inventory old IDs `NCBITaxon:2200815`, `NCBITaxon:2200816`, `NCBITaxon:2200817`, `NCBITaxon:2200818`, `NCBITaxon:2200819`, `NCBITaxon:2200820`, `NCBITaxon:2200821`, `NCBITaxon:2200822`, `NCBITaxon:2200823`, `NCBITaxon:2200824`, `NCBITaxon:2200825`, and `NCBITaxon:2200826` in `data/raw/ncbi_merged_ids.tsv`, but no retained retired rows in `data/raw/ncbitaxon_taxa.tsv` that would generate `replaces` entries.
