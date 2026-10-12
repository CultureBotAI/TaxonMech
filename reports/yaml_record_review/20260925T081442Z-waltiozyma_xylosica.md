# YAML Record Review: Waltiozyma xylosica

- Verdict: pass
- Target: `data/taxa/eukaryota/waltiozyma_xylosica.yaml`
- Identifier: `NCBITaxon:1258691`

## Target

Reviewed the complete 80-line YAML record for Waltiozyma xylosica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for waltiozyma_xylosica.

## Validation

- `just validate data/taxa/eukaryota/waltiozyma_xylosica.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/waltiozyma_xylosica.yaml data/taxa/eukaryota/wenyingozyma_methanosorbosa.yaml data/taxa/eukaryota/wenyingozyma_methylovora.yaml data/taxa/eukaryota/wenyingozyma_naganishii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 290316 retains `NCBITaxon:1258691` as `Waltiozyma xylosica`, rank `SPECIES`, parent `NCBITaxon:3713752`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1258691` at line 58785, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table retains old identifier `NCBITaxon:756822` for this current target at line 94703.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1258691` at line 6116 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 15 type-material rows for the target at lines 17216 through 17230. BacDive contributed 0 exact rows; StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:1258691`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material support, no BacDive or StrainInfo matches, and a single retained NCBI old identifier already reconciled to the current target.
