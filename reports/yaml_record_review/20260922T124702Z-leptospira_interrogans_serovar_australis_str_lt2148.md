# YAML Record Review: Leptospira interrogans serovar Australis str. LT2148

## Target

- Record: `data/taxa/bacteria/leptospira_interrogans_serovar_australis_str_lt2148.yaml`
- Identifier: `NCBITaxon:1001594`
- Slug: `leptospira_interrogans_serovar_australis_str_lt2148`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:211882` (`Leptospira interrogans serovar Australis`)

## Validation

- `just validate data/taxa/bacteria/leptospira_interrogans_serovar_australis_str_lt2148.yaml`: passed.
- `just validate-strict data/taxa/bacteria/leptospira_noguchii_str_2006001870.yaml data/taxa/bacteria/leptospira_interrogans_serovar_australis_str_lt2148.yaml data/taxa/bacteria/leptospira_noguchii_serovar_panama_str_cz214.yaml data/taxa/bacteria/leptospira_interrogans_serovar_djasiman_str_lt1649.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The record is an exact, seeded NCBI Taxonomy concept for `NCBITaxon:1001594` / `Leptospira interrogans serovar Australis str. LT2148`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label`, rank `STRAIN`, parent `NCBITaxon:211882`, and genetic code `11` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the NCBI identity.
- The lineage places this strain under `Leptospira interrogans` and the no-rank `Leptospira interrogans serovar Australis`.

## Evidence

Three source attestations are backed by local source rows keyed to `NCBITaxon:1001594`:

- `NCBITAXON`: 1 name assertion.
- `GOLD`: 1 organism assertion.
- `MADIN`: 5 trait assertions.

An exact `rg --no-ignore --hidden` search for `NCBITaxon:1001594` over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected `PATHS.tsv`, `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, `gold_organisms.tsv`, and `madin_taxa.tsv` rows, and no ATB, BacDive, GTDB, or strain-info rows keyed to the reviewed identifier.

## Completeness

The record includes the expected NCBI synonym and three source attestations. The absence of `taxonomy_mappings`, `xrefs`, and GTDB synonyms is consistent with there being no `gtdb_mappings.tsv` row for `NCBITaxon:1001594`; `strain_count: 0` is consistent with the absence of child strain rows in the reviewed local source footprint.

## Findings

No findings.

## Recommended Edits

None.

## Follow-up Checks

None urgent. Re-check only if a future source refresh adds ATB, BacDive, GTDB, or strain-info rows for `NCBITaxon:1001594`.

## Additional Notes

- The NCBI, GOLD, and MADIN evidence was reviewed from pinned local `data/raw/` snapshots rather than live provider lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `leptospira_interrogans_serovar_australis_str_lt2148` review.
