# YAML Record Review: Torulaspora microellipsoides

- Verdict: pass
- Target: `data/taxa/eukaryota/torulaspora_microellipsoides.yaml`
- Identifier: `NCBITaxon:1136883`

## Target
Reviewed the complete 81-line YAML record for Torulaspora microellipsoides. The final ignored-file-inclusive preflight of reports/yaml_record_review found no existing or parallel report for `torulaspora_microellipsoides`.

## Validation
- `just validate data/taxa/eukaryota/torulaspora_microellipsoides.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/torulaspora_maleeae.yaml data/taxa/eukaryota/torulaspora_microellipsoides.yaml data/taxa/eukaryota/torulaspora_pretoriensis.yaml data/taxa/eukaryota/tothia_fuscella.yaml` scanned all four files and reported 0 files with ERROR and 0 total ERROR rows.

## Identity and Grounding
- NCBI taxa line 247208 retained `NCBITaxon:1136883` as `Torulaspora microellipsoides` at rank `SPECIES`, with parent `NCBITaxon:4948`, genetic code `1`, and taxonomy snapshot `2026-09-13`.
- The seed-scope table contained exactly one row for `NCBITaxon:1136883` on line 57882.
- The NCBI synonym columns supplied 2 exact synonyms, 0 broad synonyms, and 2 related synonyms.
- All 13 lineage identifiers were checked against the NCBI snapshot with 0 missing ancestors and 0 mismatches.
- `NCBITaxon:42259` occurred only as an old identifier merged into `NCBITaxon:1136883` in `data/raw/ncbi_merged_ids.tsv`, and it was not retained as a live YAML identifier.

## Evidence
- The GOLD aggregate table contained exactly one row for `NCBITaxon:1136883` on line 2804, matching the YAML aggregate with `organism_count` 10.
- Native GOLD carried 2 analysis rows, 10 organism rows, and 2 project rows for this taxon.
- `data/raw/ncbi_type_material.tsv` contained 21 exact rows for `NCBITaxon:1136883` across ATCC, BCRC, CBS, CCRC, DBVPG, IFO, NCYC, NRRL, UCD, and VKM spellings of the type material.
- BacDive found 0 exact rows. StrainInfo found 16 direct strain rows and 47 deposit rows under `NCBITaxon:1136883`; the compressed JSONL contained one additional non-target `Sakaguchia dacryoidea` strain record with two deposits under `NCBITaxon:1136883`.

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
