# YAML Record Review: Williopsis sargentensis

- Verdict: pass
- Target: `data/taxa/eukaryota/williopsis_sargentensis.yaml`
- Identifier: `NCBITaxon:907339`

## Target

Reviewed the complete 91-line YAML record for Williopsis sargentensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for williopsis_sargentensis.

## Validation

- `just validate data/taxa/eukaryota/williopsis_sargentensis.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/williopsis_misumaiensis.yaml data/taxa/eukaryota/williopsis_samutprakarnensis.yaml data/taxa/eukaryota/williopsis_sargentensis.yaml data/taxa/eukaryota/williopsis_saturnus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 191055 retains `NCBITaxon:907339` as `Williopsis sargentensis`, rank `SPECIES`, parent `NCBITaxon:4962`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:907339` at line 56872, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 4 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps one old identifier, `NCBITaxon:58639`, into this retained target, and the YAML keeps only `NCBITaxon:907339`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:907339` at line 44261 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 25 type-material rows for the target at lines 272117 through 272141. BacDive contributed 0 exact rows; StrainInfo contributed 0 exact direct rows and 6 exact deposit rows for `NCBITaxon:907339`, all carried by one exact `NCBITaxon:907340` StrainInfo record.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact retained NCBITaxon and GOLD seed with exact NCBI type-material support, and its StrainInfo deposits were present only on a different exact direct StrainInfo taxon.
