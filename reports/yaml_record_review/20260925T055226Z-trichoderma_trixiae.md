# YAML Record Review: Trichoderma trixiae

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_trixiae.yaml`
- Identifier: `NCBITaxon:1383392`

## Target

Reviewed the complete 84-line YAML record for Trichoderma trixiae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_trixiae.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_trixiae.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_texanum.yaml data/taxa/eukaryota/trichoderma_theobromicola.yaml data/taxa/eukaryota/trichoderma_trixiae.yaml data/taxa/eukaryota/trichoderma_turrialbense.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 338068 retains `NCBITaxon:1383392` as `Trichoderma trixiae`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1383392` at line 59745, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 2 related synonyms, matching the two related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1383392` at line 9016 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found nine type-material rows for the target: `C.P.K. 2138`, `CBS 134702`, `CBS:134702`, `CPK 2138`, `CPK:2138`, `Hypo 228`, `personal:Hypo:228`, `WU 24023`, and `WU:24023`. BacDive contributed 0 exact rows; StrainInfo contributed 7 exact direct rows and 7 exact deposit rows for `NCBITaxon:1383392`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material and exact StrainInfo support but no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
