# YAML Record Review: Starmerella bacillaris

- Verdict: pass
- Target: `data/taxa/eukaryota/starmerella_bacillaris.yaml`
- Identifier: `NCBITaxon:1247836`

## Target

Reviewed the complete 109-line YAML record for Starmerella bacillaris. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmerella_bacillaris`.

## Validation

- `just validate data/taxa/eukaryota/starmerella_bacillaris.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmerella_asiatica.yaml data/taxa/eukaryota/starmerella_bacillaris.yaml data/taxa/eukaryota/starmerella_bombi.yaml data/taxa/eukaryota/starmerella_bombicola.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:1247836`, `label: Starmerella bacillaris`, `rank: SPECIES`, `parent: NCBITaxon:75735`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 4 exact synonyms, 0 broad synonyms, and 9 related synonyms for `NCBITaxon:1247836`; the YAML carries the same 13 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1247836` in `data/seed/scope.tsv`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps 5 retired IDs into `NCBITaxon:1247836`: `NCBITaxon:186762`, `NCBITaxon:214700`, `NCBITaxon:214701`, `NCBITaxon:214702`, and `NCBITaxon:214703`. The exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only those merged-ID rows and no retained old-ID taxon rows.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:5961` reports `organism_count=4`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 4 organism rows, 4 project rows, and 3 analysis rows for `NCBITaxon:1247836`, including organism rows for `PAS13`, `FRI751`, `NP2`, and `CBS 9494`.
- `data/raw/ncbi_type_material.tsv` contains 6 exact `NCBITaxon:1247836` rows for `CBS 9494` type-material designations under `Candida zemplinina` and `CBS 843` / `PYCC 3044` culture-from-neotype designations under `Saccharomyces bacillaris`.
- Local StrainInfo records contained 5 direct exact records and 14 exact deposit placements for `NCBITaxon:1247836`; the exact JSONL search found 11 records carrying `"ncbi":1247836`, including 6 `Starmerella stellata` primary records with exact `S. bacillaris` deposits.
- No exact BacDive rows referenced `NCBITaxon:1247836`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1247836` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
