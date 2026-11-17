# YAML Record Review: Sporothrix dombeyi

- Verdict: pass
- Target: `data/taxa/eukaryota/sporothrix_dombeyi.yaml`
- Identifier: `NCBITaxon:1892476`

## Target

Reviewed the complete 87-line YAML record for Sporothrix dombeyi. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sporothrix_dombeyi`.

## Validation

- `just validate data/taxa/eukaryota/sporothrix_dombeyi.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporopachydermia_quercuum.yaml data/taxa/eukaryota/sporormiaceae_sp.yaml data/taxa/eukaryota/sporothrix_dombeyi.yaml data/taxa/eukaryota/sporothrix_globosa.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:491171` keeps `NCBITaxon:1892476` as `Sporothrix dombeyi`, rank `SPECIES`, parent `NCBITaxon:29907`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:61472` keeps `NCBITaxon:1892476` because `Sporothrix dombeyi` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 2 exact synonyms, 1 related synonym, and 0 broad synonyms.
- Checked all 16 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:1892476`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:17059` is the only aggregate row for `NCBITaxon:1892476` and reports organism count `3`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 3 organism rows, 0 project rows, and 0 analysis rows.
- Local NCBI type-material evidence had 2 exact `NCBITaxon:1892476` rows, both from `typematerial.dmp`, covering CBS 455.83 culture-from-isotype alias spellings.
- Local StrainInfo evidence had 1 direct strain row and 2 exact deposit rows for `NCBITaxon:1892476`; an exact numeric-boundary check found one record carrying `"ncbi":1892476}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:1892476`.

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
