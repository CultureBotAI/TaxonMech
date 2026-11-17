# YAML Record Review: Sungouiella berkhoutiae

- Verdict: pass
- Target: `data/taxa/eukaryota/sungouiella_berkhoutiae.yaml`
- Identifier: `NCBITaxon:432108`

## Target

Reviewed the complete 82-line YAML record for Sungouiella berkhoutiae. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sungouiella_berkhoutiae`.

## Validation

- `just validate data/taxa/eukaryota/sungouiella_berkhoutiae.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suillus_volcanalis.yaml data/taxa/eukaryota/suillus_weaverae.yaml data/taxa/eukaryota/sundstroemia_setigera.yaml data/taxa/eukaryota/sungouiella_berkhoutiae.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:432108`, `label: Sungouiella berkhoutiae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3315605`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:95500` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:432108`; the YAML carries the same four synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:432108` at `data/seed/scope.tsv:55635`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv:73860` maps retired ID `NCBITaxon:374335` into `NCBITaxon:432108`, and the exact merged-ID search found no retained row for the retired ID in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:35329` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:432108`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 11 exact `NCBITaxon:432108` rows for `Candida berkhoutiae`, covering CBS 11722, NBRC 106733, and BCC 7749 type-material variants from `typematerial.dmp`.
- No exact StrainInfo or BacDive rows referenced `NCBITaxon:432108`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:432108` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
