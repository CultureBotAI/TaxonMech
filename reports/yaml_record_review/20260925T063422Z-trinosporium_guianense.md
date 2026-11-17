# YAML Record Review: Trinosporium guianense

- Verdict: pass
- Target: `data/taxa/eukaryota/trinosporium_guianense.yaml`
- Identifier: `NCBITaxon:1196434`

## Target

Reviewed the complete 75-line YAML record for Trinosporium guianense. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trinosporium_guianense.

## Validation

- `just validate data/taxa/eukaryota/trinosporium_guianense.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trigonopsis_cantarellii.yaml data/taxa/eukaryota/trigonopsis_variabilis.yaml data/taxa/eukaryota/trigonopsis_vinaria.yaml data/taxa/eukaryota/trinosporium_guianense.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 269144 retains `NCBITaxon:1196434` as `Trinosporium guianense`, rank `SPECIES`, parent `NCBITaxon:1196433`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1196434` at line 58288, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 1 related synonym, matching the single related synonym entry in YAML. All 14 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1196434` at line 4735 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 6 type-material rows for the target at lines 12947 through 12952. BacDive contributed 0 exact rows; StrainInfo contributed 1 exact direct row and 1 exact deposit row for `NCBITaxon:1196434`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with exact StrainInfo and NCBI type-material support but no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
