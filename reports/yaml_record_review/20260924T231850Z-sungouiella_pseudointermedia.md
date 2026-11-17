# YAML Record Review: Sungouiella pseudointermedia

- Verdict: pass
- Target: `data/taxa/eukaryota/sungouiella_pseudointermedia.yaml`
- Identifier: `NCBITaxon:46585`

## Target

Reviewed the complete 79-line YAML record for Sungouiella pseudointermedia. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sungouiella_pseudointermedia`.

## Validation

- `just validate data/taxa/eukaryota/sungouiella_pseudointermedia.yaml` exited successfully and LinkML reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sungouiella_pseudoflosculorum.yaml data/taxa/eukaryota/sungouiella_pseudointermedia.yaml data/taxa/eukaryota/sungouiella_sharkensis.yaml data/taxa/eukaryota/sungouiella_suratensis.yaml` scanned all four batch records and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The record retains `identifier: NCBITaxon:46585`, `label: Sungouiella pseudointermedia`, `rank: SPECIES`, `parent_taxon: NCBITaxon:3315605`, `genetic_code: 12`, and the NCBI `taxonomy_snapshot` dated `2026-09-13`; `data/raw/ncbitaxon_taxa.tsv:5858` retains the same current species row.
- NCBI lists 1 exact synonym, 0 broad synonyms, and 2 related synonyms for `NCBITaxon:46585`; the YAML carries the same three synonym entries.
- The seeded-scope search found exactly one row for `NCBITaxon:46585` at `data/seed/scope.tsv:52709`.
- All 13 YAML lineage entries were checked against current NCBI rows, with no missing ancestors and no parent, label, or rank mismatches.
- `data/raw/ncbi_merged_ids.tsv` contains no retired ID mapped into `NCBITaxon:46585`.

## Evidence

- The single aggregate GOLD row at `data/raw/gold_taxon_summary.tsv:36326` reports `organism_count=1`, matching the YAML GOLD source attestation.
- Native GOLD contained 1 organism row and 1 project row for `NCBITaxon:46585`; no GOLD analysis rows used that taxon ID.
- `data/raw/ncbi_type_material.tsv` contains 18 exact `NCBITaxon:46585` rows for `Candida pseudointermedia`, covering AJ 4481, ATCC 60126, BCRC 22401, CBS 6918, CCRC 22401, IFO 1693, JCM 1592, NCYC 2610, and NRRL Y-10939 type-material variants from `typematerial.dmp`.
- StrainInfo contained 20 direct strain records and 36 exact deposit rows for `NCBITaxon:46585`; no exact BacDive rows referenced the taxon ID.

## Completeness

- Generated raw strain tables had no rows for `NCBITaxon:46585` in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, or `data/raw/strain_related_records.tsv`.
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
