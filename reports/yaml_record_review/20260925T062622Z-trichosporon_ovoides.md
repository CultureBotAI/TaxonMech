# YAML Record Review: Trichosporon ovoides

- Verdict: pass
- Target: `data/taxa/eukaryota/trichosporon_ovoides.yaml`
- Identifier: `NCBITaxon:82524`

## Target

Reviewed the complete 69-line YAML record for Trichosporon ovoides. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichosporon_ovoides.

## Validation

- `just validate data/taxa/eukaryota/trichosporon_ovoides.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichosporon_faecale.yaml data/taxa/eukaryota/trichosporon_inkin.yaml data/taxa/eukaryota/trichosporon_ovoides.yaml data/taxa/eukaryota/trichothecium_ovalisporum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 12388 retains `NCBITaxon:82524` as `Trichosporon ovoides`, rank `SPECIES`, parent `NCBITaxon:5552`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:82524` at line 53384, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 1 related synonym, matching the single related synonym entry in YAML. All 12 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:82524` at line 43001 with `organism_count` 5, matching the YAML GOLD assertion count. The native GOLD tables contained 5 analyses, 5 organism rows, and 6 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 2 culture-from-neotype rows for the target at lines 266247 and 266248. BacDive contributed 0 exact rows; StrainInfo contributed 12 exact direct rows and 27 exact deposit rows for `NCBITaxon:82524`.

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
