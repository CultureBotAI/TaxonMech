# YAML Record Review: Stromatinia cepivora

- Verdict: pass
- Target: `data/taxa/eukaryota/stromatinia_cepivora.yaml`
- Identifier: `NCBITaxon:38492`

## Target

Reviewed the complete 84-line YAML record for Stromatinia cepivora. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stromatinia_cepivora`.

## Validation

- `just validate data/taxa/eukaryota/stromatinia_cepivora.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/striatella_unipunctata.yaml data/taxa/eukaryota/stromatinia_cepivora.yaml data/taxa/eukaryota/strombidinopsis_acuminata.yaml data/taxa/eukaryota/strombidium_inclinatum.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:38492`, `label: Stromatinia cepivora`, `rank: SPECIES`, `parent_taxon: NCBITaxon:66101`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:4384` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:38492`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:38492` at `data/seed/scope.tsv:52394`.
- All 15 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:38492`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:33991` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row, 1 project row, and 1 analysis row for `NCBITaxon:38492`.
- No exact NCBI type-material rows referenced `NCBITaxon:38492`.
- Local StrainInfo records contained 38 direct exact records and 46 exact deposit placements for `NCBITaxon:38492`; the exact JSONL search found 38 records carrying `"ncbi":38492`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:38492`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:38492` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
