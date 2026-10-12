# YAML Record Review: Suillus cothurnatus

- Verdict: pass
- Target: `data/taxa/eukaryota/suillus_cothurnatus.yaml`
- Identifier: `NCBITaxon:48568`

## Target

Reviewed the complete 75-line YAML record for Suillus cothurnatus. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suillus_cothurnatus`.

## Validation

- `just validate data/taxa/eukaryota/suillus_cothurnatus.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suillus_brunnescens.yaml data/taxa/eukaryota/suillus_clintonianus.yaml data/taxa/eukaryota/suillus_collinitus.yaml data/taxa/eukaryota/suillus_cothurnatus.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:48568`, `label: Suillus cothurnatus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5379`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:6189` retains the same current species row.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 1 related synonym for `NCBITaxon:48568`; the YAML carries the same single synonym entry.
- The seeded-scope search found exactly one row for `NCBITaxon:48568` at `data/seed/scope.tsv:52761`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:48568`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:36877` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 analysis row, 1 organism row, and 2 project rows for `NCBITaxon:48568`.
- The exact search of `data/raw/ncbi_type_material.tsv` found no row for `NCBITaxon:48568`.
- Local StrainInfo records contained 2 direct exact records and 4 exact deposit placements for `NCBITaxon:48568`; the exact JSONL search found 2 direct records carrying `"ncbi":48568`.
- No exact BacDive rows referenced `NCBITaxon:48568`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:48568` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
