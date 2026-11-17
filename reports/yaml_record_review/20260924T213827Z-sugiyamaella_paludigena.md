# YAML Record Review: Sugiyamaella paludigena

- Verdict: pass
- Target: `data/taxa/eukaryota/sugiyamaella_paludigena.yaml`
- Identifier: `NCBITaxon:45575`

## Target

Reviewed the complete 79-line YAML record for Sugiyamaella paludigena. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sugiyamaella_paludigena`.

## Validation

- `just validate data/taxa/eukaryota/sugiyamaella_paludigena.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sugiyamaella_mastotermitis.yaml data/taxa/eukaryota/sugiyamaella_neomexicana.yaml data/taxa/eukaryota/sugiyamaella_novakii.yaml data/taxa/eukaryota/sugiyamaella_paludigena.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:45575`, `label: Sugiyamaella paludigena`, `rank: SPECIES`, `parent_taxon: NCBITaxon:410829`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:5622` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:45575`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:45575` at `data/seed/scope.tsv:52668`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:45575`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:36077` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:45575`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 16 exact `NCBITaxon:45575` rows under `Candida paludigena`, including NRRL Y-12697 culture-from-holotype and ATCC, CBS, IFO, IGC, JCM, and VKM type-material designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 5 direct exact records and 23 exact deposit placements for `NCBITaxon:45575`; the exact JSONL search found 6 records carrying `"ncbi":45575`, including one non-direct `Sugiyamaella castrensis` record, StrainInfo `65905`, with one exact `NCBITaxon:45575` deposit.
- No exact BacDive rows referenced `NCBITaxon:45575`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:45575` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
