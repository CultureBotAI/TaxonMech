# YAML Record Review: Suillus americanus

- Verdict: pass
- Target: `data/taxa/eukaryota/suillus_americanus.yaml`
- Identifier: `NCBITaxon:48561`

## Target

Reviewed the complete 81-line YAML record for Suillus americanus. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suillus_americanus`.

## Validation

- `just validate data/taxa/eukaryota/suillus_americanus.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suillus_americanus.yaml data/taxa/eukaryota/suillus_ampliporus.yaml data/taxa/eukaryota/suillus_anomalus.yaml data/taxa/eukaryota/suillus_bovinus.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:48561`, `label: Suillus americanus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5379`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:6186` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:48561`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:48561` at `data/seed/scope.tsv:52758`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:48561`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:36874` reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 2 project rows for `NCBITaxon:48561`; no GOLD analysis rows used that taxon ID.
- The exact search of `data/raw/ncbi_type_material.tsv` found no row for `NCBITaxon:48561`.
- Local StrainInfo records contained 3 direct exact records and 3 exact deposit placements for `NCBITaxon:48561`; the exact JSONL search found 3 direct records carrying `"ncbi":48561`.
- No exact BacDive rows referenced `NCBITaxon:48561`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:48561` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
