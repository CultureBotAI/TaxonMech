# YAML Record Review: Strombidium stylifer

- Verdict: pass
- Target: `data/taxa/eukaryota/strombidium_stylifer.yaml`
- Identifier: `NCBITaxon:356896`

## Target

Reviewed the complete 69-line YAML record for Strombidium stylifer. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `strombidium_stylifer`.

## Validation

- `just validate data/taxa/eukaryota/strombidium_stylifer.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/strombidium_rassoulzadegani.yaml data/taxa/eukaryota/strombidium_stylifer.yaml data/taxa/eukaryota/stropharia_rugosoannulata.yaml data/taxa/eukaryota/stygamoeba_regulata.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:356896`, `label: Strombidium stylifer`, `rank: SPECIES`, `parent_taxon: NCBITaxon:60005`, `genetic_code: 6`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:73606` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 1 related synonym for `NCBITaxon:356896`; the YAML carries the same 2 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:356896` at `data/seed/scope.tsv:55337`.
- All 11 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:236066`, into `NCBITaxon:356896`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:33112` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row, 1 project row, and 1 analysis row for `NCBITaxon:356896`.
- No exact NCBI type-material rows referenced `NCBITaxon:356896`.
- No local StrainInfo rows or exact BacDive rows referenced `NCBITaxon:356896`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:356896` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
