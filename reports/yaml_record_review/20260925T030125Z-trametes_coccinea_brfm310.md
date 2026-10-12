# YAML Record Review: Trametes coccinea BRFM310

- Verdict: pass
- Target: `data/taxa/eukaryota/trametes_coccinea_brfm310.yaml`
- Identifier: `NCBITaxon:1353009`

## Target
Reviewed the complete 75-line YAML record for Trametes coccinea BRFM310. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trametes_coccinea_brfm310`.

## Validation
- `just validate data/taxa/eukaryota/trametes_coccinea_brfm310.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trametes_coccinea_brfm310.yaml data/taxa/eukaryota/trametes_elegans.yaml data/taxa/eukaryota/trametes_gibbosa.yaml data/taxa/eukaryota/trametes_hirsuta.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 326814 retained `NCBITaxon:1353009` as `Trametes coccinea BRFM310` at rank `STRAIN`, with parent `NCBITaxon:158605`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:1353009` on line 59625.
- The NCBI synonym columns supplied 1 exact synonym, 0 broad synonyms, and 0 related synonyms.
- All 14 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:1353009`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:1353009` on line 8553, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 0 analysis rows, 0 organism rows, and 0 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 0 exact rows for `NCBITaxon:1353009`.
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
