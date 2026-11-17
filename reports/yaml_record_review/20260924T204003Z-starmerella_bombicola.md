# YAML Record Review: Starmerella bombicola

- Verdict: pass
- Target: `data/taxa/eukaryota/starmerella_bombicola.yaml`
- Identifier: `NCBITaxon:75736`

## Target

Reviewed the complete 75-line YAML record for Starmerella bombicola. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmerella_bombicola`.

## Validation

- `just validate data/taxa/eukaryota/starmerella_bombicola.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmerella_asiatica.yaml data/taxa/eukaryota/starmerella_bacillaris.yaml data/taxa/eukaryota/starmerella_bombi.yaml data/taxa/eukaryota/starmerella_bombicola.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:75736`, `label: Starmerella bombicola`, `rank: SPECIES`, `parent: NCBITaxon:75735`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 1 related synonym for `NCBITaxon:75736`; the YAML carries the same 2 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:75736` in `data/seed/scope.tsv`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps one retired ID, `NCBITaxon:45527`, into `NCBITaxon:75736`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only that merged-ID row and no retained old-ID taxon row.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:42410` reports `organism_count=8`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 8 organism rows, 5 project rows, and 2 analysis rows for `NCBITaxon:75736`, including organism rows for `SB1`, `NBRC 10243`, `JCM 9596`, `NRRL Y-17069`, and `DSM 27465`.
- `data/raw/ncbi_type_material.tsv` contains 26 exact `NCBITaxon:75736` rows, including ATCC, CBS, NRRL, BCRC, CCRC, DBVPG, IFO, JCM, and NRIC type-material designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 18 direct exact records and 40 exact deposit placements for `NCBITaxon:75736`; the exact JSONL search found 18 records carrying `"ncbi":75736`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:75736`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:75736` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
