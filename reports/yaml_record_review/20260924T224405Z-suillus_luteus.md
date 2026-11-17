# YAML Record Review: Suillus luteus

- Verdict: pass
- Target: `data/taxa/eukaryota/suillus_luteus.yaml`
- Identifier: `NCBITaxon:5384`

## Target

Reviewed the complete 80-line YAML record for Suillus luteus. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suillus_luteus`.

## Validation

- `just validate data/taxa/eukaryota/suillus_luteus.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suillus_hirtellus.yaml data/taxa/eukaryota/suillus_kaibabensis.yaml data/taxa/eukaryota/suillus_lakei.yaml data/taxa/eukaryota/suillus_luteus.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:5384`, `label: Suillus luteus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5379`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:2383` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:5384`; the YAML carries the same three synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:5384` at `data/seed/scope.tsv:51983`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:5384`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:38248` reports `organism_count=324`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 analysis row, 269 organism rows, and 334 project rows for `NCBITaxon:5384`.
- `data/raw/ncbi_type_material.tsv` contains no exact rows for `NCBITaxon:5384`.
- StrainInfo contained 19 direct strain records and 27 exact deposit rows for `NCBITaxon:5384`; no exact BacDive rows referenced the taxon ID.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:5384` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
