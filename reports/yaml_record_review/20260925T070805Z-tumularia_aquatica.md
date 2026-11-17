# YAML Record Review: Tumularia aquatica

- Verdict: pass
- Target: `data/taxa/eukaryota/tumularia_aquatica.yaml`
- Identifier: `NCBITaxon:213314`

## Target

Reviewed the complete 81-line YAML record for Tumularia aquatica. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for tumularia_aquatica.

## Validation

- `just validate data/taxa/eukaryota/tumularia_aquatica.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tumularia_aquatica.yaml data/taxa/eukaryota/tylopilus_felleus.yaml data/taxa/eukaryota/tylopilus_plumbeoviolaceoides.yaml data/taxa/eukaryota/tylopilus_sp.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 42009 retains `NCBITaxon:213314` as `Tumularia aquatica`, rank `SPECIES`, parent `NCBITaxon:213313`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:213314` at line 54538, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 14 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:213314` at line 20273 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 0 organism rows, and 0 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 4 type-material rows for the target at lines 85279 through 85282. BacDive contributed 0 exact rows; StrainInfo contributed 2 exact direct rows and 4 exact deposit rows for `NCBITaxon:213314`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact StrainInfo and NCBI type-material support but no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
