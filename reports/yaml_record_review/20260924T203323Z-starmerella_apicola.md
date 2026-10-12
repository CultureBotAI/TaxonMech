# YAML Record Review: Starmerella apicola

- Verdict: pass
- Target: `data/taxa/eukaryota/starmerella_apicola.yaml`
- Identifier: `NCBITaxon:29830`

## Target

Reviewed the complete 141-line YAML record for Starmerella apicola. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmerella_apicola`.

## Validation

- `just validate data/taxa/eukaryota/starmerella_apicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/starmera_caribaea.yaml data/taxa/eukaryota/starmera_pachycereana.yaml data/taxa/eukaryota/starmera_stellimalicola.yaml data/taxa/eukaryota/starmerella_apicola.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:3271` keeps `NCBITaxon:29830` as `Starmerella apicola`, rank `SPECIES`, parent `NCBITaxon:75735`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:52207` keeps `NCBITaxon:29830` because `Starmerella apicola` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 2 exact synonyms, 22 related synonyms, and 0 broad synonyms.
- Checked all 13 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- Twenty retired NCBI IDs merge into `NCBITaxon:29830`: `NCBITaxon:121234`, `NCBITaxon:228555` through `NCBITaxon:228559`, `NCBITaxon:270619`, `NCBITaxon:554851` through `NCBITaxon:554861`, `NCBITaxon:858105`, and `NCBITaxon:91467`; exact ignored-file-inclusive checks found each only in `data/raw/ncbi_merged_ids.tsv` and found no retained `data/raw/ncbitaxon_taxa.tsv` rows for the old identifiers.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:29832` is the only aggregate row for `NCBITaxon:29830` and reports organism count `2`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 2 organism rows, 2 project rows, and 1 analysis row.
- Local NCBI type-material evidence had 19 exact `NCBITaxon:29830` rows, all from `typematerial.dmp`, covering ATCC 24616, BCRC 22277, CBS 2868, CCRC 22277, IFO 10261, JCM 9592, NRIC 1802, NRRL Y-2481, and VKM Y-1670 culture-from-type-material alias spellings.
- Local StrainInfo evidence had 42 direct strain rows and 83 exact deposit rows for `NCBITaxon:29830`; an exact numeric-boundary check found 42 records carrying `"ncbi":29830}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:29830`.

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
