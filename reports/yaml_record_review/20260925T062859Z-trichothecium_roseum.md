# YAML Record Review: Trichothecium roseum

- Verdict: pass
- Target: `data/taxa/eukaryota/trichothecium_roseum.yaml`
- Identifier: `NCBITaxon:47278`

## Target

Reviewed the complete 87-line YAML record for Trichothecium roseum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichothecium_roseum.

## Validation

- `just validate data/taxa/eukaryota/trichothecium_roseum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichothecium_roseum.yaml data/taxa/eukaryota/trichothecium_sp.yaml data/taxa/eukaryota/trichothecium_sympodiale.yaml data/taxa/eukaryota/tricladium_chaetocladium.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 5954 retains `NCBITaxon:47278` as `Trichothecium roseum`, rank `SPECIES`, parent `NCBITaxon:231006`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:47278` at line 52723, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the exact and two related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:47278` at line 36491 with `organism_count` 3, matching the YAML GOLD assertion count. The native GOLD tables contained 3 analyses, 3 organism rows, and 3 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 121 exact direct rows and 148 exact deposit rows for `NCBITaxon:47278`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays contained 0 rows for the target in `data/straininfo/assemblies.tsv` and `data/straininfo/exclusions.tsv`, while `data/straininfo/related_records.tsv.gz` contained 2 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact GOLD and NCBITaxon seed with exact StrainInfo support but no type-material support and no generated strain inventory, so the YAML accurately reflects the evidence available for the target identifier.
