# YAML Record Review: Sungouiella ecuadorensis

- Verdict: pass
- Target: `data/taxa/eukaryota/sungouiella_ecuadorensis.yaml`
- Identifier: `NCBITaxon:1253868`

## Target

Reviewed the complete 85-line YAML record for Sungouiella ecuadorensis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sungouiella_ecuadorensis`.

## Validation

- `just validate data/taxa/eukaryota/sungouiella_ecuadorensis.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sungouiella_blattae.yaml data/taxa/eukaryota/sungouiella_dosseyi.yaml data/taxa/eukaryota/sungouiella_ecuadorensis.yaml data/taxa/eukaryota/sungouiella_ezoensis.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:1253868`, `label: Sungouiella ecuadorensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3315605`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:288836` retains the same current species row.
- NCBI lists 2 exact synonyms, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:1253868`; the YAML carries the same five synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1253868` at `data/seed/scope.tsv:58695`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps retired IDs `NCBITaxon:997988` and `NCBITaxon:997989` into `NCBITaxon:1253868`, and the exact merged-ID search found no retained row for either retired ID in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:6026` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:1253868`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 8 exact `NCBITaxon:1253868` rows for `Candida ecuadorensis`, covering CBS 12653 culture-from-holotype variants and CLQCA 20-004 holotype variants from `typematerial.dmp`.
- No exact StrainInfo or BacDive rows referenced `NCBITaxon:1253868`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1253868` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
