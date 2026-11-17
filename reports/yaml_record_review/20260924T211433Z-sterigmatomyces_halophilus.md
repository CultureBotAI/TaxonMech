# YAML Record Review: Sterigmatomyces halophilus

- Verdict: pass
- Target: `data/taxa/eukaryota/sterigmatomyces_halophilus.yaml`
- Identifier: `NCBITaxon:5617`

## Target

Reviewed the complete 72-line YAML record for Sterigmatomyces halophilus. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sterigmatomyces_halophilus`.

## Validation

- `just validate data/taxa/eukaryota/sterigmatomyces_halophilus.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sterigmatomyces_halophilus.yaml data/taxa/eukaryota/sterigmatomyces_hyphaenes.yaml data/taxa/eukaryota/sterigmatosporidium_polymorphum.yaml data/taxa/eukaryota/sterkiella_histriomuscorum.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:5617`, `label: Sterigmatomyces halophilus`, `rank: SPECIES`, `parent_taxon: NCBITaxon:5615`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:2495` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 1 related synonym for `NCBITaxon:5617`; the YAML carries the same 2 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:5617` at `data/seed/scope.tsv:52045`.
- All 12 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:5617`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:38856` reports `organism_count=7`, matching the YAML GOLD source attestation.
- Native GOLD contained 6 organism rows for `NCBITaxon:5617`; no GOLD project or analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 16 exact `NCBITaxon:5617` rows for `Sterigmatomyces halophilus`, including ATCC, BCRC, CBS, CCRC, DBVPG, IFO, JCM, and NRRL type-material designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 17 direct exact records and 54 exact deposit placements for `NCBITaxon:5617`; the exact JSONL search found 17 records carrying `"ncbi":5617`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:5617`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:5617` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
