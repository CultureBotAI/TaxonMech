# YAML Record Review: Wickerhamiella brachini

- Verdict: pass
- Target: `data/taxa/eukaryota/wickerhamiella_brachini.yaml`
- Identifier: `NCBITaxon:2859419`

## Target

Reviewed the complete 75-line YAML record for Wickerhamiella brachini. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for wickerhamiella_brachini.

## Validation

- `just validate data/taxa/eukaryota/wickerhamiella_brachini.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/wickerhamiella_bombiphila.yaml data/taxa/eukaryota/wickerhamiella_brachini.yaml data/taxa/eukaryota/wickerhamiella_cacticola.yaml data/taxa/eukaryota/wickerhamiella_domercqiae.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 565399 retains `NCBITaxon:2859419` as `Wickerhamiella brachini`, rank `SPECIES`, parent `NCBITaxon:45787`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:2859419` at line 63315, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 2 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps one historical old identifier, `NCBITaxon:1775922`, into this target, and no old identifier is retained in the YAML.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:2859419` at line 27757 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 10 type-material rows for the target at lines 133015 through 133024. BacDive contributed 0 exact rows; StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:2859419`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact NCBITaxon and GOLD seed with exact NCBI type-material support; no local BacDive, StrainInfo, or auxiliary bacterial-source evidence maps to this fungal species.
