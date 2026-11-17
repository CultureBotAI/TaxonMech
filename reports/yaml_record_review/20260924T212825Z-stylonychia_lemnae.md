# YAML Record Review: Stylonychia lemnae

- Verdict: pass
- Target: `data/taxa/eukaryota/stylonychia_lemnae.yaml`
- Identifier: `NCBITaxon:5949`

## Target

Reviewed the complete 72-line YAML record for Stylonychia lemnae. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stylonychia_lemnae`.

## Validation

- `just validate data/taxa/eukaryota/stylonychia_lemnae.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stylonectria_norvegica.yaml data/taxa/eukaryota/stylonychia_lemnae.yaml data/taxa/eukaryota/sugiyamaella_americana.yaml data/taxa/eukaryota/sugiyamaella_boreocaroliniensis.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:5949`, `label: Stylonychia lemnae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5948`, `genetic_code: 6`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:2625` retains the same current species row.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 1 related synonym for `NCBITaxon:5949`; the YAML carries the same single synonym entry.
- The seeded-scope search found exactly one row for `NCBITaxon:5949` at `data/seed/scope.tsv:52113`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:5949`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:39660` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row, 1 project row, and 1 analysis row for `NCBITaxon:5949`.
- No exact NCBI type-material rows referenced `NCBITaxon:5949`.
- No local StrainInfo rows or exact BacDive rows referenced `NCBITaxon:5949`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:5949` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
- Auxiliary bacterial source tables had no rows for this eukaryotic taxon in BactoTraits, GTDB, LPSN, Madin, or MediaDive inputs.
- Generated StrainInfo overlay tables had no target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, or `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

The review ran from the detached worktree at `/private/tmp/taxonmech-codex-review`; the seeded YAML record was left unchanged.
