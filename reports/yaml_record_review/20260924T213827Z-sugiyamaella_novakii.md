# YAML Record Review: Sugiyamaella novakii

- Verdict: pass
- Target: `data/taxa/eukaryota/sugiyamaella_novakii.yaml`
- Identifier: `NCBITaxon:279894`

## Target

Reviewed the complete 85-line YAML record for Sugiyamaella novakii. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sugiyamaella_novakii`.

## Validation

- `just validate data/taxa/eukaryota/sugiyamaella_novakii.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sugiyamaella_mastotermitis.yaml data/taxa/eukaryota/sugiyamaella_neomexicana.yaml data/taxa/eukaryota/sugiyamaella_novakii.yaml data/taxa/eukaryota/sugiyamaella_paludigena.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:279894`, `label: Sugiyamaella novakii`, `rank: SPECIES`, `parent_taxon: NCBITaxon:410829`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:56936` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 4 related synonyms for `NCBITaxon:279894`; the YAML carries the same 5 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:279894` at `data/seed/scope.tsv:54953`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps two retired IDs, `NCBITaxon:2898198` and `NCBITaxon:2898200`, into `NCBITaxon:279894`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only those merged-ID rows and no retained old-ID taxon rows.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:26756` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:279894`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 7 exact `NCBITaxon:279894` rows for `Sugiyamaella novakii`, including NRRL Y-27346 culture-from-holotype and CBS 8402 and NCAIM Y 00986 type-material designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 2 direct exact records and 10 exact deposit placements for `NCBITaxon:279894`; the exact JSONL search found 2 records carrying `"ncbi":279894`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:279894`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:279894` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
