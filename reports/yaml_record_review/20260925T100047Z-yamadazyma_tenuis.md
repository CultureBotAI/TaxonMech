# YAML Record Review: Yamadazyma tenuis

- Verdict: pass
- Target: `data/taxa/eukaryota/yamadazyma_tenuis.yaml`
- Identifier: `NCBITaxon:2315449`

## Target

Reviewed the complete 82-line YAML record for Yamadazyma tenuis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for yamadazyma_tenuis.

## Validation

- `just validate data/taxa/eukaryota/yamadazyma_tenuis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/yamadazyma_tenuis.yaml data/taxa/eukaryota/yamadazyma_triangularis.yaml data/taxa/eukaryota/yamadazyma_tumulicola.yaml data/taxa/eukaryota/yamadazyma_ubonensis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 524742 retains `NCBITaxon:2315449` as `Yamadazyma tenuis`, rank `SPECIES`, parent `NCBITaxon:766765`, genetic code `12`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:2315449` at line 62553, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps old `NCBITaxon:45596` and `NCBITaxon:533344` to this target at lines 79033 and 85044; an ignored-file-inclusive exact scan found no retained current NCBITaxon rows for those old identifiers.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:2315449` at line 21685 with `organism_count` 6, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 6 organism rows, and 1 project for this identifier. `data/raw/ncbi_type_material.tsv` contained 19 type-material rows for ATCC, BCRC/CCRC, CBS, DBVPG, IFO, JCM, NRRL, and VKM designations of `Candida tenuis`. BacDive contributed 0 exact rows, and StrainInfo contributed 24 exact direct rows and 73 exact deposit rows for `NCBITaxon:2315449`.

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
