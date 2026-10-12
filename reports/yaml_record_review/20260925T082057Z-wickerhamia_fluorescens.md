# YAML Record Review: Wickerhamia fluorescens

- Verdict: pass
- Target: `data/taxa/eukaryota/wickerhamia_fluorescens.yaml`
- Identifier: `NCBITaxon:45790`

## Target

Reviewed the complete 78-line YAML record for Wickerhamia fluorescens. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for wickerhamia_fluorescens.

## Validation

- `just validate data/taxa/eukaryota/wickerhamia_fluorescens.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/wenyingozyma_suzukii.yaml data/taxa/eukaryota/westerdykella_ornata.yaml data/taxa/eukaryota/whalleya_microplaca.yaml data/taxa/eukaryota/wickerhamia_fluorescens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 5705 retains `NCBITaxon:45790` as `Wickerhamia fluorescens`, rank `SPECIES`, parent `NCBITaxon:45789`, genetic code `12`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:45790` at line 52690, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:45790` at line 36149 with `organism_count` 9, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 9 organism rows, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 13 type-material rows for the target at lines 216129 through 216141. BacDive contributed 0 exact rows; StrainInfo contributed 8 exact direct rows and 32 exact deposit rows for `NCBITaxon:45790`, with the target deposits all carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with nonstandard genetic code `12`, exact NCBI type-material support, and exact StrainInfo support already reconciled to the target identifier.
