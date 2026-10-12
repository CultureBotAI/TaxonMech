# YAML Record Review: Hepatocystis sp. ex Piliocolobus tephrosceles

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hepatocystis_sp_ex_piliocolobus_tephrosceles.yaml
- Started UTC: 2026-09-23T06:38:21Z
- Finished UTC: 2026-09-23T06:38:21Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:2600580` |
| Label | `Hepatocystis sp. ex Piliocolobus tephrosceles` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2632946` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hepatocystis_sp_ex_piliocolobus_tephrosceles.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hemisphaericaspora_xylofermentans.yaml data/taxa/eukaryota/henningerozyma_blattae.yaml data/taxa/eukaryota/henningerozyma_blattae_cbs_6284.yaml data/taxa/eukaryota/hepatocystis_sp_ex_piliocolobus_tephrosceles.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and one linked native analysis, no exact NCBI type-material rows, no side NCBI merged-ID rows, no exact BacDive or StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:2600580`, `label: Hepatocystis sp. ex Piliocolobus tephrosceles`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2632946`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:535484`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `unclassified Hepatocystis`; the bounded scan checked all 11 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:23892`, which records one retained direct organism for `NCBITaxon:2600580`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism, one linked project, and one linked analysis.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:2600580`. `data/raw/ncbitaxon_taxa.tsv:535484` has no exact, broad, or related synonyms, so the generated record correctly has no `synonyms` block.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have an exact `Go0567959` organism, a linked `Gp0538322` project in `data/gold/projects.jsonl.gz:394149`, and one native analysis linked by that exact project ID.

No NCBI type-material row, side NCBI merged-ID row, exact BacDive row, exact StrainInfo row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, no source NCBI synonyms to carry, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hepatocystis_sp_ex_piliocolobus_tephrosceles.yaml` plus `just validate-strict data/taxa/eukaryota/hepatocystis_sp_ex_piliocolobus_tephrosceles.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hepatocystis_sp_ex_piliocolobus_tephrosceles` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
