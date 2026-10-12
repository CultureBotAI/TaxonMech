# YAML Record Review: Suhomyces maxii

- Verdict: pass
- Target: `data/taxa/eukaryota/suhomyces_maxii.yaml`
- Identifier: `NCBITaxon:246000`

## Target

Reviewed the complete 84-line YAML record for Suhomyces maxii. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suhomyces_maxii`.

## Validation

- `just validate data/taxa/eukaryota/suhomyces_maxii.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suhomyces_kunorum.yaml data/taxa/eukaryota/suhomyces_maxii.yaml data/taxa/eukaryota/suhomyces_panamericanus.yaml data/taxa/eukaryota/suhomyces_prunicola.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:246000`, `label: Suhomyces maxii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1539666`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:48260` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 4 related synonyms for `NCBITaxon:246000`; the YAML carries the same 5 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:246000` at `data/seed/scope.tsv:54724`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps 1 retired ID into `NCBITaxon:246000`; the exact ignored-file-inclusive search over `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon rows.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:22132` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:246000`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 10 exact `NCBITaxon:246000` rows for `Candida maxii`, including ATCC MYA-4320 culture-from-type-material variants plus BG 01-7-21-006A-1-1, CBS 9836, and NRRL Y-27588 type-material variants from `typematerial.dmp`.
- No exact StrainInfo or BacDive rows referenced `NCBITaxon:246000`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:246000` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
