# YAML Record Review: Williopsis jadinii

- Verdict: pass
- Target: `data/taxa/eukaryota/williopsis_jadinii.yaml`
- Identifier: `NCBITaxon:4903`

## Target

Reviewed the complete 128-line YAML record for Williopsis jadinii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for williopsis_jadinii.

## Validation

- `just validate data/taxa/eukaryota/williopsis_jadinii.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/williopsis_galapagoensis.yaml data/taxa/eukaryota/williopsis_jadinii.yaml data/taxa/eukaryota/williopsis_lachancei.yaml data/taxa/eukaryota/williopsis_maclurae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 2133 retains `NCBITaxon:4903` as `Williopsis jadinii`, rank `SPECIES`, parent `NCBITaxon:4962`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:4903` at line 51871, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 9 exact, 0 broad, and 10 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps three old identifiers, `NCBITaxon:1128122`, `NCBITaxon:4961`, and `NCBITaxon:983966`, into this retained target, and the YAML keeps only `NCBITaxon:4903`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:4903` at line 37076 with `organism_count` 5, matching the YAML GOLD assertion count. The native GOLD tables contained 2 analyses, 2 organism rows, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 19 type-material rows for the target at lines 222710 through 222728. BacDive contributed 0 exact rows; StrainInfo contributed 147 exact direct rows and 317 exact deposit rows for `NCBITaxon:4903`, with all target deposits carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a retained NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support, and the three old NCBI identifiers correctly remain out of the YAML identifier set.
