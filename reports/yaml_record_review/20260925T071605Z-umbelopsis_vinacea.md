# YAML Record Review: Umbelopsis vinacea

- Verdict: pass
- Target: `data/taxa/eukaryota/umbelopsis_vinacea.yaml`
- Identifier: `NCBITaxon:44442`

## Target

Reviewed the complete 81-line YAML record for Umbelopsis vinacea. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for umbelopsis_vinacea.

## Validation

- `just validate data/taxa/eukaryota/umbelopsis_vinacea.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/umbelopsis_sp.yaml data/taxa/eukaryota/umbelopsis_sp_tlt204.yaml data/taxa/eukaryota/umbelopsis_vinacea.yaml data/taxa/eukaryota/umbilicaria_hispanica.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 5392 retains `NCBITaxon:44442` as `Umbelopsis vinacea`, rank `SPECIES`, parent `NCBITaxon:64561`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:44442` at line 52588, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 2 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 12 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps 1 old identifier into this target at line 7289, and an exact scan of the retained NCBITaxon rows found only the current `NCBITaxon:44442`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:44442` at line 35667 with `organism_count` 3, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 3 organism rows, and 3 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 4 type-material rows for the target at lines 212504 through 212507. BacDive contributed 0 exact rows; StrainInfo contributed 28 exact direct rows and 33 exact deposit rows for `NCBITaxon:44442`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI epitype and StrainInfo support plus one retired NCBI identifier resolved into the current target, so the YAML accurately reflects the evidence available for the target identifier.
