# YAML Record Review: Suhomyces pyralidae

- Verdict: pass
- Target: `data/taxa/eukaryota/suhomyces_pyralidae.yaml`
- Identifier: `NCBITaxon:147331`

## Target

Reviewed the complete 78-line YAML record for Suhomyces pyralidae. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suhomyces_pyralidae`.

## Validation

- `just validate data/taxa/eukaryota/suhomyces_pyralidae.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suhomyces_pyralidae.yaml data/taxa/eukaryota/suhomyces_taliae.yaml data/taxa/eukaryota/suhomyces_tanzawaensis.yaml data/taxa/eukaryota/suhomyces_terraborum.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:147331`, `label: Suhomyces pyralidae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1539666`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:30034` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:147331`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:147331` at `data/seed/scope.tsv:54039`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:147331`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:11385` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 analysis row, 1 organism row, and 1 project row for `NCBITaxon:147331`.
- `data/raw/ncbi_type_material.tsv` contains 5 exact `NCBITaxon:147331` rows for `Candida pyralidae`, covering CBS 5035 and NRRL Y-27085 type-material variants from `typematerial.dmp`.
- Local StrainInfo records contained 1 direct exact record and 2 exact deposit placements for `NCBITaxon:147331`; the exact JSONL search found 1 direct record carrying `"ncbi":147331`.
- No exact BacDive rows referenced `NCBITaxon:147331`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:147331` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
