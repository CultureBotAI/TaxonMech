# YAML Record Review: Suhomyces wounanorum

- Verdict: pass
- Target: `data/taxa/eukaryota/suhomyces_wounanorum.yaml`
- Identifier: `NCBITaxon:246083`

## Target

Reviewed the complete 82-line YAML record for Suhomyces wounanorum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suhomyces_wounanorum`.

## Validation

- `just validate data/taxa/eukaryota/suhomyces_wounanorum.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suhomyces_tibetensis.yaml data/taxa/eukaryota/suhomyces_vadensis.yaml data/taxa/eukaryota/suhomyces_wounanorum.yaml data/taxa/eukaryota/suhomyces_xylopsoci.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:246083`, `label: Suhomyces wounanorum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1539666`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:48272` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:246083`; the YAML carries the same 4 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:246083` at `data/seed/scope.tsv:54736`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:246083`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:22144` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:246083`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 10 exact `NCBITaxon:246083` rows for `Candida wounanorum`, including ATCC MYA-4312 culture-from-type-material variants plus BG 02-7-18-027A-1-1, CBS 9828, and NRRL Y-27574 type-material variants from `typematerial.dmp`.
- No exact StrainInfo or BacDive rows referenced `NCBITaxon:246083`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:246083` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
