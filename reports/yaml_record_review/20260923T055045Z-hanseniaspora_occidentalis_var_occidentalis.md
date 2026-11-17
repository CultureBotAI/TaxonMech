# YAML Record Review: Hanseniaspora occidentalis var. occidentalis

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hanseniaspora_occidentalis_var_occidentalis.yaml
- Started UTC: 2026-09-23T05:50:45Z
- Finished UTC: 2026-09-23T05:50:45Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:331639` |
| Label | `Hanseniaspora occidentalis var. occidentalis` |
| Rank | `VARIETAS` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:56407` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hanseniaspora_occidentalis_var_occidentalis.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hanseniaspora_occidentalis_var_citrica.yaml data/taxa/eukaryota/hanseniaspora_occidentalis_var_occidentalis.yaml data/taxa/eukaryota/hanseniaspora_opuntiae.yaml data/taxa/eukaryota/hanseniaspora_osmophila.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and no linked native analyses, 17 exact NCBI type-material rows, no side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:331639`, `label: Hanseniaspora occidentalis var. occidentalis`, `rank: VARIETAS`, `parent_taxon: NCBITaxon:56407`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:67662`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through parent species `Hanseniaspora occidentalis`; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy variety ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:32322`, which records one retained direct organism for `NCBITaxon:331639`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0705660` for strain `NRRL Y-7946` with linked project `Gp0831710`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:331639`. `data/raw/ncbitaxon_taxa.tsv:67662` has no exact or broad synonyms for this variety, and the generated related synonym `Hanseniaspora occidentalis var. occidentalis M.T. Sm., 1974` is present in the source row as a related synonym.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Hanseniaspora occidentalis var. occidentalis NRRL Y-7946`, one linked project, and no linked native analysis rows.

NCBI type material is present in `data/raw/ncbi_type_material.tsv:178906` through `data/raw/ncbi_type_material.tsv:178922` as 17 spellings for `ATCC 32053`, `BCRC 21358`, `CBS 2592`, `CCRC 21358`, `DBVPG 6798`, `IFO 1819`, `NRRL Y-7946`, and `VKM Y-211`. No side NCBI merged-ID row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded variety identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, the one NCBI related synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hanseniaspora_occidentalis_var_occidentalis.yaml` plus `just validate-strict data/taxa/eukaryota/hanseniaspora_occidentalis_var_occidentalis.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hanseniaspora_occidentalis_var_occidentalis` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
