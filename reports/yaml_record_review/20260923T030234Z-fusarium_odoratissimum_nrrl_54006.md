# YAML Record Review: Fusarium odoratissimum NRRL 54006

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/fusarium_odoratissimum_nrrl_54006.yaml
- Started UTC: 2026-09-23T03:02:34Z
- Finished UTC: 2026-09-23T03:02:34Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:1089451` |
| Label | `Fusarium odoratissimum NRRL 54006` |
| Rank | `STRAIN` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:2502994` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/fusarium_odoratissimum_nrrl_54006.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/fusarium_nurragi.yaml data/taxa/eukaryota/fusarium_nygamai.yaml data/taxa/eukaryota/fusarium_odoratissimum.yaml data/taxa/eukaryota/fusarium_odoratissimum_nrrl_54006.yaml` | Passed; the strict batch scanned 4 files with 0 files with errors and 0 total error rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one retained GOLD aggregate row with one organism assertion, one current native GOLD organism row with one linked project and one native analysis row, no NCBI merged-ID side rows, no NCBI type-material rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:1089451`, `label: Fusarium odoratissimum NRRL 54006`, `rank: STRAIN`, `parent_taxon: NCBITaxon:2502994`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:234258`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through `Fusarium odoratissimum`; the bounded scan checked all 18 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy strain ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:1642`, which records one retained direct organism for `NCBITaxon:1089451`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs still contain the exact organism `Go0037084`, the linked project `Gp0037084`, and one analysis linked to that project.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:1089451`. The YAML preserves both exact NCBI synonyms, `Fusarium oxysporum f. sp. cubense tropical race 4 54006` and `Fusarium oxysporum f. sp. cubense tropical race 4 II5`.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs still contain one exact organism row, one linked project row, and one project-linked analysis row, all using the same strain-specific NCBI taxon ID.

No side-inventory NCBI old IDs merge into `NCBITaxon:1089451`, so the YAML correctly has no generated `replaces` entry. The NCBI type-material inventory has no exact row for this strain ID, which is appropriate for a strain-level child. No exact StrainInfo, exact BacDive, or maintained final strain-table rows are present, so `strain_count: 0` is consistent with no generated child strains in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded strain identity, NCBI and GOLD source attestations, NCBI exact synonyms, genetic code `1`, a complete generated lineage, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/fusarium_odoratissimum_nrrl_54006.yaml` plus `just validate-strict data/taxa/eukaryota/fusarium_odoratissimum_nrrl_54006.yaml`.

## Additional Notes

No prior exact ignored review report existed for `fusarium_odoratissimum_nrrl_54006` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
