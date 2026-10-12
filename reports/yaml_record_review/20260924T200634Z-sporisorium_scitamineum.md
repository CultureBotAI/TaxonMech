# YAML Record Review: Sporisorium scitamineum

- Verdict: pass
- Target: `data/taxa/eukaryota/sporisorium_scitamineum.yaml`
- Identifier: `NCBITaxon:49012`

## Target

Reviewed the complete 75-line YAML record for Sporisorium scitamineum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sporisorium_scitamineum`.

## Validation

- `just validate data/taxa/eukaryota/sporisorium_scitamineum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporisorium_reilianum_f_sp_reilianum.yaml data/taxa/eukaryota/sporisorium_scitamineum.yaml data/taxa/eukaryota/sporopachydermia_cereana.yaml data/taxa/eukaryota/sporopachydermia_lactativora.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:6232` keeps `NCBITaxon:49012` as `Sporisorium scitamineum`, rank `SPECIES`, parent `NCBITaxon:63265`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:52786` keeps `NCBITaxon:49012` because `Sporisorium scitamineum` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- Checked all 12 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:49012`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:37069` is the only aggregate row for `NCBITaxon:49012` and reports organism count `4`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 5 organism rows, 6 project rows, and 3 analysis rows.
- Local NCBI type-material evidence had 0 exact rows for `NCBITaxon:49012`.
- Local StrainInfo evidence had 11 direct strain rows and 13 exact deposit rows for `NCBITaxon:49012`; an exact numeric-boundary check found 11 records carrying `"ncbi":49012}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:49012`.

## Completeness

- Generated raw strain tables had 0 target rows in `data/raw/bacdive_strains.tsv`, `data/raw/culture_collection_strains.tsv`, `data/raw/strain_assemblies.tsv`, `data/raw/strain_genome_records.tsv`, and `data/raw/strain_related_records.tsv`.
- Auxiliary raw source tables had 0 exact target rows in `data/raw/bactotraits_taxa.tsv`, `data/raw/gtdb_mappings.tsv`, `data/raw/gtdb_species.tsv`, `data/raw/lpsn_names.tsv`, `data/raw/madin_taxa.tsv`, and `data/raw/mediadive_taxa.tsv`.
- Generated StrainInfo overlay tables had 0 target rows in `data/straininfo/assemblies.tsv`, `data/straininfo/exclusions.tsv`, and `data/straininfo/related_records.tsv.gz`.

## Findings

No findings.

## Recommended Edits

No edits are recommended.

## Follow-up Checks

No follow-up checks are required.

## Additional Notes

None.
