# YAML Record Review: Sungouiella dosseyi

- Verdict: pass
- Target: `data/taxa/eukaryota/sungouiella_dosseyi.yaml`
- Identifier: `NCBITaxon:391827`

## Target

Reviewed the complete 82-line YAML record for Sungouiella dosseyi. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sungouiella_dosseyi`.

## Validation

- `just validate data/taxa/eukaryota/sungouiella_dosseyi.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sungouiella_blattae.yaml data/taxa/eukaryota/sungouiella_dosseyi.yaml data/taxa/eukaryota/sungouiella_ecuadorensis.yaml data/taxa/eukaryota/sungouiella_ezoensis.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:391827`, `label: Sungouiella dosseyi`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3315605`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:83043` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:391827`; the YAML carries the same four synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:391827` at `data/seed/scope.tsv:55482`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:391827`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:34124` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:391827`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 8 exact `NCBITaxon:391827` rows for `Candida dosseyi`, covering ATCC MYA-4359 and NRRL Y-27950 culture-from-holotype variants from `typematerial.dmp`.
- No exact StrainInfo or BacDive rows referenced `NCBITaxon:391827`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:391827` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
