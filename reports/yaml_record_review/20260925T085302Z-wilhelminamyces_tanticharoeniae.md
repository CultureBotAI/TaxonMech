# YAML Record Review: Wilhelminamyces tanticharoeniae

- Verdict: pass
- Target: `data/taxa/eukaryota/wilhelminamyces_tanticharoeniae.yaml`
- Identifier: `NCBITaxon:1215685`

## Target

Reviewed the complete 83-line YAML record for Wilhelminamyces tanticharoeniae. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for wilhelminamyces_tanticharoeniae.

## Validation

- `just validate data/taxa/eukaryota/wilhelminamyces_tanticharoeniae.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/wilcoxina_mikolae.yaml data/taxa/eukaryota/wilhelminamyces_savonicus.yaml data/taxa/eukaryota/wilhelminamyces_tanticharoeniae.yaml data/taxa/eukaryota/willaertia_magna.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 275113 retains `NCBITaxon:1215685` as `Wilhelminamyces tanticharoeniae`, rank `SPECIES`, parent `NCBITaxon:3315612`, genetic code `12`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1215685` at line 58436, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 1 exact, 0 broad, and 3 related synonyms, matching the YAML synonym entries. All 13 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps one old identifier, `NCBITaxon:374319`, into this retained target, and the YAML keeps only `NCBITaxon:1215685`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1215685` at line 5136 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 1 project for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found 10 type-material rows for the target at lines 14329 through 14338. BacDive contributed 0 exact rows, and StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:1215685`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/madin_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a compact retained NCBITaxon and GOLD seed with exact NCBI type-material support, and no generated raw strain-table rows pending YAML incorporation.
