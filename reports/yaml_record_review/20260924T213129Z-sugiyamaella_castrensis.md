# YAML Record Review: Sugiyamaella castrensis

- Verdict: pass
- Target: `data/taxa/eukaryota/sugiyamaella_castrensis.yaml`
- Identifier: `NCBITaxon:45535`

## Target

Reviewed the complete 79-line YAML record for Sugiyamaella castrensis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sugiyamaella_castrensis`.

## Validation

- `just validate data/taxa/eukaryota/sugiyamaella_castrensis.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sugiyamaella_castrensis.yaml data/taxa/eukaryota/sugiyamaella_chiloensis.yaml data/taxa/eukaryota/sugiyamaella_floridensis.yaml data/taxa/eukaryota/sugiyamaella_grinbergsii.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:45535`, `label: Sugiyamaella castrensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:410829`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:5594` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:45535`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:45535` at `data/seed/scope.tsv:52640`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:45535`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:36042` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:45535`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 13 exact `NCBITaxon:45535` rows for `Sugiyamaella castrensis`, including NRRL Y-17329 culture-from-holotype and ATCC, CBS, IGC, IJFM, and JCM type-material designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 2 direct exact records and 9 exact deposit placements for `NCBITaxon:45535`; the exact JSONL search found 2 records carrying `"ncbi":45535`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:45535`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:45535` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
