# YAML Record Review: Williopsis saturnus

- Verdict: pass
- Target: `data/taxa/eukaryota/williopsis_saturnus.yaml`
- Identifier: `NCBITaxon:907340`

## Target

Reviewed the complete 120-line YAML record for Williopsis saturnus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for williopsis_saturnus.

## Validation

- `just validate data/taxa/eukaryota/williopsis_saturnus.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/williopsis_misumaiensis.yaml data/taxa/eukaryota/williopsis_samutprakarnensis.yaml data/taxa/eukaryota/williopsis_sargentensis.yaml data/taxa/eukaryota/williopsis_saturnus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 191056 retains `NCBITaxon:907340` as `Williopsis saturnus`, rank `SPECIES`, parent `NCBITaxon:4962`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:907340` at line 56873, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 9 exact, 0 broad, and 8 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps four old identifiers, `NCBITaxon:1781328`, `NCBITaxon:36037`, `NCBITaxon:4906`, and `NCBITaxon:54047`, into this retained target, and the YAML keeps only `NCBITaxon:907340`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:907340` at line 44262 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 25 type-material rows for the target at lines 272142 through 272166. BacDive contributed 0 exact rows; StrainInfo contributed 88 exact direct rows and 206 exact deposit rows for `NCBITaxon:907340`, with six deposit-only StrainInfo records carried by other exact direct taxa.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a retained NCBITaxon and GOLD seed with exact NCBI type-material and substantial exact StrainInfo support, and the four old NCBI identifiers correctly remain out of the YAML identifier set.
