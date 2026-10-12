# YAML Record Review: Sterkiella histriomuscorum

- Verdict: pass
- Target: `data/taxa/eukaryota/sterkiella_histriomuscorum.yaml`
- Identifier: `NCBITaxon:94289`

## Target

Reviewed the complete 79-line YAML record for Sterkiella histriomuscorum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sterkiella_histriomuscorum`.

## Validation

- `just validate data/taxa/eukaryota/sterkiella_histriomuscorum.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sterigmatomyces_halophilus.yaml data/taxa/eukaryota/sterigmatomyces_hyphaenes.yaml data/taxa/eukaryota/sterigmatosporidium_polymorphum.yaml data/taxa/eukaryota/sterkiella_histriomuscorum.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:94289`, `label: Sterkiella histriomuscorum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:94288`, `genetic_code: 6`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:15644` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:94289`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:94289` at `data/seed/scope.tsv:53552`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:5946`, into `NCBITaxon:94289`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:44974` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 2 organism rows, 2 project rows, and 1 analysis row for `NCBITaxon:94289`.
- No exact NCBI type-material rows referenced `NCBITaxon:94289`.
- No local StrainInfo rows or exact BacDive rows referenced `NCBITaxon:94289`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:94289` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
