# YAML Record Review: Wolfiporia cocos

- Verdict: pass
- Target: `data/taxa/eukaryota/wolfiporia_cocos.yaml`
- Identifier: `NCBITaxon:81056`

## Target

Reviewed the complete 97-line YAML record for Wolfiporia cocos. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for wolfiporia_cocos.

## Validation

- `just validate data/taxa/eukaryota/wolfiporia_cocos.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/williopsis_suaveolens.yaml data/taxa/eukaryota/williopsis_takata.yaml data/taxa/eukaryota/williopsis_vartiovaarae.yaml data/taxa/eukaryota/wolfiporia_cocos.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 12194 retains `NCBITaxon:81056` as `Wolfiporia cocos`, rank `SPECIES`, parent `NCBITaxon:81055`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:81056` at line 53365, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 4 exact, 0 broad, and 5 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps three old identifiers, `NCBITaxon:2603541`, `NCBITaxon:2788928`, and `NCBITaxon:87299`, into this retained target, and the YAML keeps only `NCBITaxon:81056`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:81056` at line 42926 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 2 analyses, 1 organism row, and 11 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 12 exact direct rows and 26 exact deposit rows for `NCBITaxon:81056`, with all target deposits carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a retained NCBITaxon and GOLD seed with exact StrainInfo support, and descendant Wolfiporia records remain deliberately outside this direct-target assertion count.
