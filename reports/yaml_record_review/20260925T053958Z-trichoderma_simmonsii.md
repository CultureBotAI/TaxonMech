# YAML Record Review: Trichoderma simmonsii

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_simmonsii.yaml`
- Identifier: `NCBITaxon:1491479`

## Target

Reviewed the complete 84-line YAML record for Trichoderma simmonsii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_simmonsii.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_simmonsii.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_sempervirentis.yaml data/taxa/eukaryota/trichoderma_simmonsii.yaml data/taxa/eukaryota/trichoderma_sinense.yaml data/taxa/eukaryota/trichoderma_sinuosum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 381760 retains `NCBITaxon:1491479` as `Trichoderma simmonsii`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1491479` at line 60313, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 1 related synonym, matching the exact and related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1491479` at line 11606 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found seven type-material rows for the target: `CBS 130431`, `CBS:130431`, `G.J.S. 91-138`, `GJS 91-138`, `GJS:91-138`, `BPI 1112907`, and `BPI:1112907`. BacDive contributed 0 exact rows; StrainInfo contributed 1 exact direct row and 4 exact deposit rows for `NCBITaxon:1491479`.

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
