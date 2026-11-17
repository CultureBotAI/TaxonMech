# YAML Record Review: Udeniozyma ferulica

- Verdict: pass
- Target: `data/taxa/eukaryota/udeniozyma_ferulica.yaml`
- Identifier: `NCBITaxon:106007`

## Target

Reviewed the complete 76-line YAML record for Udeniozyma ferulica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for udeniozyma_ferulica.

## Validation

- `just validate data/taxa/eukaryota/udeniozyma_ferulica.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/typhula_setipes.yaml data/taxa/eukaryota/udeniozyma_ferulica.yaml data/taxa/eukaryota/ulnaria_acus.yaml data/taxa/eukaryota/umbelopsis_angularis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 19041 retains `NCBITaxon:106007` as `Udeniozyma ferulica`, rank `SPECIES`, parent `NCBITaxon:1803525`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:106007` at line 53711, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 12 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:106007` at line 1094 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 4 type-material rows for the target at lines 3864 through 3867. BacDive contributed 0 exact rows; StrainInfo contributed 5 exact direct rows and 11 exact deposit rows for `NCBITaxon:106007`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support but no BacDive or generated strain-inventory rows, so the YAML accurately reflects the evidence available for the target identifier.
