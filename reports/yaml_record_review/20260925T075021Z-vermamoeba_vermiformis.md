# YAML Record Review: Vermamoeba vermiformis

- Verdict: pass
- Target: `data/taxa/eukaryota/vermamoeba_vermiformis.yaml`
- Identifier: `NCBITaxon:5778`

## Target

Reviewed the complete 60-line YAML record for Vermamoeba vermiformis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for vermamoeba_vermiformis.

## Validation

- `just validate data/taxa/eukaryota/vermamoeba_vermiformis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/venturia_nashicola.yaml data/taxa/eukaryota/venturia_populina.yaml data/taxa/eukaryota/venturia_pyrina.yaml data/taxa/eukaryota/vermamoeba_vermiformis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 2566 retains `NCBITaxon:5778` as `Vermamoeba vermiformis`, rank `SPECIES`, parent `NCBITaxon:1260114`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:5778` at line 52080, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 1 related synonym, matching the YAML synonym entries. All 8 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:5778` at line 39322 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 0 type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 11 exact direct rows and 11 exact deposit rows for `NCBITaxon:5778`.

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
