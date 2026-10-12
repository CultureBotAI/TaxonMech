# YAML Record Review: Suillus alpinus

- Verdict: pass
- Target: `data/taxa/eukaryota/suillus_alpinus.yaml`
- Identifier: `NCBITaxon:1930190`

## Target

Reviewed the complete 78-line YAML record for Suillus alpinus. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suillus_alpinus`.

## Validation

- `just validate data/taxa/eukaryota/suillus_alpinus.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suhomyces_yuchorum.yaml data/taxa/eukaryota/suillellus_queletii.yaml data/taxa/eukaryota/suillus_acidus.yaml data/taxa/eukaryota/suillus_alpinus.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:1930190`, `label: Suillus alpinus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5379`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:496199` retains the same current species row.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:1930190`; the YAML carries the same 2 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1930190` at `data/seed/scope.tsv:61641`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps 1 retired ID into `NCBITaxon:1930190`; the exact ignored-file-inclusive search over `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon rows.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:17681` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 analysis row, 1 organism row, and 1 project row for `NCBITaxon:1930190`.
- The exact search of `data/raw/ncbi_type_material.tsv` found no row for `NCBITaxon:1930190`.
- No exact StrainInfo or BacDive rows referenced `NCBITaxon:1930190`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1930190` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
