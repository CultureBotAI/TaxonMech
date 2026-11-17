# YAML Record Review: Trichothecium sympodiale

- Verdict: pass
- Target: `data/taxa/eukaryota/trichothecium_sympodiale.yaml`
- Identifier: `NCBITaxon:51912`

## Target

Reviewed the complete 87-line YAML record for Trichothecium sympodiale. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichothecium_sympodiale.

## Validation

- `just validate data/taxa/eukaryota/trichothecium_sympodiale.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichothecium_roseum.yaml data/taxa/eukaryota/trichothecium_sp.yaml data/taxa/eukaryota/trichothecium_sympodiale.yaml data/taxa/eukaryota/tricladium_chaetocladium.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 6522 retains `NCBITaxon:51912` as `Trichothecium sympodiale`, rank `SPECIES`, parent `NCBITaxon:231006`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:51912` at line 52839, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the exact and two related synonym entries in YAML. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:51912` at line 37680 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 8 type-material rows for the target at lines 227097 through 227104. BacDive contributed 0 exact rows; StrainInfo contributed 7 exact direct rows and 10 exact deposit rows for `NCBITaxon:51912`.

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
