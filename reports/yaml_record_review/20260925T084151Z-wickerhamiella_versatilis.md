# YAML Record Review: Wickerhamiella versatilis

- Verdict: pass
- Target: `data/taxa/eukaryota/wickerhamiella_versatilis.yaml`
- Identifier: `NCBITaxon:27304`

## Target

Reviewed the complete 101-line YAML record for Wickerhamiella versatilis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for wickerhamiella_versatilis.

## Validation

- `just validate data/taxa/eukaryota/wickerhamiella_versatilis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/wickerhamiella_sorbophila.yaml data/taxa/eukaryota/wickerhamiella_spandovensis.yaml data/taxa/eukaryota/wickerhamiella_vanderwaltii.yaml data/taxa/eukaryota/wickerhamiella_versatilis.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 2719 retains `NCBITaxon:27304` as `Wickerhamiella versatilis`, rank `SPECIES`, parent `NCBITaxon:45787`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:27304` at line 52142, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 5 exact, 0 broad, and 5 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table has no retained old identifiers for this target.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:27304` at line 25424 with `organism_count` 13, matching the YAML GOLD assertion count. The native GOLD tables contained 2 analyses, 13 organism rows, and 3 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 27 type-material rows for the target at lines 114767 through 114793. BacDive contributed 0 exact rows; StrainInfo contributed 48 exact direct rows and 150 exact deposit rows for `NCBITaxon:27304`, with one target deposit carried by a non-target `Starmerella etchellsii` direct StrainInfo record.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with the largest exact StrainInfo support in this Wickerhamiella run, exact NCBI type-material support, and no generated raw strain-table rows pending YAML incorporation.
