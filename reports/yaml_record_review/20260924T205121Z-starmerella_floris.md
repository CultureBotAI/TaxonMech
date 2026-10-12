# YAML Record Review: Starmerella floris

- Verdict: pass
- Target: `data/taxa/eukaryota/starmerella_floris.yaml`
- Identifier: `NCBITaxon:453956`

## Target

Reviewed the complete 85-line YAML record for Starmerella floris. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmerella_floris`.

## Validation

- `just validate data/taxa/eukaryota/starmerella_floris.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmerella_floris.yaml data/taxa/eukaryota/starmerella_khaoyaiensis.yaml data/taxa/eukaryota/starmerella_lactis_condensi.yaml data/taxa/eukaryota/starmerella_powellii.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:453956`, `label: Starmerella floris`, `rank: SPECIES`, `parent: NCBITaxon:75735`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 2 exact synonyms, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:453956`; the YAML carries the same 5 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:453956` in `data/seed/scope.tsv`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:150211`, into `NCBITaxon:453956`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:35962` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0705532` and 1 project row for `Gp0831575`; no GOLD analysis rows used `NCBITaxon:453956`.
- `data/raw/ncbi_type_material.tsv` contains 9 exact `NCBITaxon:453956` rows under `Candida floris`, including `CBS 10593`, `NRRL Y-48255`, and `UWO(PS)00-226.2` type-material designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 1 direct exact record and 1 exact deposit placement for `NCBITaxon:453956`; the exact JSONL search found 1 record carrying `"ncbi":453956`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:453956`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:453956` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
