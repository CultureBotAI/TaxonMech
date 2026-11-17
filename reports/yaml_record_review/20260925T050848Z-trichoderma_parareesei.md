# YAML Record Review: Trichoderma parareesei

- Verdict: pass
- Target: `data/taxa/eukaryota/trichoderma_parareesei.yaml`
- Identifier: `NCBITaxon:858221`

## Target

Reviewed the complete 84-line YAML record for Trichoderma parareesei. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichoderma_parareesei.

## Validation

- `just validate data/taxa/eukaryota/trichoderma_parareesei.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichoderma_orientale.yaml data/taxa/eukaryota/trichoderma_ovalisporum.yaml data/taxa/eukaryota/trichoderma_parapiluliferum.yaml data/taxa/eukaryota/trichoderma_parareesei.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 180399 retains `NCBITaxon:858221` as `Trichoderma parareesei`, rank `SPECIES`, parent `NCBITaxon:5543`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:858221` at line 56733, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 2 related synonyms, matching the two related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:858221` at line 43285 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 12 type-material rows for the target: `ATCC MYA-4777`, `ATCC:MYA-4777`, `ATCC:MYA:4777`, `CBS 125925`, `CBS:125925`, `WU 30015`, `WU:30015`, `NY 01048452`, `NY:01048452`, `C.P.K. 717`, `TUB F-1066`, and `TUB:F:1066`. BacDive and StrainInfo contributed 0 exact direct or deposit rows for `NCBITaxon:858221`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with type-material and native GOLD support and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
