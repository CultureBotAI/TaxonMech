# YAML Record Review: Streblomastix strix

- Verdict: pass
- Target: `data/taxa/eukaryota/streblomastix_strix.yaml`
- Identifier: `NCBITaxon:222440`

## Target

Reviewed the complete 53-line YAML record for Streblomastix strix. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `streblomastix_strix`.

## Validation

- `just validate data/taxa/eukaryota/streblomastix_strix.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stipitochalara_longipes_bdj.yaml data/taxa/eukaryota/stomiopeltis_betulae.yaml data/taxa/eukaryota/storeatula_major.yaml data/taxa/eukaryota/streblomastix_strix.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:222440`, `label: Streblomastix strix`, `rank: SPECIES`, `parent_taxon: NCBITaxon:222439`, `genetic_code: 6`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:43746` retains the same current species row.
- NCBI lists 0 exact synonyms, 0 broad synonyms, and 0 related synonyms for `NCBITaxon:222440`; the YAML likewise carries no synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:222440` at `data/seed/scope.tsv:54602`.
- All 8 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:222440`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:21089` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 analysis row for `NCBITaxon:222440`; no GOLD project rows used that taxon ID.
- No exact NCBI type-material rows referenced `NCBITaxon:222440`.
- No local StrainInfo rows or exact BacDive rows referenced `NCBITaxon:222440`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:222440` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
