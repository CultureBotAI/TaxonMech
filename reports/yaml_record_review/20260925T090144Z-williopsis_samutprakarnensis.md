# YAML Record Review: Williopsis samutprakarnensis

- Verdict: pass
- Target: `data/taxa/eukaryota/williopsis_samutprakarnensis.yaml`
- Identifier: `NCBITaxon:1241557`

## Target

Reviewed the complete 86-line YAML record for Williopsis samutprakarnensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for williopsis_samutprakarnensis.

## Validation

- `just validate data/taxa/eukaryota/williopsis_samutprakarnensis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/williopsis_misumaiensis.yaml data/taxa/eukaryota/williopsis_samutprakarnensis.yaml data/taxa/eukaryota/williopsis_sargentensis.yaml data/taxa/eukaryota/williopsis_saturnus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 284515 retains `NCBITaxon:1241557` as `Williopsis samutprakarnensis`, rank `SPECIES`, parent `NCBITaxon:4962`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1241557` at line 58640, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 4 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps two old identifiers, `NCBITaxon:1138491` and `NCBITaxon:913275`, into this retained target, and the YAML keeps only `NCBITaxon:1241557`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1241557` at line 5760 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 8 type-material rows for the target at lines 16150 through 16157. BacDive contributed 0 exact rows, and StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:1241557`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact retained NCBITaxon and GOLD seed with exact NCBI type-material support, and the two old NCBI identifiers correctly remain out of the YAML identifier set.
