# YAML Record Review: Starmerella sirachaensis

- Verdict: pass
- Target: `data/taxa/eukaryota/starmerella_sirachaensis.yaml`
- Identifier: `NCBITaxon:1217581`

## Target

Reviewed the complete 85-line YAML record for Starmerella sirachaensis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmerella_sirachaensis`.

## Validation

- `just validate data/taxa/eukaryota/starmerella_sirachaensis.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmerella_sirachaensis.yaml data/taxa/eukaryota/starmerella_stellata.yaml data/taxa/eukaryota/starmerella_vitae.yaml data/taxa/eukaryota/stauroneis_constricta.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:1217581`, `label: Starmerella sirachaensis`, `rank: SPECIES`, `parent: NCBITaxon:75735`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 2 exact synonyms, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:1217581`; the YAML carries the same 5 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1217581` in `data/seed/scope.tsv`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:991124`, into `NCBITaxon:1217581`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:5173` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0705191` and 1 project row for `Gp0831214`; no GOLD analysis rows used `NCBITaxon:1217581`.
- `data/raw/ncbi_type_material.tsv` contains 12 exact `NCBITaxon:1217581` rows under `Starmerella sirachaensis`, including `BCC 47628`, `NBRC 108605`, `CBS 12094`, and `LM008` holotype or culture-from-holotype designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 1 direct exact record and 1 exact deposit placement for `NCBITaxon:1217581`; the exact JSONL search found 1 record carrying `"ncbi":1217581`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:1217581`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1217581` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
