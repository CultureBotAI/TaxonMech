# YAML Record Review: Sporopachydermia quercuum

- Verdict: pass
- Target: `data/taxa/eukaryota/sporopachydermia_quercuum.yaml`
- Identifier: `NCBITaxon:54094`

## Target

Reviewed the complete 75-line YAML record for Sporopachydermia quercuum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sporopachydermia_quercuum`.

## Validation

- `just validate data/taxa/eukaryota/sporopachydermia_quercuum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporopachydermia_quercuum.yaml data/taxa/eukaryota/sporormiaceae_sp.yaml data/taxa/eukaryota/sporothrix_dombeyi.yaml data/taxa/eukaryota/sporothrix_globosa.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:6838` keeps `NCBITaxon:54094` as `Sporopachydermia quercuum`, rank `SPECIES`, parent `NCBITaxon:45793`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:52909` keeps `NCBITaxon:54094` because `Sporopachydermia quercuum` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 0 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- Checked all 13 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- `NCBITaxon:2898210` is retired into `NCBITaxon:54094` at `data/raw/ncbi_merged_ids.tsv:56671`; the exact ignored-file-inclusive merged-ID check found no retained `data/raw/ncbitaxon_taxa.tsv` row for the old identifier.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:38299` is the only aggregate row for `NCBITaxon:54094` and reports organism count `2`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 2 organism rows, 2 project rows, and 1 analysis row.
- Local NCBI type-material evidence had 27 exact `NCBITaxon:54094` rows, all from `typematerial.dmp`, covering ATCC 56629, BCRC 22600, CBS 8070, CCRC 22600, IFO 10117, JCM 9486, and NRRL Y-17847 culture-from-holotype alias spellings.
- Local StrainInfo evidence had 2 direct strain rows and 13 exact deposit rows for `NCBITaxon:54094`; an exact numeric-boundary check found 2 records carrying `"ncbi":54094}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:54094`.

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
