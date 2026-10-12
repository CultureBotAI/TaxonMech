# YAML Record Review: Spraguea lophii

- Verdict: pass
- Target: `data/taxa/eukaryota/spraguea_lophii.yaml`
- Identifier: `NCBITaxon:51541`

## Target

Reviewed the complete 69-line YAML record for Spraguea lophii. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `spraguea_lophii`.

## Validation

- `just validate data/taxa/eukaryota/spraguea_lophii.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporothrix_pallida.yaml data/taxa/eukaryota/spraguea_lophii.yaml data/taxa/eukaryota/spumella_elongata.yaml data/taxa/eukaryota/stachybotrys_chartarum.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:6469` keeps `NCBITaxon:51541` as `Spraguea lophii`, rank `SPECIES`, parent `NCBITaxon:51540`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:52830` keeps `NCBITaxon:51541` because `Spraguea lophii` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 1 exact synonym, 2 related synonyms, and 0 broad synonyms.
- Checked all 10 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:51541`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:37585` is the only aggregate row for `NCBITaxon:51541` and reports organism count `4`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 6 organism rows, 6 project rows, and 5 analysis rows.
- Local NCBI type-material evidence had 0 exact rows for `NCBITaxon:51541`.
- Local StrainInfo evidence had 0 direct strain rows and 0 exact deposit rows for `NCBITaxon:51541`.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:51541`.

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
