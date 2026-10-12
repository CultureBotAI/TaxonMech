# YAML Record Review: Sporopachydermia cereana

- Verdict: pass
- Target: `data/taxa/eukaryota/sporopachydermia_cereana.yaml`
- Identifier: `NCBITaxon:54093`

## Target

Reviewed the complete 81-line YAML record for Sporopachydermia cereana. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `sporopachydermia_cereana`.

## Validation

- `just validate data/taxa/eukaryota/sporopachydermia_cereana.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/sporisorium_reilianum_f_sp_reilianum.yaml data/taxa/eukaryota/sporisorium_scitamineum.yaml data/taxa/eukaryota/sporopachydermia_cereana.yaml data/taxa/eukaryota/sporopachydermia_lactativora.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:6837` keeps `NCBITaxon:54093` as `Sporopachydermia cereana`, rank `SPECIES`, parent `NCBITaxon:45793`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:52908` keeps `NCBITaxon:54093` because `Sporopachydermia cereana` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 1 exact synonym, 3 related synonyms, and 0 broad synonyms.
- Checked all 13 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- `NCBITaxon:111498` and `NCBITaxon:111499` are retired into `NCBITaxon:54093` at `data/raw/ncbi_merged_ids.tsv:3873` and `data/raw/ncbi_merged_ids.tsv:3876`; exact ignored-file-inclusive merged-ID checks found no retained `data/raw/ncbitaxon_taxa.tsv` rows for either old identifier.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:38298` is the only aggregate row for `NCBITaxon:54093` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 1 organism row, 1 project row, and 0 analysis rows.
- Local NCBI type-material evidence had 26 exact `NCBITaxon:54093` rows, all from `typematerial.dmp`, covering ATCC 26895, ATCC 38532, BCRC 22599, CCRC 22599, DBVPG 6098, IFO 10013, IGC 4163, JCM 9480, NRRL Y-7798, UCD 72-313, and CBS 6644 holotype or culture-from-holotype alias spellings.
- Local StrainInfo evidence had 6 direct strain rows and 27 exact deposit rows for `NCBITaxon:54093`; an exact numeric-boundary check found 6 records carrying `"ncbi":54093}`, matching the direct StrainInfo row count.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:54093`.

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
