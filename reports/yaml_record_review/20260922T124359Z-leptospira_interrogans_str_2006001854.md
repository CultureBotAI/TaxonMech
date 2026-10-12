# YAML Record Review: Leptospira interrogans str. 2006001854

## Target

- Record: `data/taxa/bacteria/leptospira_interrogans_str_2006001854.yaml`
- Identifier: `NCBITaxon:1001590`
- Slug: `leptospira_interrogans_str_2006001854`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:173` (`Leptospira interrogans`)

## Validation

- `just validate data/taxa/bacteria/leptospira_interrogans_str_2006001854.yaml`: passed.
- `just validate-strict data/taxa/bacteria/leptospira_weilii_str_2006001853.yaml data/taxa/bacteria/leptospira_interrogans_str_2006001854.yaml data/taxa/bacteria/leptospira_interrogans_str_c10069.yaml data/taxa/bacteria/leptospira_santarosai_str_2000027870.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The record is an exact, seeded NCBI Taxonomy concept for `NCBITaxon:1001590` / `Leptospira interrogans str. 2006001854`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label`, rank `STRAIN`, parent `NCBITaxon:173`, and genetic code `11` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the NCBI identity.
- The NCBI lineage places this strain directly under `Leptospira interrogans`.

## Evidence

Four source attestations are backed by local source rows keyed to `NCBITaxon:1001590`:

- `NCBITAXON`: 1 name assertion.
- `GTDB`: `GTDB:s__Leptospira_interrogans`, `skos:closeMatch`, 556 genomes.
- `GOLD`: 1 organism assertion.
- `MADIN`: 5 trait assertions.

An exact `rg --no-ignore --hidden` search for `NCBITaxon:1001590` over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected `PATHS.tsv`, `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, and `madin_taxa.tsv` rows, and no ATB, BacDive, or strain-info rows keyed to the reviewed identifier.

## Completeness

The record includes the expected NCBI synonyms, GTDB cross-reference, `taxonomy_mappings` entry, and four source attestations. `strain_count: 0` is consistent with the absence of child strain rows in the reviewed local source footprint.

## Findings

- Major: the GTDB mapping is species-level but is emitted onto a strain-level NCBI record. `GTDB:s__Leptospira_interrogans` and synonym text `Leptospira interrogans` both describe the species, while `NCBITaxon:1001590` is the `Leptospira interrogans` 2006001854 strain. Treating `Leptospira interrogans` as an `EXACT_SYNONYM` of the strain overstates equivalence, and the 556-genome GTDB assertion reads as evidence for this one strain rather than for the species cluster.

## Recommended Edits

- Route the `GTDB:s__Leptospira_interrogans` mapping and 556-genome count to the species-level target, `NCBITaxon:173`, or suppress/downgrade the GTDB mapping and synonym when a GTDB species maps to a lower-rank NCBI strain.
- Add a regression check that rejects `EXACT_SYNONYM` emission when the synonym is generated from a GTDB species mapping onto an NCBI `STRAIN`.

## Follow-up Checks

- After the GTDB rank-mismatch handling is changed, re-run seeding and confirm this strain no longer carries a species-level `GTDB:s__Leptospira_interrogans` exact synonym or 556-genome species assertion.

## Additional Notes

- The NCBI, GTDB, GOLD, and MADIN evidence was reviewed from pinned local `data/raw/` snapshots rather than live provider lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `leptospira_interrogans_str_2006001854` review.
