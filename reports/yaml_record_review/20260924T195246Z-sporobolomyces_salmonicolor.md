# YAML Record Review: Sporobolomyces salmonicolor

- Verdict: pass
- Target: `data/taxa/eukaryota/sporobolomyces_salmonicolor.yaml`
- Identifier: `NCBITaxon:5005`

## Target

Reviewed the complete 85-line YAML record for Sporobolomyces salmonicolor. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sporobolomyces_salmonicolor`.

## Validation

- `just validate data/taxa/eukaryota/sporobolomyces_salmonicolor.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporobolomyces_salmonicolor.yaml data/taxa/eukaryota/sporobolomyces_sp.yaml data/taxa/eukaryota/sporodiniella_umbellata.yaml data/taxa/eukaryota/sporisorium_graminicola.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:2181` keeps `NCBITaxon:5005` as `Sporobolomyces salmonicolor`, rank `SPECIES`, parent `NCBITaxon:5429`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:51905` keeps `NCBITaxon:5005` because `Sporobolomyces salmonicolor` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 3 exact synonyms, 3 related synonyms, and 0 broad synonyms.
- Checked all 12 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- No retired NCBI IDs are merged into `NCBITaxon:5005`.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:37305` is the only aggregate row for `NCBITaxon:5005` and reports organism count `2`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 2 organism rows, 2 project rows, and 1 analysis row.
- Local NCBI type-material evidence had 19 exact `NCBITaxon:5005` rows, all from `typematerial.dmp`, including ATCC 36400, CBS 490, IGC 4111, JCM 1841, NCYC 891, NRRL Y-17301, NRRL Y-5483, and VKM Y-685 alias spellings.
- Local StrainInfo evidence had 75 direct strain rows and 137 exact deposit rows for `NCBITaxon:5005`; an exact numeric-boundary check found one additional non-direct strain record, `SI-ID193524` for `Sporobolomyces johnsonii` with one exact `NCBITaxon:5005` deposit.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:5005`.

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
