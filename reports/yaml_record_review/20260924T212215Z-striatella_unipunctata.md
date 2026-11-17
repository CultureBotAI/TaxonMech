# YAML Record Review: Striatella unipunctata

- Verdict: pass
- Target: `data/taxa/eukaryota/striatella_unipunctata.yaml`
- Identifier: `NCBITaxon:210618`

## Target

Reviewed the complete 72-line YAML record for Striatella unipunctata. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `striatella_unipunctata`.

## Validation

- `just validate data/taxa/eukaryota/striatella_unipunctata.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/striatella_unipunctata.yaml data/taxa/eukaryota/stromatinia_cepivora.yaml data/taxa/eukaryota/strombidinopsis_acuminata.yaml data/taxa/eukaryota/strombidium_inclinatum.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:210618`, `label: Striatella unipunctata`, `rank: SPECIES`, `parent_taxon: NCBITaxon:210617`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:41510` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:210618`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:210618` at `data/seed/scope.tsv:54521`.
- All 11 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:210618`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:20131` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row for `NCBITaxon:210618`; no GOLD project or analysis rows used that taxon ID.
- No exact NCBI type-material rows referenced `NCBITaxon:210618`.
- No local StrainInfo rows or exact BacDive rows referenced `NCBITaxon:210618`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:210618` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
