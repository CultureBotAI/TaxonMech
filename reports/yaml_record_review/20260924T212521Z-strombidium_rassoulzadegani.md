# YAML Record Review: Strombidium rassoulzadegani

- Verdict: pass
- Target: `data/taxa/eukaryota/strombidium_rassoulzadegani.yaml`
- Identifier: `NCBITaxon:1082188`

## Target

Reviewed the complete 72-line YAML record for Strombidium rassoulzadegani. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `strombidium_rassoulzadegani`.

## Validation

- `just validate data/taxa/eukaryota/strombidium_rassoulzadegani.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/strombidium_rassoulzadegani.yaml data/taxa/eukaryota/strombidium_stylifer.yaml data/taxa/eukaryota/stropharia_rugosoannulata.yaml data/taxa/eukaryota/stygamoeba_regulata.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:1082188`, `label: Strombidium rassoulzadegani`, `rank: SPECIES`, `parent_taxon: NCBITaxon:60005`, `genetic_code: 6`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:232538` retains the same current species row.
- NCBI lists 2 exact synonyms, 0 broad synonyms, and 1 related synonym for `NCBITaxon:1082188`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1082188` at `data/seed/scope.tsv:57561`.
- All 11 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps two retired IDs, `NCBITaxon:693418` and `NCBITaxon:693434`, into `NCBITaxon:1082188`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only those merged-ID rows and no retained old-ID taxon rows.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:1525` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row for `NCBITaxon:1082188`; no GOLD project or analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 4 exact `NCBITaxon:1082188` rows for `Strombidium rassoulzadegani`, all USNM 1137682 holotype designation variants from `typematerial.dmp`.
- No local StrainInfo rows or exact BacDive rows referenced `NCBITaxon:1082188`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1082188` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
