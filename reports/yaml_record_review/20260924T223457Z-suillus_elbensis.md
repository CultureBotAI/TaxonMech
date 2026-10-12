# YAML Record Review: Suillus elbensis

- Verdict: pass
- Target: `data/taxa/eukaryota/suillus_elbensis.yaml`
- Identifier: `NCBITaxon:1912937`

## Target

Reviewed the complete 81-line YAML record for Suillus elbensis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suillus_elbensis`.

## Validation

- `just validate data/taxa/eukaryota/suillus_elbensis.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suillus_decipiens.yaml data/taxa/eukaryota/suillus_discolor.yaml data/taxa/eukaryota/suillus_elbensis.yaml data/taxa/eukaryota/suillus_fuscotomentosus.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:1912937`, `label: Suillus elbensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5379`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:493738` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:1912937`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1912937` at `data/seed/scope.tsv:61584`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:1912937`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:17408` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 2 project rows for `NCBITaxon:1912937`; no GOLD analysis rows used that taxon ID.
- The exact search of `data/raw/ncbi_type_material.tsv` found no row for `NCBITaxon:1912937`.
- No exact StrainInfo or BacDive rows referenced `NCBITaxon:1912937`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1912937` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
