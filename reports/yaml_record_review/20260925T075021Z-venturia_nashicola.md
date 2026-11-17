# YAML Record Review: Venturia nashicola

- Verdict: pass
- Target: `data/taxa/eukaryota/venturia_nashicola.yaml`
- Identifier: `NCBITaxon:86259`

## Target

Reviewed the complete 81-line YAML record for Venturia nashicola. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for venturia_nashicola.

## Validation

- `just validate data/taxa/eukaryota/venturia_nashicola.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/venturia_nashicola.yaml data/taxa/eukaryota/venturia_populina.yaml data/taxa/eukaryota/venturia_pyrina.yaml data/taxa/eukaryota/vermamoeba_vermiformis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 13346 retains `NCBITaxon:86259` as `Venturia nashicola`, rank `SPECIES`, parent `NCBITaxon:5024`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:86259` at line 53439, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 1 related synonym, matching the YAML synonym entries. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:86259` at line 43426 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 2 analyses, 2 organism rows, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 0 type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 5 exact direct rows and 7 exact deposit rows for `NCBITaxon:86259`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact StrainInfo support but no BacDive, type-material, merged-ID, or generated strain-inventory rows to reconcile, so the YAML accurately reflects the evidence available for the target identifier.
