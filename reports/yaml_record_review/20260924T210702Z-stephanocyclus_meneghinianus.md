# YAML Record Review: Stephanocyclus meneghinianus

- Verdict: pass
- Target: `data/taxa/eukaryota/stephanocyclus_meneghinianus.yaml`
- Identifier: `NCBITaxon:29205`

## Target

Reviewed the complete 72-line YAML record for Stephanocyclus meneghinianus. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stephanocyclus_meneghinianus`.

## Validation

- `just validate data/taxa/eukaryota/stephanocyclus_meneghinianus.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stentor_coeruleus.yaml data/taxa/eukaryota/stentor_roeselii.yaml data/taxa/eukaryota/stephanocyclus_meneghinianus.yaml data/taxa/eukaryota/stephanopyxis_broschii.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:29205`, `label: Stephanocyclus meneghinianus`, `rank: SPECIES`, `parent: NCBITaxon:2818153`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 2 exact synonyms, 0 broad synonyms, and 0 related synonyms for `NCBITaxon:29205`; the YAML carries the same 2 exact synonym entries and no related or broad synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:29205` in `data/seed/scope.tsv`.
- All 12 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:382363`, into `NCBITaxon:29205`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:28723` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 3 organism rows and 2 project rows for `NCBITaxon:29205`; no GOLD analysis rows used that taxon ID.
- No exact type-material rows for `NCBITaxon:29205` were present in `data/raw/ncbi_type_material.tsv`.
- Local StrainInfo records contained 36 direct exact records and 38 exact deposit placements for `NCBITaxon:29205`; the exact JSONL search found 37 records carrying `"ncbi":29205`, including one `Cyclotella cryptica` primary record with an exact `S. meneghinianus` deposit.
- No exact BacDive rows referenced `NCBITaxon:29205`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:29205` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
