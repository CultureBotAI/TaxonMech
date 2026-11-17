# YAML Record Review: Bipolaris oryzae ATCC 44560

- Verdict: pass
- Target: `data/taxa/eukaryota/bipolaris_oryzae_atcc_44560.yaml`
- Identifier: `NCBITaxon:930090`

## Target

Reviewed the complete 90-line YAML record for Bipolaris oryzae ATCC 44560. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `bipolaris_oryzae_atcc_44560`.

## Validation

- `just validate data/taxa/eukaryota/bipolaris_oryzae_atcc_44560.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/baudoinia_panamericana_uamh_10762.yaml data/taxa/eukaryota/bigelowiella_natans_ccmp2755.yaml data/taxa/eukaryota/bipolaris_maydis_atcc_48331.yaml data/taxa/eukaryota/bipolaris_oryzae_atcc_44560.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:195924` keeps `NCBITaxon:930090` as `Bipolaris oryzae ATCC 44560`, rank `STRAIN`, parent `NCBITaxon:101162`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:56929` keeps `NCBITaxon:930090` because `Bipolaris oryzae ATCC 44560` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 2 exact synonyms, 0 related synonyms, and 0 broad synonyms.
- Checked all 18 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:930090`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:44632` is the only aggregate row for `NCBITaxon:930090` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 2 organism rows, 1 project row, and 2 analysis rows.
- Local NCBI type-material evidence had 0 exact rows for `NCBITaxon:930090`.
- Local StrainInfo evidence had 0 direct strain rows and 0 exact deposit rows for `NCBITaxon:930090`.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:930090`.

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
