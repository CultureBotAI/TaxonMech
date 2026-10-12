# YAML Record Review: Westerdykella ornata

- Verdict: pass
- Target: `data/taxa/eukaryota/westerdykella_ornata.yaml`
- Identifier: `NCBITaxon:318751`

## Target

Reviewed the complete 81-line YAML record for Westerdykella ornata. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for westerdykella_ornata.

## Validation

- `just validate data/taxa/eukaryota/westerdykella_ornata.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/wenyingozyma_suzukii.yaml data/taxa/eukaryota/westerdykella_ornata.yaml data/taxa/eukaryota/whalleya_microplaca.yaml data/taxa/eukaryota/wickerhamia_fluorescens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 65301 retains `NCBITaxon:318751` as `Westerdykella ornata`, rank `SPECIES`, parent `NCBITaxon:45153`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:318751` at line 55175, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 1 related synonym, matching the YAML synonym entries. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:318751` at line 31883 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 4 type-material rows for the target at lines 174410 through 174413. BacDive contributed 0 exact rows; StrainInfo contributed 3 exact direct rows and 5 exact deposit rows for `NCBITaxon:318751`, with the target deposits all carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support, so the YAML accurately reflects the evidence available for the target identifier.
