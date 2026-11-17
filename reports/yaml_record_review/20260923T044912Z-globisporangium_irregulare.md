# YAML Record Review: Globisporangium irregulare

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/globisporangium_irregulare.yaml
- Started UTC: 2026-09-23T04:49:12Z
- Finished UTC: 2026-09-23T04:49:12Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:36331` |
| Label | `Globisporangium irregulare` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1448052` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/globisporangium_irregulare.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/globisporangium_irregulare.yaml data/taxa/eukaryota/globisporangium_iwayamae_daom_br242034.yaml data/taxa/eukaryota/globisporangium_splendens.yaml data/taxa/eukaryota/globisporangium_ultimum.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, two exact current native GOLD organisms with one linked native GOLD project and one linked native analysis, two side NCBI merged-ID rows, no retained retired NCBI rows, 75 exact StrainInfo rows, 84 exact StrainInfo deposit rows, no exact NCBI type-material rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:36331`, `label: Globisporangium irregulare`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1448052`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:4068`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Globisporangium`; the bounded scan checked all 10 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:33333`, which records one retained direct organism for `NCBITaxon:36331`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs additionally contain exact organism `Go0022611` plus exact organism `Go0572404` for strain `CBS 494.86`, with linked project `Gp0546994` and one native analysis whose `AP PROJECT GOLD IDS` include `Gp0546994`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:36331`. `Pythium irregulare` is present in `data/raw/ncbitaxon_taxa.tsv:4068` as an exact synonym, and all four generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. Current native GOLD side evidence has two exact organism rows by NCBI taxon ID and one linked project/analysis pair for `Globisporangium irregulare CBS 494.86`.

Exact StrainInfo rows are present as side inventory rows, but there are no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; StrainInfo only overlays BacDive-derived local strains, and this taxon has no generated local strain rows.

The side `data/raw/ncbi_merged_ids.tsv` inventory has `NCBITaxon:482709` and `NCBITaxon:482718` merged into `NCBITaxon:36331`, but the retained retired NCBI table contributes no old ID rows for this target. Omitting `replaces` is therefore consistent with the generated source state.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/globisporangium_irregulare.yaml` plus `just validate-strict data/taxa/eukaryota/globisporangium_irregulare.yaml`.

## Additional Notes

No prior exact ignored review report existed for `globisporangium_irregulare` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
