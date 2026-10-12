# YAML Record Review: Sugiyamaella lignohabitans

- Verdict: pass
- Target: `data/taxa/eukaryota/sugiyamaella_lignohabitans.yaml`
- Identifier: `NCBITaxon:796027`

## Target

Reviewed the complete 81-line YAML record for Sugiyamaella lignohabitans. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sugiyamaella_lignohabitans`.

## Validation

- `just validate data/taxa/eukaryota/sugiyamaella_lignohabitans.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sugiyamaella_japonica.yaml data/taxa/eukaryota/sugiyamaella_lignohabitans.yaml data/taxa/eukaryota/sugiyamaella_marilandica.yaml data/taxa/eukaryota/sugiyamaella_marionensis.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:796027`, `label: Sugiyamaella lignohabitans`, `rank: SPECIES`, `parent_taxon: NCBITaxon:410829`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:179597` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:796027`; the YAML carries the same 4 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:796027` at `data/seed/scope.tsv:56708`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:378057`, into `NCBITaxon:796027`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:42807` reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD contained 2 organism rows, 2 project rows, and 1 analysis row for `NCBITaxon:796027`.
- `data/raw/ncbi_type_material.tsv` contains 5 exact `NCBITaxon:796027` rows under `Candida lignohabitans`, including CBS 10342 and NRRL YB-1473 culture-from-holotype designation variants from `typematerial.dmp`.
- No local StrainInfo rows or exact BacDive rows referenced `NCBITaxon:796027`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:796027` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
