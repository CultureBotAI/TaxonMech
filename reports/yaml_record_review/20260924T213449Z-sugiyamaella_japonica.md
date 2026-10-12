# YAML Record Review: Sugiyamaella japonica

- Verdict: pass
- Target: `data/taxa/eukaryota/sugiyamaella_japonica.yaml`
- Identifier: `NCBITaxon:410836`

## Target

Reviewed the complete 81-line YAML record for Sugiyamaella japonica. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sugiyamaella_japonica`.

## Validation

- `just validate data/taxa/eukaryota/sugiyamaella_japonica.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sugiyamaella_japonica.yaml data/taxa/eukaryota/sugiyamaella_lignohabitans.yaml data/taxa/eukaryota/sugiyamaella_marilandica.yaml data/taxa/eukaryota/sugiyamaella_marionensis.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:410836`, `label: Sugiyamaella japonica`, `rank: SPECIES`, `parent_taxon: NCBITaxon:410829`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:89279` retains the same current species row.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 4 related synonyms for `NCBITaxon:410836`; the YAML carries the same 4 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:410836` at `data/seed/scope.tsv:55550`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps two retired IDs, `NCBITaxon:378061` and `NCBITaxon:420273`, into `NCBITaxon:410836`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only those merged-ID rows and no retained old-ID taxon rows.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:34727` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:410836`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 8 exact `NCBITaxon:410836` rows for `Sugiyamaella japonica`, including CBS 10354 and NRRL YB-2788 culture-from-holotype variants plus NRRL YB-2798 reference-material variants from `typematerial.dmp`.
- Local StrainInfo records contained 1 direct exact record and 1 exact deposit placement for `NCBITaxon:410836`; the exact JSONL search found 1 record carrying `"ncbi":410836`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:410836`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:410836` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
