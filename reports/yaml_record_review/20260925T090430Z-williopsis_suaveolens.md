# YAML Record Review: Williopsis suaveolens

- Verdict: pass
- Target: `data/taxa/eukaryota/williopsis_suaveolens.yaml`
- Identifier: `NCBITaxon:907738`

## Target

Reviewed the complete 93-line YAML record for Williopsis suaveolens. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for williopsis_suaveolens.

## Validation

- `just validate data/taxa/eukaryota/williopsis_suaveolens.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/williopsis_suaveolens.yaml data/taxa/eukaryota/williopsis_takata.yaml data/taxa/eukaryota/williopsis_vartiovaarae.yaml data/taxa/eukaryota/wolfiporia_cocos.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 191275 retains `NCBITaxon:907738` as `Williopsis suaveolens`, rank `SPECIES`, parent `NCBITaxon:4962`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:907738` at line 56875, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 4 exact, 0 broad, and 4 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps two old identifiers, `NCBITaxon:27307` and `NCBITaxon:58637`, into this retained target, and the YAML keeps only `NCBITaxon:907738`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:907738` at line 44275 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 5 type-material rows for the target at lines 272192 through 272196. BacDive contributed 0 exact rows; StrainInfo contributed 26 exact direct rows and 44 exact deposit rows for `NCBITaxon:907738`, with all target deposits carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a retained NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support, and the two old NCBI identifiers correctly remain out of the YAML identifier set.
