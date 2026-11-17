# YAML Record Review: Geotrichum armillariae

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/geotrichum_armillariae.yaml
- Started UTC: 2026-09-23T04:23:36Z
- Finished UTC: 2026-09-23T04:23:36Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:43962` |
| Label | `Geotrichum armillariae` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:43987` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/geotrichum_armillariae.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/geopyxis_carbonaria.yaml data/taxa/eukaryota/geosiphon_pyriformis.yaml data/taxa/eukaryota/geotrichum_armillariae.yaml data/taxa/eukaryota/geotrichum_candidum.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and no native analysis rows, nine exact NCBI type-material rows, 16 exact StrainInfo records carrying 33 exact deposit rows, one NCBI merged-ID side row but no retained retired old IDs, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:43962`, `label: Geotrichum armillariae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:43987`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:5279`, which carries the same label, parent, rank, code, two exact synonyms, two related synonyms, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Geotrichum`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:35519`, which records one retained direct organism for `NCBITaxon:43962`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0705304` for strain `NRRL Y-17580`, with linked project `Gp0831340`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:43962`. The YAML preserves exact synonyms `Dipodascus armillariae` and `Geotrichum decipiens`, and it preserves both related synonyms from the NCBI row.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Geotrichum armillariae NRRL Y-17580`, one linked project, and no native GOLD analysis currently links to that project.

The NCBI type-material table has nine exact rows for the target under `Dipodascus armillariae`: `ATCC 36758`, `ATCC:36758`, `CBS 817.71`, `CBS:817.71`, `IFO 10804`, `IFO:10804`, `NRRL Y-17580`, `NRRL:Y-17580`, and `NRRL:Y:17580`. StrainInfo has 16 exact target records and 33 exact deposits. These side rows do not create generated local strain entries by themselves.

The side `data/raw/ncbi_merged_ids.tsv` inventory maps old ID `NCBITaxon:1737032` into `NCBITaxon:43962`, but no retained row in `data/raw/ncbitaxon_taxa.tsv` carries that old ID with `retired_into`, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, two exact synonyms, two related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/geotrichum_armillariae.yaml` plus `just validate-strict data/taxa/eukaryota/geotrichum_armillariae.yaml`.

## Additional Notes

No prior exact ignored review report existed for `geotrichum_armillariae` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.

StrainInfo exact rows only overlay BacDive-derived local strains in this pipeline. Exact StrainInfo records for `NCBITaxon:43962` do not, by themselves, produce `data/straininfo/assemblies.tsv` or `data/straininfo/related_records.tsv.gz` rows.

The NCBI merged-ID hit for `NCBITaxon:1737032` is a side-inventory old ID only. Generated `replaces` values come from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`, not directly from every side row in `data/raw/ncbi_merged_ids.tsv`.
