# YAML Record Review: Globisporangium splendens

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/globisporangium_splendens.yaml
- Started UTC: 2026-09-23T04:49:12Z
- Finished UTC: 2026-09-23T04:49:12Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:82926` |
| Label | `Globisporangium splendens` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:1448052` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/globisporangium_splendens.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/globisporangium_irregulare.yaml data/taxa/eukaryota/globisporangium_iwayamae_daom_br242034.yaml data/taxa/eukaryota/globisporangium_splendens.yaml data/taxa/eukaryota/globisporangium_ultimum.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and one linked native analysis, 32 exact StrainInfo rows, 43 exact StrainInfo deposit rows, no exact NCBI type-material rows, no NCBI merged-ID rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:82926`, `label: Globisporangium splendens`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1448052`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:12504`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Globisporangium`; the bounded scan checked all 10 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:43018`, which records one retained direct organism for `NCBITaxon:82926`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0572113` for strain `rgcb-1`, linked project `Gp0546626`, and one native analysis whose `AP PROJECT GOLD IDS` include `Gp0546626`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:82926`. `Pythium splendens` is present in `data/raw/ncbitaxon_taxa.tsv:12504` as an exact synonym, and both generated related synonyms are present in the source row as related synonyms.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Globisporangium splendens rgcb-1`, one linked project, and one native analysis linked by `AP PROJECT GOLD IDS`.

Exact StrainInfo rows are present as side inventory rows, but there are no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; StrainInfo only overlays BacDive-derived local strains, and this taxon has no generated local strain rows.

No side `data/raw/ncbi_merged_ids.tsv` row, exact NCBI type-material row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, all NCBI exact and related synonyms for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/globisporangium_splendens.yaml` plus `just validate-strict data/taxa/eukaryota/globisporangium_splendens.yaml`.

## Additional Notes

No prior exact ignored review report existed for `globisporangium_splendens` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
