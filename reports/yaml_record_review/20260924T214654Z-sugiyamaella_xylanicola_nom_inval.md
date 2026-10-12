# YAML Record Review: Sugiyamaella xylanicola (nom. inval.)

- Verdict: pass
- Target: `data/taxa/eukaryota/sugiyamaella_xylanicola_nom_inval.yaml`
- Identifier: `NCBITaxon:1234609`

## Target

Reviewed the complete 81-line YAML record for Sugiyamaella xylanicola (nom. inval.). The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sugiyamaella_xylanicola_nom_inval`.

## Validation

- `just validate data/taxa/eukaryota/sugiyamaella_xylanicola_nom_inval.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sugiyamaella_xylanicola_nom_inval.yaml data/taxa/eukaryota/suhomyces_ambrosiae.yaml data/taxa/eukaryota/suhomyces_anneliseae.yaml data/taxa/eukaryota/suhomyces_atakaporum.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:1234609`, `label: Sugiyamaella xylanicola (nom. inval.)`, `rank: SPECIES`, `parent_taxon: NCBITaxon:2622548`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:282399` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:1234609`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1234609` at `data/seed/scope.tsv:58609`.
- All 14 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:1234609`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:5610` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row, 1 project row, and 1 analysis row for `NCBITaxon:1234609`.
- No exact NCBI type-material rows referenced `NCBITaxon:1234609`.
- No local StrainInfo rows or exact BacDive rows referenced `NCBITaxon:1234609`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1234609` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
