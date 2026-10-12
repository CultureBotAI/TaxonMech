# YAML Record Review: Starmera amethionina

- Verdict: pass
- Target: `data/taxa/eukaryota/starmera_amethionina.yaml`
- Identifier: `NCBITaxon:53643`

## Target

Reviewed the complete 82-line YAML record for Starmera amethionina. The final ignored-file-inclusive preflight of `reports/yaml_record_review` found no existing or parallel report for `starmera_amethionina`.

## Validation

- `just validate data/taxa/eukaryota/starmera_amethionina.yaml` reported `No issues found`.
- `just validate-strict data/taxa/eukaryota/stagonosporopsis_tanaceti.yaml data/taxa/eukaryota/stanjemonium_grisellum.yaml data/taxa/eukaryota/staphylotrichum_longicolle.yaml data/taxa/eukaryota/starmera_amethionina.yaml` scanned all four files and reported 0 files with `ERROR` and 0 total `ERROR` rows.

## Identity and Grounding

- The retained NCBI row at `data/raw/ncbitaxon_taxa.tsv:6784` keeps `NCBITaxon:53643` as `Starmera amethionina`, rank `SPECIES`, parent `NCBITaxon:83173`, genetic code `1`, and `attested_by` `gold` in taxonomy snapshot `2026-09-13`.
- The seed-scope row at `curation/seed_scope.tsv:52880` keeps `NCBITaxon:53643` because `Starmera amethionina` satisfied the attested rule with 2 sources including NCBI.
- The YAML synonym block matches the NCBI retained row: 2 exact synonyms, 2 related synonyms, and 0 broad synonyms.
- Checked all 13 YAML lineage entries against retained NCBI rows; no lineage taxa were missing and no labels or parent identifiers mismatched.
- `NCBITaxon:53682` is retired into `NCBITaxon:53643` at `data/raw/ncbi_merged_ids.tsv:85146`; the exact ignored-file-inclusive merged-ID check found no retained `data/raw/ncbitaxon_taxa.tsv` row for the old identifier.

## Evidence

- The GOLD aggregate row at `data/raw/gold_organisms.tsv:38200` is the only aggregate row for `NCBITaxon:53643` and reports organism count `1`, matching the YAML GOLD assertion.
- Native GOLD evidence for the taxon comprised 1 organism row, 2 project rows, and 2 analysis rows.
- Local NCBI type-material evidence had 20 exact `NCBITaxon:53643` rows, all from `typematerial.dmp`, covering ATCC 36080, BCRC 22202, CBS 6940, CCRC 22202, IFO 10014, JCM 1831, NCYC 1485, NRRL Y-10978, UCD 76-401.2, and UCD 76-401B alias spellings.
- Local StrainInfo evidence had 6 direct strain rows and 20 exact deposit rows for `NCBITaxon:53643`; an exact numeric-boundary check found one additional non-direct strain record, `SI-ID63416` for `Starmera pachycereana` with three exact `NCBITaxon:53643` deposits.
- Local BacDive exact evidence had 0 rows for `NCBITaxon:53643`.

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
