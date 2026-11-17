# YAML Record Review: Triparma pacifica

- Verdict: pass
- Target: `data/taxa/eukaryota/triparma_pacifica.yaml`
- Identifier: `NCBITaxon:91992`

## Target

Reviewed the complete 74-line YAML record for Triparma pacifica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for triparma_pacifica.

## Validation

- `just validate data/taxa/eukaryota/triparma_pacifica.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/triparma_pacifica.yaml data/taxa/eukaryota/tripos_fusus.yaml data/taxa/eukaryota/tritrichomonas_foetus.yaml data/taxa/eukaryota/truncatella_angustata.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 14878 retains `NCBITaxon:91992` as `Triparma pacifica`, rank `SPECIES`, parent `NCBITaxon:722752`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:91992` at line 53533, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 2 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 10 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:91992` at line 44495 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 2 organism rows, and 1 project for this identifier. The NCBI type-material table has no rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 8 exact direct rows and 9 exact deposit rows for `NCBITaxon:91992`.

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
