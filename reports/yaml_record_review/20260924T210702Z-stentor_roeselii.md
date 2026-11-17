# YAML Record Review: Stentor roeselii

- Verdict: pass
- Target: `data/taxa/eukaryota/stentor_roeselii.yaml`
- Identifier: `NCBITaxon:1703786`

## Target

Reviewed the complete 66-line YAML record for Stentor roeselii. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stentor_roeselii`.

## Validation

- `just validate data/taxa/eukaryota/stentor_roeselii.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stentor_coeruleus.yaml data/taxa/eukaryota/stentor_roeselii.yaml data/taxa/eukaryota/stephanocyclus_meneghinianus.yaml data/taxa/eukaryota/stephanopyxis_broschii.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:1703786`, `label: Stentor roeselii`, `rank: SPECIES`, `parent: NCBITaxon:5962`, `genetic_code: 10`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 1 related synonym for `NCBITaxon:1703786`; the YAML carries the same related synonym and no extra exact or broad synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1703786` in `data/seed/scope.tsv`.
- All 11 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:157965`, into `NCBITaxon:1703786`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:14739` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0573861`, 1 project row for `Gp0548531`, and 1 analysis row for `Stentor roeselii QDSR01`.
- No exact type-material rows for `NCBITaxon:1703786` were present in `data/raw/ncbi_type_material.tsv`.
- No exact BacDive or StrainInfo rows referenced `NCBITaxon:1703786`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1703786` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
