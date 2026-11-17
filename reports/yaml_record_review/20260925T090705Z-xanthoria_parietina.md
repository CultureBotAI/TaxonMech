# YAML Record Review: Xanthoria parietina

- Verdict: pass
- Target: `data/taxa/eukaryota/xanthoria_parietina.yaml`
- Identifier: `NCBITaxon:107463`

## Target

Reviewed the complete 97-line YAML record for Xanthoria parietina. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for xanthoria_parietina.

## Validation

- `just validate data/taxa/eukaryota/xanthoria_parietina.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/wolfiporia_cocos_cgmcc_5_0078.yaml data/taxa/eukaryota/wolfiporia_cocos_md_104_ss10.yaml data/taxa/eukaryota/xanthoporus_peckianus.yaml data/taxa/eukaryota/xanthoria_parietina.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 19411 retains `NCBITaxon:107463` as `Xanthoria parietina`, rank `SPECIES`, parent `NCBITaxon:88741`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:107463` at line 53725, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 18 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:107463` at line 1354 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 2 organism rows, and 8 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 1 exact direct row and 1 exact deposit row for `NCBITaxon:107463`, with all target deposits carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact StrainInfo support, and descendant Xanthoria records remain deliberately outside this direct-target assertion count.
