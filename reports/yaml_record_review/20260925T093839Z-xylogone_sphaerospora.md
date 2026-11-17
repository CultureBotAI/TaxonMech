# YAML Record Review: Xylogone sphaerospora

- Verdict: pass
- Target: `data/taxa/eukaryota/xylogone_sphaerospora.yaml`
- Identifier: `NCBITaxon:756024`

## Target

Reviewed the complete 81-line YAML record for Xylogone sphaerospora. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for xylogone_sphaerospora.

## Validation

- `just validate data/taxa/eukaryota/xylogone_sphaerospora.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/xylodon_sp_omc1960.yaml data/taxa/eukaryota/xylogone_sphaerospora.yaml data/taxa/eukaryota/yamadazyma_akitaensis.yaml data/taxa/eukaryota/yamadazyma_andamanensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 175141 retains `NCBITaxon:756024` as `Xylogone sphaerospora`, rank `SPECIES`, parent `NCBITaxon:756023`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:756024` at line 56661, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 14 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps old `NCBITaxon:1028709` to this target at line 802, and an ignored-file-inclusive exact scan found no retained current NCBITaxon row for that old identifier.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:756024` at line 42383 with `organism_count` 4, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 4 organism rows, and 0 projects for this identifier. `data/raw/ncbi_type_material.tsv` contained 10 type-material rows: 4 culture-from-holotype aliases for `ATCC 34392` and `CBS 186.69`, plus 6 type-material aliases for `DSM 2684`, `IMI 212121`, and `MUCL 11833`. BacDive contributed 0 exact rows, and StrainInfo contributed 8 exact direct rows and 17 exact deposit rows for `NCBITaxon:756024`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with no generated raw strain-table rows pending YAML incorporation.
