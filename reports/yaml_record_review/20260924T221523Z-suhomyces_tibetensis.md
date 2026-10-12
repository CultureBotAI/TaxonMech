# YAML Record Review: Suhomyces tibetensis

- Verdict: pass
- Target: `data/taxa/eukaryota/suhomyces_tibetensis.yaml`
- Identifier: `NCBITaxon:356546`

## Target

Reviewed the complete 82-line YAML record for Suhomyces tibetensis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suhomyces_tibetensis`.

## Validation

- `just validate data/taxa/eukaryota/suhomyces_tibetensis.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/suhomyces_tibetensis.yaml data/taxa/eukaryota/suhomyces_vadensis.yaml data/taxa/eukaryota/suhomyces_wounanorum.yaml data/taxa/eukaryota/suhomyces_xylopsoci.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:356546`, `label: Suhomyces tibetensis`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1539666`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:73504` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:356546`; the YAML carries the same 4 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:356546` at `data/seed/scope.tsv:55334`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:356546`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:33096` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:356546`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 6 exact `NCBITaxon:356546` rows for `Candida tibetensis`, covering CBS 10298 culture-from-holotype variants plus AS 2.3072, CGMCC 2.3072, and XZ 41-6 holotype variants from `typematerial.dmp`.
- Local StrainInfo records contained 3 direct exact records and 5 exact deposit placements for `NCBITaxon:356546`; the exact JSONL search found 3 direct records carrying `"ncbi":356546`.
- No exact BacDive rows referenced `NCBITaxon:356546`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:356546` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
