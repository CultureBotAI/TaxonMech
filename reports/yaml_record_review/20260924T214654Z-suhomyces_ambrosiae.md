# YAML Record Review: Suhomyces ambrosiae

- Verdict: pass
- Target: `data/taxa/eukaryota/suhomyces_ambrosiae.yaml`
- Identifier: `NCBITaxon:147332`

## Target

Reviewed the complete 90-line YAML record for Suhomyces ambrosiae. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suhomyces_ambrosiae`.

## Validation

- `just validate data/taxa/eukaryota/suhomyces_ambrosiae.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sugiyamaella_xylanicola_nom_inval.yaml data/taxa/eukaryota/suhomyces_ambrosiae.yaml data/taxa/eukaryota/suhomyces_anneliseae.yaml data/taxa/eukaryota/suhomyces_atakaporum.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:147332`, `label: Suhomyces ambrosiae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1539666`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:30035` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 6 related synonyms for `NCBITaxon:147332`; the YAML carries the same 7 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:147332` at `data/seed/scope.tsv:54040`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps four retired IDs into `NCBITaxon:147332`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only those four merged-ID rows and no retained old-ID taxon rows.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:11386` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:147332`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 5 exact `NCBITaxon:147332` rows under `Candida ambrosiae`, including CBS 8844 and NRRL YB-1316 type-material designation variants from `typematerial.dmp`.
- Local StrainInfo records contained 2 direct exact records and 4 exact deposit placements for `NCBITaxon:147332`; the exact JSONL search found 2 records carrying `"ncbi":147332`, matching the direct-record count.
- No exact BacDive rows referenced `NCBITaxon:147332`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:147332` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
