# YAML Record Review: Sugiyamaella floridensis

- Verdict: pass
- Target: `data/taxa/eukaryota/sugiyamaella_floridensis.yaml`
- Identifier: `NCBITaxon:377601`

## Target

Reviewed the complete 81-line YAML record for Sugiyamaella floridensis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sugiyamaella_floridensis`.

## Validation

- `just validate data/taxa/eukaryota/sugiyamaella_floridensis.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sugiyamaella_castrensis.yaml data/taxa/eukaryota/sugiyamaella_chiloensis.yaml data/taxa/eukaryota/sugiyamaella_floridensis.yaml data/taxa/eukaryota/sugiyamaella_grinbergsii.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:377601`, `label: Sugiyamaella floridensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:410829`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:79370` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:377601`; the YAML carries the same 4 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:377601` at `data/seed/scope.tsv:55414`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:377601`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:33788` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:377601`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 5 exact `NCBITaxon:377601` rows under `Candida floridensis`, including CBS 10350 and NRRL YB-3827 culture-from-holotype designation variants from `typematerial.dmp`.
- No local StrainInfo rows or exact BacDive rows referenced `NCBITaxon:377601`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:377601` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
