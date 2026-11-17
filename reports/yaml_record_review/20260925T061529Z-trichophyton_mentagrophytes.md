# YAML Record Review: Trichophyton mentagrophytes

- Verdict: pass
- Target: `data/taxa/eukaryota/trichophyton_mentagrophytes.yaml`
- Identifier: `NCBITaxon:523103`

## Target

Reviewed the complete 120-line YAML record for Trichophyton mentagrophytes. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for trichophyton_mentagrophytes.

## Validation

- `just validate data/taxa/eukaryota/trichophyton_mentagrophytes.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichophyton_interdigitale_h6.yaml data/taxa/eukaryota/trichophyton_mentagrophytes.yaml data/taxa/eukaryota/trichophyton_rubrum.yaml data/taxa/eukaryota/trichophyton_rubrum_cbs_100081.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 119416 retains `NCBITaxon:523103` as `Trichophyton mentagrophytes`, rank `SPECIES`, parent `NCBITaxon:5550`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:523103` at line 55886, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 11 exact, 0 broad, and 4 related synonyms, matching the eleven exact and four related synonym entries in YAML. All 15 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps five historical identifiers, `NCBITaxon:3478194`, `NCBITaxon:3478195`, `NCBITaxon:3478196`, `NCBITaxon:3478197`, and `NCBITaxon:63407`, into this target; an exact ignored-file-inclusive scan found no retained current rows for those old identifiers in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:523103` at line 37848 with `organism_count` 2, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 15 type-material rows for the target at lines 228073 through 228087. BacDive contributed 0 exact rows; StrainInfo contributed 417 exact direct rows and 495 exact deposit rows for `NCBITaxon:523103`.

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
