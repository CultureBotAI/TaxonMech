# YAML Record Review: Stephanopyxis turris

- Verdict: pass
- Target: `data/taxa/eukaryota/stephanopyxis_turris.yaml`
- Identifier: `NCBITaxon:515487`

## Target

Reviewed the complete 84-line YAML record for Stephanopyxis turris. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stephanopyxis_turris`.

## Validation

- `just validate data/taxa/eukaryota/stephanopyxis_turris.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stephanopyxis_turris.yaml data/taxa/eukaryota/stereomyxa_ramosa.yaml data/taxa/eukaryota/stereum_hirsutum.yaml data/taxa/eukaryota/sterigmatomyces_elviae.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:515487`, `label: Stephanopyxis turris`, `rank: SPECIES`, `parent: NCBITaxon:3006`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 2 exact synonyms, 0 broad synonyms, and 4 related synonyms for `NCBITaxon:515487`; the YAML carries the same 6 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:515487` in `data/seed/scope.tsv`.
- All 12 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:1606799`, into `NCBITaxon:515487`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:37591` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0368878`; no GOLD project or analysis rows used `NCBITaxon:515487`.
- No exact type-material rows for `NCBITaxon:515487` were present in `data/raw/ncbi_type_material.tsv`.
- Local StrainInfo records contained 8 direct exact records and 8 exact deposit placements for `NCBITaxon:515487`; the exact JSONL search found 8 records carrying `"ncbi":515487`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:515487`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:515487` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
