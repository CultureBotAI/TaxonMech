# YAML Record Review: Coniferiporia sulphurascens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/coniferiporia_sulphurascens.yaml
- Started UTC: 2026-09-22T14:16:11Z
- Finished UTC: 2026-09-22T14:20:13Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:175648` |
| Label | `Coniferiporia sulphurascens` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2038740` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/coniferiporia_sulphurascens.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/coniferiporia_sulphurascens.yaml` | Passed; the strict validator scanned one file with zero errors. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism/project/analysis chain, no NCBI type-material rows, one NCBI merged-ID side row, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:175648`, `label: Coniferiporia sulphurascens`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2038740`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:35590`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Coniferiporia` genus; the bounded scan checked all 13 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:15291`, which records one retained organism for `NCBITaxon:175648`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:175648`. NCBI supplies all three exact synonyms and all three related synonyms present in the YAML.

The native GOLD snapshot has one exact organism row for this NCBI taxon, `Go0448971` / `Coniferiporia sulphurascens FP133613(A)Sp`, with project `Gp0313361` / `Coniferiporia sulphurascens FP133613(A)Sp` and one linked analysis row; this agrees with the retained aggregate count.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, all generated synonyms from NCBI, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no NCBI type-material rows for `NCBITaxon:175648`; no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/coniferiporia_sulphurascens.yaml` plus `just validate-strict data/taxa/eukaryota/coniferiporia_sulphurascens.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv` has one side-inventory old ID that now maps into `NCBITaxon:175648`: `NCBITaxon:1664312`. The retained retired-row inventory is empty for this target, so the absence of `replaces` values in the YAML is expected.
