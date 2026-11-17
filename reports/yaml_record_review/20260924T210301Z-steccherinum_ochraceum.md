# YAML Record Review: Steccherinum ochraceum

- Verdict: pass
- Target: `data/taxa/eukaryota/steccherinum_ochraceum.yaml`
- Identifier: `NCBITaxon:92696`

## Target

Reviewed the complete 78-line YAML record for Steccherinum ochraceum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `steccherinum_ochraceum`.

## Validation

- `just validate data/taxa/eukaryota/steccherinum_ochraceum.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/staurosirella_guenter_grassii.yaml data/taxa/eukaryota/steccherinum_ochraceum.yaml data/taxa/eukaryota/stellarima_microtrias.yaml data/taxa/eukaryota/stemphylium_lycopersici.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:92696`, `label: Steccherinum ochraceum`, `rank: SPECIES`, `parent: NCBITaxon:81060`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:92696`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:92696` in `data/seed/scope.tsv`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- No retired IDs were mapped into `NCBITaxon:92696` in `data/raw/ncbi_merged_ids.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:44564` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0519723`, 1 project row for `Gp0443876`, and 1 analysis row for `Steccherinum ochraceum LE-BIN_3174`.
- No exact type-material rows for `NCBITaxon:92696` were present in `data/raw/ncbi_type_material.tsv`.
- Local StrainInfo records contained 16 direct exact records and 16 exact deposit placements for `NCBITaxon:92696`; the exact JSONL search found 16 records carrying `"ncbi":92696`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:92696`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:92696` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
