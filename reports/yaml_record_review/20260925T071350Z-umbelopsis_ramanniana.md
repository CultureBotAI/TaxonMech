# YAML Record Review: Umbelopsis ramanniana

- Verdict: pass
- Target: `data/taxa/eukaryota/umbelopsis_ramanniana.yaml`
- Identifier: `NCBITaxon:41833`

## Target

Reviewed the complete 99-line YAML record for Umbelopsis ramanniana. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for umbelopsis_ramanniana.

## Validation

- `just validate data/taxa/eukaryota/umbelopsis_ramanniana.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/umbelopsis_dimorpha.yaml data/taxa/eukaryota/umbelopsis_isabellina.yaml data/taxa/eukaryota/umbelopsis_ovata.yaml data/taxa/eukaryota/umbelopsis_ramanniana.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 4888 retains `NCBITaxon:41833` as `Umbelopsis ramanniana`, rank `SPECIES`, parent `NCBITaxon:64561`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:41833` at line 52500, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 7 exact, 0 broad, and 4 related synonyms, matching the YAML synonym entries. All 12 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps 4 old identifiers into this target at lines 86232, 90135, 100210, and 100221, and an exact scan of the retained NCBITaxon rows found only the current `NCBITaxon:41833`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:41833` at line 34967 with `organism_count` 6, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 6 organism rows, and 9 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 0 type-material rows for the target. BacDive contributed 0 exact rows; StrainInfo contributed 87 exact direct rows and 105 exact deposit rows for `NCBITaxon:41833`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with a large exact StrainInfo footprint and four retired NCBI identifiers resolved into the current target, so the YAML accurately reflects the evidence available for the target identifier.
