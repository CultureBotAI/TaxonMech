# YAML Record Review: Staphylotrichum longicolle

- Verdict: pass
- Target: `data/taxa/eukaryota/staphylotrichum_longicolle.yaml`
- Identifier: `NCBITaxon:669026`

## Target

Reviewed the complete 88-line YAML record for Staphylotrichum longicolle. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `staphylotrichum_longicolle`.

## Validation

- `just validate data/taxa/eukaryota/staphylotrichum_longicolle.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stagonosporopsis_tanaceti.yaml data/taxa/eukaryota/stanjemonium_grisellum.yaml data/taxa/eukaryota/staphylotrichum_longicolle.yaml data/taxa/eukaryota/starmera_amethionina.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:155007` keeps `NCBITaxon:669026` as `Staphylotrichum longicolle`, rank `SPECIES`, parent `NCBITaxon:370954`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:56324` keeps `NCBITaxon:669026` because `Staphylotrichum longicolle` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- Checked all 16 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- `NCBITaxon:1737314` is retired into `NCBITaxon:669026` at `data/raw/ncbi_merged_ids.tsv:25833`; the exact ignored-file-inclusive merged-ID check found no retained `data/raw/ncbitaxon_taxa.tsv` row for the old identifier.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:40868` is the only aggregate row for `NCBITaxon:669026` and reports organism count `3`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 2 organism rows, 2 project rows, and 1 analysis row.
- Local NCBI type-material evidence had 0 exact rows for `NCBITaxon:669026`.
- Local StrainInfo evidence had 1 direct strain row and 1 exact deposit row for `NCBITaxon:669026`; an exact numeric-boundary check found one record carrying `"ncbi":669026}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:669026`.

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
