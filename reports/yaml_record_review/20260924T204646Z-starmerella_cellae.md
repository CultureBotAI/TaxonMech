# YAML Record Review: Starmerella cellae

- Verdict: pass
- Target: `data/taxa/eukaryota/starmerella_cellae.yaml`
- Identifier: `NCBITaxon:308923`

## Target

Reviewed the complete 79-line YAML record for Starmerella cellae. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmerella_cellae`.

## Validation

- `just validate data/taxa/eukaryota/starmerella_cellae.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmerella_cellae.yaml data/taxa/eukaryota/starmerella_davenportii.yaml data/taxa/eukaryota/starmerella_etchellsii.yaml data/taxa/eukaryota/starmerella_floricola.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:308923`, `label: Starmerella cellae`, `rank: SPECIES`, `parent: NCBITaxon:75735`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:308923`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:308923` in `data/seed/scope.tsv`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- No retired IDs were mapped into `NCBITaxon:308923` in `data/raw/ncbi_merged_ids.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:31250` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0705503` and 1 project row for `Gp0831546`; no GOLD analysis rows used `NCBITaxon:308923`.
- `data/raw/ncbi_type_material.tsv` contains 9 exact `NCBITaxon:308923` rows under `Candida cellae`, including `CBS 10086`, `NRRL Y-27860`, and `UFMG-PC04` type-material designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 1 direct exact record and 3 exact deposit placements for `NCBITaxon:308923`; the exact JSONL search found 1 record carrying `"ncbi":308923`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:308923`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:308923` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
