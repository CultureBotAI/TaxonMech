# YAML Record Review: Trypanosoma cruzi

- Verdict: pass
- Target: `data/taxa/eukaryota/trypanosoma_cruzi.yaml`
- Identifier: `NCBITaxon:5693`

## Target

Reviewed the complete 67-line YAML record for Trypanosoma cruzi. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trypanosoma_cruzi.

## Validation

- `just validate data/taxa/eukaryota/trypanosoma_cruzi.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trypanosoma_cruzi.yaml data/taxa/eukaryota/trypanosoma_cruzi_cruzi.yaml data/taxa/eukaryota/trypanosoma_cruzi_strain_cl_brener.yaml data/taxa/eukaryota/trypanosoma_cruzi_strain_esmeraldo.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 2539 retains `NCBITaxon:5693` as `Trypanosoma cruzi`, rank `SPECIES`, parent `NCBITaxon:47570`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:5693` at line 52070, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 1 related synonym, matching the single related synonym entry in YAML. All 11 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:5693` at line 39085 with `organism_count` 9, matching the YAML GOLD assertion count. The native GOLD tables contained 8 analyses, 9 organism rows, and 12 projects for this identifier. The NCBI type-material table has no rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 33 exact direct rows and 33 exact deposit rows for `NCBITaxon:5693`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a GOLD-rich NCBITaxon seed with exact StrainInfo support but no generated strain inventory, so the YAML accurately reflects the evidence available directly for the target identifier.
