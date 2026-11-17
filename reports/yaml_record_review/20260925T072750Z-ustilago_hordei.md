# YAML Record Review: Ustilago hordei

- Verdict: pass
- Target: `data/taxa/eukaryota/ustilago_hordei.yaml`
- Identifier: `NCBITaxon:120017`

## Target

Reviewed the complete 81-line YAML record for Ustilago hordei. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for ustilago_hordei.

## Validation

- `just validate data/taxa/eukaryota/ustilago_hordei.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/ustilago_hordei.yaml data/taxa/eukaryota/ustilago_sp_ug_2017a.yaml data/taxa/eukaryota/ustilago_sp_ug_2017b.yaml data/taxa/eukaryota/ustilago_trichophora.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 22478 retains `NCBITaxon:120017` as `Ustilago hordei`, rank `SPECIES`, parent `NCBITaxon:5269`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:120017` at line 53853, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 3 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 12 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps 6 old identifiers into this target at lines 6217, 6219, 7354, 7426, 84720, and 97152, with no old identifiers retained as current NCBITaxon rows.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:120017` at line 4817 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 2 organism rows, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 0 type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 21 exact direct rows and 22 exact deposit rows for `NCBITaxon:120017`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact StrainInfo support and six retired NCBI identifiers resolved into the current target, so the YAML accurately reflects the evidence available for the target identifier.
