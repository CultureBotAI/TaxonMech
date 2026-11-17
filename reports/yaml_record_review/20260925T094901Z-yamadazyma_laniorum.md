# YAML Record Review: Yamadazyma laniorum

- Verdict: pass
- Target: `data/taxa/eukaryota/yamadazyma_laniorum.yaml`
- Identifier: `NCBITaxon:1944661`

## Target

Reviewed the complete 80-line YAML record for Yamadazyma laniorum. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yamadazyma_laniorum.

## Validation

- `just validate data/taxa/eukaryota/yamadazyma_laniorum.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/yamadazyma_laniorum.yaml data/taxa/eukaryota/yamadazyma_mexicana.yaml data/taxa/eukaryota/yamadazyma_nakazawae.yaml data/taxa/eukaryota/yamadazyma_oceani.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 498102 retains `NCBITaxon:1944661` as `Yamadazyma laniorum`, rank `SPECIES`, parent `NCBITaxon:766765`, genetic code `12`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1944661` at line 61703, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1944661` at line 17890 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 1 analysis, 1 organism row, and 1 project for this identifier. `data/raw/ncbi_type_material.tsv` contained 3 holotype rows for `NRRL Y-63967` variants. BacDive contributed 0 exact rows, and StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:1944661`.

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
