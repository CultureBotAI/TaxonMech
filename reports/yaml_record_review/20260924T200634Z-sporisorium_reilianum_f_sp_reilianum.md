# YAML Record Review: Sporisorium reilianum f. sp. reilianum

- Verdict: pass
- Target: `data/taxa/eukaryota/sporisorium_reilianum_f_sp_reilianum.yaml`
- Identifier: `NCBITaxon:72559`

## Target

Reviewed the complete 68-line YAML record for Sporisorium reilianum f. sp. reilianum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sporisorium_reilianum_f_sp_reilianum`.

## Validation

- `just validate data/taxa/eukaryota/sporisorium_reilianum_f_sp_reilianum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporisorium_reilianum_f_sp_reilianum.yaml data/taxa/eukaryota/sporisorium_scitamineum.yaml data/taxa/eukaryota/sporopachydermia_cereana.yaml data/taxa/eukaryota/sporopachydermia_lactativora.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:10145` keeps `NCBITaxon:72559` as `Sporisorium reilianum f. sp. reilianum`, rank `FORMA_SPECIALIS`, parent `NCBITaxon:72558`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:53244` keeps `NCBITaxon:72559` because `Sporisorium reilianum f. sp. reilianum` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 0 exact synonyms, 0 related synonyms, and 0 broad synonyms.
- Checked all 13 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:72559`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:42015` is the only aggregate row for `NCBITaxon:72559` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 1 organism row, 1 project row, and 1 analysis row.
- Local NCBI type-material evidence had 0 exact rows for `NCBITaxon:72559`.
- Local StrainInfo evidence had 0 direct strain rows and 0 exact deposit rows for `NCBITaxon:72559`.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:72559`.

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
