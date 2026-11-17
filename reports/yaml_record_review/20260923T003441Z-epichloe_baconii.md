# YAML Record Review: Epichloe baconii

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/epichloe_baconii.yaml
- Started UTC: 2026-09-23T00:34:41Z
- Finished UTC: 2026-09-23T00:34:41Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:47801` |
| Label | `Epichloe baconii` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:5112` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/epichloe_baconii.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/epichloe_baconii.yaml data/taxa/eukaryota/epichloe_brachyelytri.yaml data/taxa/eukaryota/epichloe_bromicola.yaml data/taxa/eukaryota/epichloe_coenophiala.yaml` | Passed; the strict batch scanned 4 files and reported 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one exact native GOLD organism/project/analysis row, three exact StrainInfo rows with three deposits, no NCBI type-material rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:47801`, `label: Epichloe baconii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5112`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:6032`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through the `Epichloe` genus; the bounded scan checked all 16 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:36621`, which records one retained direct organism for `NCBITaxon:47801`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:47801`. The YAML preserves NCBI's one related synonym, `Epichloe baconii J.F. White, 1993`; NCBI supplies no exact or broad synonyms and no old-ID side rows.

The native GOLD catalogs contain one exact organism row, `Go0680290` for `Epichloe baconii E357`, with one matching project, `Gp0782308`, and one linked native GOLD analysis row. StrainInfo contains three exact target rows with three deposit designations for `Epichloe baconii`; those side rows do not produce BacDive-derived local strain children for this taxon.

No exact BacDive, NCBI type-material, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded identity, NCBI and GOLD source attestations, one NCBI related synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, or `data/raw/mediadive_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/epichloe_baconii.yaml` plus `just validate-strict data/taxa/eukaryota/epichloe_baconii.yaml`.

## Additional Notes

The retained GOLD aggregate count matches the one current native GOLD organism row. The native GOLD analysis row links through `AP PROJECT GOLD IDS` to current project `Gp0782308`.
