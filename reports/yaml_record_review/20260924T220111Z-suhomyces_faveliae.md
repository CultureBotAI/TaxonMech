# YAML Record Review: Suhomyces faveliae

- Verdict: pass
- Target: `data/taxa/eukaryota/suhomyces_faveliae.yaml`
- Identifier: `NCBITaxon:1701727`

## Target

Reviewed the complete 78-line YAML record for Suhomyces faveliae. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suhomyces_faveliae`.

## Validation

- `just validate data/taxa/eukaryota/suhomyces_faveliae.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suhomyces_emberorum.yaml data/taxa/eukaryota/suhomyces_faveliae.yaml data/taxa/eukaryota/suhomyces_guaymorum.yaml data/taxa/eukaryota/suhomyces_kilbournensis.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:1701727`, `label: Suhomyces faveliae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1539666`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:443428` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:1701727`; the YAML carries the same 3 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:1701727` at `data/seed/scope.tsv:61077`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:1701727`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:14713` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:1701727`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 6 exact `NCBITaxon:1701727` rows for `Suhomyces faveliae`, covering CBS 14299 culture-from-holotype variants plus CLIB 1725 holotype variants from `typematerial.dmp`.
- No exact StrainInfo or BacDive rows referenced `NCBITaxon:1701727`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:1701727` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
