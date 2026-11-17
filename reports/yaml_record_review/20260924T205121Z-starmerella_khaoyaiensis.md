# YAML Record Review: Starmerella khaoyaiensis

- Verdict: pass
- Target: `data/taxa/eukaryota/starmerella_khaoyaiensis.yaml`
- Identifier: `NCBITaxon:1540079`

## Target

Reviewed the complete 83-line YAML record for Starmerella khaoyaiensis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmerella_khaoyaiensis`.

## Validation

- `just validate data/taxa/eukaryota/starmerella_khaoyaiensis.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmerella_floris.yaml data/taxa/eukaryota/starmerella_khaoyaiensis.yaml data/taxa/eukaryota/starmerella_lactis_condensi.yaml data/taxa/eukaryota/starmerella_powellii.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:1540079`, `label: Starmerella khaoyaiensis`, `rank: SPECIES`, `parent: NCBITaxon:75735`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:1540079`; the YAML carries the same 4 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1540079` in `data/seed/scope.tsv`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:374312`, into `NCBITaxon:1540079`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:12257` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0705184` and 1 project row for `Gp0831207`; no GOLD analysis rows used `NCBITaxon:1540079`.
- `data/raw/ncbi_type_material.tsv` contains 13 exact `NCBITaxon:1540079` rows under `Starmerella khaoyaiensis`, including `CBS 10839`, `NBRC 104213`, `BCC 7729`, and `ST-29` holotype or culture-from-holotype designation variants from `typematerial.dmp`.
- No exact BacDive or StrainInfo rows referenced `NCBITaxon:1540079`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1540079` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
