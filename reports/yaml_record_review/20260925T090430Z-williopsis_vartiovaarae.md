# YAML Record Review: Williopsis vartiovaarae

- Verdict: pass
- Target: `data/taxa/eukaryota/williopsis_vartiovaarae.yaml`
- Identifier: `NCBITaxon:51918`

## Target

Reviewed the complete 85-line YAML record for Williopsis vartiovaarae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for williopsis_vartiovaarae.

## Validation

- `just validate data/taxa/eukaryota/williopsis_vartiovaarae.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/williopsis_suaveolens.yaml data/taxa/eukaryota/williopsis_takata.yaml data/taxa/eukaryota/williopsis_vartiovaarae.yaml data/taxa/eukaryota/wolfiporia_cocos.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 6527 retains `NCBITaxon:51918` as `Williopsis vartiovaarae`, rank `SPECIES`, parent `NCBITaxon:4962`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:51918` at line 52844, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 2 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:51918` at line 37685 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 18 type-material rows for the target at lines 227185 through 227202. BacDive contributed 0 exact rows; StrainInfo contributed 8 exact direct rows and 17 exact deposit rows for `NCBITaxon:51918`, with all target deposits carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support, and no generated raw strain-table rows pending YAML incorporation.
