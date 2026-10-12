# YAML Record Review: Triangularia tetraspora

- Verdict: pass
- Target: `data/taxa/eukaryota/triangularia_tetraspora.yaml`
- Identifier: `NCBITaxon:330532`

## Target
Reviewed the complete 94-line YAML record for Triangularia tetraspora. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `triangularia_tetraspora`.

## Validation
- `just validate data/taxa/eukaryota/triangularia_tetraspora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/triangularia_tetraspora.yaml data/taxa/eukaryota/triangularia_verruculosa.yaml data/taxa/eukaryota/tribonema_aequale.yaml data/taxa/eukaryota/tribonema_minus.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 67556 retained `NCBITaxon:330532` as `Triangularia tetraspora` at rank `SPECIES`, with parent `NCBITaxon:252192`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:330532` on line 55250.
- The NCBI synonym columns supplied 2 exact synonyms, 0 broad synonyms, and 3 related synonyms.
- All 16 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:330532`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:330532` on line 32293, matching the YAML aggregate with `organism_count` 1.
- Native GOLD carried 0 analysis rows, 1 organism row, and 2 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 0 exact rows for `NCBITaxon:330532`.
- BacDive found 0 exact rows. StrainInfo found 9 direct strain rows and 11 deposit rows under `NCBITaxon:330532`, with all 9 compressed JSONL rows assigned directly to the target taxon.

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
