# YAML Record Review: Yamadazyma tumulicola

- Verdict: pass
- Target: `data/taxa/eukaryota/yamadazyma_tumulicola.yaml`
- Identifier: `NCBITaxon:480051`

## Target

Reviewed the complete 121-line YAML record for Yamadazyma tumulicola. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yamadazyma_tumulicola.

## Validation

- `just validate data/taxa/eukaryota/yamadazyma_tumulicola.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/yamadazyma_tenuis.yaml data/taxa/eukaryota/yamadazyma_triangularis.yaml data/taxa/eukaryota/yamadazyma_tumulicola.yaml data/taxa/eukaryota/yamadazyma_ubonensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 107219 retains `NCBITaxon:480051` as `Yamadazyma tumulicola`, rank `SPECIES`, parent `NCBITaxon:766765`, genetic code `12`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:480051` at line 55787, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 16 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps old `NCBITaxon:480052` through `NCBITaxon:480064` to this target at lines 80891 through 80903; an ignored-file-inclusive exact scan found no retained current NCBITaxon rows for those old identifiers.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:480051` at line 36730 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. `data/raw/ncbi_type_material.tsv` contained 9 rows, covering 2 culture-from-holotype aliases for `CBS 10917`, 3 culture-from-type-material aliases for `NBRC 104392`, and 4 type-material aliases for `JCM 15403` and `T6517-9-5`. BacDive contributed 0 exact rows, and StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:480051`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with no generated raw strain-table rows pending YAML incorporation.
