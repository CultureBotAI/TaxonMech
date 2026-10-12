# YAML Record Review: Fusarium avenaceum

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_avenaceum.yaml
- Started UTC: 2026-09-23T02:13:03Z
- Finished UTC: 2026-09-23T02:13:03Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:40199` |
| Label | `Fusarium avenaceum` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:679429` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_avenaceum.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/fusarium_austroamericanum.yaml data/taxa/eukaryota/fusarium_avenaceum.yaml data/taxa/eukaryota/fusarium_aywerte.yaml data/taxa/eukaryota/fusarium_azukiicola.yaml` | Passed; the strict batch scanned 4 files and exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with five organism assertions, five current native GOLD organism rows with eight linked projects, five native GOLD analysis rows linked by project ID, 207 direct StrainInfo rows, 220 StrainInfo deposit rows, eight NCBI type-material rows, eight NCBI merged-ID side rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:40199`, `label: Fusarium avenaceum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:679429`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:4563`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Fusarium tricinctum species complex`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:34478`, which records five retained direct organisms for `NCBITaxon:40199`; this agrees with `source_attestations[1].assertion_count: 5` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:40199`. The YAML preserves NCBI's exact synonyms `Fusisporium avenaceum`, `Gibberella avenacea`, and `Gibberella avenacea R.J. Cook, 1967` plus nine related synonyms.

`data/raw/ncbi_merged_ids.tsv` maps the old side-inventory IDs `NCBITaxon:1565509`, `NCBITaxon:1582856`, `NCBITaxon:502706`, `NCBITaxon:502707`, `NCBITaxon:502708`, `NCBITaxon:502709`, `NCBITaxon:502715`, and `NCBITaxon:502741` to `NCBITaxon:40199`; none is retained as a row with `retired_into` in `data/raw/ncbitaxon_taxa.tsv`, so the YAML correctly has no generated `replaces` entry. The retained GOLD aggregate supplies five organism assertions; the current native GOLD catalogs still contain five exact organism rows, eight linked project rows, and five linked analysis rows for the target NCBI taxon.

NCBI type-material rows 203918-203925 list eight culture-from-neotype designations for `Fusisporium avenaceum`, covering CBS 408.86, FRC R-8510, NRRL 26850, and NRRL 26911 variants; StrainInfo contains exact side evidence for the target in both the direct SI-ID view and the deposit view. Those side rows do not produce BacDive-derived local strain children for this taxon. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, three NCBI exact synonyms, nine NCBI related synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_avenaceum.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_avenaceum.yaml`.

## Additional Notes

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries. The NCBI merged-ID side rows are side evidence only; generated `replaces` comes from retained retired rows in `data/raw/ncbitaxon_taxa.tsv`.
