# YAML Record Review: Starmerella lactis-condensi

- Verdict: pass
- Target: `data/taxa/eukaryota/starmerella_lactis_condensi.yaml`
- Identifier: `NCBITaxon:45562`

## Target

Reviewed the complete 84-line YAML record for Starmerella lactis-condensi. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmerella_lactis_condensi`.

## Validation

- `just validate data/taxa/eukaryota/starmerella_lactis_condensi.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmerella_floris.yaml data/taxa/eukaryota/starmerella_khaoyaiensis.yaml data/taxa/eukaryota/starmerella_lactis_condensi.yaml data/taxa/eukaryota/starmerella_powellii.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:45562`, `label: Starmerella lactis-condensi`, `rank: SPECIES`, `parent: NCBITaxon:75735`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 2 exact synonyms, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:45562`; the YAML carries the same 5 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:45562` in `data/seed/scope.tsv`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- No retired IDs were mapped into `NCBITaxon:45562` in `data/raw/ncbi_merged_ids.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:36069` reports `organism_count=9`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 9 organism rows and 1 project row for `NCBITaxon:45562`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 19 exact `NCBITaxon:45562` rows under `Torula lactis-condensi`, including ATCC, CBS, IFO, JCM, NRRL, and VKM type-material designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 5 direct exact records and 22 exact deposit placements for `NCBITaxon:45562`; the exact JSONL search found 6 records carrying `"ncbi":45562`, including one `Cryptococcus neoformans var. neoformans` primary record with an exact `S. lactis-condensi` deposit.
- No exact BacDive rows referenced `NCBITaxon:45562`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:45562` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
