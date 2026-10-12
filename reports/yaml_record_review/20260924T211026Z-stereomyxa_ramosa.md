# YAML Record Review: Stereomyxa ramosa

- Verdict: pass
- Target: `data/taxa/eukaryota/stereomyxa_ramosa.yaml`
- Identifier: `NCBITaxon:1078864`

## Target

Reviewed the complete 51-line YAML record for Stereomyxa ramosa. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stereomyxa_ramosa`.

## Validation

- `just validate data/taxa/eukaryota/stereomyxa_ramosa.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stephanopyxis_turris.yaml data/taxa/eukaryota/stereomyxa_ramosa.yaml data/taxa/eukaryota/stereum_hirsutum.yaml data/taxa/eukaryota/sterigmatomyces_elviae.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:1078864`, `label: Stereomyxa ramosa`, `rank: SPECIES`, `parent: NCBITaxon:1078863`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 1 related synonym for `NCBITaxon:1078864`; the YAML carries the same related synonym and no extra exact or broad synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1078864` in `data/seed/scope.tsv`.
- All 6 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- No retired IDs were mapped into `NCBITaxon:1078864` in `data/raw/ncbi_merged_ids.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:1446` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0368879`; no GOLD project or analysis rows used `NCBITaxon:1078864`.
- No exact type-material rows for `NCBITaxon:1078864` were present in `data/raw/ncbi_type_material.tsv`.
- Local StrainInfo records contained 1 direct exact record and 1 exact deposit placement for `NCBITaxon:1078864`; the exact JSONL search found 1 record carrying `"ncbi":1078864`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:1078864`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1078864` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
