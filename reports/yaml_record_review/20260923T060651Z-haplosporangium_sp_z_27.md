# YAML Record Review: Haplosporangium sp. Z 27

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/haplosporangium_sp_z_27.yaml
- Started UTC: 2026-09-23T06:06:51Z
- Finished UTC: 2026-09-23T06:06:51Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1897644` |
| Label | `Haplosporangium sp. Z 27` |
| Rank | `SPECIES` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2626619` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/haplosporangium_sp_z_27.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/haplosporangium_sp_z_27.yaml data/taxa/eukaryota/hapsidospora_chrysogena.yaml data/taxa/eukaryota/haptolina_brevifila.yaml data/taxa/eukaryota/haptolina_ericina.yaml` | Passed; the strict batch exited successfully. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, two exact current native GOLD organisms with two linked native GOLD projects and no linked native analyses, no exact NCBI type-material rows, no side NCBI merged-ID rows, no exact BacDive or StrainInfo rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1897644`, `label: Haplosporangium sp. Z 27`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2626619`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:491722`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `unclassified Haplosporangium`; the bounded scan checked all 13 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy species ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:17124`, which records one retained direct organism for `NCBITaxon:1897644`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs contain two exact organisms and two linked projects.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1897644`. `Haplosporangium sp. NRRL 3175` is present in `data/raw/ncbitaxon_taxa.tsv:491722` as an exact synonym, and there are no source related synonyms to emit.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have exact organisms for `Z 27` and `NRRL 3175`; both organisms have linked projects, and no exact linked project has a native analysis row.

No NCBI type-material row, side NCBI merged-ID row, exact BacDive row, direct exact StrainInfo row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded species identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, the NCBI exact synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive or StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/haplosporangium_sp_z_27.yaml` plus `just validate-strict data/taxa/eukaryota/haplosporangium_sp_z_27.yaml`.

## Additional Notes

No prior exact ignored review report existed for `haplosporangium_sp_z_27` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism and project rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
