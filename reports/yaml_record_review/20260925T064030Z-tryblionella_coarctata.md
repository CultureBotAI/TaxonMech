# YAML Record Review: Tryblionella coarctata

- Verdict: pass
- Target: `data/taxa/eukaryota/tryblionella_coarctata.yaml`
- Identifier: `NCBITaxon:3687705`

## Target

Reviewed the complete 75-line YAML record for Tryblionella coarctata. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tryblionella_coarctata.

## Validation

- `just validate data/taxa/eukaryota/tryblionella_coarctata.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/truncocolumella_citrina.yaml data/taxa/eukaryota/tryblionella_coarctata.yaml data/taxa/eukaryota/tryblionella_compressa.yaml data/taxa/eukaryota/trypanosoma_brucei_brucei.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 641551 retains `NCBITaxon:3687705` as `Tryblionella coarctata`, rank `SPECIES`, parent `NCBITaxon:913972`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:3687705` at line 63692, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 12 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:3687705` at line 33533 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. The NCBI type-material table has no rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:3687705`.

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
