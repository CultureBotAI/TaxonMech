# YAML Record Review: Stipitochalara longipes BDJ

- Verdict: pass
- Target: `data/taxa/eukaryota/stipitochalara_longipes_bdj.yaml`
- Identifier: `NCBITaxon:1379296`

## Target

Reviewed the complete 77-line YAML record for Stipitochalara longipes BDJ. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stipitochalara_longipes_bdj`.

## Validation

- `just validate data/taxa/eukaryota/stipitochalara_longipes_bdj.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stipitochalara_longipes_bdj.yaml data/taxa/eukaryota/stomiopeltis_betulae.yaml data/taxa/eukaryota/storeatula_major.yaml data/taxa/eukaryota/streblomastix_strix.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:1379296`, `label: Stipitochalara longipes BDJ`, `rank: STRAIN`, `parent_taxon: NCBITaxon:112123`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:336759` retains the same current strain row.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 0 related synonyms for `NCBITaxon:1379296`; the YAML likewise carries no synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1379296` at `data/seed/scope.tsv:59706`.
- All 16 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:1379296`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:8909` reports `organism_count=2`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row, 2 project rows, and 1 analysis row for `NCBITaxon:1379296`.
- No exact NCBI type-material rows referenced `NCBITaxon:1379296`.
- No local StrainInfo rows or exact BacDive rows referenced `NCBITaxon:1379296`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1379296` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
