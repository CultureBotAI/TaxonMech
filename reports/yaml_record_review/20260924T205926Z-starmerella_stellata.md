# YAML Record Review: Starmerella stellata

- Verdict: pass
- Target: `data/taxa/eukaryota/starmerella_stellata.yaml`
- Identifier: `NCBITaxon:45594`

## Target

Reviewed the complete 84-line YAML record for Starmerella stellata. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmerella_stellata`.

## Validation

- `just validate data/taxa/eukaryota/starmerella_stellata.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmerella_sirachaensis.yaml data/taxa/eukaryota/starmerella_stellata.yaml data/taxa/eukaryota/starmerella_vitae.yaml data/taxa/eukaryota/stauroneis_constricta.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `id: NCBITaxon:45594`, `label: Starmerella stellata`, `rank: SPECIES`, `parent: NCBITaxon:75735`, `genetic_code: 1`, and the NCBI `taxonomy_snapshot` dated `2026-09-13` from `data/raw/ncbitaxon_taxa.tsv`.
- NCBI lists 2 exact synonyms, 0 broad synonyms, and 3 related synonyms for `NCBITaxon:45594`; the YAML carries the same 5 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:45594` in `data/seed/scope.tsv`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- No retired IDs were mapped into `NCBITaxon:45594` in `data/raw/ncbi_merged_ids.tsv`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:36086` reports `organism_count=1`, matching the YAML `knowledge_source: GOLD` assertion.
- Native GOLD contained 1 organism row for `Go0705236` and 1 project row for `Gp0831267`; no GOLD analysis rows used `NCBITaxon:45594`.
- `data/raw/ncbi_type_material.tsv` contains 23 exact `NCBITaxon:45594` rows under `Saccharomyces stellatus`, including ATCC, CBS, IFO, JCM, NCYC, NRRL, and VKM type-material designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 69 direct exact records and 105 exact deposit placements for `NCBITaxon:45594`; the exact JSONL search found 71 records carrying `"ncbi":45594`, including one `Torulaspora delbrueckii` primary record and one `Starmerella bacillaris` primary record with exact `S. stellata` deposits.
- No exact BacDive rows referenced `NCBITaxon:45594`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:45594` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
