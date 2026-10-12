# YAML Record Review: Yamadazyma andamanensis

- Verdict: pass
- Target: `data/taxa/eukaryota/yamadazyma_andamanensis.yaml`
- Identifier: `NCBITaxon:456249`

## Target

Reviewed the complete 88-line YAML record for Yamadazyma andamanensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yamadazyma_andamanensis.

## Validation

- `just validate data/taxa/eukaryota/yamadazyma_andamanensis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/xylodon_sp_omc1960.yaml data/taxa/eukaryota/xylogone_sphaerospora.yaml data/taxa/eukaryota/yamadazyma_akitaensis.yaml data/taxa/eukaryota/yamadazyma_andamanensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 102080 retains `NCBITaxon:456249` as `Yamadazyma andamanensis`, rank `SPECIES`, parent `NCBITaxon:2640732`, genetic code `12`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:456249` at line 55714, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 4 related synonyms, matching the YAML synonym entries. All 14 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps old `NCBITaxon:456250` to this target at line 79040, and an ignored-file-inclusive exact scan found no retained current NCBITaxon row for that old identifier.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:456249` at line 36102 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. `data/raw/ncbi_type_material.tsv` contained 4 holotype rows for the `CBS 10859`, `CBS-10859`, `CBS10859`, and `CBS:10859` variants. BacDive contributed 0 exact rows, and StrainInfo contributed 1 exact direct row and 1 exact deposit row for `NCBITaxon:456249`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed under unclassified Yamadazyma with no generated raw strain-table rows pending YAML incorporation.
