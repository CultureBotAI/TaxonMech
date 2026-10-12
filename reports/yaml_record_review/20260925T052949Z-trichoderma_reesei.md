# YAML Record Review: Trichoderma reesei

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_reesei.yaml`
- Identifier: `NCBITaxon:51453`

## Target

Reviewed the complete 87-line YAML record for Trichoderma reesei. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_reesei.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_reesei.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_pulvinatum.yaml data/taxa/eukaryota/trichoderma_pyramidale.yaml data/taxa/eukaryota/trichoderma_reesei.yaml data/taxa/eukaryota/trichoderma_rhododendri.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 6464 retains `NCBITaxon:51453` as `Trichoderma reesei`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:51453` at line 52829, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the three synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps retired `NCBITaxon:5546` to retained `NCBITaxon:51453`, and an exact tab-anchored lookup found the old identifier only in `data/raw/ncbi_merged_ids.tsv`, not in the active `data/raw/ncbitaxon_taxa.tsv` row set.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:51453` at line 37572 with `organism_count` 22, matching the YAML GOLD assertion count. The native GOLD tables contained 4 analyses, 21 organism rows, and 354 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 19 type-material rows for the target: `ATCC 13631`, `ATCC:13631`, `DAOM 167654`, `DAOM:167654`, `CBS 383.78`, `CBS:383.78`, `CCM F-560`, `CCM:F:560`, `DSM 768`, `DSM:768`, `IMI 192654`, `IMI:192654`, `QM 6a`, `QM:6a`, `VKM F-2047`, `VKM:F-2047`, `VKM:F:2047`, `VTT D-74083`, and `VTT:D:74083`. The raw StrainInfo JSONL contains 79 exact direct records and 189 exact deposit rows for `NCBITaxon:51453`; four non-direct rows, StrainInfo 107370, 107396, 146543, and 175963, also carry exact target deposits. BacDive contributed 0 exact rows.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target, so the exact raw StrainInfo side inventory has not been materialized as local child strain records.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with extensive native GOLD, type-material, and raw StrainInfo evidence, one retired NCBI identifier pointing into the retained target, and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
