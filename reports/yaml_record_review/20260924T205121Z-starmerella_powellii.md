# YAML Record Review: Starmerella powellii

- Verdict: pass
- Target: `data/taxa/eukaryota/starmerella_powellii.yaml`
- Identifier: `NCBITaxon:121467`

## Target

Reviewed the complete 85-line YAML record for Starmerella powellii. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmerella_powellii`.

## Validation

- `just validate data/taxa/eukaryota/starmerella_powellii.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmerella_floris.yaml data/taxa/eukaryota/starmerella_khaoyaiensis.yaml data/taxa/eukaryota/starmerella_lactis_condensi.yaml data/taxa/eukaryota/starmerella_powellii.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:121467`, `label: Starmerella powellii`, `rank: SPECIES`, `parent: NCBITaxon:75735`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 4 related synonyms for `NCBITaxon:121467`; the YAML carries the same 5 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:121467` in `data/seed/scope.tsv`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- No retired IDs were mapped into `NCBITaxon:121467` in `data/raw/ncbi_merged_ids.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:5103` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0705157` and 1 project row for `Gp0831180`; no GOLD analysis rows used `NCBITaxon:121467`.
- `data/raw/ncbi_type_material.tsv` contains 9 exact `NCBITaxon:121467` rows under `Starmerella powellii`, covering `UWOPS 99-325.3` culture-from-holotype variants and `CBS 8795` holotype variants from `typematerial.dmp`.
- Local StrainInfo records contained 1 direct exact record and 2 exact deposit placements for `NCBITaxon:121467`; the exact JSONL search found 1 record carrying `"ncbi":121467`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:121467`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:121467` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
