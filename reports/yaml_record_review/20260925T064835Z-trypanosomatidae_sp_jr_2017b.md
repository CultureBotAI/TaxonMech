# YAML Record Review: Trypanosomatidae sp. JR-2017b

- Verdict: pass
- Target: `data/taxa/eukaryota/trypanosomatidae_sp_jr_2017b.yaml`
- Identifier: `NCBITaxon:2029566`

## Target

Reviewed the complete 59-line YAML record for Trypanosomatidae sp. JR-2017b. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trypanosomatidae_sp_jr_2017b.

## Validation

- `just validate data/taxa/eukaryota/trypanosomatidae_sp_jr_2017b.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trypanosoma_vivax.yaml data/taxa/eukaryota/trypanosomatidae_sp_jr_2017a.yaml data/taxa/eukaryota/trypanosomatidae_sp_jr_2017b.yaml data/taxa/eukaryota/trypethelium_eluteriae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 512220 retains `NCBITaxon:2029566` as `Trypanosomatidae sp. JR-2017b`, rank `SPECIES`, parent `NCBITaxon:193125`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:2029566` at line 62090, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 0 related synonyms, matching the absence of a YAML synonyms block. All 10 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:2029566` at line 19129 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. The NCBI type-material table has no rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:2029566`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed under unclassified Trypanosomatidae with no local BacDive or StrainInfo evidence and no generated strain inventory, so the YAML accurately reflects the direct target evidence.
