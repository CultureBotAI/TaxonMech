# YAML Record Review: Stachybotrys echinatus

- Verdict: pass
- Target: `data/taxa/eukaryota/stachybotrys_echinatus.yaml`
- Identifier: `NCBITaxon:80383`

## Target

Reviewed the complete 93-line YAML record for Stachybotrys echinatus. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `stachybotrys_echinatus`.

## Validation

- `just validate data/taxa/eukaryota/stachybotrys_echinatus.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stachybotrys_chlorohalonatus_ibt_40285.yaml data/taxa/eukaryota/stachybotrys_echinatus.yaml data/taxa/eukaryota/stachybotrys_elegans.yaml data/taxa/eukaryota/stagonosporopsis_rhizophila.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:12023` keeps `NCBITaxon:80383` as `Stachybotrys echinatus`, rank `SPECIES`, parent `NCBITaxon:74721`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:53343` keeps `NCBITaxon:80383` because `Stachybotrys echinatus` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 3 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- Checked all 16 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- `NCBITaxon:1195886` is retired into `NCBITaxon:80383` at `data/raw/ncbi_merged_ids.tsv:7221`; the exact ignored-file-inclusive merged-ID check found no retained `data/raw/ncbitaxon_taxa.tsv` row for the old identifier.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:42869` is the only aggregate row for `NCBITaxon:80383` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 1 organism row, 1 project row, and 1 analysis row.
- Local NCBI type-material evidence had 0 exact rows for `NCBITaxon:80383`.
- Local StrainInfo evidence had 50 direct strain rows and 75 exact deposit rows for `NCBITaxon:80383`; an exact numeric-boundary check found 50 records carrying `"ncbi":80383}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:80383`.

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
