# YAML Record Review: Hanseniaspora occidentalis var. citrica

- Repository: CultureBotAI/TaxonMech
- Record: data/taxa/eukaryota/hanseniaspora_occidentalis_var_citrica.yaml
- Started UTC: 2026-09-23T05:50:45Z
- Finished UTC: 2026-09-23T05:50:45Z
- Verdict: pass

## Target

| Field | Value |
| --- | --- |
| Class | `TaxonRecord` |
| Identifier | `NCBITaxon:331638` |
| Label | `Hanseniaspora occidentalis var. citrica` |
| Rank | `VARIETAS` |
| Domain | `EUKARYOTA` |
| Parent | `NCBITaxon:56407` |
| Generated or maintained | Generated seeded record |
| Source provenance | `NCBITAXON`, `GOLD` |

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/eukaryota/hanseniaspora_occidentalis_var_citrica.yaml` | Passed; LinkML reported `No issues found`. |
| `just validate-strict data/taxa/eukaryota/hanseniaspora_occidentalis_var_citrica.yaml data/taxa/eukaryota/hanseniaspora_occidentalis_var_occidentalis.yaml data/taxa/eukaryota/hanseniaspora_opuntiae.yaml data/taxa/eukaryota/hanseniaspora_osmophila.yaml` | Passed; the strict batch reported zero ERROR rows. |
| `just validate-history` | Not rerun for this generated single-record review; the full-corpus history validator already passed on this checkout and this review did not edit YAML. |
| `just verify-corpus` | Not rerun for this generated single-record review; the full-corpus corpus check already passed on this checkout and this review did not edit YAML. |
| `just validate-products` | Not applicable; this generated taxon record has no `causal_graphs` block or generated causal products. |
| Bounded source scan | Passed; `taxonmech_bounded_scan.py` found an exact NCBI row, one seed-scope row, one retained GOLD aggregate row with one organism assertion, one exact current native GOLD organism with one linked native GOLD project and no linked native analyses, no exact NCBI type-material rows, no side NCBI merged-ID rows, no exact StrainInfo rows, no exact BacDive rows, no final raw strain rows, and no lineage mismatches. |

## Identity and Grounding

The record identity is internally consistent. `identifier: NCBITaxon:331638`, `label: Hanseniaspora occidentalis var. citrica`, `rank: VARIETAS`, `parent_taxon: NCBITaxon:56407`, and `genetic_code: 1` match `data/raw/ncbitaxon_taxa.tsv:67661`, which carries the same label, parent, rank, code, and `gold` attestation flag in the 2026-09-13 NCBI taxonomy snapshot.

The lineage is complete for the generated NCBI path from root through parent species `Hanseniaspora occidentalis`; the bounded scan checked all 14 lineage entries and found no missing or mismatched IDs. `grounding_status: EXACT` is appropriate because the file is keyed by the exact NCBI Taxonomy variety ID.

The `GOLD` attestation is supported by `data/raw/gold_organisms.tsv:32321`, which records one retained direct organism for `NCBITaxon:331638`; this agrees with `source_attestations[1].assertion_count: 1` and its organism assertion unit. The current native GOLD catalogs also contain exact organism `Go0705143` for strain `CBS 6783` with linked project `Gp0831166`.

## Evidence

The `NCBITAXON` attestation correctly points at `NCBITaxon:331638`. `data/raw/ncbitaxon_taxa.tsv:67661` has no exact or broad synonyms for this variety, and the generated related synonym `Hanseniaspora occidentalis var. citrica Cadez, Raspor & M.T. Sm.,` is present in the source row as a related synonym.

The retained GOLD aggregate supplies one organism assertion. The current native GOLD catalogs have one exact organism for `Hanseniaspora occidentalis var. citrica CBS 6783`, one linked project, and no linked native analysis rows.

No exact NCBI type-material row, side NCBI merged-ID row, exact StrainInfo row, exact BacDive row, or maintained final strain-table row is present, so `strain_count: 0` is consistent with no generated local strain entries in the output.

## Completeness

No consequential generated fields are missing. The record has a seeded variety identity, NCBI and GOLD source attestations, genetic code `1`, a complete generated lineage, the one NCBI related synonym for the source row, and `strain_count: 0`.

The bounded scan found no exact target rows in the maintained final strain tables: `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`; no exact rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`; no exact BacDive rows; no exact rows in `data/raw/mediadive_taxa.tsv`; and no exact rows in the bacterial-only auxiliary inventories `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, or `data/raw/madin_taxa.tsv`.

## Findings

None found.

## Recommended Edits

None.

## Follow-up Checks

None required. If upstream NCBI, GOLD, BacDive, or StrainInfo inputs change, regenerate the taxon records and rerun `just validate data/taxa/eukaryota/hanseniaspora_occidentalis_var_citrica.yaml` plus `just validate-strict data/taxa/eukaryota/hanseniaspora_occidentalis_var_citrica.yaml`.

## Additional Notes

No prior exact ignored review report existed for `hanseniaspora_occidentalis_var_citrica` before this report was written; the `find` check covered the ignored `reports/` tree.

The retained GOLD aggregate count is derived from `data/raw/gold_organisms.tsv`; the current native GOLD organism, project, and analysis rows are exact by NCBI taxon ID or linked project ID but are side evidence only and do not create generated child strains without BacDive-derived local strain inventory entries.
