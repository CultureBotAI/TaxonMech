# YAML Record Review: Stropharia rugosoannulata

- Verdict: pass
- Target: `data/taxa/eukaryota/stropharia_rugosoannulata.yaml`
- Identifier: `NCBITaxon:68746`

## Target

Reviewed the complete 78-line YAML record for Stropharia rugosoannulata. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stropharia_rugosoannulata`.

## Validation

- `just validate data/taxa/eukaryota/stropharia_rugosoannulata.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/strombidium_rassoulzadegani.yaml data/taxa/eukaryota/strombidium_stylifer.yaml data/taxa/eukaryota/stropharia_rugosoannulata.yaml data/taxa/eukaryota/stygamoeba_regulata.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:68746`, `label: Stropharia rugosoannulata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:68745`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:9404` retains the same current species row.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:68746`; the YAML carries the same 2 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:68746` at `data/seed/scope.tsv:53167`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:68746`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:41343` reports `organism_count=6`, matching the YAML GOLD source attestation.
- Native GOLD contained 2 organism rows, 5 project rows, and 1 analysis row for `NCBITaxon:68746`.
- No exact NCBI type-material rows referenced `NCBITaxon:68746`.
- Local StrainInfo records contained 19 direct exact records and 23 exact deposit placements for `NCBITaxon:68746`; the exact JSONL search found 19 records carrying `"ncbi":68746`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:68746`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:68746` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
