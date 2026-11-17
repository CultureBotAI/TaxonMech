# YAML Record Review: Xingzhongia hampshirensis

- Verdict: pass
- Target: `data/taxa/eukaryota/xingzhongia_hampshirensis.yaml`
- Identifier: `NCBITaxon:1041608`

## Target

Reviewed the complete 86-line YAML record for Xingzhongia hampshirensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for xingzhongia_hampshirensis.

## Validation

- `just validate data/taxa/eukaryota/xingzhongia_hampshirensis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/xeromyces_bisporus.yaml data/taxa/eukaryota/xingzhongia_hampshirensis.yaml data/taxa/eukaryota/xingzhongia_strasburgensis.yaml data/taxa/eukaryota/xiuguozyma_insectalens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 223682 retains `NCBITaxon:1041608` as `Xingzhongia hampshirensis`, rank `SPECIES`, parent `NCBITaxon:3712565`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1041608` at line 57276, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 2 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps one old identifier, `NCBITaxon:53608`, into this retained target, and the YAML keeps only `NCBITaxon:1041608`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1041608` at line 588 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 12 type-material rows for the target at lines 2546 through 2557. BacDive contributed 0 exact rows; StrainInfo contributed 1 exact direct row and 9 exact deposit rows for `NCBITaxon:1041608`, with all target deposits carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a retained NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support, and the old NCBI identifier correctly remains out of the YAML identifier set.
