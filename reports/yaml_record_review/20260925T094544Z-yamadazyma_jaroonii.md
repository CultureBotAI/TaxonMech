# YAML Record Review: Yamadazyma jaroonii

- Verdict: pass
- Target: `data/taxa/eukaryota/yamadazyma_jaroonii.yaml`
- Identifier: `NCBITaxon:467808`

## Target

Reviewed the complete 98-line YAML record for Yamadazyma jaroonii. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yamadazyma_jaroonii.

## Validation

- `just validate data/taxa/eukaryota/yamadazyma_jaroonii.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/yamadazyma_epiphylla.yaml data/taxa/eukaryota/yamadazyma_insecticola.yaml data/taxa/eukaryota/yamadazyma_jaroonii.yaml data/taxa/eukaryota/yamadazyma_kitorensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 104585 retains `NCBITaxon:467808` as `Yamadazyma jaroonii`, rank `SPECIES`, parent `NCBITaxon:766765`, genetic code `12`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:467808` at line 55752, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 8 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps old `NCBITaxon:374314`, `NCBITaxon:374324`, `NCBITaxon:374325`, `NCBITaxon:423507`, and `NCBITaxon:423508` to this target at lines 73851, 73857, 73858, 77005, and 77006; an ignored-file-inclusive exact scan found no retained current NCBITaxon rows for those old identifiers.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:467808` at line 36356 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. `data/raw/ncbi_type_material.tsv` contained 9 rows, covering 5 culture-from-holotype aliases for `BCC 11783` and `NBRC 103209` plus 4 holotype aliases for `CBS 10790`. BacDive contributed 0 exact rows, and StrainInfo contributed 3 exact direct rows and 3 exact deposit rows for `NCBITaxon:467808`.

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
