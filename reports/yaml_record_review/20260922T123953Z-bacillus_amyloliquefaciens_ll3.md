# YAML Record Review: Bacillus amyloliquefaciens LL3

## Target

- Record: `data/taxa/bacteria/bacillus_amyloliquefaciens_ll3.yaml`
- Identifier: `NCBITaxon:1001582`
- Slug: `bacillus_amyloliquefaciens_ll3`
- Rank: `STRAIN`
- Domain: `BACTERIA`
- Parent: `NCBITaxon:1390` (`Bacillus amyloliquefaciens`)

## Validation

- `just validate data/taxa/bacteria/bacillus_amyloliquefaciens_ll3.yaml`: passed.
- `just validate-strict data/taxa/bacteria/acinetobacter_sp_va2s2.yaml data/taxa/bacteria/sphingomonas_sp_a_5.yaml data/taxa/bacteria/bacillus_amyloliquefaciens_ll3.yaml data/taxa/bacteria/levilactobacillus_brevis_kb290.yaml`: passed with 4 files scanned, 0 files with `ERROR`, and 0 total `ERROR` rows.

## Identity and Grounding

The record is an exact, seeded NCBI Taxonomy concept for `NCBITaxon:1001582` / `Bacillus amyloliquefaciens LL3`.

- `identifier` matches the NCBI identifier assigned to this slug in `data/taxa/PATHS.tsv`.
- `label`, rank `STRAIN`, parent `NCBITaxon:1390`, and genetic code `11` match the pinned `data/raw/ncbitaxon_taxa.tsv` row.
- `grounding_status: EXACT` and `mapping_status: SEEDED` are appropriate for the NCBI identity.
- The NCBI lineage places this strain under `Bacillus amyloliquefaciens`.

## Evidence

Three source attestations are backed by local source rows keyed to `NCBITaxon:1001582`:

- `NCBITAXON`: 1 name assertion.
- `GTDB`: `GTDB:s__Bacillus_amyloliquefaciens`, `skos:closeMatch`, 94 genomes.
- `MADIN`: 4 trait assertions.

An exact `rg --no-ignore --hidden` search for `NCBITaxon:1001582` over `curation/seed_scope.tsv`, `data/taxa/PATHS.tsv`, `data/raw`, and `data/straininfo` found the expected `PATHS.tsv`, `seed_scope.tsv`, `ncbitaxon_taxa.tsv`, `gtdb_mappings.tsv`, and `madin_taxa.tsv` rows, and no ATB, BacDive, GOLD, or strain-info rows keyed to the reviewed identifier.

## Completeness

The record includes the expected NCBI synonyms, GTDB cross-reference, `taxonomy_mappings` entry, and three source attestations. `strain_count: 0` is consistent with the absence of child strain rows in the reviewed local source footprint.

## Findings

- Major: the GTDB mapping is species-level but is emitted onto a strain-level NCBI record. `GTDB:s__Bacillus_amyloliquefaciens` and synonym text `Bacillus amyloliquefaciens` both describe the species, while `NCBITaxon:1001582` is the `Bacillus amyloliquefaciens LL3` strain. Treating `Bacillus amyloliquefaciens` as an `EXACT_SYNONYM` of the strain overstates equivalence, and the 94-genome GTDB assertion reads as evidence for the strain rather than for the species cluster.

## Recommended Edits

- Route the `GTDB:s__Bacillus_amyloliquefaciens` mapping and 94-genome count to the species-level target, `NCBITaxon:1390`, or suppress/downgrade the GTDB mapping and synonym when a GTDB species maps to a lower-rank NCBI strain.
- Add a regression check that rejects `EXACT_SYNONYM` emission when the synonym is generated from a GTDB species mapping onto an NCBI `STRAIN`.

## Follow-up Checks

- After the GTDB rank-mismatch handling is changed, re-run seeding and confirm this strain no longer carries a species-level `GTDB:s__Bacillus_amyloliquefaciens` exact synonym or 94-genome species assertion.

## Additional Notes

- The NCBI, GTDB, and MADIN evidence was reviewed from pinned local `data/raw/` snapshots rather than live provider lookups.
- Before this report was written, an exact `find reports/yaml_record_review -maxdepth 1 ...` check over ignored report files found no prior `bacillus_amyloliquefaciens_ll3` review.
