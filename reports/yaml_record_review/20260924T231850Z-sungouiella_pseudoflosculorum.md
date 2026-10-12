# YAML Record Review: Sungouiella pseudoflosculorum

- Verdict: pass
- Target: `data/taxa/eukaryota/sungouiella_pseudoflosculorum.yaml`
- Identifier: `NCBITaxon:1041604`

## Target

Reviewed the complete 79-line YAML record for Sungouiella pseudoflosculorum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sungouiella_pseudoflosculorum`.

## Validation

- `just validate data/taxa/eukaryota/sungouiella_pseudoflosculorum.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sungouiella_pseudoflosculorum.yaml data/taxa/eukaryota/sungouiella_pseudointermedia.yaml data/taxa/eukaryota/sungouiella_sharkensis.yaml data/taxa/eukaryota/sungouiella_suratensis.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:1041604`, `label: Sungouiella pseudoflosculorum`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3315605`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:223678` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:1041604`; the YAML carries the same three synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1041604` at `data/seed/scope.tsv:57272`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:1041604`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:584` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:1041604`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 2 exact `NCBITaxon:1041604` rows for `Candida pseudoflosculorum`, covering CBS 8584 culture-from-type-material variants from `typematerial.dmp`.
- No exact StrainInfo or BacDive rows referenced `NCBITaxon:1041604`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1041604` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
