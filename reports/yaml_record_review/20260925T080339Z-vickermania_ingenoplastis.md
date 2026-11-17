# YAML Record Review: Vickermania ingenoplastis

- Verdict: pass
- Target: `data/taxa/eukaryota/vickermania_ingenoplastis.yaml`
- Identifier: `NCBITaxon:2720891`

## Target

Reviewed the complete 73-line YAML record for Vickermania ingenoplastis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for vickermania_ingenoplastis.

## Validation

- `just validate data/taxa/eukaryota/vickermania_ingenoplastis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/vickermania_ingenoplastis.yaml data/taxa/eukaryota/violaceomyces_palustris.yaml data/taxa/eukaryota/viridothelium_virens.yaml data/taxa/eukaryota/vishniacozyma_tephrensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 547273 retains `NCBITaxon:2720891` as `Vickermania ingenoplastis`, rank `SPECIES`, parent `NCBITaxon:2795773`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:2720891` at line 62991, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 10 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table retains old identifier `NCBITaxon:1967299` for this current target at line 33666.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:2720891` at line 25256 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 2 type-material rows for the target at lines 113546 through 113547. BacDive contributed 0 exact rows; StrainInfo contributed 1 exact direct row and 1 exact deposit row for `NCBITaxon:2720891`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support, so the YAML accurately reflects the evidence available for the target identifier.
