# YAML Record Review: Sporopachydermia lactativora

- Verdict: pass
- Target: `data/taxa/eukaryota/sporopachydermia_lactativora.yaml`
- Identifier: `NCBITaxon:45794`

## Target

Reviewed the complete 75-line YAML record for Sporopachydermia lactativora. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sporopachydermia_lactativora`.

## Validation

- `just validate data/taxa/eukaryota/sporopachydermia_lactativora.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporisorium_reilianum_f_sp_reilianum.yaml data/taxa/eukaryota/sporisorium_scitamineum.yaml data/taxa/eukaryota/sporopachydermia_cereana.yaml data/taxa/eukaryota/sporopachydermia_lactativora.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:5708` keeps `NCBITaxon:45794` as `Sporopachydermia lactativora`, rank `SPECIES`, parent `NCBITaxon:45793`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:52692` keeps `NCBITaxon:45794` because `Sporopachydermia lactativora` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 1 exact synonym, 1 related synonym, and 0 broad synonyms.
- Checked all 13 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:45794`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:36154` is the only aggregate row for `NCBITaxon:45794` and reports organism count `2`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 2 organism rows, 4 project rows, and 2 analysis rows.
- Local NCBI type-material evidence had 25 exact `NCBITaxon:45794` rows, all from `typematerial.dmp`, covering ATCC 32043, IFO 10565, JCM 9485, MUCL 31273, NRRL Y-11591, and CBS 6192 holotype or culture-from-holotype alias spellings.
- Local StrainInfo evidence had 7 direct strain rows and 49 exact deposit rows for `NCBITaxon:45794`; an exact numeric-boundary check found 7 records carrying `"ncbi":45794}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:45794`.

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
