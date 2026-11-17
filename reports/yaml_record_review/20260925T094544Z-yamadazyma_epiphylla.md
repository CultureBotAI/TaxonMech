# YAML Record Review: Yamadazyma epiphylla

- Verdict: pass
- Target: `data/taxa/eukaryota/yamadazyma_epiphylla.yaml`
- Identifier: `NCBITaxon:1562958`

## Target

Reviewed the complete 75-line YAML record for Yamadazyma epiphylla. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yamadazyma_epiphylla.

## Validation

- `just validate data/taxa/eukaryota/yamadazyma_epiphylla.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/yamadazyma_epiphylla.yaml data/taxa/eukaryota/yamadazyma_insecticola.yaml data/taxa/eukaryota/yamadazyma_jaroonii.yaml data/taxa/eukaryota/yamadazyma_kitorensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 401783 retains `NCBITaxon:1562958` as `Yamadazyma epiphylla`, rank `SPECIES`, parent `NCBITaxon:766765`, genetic code `12`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1562958` at line 60469, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1562958` at line 12525 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. `data/raw/ncbi_type_material.tsv` contained 9 rows, covering 7 culture-from-holotype aliases for `BCC 6346`, `CBS 13384`, and `NBRC 11042` plus 2 holotype aliases for `YE170`. BacDive contributed 0 exact rows, and StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:1562958`.

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
