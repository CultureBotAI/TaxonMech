# YAML Record Review: Xylaria cf. heliscus

- Verdict: pass
- Target: `data/taxa/eukaryota/xylaria_cf_heliscus.yaml`
- Identifier: `NCBITaxon:1803070`

## Target

Reviewed the complete 102-line YAML record for Xylaria cf. heliscus. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for xylaria_cf_heliscus.

## Validation

- `just validate data/taxa/eukaryota/xylaria_cf_heliscus.yaml` exited 0 and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/xylaria_berteroi.yaml data/taxa/eukaryota/xylaria_brunneovinosa.yaml data/taxa/eukaryota/xylaria_castorea.yaml data/taxa/eukaryota/xylaria_cf_heliscus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding

NCBI row 470747 retains `NCBITaxon:1803070` as `Xylaria cf. heliscus`, rank `SPECIES`, parent `NCBITaxon:37991`, genetic code `1`, with taxonomy snapshot `2026-09-13`. The seed-scope index contains exactly one in-scope row for `NCBITaxon:1803070` at line 61269, matching the YAML `SEEDED` mapping and `EXACT` grounding. NCBI contributes 0 exact, 0 broad, and 8 related synonyms, matching the YAML synonym entries. All 16 YAML lineage entries were checked against NCBITaxon with no missing entries and no mismatches. The NCBI merged-ID table maps eight old identifiers, `NCBITaxon:1180893`, `NCBITaxon:1180943`, `NCBITaxon:1181007`, `NCBITaxon:1181011`, `NCBITaxon:1181025`, `NCBITaxon:1181078`, `NCBITaxon:1181090`, and `NCBITaxon:1181099`, into this retained target, and the YAML keeps only `NCBITaxon:1803070`.

## Evidence

The generated GOLD aggregate contains exactly one row for `NCBITaxon:1803070` at line 15813 with `organism_count` 1, matching the YAML GOLD assertion count. The native GOLD tables contained 0 analyses, 1 organism row, and 2 projects for this identifier. A tab-anchored exact scan of `data/raw/ncbi_type_material.tsv` found no type-material rows for the target. BacDive contributed 0 exact rows, and StrainInfo contributed 0 exact direct rows and 0 exact deposit rows for `NCBITaxon:1803070`.

## Completeness

The generated raw strain tables `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv` each contained 0 target rows, matching `strain_count: 0`. The auxiliary source tables `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv` also contained 0 target rows. Generated StrainInfo overlays in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz` contained 0 rows for the target.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The record is a retained NCBITaxon and GOLD seed with no generated raw strain-table rows pending YAML incorporation, and the eight old NCBI identifiers correctly remain out of the YAML identifier set.
