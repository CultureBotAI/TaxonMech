# YAML Record Review: Soucietia sequanensis

- Verdict: pass
- Target: `data/taxa/eukaryota/soucietia_sequanensis.yaml`
- Identifier: `NCBITaxon:45588`

## Target

Reviewed the complete 79-line YAML record for Soucietia sequanensis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `soucietia_sequanensis`.

## Validation

- `just validate data/taxa/eukaryota/soucietia_sequanensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/bipolaris_sorokiniana_nd90pr.yaml data/taxa/eukaryota/candida_loeiensis.yaml data/taxa/eukaryota/soucietia_sequanensis.yaml data/taxa/eukaryota/sporisorium_iseilematis_ciliati.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:5628` keeps `NCBITaxon:45588` as `Soucietia sequanensis`, rank `SPECIES`, parent `NCBITaxon:3315604`, genetic code `12`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:52674` keeps `NCBITaxon:45588` because `Soucietia sequanensis` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- Checked all 13 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:45588`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:36083` is the only aggregate row for `NCBITaxon:45588` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 1 organism row, 1 project row, and 0 analysis rows.
- Local NCBI type-material evidence had 16 exact `NCBITaxon:45588` rows, all from `typematerial.dmp`, covering ATCC 58862, BCRC 22416, CBS 8118, CCRC 22416, JCM 9841, MUCL 29886, and NRRL Y-17682 alias spellings.
- Local StrainInfo evidence had 1 direct strain row and 8 exact deposit rows for `NCBITaxon:45588`; an exact numeric-boundary check found one record carrying `"ncbi":45588}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:45588`.

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
