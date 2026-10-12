# YAML Record Review: Tuber melosporum

- Verdict: pass
- Target: `data/taxa/eukaryota/tuber_melosporum.yaml`
- Identifier: `NCBITaxon:1258559`

## Target

Reviewed the complete 79-line YAML record for Tuber melosporum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tuber_melosporum.

## Validation

- `just validate data/taxa/eukaryota/tuber_melosporum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tuber_melanosporum.yaml data/taxa/eukaryota/tuber_melosporum.yaml data/taxa/eukaryota/tuber_mesentericum.yaml data/taxa/eukaryota/tuber_microsphaerosporum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 290305 retains `NCBITaxon:1258559` as `Tuber melosporum`, rank `SPECIES`, parent `NCBITaxon:36048`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1258559` at line 58783, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps `NCBITaxon:1150372` to this target, and an ignored-file-inclusive lookup found that old identifier only in `data/raw/ncbi_merged_ids.tsv`, not retained in current NCBI rows.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1258559` at line 6111 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 2 type-material rows for the target at lines 17192 through 17193. BacDive contributed 0 exact rows; StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:1258559`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with NCBI type-material support and one safely merged historical NCBI identifier but no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
