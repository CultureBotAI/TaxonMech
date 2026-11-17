# YAML Record Review: Sporobolomyces sp.

- Verdict: pass
- Target: `data/taxa/eukaryota/sporobolomyces_sp.yaml`
- Identifier: `NCBITaxon:1928706`

## Target

Reviewed the complete 75-line YAML record for Sporobolomyces sp. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sporobolomyces_sp`.

## Validation

- `just validate data/taxa/eukaryota/sporobolomyces_sp.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporobolomyces_salmonicolor.yaml data/taxa/eukaryota/sporobolomyces_sp.yaml data/taxa/eukaryota/sporodiniella_umbellata.yaml data/taxa/eukaryota/sporisorium_graminicola.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:496009` keeps `NCBITaxon:1928706` as `Sporobolomyces sp.`, rank `SPECIES`, parent `NCBITaxon:2688955`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:61639` keeps `NCBITaxon:1928706` because `Sporobolomyces sp.` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 1 exact synonym, 1 related synonym, and 0 broad synonyms.
- Checked all 13 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- `NCBITaxon:1891165` is retired into `NCBITaxon:1928706` at `data/raw/ncbi_merged_ids.tsv:31265`; the exact ignored-file-inclusive merged-ID check found no retained `data/raw/ncbitaxon_taxa.tsv` row for the old identifier.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:17657` is the only aggregate row for `NCBITaxon:1928706` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence currently has 0 organism rows, 0 project rows, and 0 analysis rows for the taxon.
- Local NCBI type-material evidence had 0 exact rows for `NCBITaxon:1928706`.
- Local StrainInfo evidence had 0 direct strain rows and 0 exact deposit rows for `NCBITaxon:1928706`.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:1928706`.

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
