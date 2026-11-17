# YAML Record Review: Trichomonascaceae sp. Y4102

- Verdict: pass
- Target: `data/taxa/eukaryota/trichomonascaceae_sp_y4102.yaml`
- Identifier: `NCBITaxon:2939545`

## Target

Reviewed the complete 68-line YAML record for Trichomonascaceae sp. Y4102. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichomonascaceae_sp_y4102.

## Validation

- `just validate data/taxa/eukaryota/trichomonascaceae_sp_y4102.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichomonas_tenax.yaml data/taxa/eukaryota/trichomonascaceae_sp_y4102.yaml data/taxa/eukaryota/trichophaea_hybrida.yaml data/taxa/eukaryota/trichophyton_interdigitale.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 574179 retains `NCBITaxon:2939545` as `Trichomonascaceae sp. Y4102`, rank `SPECIES`, parent `NCBITaxon:1194608`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:2939545` at line 63391, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 0 related synonyms, matching the absence of YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:2939545` at line 29049 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for the target. BacDive and StrainInfo contributed 0 exact direct or deposit rows for `NCBITaxon:2939545`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with no type-material support and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
