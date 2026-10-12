# YAML Record Review: Wallemia mellicola

- Verdict: pass
- Target: `data/taxa/eukaryota/wallemia_mellicola.yaml`
- Identifier: `NCBITaxon:1708541`

## Target

Reviewed the complete 70-line YAML record for Wallemia mellicola. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for wallemia_mellicola.

## Validation

- `just validate data/taxa/eukaryota/wallemia_mellicola.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/wallemia_ichthyophaga.yaml data/taxa/eukaryota/wallemia_mellicola.yaml data/taxa/eukaryota/wallemia_mellicola_cbs_633_66.yaml data/taxa/eukaryota/waltiozyma_chaumierensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 445969 retains `NCBITaxon:1708541` as `Wallemia mellicola`, rank `SPECIES`, parent `NCBITaxon:148959`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1708541` at line 61137, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 1 related synonym, matching the YAML synonym entries. All 12 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1708541` at line 14794 with `organism_count` 25, matching the YAML GOLD assertion count. The native GOLD tables contained 25 analyses, 25 organism rows, and 25 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 5 type-material rows for the target at lines 53912 through 53916. BacDive contributed 0 exact rows; StrainInfo contributed 9 exact direct rows and 10 exact deposit rows for `NCBITaxon:1708541`, including 1 target deposit on 1 non-direct StrainInfo row.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with direct GOLD rows, exact NCBI type-material support, and exact StrainInfo support; the descendant strain target has a separate record and GOLD aggregate.
