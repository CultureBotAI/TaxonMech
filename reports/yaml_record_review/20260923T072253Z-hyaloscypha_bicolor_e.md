# YAML Record Review: Hyaloscypha bicolor E

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hyaloscypha_bicolor_e.yaml
- Started UTC: 2026-09-23T07:22:53Z
- Finished UTC: 2026-09-23T07:22:53Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1095630` |
| Label | `Hyaloscypha bicolor E` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2482752` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hyaloscypha_bicolor_e.yaml` | Passed; LinkML exited successfully. |
| `just validate-strict data/taxa/eukaryota/hyaloraphidium_curvatum.yaml data/taxa/eukaryota/hyaloscypha_bicolor.yaml data/taxa/eukaryota/hyaloscypha_bicolor_e.yaml data/taxa/eukaryota/hyaloscypha_finlandica.yaml` | Passed; the strict batch found zero error rows across four files. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, no current native GOLD organism, project, or analysis rows filed directly under this NCBI taxon ID, no exact NCBI type-material rows, no side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1095630`, `label: Hyaloscypha bicolor E`, `rank: STRAIN`, `parent_taxon: NCBITaxon:2482752`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:235680`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Hyaloscypha bicolor`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:1759`, which records one retained direct organism for `NCBITaxon:1095630`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1095630`. The source row has no exact or related synonyms to omit.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs no longer file an organism directly under `ORGANISM NCBI TAX ID` 1095630; the current `Hyaloscypha bicolor E` native GOLD organism is filed under the parent species NCBI taxon ID instead.

The scan found no exact NCBI type-material rows, side NCBI merged-ID rows, exact StrainInfo rows, exact BacDive rows, or maintained final strain-table rows. `strain_count: 0` is consistent with no generated child strain entries for this strain-rank taxon.

## Completeness

No consequential generated fields are missing. The record has a seeded strain identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact StrainInfo rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hyaloscypha_bicolor_e.yaml` plus `just validate-strict data/taxa/eukaryota/hyaloscypha_bicolor_e.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hyaloscypha_bicolor_e` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; no current native GOLD organism, project, or analysis rows are exact for `ORGANISM NCBI TAX ID` 1095630.
