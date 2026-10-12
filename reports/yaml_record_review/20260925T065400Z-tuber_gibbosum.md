# YAML Record Review: Tuber gibbosum

- Verdict: pass
- Target: `data/taxa/eukaryota/tuber_gibbosum.yaml`
- Identifier: `NCBITaxon:44634`

## Target

Reviewed the complete 71-line YAML record for Tuber gibbosum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tuber_gibbosum.

## Validation

- `just validate data/taxa/eukaryota/tuber_gibbosum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tuber_canaliculatum.yaml data/taxa/eukaryota/tuber_gibbosum.yaml data/taxa/eukaryota/tuber_indicum.yaml data/taxa/eukaryota/tuber_magnatum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 5423 retains `NCBITaxon:44634` as `Tuber gibbosum`, rank `SPECIES`, parent `NCBITaxon:36048`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:44634` at line 52598, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 1 related synonym, matching the single related synonym entry in YAML. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:44634` at line 35728 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 2 type-material rows for the target at lines 212742 through 212743. BacDive contributed 0 exact rows; StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:44634`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with NCBI type-material support but no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
