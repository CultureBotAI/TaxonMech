# YAML Record Review: Suillus acidus

- Verdict: pass
- Target: `data/taxa/eukaryota/suillus_acidus.yaml`
- Identifier: `NCBITaxon:1904412`

## Target

Reviewed the complete 92-line YAML record for Suillus acidus. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suillus_acidus`.

## Validation

- `just validate data/taxa/eukaryota/suillus_acidus.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suhomyces_yuchorum.yaml data/taxa/eukaryota/suillellus_queletii.yaml data/taxa/eukaryota/suillus_acidus.yaml data/taxa/eukaryota/suillus_alpinus.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:1904412`, `label: Suillus acidus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5379`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:492359` retains the same current species row.
- NCBI lists 3 exact synonyms, 0 broad synonyms, and 4 related synonyms for `NCBITaxon:1904412`; the YAML carries the same 7 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1904412` at `data/seed/scope.tsv:61514`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps 2 retired IDs into `NCBITaxon:1904412`; the exact ignored-file-inclusive search over `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only those 2 merged-ID rows and no retained old-ID taxon rows.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:17215` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 2 project rows for `NCBITaxon:1904412`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 4 exact `NCBITaxon:1904412` rows, covering `Suillus lutescens` MICH 340781 holotype variants and `Suillus subolivaceus` MICH 340785 holotype variants from `typematerial.dmp`.
- Local StrainInfo records contained 2 direct exact records and 2 exact deposit placements for `NCBITaxon:1904412`; the exact JSONL search found 2 direct records carrying `"ncbi":1904412`.
- No exact BacDive rows referenced `NCBITaxon:1904412`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1904412` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
