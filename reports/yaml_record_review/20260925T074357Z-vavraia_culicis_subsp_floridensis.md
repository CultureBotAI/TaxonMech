# YAML Record Review: Vavraia culicis subsp. floridensis

- Verdict: pass
- Target: `data/taxa/eukaryota/vavraia_culicis_subsp_floridensis.yaml`
- Identifier: `NCBITaxon:948595`

## Target

Reviewed the complete 70-line YAML record for Vavraia culicis subsp. floridensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for vavraia_culicis_subsp_floridensis.

## Validation

- `just validate data/taxa/eukaryota/vavraia_culicis_subsp_floridensis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/vanrija_thermophila.yaml data/taxa/eukaryota/vaucheria_litorea.yaml data/taxa/eukaryota/vavraia_culicis_subsp_floridensis.yaml data/taxa/eukaryota/vavraia_culicis_subsp_floridensis_vc3h.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 203805 retains `NCBITaxon:948595` as `Vavraia culicis subsp. floridensis`, rank `SUBSPECIES`, parent `NCBITaxon:103449`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:948595` at line 57030, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 1 related synonym, matching the YAML synonym entries. All 11 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:948595` at line 45056 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 0 type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:948595`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact direct-only NCBITaxon and GOLD seed for a Vavraia subspecies target with no BacDive, StrainInfo, type-material, or generated strain-inventory rows to reconcile, so the YAML accurately reflects the evidence available for the target identifier.
