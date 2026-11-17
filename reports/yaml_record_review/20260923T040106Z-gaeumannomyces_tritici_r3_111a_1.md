# YAML Record Review: Gaeumannomyces tritici R3-111a-1

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/gaeumannomyces_tritici_r3_111a_1.yaml
- Started UTC: 2026-09-23T04:01:06Z
- Finished UTC: 2026-09-23T04:01:06Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:644352` |
| Label | `Gaeumannomyces tritici R3-111a-1` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:36779` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/gaeumannomyces_tritici_r3_111a_1.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fuscoporia_sp.yaml data/taxa/eukaryota/gaertneriomyces_semiglobifer.yaml data/taxa/eukaryota/gaeumannomyces_tritici_r3_111a_1.yaml data/taxa/eukaryota/gaillardinia_entomophila.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI strain row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and one linked native analysis row, no exact NCBI type-material, StrainInfo, BacDive, or NCBI merged-ID rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:644352`, `label: Gaeumannomyces tritici R3-111a-1`, `rank: STRAIN`, `parent_taxon: NCBITaxon:36779`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:148699`, which carries the same label, parent, rank, code, exact synonym, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through parent species `Gaeumannomyces tritici`; the bounded scan checked all 17 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:40289`, which records one retained direct organism for `NCBITaxon:644352`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain one exact organism, `Go0005124` for strain `R3-111a-1`, with one linked project, `Gp0005124`, and one analysis row linked through `AP PROJECT GOLD IDS`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:644352`. The YAML preserves exact synonym `Gaeumannomyces graminis var. tritici R3-111a-1` and correctly has no related-synonym entries because the related-synonym field is empty upstream.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have the exact organism `Gaeumannomyces graminis tritici R3-111a-1`, one matching project, and one native GOLD analysis for `Gaeumannomyces graminis tritici R3-111a-1`.

The NCBI type-material table and StrainInfo inventories have no exact rows for the target.

No side `data/raw/ncbi_merged_ids.tsv` row maps an old ID into `NCBITaxon:644352`, and no retained row in `data/raw/ncbitaxon_taxa.tsv` carries a retired ID for this target, so the YAML correctly has no generated `replaces` entry. No exact BacDive or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded strain identity, NCBI and GOLD source attestations, one exact synonym, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/gaeumannomyces_tritici_r3_111a_1.yaml` plus `just validate-strict data/taxa/eukaryota/gaeumannomyces_tritici_r3_111a_1.yaml`.

## Additional Notes

No prior exact ignored review report existed for `gaeumannomyces_tritici_r3_111a_1` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from direct rows in `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
