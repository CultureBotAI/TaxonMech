# YAML Record Review: Trametes punicea

- Verdict: pass
- Target: `data/taxa/eukaryota/trametes_punicea.yaml`
- Identifier: `NCBITaxon:571087`

## Target
Reviewed the complete 78-line YAML record for Trametes punicea. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trametes_punicea`.

## Validation
- `just validate data/taxa/eukaryota/trametes_punicea.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trametes_punicea.yaml data/taxa/eukaryota/trametes_sanguinea.yaml data/taxa/eukaryota/trametes_versicolor.yaml data/taxa/eukaryota/trametes_villosa.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 134698 retained `NCBITaxon:571087` as `Trametes punicea` at rank `SPECIES`, with parent `NCBITaxon:5324`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:571087` on line 56069.
- The NCBI synonym columns supplied 1 exact synonym, 0 broad synonyms, and 2 related synonyms.
- All 13 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- No merged-ID rows were retained for `NCBITaxon:571087`.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:571087` on line 39140, matching the YAML aggregate with `organism_count` 4.
- Native GOLD carried 0 analysis rows, 1 organism row, and 15 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 0 exact rows for `NCBITaxon:571087`.
- BacDive found 0 exact rows. StrainInfo found 5 direct strain rows and 5 deposit rows under `NCBITaxon:571087`, with all 5 compressed JSONL rows assigned directly to the target taxon.

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
