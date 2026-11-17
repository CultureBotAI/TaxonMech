# YAML Record Review: Trichophyton tonsurans

- Verdict: pass
- Target: `data/taxa/eukaryota/trichophyton_tonsurans.yaml`
- Identifier: `NCBITaxon:34387`

## Target

Reviewed the complete 87-line YAML record for Trichophyton tonsurans. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichophyton_tonsurans.

## Validation

- `just validate data/taxa/eukaryota/trichophyton_tonsurans.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichophyton_rubrum_cbs_735_88.yaml data/taxa/eukaryota/trichophyton_tonsurans.yaml data/taxa/eukaryota/trichophyton_violaceum.yaml data/taxa/eukaryota/trichosporon_asahii.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 3842 retains `NCBITaxon:34387` as `Trichophyton tonsurans`, rank `SPECIES`, parent `NCBITaxon:5550`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:34387` at line 52275, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 2 exact, 0 broad, and 2 related synonyms, matching the two exact and two related synonym entries in YAML. All 15 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:34387` at line 32857 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 2 culture-from-neotype rows for the target at lines 188642 and 188643. BacDive contributed 0 exact rows; StrainInfo contributed 200 exact direct rows and 209 exact deposit rows for `NCBITaxon:34387`.

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
