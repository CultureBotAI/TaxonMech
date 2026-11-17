# YAML Record Review: Torulaspora globosa

- Verdict: pass
- Target: `data/taxa/eukaryota/torulaspora_globosa.yaml`
- Identifier: `NCBITaxon:48254`

## Target
Reviewed the complete 81-line YAML record for Torulaspora globosa. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `torulaspora_globosa`.

## Validation
- `just validate data/taxa/eukaryota/torulaspora_globosa.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/torulaspora_delbrueckii.yaml data/taxa/eukaryota/torulaspora_franciscae.yaml data/taxa/eukaryota/torulaspora_gathmanii.yaml data/taxa/eukaryota/torulaspora_globosa.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 6141 retained `NCBITaxon:48254` as `Torulaspora globosa` at rank `SPECIES`, with parent `NCBITaxon:4948`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:48254` on line 52749.
- The NCBI synonym columns supplied 1 exact synonym, 0 broad synonyms, and 3 related synonyms.
- All 13 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:2792677` occurred only as an old identifier merged into `NCBITaxon:48254` in `data/raw/ncbi_merged_ids.tsv`, and it was not retained as a live YAML identifier.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:48254` on line 36791, matching the YAML aggregate with `organism_count` 2.
- Native GOLD carried 0 analysis rows, 1 organism row, and 1 project row for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 16 exact rows for `NCBITaxon:48254` across `BCRC:21649`, `CBS 764`, `CBS:764`, `CCRC 21649`, `CCRC:21649`, `DBVPG 6843`, `DBVPG:6843`, `IFO 1160`, `IFO:1160`, `NCYC 820`, `NCYC:820`, `NRRL Y-12650`, `NRRL:Y-12650`, `NRRL:Y:12650`, `UCD 68-37`, and `UCD:68-37`.
- BacDive found 0 exact rows. StrainInfo found 21 direct strain rows and 50 deposit rows under `NCBITaxon:48254`, with all 21 compressed JSONL rows assigned directly to the target taxon.

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
