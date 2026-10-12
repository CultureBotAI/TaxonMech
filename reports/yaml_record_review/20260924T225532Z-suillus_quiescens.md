# YAML Record Review: Suillus quiescens

- Verdict: pass
- Target: `data/taxa/eukaryota/suillus_quiescens.yaml`
- Identifier: `NCBITaxon:627136`

## Target

Reviewed the complete 78-line YAML record for Suillus quiescens. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suillus_quiescens`.

## Validation

- `just validate data/taxa/eukaryota/suillus_quiescens.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suillus_pungens.yaml data/taxa/eukaryota/suillus_quiescens.yaml data/taxa/eukaryota/suillus_sibiricus.yaml data/taxa/eukaryota/suillus_spectabilis.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:627136`, `label: Suillus quiescens`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5379`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:144688` retains the same current species row.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:627136`; the YAML carries the same two synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:627136` at `data/seed/scope.tsv:56178`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:627136`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:40006` reports `organism_count=7`, matching the YAML GOLD source attestation.
- Native GOLD contained 7 organism rows and 13 project rows for `NCBITaxon:627136`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 4 exact `NCBITaxon:627136` rows for `Suillus quiescens`, covering UC 1860306 holotype and type-material variants from `typematerial.dmp`.
- No exact StrainInfo or BacDive rows referenced `NCBITaxon:627136`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:627136` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
