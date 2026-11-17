# YAML Record Review: Stellarima microtrias

- Verdict: pass
- Target: `data/taxa/eukaryota/stellarima_microtrias.yaml`
- Identifier: `NCBITaxon:188541`

## Target

Reviewed the complete 75-line YAML record for Stellarima microtrias. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stellarima_microtrias`.

## Validation

- `just validate data/taxa/eukaryota/stellarima_microtrias.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/staurosirella_guenter_grassii.yaml data/taxa/eukaryota/steccherinum_ochraceum.yaml data/taxa/eukaryota/stellarima_microtrias.yaml data/taxa/eukaryota/stemphylium_lycopersici.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:188541`, `label: Stellarima microtrias`, `rank: SPECIES`, `parent: NCBITaxon:188540`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:188541`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:188541` in `data/seed/scope.tsv`.
- All 12 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- No retired IDs were mapped into `NCBITaxon:188541` in `data/raw/ncbi_merged_ids.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:16961` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- The bounded native GOLD scan found no exact organism, project, or analysis rows carrying `NCBITaxon:188541`.
- No exact type-material rows for `NCBITaxon:188541` were present in `data/raw/ncbi_type_material.tsv`.
- Local StrainInfo records contained 15 direct exact records and 15 exact deposit placements for `NCBITaxon:188541`; the exact JSONL search found 15 records carrying `"ncbi":188541`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:188541`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:188541` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
