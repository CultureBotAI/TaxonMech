# YAML Record Review: Vanderwaltozyma yarrowii

- Verdict: pass
- Target: `data/taxa/eukaryota/vanderwaltozyma_yarrowii.yaml`
- Identifier: `NCBITaxon:51620`

## Target

Reviewed the complete 78-line YAML record for Vanderwaltozyma yarrowii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for vanderwaltozyma_yarrowii.

## Validation

- `just validate data/taxa/eukaryota/vanderwaltozyma_yarrowii.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/vanderwaltozyma_verrucispora.yaml data/taxa/eukaryota/vanderwaltozyma_yarrowii.yaml data/taxa/eukaryota/vannella_robusta.yaml data/taxa/eukaryota/vanrija_humicola.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 6477 retains `NCBITaxon:51620` as `Vanderwaltozyma yarrowii`, rank `SPECIES`, parent `NCBITaxon:374469`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:51620` at line 52832, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:51620` at line 37618 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 11 type-material rows for the target at lines 226642 through 226652. BacDive contributed 0 exact rows; StrainInfo contributed 4 exact direct rows and 30 exact deposit rows for `NCBITaxon:51620`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support, so the YAML accurately reflects the evidence available for the target identifier.
