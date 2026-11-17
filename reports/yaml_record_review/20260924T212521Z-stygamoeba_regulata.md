# YAML Record Review: Stygamoeba regulata

- Verdict: pass
- Target: `data/taxa/eukaryota/stygamoeba_regulata.yaml`
- Identifier: `NCBITaxon:1042828`

## Target

Reviewed the complete 54-line YAML record for Stygamoeba regulata. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stygamoeba_regulata`.

## Validation

- `just validate data/taxa/eukaryota/stygamoeba_regulata.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/strombidium_rassoulzadegani.yaml data/taxa/eukaryota/strombidium_stylifer.yaml data/taxa/eukaryota/stropharia_rugosoannulata.yaml data/taxa/eukaryota/stygamoeba_regulata.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:1042828`, `label: Stygamoeba regulata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:373141`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:224112` retains the same current species row.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 1 related synonym for `NCBITaxon:1042828`; the YAML carries the same single synonym entry.
- The seeded-scope search found exactly one row for `NCBITaxon:1042828` at `data/seed/scope.tsv:57282`.
- All 7 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:1042828`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:626` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row for `NCBITaxon:1042828`; no GOLD project or analysis rows used that taxon ID.
- No exact NCBI type-material rows referenced `NCBITaxon:1042828`.
- Local StrainInfo records contained 1 direct exact record and 1 exact deposit placement for `NCBITaxon:1042828`; the exact JSONL search found 1 record carrying `"ncbi":1042828`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:1042828`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1042828` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
