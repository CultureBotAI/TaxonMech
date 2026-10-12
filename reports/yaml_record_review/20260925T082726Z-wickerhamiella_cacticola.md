# YAML Record Review: Wickerhamiella cacticola

- Verdict: pass
- Target: `data/taxa/eukaryota/wickerhamiella_cacticola.yaml`
- Identifier: `NCBITaxon:75733`

## Target

Reviewed the complete 77-line YAML record for Wickerhamiella cacticola. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for wickerhamiella_cacticola.

## Validation

- `just validate data/taxa/eukaryota/wickerhamiella_cacticola.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/wickerhamiella_bombiphila.yaml data/taxa/eukaryota/wickerhamiella_brachini.yaml data/taxa/eukaryota/wickerhamiella_cacticola.yaml data/taxa/eukaryota/wickerhamiella_domercqiae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 10821 retains `NCBITaxon:75733` as `Wickerhamiella cacticola`, rank `SPECIES`, parent `NCBITaxon:45787`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:75733` at line 53281, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:75733` at line 42408 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 2 analyses, 1 organism row, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 9 type-material rows for the target at lines 262567 through 262575. BacDive contributed 0 exact rows; StrainInfo contributed 2 exact direct rows and 6 exact deposit rows for `NCBITaxon:75733`, with all target deposits carried by exact direct StrainInfo records.

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
