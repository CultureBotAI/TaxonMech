# YAML Record Review: Trichodelitschia bisporula

- Verdict: pass
- Target: `data/taxa/eukaryota/trichodelitschia_bisporula.yaml`
- Identifier: `NCBITaxon:703511`

## Target
Reviewed the complete 87-line YAML record for Trichodelitschia bisporula. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trichodelitschia_bisporula`.

## Validation
- `just validate data/taxa/eukaryota/trichodelitschia_bisporula.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trichocoma_paradoxa.yaml data/taxa/eukaryota/trichocomaceae_sp_pys4502.yaml data/taxa/eukaryota/trichodelitschia_bisporula.yaml data/taxa/eukaryota/trichoderma_aethiopicum.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 165045 retained `NCBITaxon:703511` as `Trichodelitschia bisporula` at rank `SPECIES`, with parent `NCBITaxon:372047`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:703511` on line 56495.
- The NCBI synonym columns supplied 1 exact synonym, 0 broad synonyms, and 2 related synonyms.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:703511`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:703511` on line 41689, matching the YAML aggregate with `organism_count` 2.
- Native GOLD carried 0 analysis rows, 1 organism row, and 2 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 0 exact rows for `NCBITaxon:703511`.
- BacDive found 0 exact rows. StrainInfo found 1 direct strain row and 1 deposit row under `NCBITaxon:703511`, with the compressed JSONL row assigned directly to the target taxon.

## Completeness
- Generated strain tables had 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary source tables had 0 target rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlays had 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings
No findings.

## Recommended Edits
No edits are recommended.

## Follow-up Checks
No follow-up checks are required.

## Additional Notes
No YAML edits were made; this report records the read-only evidence review.
