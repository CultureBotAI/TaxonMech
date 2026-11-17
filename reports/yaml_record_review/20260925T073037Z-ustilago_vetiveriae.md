# YAML Record Review: Ustilago vetiveriae

- Verdict: pass
- Target: `data/taxa/eukaryota/ustilago_vetiveriae.yaml`
- Identifier: `NCBITaxon:249491`

## Target

Reviewed the complete 69-line YAML record for Ustilago vetiveriae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for ustilago_vetiveriae.

## Validation

- `just validate data/taxa/eukaryota/ustilago_vetiveriae.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ustilago_tritici.yaml data/taxa/eukaryota/ustilago_vetiveriae.yaml data/taxa/eukaryota/ustilago_xerochloae.yaml data/taxa/eukaryota/ustilentyloma_graminis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 49069 retains `NCBITaxon:249491` as `Ustilago vetiveriae`, rank `SPECIES`, parent `NCBITaxon:5269`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:249491` at line 54756, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 1 related synonym, matching the YAML synonym entries. All 12 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:249491` at line 22542 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 0 type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:249491`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with native GOLD support but no BacDive, StrainInfo, type-material, or generated strain-inventory rows to reconcile, so the YAML accurately reflects the evidence available for the target identifier.
