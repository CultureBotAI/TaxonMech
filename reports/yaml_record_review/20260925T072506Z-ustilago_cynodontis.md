# YAML Record Review: Ustilago cynodontis

- Verdict: pass
- Target: `data/taxa/eukaryota/ustilago_cynodontis.yaml`
- Identifier: `NCBITaxon:63396`

## Target

Reviewed the complete 75-line YAML record for Ustilago cynodontis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for ustilago_cynodontis.

## Validation

- `just validate data/taxa/eukaryota/ustilago_cynodontis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ustilaginoidea_virens.yaml data/taxa/eukaryota/ustilago_bromivora.yaml data/taxa/eukaryota/ustilago_cynodontis.yaml data/taxa/eukaryota/ustilago_esculenta.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 7970 retains `NCBITaxon:63396` as `Ustilago cynodontis`, rank `SPECIES`, parent `NCBITaxon:5269`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:63396` at line 53055, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 12 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:63396` at line 40098 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 2 analyses, 2 organism rows, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 0 type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 12 exact direct rows and 20 exact deposit rows for `NCBITaxon:63396`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact StrainInfo support but no BacDive, type-material, or generated strain-inventory rows, so the YAML accurately reflects the evidence available for the target identifier.
