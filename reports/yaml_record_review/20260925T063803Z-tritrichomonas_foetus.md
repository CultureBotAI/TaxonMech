# YAML Record Review: Tritrichomonas foetus

- Verdict: pass
- Target: `data/taxa/eukaryota/tritrichomonas_foetus.yaml`
- Identifier: `NCBITaxon:1144522`

## Target

Reviewed the complete 60-line YAML record for Tritrichomonas foetus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tritrichomonas_foetus.

## Validation

- `just validate data/taxa/eukaryota/tritrichomonas_foetus.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/triparma_pacifica.yaml data/taxa/eukaryota/tripos_fusus.yaml data/taxa/eukaryota/tritrichomonas_foetus.yaml data/taxa/eukaryota/truncatella_angustata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 248692 retains `NCBITaxon:1144522` as `Tritrichomonas foetus`, rank `SPECIES`, parent `NCBITaxon:5723`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1144522` at line 57917, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 1 related synonym, matching the YAML synonym entries. All 8 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1144522` at line 2966 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. The NCBI type-material table has no rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 8 exact direct rows and 8 exact deposit rows for `NCBITaxon:1144522`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact StrainInfo support but no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
