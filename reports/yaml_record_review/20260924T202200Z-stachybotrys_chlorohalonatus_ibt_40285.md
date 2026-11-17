# YAML Record Review: Stachybotrys chlorohalonatus IBT 40285

- Verdict: pass
- Target: `data/taxa/eukaryota/stachybotrys_chlorohalonatus_ibt_40285.yaml`
- Identifier: `NCBITaxon:1283841`

## Target

Reviewed the complete 80-line YAML record for Stachybotrys chlorohalonatus IBT 40285. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stachybotrys_chlorohalonatus_ibt_40285`.

## Validation

- `just validate data/taxa/eukaryota/stachybotrys_chlorohalonatus_ibt_40285.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stachybotrys_chlorohalonatus_ibt_40285.yaml data/taxa/eukaryota/stachybotrys_echinatus.yaml data/taxa/eukaryota/stachybotrys_elegans.yaml data/taxa/eukaryota/stagonosporopsis_rhizophila.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:300151` keeps `NCBITaxon:1283841` as `Stachybotrys chlorohalonatus IBT 40285`, rank `STRAIN`, parent `NCBITaxon:388913`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:58912` keeps `NCBITaxon:1283841` because `Stachybotrys chlorohalonatus IBT 40285` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 0 exact synonyms, 0 related synonyms, and 0 broad synonyms.
- Checked all 17 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:1283841`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:6591` is the only aggregate row for `NCBITaxon:1283841` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 1 organism row, 1 project row, and 1 analysis row.
- Local NCBI type-material evidence had 0 exact rows for `NCBITaxon:1283841`.
- Local StrainInfo evidence had 0 direct strain rows and 0 exact deposit rows for `NCBITaxon:1283841`.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:1283841`.

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
