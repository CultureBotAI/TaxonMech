# YAML Record Review: Cystobasidium sp. 2NP905A

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cystobasidium_sp_2np905a.yaml
- Started UTC: 2026-09-22T21:31:24Z
- Finished UTC: 2026-09-22T21:31:24Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2939524` |
| Label | `Cystobasidium sp. 2NP905A` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2605300` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cystobasidium_sp_2np905a.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cystobasidium_sp_2np905a.yaml data/taxa/eukaryota/cystobasidium_sp_p9004.yaml data/taxa/eukaryota/cystobasidium_sp_r9020.yaml data/taxa/eukaryota/cystofilobasidium_bisporidii.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism/project/analysis chain, no exact NCBI type-material rows, no exact BacDive or StrainInfo rows, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2939524`, `label: Cystobasidium sp. 2NP905A`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2605300`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:574171`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `unclassified Cystobasidium` parent; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:29041`, which records one retained organism for `NCBITaxon:2939524`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2939524`. NCBI supplies no exact, related, or broad synonyms for this row, so the absence of a `synonyms` block is expected.

The retained GOLD aggregate row supports the `GOLD` source attestation. The exact native GOLD chain contains organism `Go0657522`, project `Gp0701790`, and an analysis row named `Cystobasidiaceae sp. 2NP905A` that links back through `AP PROJECT GOLD IDS`.

No exact rows are present in NCBI type material, BacDive, StrainInfo, or the maintained final strain tables. `strain_count: 0` is therefore consistent with no generated child strains in the output.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cystobasidium_sp_2np905a.yaml` plus `just validate-strict data/taxa/eukaryota/cystobasidium_sp_2np905a.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:2939524`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
