# YAML Record Review: Waltiozyma mucosa

- Verdict: pass
- Target: `data/taxa/eukaryota/waltiozyma_mucosa.yaml`
- Identifier: `NCBITaxon:1378264`

## Target

Reviewed the complete 91-line YAML record for Waltiozyma mucosa. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for waltiozyma_mucosa.

## Validation

- `just validate data/taxa/eukaryota/waltiozyma_mucosa.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/waltiozyma_mucosa.yaml data/taxa/eukaryota/waltiozyma_pijperi.yaml data/taxa/eukaryota/waltiozyma_solani.yaml data/taxa/eukaryota/waltiozyma_sp_nrrl_y_48258.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 336116 retains `NCBITaxon:1378264` as `Waltiozyma mucosa`, rank `SPECIES`, parent `NCBITaxon:3713752`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1378264` at line 59703, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 3 exact, 0 broad, and 4 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table retains old identifier `NCBITaxon:36039` for this current target at line 72554.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1378264` at line 8897 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 2 organism rows, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 16 type-material rows for the target at lines 26756 through 26771. BacDive contributed 0 exact rows; StrainInfo contributed 4 exact direct rows and 19 exact deposit rows for `NCBITaxon:1378264`, with the target deposits all carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with extensive exact synonym support, exact NCBI type-material rows, and exact StrainInfo deposit support already reconciled to the current target.
