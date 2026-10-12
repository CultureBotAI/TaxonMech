# YAML Record Review: Xingzhongia strasburgensis

- Verdict: pass
- Target: `data/taxa/eukaryota/xingzhongia_strasburgensis.yaml`
- Identifier: `NCBITaxon:3713894`

## Target

Reviewed the complete 98-line YAML record for Xingzhongia strasburgensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for xingzhongia_strasburgensis.

## Validation

- `just validate data/taxa/eukaryota/xingzhongia_strasburgensis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/xeromyces_bisporus.yaml data/taxa/eukaryota/xingzhongia_hampshirensis.yaml data/taxa/eukaryota/xingzhongia_strasburgensis.yaml data/taxa/eukaryota/xiuguozyma_insectalens.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 645460 retains `NCBITaxon:3713894` as `Xingzhongia strasburgensis`, rank `SPECIES`, parent `NCBITaxon:3712565`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:3713894` at line 63698, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 6 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps one old identifier, `NCBITaxon:53604`, into this retained target, and the YAML keeps only `NCBITaxon:3713894`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:3713894` at line 33607 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 14 type-material rows for the target at lines 197312 through 197325. BacDive contributed 0 exact rows, and StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:3713894`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact retained NCBITaxon and GOLD seed with exact NCBI type-material support, and the old NCBI identifier correctly remains out of the YAML identifier set.
