# YAML Record Review: Truncocolumella citrina

- Verdict: pass
- Target: `data/taxa/eukaryota/truncocolumella_citrina.yaml`
- Identifier: `NCBITaxon:48597`

## Target

Reviewed the complete 75-line YAML record for Truncocolumella citrina. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for truncocolumella_citrina.

## Validation

- `just validate data/taxa/eukaryota/truncocolumella_citrina.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/truncocolumella_citrina.yaml data/taxa/eukaryota/tryblionella_coarctata.yaml data/taxa/eukaryota/tryblionella_compressa.yaml data/taxa/eukaryota/trypanosoma_brucei_brucei.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 6212 retains `NCBITaxon:48597` as `Truncocolumella citrina`, rank `SPECIES`, parent `NCBITaxon:48596`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:48597` at line 52782, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 1 related synonym, matching the single related synonym entry in YAML. All 14 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:48597` at line 36909 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 2 projects for this identifier. The NCBI type-material table has no rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:48597`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with no local BacDive or StrainInfo evidence and no generated strain inventory, so the YAML accurately preserves the sparse target-specific evidence.
