# YAML Record Review: Tortispora sangerardonensis

- Verdict: pass
- Target: `data/taxa/eukaryota/tortispora_sangerardonensis.yaml`
- Identifier: `NCBITaxon:1326890`

## Target
Reviewed the complete 75-line YAML record for Tortispora sangerardonensis. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `tortispora_sangerardonensis`.

## Validation
- `just validate data/taxa/eukaryota/tortispora_sangerardonensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/tortispora_mauiana.yaml data/taxa/eukaryota/tortispora_phaffii.yaml data/taxa/eukaryota/tortispora_sangerardonensis.yaml data/taxa/eukaryota/tortispora_starmeri.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 316539 retained `NCBITaxon:1326890` as `Tortispora sangerardonensis` at rank `SPECIES`, with parent `NCBITaxon:1540147`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:1326890` on line 59485.
- The NCBI synonym columns supplied 0 exact synonyms, 0 broad synonyms, and 2 related synonyms.
- All 13 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:1326890`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:1326890` on line 7957, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 0 analysis rows, 1 organism row, and 1 project row for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 7 exact rows for `NCBITaxon:1326890`: `CBS 12795`, `CBS:12795`, `NRRL Y-63663`, `NRRL:Y-63663`, `NRRL:Y:63663`, `UWOPS 00-157.1`, and `UWOPS:00-157.1`.
- BacDive and StrainInfo exact scans found 0 matching rows.

## Completeness
- Generated strain tables had 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables had 0 target rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlays had 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
No YAML edits were made; this report records the read-only evidence review.
