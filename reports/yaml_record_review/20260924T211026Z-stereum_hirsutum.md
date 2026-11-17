# YAML Record Review: Stereum hirsutum

- Verdict: pass
- Target: `data/taxa/eukaryota/stereum_hirsutum.yaml`
- Identifier: `NCBITaxon:40492`

## Target

Reviewed the complete 78-line YAML record for Stereum hirsutum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stereum_hirsutum`.

## Validation

- `just validate data/taxa/eukaryota/stereum_hirsutum.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stephanopyxis_turris.yaml data/taxa/eukaryota/stereomyxa_ramosa.yaml data/taxa/eukaryota/stereum_hirsutum.yaml data/taxa/eukaryota/sterigmatomyces_elviae.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:40492`, `label: Stereum hirsutum`, `rank: SPECIES`, `parent: NCBITaxon:5644`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:40492`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:40492` in `data/seed/scope.tsv`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- No retired IDs were mapped into `NCBITaxon:40492` in `data/raw/ncbi_merged_ids.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:34569` reports `organism_count=2`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0017583` and 2 project rows for `Gp0332790` and `Gp0332791`; no GOLD analysis rows used `NCBITaxon:40492`.
- No exact type-material rows for `NCBITaxon:40492` were present in `data/raw/ncbi_type_material.tsv`.
- Local StrainInfo records contained 41 direct exact records and 50 exact deposit placements for `NCBITaxon:40492`; the exact JSONL search found 41 records carrying `"ncbi":40492`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:40492`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:40492` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
