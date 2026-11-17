# YAML Record Review: Stachybotrys chartarum

- Verdict: pass
- Target: `data/taxa/eukaryota/stachybotrys_chartarum.yaml`
- Identifier: `NCBITaxon:74722`

## Target

Reviewed the complete 99-line YAML record for Stachybotrys chartarum. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stachybotrys_chartarum`.

## Validation

- `just validate data/taxa/eukaryota/stachybotrys_chartarum.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporothrix_pallida.yaml data/taxa/eukaryota/spraguea_lophii.yaml data/taxa/eukaryota/spumella_elongata.yaml data/taxa/eukaryota/stachybotrys_chartarum.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:10638` keeps `NCBITaxon:74722` as `Stachybotrys chartarum`, rank `SPECIES`, parent `NCBITaxon:74721`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:53269` keeps `NCBITaxon:74722` because `Stachybotrys chartarum` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 4 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- Checked all 16 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- `NCBITaxon:1304189` is retired into `NCBITaxon:74722` at `data/raw/ncbi_merged_ids.tsv:11553`; the exact ignored-file-inclusive merged-ID check found no retained `data/raw/ncbitaxon_taxa.tsv` row for the old identifier.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:42236` is the only aggregate row for `NCBITaxon:74722` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 1 organism row, 1 project row, and 1 analysis row.
- Local NCBI type-material evidence had 4 exact `NCBITaxon:74722` rows, all from `typematerial.dmp`, covering CBS 182.80 culture-from-epitype and DAOM 51026 culture-from-holotype alias spellings.
- Local StrainInfo evidence had 209 direct strain rows and 269 exact deposit rows for `NCBITaxon:74722`; an exact numeric-boundary check found 209 records carrying `"ncbi":74722}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:74722`.

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
