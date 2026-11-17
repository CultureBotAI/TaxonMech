# YAML Record Review: Suillus weaverae

- Verdict: pass
- Target: `data/taxa/eukaryota/suillus_weaverae.yaml`
- Identifier: `NCBITaxon:48593`

## Target

Reviewed the complete 81-line YAML record for Suillus weaverae. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suillus_weaverae`.

## Validation

- `just validate data/taxa/eukaryota/suillus_weaverae.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suillus_volcanalis.yaml data/taxa/eukaryota/suillus_weaverae.yaml data/taxa/eukaryota/sundstroemia_setigera.yaml data/taxa/eukaryota/sungouiella_berkhoutiae.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:48593`, `label: Suillus weaverae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5379`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:6209` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:48593`; the YAML carries the same three synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:48593` at `data/seed/scope.tsv:52781`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:48593`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:36908` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 2 project rows for `NCBITaxon:48593`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 2 exact `NCBITaxon:48593` rows for `Fuscoboletinus weaverae`, covering MICH 10563 holotype variants from `typematerial.dmp`.
- No exact StrainInfo or BacDive rows referenced `NCBITaxon:48593`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:48593` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
