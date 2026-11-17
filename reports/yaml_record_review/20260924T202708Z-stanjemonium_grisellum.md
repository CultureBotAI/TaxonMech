# YAML Record Review: Stanjemonium grisellum

- Verdict: pass
- Target: `data/taxa/eukaryota/stanjemonium_grisellum.yaml`
- Identifier: `NCBITaxon:73508`

## Target

Reviewed the complete 81-line YAML record for Stanjemonium grisellum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stanjemonium_grisellum`.

## Validation

- `just validate data/taxa/eukaryota/stanjemonium_grisellum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stagonosporopsis_tanaceti.yaml data/taxa/eukaryota/stanjemonium_grisellum.yaml data/taxa/eukaryota/staphylotrichum_longicolle.yaml data/taxa/eukaryota/starmera_amethionina.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:10321` keeps `NCBITaxon:73508` as `Stanjemonium grisellum`, rank `SPECIES`, parent `NCBITaxon:73506`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:53256` keeps `NCBITaxon:73508` because `Stanjemonium grisellum` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- Checked all 16 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:73508`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:42062` is the only aggregate row for `NCBITaxon:73508` and reports organism count `2`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 1 organism row, 2 project rows, and 0 analysis rows.
- Local NCBI type-material evidence had 2 exact `NCBITaxon:73508` rows, both from `typematerial.dmp`, covering CBS 655.79 holotype alias spellings.
- Local StrainInfo evidence had 3 direct strain rows and 6 exact deposit rows for `NCBITaxon:73508`; an exact numeric-boundary check found 3 records carrying `"ncbi":73508}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:73508`.

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
