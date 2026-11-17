# YAML Record Review: Wenyingozyma succiphila

- Verdict: pass
- Target: `data/taxa/eukaryota/wenyingozyma_succiphila.yaml`
- Identifier: `NCBITaxon:51927`

## Target

Reviewed the complete 85-line YAML record for Wenyingozyma succiphila. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for wenyingozyma_succiphila.

## Validation

- `just validate data/taxa/eukaryota/wenyingozyma_succiphila.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/wenyingozyma_nanaspora.yaml data/taxa/eukaryota/wenyingozyma_nitratophila.yaml data/taxa/eukaryota/wenyingozyma_ramenticola.yaml data/taxa/eukaryota/wenyingozyma_succiphila.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 6535 retains `NCBITaxon:51927` as `Wenyingozyma succiphila`, rank `SPECIES`, parent `NCBITaxon:3712563`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:51927` at line 52852, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 2 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table retains old identifier `NCBITaxon:58623` for this current target at line 87700.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:51927` at line 37693 with `organism_count` 10, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 10 organism rows, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 26 type-material rows for the target at lines 227318 through 227343. BacDive contributed 0 exact rows; StrainInfo contributed 13 exact direct rows and 41 exact deposit rows for `NCBITaxon:51927`, including 1 target deposit on 1 non-direct StrainInfo row.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support plus a single retained NCBI old identifier already reconciled to the current target.
