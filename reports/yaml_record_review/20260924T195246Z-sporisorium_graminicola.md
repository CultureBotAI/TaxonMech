# YAML Record Review: Sporisorium graminicola

- Verdict: pass
- Target: `data/taxa/eukaryota/sporisorium_graminicola.yaml`
- Identifier: `NCBITaxon:280036`

## Target

Reviewed the complete 76-line YAML record for Sporisorium graminicola. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sporisorium_graminicola`.

## Validation

- `just validate data/taxa/eukaryota/sporisorium_graminicola.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporobolomyces_salmonicolor.yaml data/taxa/eukaryota/sporobolomyces_sp.yaml data/taxa/eukaryota/sporodiniella_umbellata.yaml data/taxa/eukaryota/sporisorium_graminicola.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:56939` keeps `NCBITaxon:280036` as `Sporisorium graminicola`, rank `SPECIES`, parent `NCBITaxon:63265`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:54954` keeps `NCBITaxon:280036` because `Sporisorium graminicola` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- Checked all 12 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:280036`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:26781` is the only aggregate row for `NCBITaxon:280036` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 1 organism row, 1 project row, and 1 analysis row.
- Local NCBI type-material evidence had 9 exact `NCBITaxon:280036` rows, all from `typematerial.dmp`, covering CBS 10092, JCM 12496, L1-20, and VKM Y-2938 alias spellings.
- Local StrainInfo evidence had 2 direct strain rows and 5 exact deposit rows for `NCBITaxon:280036`; an exact numeric-boundary check found 2 records carrying `"ncbi":280036}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:280036`.

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
