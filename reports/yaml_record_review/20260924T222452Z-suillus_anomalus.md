# YAML Record Review: Suillus anomalus

- Verdict: pass
- Target: `data/taxa/eukaryota/suillus_anomalus.yaml`
- Identifier: `NCBITaxon:1912933`

## Target

Reviewed the complete 75-line YAML record for Suillus anomalus. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suillus_anomalus`.

## Validation

- `just validate data/taxa/eukaryota/suillus_anomalus.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suillus_americanus.yaml data/taxa/eukaryota/suillus_ampliporus.yaml data/taxa/eukaryota/suillus_anomalus.yaml data/taxa/eukaryota/suillus_bovinus.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:1912933`, `label: Suillus anomalus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5379`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:493735` retains the same current species row.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 1 related synonym for `NCBITaxon:1912933`; the YAML carries the same single synonym entry.
- The seeded-scope search found exactly one row for `NCBITaxon:1912933` at `data/seed/scope.tsv:61581`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:1912933`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:17405` reports `organism_count=1`, matching the YAML GOLD source attestation.
- No native GOLD analysis, organism, or project rows carried `NCBITaxon:1912933`.
- The exact search of `data/raw/ncbi_type_material.tsv` found no row for `NCBITaxon:1912933`.
- No exact StrainInfo or BacDive rows referenced `NCBITaxon:1912933`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1912933` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
