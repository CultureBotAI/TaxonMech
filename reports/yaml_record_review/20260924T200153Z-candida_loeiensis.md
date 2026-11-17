# YAML Record Review: [Candida] loeiensis

- Verdict: pass
- Target: `data/taxa/eukaryota/candida_loeiensis.yaml`
- Identifier: `NCBITaxon:931974`

## Target

Reviewed the complete 88-line YAML record for [Candida] loeiensis. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `candida_loeiensis`.

## Validation

- `just validate data/taxa/eukaryota/candida_loeiensis.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/bipolaris_sorokiniana_nd90pr.yaml data/taxa/eukaryota/candida_loeiensis.yaml data/taxa/eukaryota/soucietia_sequanensis.yaml data/taxa/eukaryota/sporisorium_iseilematis_ciliati.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:196545` keeps `NCBITaxon:931974` as `[Candida] loeiensis`, rank `SPECIES`, parent `NCBITaxon:1540040`, genetic code `12`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:56938` keeps `NCBITaxon:931974` because `[Candida] loeiensis` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 1 exact synonym, 4 related synonyms, and 0 broad synonyms.
- Checked all 14 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- `NCBITaxon:931975` is retired into `NCBITaxon:931974` at `data/raw/ncbi_merged_ids.tsv:99258`; the exact ignored-file-inclusive merged-ID check found no retained `data/raw/ncbitaxon_taxa.tsv` row for the old identifier.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:44735` is the only aggregate row for `NCBITaxon:931974` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 1 organism row, 1 project row, and 0 analysis rows.
- Local NCBI type-material evidence had 9 exact `NCBITaxon:931974` rows, all from `typematerial.dmp`, covering BCC 17239, CBS 11899, NBRC 106731, and ST-720 holotype or culture-from-holotype alias spellings.
- Local StrainInfo evidence had 0 direct strain rows and 0 exact deposit rows for `NCBITaxon:931974`.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:931974`.

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
