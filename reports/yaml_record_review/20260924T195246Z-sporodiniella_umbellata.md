# YAML Record Review: Sporodiniella umbellata

- Verdict: pass
- Target: `data/taxa/eukaryota/sporodiniella_umbellata.yaml`
- Identifier: `NCBITaxon:101117`

## Target

Reviewed the complete 72-line YAML record for Sporodiniella umbellata. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sporodiniella_umbellata`.

## Validation

- `just validate data/taxa/eukaryota/sporodiniella_umbellata.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporobolomyces_salmonicolor.yaml data/taxa/eukaryota/sporobolomyces_sp.yaml data/taxa/eukaryota/sporodiniella_umbellata.yaml data/taxa/eukaryota/sporisorium_graminicola.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:17433` keeps `NCBITaxon:101117` as `Sporodiniella umbellata`, rank `SPECIES`, parent `NCBITaxon:101116`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:53641` keeps `NCBITaxon:101117` because `Sporodiniella umbellata` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 0 exact synonyms, 1 related synonym, and 0 broad synonyms.
- Checked all 13 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:101117`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:252` is the only aggregate row for `NCBITaxon:101117` and reports organism count `2`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 2 organism rows, 3 project rows, and 1 analysis row.
- Local NCBI type-material evidence had 0 exact rows for `NCBITaxon:101117`.
- Local StrainInfo evidence had 3 direct strain rows and 8 exact deposit rows for `NCBITaxon:101117`; an exact numeric-boundary check found 3 records carrying `"ncbi":101117}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:101117`.

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
