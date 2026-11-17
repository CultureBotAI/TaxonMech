# YAML Record Review: Trametes hirsuta

- Verdict: pass
- Target: `data/taxa/eukaryota/trametes_hirsuta.yaml`
- Identifier: `NCBITaxon:5327`

## Target
Reviewed the complete 102-line YAML record for Trametes hirsuta. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `trametes_hirsuta`.

## Validation
- `just validate data/taxa/eukaryota/trametes_hirsuta.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/trametes_coccinea_brfm310.yaml data/taxa/eukaryota/trametes_elegans.yaml data/taxa/eukaryota/trametes_gibbosa.yaml data/taxa/eukaryota/trametes_hirsuta.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 2353 retained `NCBITaxon:5327` as `Trametes hirsuta` at rank `SPECIES`, with parent `NCBITaxon:5324`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:5327` on line 51970.
- The NCBI synonym columns supplied 7 exact synonyms, 0 broad synonyms, and 4 related synonyms.
- All 13 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:318040`, `NCBITaxon:659437`, and `NCBITaxon:76129` occurred only as old identifiers merged into `NCBITaxon:5327` in `data/raw/ncbi_merged_ids.tsv`, and none were retained as live YAML identifiers.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:5327` on line 38049, matching the YAML aggregate with `organism_count` 2.
- Native GOLD carried 1 analysis row, 1 organism row, and 1 project row for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 0 exact rows for `NCBITaxon:5327`.
- BacDive found 0 exact rows. StrainInfo found 66 direct strain rows and 86 deposit rows under `NCBITaxon:5327`, with all 66 compressed JSONL rows assigned directly to the target taxon.

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
