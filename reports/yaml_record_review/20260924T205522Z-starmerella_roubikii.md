# YAML Record Review: Starmerella roubikii

- Verdict: pass
- Target: `data/taxa/eukaryota/starmerella_roubikii.yaml`
- Identifier: `NCBITaxon:2596946`

## Target

Reviewed the complete 75-line YAML record for Starmerella roubikii. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmerella_roubikii`.

## Validation

- `just validate data/taxa/eukaryota/starmerella_roubikii.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmerella_ratchasimensis.yaml data/taxa/eukaryota/starmerella_riodocensis.yaml data/taxa/eukaryota/starmerella_roubikii.yaml data/taxa/eukaryota/starmerella_scarabaei.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:2596946`, `label: Starmerella roubikii`, `rank: SPECIES`, `parent: NCBITaxon:75735`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:2596946`; the YAML carries the 2 related synonyms and no extra exact or broad synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:2596946` in `data/seed/scope.tsv`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:228554`, into `NCBITaxon:2596946`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:23836` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0705118` and 1 project row for `Gp0831141`; no GOLD analysis rows used `NCBITaxon:2596946`.
- `data/raw/ncbi_type_material.tsv` contains 6 exact `NCBITaxon:2596946` rows under `Starmerella roubikii`, covering `NRRL Y-63974` and `UWOPS 01-191.1` culture-from-holotype variants plus `CBS 15148` holotype variants from `typematerial.dmp`.
- No exact BacDive or StrainInfo rows referenced `NCBITaxon:2596946`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:2596946` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
