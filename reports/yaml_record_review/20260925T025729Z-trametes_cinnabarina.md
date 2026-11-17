# YAML Record Review: Trametes cinnabarina

- Verdict: pass
- Target: `data/taxa/eukaryota/trametes_cinnabarina.yaml`
- Identifier: `NCBITaxon:5643`

## Target
Reviewed the complete 84-line YAML record for Trametes cinnabarina. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trametes_cinnabarina`.

## Validation
- `just validate data/taxa/eukaryota/trametes_cinnabarina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/toxoplasma_gondii_tgckgy2.yaml data/taxa/eukaryota/trametes_cingulata.yaml data/taxa/eukaryota/trametes_cinnabarina.yaml data/taxa/eukaryota/trametes_coccinea.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 2511 retained `NCBITaxon:5643` as `Trametes cinnabarina` at rank `SPECIES`, with parent `NCBITaxon:5324`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:5643` on line 52052.
- The NCBI synonym columns supplied 2 exact synonyms, 0 broad synonyms, and 3 related synonyms.
- All 13 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:5643`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:5643` on line 38928, matching the YAML aggregate with `organism_count` 6.
- Native GOLD carried 1 analysis row, 3 organism rows, and 31 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 0 exact rows for `NCBITaxon:5643`.
- BacDive found 0 exact rows. StrainInfo found 43 direct strain rows and 67 deposit rows under `NCBITaxon:5643`; the compressed JSONL contained one additional non-target `Trametes coccinea` strain record with one deposit under `NCBITaxon:5643`.

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
