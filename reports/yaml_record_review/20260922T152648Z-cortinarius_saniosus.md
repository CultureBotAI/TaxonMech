# YAML Record Review: Cortinarius saniosus

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/cortinarius_saniosus.yaml
- Started UTC: 2026-09-22T15:26:48Z
- Finished UTC: 2026-09-22T15:26:48Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:304786` |
| Label | `Cortinarius saniosus` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:34451` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/cortinarius_saniosus.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/cortinarius_rubellus.yaml data/taxa/eukaryota/cortinarius_saniosus.yaml data/taxa/eukaryota/cortinarius_sp.yaml data/taxa/eukaryota/corynascus_novoguineensis.yaml` | Passed; the strict validator scanned four files with zero errors, including this record. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one retained organism, one exact native GOLD organism row, two exact native GOLD project rows, no exact native GOLD analysis rows, three NCBI type-material rows, one NCBI merged-ID side row, no exact StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:304786`, `label: Cortinarius saniosus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:34451`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:62215`, which carries the same label, parent, rank, and code in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Cortinarius` genus; the bounded scan checked all 14 ancestors and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:30593`, which records one retained organism for `NCBITaxon:304786`; this agrees with `source_attestations[1].assertion_count: 1`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:304786`. NCBI supplies exact synonyms `Agaricus saniosus` and `Cortinarius bavaricus`, plus related synonyms `Agaricus saniosus Fr., 1821`, `Cortinarius bavaricus M.M. Moser, 1983`, and `Cortinarius saniosus (Fr.) Fr., 1838`, matching the YAML synonyms.

The retained GOLD aggregate row supports the `GOLD` source attestation. The local native GOLD JSONL snapshot also has exact organism `Go0532375` for `Cortinarius saniosus 2018PMI107` and exact projects `Gp0478825` and `Gp0484076`; no native analysis rows are filed under those projects.

NCBI has three exact type-material side rows for this taxon, all holotype variants for the synonymous `Cortinarius bavaricus` name. No exact StrainInfo rows or maintained final strain-table rows are present, so `strain_count: 0` is consistent with the generated outputs.

The single `curation_history` event records seeding from `data/raw/`, `data/atb/`, and `data/straininfo/`, and its source list agrees with the two retained source attestations.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, the generated NCBI exact and related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no joined exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/related_records.tsv.gz`, or `data/straininfo/exclusions.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/cortinarius_saniosus.yaml` plus `just validate-strict data/taxa/eukaryota/cortinarius_saniosus.yaml`.

## Additional Notes

`data/raw/ncbi_merged_ids.tsv:43050` maps old ID `NCBITaxon:2493870` into `NCBITaxon:304786`, but the bounded scan found no retained retired NCBI row, so no generated `replaces` entry is expected.
