# YAML Record Review: Toxicocladosporium irritans

- Verdict: pass
- Target: `data/taxa/eukaryota/toxicocladosporium_irritans.yaml`
- Identifier: `NCBITaxon:470064`

## Target
Reviewed the complete 84-line YAML record for Toxicocladosporium irritans. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `toxicocladosporium_irritans`.

## Validation
- `just validate data/taxa/eukaryota/toxicocladosporium_irritans.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/toxicocladosporium_irritans.yaml data/taxa/eukaryota/toxoplasma_gondii.yaml data/taxa/eukaryota/toxoplasma_gondii_guy_dos.yaml data/taxa/eukaryota/toxoplasma_gondii_guy_mat.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 104929 retained `NCBITaxon:470064` as `Toxicocladosporium irritans` at rank `SPECIES`, with parent `NCBITaxon:470063`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:470064` on line 55762.
- The NCBI synonym columns supplied 0 exact synonyms, 0 broad synonyms, and 2 related synonyms.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:1635019` occurred only as an old identifier merged into `NCBITaxon:470064` in `data/raw/ncbi_merged_ids.tsv`, and it was not retained as a live YAML identifier.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:470064` on line 36409, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 1 analysis row, 1 organism row, and 1 project row for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 2 exact rows for `NCBITaxon:470064`: `CBS 185.58` and `CBS:185.58`.
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
