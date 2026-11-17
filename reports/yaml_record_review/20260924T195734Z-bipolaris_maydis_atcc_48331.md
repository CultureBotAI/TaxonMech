# YAML Record Review: Bipolaris maydis ATCC 48331

- Verdict: pass
- Target: `data/taxa/eukaryota/bipolaris_maydis_atcc_48331.yaml`
- Identifier: `NCBITaxon:665024`

## Target

Reviewed the complete 90-line YAML record for Bipolaris maydis ATCC 48331. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `bipolaris_maydis_atcc_48331`.

## Validation

- `just validate data/taxa/eukaryota/bipolaris_maydis_atcc_48331.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/baudoinia_panamericana_uamh_10762.yaml data/taxa/eukaryota/bigelowiella_natans_ccmp2755.yaml data/taxa/eukaryota/bipolaris_maydis_atcc_48331.yaml data/taxa/eukaryota/bipolaris_oryzae_atcc_44560.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:154176` keeps `NCBITaxon:665024` as `Bipolaris maydis ATCC 48331`, rank `STRAIN`, parent `NCBITaxon:5016`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:56313` keeps `NCBITaxon:665024` because `Bipolaris maydis ATCC 48331` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 2 exact synonyms, 0 related synonyms, and 0 broad synonyms.
- Checked all 18 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:665024`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:40771` is the only aggregate row for `NCBITaxon:665024` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence currently has 0 organism rows, 0 project rows, and 0 analysis rows for the taxon.
- Local NCBI type-material evidence had 0 exact rows for `NCBITaxon:665024`.
- Local StrainInfo evidence had 0 direct strain rows and 0 exact deposit rows for `NCBITaxon:665024`.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:665024`.

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
