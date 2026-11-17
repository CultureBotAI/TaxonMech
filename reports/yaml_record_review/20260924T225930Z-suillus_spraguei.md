# YAML Record Review: Suillus spraguei

- Verdict: pass
- Target: `data/taxa/eukaryota/suillus_spraguei.yaml`
- Identifier: `NCBITaxon:5383`

## Target

Reviewed the complete 93-line YAML record for Suillus spraguei. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suillus_spraguei`.

## Validation

- `just validate data/taxa/eukaryota/suillus_spraguei.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suillus_spraguei.yaml data/taxa/eukaryota/suillus_subalutaceus.yaml data/taxa/eukaryota/suillus_subaureus.yaml data/taxa/eukaryota/suillus_subluteus.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:5383`, `label: Suillus spraguei`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5379`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:2382` retains the same current species row.
- NCBI lists 3 exact synonyms, 0 broad synonyms, and 4 related synonyms for `NCBITaxon:5383`; the YAML carries the same seven synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:5383` at `data/seed/scope.tsv:51982`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv:39366` maps retired ID `NCBITaxon:222705` into `NCBITaxon:5383`, and the exact merged-ID search found no retained row for the retired ID in `data/raw/ncbitaxon_taxa.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:38245` reports `organism_count=4`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 analysis row, 3 organism rows, and 4 project rows for `NCBITaxon:5383`.
- `data/raw/ncbi_type_material.tsv` contains no exact rows for `NCBITaxon:5383`.
- StrainInfo contained 2 direct strain records and 2 exact deposit rows for `NCBITaxon:5383`; no exact BacDive rows referenced the taxon ID.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:5383` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
