# YAML Record Review: Suhomyces anneliseae

- Verdict: pass
- Target: `data/taxa/eukaryota/suhomyces_anneliseae.yaml`
- Identifier: `NCBITaxon:246025`

## Target

Reviewed the complete 190-line YAML record for Suhomyces anneliseae. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `suhomyces_anneliseae`.

## Validation

- `just validate data/taxa/eukaryota/suhomyces_anneliseae.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sugiyamaella_xylanicola_nom_inval.yaml data/taxa/eukaryota/suhomyces_ambrosiae.yaml data/taxa/eukaryota/suhomyces_anneliseae.yaml data/taxa/eukaryota/suhomyces_atakaporum.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:246025`, `label: Suhomyces anneliseae`, `rank: SPECIES`, `parent_taxon: NCBITaxon:1539666`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:48264` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 39 related synonyms for `NCBITaxon:246025`; the YAML carries the same 40 synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:246025` at `data/seed/scope.tsv:54728`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` maps 36 retired IDs into `NCBITaxon:246025`; the exact ignored-file-inclusive search of `data/raw/ncbi_merged_ids.tsv` and `data/raw/ncbitaxon_taxa.tsv` matched only those 36 merged-ID rows and no retained old-ID taxon rows.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:22136` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:246025`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 10 exact `NCBITaxon:246025` rows under `Candida anneliseae`, including ATCC MYA-4321 culture-from-type-material and BG 99-8-11-1-2-2, CBS 9837, and NRRL Y-27563 type-material designation variants from `typematerial.dmp`.
- No local StrainInfo rows or exact BacDive rows referenced `NCBITaxon:246025`.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:246025` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
