# YAML Record Review: Sugiyamaella mastotermitis

- Verdict: pass
- Target: `data/taxa/eukaryota/sugiyamaella_mastotermitis.yaml`
- Identifier: `NCBITaxon:1857663`

## Target

Reviewed the complete 80-line YAML record for Sugiyamaella mastotermitis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sugiyamaella_mastotermitis`.

## Validation

- `just validate data/taxa/eukaryota/sugiyamaella_mastotermitis.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sugiyamaella_mastotermitis.yaml data/taxa/eukaryota/sugiyamaella_neomexicana.yaml data/taxa/eukaryota/sugiyamaella_novakii.yaml data/taxa/eukaryota/sugiyamaella_paludigena.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:1857663`, `label: Sugiyamaella mastotermitis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:410829`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:485652` retains the same current species row.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:1857663`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1857663` at `data/seed/scope.tsv:61373`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:1857663`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:16583` reports `organism_count=3`, matching the YAML GOLD source attestation.
- Native GOLD contained 3 organism rows and 1 project row for `NCBITaxon:1857663`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 2 exact `NCBITaxon:1857663` rows for `Sugiyamaella mastotermitis`, both MD39 type-material designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 4 direct exact records and 4 exact deposit placements for `NCBITaxon:1857663`; the exact JSONL search found 4 records carrying `"ncbi":1857663`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:1857663`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1857663` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
