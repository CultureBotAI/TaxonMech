# YAML Record Review: Suillus paluster

- Verdict: pass
- Target: `data/taxa/eukaryota/suillus_paluster.yaml`
- Identifier: `NCBITaxon:48578`

## Target

Reviewed the complete 81-line YAML record for Suillus paluster. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suillus_paluster`.

## Validation

- `just validate data/taxa/eukaryota/suillus_paluster.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suillus_occidentalis.yaml data/taxa/eukaryota/suillus_ochraceoroseus.yaml data/taxa/eukaryota/suillus_paluster.yaml data/taxa/eukaryota/suillus_placidus.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:48578`, `label: Suillus paluster`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5379`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:6196` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:48578`; the YAML carries the same three synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:48578` at `data/seed/scope.tsv:52768`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv:63470` maps retired ID `NCBITaxon:3102701` into `NCBITaxon:48578`, and the exact merged-ID search found no retained row for the retired ID in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:36884` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 analysis row, 1 organism row, and 2 project rows for `NCBITaxon:48578`.
- `data/raw/ncbi_type_material.tsv` contains no exact rows for `NCBITaxon:48578`.
- StrainInfo contained 1 direct strain record and 1 exact deposit row for `NCBITaxon:48578`; no exact BacDive rows referenced the taxon ID.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:48578` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
