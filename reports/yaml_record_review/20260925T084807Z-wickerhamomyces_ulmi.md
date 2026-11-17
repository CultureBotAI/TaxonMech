# YAML Record Review: Wickerhamomyces ulmi

- Verdict: pass
- Target: `data/taxa/eukaryota/wickerhamomyces_ulmi.yaml`
- Identifier: `NCBITaxon:130815`

## Target

Reviewed the complete 79-line YAML record for Wickerhamomyces ulmi. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for wickerhamomyces_ulmi.

## Validation

- `just validate data/taxa/eukaryota/wickerhamomyces_ulmi.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/wickerhamomyces_kurtzmanii.yaml data/taxa/eukaryota/wickerhamomyces_quercuum.yaml data/taxa/eukaryota/wickerhamomyces_silvicola.yaml data/taxa/eukaryota/wickerhamomyces_ulmi.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 25098 retains `NCBITaxon:130815` as `Wickerhamomyces ulmi`, rank `SPECIES`, parent `NCBITaxon:599737`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:130815` at line 53936, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:130815` at line 7550 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 7 type-material rows for the target at lines 21570 through 21576. BacDive contributed 0 exact rows; StrainInfo contributed 3 exact direct rows and 9 exact deposit rows for `NCBITaxon:130815`, with all target deposits carried by exact direct StrainInfo records.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material and StrainInfo support, and no generated raw strain-table rows pending YAML incorporation.
