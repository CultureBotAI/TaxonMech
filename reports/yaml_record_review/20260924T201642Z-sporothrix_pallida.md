# YAML Record Review: Sporothrix pallida

- Verdict: pass
- Target: `data/taxa/eukaryota/sporothrix_pallida.yaml`
- Identifier: `NCBITaxon:431197`

## Target

Reviewed the complete 87-line YAML record for Sporothrix pallida. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sporothrix_pallida`.

## Validation

- `just validate data/taxa/eukaryota/sporothrix_pallida.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporothrix_pallida.yaml data/taxa/eukaryota/spraguea_lophii.yaml data/taxa/eukaryota/spumella_elongata.yaml data/taxa/eukaryota/stachybotrys_chartarum.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:95121` keeps `NCBITaxon:431197` as `Sporothrix pallida`, rank `SPECIES`, parent `NCBITaxon:29907`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:55629` keeps `NCBITaxon:431197` because `Sporothrix pallida` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- Checked all 16 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:431197`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:35306` is the only aggregate row for `NCBITaxon:431197` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 1 organism row, 1 project row, and 1 analysis row.
- Local NCBI type-material evidence had 4 exact `NCBITaxon:431197` rows, all from `typematerial.dmp`, covering CBS 131.56 culture-from-type-material and MUCL 10062 type-material alias spellings.
- Local StrainInfo evidence had 6 direct strain rows and 12 exact deposit rows for `NCBITaxon:431197`; an exact numeric-boundary check found one additional non-direct strain record, `SI-ID75797` for `Sporothrix albicans` with two exact `NCBITaxon:431197` deposits.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:431197`.

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
