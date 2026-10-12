# YAML Record Review: Trichoderma inhamatum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_inhamatum.yaml`
- Identifier: `NCBITaxon:58856`

## Target

Reviewed the complete 81-line YAML record for Trichoderma inhamatum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_inhamatum.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_inhamatum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_hunua.yaml data/taxa/eukaryota/trichoderma_inhamatum.yaml data/taxa/eukaryota/trichoderma_intricatum.yaml data/taxa/eukaryota/trichoderma_istrianum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 7441 retains `NCBITaxon:58856` as `Trichoderma inhamatum`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:58856` at line 52997, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 1 related synonym, matching the single related synonym entry in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table reported no retired identifiers mapping to this taxon, and no retained old identifiers were present in the active NCBI row.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:58856` at line 39550 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 12 type-material rows for the target: `CBS 273.78`, `CBS:273.78`, `BPI 748209`, `BPI:748209`, `CBS H-18863`, `CBS:H:18863`, `CBS 274.78`, `CBS 275.78`, `CBS:274.78`, `CBS:275.78`, `IMI 287526`, and `IMI:287526`. The raw StrainInfo JSONL contains 28 exact direct records and 37 exact deposit rows for `NCBITaxon:58856`, including one non-direct `Trichoderma harzianum` record carrying one exact deposit for the target; BacDive contributed 0 exact rows.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target, so the exact raw StrainInfo side inventory has not been materialized as local child strain records.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material support, raw StrainInfo side evidence, and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
