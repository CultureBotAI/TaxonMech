# YAML Record Review: Corynascus novoguineensis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/corynascus_novoguineensis.yaml
- Started UTC: 2026-09-22T15:26:48Z
- Finished UTC: 2026-09-22T15:26:48Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1126955` |
| Label | `Corynascus novoguineensis` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:72985` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/corynascus_novoguineensis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cortinarius_rubellus.yaml data/taxa/eukaryota/cortinarius_saniosus.yaml data/taxa/eukaryota/cortinarius_sp.yaml data/taxa/eukaryota/corynascus_novoguineensis.yaml` | Passed; the strict validator scanned four files with zero errors, including this record. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, one exact native GOLD project row, no exact native GOLD analysis rows, two NCBI type-material rows, six exact StrainInfo deposit hits across four direct records, no final raw strain rows, no NCBI merged-ID side rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1126955`, `label: Corynascus novoguineensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:72985`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:244476`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Corynascus` genus; the bounded scan checked all 16 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:2542`, which records one retained organism for `NCBITaxon:1126955`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1126955`. NCBI supplies exact synonyms `Myceliophthora novoguineensis` and `Thielavia novoguineensis`, plus related synonyms `Corynascus novoguineensis (Udagawa & Y. Horie) Arx, 1973`, `Myceliophthora novoguineensis (Udagawa & Y. Horie) van den Brink & Samson 2012`, and `Thielavia novoguineensis Udagawa & Y. Horie, 1972`, matching the YAML synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0382589` for `Corynascus novoguineensis CBS 359.72` and exact project `Gp0223619`; no native analysis rows are filed under that project.

NCBI has two exact type-material side rows for `CBS 359.72` under the synonymous `Thielavia novoguineensis` name. StrainInfo has exact direct records for the taxon, but no BacDive-backed strain row joins them into `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; `strain_count: 0` is therefore consistent with the maintained generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/corynascus_novoguineensis.yaml` plus `just validate-strict data/taxa/eukaryota/corynascus_novoguineensis.yaml`.

## Additional Notes

The bounded scan found no rows in `data/raw/ncbi_merged_ids.tsv` that map an old ID into `NCBITaxon:1126955`; there are no side-inventory old IDs and no retained retired rows that would generate `replaces` entries.
