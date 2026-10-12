# YAML Record Review: Sterigmatosporidium polymorphum

- Verdict: pass
- Target: `data/taxa/eukaryota/sterigmatosporidium_polymorphum.yaml`
- Identifier: `NCBITaxon:5647`

## Target

Reviewed the complete 72-line YAML record for Sterigmatosporidium polymorphum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sterigmatosporidium_polymorphum`.

## Validation

- `just validate data/taxa/eukaryota/sterigmatosporidium_polymorphum.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sterigmatomyces_halophilus.yaml data/taxa/eukaryota/sterigmatomyces_hyphaenes.yaml data/taxa/eukaryota/sterigmatosporidium_polymorphum.yaml data/taxa/eukaryota/sterkiella_histriomuscorum.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:5647`, `label: Sterigmatosporidium polymorphum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:157883`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:2513` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 1 related synonym for `NCBITaxon:5647`; the YAML carries the same 2 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:5647` at `data/seed/scope.tsv:52053`.
- All 12 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:157884`, into `NCBITaxon:5647`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:38955` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:5647`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 6 exact `NCBITaxon:5647` rows for `Sterigmatosporidium polymorphum`, including CBS and PYCC type or reference material designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 13 direct exact records and 32 exact deposit placements for `NCBITaxon:5647`; the exact JSONL search found 13 records carrying `"ncbi":5647`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:5647`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:5647` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
