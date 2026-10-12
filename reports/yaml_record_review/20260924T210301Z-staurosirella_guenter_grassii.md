# YAML Record Review: Staurosirella guenter-grassii

- Verdict: pass
- Target: `data/taxa/eukaryota/staurosirella_guenter_grassii.yaml`
- Identifier: `NCBITaxon:528331`

## Target

Reviewed the complete 82-line YAML record for Staurosirella guenter-grassii. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `staurosirella_guenter_grassii`.

## Validation

- `just validate data/taxa/eukaryota/staurosirella_guenter_grassii.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/staurosirella_guenter_grassii.yaml data/taxa/eukaryota/steccherinum_ochraceum.yaml data/taxa/eukaryota/stellarima_microtrias.yaml data/taxa/eukaryota/stemphylium_lycopersici.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:528331`, `label: Staurosirella guenter-grassii`, `rank: SPECIES`, `parent: NCBITaxon:449168`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 2 exact synonyms, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:528331`; the YAML carries the same 5 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:528331` in `data/seed/scope.tsv`.
- All 12 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:3112049`, into `NCBITaxon:528331`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:37999` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- The bounded native GOLD scan found no exact organism, project, or analysis rows carrying `NCBITaxon:528331`.
- No exact type-material rows for `NCBITaxon:528331` were present in `data/raw/ncbi_type_material.tsv`.
- No exact BacDive or StrainInfo rows referenced `NCBITaxon:528331`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:528331` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
