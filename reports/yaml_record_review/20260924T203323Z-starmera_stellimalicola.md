# YAML Record Review: Starmera stellimalicola

- Verdict: pass
- Target: `data/taxa/eukaryota/starmera_stellimalicola.yaml`
- Identifier: `NCBITaxon:56415`

## Target

Reviewed the complete 79-line YAML record for Starmera stellimalicola. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmera_stellimalicola`.

## Validation

- `just validate data/taxa/eukaryota/starmera_stellimalicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmera_caribaea.yaml data/taxa/eukaryota/starmera_pachycereana.yaml data/taxa/eukaryota/starmera_stellimalicola.yaml data/taxa/eukaryota/starmerella_apicola.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:7090` keeps `NCBITaxon:56415` as `Starmera stellimalicola`, rank `SPECIES`, parent `NCBITaxon:83173`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:52959` keeps `NCBITaxon:56415` because `Starmera stellimalicola` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- Checked all 13 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:56415`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:38919` is the only aggregate row for `NCBITaxon:56415` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 1 organism row, 2 project rows, and 2 analysis rows.
- Local NCBI type-material evidence had 6 exact `NCBITaxon:56415` rows, all from `typematerial.dmp`, covering CBS 7853, JCM 3546, and NRRL Y-17912 culture-from-type-material alias spellings.
- Local StrainInfo evidence had 3 direct strain rows and 11 exact deposit rows for `NCBITaxon:56415`; an exact numeric-boundary check found 3 records carrying `"ncbi":56415}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:56415`.

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
